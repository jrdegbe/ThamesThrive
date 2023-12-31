from typing import Optional
from pydantic import BaseModel
from ThamesThrive.domain.value_object.save_result import SaveResult


class TrackerPayloadResult(BaseModel):
    session: Optional[SaveResult] = None
    events: SaveResult
    profile: Optional[SaveResult] = None
