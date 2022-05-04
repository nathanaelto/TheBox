import subprocess
import random
import uuid
from typing import List

from src.core.Box import Box
from src.dto.RequestRunDTO import RequestRunDTO
from src.dto.RequestRunStepDTO import RequestRunStepDTO
from src.dto.ResultStepDTO import ResultStepDTO
from src.utils.FilesUtils import decode_base64


async def run_command(command):
    print('command : ' + ' '.join(command))
    process = subprocess.Popen(' '.join(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    process.wait()
    out, err = process.communicate()
    return out.decode('utf-8'), err.decode('utf-8')


async def cleanup_box(box_id):
    command_cleanup = ['isolate', '--cg', '-b', box_id, '--cleanup']
    out, err = await run_command(command_cleanup)
    if len(err) > 0:
        raise Exception('Fail to cleanup Sandbox')
    return out, err


async def exec_step(box, script, meta_data_file):
    command_to_exec = ['isolate', '--cg', '-b', box.box_id, '-M {}/box/{}'.format(box.workdir, meta_data_file)]
    command_to_exec += box.exec_settings
    command_to_exec += ['--run', '--']
    command_to_exec.append('/bin/bash /box/{}'.format(script))
    return await run_command(command_to_exec)


async def add_right_to_exec(file):
    command_to_exec = ['chmod', '+x', file]
    await run_command(command_to_exec)


def IsolateSingleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@IsolateSingleton
class Isolate:
    MIN_BOX_ID = 1
    MAX_BOX_ID = 999

    def __init__(self):
        self.boxes: dict[str, Box] = dict()

    async def init_box(self, request: RequestRunDTO):
        box_id = random.randint(self.MIN_BOX_ID, self.MAX_BOX_ID)
        while str(box_id) in self.boxes.keys():
            box_id = random.randint(self.MIN_BOX_ID, self.MAX_BOX_ID)
        box_id_str = str(box_id)
        command_init = ['isolate', '--cg', '-b', box_id_str, '--init']
        out, err = await run_command(command_init)
        if len(err) > 0:
            print('err : {}'.format(err))
            raise Exception('Fail to create Sandbox')
        work_dir = out.strip()
        box = Box.init_box(box_id=box_id_str, workdir=work_dir)
        if request.settings is None:
            box.default_exec_settings()
        else:
            box.set_exec_settings(request.settings)

        zipped_file_path = box.write_file_in_box('', 'file.zip', decode_base64(request.files), True)
        box.write_files_zipped(zipped_file_path, 'box')

        self.boxes[box_id_str] = box
        print('New box id : {} are up'.format(box_id_str))
        return box_id_str

    async def run_steps(self, box_id, steps: List[RequestRunStepDTO]):
        box = self.boxes[box_id]
        steps_result = []

        for step in steps:
            step_id = uuid.uuid1()
            script_to_exec = box.write_script('box', step.script, step_id)
            await add_right_to_exec('{}/box/{}'.format(box.workdir, script_to_exec))
            meta_data_filename = 'meta-data-{}.txt'.format(step_id)
            out, err = await exec_step(box, script_to_exec, meta_data_filename)
            meta_data_file = '{}/box/{}'.format(box.workdir, meta_data_filename)
            meta_data = {}
            with open(meta_data_file, 'r') as f:
                for line in f:
                    tab_line = line.strip().split(':')
                    meta_data[tab_line[0]] = tab_line[1]
            steps_result.append(
                ResultStepDTO(
                    name=step.name,
                    status=int(meta_data['exitcode']),
                    stdout=out,
                    stderr=err,
                    time=meta_data['time'],
                    time_wall=meta_data['time-wall'],
                    memory_used=int(meta_data['cg-mem'])
                )
            )

        print('Results : {}'.format(steps_result))
        return steps_result

    async def delete_box(self, box_id):
        await cleanup_box(box_id)
        del self.boxes[box_id]
        print('Box id : {} are deleting'.format(box_id))

    def get_box(self, box_id: str):
        if box_id in self.boxes:
            return self.boxes[box_id]
        return None
