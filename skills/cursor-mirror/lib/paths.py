# Platform paths for Cursor storage.
# Driven by reference/universal/model/paths.yml
# Currently validated on macOS only. Linux and Windows paths are from the
# universal model and community sources but have NOT been tested.

import sys
import warnings
from pathlib import Path
from typing import Any

import yaml

_MODEL_DIR = Path(__file__).resolve().parent.parent / "reference" / "universal" / "model"


def _load_paths_from_model() -> dict[str, Any]:
    path = _MODEL_DIR / "paths.yml"
    if path.exists():
        return yaml.safe_load(path.read_text()) or {}
    return {}


_model = _load_paths_from_model()

# Platform detection and path resolution
_platform_key: str
match sys.platform:
    case "darwin":
        _platform_key = "darwin"
    case "win32":
        _platform_key = "win32"
        warnings.warn(
            "cursor-mirror: Windows paths loaded from model but NOT tested. "
            "Please report issues at github.com/SimHacker/moollm",
            stacklevel=2,
        )
    case s if s.startswith("linux"):
        _platform_key = "linux"
        warnings.warn(
            "cursor-mirror: Linux paths loaded from model but NOT tested. "
            "Please report issues at github.com/SimHacker/moollm",
            stacklevel=2,
        )
    case _:
        _platform_key = "darwin"
        warnings.warn(
            f"cursor-mirror: Unknown platform {sys.platform!r}, falling back to macOS paths. "
            "Please report issues at github.com/SimHacker/moollm",
            stacklevel=2,
        )

_platform = _model.get(_platform_key, {})

def _resolve_base(raw: str) -> Path:
    """Expand ~ and %APPDATA% in base path from model."""
    if raw.startswith("~"):
        return Path(raw).expanduser()
    if raw.startswith("%APPDATA%"):
        import os
        appdata = os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))
        return Path(raw.replace("%APPDATA%", appdata))
    return Path(raw)

# Defaults (macOS) in case model is missing
_DEFAULT_BASE = Path.home() / "Library" / "Application Support" / "Cursor" / "User"
_DEFAULT_GLOBAL_DB = "globalStorage/state.vscdb"
_DEFAULT_WORKSPACE_STORAGE = "workspaceStorage"

_base = _resolve_base(_platform.get("base", str(_DEFAULT_BASE)))
_global_db_rel = _platform.get("global_db", _DEFAULT_GLOBAL_DB)
_ws_storage_rel = _platform.get("workspace_storage", _DEFAULT_WORKSPACE_STORAGE)

GLOBAL_DB: Path = _base / _global_db_rel
WORKSPACES_ROOT: Path = _base / _ws_storage_rel
BASE_DIR: Path = _base

# Workspace DB pattern (from model: "workspaceStorage/{id}/state.vscdb")
WORKSPACE_DB_PATTERN: str = _model.get("workspace_db", "workspaceStorage/{id}/state.vscdb")

# Recovery/backup paths (from model, macOS only for now)
_recovery = _model.get("recovery_backup_paths", {})
GLOBAL_DB_BACKUP: Path = _base / _recovery.get("global_backup", "globalStorage/state.vscdb.backup")
HISTORY_FOLDER: Path = _base / _recovery.get("history_folder", "History/")

# cursor-agent CLI paths (separate from IDE -- not validated)
_agent = _model.get("cursor_agent", {})
CURSOR_AGENT_DB_PATTERN: str = _agent.get("path_pattern", "~/.cursor/chats/<user_hash>/<chat_id>/store.db")
