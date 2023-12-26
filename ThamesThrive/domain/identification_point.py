from typing import Optional, List

from pydantic import BaseModel

from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.named_entity import NamedEntity
from ThamesThrive.domain.ref_value import RefValue


class IdentificationField(BaseModel):
    profile_trait: RefValue
    event_property: RefValue


class IdentificationPoint(Entity):
    name: str
    description: Optional[str] = ""
    source: NamedEntity
    event_type: NamedEntity
    fields: List[IdentificationField]
    enabled: bool = False
    settings: Optional[dict] = {"conflict_aux_field": "conflict"}
