# Files and todos commands
# Extracted from cursor_mirror_old.py during Phase 2 refactoring.

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml
import os

from ..db import open_db, decode_blob, get_item_table_value, get_reactive_storage
from ..paths import GLOBAL_DB, WORKSPACES_ROOT, BASE_DIR
from ..keys import SESSION_LIST_KEYS, COMPOSER_STATE_KEY, NOTABLE_GLOBAL_KEYS
from ..discovery import iter_workspace_paths, get_workspace_folder, folder_uri_to_path
from ..composers import get_workspace_composers, get_all_composers, get_bubble_counts, clear_caches
from ..bubbles import iter_bubbles, load_bubbles, get_bubble_text, has_content, extract_bubble_text, is_error, USER, ASSISTANT
from ..resolve import resolve_workspace, resolve_composer, resolve_composer_id
from ..format_util import format_ts, get_output_format, output_data, format_not_supported
from ..debug_util import debug
from ..sources import register_source


def _replay_todos_from_transcript(composer_id: str) -> Optional[List[Dict]]:
    """Replay TodoWrite calls from agent transcript to reconstruct todo state.
    
    Parses lines like:
      [Tool call] TodoWrite
        todos: [{"id":"x","content":"...","status":"pending"}]
        merge: false
    
    Applies merge logic: merge=false replaces, merge=true patches by id.
    Returns final todo list or None if no transcript found.
    """
    workspaces = get_dotcursor_workspaces()
    transcript_path = None
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        for f in os.listdir(trans_dir):
            if f.startswith(composer_id) and f.endswith(".txt"):
                transcript_path = os.path.join(trans_dir, f)
                break
        if transcript_path:
            break

    if not transcript_path:
        return None

    with open(transcript_path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    # Parse TodoWrite calls: look for "[Tool call] TodoWrite" then extract args
    todos_by_id: Dict[str, Dict] = {}
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if line == "[Tool call] TodoWrite":
            todos_json = None
            merge = False
            # Read the next few lines for todos: and merge: fields
            for j in range(i + 1, min(i + 6, len(lines))):
                arg_line = lines[j].rstrip()
                if arg_line.startswith("  todos: "):
                    try:
                        todos_json = json.loads(arg_line[9:])
                    except json.JSONDecodeError:
                        pass
                elif arg_line.startswith("  merge: "):
                    merge = arg_line[9:].strip().lower() == "true"
                elif arg_line.startswith("[") or arg_line.startswith("assistant:"):
                    break
            if todos_json is not None:
                if not merge:
                    todos_by_id = {}
                for item in todos_json:
                    tid = item.get("id")
                    if not tid:
                        continue
                    if merge and tid in todos_by_id:
                        # Patch: only update fields that are present
                        for k, v in item.items():
                            if v is not None:
                                todos_by_id[tid][k] = v
                    else:
                        todos_by_id[tid] = item
        i += 1

    if not todos_by_id:
        return None
    return list(todos_by_id.values())


def cmd_files(args):
    """List files touched in a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Collect file references
    files_seen: Dict[str, Dict[str, int]] = {}
    
    def add_file(path: Any, is_write: bool = False) -> None:
        """Add a file path to the seen files, handling various formats."""
        if not path:
            return
        # Handle dict (e.g., URI objects)
        if isinstance(path, dict):
            path = path.get("fsPath") or path.get("path") or path.get("uri") or ""
        if not isinstance(path, str) or not path:
            return
        files_seen.setdefault(path, {"reads": 0, "writes": 0})
        if is_write:
            files_seen[path]["writes"] += 1
        else:
            files_seen[path]["reads"] += 1
    
    for b in bubbles:
        # From context
        ctx = b.get("context", {})
        for sel in ctx.get("fileSelections", []):
            if isinstance(sel, dict):
                add_file(sel.get("relativePath") or sel.get("uri"))
            else:
                add_file(sel)
        
        # From code blocks (potential writes)
        for cb in b.get("codeBlocks", []):
            if isinstance(cb, dict):
                add_file(cb.get("relativePath"), is_write=True)
        
        # From file links in response
        for fl in b.get("fileLinks", []):
            if isinstance(fl, str):
                try:
                    fl = json.loads(fl)
                except:
                    continue
            if isinstance(fl, dict):
                add_file(fl.get("relativeWorkspacePath") or fl.get("displayName"))
        
        # From symbol links
        for sl in b.get("symbolLinks", []):
            if isinstance(sl, str):
                try:
                    sl = json.loads(sl)
                except:
                    continue
            if isinstance(sl, dict):
                add_file(sl.get("relativeWorkspacePath"))
    
    # Sort by activity
    files_list = [
        {"path": path, **counts}
        for path, counts in sorted(files_seen.items(), key=lambda x: -(x[1]["reads"] + x[1]["writes"]))
    ]
    
    if get_output_format(args) != "text":
        print(fmt(files_list, args))
    else:
        print(f"Files touched in composer {target[:16]}...")
        print(f"{'PATH':<60} {'READS':>6} {'WRITES':>6}")
        print()
        for f in files_list[:50]:
            path = f["path"]
            if len(path) > 58:
                path = "..." + path[-55:]
            print(f"{path:<60} {f['reads']:>6} {f['writes']:>6}")


def cmd_todos(args):
    """Show todos/tasks from a conversation.
    
    Reconstructs todo state by replaying TodoWrite tool calls from the
    agent transcript. Falls back to bubble 'todos' field if no transcript.
    """
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")

    # Primary: replay from agent transcript (has full TodoWrite history)
    all_todos = _replay_todos_from_transcript(target)
    source = "transcript"

    # Fallback: check bubble data
    if not all_todos:
        source = "bubbles"
        bubbles = load_bubbles(target)
        all_todos = []
        for b in bubbles:
            todos = b.get("todos", [])
            if todos:
                parsed = []
                for t in todos:
                    if isinstance(t, str):
                        try:
                            t = json.loads(t)
                        except Exception:
                            continue
                    parsed.append(t)
                if parsed:
                    all_todos = parsed

    if not all_todos:
        all_todos = []

    # Apply filters
    status_filter = getattr(args, "status", "all")
    search_filter = getattr(args, "search", None)
    if status_filter and status_filter != "all":
        all_todos = [t for t in all_todos if t.get("status") == status_filter]
    if search_filter:
        search_lower = search_filter.lower()
        all_todos = [t for t in all_todos
                     if search_lower in (t.get("content", "") + t.get("id", "")).lower()]

    if get_output_format(args) != "text":
        print(fmt(all_todos, args))
    else:
        status_counts = {}
        for t in all_todos:
            s = t.get("status", "?")
            status_counts[s] = status_counts.get(s, 0) + 1
        summary = ", ".join(f"{v} {k}" for k, v in sorted(status_counts.items()))
        print(f"Todos in {target[:16]}... ({len(all_todos)} items, source: {source})")
        if summary:
            print(f"  {summary}")
        print("─" * 60)
        for t in all_todos:
            status = t.get("status", "?")
            icon = {"completed": "✓", "in_progress": "→", "pending": "○",
                    "cancelled": "✗"}.get(status, "?")
            tid = t.get("id", "")
            content = t.get("content", "")
            print(f"  {icon} [{status:<11}] {content}  ({tid})")

