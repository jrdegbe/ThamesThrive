from pydantic import field_validator, BaseModel
from westgate.domain.named_entity import NamedEntity
from typing import Optional
from westgate.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    source: NamedEntity
    text: str
    lang: Optional[str] = "auto"

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if value is None or len(value) == 0:
            raise ValueError("This field cannot be empty.")
        return value


class Token(BaseModel):
    token: str
