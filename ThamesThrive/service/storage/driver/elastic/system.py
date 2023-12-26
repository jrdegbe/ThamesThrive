from typing import Tuple

from ThamesThrive.context import ServerContext, get_context
from ThamesThrive.service.storage.indices_manager import get_indices_status


def get_missing(indices, type) -> list:
    return [idx[1] for idx in indices if idx[0] == type]


async def is_schema_ok() -> Tuple[bool, list]:

    # Missing indices in staging
    with ServerContext(get_context().switch_context(production=False)):
        _indices_staging = [item async for item in get_indices_status()]

    # Missing indices in production
    with ServerContext(get_context().switch_context(production=True)):
        _indices_production = [item async for item in get_indices_status()]

    _indices = _indices_staging + _indices_production

    missing_indices = get_missing(_indices, type='missing_index')
    missing_aliases = get_missing(_indices, type='missing_alias')
    missing_templates = get_missing(_indices, type='missing_template')

    is_schema_ok = not missing_indices and not missing_aliases and not missing_templates

    return is_schema_ok, _indices
