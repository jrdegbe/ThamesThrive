from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime
from ThamesThrive.domain.session import Session, SessionMetadata
from ThamesThrive.domain.event import Event, EventSession
from ThamesThrive.process_engine.action.v1.traits.hash_traits_action import HashTraitsAction
from ThamesThrive.service.plugin.service.plugin_runner import run_plugin
from ThamesThrive.domain.flow import Flow
from hashlib import md5
import json


def test_plugin_hash_traits():
    payload = {}
    event = Event(
        id='1',
        type='text',
        metadata=EventMetadata(time=EventTime(), profile_less=True),
        session=EventSession(id='1'),
        source=Entity(id='1'),
        properties={"prop1": 5}
    )
    session = Session(
        id='1',
        metadata=SessionMetadata()
    )
    result = run_plugin(
        HashTraitsAction,
        {
            "traits": ["flow@id", "profile@traits.public.something", "event@properties.prop1"],
            "func": "md5"
        },
        payload=payload,
        event=event,
        session=session,
        profile=None,
        flow=Flow(id="1", name="flow1", lock=False, type="collection")
    )
    assert result.profile is None
    assert result.flow.id == "1"
    assert result.event.properties["prop1"] == md5(json.dumps(5).encode("utf-8")).hexdigest()



