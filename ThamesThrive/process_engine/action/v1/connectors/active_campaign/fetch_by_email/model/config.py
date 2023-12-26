from westgate.service.plugin.domain.config import PluginConfig
from westgate.domain.named_entity import NamedEntity


class Config(PluginConfig):
    source: NamedEntity
    email: str
