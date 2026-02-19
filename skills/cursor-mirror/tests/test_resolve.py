# Layer 1: resolution works against real Cursor data.

from pathlib import Path


def test_resolve_workspace_by_index(workspaces_root: Path):
    from lib.resolve import resolve_workspace
    ws = resolve_workspace("@1")
    assert ws is not None, "@1 should resolve to something"
    assert ws.is_dir()


def test_resolve_workspace_by_hash(workspaces_root: Path):
    from lib.resolve import resolve_workspace
    ws1 = resolve_workspace("@1")
    if ws1 is None:
        return
    prefix = ws1.name[:8]
    ws2 = resolve_workspace(prefix)
    assert ws2 is not None
    assert ws2.name == ws1.name


def test_resolve_workspace_missing():
    from lib.resolve import resolve_workspace
    assert resolve_workspace("zzzznotaworkspacezzz") is None


def test_resolve_composer_by_index(global_db: Path):
    from lib.resolve import resolve_composer
    result = resolve_composer("@1")
    assert result is not None, "@1 should resolve to a composer"
    cid, meta = result
    assert isinstance(cid, str)
    assert len(cid) > 8
    assert isinstance(meta, dict)


def test_resolve_composer_missing():
    from lib.resolve import resolve_composer
    assert resolve_composer("zzzznotacomposerzzz") is None


def test_resolve_composer_id(global_db: Path):
    from lib.resolve import resolve_composer_id
    cid = resolve_composer_id("@1")
    assert cid is not None
    assert isinstance(cid, str)
