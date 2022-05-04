import os
from json import JSONEncoder

from dotenv import load_dotenv

load_dotenv()


def EnvironmentVariablesSingleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@EnvironmentVariablesSingleton
class EnvironmentVariables:
    def __init__(self):
        self.run_time_limit = os.getenv('RUN_TIME_LIMIT')
        self.wall_time_limit = os.getenv('WALL_TIME_LIMIT')
        self.stack_size_limit = os.getenv('STACK_SIZE_LIMIT')
        self.process_count_limit = os.getenv('PROCESS_COUNT_LIMIT')
        self.storage_size_limit = os.getenv('STORAGE_SIZE_LIMIT')
        self.check_valid_env()

    def check_valid_env(self):
        if self.run_time_limit is None:
            raise Exception('Env error : RUN_TIME_LIMIT not found')
        if self.wall_time_limit is None:
            raise Exception('Env error : WALL_TIME_LIMIT not found')
        if self.stack_size_limit is None:
            raise Exception('Env error : STACK_SIZE_LIMIT not found')
        if self.process_count_limit is None:
            raise Exception('Env error : PROCESS_COUNT_LIMIT not found')
        if self.storage_size_limit is None:
            raise Exception('Env error : STORAGE_SIZE_LIMIT not found')


    def get_run_time_limit(self):
        return self.run_time_limit

    def get_wall_time_limit(self):
        return self.wall_time_limit

    def get_stack_size_limit(self):
        return self.stack_size_limit

    def get_process_count_limit(self):
        return self.process_count_limit

    def get_storage_size_limit(self):
        return self.storage_size_limit


class EnvironmentVariablesEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
