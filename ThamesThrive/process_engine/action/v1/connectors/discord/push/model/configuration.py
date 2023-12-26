from typing import Optional


from westgate.domain.named_entity import NamedEntity
from westgate.service.plugin.domain.config import PluginConfig


class DiscordWebHookConfiguration(PluginConfig):
    resource: NamedEntity
    timeout: int = 10
    message: str
    username: Optional[str] = None

