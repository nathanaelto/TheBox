from src.dto.RequestRunSettingsDTO import RequestRunSettingsDTO
from src.utils.EnvironmentVariable import EnvironmentVariables
from src.utils.FilesUtils import write_file, unzip_files


class Box:
    def __init__(self, box_id, workdir, out_fn, err_fn):
        self.box_id = box_id
        self.workdir = workdir
        self.out_fn = out_fn
        self.err_fn = err_fn
        self.exec_settings = None

    @staticmethod
    def init_box(box_id, workdir):
        return Box(box_id=box_id, workdir=workdir, out_fn=None, err_fn=None)

    def default_exec_settings(self):
        env = EnvironmentVariables()

        self.exec_settings = [
            "-s",
            "-t {}".format(env.get_run_time_limit()),
            "-w {}".format(env.get_wall_time_limit()),
            "-k {}".format(env.get_stack_size_limit()),
            "-p{}".format(env.get_process_count_limit()),
            "-f {}".format(env.get_storage_size_limit()),
            "--cg-mem={}".format(env.get_memory_limit()),
            "-e"
        ]

    def set_exec_settings(self, request_settings: RequestRunSettingsDTO = None):
        env = EnvironmentVariables()
        settings = request_settings

        run_time_limit = settings.run_time_limit if settings.run_time_limit is not None else env.get_run_time_limit()
        wall_time_limit = settings.wall_time_limit if settings.wall_time_limit is not None else env.get_wall_time_limit()
        stack_size_limit = settings.stack_size_limit if settings.stack_size_limit is not None else env.get_stack_size_limit()
        process_count_limit = settings.process_count_limit if settings.process_count_limit is not None else env.get_process_count_limit()
        storage_size_limit = settings.storage_size_limit if settings.storage_size_limit is not None else env.get_storage_size_limit()
        memory_limit = settings.memory_limit if settings.memory_limit is not None else env.get_memory_limit()

        self.exec_settings = [
            "-s",
            "-t {}".format(run_time_limit),
            "-w {}".format(wall_time_limit),
            "-k {}".format(stack_size_limit),
            "-p{}".format(process_count_limit),
            "-f {}".format(storage_size_limit),
            "--cg-mem={}".format(memory_limit),
            "-e"
        ]

    def write_file_in_box(self, directory, filename, data, is_binary_file=False):
        path = '{}/{}'.format(self.workdir, directory).replace('//', '/')
        file_write = write_file(data, path, filename, is_binary_file)
        return file_write

    def write_script(self, directory, data, uuid_id):
        filename = 'script-{}.sh'.format(uuid_id)
        # self.write_file_in_box(directory, filename, decode_base64(data))
        self.write_file_in_box(directory, filename, data)
        return filename

    def write_files_zipped(self, file_to_unzip, directory):
        path = '{}/{}'.format(self.workdir, directory).replace('//', '/')
        unzip_files(file_to_unzip, path)
