from uuid import uuid4

from ThamesThrive.context import Context
from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event import Event
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime
from ThamesThrive.service.failover.failover_manager import FailOverManager


def closure_true(context, data, options):
    return True

def closure_false(context, data, options):
    return False

def test_fail_over():
    fail_over = FailOverManager('test')
    events = [Event(
        id=str(uuid4()),
        name="test",
        type="test",
        metadata=EventMetadata(time=EventTime()),
        source=Entity(id="1")
    ).model_dump() for _ in range(0, 10)]
    context = Context(production=True)


    fail_over.add(context, events, options={})

    fail_over.flush(closure_false)
    assert not fail_over.is_empty()
    fail_over.flush(closure_true)
    assert fail_over.is_empty()
