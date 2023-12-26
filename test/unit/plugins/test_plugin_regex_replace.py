from ThamesThrive.service.plugin.service.plugin_runner import run_plugin
from ThamesThrive.process_engine.action.v1.strings.regex_replace.plugin import RegexReplacer
from ThamesThrive.domain.profile import Profile
from ThamesThrive.domain.event import Event, EventSession
from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime


def test_should_work():
    init = {
        "string": "payload@text",
        "replace_with": "REPLACED",
        "find_regex": "[a-z]{5}"
    }
    payload = {
        "text": "Lorem ipsum dolor sit amet"
    }

    event = Event(
        id='1',
        type='text',
        metadata=EventMetadata(time=EventTime()),
        session=EventSession(id='1'),
        source=Entity(id='1')
    )

    result = run_plugin(RegexReplacer, init, payload, profile=Profile(id="1"), event=event)

    assert result.output.value == {"value": "Lorem REPLACED REPLACED sit amet"}
