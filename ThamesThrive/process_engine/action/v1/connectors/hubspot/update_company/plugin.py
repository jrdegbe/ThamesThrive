from westgate.service.notation.dict_traverser import DictTraverser
from westgate.service.plugin.domain.register import Plugin, Spec, MetaData, Documentation, PortDoc, Form, FormGroup, \
    FormField, FormComponent
from westgate.service.plugin.domain.result import Result
from westgate.service.plugin.runner import ActionRunner
from .model.config import Config
from westgate.service.storage.driver.elastic import resource as resource_db
from westgate.domain.resource import Resource
from westgate.process_engine.action.v1.connectors.hubspot.client import HubSpotClient, HubSpotClientException

from datetime import datetime


def validate(config: dict) -> Config:
    return Config(**config)


class HubSpotCompanyUpdater(ActionRunner):

    resource: Resource
    config: Config
    client: HubSpotClient

    async def set_up(self, init):
        config = validate(init)
        resource = await resource_db.load(config.source.id)

        self.config = config
        self.resource = resource
        self.client = HubSpotClient(**resource.credentials.get_credentials(self, None))
        self.client.set_retries(self.node.on_connection_error_repeat)

    def parse_mapping(self):
        for key, value in self.config.properties.items():

            if isinstance(value, list):
                if key == "tags":
                    self.config.properties[key] = ",".join(value)

                else:
                    self.config.properties[key] = "|".join(value)

            elif isinstance(value, datetime):
                self.config.properties[key] = str(value)

    async def run(self, payload: dict, in_edge=None) -> Result:

        dot = self._get_dot_accessor(payload)
        traverser = DictTraverser(dot)

        self.config.properties = traverser.reshape(self.config.properties)
        self.parse_mapping()

        try:
            result = await self.client.update_company(
                self.config.company_id,
                self.config.properties
            )
            return Result(port="response", value=result)

        except HubSpotClientException as e:
            return Result(port="error", value={"message": str(e)})


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module=__name__,
            className='HubSpotCompanyUpdater',
            inputs=["payload"],
            outputs=["response", "error"],
            version='0.7.2',
            license="MIT + CC",
            author="Marcin Gaca, Risto Kowaczewski, Ben Ullrich",
            manual="hubspot_add_company_action",
            init={
                "source": {
                    "id": "",
                    "name": ""
                },
                "company_id": None,
                "properties": {},
            },
            form=Form(
                groups=[
                    FormGroup(
                        name="Plugin configuration",
                        fields=[
                            FormField(
                                id="source",
                                name="HubSpot resource",
                                description="Please select your HubSpot resource.",
                                component=FormComponent(type="resource", props={"label": "Resource", "tag": "hubspot"})
                            ),
                            FormField(
                                id="company_id",
                                name="Company id",
                                description="Please write an id of the company you want to update.",
                                component=FormComponent(type="text", props={"label": "Company id"})
                            ),
                            FormField(
                                id="properties",
                                name="Properties fields",
                                description="You can add some more fields to your company. Just type in the alias of "
                                            "the field as key, and a path as a value for this field. This is fully "
                                            "optional.",
                                component=FormComponent(type="keyValueList", props={"label": "Fields"})
                            ),
                        ]
                    )
                ]
            )
        ),
        metadata=MetaData(
            name='Update company',
            brand="Hubspot",
            desc='Updates a company in Hubspot based on provided data.',
            icon='hubspot',
            group=["Hubspot"],
            documentation=Documentation(
                inputs={
                    "payload": PortDoc(desc="This port takes payload object.")
                },
                outputs={
                    "response": PortDoc(desc="This port returns response from HubSpot API."),
                    "error": PortDoc(desc="This port gets triggered if an error occurs.")
                }
            )
        )
    )

