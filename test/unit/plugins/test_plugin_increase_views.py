from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event import Event, EventSession
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime
from ThamesThrive.process_engine.action.v1.increase_views_action import IncreaseViewsAction
from ThamesThrive.domain.profile import Profile
from ThamesThrive.service.plugin.service.plugin_runner import run_plugin


def test_plugin_increase_views():
    init = {}

    payload = {}
    event = Event(
        id='1',
        type='text',
        metadata=EventMetadata(time=EventTime()),
        session=EventSession(id='1'),
        source=Entity(id='1')
    )
    result = run_plugin(IncreaseViewsAction, init, payload, profile=Profile(id="1"), event=event)
    result = run_plugin(IncreaseViewsAction, init, payload, profile=result.profile, event=event)
    assert result.profile.stats.views == 2



