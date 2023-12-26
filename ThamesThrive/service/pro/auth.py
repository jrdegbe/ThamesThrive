import logging
import os

from ThamesThrive.config import ThamesThrive
from ThamesThrive.exceptions.log_handler import log_handler
from ThamesThrive.service.storage.driver.elastic import pro as pro_db

_local_path = os.path.dirname(__file__)
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.setLevel(ThamesThrive.logging_level)
logger.addHandler(log_handler)


async def get_tpro_token():
    """
    Return None if not configured otherwise returns token.
    """
    try:
        # todo add cache
        result = await pro_db.read_pro_service_endpoint()
    except Exception as e:
        logger.error(f"Exception when reading pro service user data: {str(e)}")
        result = None

    if result is None:
        return None

    return result.token
