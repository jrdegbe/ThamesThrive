from pydantic import BaseModel
from westgate.domain.named_entity import NamedEntity
from typing import Dict, Optional
from westgate.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    source: NamedEntity
    organization: str
    bucket: str
    filters: Dict
    aggregation: Optional[str] = None
    start: str
    stop: str


class InfluxCredentials(BaseModel):
    url: str
    token: str
