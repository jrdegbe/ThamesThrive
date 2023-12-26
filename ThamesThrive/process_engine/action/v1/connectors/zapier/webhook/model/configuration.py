from westgate.service.plugin.domain.config import PluginConfig


class Configuration(PluginConfig):
    url: str  # AnyHttpUrl
    body: str = "{}"
    timeout: int = 10
