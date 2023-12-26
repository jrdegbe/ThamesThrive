import pytest
from pydantic import ValidationError

from ThamesThrive.context import Context, ServerContext
from ThamesThrive.domain.session import FrozenSession, Session


def test_frozen_session():
    with ServerContext(Context(production=True)):
        session = FrozenSession(**Session.new().model_dump())
        assert session.operation.new is True
        with pytest.raises(ValidationError):
            session.id = "1"
