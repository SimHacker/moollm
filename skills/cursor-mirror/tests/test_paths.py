# Layer 1: paths resolve correctly on this platform; model loads.

import sys
from pathlib import Path


def test_paths_are_pathlib():
    from lib.paths import GLOBAL_DB, WORKSPACES_ROOT, BASE_DIR
    assert isinstance(GLOBAL_DB, Path)
    assert isinstance(WORKSPACES_ROOT, Path)
    assert isinstance(BASE_DIR, Path)


def test_global_db_exists(global_db: Path):
    assert global_db.exists()
    assert global_db.suffix == ".vscdb"


def test_workspaces_root_exists(workspaces_root: Path):
    assert workspaces_root.exists()
    assert workspaces_root.is_dir()


def test_platform_detected():
    from lib.paths import _platform_key
    assert _platform_key in ("darwin", "win32", "linux")
    if sys.platform == "darwin":
        assert _platform_key == "darwin"


def test_model_paths_loaded():
    from lib.paths import _model
    assert isinstance(_model, dict)
    assert "darwin" in _model
    assert "global_db" in _model["darwin"]


def test_backup_and_history_paths():
    from lib.paths import GLOBAL_DB_BACKUP, HISTORY_FOLDER
    assert isinstance(GLOBAL_DB_BACKUP, Path)
    assert isinstance(HISTORY_FOLDER, Path)
    assert "state.vscdb.backup" in str(GLOBAL_DB_BACKUP)
