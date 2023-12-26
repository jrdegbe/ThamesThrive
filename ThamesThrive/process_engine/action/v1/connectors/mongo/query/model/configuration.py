from pydantic import BaseModel

from westgate.service.plugin.domain.config import PluginConfig
from westgate.domain.named_entity import NamedEntity
from westgate.domain.resource_id import ResourceId


class MongoConfiguration(BaseModel):
    uri: str
    timeout: int = 5000


class PluginConfiguration(PluginConfig):
    source: NamedEntity
    database: NamedEntity
    collection: NamedEntity
    query: str = "{}"


class DatabaseConfig(BaseModel):
    source: ResourceId
    database: NamedEntity


