-- id: count_bubbles
-- usage: Per-composer bubble counts from global cursorDiskKV
-- sources: BORG

SELECT key, (SELECT COUNT(*) FROM cursorDiskKV k2 WHERE k2.key LIKE 'bubbleId:' || replace(k.key, 'composerData:', '') || ':%') as cnt
FROM cursorDiskKV k WHERE key LIKE 'composerData:%';
