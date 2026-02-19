# Layer 1: database access works against real Cursor DBs.

from pathlib import Path


def test_open_db_readonly(global_db: Path):
    from lib.db import open_db
    conn = open_db(global_db)
    cur = conn.cursor()
    tables = [row[0] for row in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]
    conn.close()
    assert "ItemTable" in tables


def test_cursor_disk_kv_exists(global_db: Path):
    from lib.db import open_db
    conn = open_db(global_db)
    cur = conn.cursor()
    tables = [row[0] for row in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]
    conn.close()
    assert "cursorDiskKV" in tables


def test_decode_blob_str():
    from lib.db import decode_blob
    assert decode_blob(b"hello") == "hello"
    assert decode_blob("hello") == "hello"


def test_decode_blob_utf8():
    from lib.db import decode_blob
    assert decode_blob("test".encode("utf-8")) == "test"


def test_get_item_table_value(global_db: Path):
    from lib.db import get_item_table_value
    from lib.keys import COMPOSER_STATE_KEY
    value = get_item_table_value(COMPOSER_STATE_KEY)
    assert value is not None, "composerState key should exist in global DB"
    assert isinstance(value, dict), "composerState should parse as dict"
