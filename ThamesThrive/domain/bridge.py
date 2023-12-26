from typing import Optional

from ThamesThrive.domain.named_entity import NamedEntity
from ThamesThrive.service.plugin.domain.register import Form


class Bridge(NamedEntity):
    description: Optional[str] = ""
    type: str
    config: Optional[dict] = {}
    form: Optional[Form] = None
    manual: Optional[str] = None
