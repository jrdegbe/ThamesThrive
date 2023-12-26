from westgate.domain.named_entity import NamedEntity
from westgate.service.plugin.domain.config import PluginConfig


class Configuration(PluginConfig):
    source: NamedEntity
    spreadsheet_id: str
    sheet_name: str
    range: str
    read: bool
    write: bool
    values: str
