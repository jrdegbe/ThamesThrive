from ThamesThrive.domain.entity import Entity
from ThamesThrive.domain.event_metadata import EventPayloadMetadata
from ThamesThrive.domain.payload.event_payload import EventPayload
from ThamesThrive.domain.payload.tracker_payload import TrackerPayload
from ThamesThrive.domain.time import Time


def test_should_return_the_same_fp_for_similar_payloads():
    tp1 = TrackerPayload(
        source=Entity(id="1"),
        session=None,
        metadata=EventPayloadMetadata(time=Time()),
        profile=Entity(id="2"),
        context={},
        request={},
        properties={},
        events=[EventPayload(type=event_type, properties=properties) for event_type, properties in
                [('event-type1', {}), ('event-type2', {})]],
        options={"saveSession": False}
    )

    tp2 = TrackerPayload(
        source=Entity(id="1"),
        session=None,
        metadata=EventPayloadMetadata(time=Time()),
        profile=Entity(id="2"),
        context={},
        request={},
        properties={},
        events=[EventPayload(type=event_type, properties=properties) for event_type, properties in
                [('event-type4', {}), ('event-type5', {})]],
        options={"saveSession": False}
    )

    assert tp1.get_finger_print() == tp2.get_finger_print()
