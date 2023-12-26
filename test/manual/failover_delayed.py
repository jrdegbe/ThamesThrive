from datetime import timedelta

import asyncio
import logging

from time import sleep

from com_ThamesThrive.service.tracking.queue.pulsar_queue import QueueWithFailOverPublisher
from com_ThamesThrive.service.tracking.queue.pulsar_topics import EVENT_TOPIC, EVENT_FO
from ThamesThrive.config import tracardi
from ThamesThrive.context import Context
from ThamesThrive.domain.entity import Entity
from tracardi.domain.event import Event
from ThamesThrive.domain.event_metadata import EventMetadata
from ThamesThrive.domain.time import EventTime
from ThamesThrive.exceptions.log_handler import log_handler

logger = logging.getLogger(__name__)
logger.setLevel(tracardi.logging_level)
logger.addHandler(log_handler)


async def main():
    context = Context(production=True)
    manager = QueueWithFailOverPublisher.instance(EVENT_TOPIC, EVENT_FO, send_timeout_millis=1000)

    message = ("workflow", {
        "payload": {},
        "profile": {},
        "session": {},
        "events": {}
    })

    manager.send(message, context, options=dict(
        deliver_after = timedelta(seconds=15)
    ))


asyncio.run(main())
