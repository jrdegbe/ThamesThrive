from ThamesThrive.process_engine.action.v1.end_action import EndAction
from ThamesThrive.domain.profile import Profile
from ThamesThrive.service.plugin.service.plugin_runner import run_plugin


def test_plugin_end():
    init = {}

    payload = {}

    result = run_plugin(EndAction, init, payload, profile=Profile(id="1"))
    assert result.output is None



