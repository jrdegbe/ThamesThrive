from pydantic import field_validator

from westgate.domain.named_entity import NamedEntity
from westgate.service.plugin.domain.config import PluginConfig


class Configuration(PluginConfig):
    source: NamedEntity
    tweet: str

    @field_validator('tweet')
    @classmethod
    def check_given_tweet(cls, value):
        if not value:
            raise ValueError("Please fill tweet field with content which you want to send.")
        return value
