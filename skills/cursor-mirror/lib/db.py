# Database access for Cursor SQLite (read-only).
# Align with reference/universal/model/tables.yml

import json
import sqlite3
from pathlib import Path
from typing import Any

from .debug_util import debug
from .sources import register_source
from .paths import GLOBAL_DB
from .keys import COMPOSER_STATE_KEY


def open_db(path: Path) -> sqlite3.Connection:
    """Open SQLite in read-only mode."""
    debug("open_db: %s", path.name if hasattr(path, "name") else path)
    register_source("database", str(path))
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def decode_blob(raw: bytes | str) -> str:
    """Decode blob to UTF-8 string."""
    b = raw if isinstance(raw, (bytes, bytearray)) else str(raw).encode()
    return b.decode("utf-8", errors="replace")


def get_item_table_value(key: str, db_path: Path | None = None) -> Any | None:
    """Get a value from global ItemTable, parsing JSON if applicable."""
    path = db_path or GLOBAL_DB
    conn = open_db(path)
    cur = conn.cursor()
    register_source("database", str(path), "ItemTable")
    register_source("sql", f"SELECT value FROM ItemTable WHERE key = '{key}'")
    row = cur.execute("SELECT value FROM ItemTable WHERE key = ?", (key,)).fetchone()
    conn.close()
    if not row:
        return None
    try:
        return json.loads(row[0])
    except (json.JSONDecodeError, TypeError):
        return row[0]


def get_reactive_storage(db_path: Path | None = None) -> dict[str, Any]:
    """Get the reactive storage blob (composerState, AI settings, etc.)."""
    return get_item_table_value(COMPOSER_STATE_KEY, db_path) or {}
