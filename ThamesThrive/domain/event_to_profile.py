from typing import List
from typing import Optional

from pydantic import BaseModel
from ThamesThrive.domain.ref_value import RefValue

from ThamesThrive.domain.named_entity import NamedEntity


class EventToProfileMap(BaseModel):
    event: RefValue
    op: int
    profile: RefValue

    def is_empty(self) -> bool:
        return not self.event.has_value() or not self.profile.has_value()


class EventToProfile(NamedEntity):
    event_type: NamedEntity
    description: Optional[str] = "No description provided"
    enabled: Optional[bool] = False
    config: Optional[dict] = {}
    event_to_profile: Optional[List[EventToProfileMap]] = []
    tags: List[str] = []

    def items(self):
        for item in self.event_to_profile:
            yield item.event.value, item.profile.value, item.op
