from westgate.domain.named_entity import NamedEntity
from westgate.domain.resources.token import Token
from westgate.service.plugin.domain.config import PluginConfig
from westgate.service.plugin.plugin_endpoint import PluginEndpoint
from westgate.process_engine.action.v1.connectors.mailchimp.service.mailchimp_audience_editor import MailChimpAudienceEditor
from westgate.service.storage.driver.elastic import resource as resource_db


class AudienceConfig(PluginConfig):
    source: NamedEntity

class Endpoint(PluginEndpoint):

    @staticmethod
    async def get_audiences(config: dict):
        config = AudienceConfig(**config)
        if config.source.is_empty():
            raise ValueError("Resource not set.")

        resource = await resource_db.load(config.source.id)
        creds = Token(**resource.credentials.production)
        client = MailChimpAudienceEditor(
            creds.token,
            2
        )
        result = await client.get_all_audience_ids()

        return {
            "total": len(result),
            "result": result
        }


