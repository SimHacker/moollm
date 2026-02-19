-- id: composer_state
-- usage: Global ItemTable; read composerState (YOLO, modes, defaultMode)
-- sources: BORG, TARQ

SELECT json_extract(value, '$.composerState.useYoloMode') as useYoloMode,
       json_extract(value, '$.composerState.yoloCommandAllowlist') as allowlist,
       json_extract(value, '$.composerState.defaultMode2') as defaultMode
FROM ItemTable
WHERE key = 'src.vs.platform.reactivestorage.browser.reactiveStorageServiceImpl.persistentStorage.applicationUser';
