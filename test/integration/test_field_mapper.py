from ThamesThrive.context import ServerContext, Context
from ThamesThrive.domain.event_metadata import EventMetadata

from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event import Event
from ThamesThrive.domain.time import EventTime
from ThamesThrive.service.field_mappings_cache import FieldMapper


def test_field_mapper():
    with ServerContext(Context(production=False)):
        fm = FieldMapper()
        fm.batch = 1
        is_added = fm.add_field_mappings('event',
                                         [
                                             Event(id="1", name="ev1", type="ev1", properties={"a": 1}, source=Entity(id="1"),
                                                   metadata=EventMetadata(time=EventTime())),
                                             Event(id="2", name="ev2", type="ev2", properties={"b": 1}, source=Entity(id="1"),
                                                   metadata=EventMetadata(time=EventTime())),
                                             Event(id="3", name="ev3", type="ev3", properties={"c": 1}, source=Entity(id="1"),
                                                   metadata=EventMetadata(time=EventTime())),
                                         ])
        data = fm.get_field_mapping('event')
        fm.save_cache()
        assert 'properties.a' in data
        assert 'properties.b' in data
        assert 'properties.c' in data
