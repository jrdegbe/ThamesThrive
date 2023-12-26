from typing import Optional, List

from ThamesThrive.domain.event import Event
from ThamesThrive.domain.profile import Profile
from ThamesThrive.domain.session import Session
from ThamesThrive.service.plugin.domain.console import Log
from ThamesThrive.service.wf.domain.debug_info import DebugInfo
from ThamesThrive.service.wf.domain.flow_graph import FlowGraph


class FlowInvokeResult:

    def __init__(self, debug_info: DebugInfo, log_list: List[Log], flow: FlowGraph, event: Event,
                 profile: Optional[Profile] = None,
                 session: Optional[Session] = None):
        self.debug_info = debug_info
        self.log_list: List[Log] = log_list
        self.event = event
        self.profile = profile
        self.session = session
        self.flow = flow

    def __repr__(self):
        return f"FlowInvokeResult(\n\tprofile=({self.profile})\n\tsession=({self.session})\n\tevent=({self.event}))"
