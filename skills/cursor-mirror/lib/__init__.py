# cursor-mirror lib: reusable library for Cursor IDE introspection.
# Package: skills/cursor-mirror/lib/ (relative imports; not pip-installable yet)
# Reference: designs/CURSOR-MIRROR-PY-REFACTORING-PLAN.md

from .exceptions import (
    CursorMirrorError,
    NotFoundError,
    DatabaseError,
    ValidationError,
)
from .paths import GLOBAL_DB, WORKSPACES_ROOT
from .db import open_db, decode_blob, get_item_table_value
from .resolve import resolve_workspace, resolve_composer, resolve_composer_id
from .composers import (
    get_workspace_folder,
    get_workspace_composers,
    get_all_composers,
    get_bubble_counts,
)
from .bubbles import load_bubbles, iter_bubbles, get_bubble_text, has_content
from .format_util import format_ts
from .debug_util import set_debug

__all__ = [
    "CursorMirrorError",
    "NotFoundError",
    "DatabaseError",
    "ValidationError",
    "GLOBAL_DB",
    "WORKSPACES_ROOT",
    "resolve_workspace",
    "resolve_composer",
    "resolve_composer_id",
    "get_workspace_folder",
    "get_workspace_composers",
    "get_all_composers",
    "get_bubble_counts",
    "load_bubbles",
    "iter_bubbles",
    "get_bubble_text",
    "has_content",
    "open_db",
    "get_item_table_value",
    "decode_blob",
    "format_ts",
    "set_debug",
]
