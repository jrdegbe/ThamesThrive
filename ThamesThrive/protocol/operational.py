from typing import Protocol, runtime_checkable

from ThamesThrive.domain.value_object.operation import RecordFlag


@runtime_checkable
class Operational(Protocol):
    operation: RecordFlag
