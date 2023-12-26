from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event import Event, EventSession
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime
from ThamesThrive.process_engine.action.v1.converters.base64.encode.plugin import Base64EncodeAction
from ThamesThrive.service.plugin.service.plugin_runner import run_plugin


def test_encodes_payload_text_to_base64():
    init = {
        'source': 'payload@text',
        'source_encoding': 'utf-8',
    }
    payload = {
        'text': 'hello tracardi',
    }
    result = run_plugin(Base64EncodeAction, init, payload)

    assert result.output.port == 'payload'
    assert result.output.value == {'base64': 'aGVsbG8gdHJhY2FyZGk='}


def test_encodes_default_to_base64():
    init = {
        'source': 'event@id',
        'source_encoding': 'utf-8',
    }
    payload = {}
    event = Event(
        id='1',
        type='text',
        metadata=EventMetadata(time=EventTime()),
        session=EventSession(id='1'),
        source=Entity(id='1')
    )

    result = run_plugin(Base64EncodeAction, init, payload, event=event)

    assert result.output.port == 'payload'
    assert result.output.value == {'base64': 'MQ=='}


def test_uses_source_encoding():
    init = {
        'source': 'payload@text',
        'source_encoding': 'utf-32-be',
    }
    payload = {
        'text': 'hi',
    }
    result = run_plugin(Base64EncodeAction, init, payload)

    assert result.output.port == 'payload'
    assert result.output.value == {'base64': 'AAAAaAAAAGk='}
