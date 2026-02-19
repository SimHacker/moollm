# Reference resolution: workspace and composer lookups by @index, hash prefix, name.
# Uses discovery, composers, bubble counts.

from pathlib import Path
from typing import Any

from .composers import get_all_composers, get_bubble_counts, get_workspace_composers
from .debug_util import debug
from .discovery import get_workspace_folder, iter_workspace_paths


def resolve_workspace(ref: str) -> Path | None:
    """Resolve workspace reference to full path.

    Accepts:
      @1, @2, @3  -> index by recency (most recent first)
      hex prefix  -> hash prefix match (4+ chars)
      name        -> folder name fragment search
    """
    workspaces = sorted(
        iter_workspace_paths(),
        key=lambda ws: (ws / "state.vscdb").stat().st_mtime if (ws / "state.vscdb").exists() else 0,
        reverse=True,
    )

    if ref.startswith("@"):
        idx = int(ref[1:]) - 1
        if 0 <= idx < len(workspaces):
            debug("resolve_workspace: index @%d -> %s", idx + 1, workspaces[idx].name[:8])
            return workspaces[idx]
        debug("resolve_workspace: index @%d out of range", idx + 1)
        return None

    ref_lower = ref.lower()

    for ws in workspaces:
        if ws.name.startswith(ref_lower):
            debug("resolve_workspace: hash prefix match -> %s", ws.name[:8])
            return ws

    for ws in workspaces:
        folder = get_workspace_folder(ws) or ""
        if ref_lower in folder.lower():
            debug("resolve_workspace: name match -> %s (%s)", ws.name[:8], folder)
            return ws

    debug("resolve_workspace: no match for %s", ref)
    return None


def resolve_composer(
    ref: str,
    workspace_ref: str | None = None,
) -> tuple[str, dict[str, Any]] | None:
    """Resolve composer reference to (composer_id, metadata).

    Accepts:
      @1, @2  -> index by bubble count (most messages first)
      hex     -> UUID prefix match
      name    -> name fragment search
    """
    composers_meta = get_all_composers()

    if workspace_ref:
        ws = resolve_workspace(workspace_ref)
        if ws:
            ws_composers = get_workspace_composers(ws)
            ws_ids = {c.get("composerId") for c in ws_composers}
            composers_meta = {k: v for k, v in composers_meta.items() if k in ws_ids}

    sorted_composers = sorted(
        composers_meta.items(),
        key=lambda item: item[1].get("_bubble_count", 0),
        reverse=True,
    )

    if ref.startswith("@"):
        idx = int(ref[1:]) - 1
        if 0 <= idx < len(sorted_composers):
            cid, meta = sorted_composers[idx]
            debug("resolve_composer: index @%d -> %s", idx + 1, cid[:8])
            return cid, meta
        debug("resolve_composer: index @%d out of range", idx + 1)
        return None

    for cid, meta in composers_meta.items():
        if cid.startswith(ref):
            debug("resolve_composer: UUID prefix match -> %s", cid[:8])
            return cid, meta

    ref_lower = ref.lower()
    matches: list[tuple[str, dict[str, Any]]] = []
    for cid, meta in composers_meta.items():
        name = meta.get("name", "") or ""
        if ref_lower in name.lower():
            matches.append((cid, meta))

    if len(matches) == 1:
        debug("resolve_composer: single name match -> %s", matches[0][0][:8])
        return matches[0]
    elif len(matches) > 1:
        matches.sort(key=lambda x: x[1].get("_bubble_count", 0), reverse=True)
        debug("resolve_composer: %d name matches, using highest count -> %s", len(matches), matches[0][0][:8])
        return matches[0]

    debug("resolve_composer: no match found")
    return None


def resolve_composer_id(
    ref: str,
    workspace_ref: str | None = None,
) -> str | None:
    """Resolve composer reference to just the composer UUID."""
    result = resolve_composer(ref, workspace_ref)
    return result[0] if result else None
