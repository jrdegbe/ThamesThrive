from typing import List, Optional

from pydantic import BaseModel

from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.named_entity import NamedEntity
from ThamesThrive.domain.ref_value import RefValue


class ConsentFieldComplianceSetting(BaseModel):
    action: str  # Remove, Hash, Do nothing
    field: RefValue
    consents: List[NamedEntity]

    def get_consents(self) -> set:
        return {item.id for item in self.consents}

    def complies_to_consents(self, profile_consents: set) -> bool:
        required_consents = self.get_consents()
        return required_consents.intersection(profile_consents) == required_consents


class ConsentFieldCompliance(Entity):
    name: str
    description: Optional[str] = ""
    event_type: NamedEntity
    settings: List[ConsentFieldComplianceSetting]  # Flattened ES field
    enabled: Optional[bool] = False
