# Platform paths for Cursor storage. Align with reference/universal/model/paths.yml

from pathlib import Path

# macOS default; extend for win32/linux via paths.yml when model-driven loading is added
GLOBAL_DB = Path.home() / "Library/Application Support/Cursor/User/globalStorage/state.vscdb"
WORKSPACES_ROOT = Path.home() / "Library/Application Support/Cursor/User/workspaceStorage"
