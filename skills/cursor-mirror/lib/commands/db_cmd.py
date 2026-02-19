# Database commands: sql, dbs, tables, keys, find, which
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


def resolve_db_path(ref: str) -> Optional[Path]:
    """Resolve database reference to path.
    
    Accepts:
      - 'global' or 'g': global state.vscdb
      - Workspace reference (hash, @index, folder name)
      - Full path to .vscdb file
    """
    if ref in ("global", "g"):
        return GLOBAL_DB
    
    # Check if it's a direct path
    if ref.endswith(".vscdb"):
        p = Path(ref)
        if p.exists():
            return p
    
    # Try workspace reference
    ws = resolve_workspace(ref)
    if ws:
        return ws / "state.vscdb"
    
    return None


def cmd_sql(args):
    """Run SQL query on Cursor databases."""
    db_path = resolve_db_path(args.db)
    if not db_path or not db_path.exists():
        raise NotFoundError(f"Database not found: {args.db}")
    
    conn = open_db(db_path)
    cur = conn.cursor()
    
    # Shortcut: --key to get a specific ItemTable value
    if args.key:
        row = cur.execute("SELECT value FROM ItemTable WHERE key = ?", (args.key,)).fetchone()
        conn.close()
        if not row:
            raise NotFoundError(f"Key not found: {args.key}")
        try:
            data = json.loads(row[0])
            if args.yaml:
                print(yaml.dump(data, default_flow_style=False, allow_unicode=True))
            elif args.json or not args.raw:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                print(row[0])
        except:
            print(row[0])
        return
    
    # Shortcut: --keys to list keys matching pattern
    if args.keys:
        pattern = args.keys if "%" in args.keys else f"%{args.keys}%"
        rows = cur.execute(
            "SELECT key, length(value) FROM ItemTable WHERE key LIKE ? ORDER BY length(value) DESC LIMIT ?",
            (pattern, args.limit)
        ).fetchall()
        conn.close()
        
        if get_output_format(args) != "text":
            data = [{"key": k, "size": s} for k, s in rows]
            print(fmt(data, args))
        else:
            print(f"{'KEY':<60} {'SIZE':>10}")
            print("─" * 72)
            for k, s in rows:
                k_display = k[:58] + ".." if len(k) > 60 else k
                print(f"{k_display:<60} {s:>10}")
        return
    
    # Shortcut: --table for simple table scan
    if args.table:
        query = f"SELECT * FROM {args.table} LIMIT {args.limit}"
    elif args.query:
        query = args.query
    else:
        # Interactive mode - show help
        print("Usage: sql [query] --db [global|workspace] [--key KEY] [--keys PATTERN] [--table TABLE]")
        print("\nExamples:")
        print("  sql \"SELECT key FROM ItemTable LIMIT 10\"")
        print("  sql --key cursorai/serverConfig")
        print("  sql --keys mcp")
        print("  sql --table ItemTable --limit 5")
        print("  sql --db moollm --keys composer")
        conn.close()
        return
    
    try:
        rows = cur.execute(query).fetchall()
        columns = [desc[0] for desc in cur.description] if cur.description else []
        conn.close()
        
        if get_output_format(args) != "text":
            data = [dict(zip(columns, row)) for row in rows]
            print(fmt(data, args))
        else:
            if columns:
                # Pretty print table
                col_widths = [max(len(str(c)), max(len(str(row[i])) for row in rows) if rows else 0) 
                              for i, c in enumerate(columns)]
                col_widths = [min(w, 40) for w in col_widths]  # Cap width
                
                header = "  ".join(f"{c:<{col_widths[i]}}" for i, c in enumerate(columns))
                print(header)
                print("─" * len(header))
                for row in rows:
                    line = "  ".join(
                        f"{str(v)[:col_widths[i]]:<{col_widths[i]}}" 
                        for i, v in enumerate(row)
                    )
                    print(line)
                print(f"\n({len(rows)} rows)")
    except Exception as e:
        conn.close()
        raise DatabaseError(f"SQL Error: {e}")


def cmd_dbs(args):
    """List all Cursor databases with sizes."""
    dbs = []
    
    # Global DB
    if GLOBAL_DB.exists():
        dbs.append({
            "name": "global",
            "path": str(GLOBAL_DB),
            "size_mb": round(GLOBAL_DB.stat().st_size / 1024 / 1024, 2),
            "type": "global",
        })
    
    # Workspace DBs
    for ws in sorted(WORKSPACES_ROOT.iterdir(), key=lambda w: (w / "state.vscdb").stat().st_size if (w / "state.vscdb").exists() else 0, reverse=True):
        if not ws.is_dir():
            continue
        db_path = ws / "state.vscdb"
        if db_path.exists():
            folder = get_workspace_folder(ws)
            dbs.append({
                "name": ws.name[:8],
                "hash": ws.name,
                "folder": folder,
                "path": str(db_path),
                "size_mb": round(db_path.stat().st_size / 1024 / 1024, 2),
                "type": "workspace",
            })
    
    if get_output_format(args) != "text":
        print(fmt(dbs, args))
    else:
        print(f"{'NAME':<10} {'SIZE':>8} {'TYPE':<10} PATH/FOLDER")
        print("─" * 90)
        for db in dbs:
            if db["type"] == "global":
                print(f"{'global':<10} {db['size_mb']:>6}MB {'global':<10} {db['path']}")
            else:
                folder = db.get("folder", "?")
                if folder and len(folder) > 50:
                    folder = "..." + folder[-47:]
                print(f"{db['name']:<10} {db['size_mb']:>6}MB {'workspace':<10} {folder}")
        print(f"\nTotal: {len(dbs)} databases, {sum(d['size_mb'] for d in dbs):.1f} MB")


def cmd_tables(args):
    """List tables in a database."""
    db_path = resolve_db_path(args.db)
    if not db_path or not db_path.exists():
        raise NotFoundError(f"Database not found: {args.db}")
    
    conn = open_db(db_path)
    cur = conn.cursor()
    
    tables = []
    for (name,) in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
        row_count = cur.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
        tables.append({"name": name, "rows": row_count})
    
    conn.close()
    
    if get_output_format(args) != "text":
        print(fmt(tables, args))
    else:
        print(f"Database: {db_path}")
        print("─" * 50)
        print(f"{'TABLE':<30} {'ROWS':>10}")
        print("─" * 50)
        for t in tables:
            print(f"{t['name']:<30} {t['rows']:>10}")


def cmd_keys(args):
    """List ItemTable keys with sizes."""
    db_path = resolve_db_path(args.db)
    if not db_path or not db_path.exists():
        raise NotFoundError(f"Database not found: {args.db}")
    
    conn = open_db(db_path)
    cur = conn.cursor()
    
    if args.pattern:
        pattern = args.pattern if "%" in args.pattern else f"%{args.pattern}%"
        rows = cur.execute(
            "SELECT key, length(value) FROM ItemTable WHERE key LIKE ? ORDER BY length(value) DESC LIMIT ?",
            (pattern, args.limit)
        ).fetchall()
    else:
        rows = cur.execute(
            "SELECT key, length(value) FROM ItemTable ORDER BY length(value) DESC LIMIT ?",
            (args.limit,)
        ).fetchall()
    
    conn.close()
    
    keys = [{"key": k, "size": s} for k, s in rows]
    
    if get_output_format(args) != "text":
        print(fmt(keys, args))
    else:
        print(f"Database: {db_path}")
        print()
        print(f"{'KEY':<60} {'SIZE':>12}")
        print()
        for k in keys:
            key_display = k["key"][:58] + ".." if len(k["key"]) > 60 else k["key"]
            size_str = f"{k['size']:,}" if k["size"] < 1024 else f"{k['size']//1024:,}KB"
            print(f"{key_display:<60} {size_str:>12}")
        print(f"\n({len(keys)} keys shown)")


def cmd_find(args):
    """Find workspaces/composers by name pattern or hash prefix."""
    pattern = args.pattern.lower()
    results = {"workspaces": [], "composers": []}
    
    # Check if pattern looks like a hash prefix (hex chars only)
    is_hash_pattern = all(c in '0123456789abcdef' for c in pattern) and len(pattern) >= 4
    
    if args.type in ("workspace", "all"):
        for ws in WORKSPACES_ROOT.iterdir():
            if not ws.is_dir():
                continue
            folder = get_workspace_folder(ws)
            # Match by hash prefix OR folder name
            hash_match = is_hash_pattern and ws.name.lower().startswith(pattern)
            name_match = folder and pattern in folder.lower()
            if hash_match or name_match:
                db_path = ws / "state.vscdb"
                results["workspaces"].append({
                    "hash": ws.name,
                    "short": ws.name[:8],
                    "folder": folder,
                    "db_size_kb": db_path.stat().st_size // 1024 if db_path.exists() else 0,
                })
    
    if args.type in ("composer", "all"):
        # Use cached all-composers
        all_composers = get_all_composers()
        
        for cid, c in all_composers.items():
            name = c.get("name", "") or ""
            folder = c.get("_workspace_folder") or ""
            # Match by hash prefix OR name/folder
            hash_match = is_hash_pattern and cid.lower().startswith(pattern)
            name_match = pattern in name.lower() or pattern in folder.lower()
            if hash_match or name_match:
                results["composers"].append({
                    "id": cid,
                    "short": cid[:8],
                    "name": name,
                    "messages": c.get("_bubble_count", 0),
                    "workspace": folder,
                    "workspace_hash": c.get("_workspace", "?")[:8],
                })
        
        results["composers"].sort(key=lambda x: x["messages"], reverse=True)
    
    if get_output_format(args) != "text":
        print(fmt(results, args))
    else:
        if results["workspaces"]:
            print("WORKSPACES")
            print()
            print(f"{'SHORT':<10} {'SIZE':>8} FOLDER")
            for w in results["workspaces"]:
                print(f"{w['short']:<10} {w['db_size_kb']:>6}KB {w['folder']}")
            print()
        
        if results["composers"]:
            print("COMPOSERS")
            print("─" * 100)
            print(f"{'SHORT':<10} {'MSGS':>6} {'WORKSPACE':<20} NAME")
            for c in results["composers"][:30]:
                ws_short = c["workspace"][-18:] if c["workspace"] and len(c["workspace"]) > 20 else (c["workspace"] or "?")
                name = c["name"][:45] if c["name"] else "(unnamed)"
                print(f"{c['short']:<10} {c['messages']:>6} {ws_short:<20} {name}")
            if len(results["composers"]) > 30:
                print(f"... and {len(results['composers']) - 30} more")


def cmd_which(args):
    """Resolve workspace/composer reference to full details."""
    if args.type == "workspace":
        ws = resolve_workspace(args.ref)
        if not ws:
            raise NotFoundError(f"Workspace not found: {args.ref}")
        
        folder = get_workspace_folder(ws)
        db_path = ws / "state.vscdb"
        composers = get_workspace_composers(ws)
        
        result = {
            "hash": ws.name,
            "short": ws.name[:8],
            "folder": folder,
            "db_path": str(db_path),
            "db_size_kb": db_path.stat().st_size // 1024 if db_path.exists() else 0,
            "composer_count": len(composers),
        }
        
        if get_output_format(args) != "text":
            print(fmt(result, args))
        else:
            print(f"Hash:     {result['hash']}")
            print(f"Short:    {result['short']}")
            print(f"Folder:   {result['folder']}")
            print(f"DB Path:  {result['db_path']}")
            print(f"DB Size:  {result['db_size_kb']} KB")
            print(f"Composers: {result['composer_count']}")
    
    else:  # composer
        resolved = resolve_composer(args.ref)
        if not resolved:
            raise NotFoundError(f"Composer not found: {args.ref}")
        
        cid, meta = resolved
        result = {
            "id": cid,
            "short": cid[:8],
            "name": meta.get("name"),
            "mode": meta.get("unifiedMode"),
            "created": meta.get("createdAt"),
            "messages": meta.get("_bubble_count", 0),
            "workspace_hash": meta.get("_workspace"),
        }
        
        if get_output_format(args) != "text":
            print(fmt(result, args))
        else:
            print(f"ID:        {result['id']}")
            print(f"Short:     {result['short']}")
            print(f"Name:      {result['name']}")
            print(f"Mode:      {result['mode']}")
            print(f"Created:   {result['created']}")
            print(f"Messages:  {result['messages']}")
            print(f"Workspace: {result['workspace_hash']}")

