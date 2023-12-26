from typing import List, Dict
from westgate.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    consent_ids: List[Dict]
    require_all: bool


