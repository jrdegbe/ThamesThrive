import logging
from typing import List

from deepdiff import DeepDiff
from ThamesThrive.service.cache_manager import CacheManager

from ThamesThrive.config import ThamesThrive
from ThamesThrive.domain.console import Console
from ThamesThrive.domain.event import Event
from ThamesThrive.domain.profile import Profile
from ThamesThrive.domain.session import Session
from ThamesThrive.exceptions.exception_service import get_traceback
from ThamesThrive.exceptions.log_handler import log_handler
from ThamesThrive.service.console_log import ConsoleLog
from ThamesThrive.service.destinations.dispatchers import profile_destination_dispatch
from ThamesThrive.service.utils.getters import get_entity_id

logger = logging.getLogger(__name__)
logger.setLevel(ThamesThrive.logging_level)
logger.addHandler(log_handler)
cache = CacheManager()


class DestinationOrchestrator:

    def __init__(self, profile: Profile, session: Session, events: List[Event], console_log: ConsoleLog):
        self.console_log = console_log
        self.events = events
        self.session = session
        self.profile = profile

    async def sync_destination(self, has_profile, profile_copy):
        if has_profile and profile_copy is not None:
            new_profile = self.profile.model_dump(exclude={"operation": ...})

            if profile_copy != new_profile:
                profile_delta = DeepDiff(profile_copy, new_profile, ignore_order=True)
                if profile_delta:
                    logger.debug("Profile changed. Destination scheduled to run.")
                    try:
                        load_destination_task = cache.profile_destinations
                        await profile_destination_dispatch(load_destination_task,
                                                           profile=self.profile,
                                                           session=self.session,
                                                           debug=False)
                    except Exception as e:
                        # todo - this appends error to the same profile - it rather should be en event error
                        self.console_log.append(Console(
                            flow_id=None,
                            node_id=None,
                            event_id=None,
                            profile_id=get_entity_id(self.profile),
                            origin='destination',
                            class_name=DestinationOrchestrator.__name__,
                            module=__name__,
                            type='error',
                            message=str(e),
                            traceback=get_traceback(e)
                        ))
                        logger.error(str(e))
