import json

from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event import Event
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime
from ThamesThrive.process_engine.action.v1.inject_action import InjectAction
from ThamesThrive.domain.profile import Profile
from ThamesThrive.service.plugin.service.plugin_runner import run_plugin


def test_plugin_inject():
    init = {"value": json.dumps({"data": 1})}

    payload = {}

    result = run_plugin(InjectAction, init, payload, profile=Profile(id="1"),
                        event=Event(
                            id="0",
                            metadata=EventMetadata(time=EventTime(), debug=False),
                            type="type",
                            source=Entity(id="0"),
                        )
                    )
    assert result.output.value == {"data": 1}
    assert result.output.port == 'payload'



