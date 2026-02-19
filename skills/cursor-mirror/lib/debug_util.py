# Debug logging. Set via set_debug(True) from CLI.

import logging
import sys
from typing import Any

log = logging.getLogger("cursor_mirror")
log.setLevel(logging.WARNING)

DEBUG = False

def debug(msg: str, *args: Any) -> None:
    """Log debug message if DEBUG is enabled."""
    if DEBUG:
        log.debug(msg, *args)

def set_debug(enabled: bool) -> None:
    """Enable or disable debug logging."""
    global DEBUG
    DEBUG = enabled
    if enabled:
        log.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter(
            '%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
            datefmt='%H:%M:%S'
        ))
        log.addHandler(handler)
