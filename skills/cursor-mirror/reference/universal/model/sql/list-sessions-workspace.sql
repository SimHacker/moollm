-- id: list_sessions_workspace
-- usage: Workspace state.vscdb. Returns single row; parse JSON allComposers[].{composerId, name, createdAt, lastUpdatedAt}
-- sources: BORG, S2THEND

SELECT value FROM ItemTable WHERE key = 'composer.composerData';
