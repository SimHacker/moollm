-- id: full_session
-- usage: Global state.vscdb. Bubbles: ORDER BY rowid = message order. Then composer metadata.
-- sources: BORG, S2THEND

-- Bubbles (order by rowid = message order)
SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:' || :composer_id || ':%' ORDER BY rowid ASC;
-- Composer metadata
SELECT value FROM cursorDiskKV WHERE key = 'composerData:' || :composer_id;
