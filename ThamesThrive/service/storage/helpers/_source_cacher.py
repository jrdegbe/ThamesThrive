import logging
from ThamesThrive.config import memory_cache, ThamesThrive
from ThamesThrive.domain.event_source import EventSource
from ThamesThrive.exceptions.log_handler import log_handler
from ThamesThrive.service.cache_manager import CacheManager

logger = logging.getLogger(__name__)
logger.setLevel(ThamesThrive.logging_level)
logger.addHandler(log_handler)
cache = CacheManager()


async def validate_source(source_id: str, allowed_bridges: list) -> EventSource:
    source = await cache.event_source(event_source_id=source_id, ttl=memory_cache.source_ttl)

    if source is None:
        raise ValueError(f"Invalid event source `{source_id}`")

    if not source.enabled:
        raise ValueError("Event source disabled.")

    if not source.is_allowed(allowed_bridges):
        raise ValueError(f"Event source `{source_id}` is not within allowed bridge types {allowed_bridges}.")

    return source
