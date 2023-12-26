from ThamesThrive.service.plugin.domain.register import Plugin, Spec, MetaData
from ThamesThrive.service.plugin.domain.result import Result
from ThamesThrive.service.plugin.runner import ActionRunner


class PayloadPlugin(ActionRunner):

    async def run(self, payload: dict, in_edge=None) -> Result:
        return Result(port="payload", value=payload)


def register() -> Plugin:
    return Plugin(
        spec=Spec(
            module=__name__,
            className='PayloadPlugin',
            inputs=[],
            outputs=["payload"]
        ),
        metadata=MetaData(
            name='Start',
            desc='Loads payload into flow.',
            type='flowNode',
            width=100,
            height=100,
            icon='payload'
        )
    )
