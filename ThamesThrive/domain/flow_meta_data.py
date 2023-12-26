from typing import List, Optional

from ThamesThrive.domain.named_entity import NamedEntity


class FlowMetaData(NamedEntity):
    description: str
    projects: Optional[List[str]] = ["General"]
    type: str = 'collection'
