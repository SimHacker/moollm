# Composer commands: list-composers, show-composer
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


def cmd_list_composers(args):
    """List composers with metadata, optionally filtered by workspace."""
    # Resolve workspace filter if provided
    target_ws = None
    target_ws_hash = None
    if args.workspace:
        target_ws = resolve_workspace(args.workspace)
        if not target_ws:
            raise NotFoundError(f"Workspace not found: {args.workspace}")
        target_ws_hash = target_ws.name
    
    # Get bubble counts (uses helper)
    bubble_counts = get_bubble_counts()
    
    # Gather composer metadata from workspaces
    composers_meta: Dict[str, Dict] = {}
    for ws in WORKSPACES_ROOT.iterdir():
        if not ws.is_dir():
            continue
        if target_ws_hash and ws.name != target_ws_hash:
            continue
        folder = get_workspace_folder(ws)
        for c in get_workspace_composers(ws):
            cid = c.get("composerId")
            if cid:
                composers_meta[cid] = c
                composers_meta[cid]["_workspace"] = ws.name
                composers_meta[cid]["_folder"] = folder
                composers_meta[cid]["_bubble_count"] = bubble_counts.get(cid, 0)
    
    # Build composer list
    composers = []
    for cid, meta in composers_meta.items():
        composers.append({
            "composerId": cid,
            "short": cid[:8],
            "bubble_count": meta.get("_bubble_count", 0),
            "name": meta.get("name"),
            "mode": meta.get("unifiedMode"),
            "createdAt": meta.get("createdAt"),
            "lastUpdatedAt": meta.get("lastUpdatedAt"),
            "workspace": meta.get("_workspace", "")[:8],
            "folder": meta.get("_folder"),
        })
    
    # Sort based on --sort option
    sort_key = args.sort if hasattr(args, 'sort') else "msgs"
    oldest_first = getattr(args, 'oldest', False)
    
    if sort_key == "date":
        # Sort by lastUpdatedAt or createdAt
        composers.sort(key=lambda c: c.get("lastUpdatedAt") or c.get("createdAt") or 0, 
                      reverse=not oldest_first)
    elif sort_key == "name":
        composers.sort(key=lambda c: (c.get("name") or "zzz").lower())
    else:  # msgs (default)
        composers.sort(key=lambda c: c["bubble_count"], reverse=True)
    
    # Limit and add indices after sorting
    composers = composers[:args.limit]
    for idx, c in enumerate(composers):
        c["index"] = f"c{idx+1}"
    
    if get_output_format(args) != "text":
        print(fmt(composers, args))
    else:
        if target_ws:
            folder = get_workspace_folder(target_ws)
            print(f"Workspace: {folder}")
            print(f"Hash: {target_ws.name}")
            print()
        
        if sort_key == "date":
            order = "oldest first" if oldest_first else "newest first"
            print(f"{'IDX':<5} {'SHORT':<10} {'DATE':<18} {'MSGS':>5} NAME  ({order})")
            print("─" * 85)
            for c in composers:
                name = (c.get("name") or "(unnamed)")[:35]
                ts = c.get("lastUpdatedAt") or c.get("createdAt")
                if ts:
                    date_str = datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M")
                else:
                    date_str = "?"
                print(f"{c['index']:<5} {c['short']:<10} {date_str:<18} {c['bubble_count']:>5} {name}")
        else:
            print(f"{'IDX':<5} {'SHORT':<10} {'MSGS':>6} {'MODE':<6} NAME")
            print()
            for c in composers:
                name = (c.get("name") or "(unnamed)")[:45]
                mode = (c.get("mode") or "")[:6]
                print(f"{c['index']:<5} {c['short']:<10} {c['bubble_count']:>6} {mode:<6} {name}")


def cmd_show_composer(args):
    """Show detailed composer info."""
    # Use unified resolve_composer for all reference types
    result = resolve_composer(args.composer)
    if not result:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    target, meta = result
    debug("cmd_show_composer: resolved %s -> %s", args.composer, target[:8])
    
    # Add folder info if not present
    if "_folder" not in meta and "_workspace" in meta:
        ws_path = WORKSPACES_ROOT / meta["_workspace"]
        meta["_folder"] = get_workspace_folder(ws_path)
    
    bubbles = load_bubbles(target)
    
    # Analyze bubbles
    user_count = sum(1 for b in bubbles if b.get("type") == 1)
    assistant_count = sum(1 for b in bubbles if b.get("type") == 2)
    with_text = sum(1 for b in bubbles if get_bubble_text(b))
    with_code = sum(1 for b in bubbles if b.get("codeBlocks"))
    with_thinking = sum(1 for b in bubbles if b.get("thinking"))
    
    info = {
        "composerId": target,
        "name": meta.get("name"),
        "mode": meta.get("unifiedMode"),
        "workspace": meta.get("_workspace"),
        "folder": meta.get("_folder"),
        "createdAt": meta.get("createdAt"),
        "lastUpdatedAt": meta.get("lastUpdatedAt"),
        "stats": {
            "total_bubbles": len(bubbles),
            "user_messages": user_count,
            "assistant_messages": assistant_count,
            "with_text": with_text,
            "with_code_blocks": with_code,
            "with_thinking": with_thinking,
        },
        "first_message": bubbles[0].get("createdAt") if bubbles else None,
        "last_message": bubbles[-1].get("createdAt") if bubbles else None,
    }
    
    if get_output_format(args) != "text":
        print(fmt(info, args))
    else:
        print(f"Composer: {info['composerId']}")
        print(f"Name:     {info['name'] or '(unnamed)'}")
        print(f"Mode:     {info['mode']}")
        print(f"Workspace: {info['workspace']}")
        print(f"Folder:   {info['folder']}")
        print(f"\nStats:")
        for k, v in info["stats"].items():
            print(f"  {k}: {v}")
        print(f"\nTimespan: {format_ts(info['first_message'])} → {format_ts(info['last_message'])}")

