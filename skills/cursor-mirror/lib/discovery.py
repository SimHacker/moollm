# Workspace discovery: iterate workspaces, read workspace.json, map folder URIs.
# Align with reference/universal/model/discovery.yml, paths.yml

import json
from collections.abc import Iterator
from pathlib import Path
from urllib.parse import unquote

from .paths import WORKSPACES_ROOT
from .sources import register_source
from .debug_util import debug


def iter_workspace_paths(root: Path | None = None) -> Iterator[Path]:
    """Iterate over all workspace directories."""
    base = root or WORKSPACES_ROOT
    register_source("directory", str(base))
    if not base.exists():
        return
    for ws in base.iterdir():
        if ws.is_dir():
            yield ws


def get_workspace_folder(ws_path: Path) -> str | None:
    """Get folder path from workspace.json."""
    ws_json = ws_path / "workspace.json"
    if ws_json.exists():
        try:
            data = json.loads(ws_json.read_text())
            folder = data.get("folder", "")
            return folder_uri_to_path(folder) if folder else None
        except (json.JSONDecodeError, OSError):
            return None
    return None


def folder_uri_to_path(uri: str) -> str:
    """Convert file:// URI to filesystem path."""
    if uri.startswith("file://"):
        return unquote(uri[7:])
    return uri


def project_name_from_uri(uri: str) -> str:
    """Extract project name from folder URI."""
    path = folder_uri_to_path(uri)
    return path.rstrip("/").rsplit("/", maxsplit=1)[-1]
