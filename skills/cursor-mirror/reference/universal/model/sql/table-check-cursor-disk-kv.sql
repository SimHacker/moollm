-- id: table_check_cursor_disk_kv
-- usage: Check if global DB has cursorDiskKV (required for bubble/composerData read)
-- sources: BORG, S2THEND

SELECT name FROM sqlite_master WHERE type='table' AND name='cursorDiskKV';
