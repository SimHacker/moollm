-- id: agent_kv_for_composer
-- usage: Tool results for a composer; ORDER BY rowid
-- sources: BORG

SELECT key, value FROM cursorDiskKV WHERE key LIKE 'agentKv:' || :composer_id || ':%' ORDER BY rowid;
