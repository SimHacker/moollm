# Layer 1: SQL queries load from .sql files.

from pathlib import Path


def test_queries_are_strings():
    from lib.sql import (
        LIST_SESSIONS_WORKSPACE, FULL_SESSION, LIST_COMPOSERS_GLOBAL,
        COUNT_BUBBLES, COMPOSER_STATE, AGENT_KV_FOR_COMPOSER,
        TABLE_CHECK_CURSOR_DISK_KV, SEARCH_KEYS_PREFIX, LIST_ITEMTABLE_KEYS,
    )
    for name, q in [
        ("LIST_SESSIONS_WORKSPACE", LIST_SESSIONS_WORKSPACE),
        ("FULL_SESSION", FULL_SESSION),
        ("LIST_COMPOSERS_GLOBAL", LIST_COMPOSERS_GLOBAL),
        ("COUNT_BUBBLES", COUNT_BUBBLES),
        ("COMPOSER_STATE", COMPOSER_STATE),
        ("AGENT_KV_FOR_COMPOSER", AGENT_KV_FOR_COMPOSER),
        ("TABLE_CHECK_CURSOR_DISK_KV", TABLE_CHECK_CURSOR_DISK_KV),
        ("SEARCH_KEYS_PREFIX", SEARCH_KEYS_PREFIX),
        ("LIST_ITEMTABLE_KEYS", LIST_ITEMTABLE_KEYS),
    ]:
        assert isinstance(q, str), f"{name} is not a string"
        assert len(q) > 10, f"{name} is too short"


def test_sql_files_exist(model_dir: Path):
    sql_dir = model_dir / "sql"
    assert sql_dir.exists()
    sql_files = list(sql_dir.glob("*.sql"))
    assert len(sql_files) >= 5, f"Expected >= 5 .sql files, got {len(sql_files)}"


def test_queries_loaded_from_files(model_dir: Path):
    """If .sql files exist, the loaded queries should start with a SQL comment (our convention)."""
    from lib.sql import LIST_SESSIONS_WORKSPACE
    sql_file = model_dir / "sql" / "list-sessions-workspace.sql"
    if sql_file.exists():
        assert LIST_SESSIONS_WORKSPACE.startswith("--"), \
            "Expected query loaded from .sql file to start with SQL comment"
