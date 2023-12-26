from pydantic import BaseModel
from westgate.service.plugin.domain.config import PluginConfig
from westgate.domain.named_entity import NamedEntity
from typing import Dict, Any
from westgate.domain.entity import Entity


class Config(PluginConfig):
    source: NamedEntity
    fields: Dict[str, Any]


class EndpointConfig(BaseModel):
    source: Entity
