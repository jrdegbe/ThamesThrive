from pydantic import BaseModel

from ThamesThrive.domain.resource_id import ResourceId


class ResourceConfig(BaseModel):
    source: ResourceId

