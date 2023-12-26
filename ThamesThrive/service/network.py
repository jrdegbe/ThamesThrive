import logging
import socket
from typing import Optional

from ThamesThrive.config import ThamesThrive

logger = logging.getLogger(__name__)
logger.setLevel(ThamesThrive.logging_level)


def get_local_ip() -> Optional[str]:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError as e:
        logger.error(str(e))
        return None


local_ip = get_local_ip()
