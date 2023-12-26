from typing import List, Union, Set

from ThamesThrive.domain.event import Event
from ThamesThrive.domain.value_object.bulk_insert_result import BulkInsertResult
from ThamesThrive.service.storage.driver.elastic import event as event_db


async def save_events(events: Union[List[Event], Set[Event]]) -> BulkInsertResult:
    return await event_db.save(events, exclude={"operation": ...})
