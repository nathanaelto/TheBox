from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ResultStepDTO:
    name: str
    status: int
    stdout: str
    stderr: str
    time: str
    time_wall: str
    memory_used: int
