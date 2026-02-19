# Composer access: session list, metadata, bubble counts.
# Align with reference/universal/model/keys/workspace-itemtable.yml, entities/composer-meta.yml

import json
from pathlib import Path
from typing import Any

from .db import open_db, decode_blob
from .debug_util import debug
from .discovery import iter_workspace_paths, get_workspace_folder
from .keys import SESSION_LIST_KEYS
from .paths import GLOBAL_DB
from .sources import register_source


_composers_cache: dict[str, list[dict[str, Any]]] = {}


def get_workspace_composers(ws_path: Path) -> list[dict[str, Any]]:
    """Get composers from workspace state.vscdb. Cached per CLI run."""
    cache_key = str(ws_path)
    if cache_key in _composers_cache:
        debug("get_workspace_composers: cache hit for %s", ws_path.name[:8])
        return _composers_cache[cache_key]

    debug("get_workspace_composers: loading from %s", ws_path.name[:8])
    db_path = ws_path / "state.vscdb"
    if not db_path.exists():
        _composers_cache[cache_key] = []
        return []

    conn = open_db(db_path)
    cur = conn.cursor()
    register_source("database", str(db_path), "ItemTable")

    row = None
    for key in SESSION_LIST_KEYS:
        register_source("sql", f"SELECT value FROM ItemTable WHERE key='{key}'")
        row = cur.execute("SELECT value FROM ItemTable WHERE key=?", (key,)).fetchone()
        if row:
            break
    conn.close()

    if not row:
        _composers_cache[cache_key] = []
        return []

    data = json.loads(decode_blob(row[0]))
    composers = data.get("allComposers", [])
    if isinstance(composers, dict):
        composers = list(composers.values())
    elif not isinstance(composers, list):
        composers = []

    _composers_cache[cache_key] = composers
    debug("get_workspace_composers: cached %d composers for %s", len(composers), ws_path.name[:8])
    return composers


_bubble_counts_cache: dict[str, int] | None = None


def get_bubble_counts() -> dict[str, int]:
    """Get message counts per composer from global DB. Cached per CLI run."""
    global _bubble_counts_cache
    if _bubble_counts_cache is not None:
        debug("get_bubble_counts: returning cached (%d composers)", len(_bubble_counts_cache))
        return _bubble_counts_cache

    debug("get_bubble_counts: loading from DB...")
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    rows = cur.execute("SELECT key FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'").fetchall()
    conn.close()

    counts: dict[str, int] = {}
    for (k,) in rows:
        parts = k.split(":")
        if len(parts) >= 2:
            counts[parts[1]] = counts.get(parts[1], 0) + 1

    _bubble_counts_cache = counts
    debug("get_bubble_counts: cached %d composers, %d total bubbles",
          len(counts), sum(counts.values()))
    return counts


_all_composers_cache: dict[str, dict[str, Any]] | None = None


def get_all_composers() -> dict[str, dict[str, Any]]:
    """Get all composers from all workspaces with metadata. Cached per CLI run."""
    global _all_composers_cache
    if _all_composers_cache is not None:
        debug("get_all_composers: returning cached (%d composers)", len(_all_composers_cache))
        return _all_composers_cache

    debug("get_all_composers: loading from all workspaces...")
    bubble_counts = get_bubble_counts()
    composers_meta: dict[str, dict[str, Any]] = {}

    for ws in iter_workspace_paths():
        folder = get_workspace_folder(ws)
        for c in get_workspace_composers(ws):
            cid = c.get("composerId")
            if cid:
                composers_meta[cid] = c.copy()
                composers_meta[cid]["_workspace"] = ws.name
                composers_meta[cid]["_workspace_folder"] = folder
                composers_meta[cid]["_bubble_count"] = bubble_counts.get(cid, 0)

    _all_composers_cache = composers_meta
    debug("get_all_composers: cached %d composers", len(composers_meta))
    return composers_meta


def clear_caches() -> None:
    """Clear all module-level caches."""
    global _bubble_counts_cache, _all_composers_cache
    _bubble_counts_cache = None
    _all_composers_cache = None
    _composers_cache.clear()
