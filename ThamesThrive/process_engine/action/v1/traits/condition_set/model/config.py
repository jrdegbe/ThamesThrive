from typing import Dict
from ThamesThrive.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    conditions: Dict[str, str]
