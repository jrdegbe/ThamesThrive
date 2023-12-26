from ThamesThrive.domain.destination import Destination
from ThamesThrive.domain.event import Event
from ThamesThrive.domain.profile import Profile
from ThamesThrive.domain.resource import Resource
from ThamesThrive.domain.session import Session


class DestinationInterface:

    def __init__(self, debug: bool, resource: Resource, destination: Destination):
        self.destination = destination
        self.debug = debug
        self.resource = resource

    async def dispatch_profile(self, data, profile: Profile, session: Session):
        pass

    async def dispatch_event(self, data, profile: Profile, session: Session, event: Event):
        pass
