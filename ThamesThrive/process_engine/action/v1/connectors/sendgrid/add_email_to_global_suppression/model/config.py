from pydantic import BaseModel

from westgate.domain.named_entity import NamedEntity
from westgate.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    source: NamedEntity
    email: str


class Token(BaseModel):
    token: str
