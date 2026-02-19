# Named SQL queries for Cursor SQLite.
# Loaded from reference/universal/model/sql/*.sql when available; fallback to inline.

from pathlib import Path

_SQL_DIR = Path(__file__).resolve().parent.parent / "reference" / "universal" / "model" / "sql"

def _load_sql(name: str, fallback: str) -> str:
    path = _SQL_DIR / name
    if path.exists():
        return path.read_text().strip()
    return fallback


LIST_SESSIONS_WORKSPACE = _load_sql("list-sessions-workspace.sql",
    "SELECT value FROM ItemTable WHERE key = 'composer.composerData';")

FULL_SESSION = _load_sql("full-session.sql",
    "SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:' || :composer_id || ':%' ORDER BY rowid ASC;\n"
    "SELECT value FROM cursorDiskKV WHERE key = 'composerData:' || :composer_id;")

LIST_COMPOSERS_GLOBAL = _load_sql("list-composers-global.sql",
    "SELECT key, value FROM cursorDiskKV WHERE key LIKE 'composerData:%';")

COUNT_BUBBLES = _load_sql("count-bubbles.sql",
    "SELECT key FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'")

COMPOSER_STATE = _load_sql("composer-state.sql",
    "SELECT json_extract(value, '$.composerState.useYoloMode') as useYoloMode "
    "FROM ItemTable WHERE key = 'src.vs.platform.reactivestorage.browser"
    ".reactiveStorageServiceImpl.persistentStorage.applicationUser';")

AGENT_KV_FOR_COMPOSER = _load_sql("agent-kv-for-composer.sql",
    "SELECT key, value FROM cursorDiskKV WHERE key LIKE 'agentKv:' || :composer_id || ':%' ORDER BY rowid;")

TABLE_CHECK_CURSOR_DISK_KV = _load_sql("table-check-cursor-disk-kv.sql",
    "SELECT name FROM sqlite_master WHERE type='table' AND name='cursorDiskKV';")

SEARCH_KEYS_PREFIX = _load_sql("search-keys-prefix.sql",
    "SELECT key FROM cursorDiskKV WHERE key LIKE :prefix ORDER BY rowid LIMIT :limit;")

LIST_ITEMTABLE_KEYS = _load_sql("list-itemtable-keys.sql",
    "SELECT key FROM ItemTable ORDER BY key;")
