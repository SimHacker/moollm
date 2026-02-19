-- id: search_keys_prefix
-- usage: cursorDiskKV; prefix e.g. 'bubbleId:uuid-here:%' or 'composerData:%'
-- sources: BORG

SELECT key FROM cursorDiskKV WHERE key LIKE :prefix ORDER BY rowid LIMIT :limit;
