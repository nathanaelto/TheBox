from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from src.dto.RequestRunSettingsDTO import RequestRunSettingsDTO
from src.dto.RequestRunStepDTO import RequestRunStepDTO


@dataclass_json
@dataclass
class RequestRunDTO:
    request_id: str
    steps: List[RequestRunStepDTO]
    settings: RequestRunSettingsDTO
    files: str

