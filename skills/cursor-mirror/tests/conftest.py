# Shared fixtures for cursor-mirror tests.
# Layer 1: test lib against current universal model + current Cursor installation.
# These are integration tests -- they read real Cursor SQLite DBs on this machine.

import sys
from pathlib import Path

import pytest

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT))

from lib.paths import GLOBAL_DB, WORKSPACES_ROOT


@pytest.fixture
def global_db() -> Path:
    """Path to the global Cursor state.vscdb. Skip if not present."""
    if not GLOBAL_DB.exists():
        pytest.skip(f"Global DB not found: {GLOBAL_DB}")
    return GLOBAL_DB


@pytest.fixture
def workspaces_root() -> Path:
    """Path to workspace storage root. Skip if not present."""
    if not WORKSPACES_ROOT.exists():
        pytest.skip(f"Workspaces root not found: {WORKSPACES_ROOT}")
    return WORKSPACES_ROOT


@pytest.fixture
def any_workspace(workspaces_root: Path) -> Path:
    """Return first workspace dir that has a state.vscdb."""
    for ws in workspaces_root.iterdir():
        if ws.is_dir() and (ws / "state.vscdb").exists():
            return ws
    pytest.skip("No workspace with state.vscdb found")


@pytest.fixture
def model_dir() -> Path:
    """Path to the universal model directory."""
    d = SKILL_ROOT / "reference" / "universal" / "model"
    if not d.exists():
        pytest.skip(f"Model dir not found: {d}")
    return d
