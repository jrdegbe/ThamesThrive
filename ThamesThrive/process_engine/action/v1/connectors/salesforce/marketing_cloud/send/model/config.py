from westgate.domain.named_entity import NamedEntity
from typing import Dict, Any
from westgate.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    source: NamedEntity
    extension_id: str
    update: bool
    mapping: Dict[str, Any]
