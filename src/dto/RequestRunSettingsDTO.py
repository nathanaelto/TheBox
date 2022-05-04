from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RequestRunSettingsDTO:
    run_time_limit: str = None
    wall_time_limit: str = None
    stack_size_limit: str = None
    process_count_limit: str = None
    storage_size_limit: str = None
