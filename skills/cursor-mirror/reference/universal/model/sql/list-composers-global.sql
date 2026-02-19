-- id: list_composers_global
-- usage: Global cursorDiskKV; key format composerData:{uuid}; value has name, title, createdAt, updatedAt, workspaceUri
-- sources: BORG

SELECT key, value FROM cursorDiskKV WHERE key LIKE 'composerData:%';
