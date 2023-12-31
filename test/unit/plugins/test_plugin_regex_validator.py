from ThamesThrive.service.plugin.service.plugin_runner import run_plugin

from ThamesThrive.process_engine.action.v1.strings.regex_validator.plugin import RegexValidatorAction


def test_regex_validator_plugin():
    payload = {'data': "12:32"}
    init = {'validation_regex': r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9](:?)([0-5]?[0-9]?)$',
            'data': "payload@data"}

    result = run_plugin(RegexValidatorAction, init, payload)

    assert result.output.port == 'valid'
    assert result.output.value == payload

