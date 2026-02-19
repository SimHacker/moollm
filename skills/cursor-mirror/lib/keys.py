# Key constants and patterns for Cursor SQLite tables.
# Driven by reference/universal/model/keys/*.yml
# Python reads model; model is the source of truth.

from pathlib import Path
from typing import Any

import yaml

type KeyList = list[str]

_MODEL_DIR = Path(__file__).resolve().parent.parent / "reference" / "universal" / "model"

def _load_yaml(name: str) -> dict[str, Any]:
    path = _MODEL_DIR / name
    if path.exists():
        return yaml.safe_load(path.read_text()) or {}
    return {}


# Workspace ItemTable keys (from keys/workspace-itemtable.yml)
_ws = _load_yaml("keys/workspace-itemtable.yml")

SESSION_LIST_KEYS: KeyList = _ws.get("session_list_priority", {}).get("keys", [
    "composer.composerData",
    "workbench.panel.aichat.view.aichat.chatdata",
    "workbench.panel.chat.view.chat.chatdata",
])

PROMPTS_KEY: str = _ws.get("prompts", "aiService.prompts")
GENERATIONS_KEY: str = _ws.get("generations", "aiService.generations")


# Global ItemTable keys (from keys/global-itemtable.yml)
_gi = _load_yaml("keys/global-itemtable.yml")

COMPOSER_STATE_KEY: str = _gi.get("composer_state_key",
    "src.vs.platform.reactivestorage.browser.reactiveStorageServiceImpl"
    ".persistentStorage.applicationUser")

NOTABLE_GLOBAL_KEYS: KeyList = _gi.get("notable", [
    "cursorai/featureStatusCache",
    "cursorPendingMemories",
    "mcpService.knownServerIds",
])


# cursorDiskKV patterns (from keys/cursor-disk-kv.yml)
_kv = _load_yaml("keys/cursor-disk-kv.yml")
_entries = _kv.get("entries", {})

BUBBLE_PREFIX: str = _entries.get("bubbleId", {}).get("pattern", "bubbleId:{composerId}:{index}").split(":")[0]
AGENT_KV_PREFIX: str = "agentKv"
COMPOSER_DATA_PREFIX: str = "composerData"
CHECKPOINT_PREFIX: str = "checkpointId"
