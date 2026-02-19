# Workspace commands: list-workspaces, show-workspace, tree
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


def get_workspace_index() -> List[Dict]:
    """Get indexed list of workspaces sorted by recency (most recent first)."""
    ws_list = sorted(
        [ws for ws in WORKSPACES_ROOT.iterdir() if ws.is_dir()],
        key=lambda w: (w / "state.vscdb").stat().st_mtime if (w / "state.vscdb").exists() else 0,
        reverse=True  # Most recent first
    )
    result = []
    for idx, ws in enumerate(ws_list):
        db_path = ws / "state.vscdb"
        result.append({
            "index": f"w{idx+1}",
            "idx": idx + 1,
            "hash": ws.name,
            "short": ws.name[:8],
            "path": ws,
            "folder": get_workspace_folder(ws) or "(unknown)",
            "db_size": db_path.stat().st_size if db_path.exists() else 0,
        })
    return result


def get_composer_index(ws_path: Path) -> List[Dict]:
    """Get indexed list of composers in a workspace sorted by message count."""
    bubble_counts = get_bubble_counts()
    composers = get_workspace_composers(ws_path)
    result = []
    for c in composers:
        cid = c.get("composerId", "")
        result.append({
            "composerId": cid,
            "short": cid[:8],
            "name": c.get("name"),
            "mode": c.get("unifiedMode"),
            "messages": bubble_counts.get(cid, 0),
            "createdAt": c.get("createdAt"),
        })
    
    # Sort by message count descending
    result.sort(key=lambda x: -x["messages"])
    for idx, c in enumerate(result):
        c["index"] = f"c{idx+1}"
        c["idx"] = idx + 1
    
    return result


def cmd_list_workspaces(args):
    """List workspaces with folder paths and stats."""
    # Gather workspace info
    ws_data = []
    for ws in WORKSPACES_ROOT.iterdir():
        if not ws.is_dir():
            continue
        db_path = ws / "state.vscdb"
        folder = get_workspace_folder(ws) or "(unknown)"
        if db_path.exists():
            st = db_path.stat()
            db_size, db_mtime = st.st_size, st.st_mtime
        else:
            db_size, db_mtime = 0, 0
        composers = get_workspace_composers(ws)
        ws_data.append({
            "hash": ws.name,
            "short": ws.name[:8],
            "folder": folder,
            "db_size": db_size,
            "db_mtime": db_mtime,
            "composer_count": len(composers),
            "path": ws,
        })
    
    # Sort based on --sort option
    sort_key = args.sort if hasattr(args, 'sort') else "size"
    oldest_first = getattr(args, 'oldest', False)
    
    if sort_key == "date":
        ws_data.sort(key=lambda w: w["db_mtime"], reverse=not oldest_first)
    elif sort_key == "name":
        ws_data.sort(key=lambda w: w["folder"].lower())
    elif sort_key == "chats":
        ws_data.sort(key=lambda w: w["composer_count"], reverse=True)
    else:  # size (default)
        ws_data.sort(key=lambda w: w["db_size"], reverse=True)
    
    # Apply limit if specified
    limit = getattr(args, 'limit', None)
    if limit:
        ws_data = ws_data[:limit]
    
    # Add indices after sorting
    for idx, w in enumerate(ws_data):
        w["index"] = f"w{idx+1}"
    
    out_fmt = get_output_format(args)
    if out_fmt != "text":
        # Remove path for serialization
        output = [{k: v for k, v in w.items() if k != "path"} for w in ws_data]
        output_data(output, out_fmt, "list-workspaces",
                   supported=["text", "json", "jsonl", "yaml", "csv", "md"])
        return
    else:
        if sort_key == "date":
            print(f"{'IDX':<5} {'SHORT':<10} {'MODIFIED':<20} {'CHATS':>5}  FOLDER")
            for w in ws_data:
                mtime_str = datetime.fromtimestamp(w["db_mtime"]).strftime("%Y-%m-%d %H:%M") if w["db_mtime"] else "?"
                folder = w["folder"]
                if len(folder) > 40:
                    folder = "..." + folder[-37:]
                print(f"{w['index']:<5} {w['short']:<10} {mtime_str:<20} {w['composer_count']:>5}  {folder}")
        else:
            print(f"{'IDX':<5} {'SHORT':<10} {'SIZE':>10} {'CHATS':>5}  FOLDER")
            for w in ws_data:
                size_kb = w["db_size"] // 1024
                folder = w["folder"]
                if len(folder) > 45:
                    folder = "..." + folder[-42:]
                print(f"{w['index']:<5} {w['short']:<10} {size_kb:>8}KB {w['composer_count']:>5}  {folder}")


def cmd_show_workspace(args):
    """Show detailed workspace info."""
    ws_path = resolve_workspace(args.workspace)
    if not ws_path:
        raise NotFoundError(f"Workspace not found: {args.workspace}")
    
    db_path = ws_path / "state.vscdb"
    composers = get_workspace_composers(ws_path)
    
    # Get prompts/generations counts
    prompts_count = 0
    generations_count = 0
    if db_path.exists():
        conn = open_db(db_path)
        cur = conn.cursor()
        for key in ["aiService.prompts", "aiService.generations"]:
            row = cur.execute("SELECT value FROM ItemTable WHERE key=?", (key,)).fetchone()
            if row:
                try:
                    data = json.loads(decode_blob(row[0]))
                    if key == "aiService.prompts":
                        prompts_count = len(data) if isinstance(data, list) else 0
                    else:
                        generations_count = len(data) if isinstance(data, list) else 0
                except:
                    pass
        conn.close()
    
    info = {
        "hash": ws_path.name,
        "folder": get_workspace_folder(ws_path),
        "db_size": db_path.stat().st_size if db_path.exists() else 0,
        "composers": composers,
        "prompts_count": prompts_count,
        "generations_count": generations_count,
    }
    
    if get_output_format(args) != "text":
        print(fmt(info, args))
    else:
        print(f"Workspace: {info['hash']}")
        print(f"Folder:    {info['folder']}")
        print(f"DB Size:   {info['db_size'] // 1024} KB")
        print(f"Prompts:   {prompts_count}")
        print(f"Generations: {generations_count}")
        print(f"\nComposers ({len(composers)}):")
        for c in composers[:20]:
            name = c.get("name") or "(unnamed)"
            mode = c.get("unifiedMode", "")
            created = format_ts(c.get("createdAt", ""))
            print(f"  {c.get('composerId', '?')[:16]}  {mode:<6} {created}  {name[:40]}")


def cmd_tree(args):
    """Tree-structured navigation with short IDs.
    
    Paths:
      (empty)    - List all workspaces as w1, w2, ...
      w1         - Show workspace 1 and its composers as c1, c2, ...
      w1.c2      - Show composer 2 in workspace 1
      w1.c2.tools - Show tools used in that composer
      w1.c2.files - Show files touched in that composer
    """
    path = args.path or ""
    parts = path.split(".") if path else []
    
    workspaces = get_workspace_index()
    
    # Level 0: List workspaces
    if not parts or not parts[0]:
        if get_output_format(args) != "text":
            print(fmt([{k: v for k, v in w.items() if k != "path"} for w in workspaces], args))
        else:
            print("WORKSPACES (use 'tree w1' to drill down)")
            print(f"{'IDX':<5} {'SHORT':<10} {'SIZE':>8} {'CHATS':>5}  FOLDER")
            for w in workspaces:
                composers = get_workspace_composers(w["path"])
                size_mb = w["db_size"] / 1024 / 1024
                folder = w["folder"]
                if len(folder) > 35:
                    folder = "..." + folder[-32:]
                print(f"{w['index']:<5} {w['short']:<10} {size_mb:>6.1f}MB {len(composers):>5}  {folder}")
        return
    
    # Parse workspace reference (w1, w2, or hash prefix)
    ws_ref = parts[0]
    ws_entry = None
    if ws_ref.startswith("w") and ws_ref[1:].isdigit():
        ws_idx = int(ws_ref[1:]) - 1
        if 0 <= ws_idx < len(workspaces):
            ws_entry = workspaces[ws_idx]
    else:
        # Try hash prefix or name
        ws_path = resolve_workspace(ws_ref)
        if ws_path:
            for w in workspaces:
                if w["path"] == ws_path:
                    ws_entry = w
                    break
    
    if not ws_entry:
        raise NotFoundError(f"Workspace not found: {ws_ref}")
    
    composers = get_composer_index(ws_entry["path"])
    
    # Level 1: Show workspace and composers
    if len(parts) == 1:
        if get_output_format(args) != "text":
            result = {
                "workspace": {k: str(v) if isinstance(v, Path) else v for k, v in ws_entry.items()},
                "composers": composers,
            }
            print(fmt(result, args))
        else:
            print(f"WORKSPACE {ws_entry['index']}: {ws_entry['folder']}")
            print(f"Hash: {ws_entry['hash']}")
            print(f"Size: {ws_entry['db_size'] / 1024 / 1024:.1f} MB")
            print()
            print(f"COMPOSERS (use 'tree {ws_entry['index']}.c1' to drill down)")
            print(f"{'IDX':<5} {'SHORT':<10} {'MSGS':>6} {'MODE':<8} NAME")
            for c in composers[:30]:
                name = (c.get("name") or "(unnamed)")[:35]
                mode = (c.get("mode") or "")[:8]
                print(f"{c['index']:<5} {c['short']:<10} {c['messages']:>6} {mode:<8} {name}")
            if len(composers) > 30:
                print(f"... and {len(composers) - 30} more")
        return
    
    # Parse composer reference (c1, c2, or UUID prefix)
    c_ref = parts[1]
    c_entry = None
    if c_ref.startswith("c") and c_ref[1:].isdigit():
        c_idx = int(c_ref[1:]) - 1
        if 0 <= c_idx < len(composers):
            c_entry = composers[c_idx]
    else:
        # Try UUID prefix or name
        for c in composers:
            if c["composerId"].startswith(c_ref) or (c.get("name") and c_ref.lower() in c["name"].lower()):
                c_entry = c
                break
    
    if not c_entry:
        raise NotFoundError(f"Composer not found: {c_ref}")
    
    # Level 2: Show composer details
    if len(parts) == 2:
        bubbles = load_bubbles(c_entry["composerId"])
        
        # Count message types
        user_msgs = sum(1 for b in bubbles if b.get("type") == 1)
        asst_msgs = sum(1 for b in bubbles if b.get("type") == 2)
        tool_calls = sum(1 for b in bubbles if b.get("toolFormerData"))
        
        # Get files touched
        files_touched = set()
        for b in bubbles:
            for f in b.get("fileSelections", []):
                uri = f.get("uri", {}).get("path", "")
                if uri:
                    files_touched.add(uri)
        
        if get_output_format(args) != "text":
            result = {
                "composer": c_entry,
                "stats": {
                    "total_bubbles": len(bubbles),
                    "user_messages": user_msgs,
                    "assistant_messages": asst_msgs,
                    "tool_calls": tool_calls,
                    "files_touched": len(files_touched),
                },
                "workspace": ws_entry["index"],
            }
            print(fmt(result, args))
        else:
            print(f"COMPOSER {ws_entry['index']}.{c_entry['index']}")
            print("─" * 60)
            print(f"  ID:       {c_entry['composerId']}")
            print(f"  Name:     {c_entry.get('name') or '(unnamed)'}")
            print(f"  Mode:     {c_entry.get('mode')}")
            print(f"  Messages: {c_entry['messages']}")
            print()
            print("  STATS")
            print(f"    User messages:      {user_msgs}")
            print(f"    Assistant messages: {asst_msgs}")
            print(f"    Tool calls:         {tool_calls}")
            print(f"    Files touched:      {len(files_touched)}")
            print()
            print("  SUBCOMMANDS")
            print(f"    tree {ws_entry['index']}.{c_entry['index']}.tools   - Tool calls")
            print(f"    tree {ws_entry['index']}.{c_entry['index']}.files   - Files touched")
            print(f"    tree {ws_entry['index']}.{c_entry['index']}.msgs    - Message preview")
            print()
            print(f"  Or use: transcript {c_entry['short']}")
        return
    
    # Level 3: Subdetails
    subcommand = parts[2] if len(parts) > 2 else ""
    bubbles = load_bubbles(c_entry["composerId"])
    
    if subcommand == "tools":
        tools = []
        for b in bubbles:
            tfd = b.get("toolFormerData")
            if tfd and isinstance(tfd, dict):
                tools.append({
                    "name": tfd.get("name", "?"),
                    "status": tfd.get("status", "?"),
                    "timestamp": format_ts(b.get("createdAt", "")),
                })
        
        if get_output_format(args) != "text":
            print(fmt(tools, args))
        else:
            print(f"TOOLS in {ws_entry['index']}.{c_entry['index']} ({len(tools)} calls)")
            print("─" * 60)
            for t in tools[:50]:
                print(f"  [{t['status']:<10}] {t['name']:<30} {t['timestamp']}")
            if len(tools) > 50:
                print(f"  ... and {len(tools) - 50} more")
    
    elif subcommand == "files":
        files = {}
        for b in bubbles:
            for f in b.get("fileSelections", []):
                uri = f.get("uri", {}).get("path", "")
                if uri:
                    files[uri] = files.get(uri, 0) + 1
        
        sorted_files = sorted(files.items(), key=lambda x: -x[1])
        
        if get_output_format(args) != "text":
            print(fmt([{"path": p, "mentions": c} for p, c in sorted_files], args))
        else:
            print(f"FILES in {ws_entry['index']}.{c_entry['index']} ({len(files)} unique)")
            print("─" * 70)
            for path, count in sorted_files[:30]:
                path_short = path if len(path) < 55 else "..." + path[-52:]
                print(f"  {count:>3}x  {path_short}")
            if len(sorted_files) > 30:
                print(f"  ... and {len(sorted_files) - 30} more")
    
    elif subcommand == "msgs":
        # Show last few messages
        recent = bubbles[-10:] if len(bubbles) > 10 else bubbles
        if get_output_format(args) != "text":
            print(fmt(recent, args))
        else:
            print(f"RECENT MESSAGES in {ws_entry['index']}.{c_entry['index']}")
            print("─" * 60)
            for b in recent:
                msg_type = "USER" if b.get("type") == 1 else "ASST" if b.get("type") == 2 else "????"
                text = (b.get("text") or "")[:80]
                ts = format_ts(b.get("createdAt", ""))
                print(f"  [{msg_type}] {ts}")
                if text:
                    print(f"         {text}")
    
    else:
        print(f"Unknown subcommand: {subcommand}")
        print(f"Available: tools, files, msgs")

