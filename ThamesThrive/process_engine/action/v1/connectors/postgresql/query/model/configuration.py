from westgate.domain.named_entity import NamedEntity
from westgate.service.plugin.domain.config import PluginConfig


class Configuration(PluginConfig):
    source: NamedEntity
    query: str
    timeout: int = 20
