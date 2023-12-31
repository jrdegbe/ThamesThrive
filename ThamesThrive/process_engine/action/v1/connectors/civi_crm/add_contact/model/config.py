from westgate.domain.named_entity import NamedEntity
from typing import Dict, Any
from westgate.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    source: NamedEntity
    contact_type: str
    fields: Dict[str, Any]
