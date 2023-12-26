from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime
from ThamesThrive.domain.session import Session, SessionMetadata
from ThamesThrive.domain.event import Event, EventSession
from ThamesThrive.domain.profile import Profile
from ThamesThrive.process_engine.action.v1.traits.append_trait_action import AppendTraitAction
from ThamesThrive.service.plugin.service.plugin_runner import run_plugin


def test_plugin_append_trait():
    payload = {}
    profile = Profile(id="1")
    event = Event(
        id='1',
        type='text',
        metadata=EventMetadata(time=EventTime()),
        session=EventSession(id='1'),
        source=Entity(id='1')
    )
    session = Session(
        id='1',
        metadata=SessionMetadata()
    )

    result = run_plugin(AppendTraitAction, {
        "append": {
            "profile@traits.public.value": 1
        }
    }, payload, profile=profile, event=event, session=session)
    assert result.profile.traits['public']['value'] == 1

    result = run_plugin(AppendTraitAction, {
        "append": {
            "profile@traits.public.value": 2
        }
    }, payload, profile=profile, event=event, session=session)
    assert result.profile.traits['public']['value'] == [1, 2]

    result = run_plugin(AppendTraitAction, {
        "remove": {
            "profile@traits.public.value": 2
        }
    }, payload, profile=profile, event=event, session=session)
    assert result.profile.traits['public']['value'] == [1]

    result = run_plugin(AppendTraitAction, {
        "append": {
            "profile@traits.public.value": 3
        }
    }, payload, profile=profile, event=event, session=session)
    assert result.profile.traits['public']['value'] == [1, 3]

    result = run_plugin(AppendTraitAction, {
        "remove": {
            "profile@traits.public.value": [1, 3]
        }
    }, payload, profile=profile, event=event, session=session)
    assert result.profile.traits['public']['value'] == []

    result = run_plugin(AppendTraitAction, {
        "append": {
            "profile@traits.public.objects": [{"A": 1}]
        }
    }, payload, profile=profile, event=event, session=session)
    assert result.profile.traits['public']['objects'] == [{"A": 1}]

    result = run_plugin(AppendTraitAction, {
        "remove": {
            "profile@traits.public.objects": [{"A": 1}]
        }
    }, payload, profile=profile, event=event, session=session)
    assert result.profile.traits['public']['objects'] == []


def test_plugin_append_trait_fail():
    payload = {}
    profile = Profile(id="1")
    event = Event(
        id='1',
        type='text',
        metadata=EventMetadata(time=EventTime()),
        session=EventSession(id='1'),
        source=Entity(id='1')
    )
    session = Session(
        id='1', metadata=SessionMetadata()
    )

    try:
        run_plugin(AppendTraitAction, {
            "remove": {
                "profile@id": 1
            }
        }, payload, profile=profile, event=event, session=session)
        assert False
    except ValueError as e:
        assert str(e) == 'Can not remove from non-list data.'

