# Context assembly commands: context, context-sources, request-context, searches, indexing
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


def cmd_context(args):
    """Show context gathered in a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Aggregate context
    context_summary = {
        "file_selections": [],
        "terminal_selections": [],
        "code_selections": [],
        "cursor_rules": [],
        "folder_selections": [],
        "mentions": [],
    }
    
    for b in bubbles:
        ctx = b.get("context", {})
        if not ctx:
            continue
        
        for sel in ctx.get("fileSelections", []):
            path = sel.get("uri", "") or sel.get("relativePath", "")
            if path and path not in context_summary["file_selections"]:
                context_summary["file_selections"].append(path)
        
        for sel in ctx.get("terminalSelections", []):
            text = sel.get("text", "")[:100]
            if text:
                context_summary["terminal_selections"].append(text)
        
        for sel in ctx.get("selections", []):
            path = sel.get("relativePath", sel.get("uri", ""))
            if path and path not in context_summary["code_selections"]:
                context_summary["code_selections"].append(path)
        
        for rule in ctx.get("cursorRules", []):
            if rule and rule not in context_summary["cursor_rules"]:
                context_summary["cursor_rules"].append(rule[:100] if isinstance(rule, str) else str(rule)[:100])
        
        for folder in ctx.get("folderSelections", []):
            path = folder.get("relativePath", folder.get("uri", ""))
            if path and path not in context_summary["folder_selections"]:
                context_summary["folder_selections"].append(path)
        
        for mention in ctx.get("mentions", []):
            if mention and mention not in context_summary["mentions"]:
                context_summary["mentions"].append(str(mention)[:100])
    
    if get_output_format(args) != "text":
        print(fmt(context_summary, args))
    else:
        print(f"Context gathered in {target[:16]}...")
        print("─" * 60)
        for key, items in context_summary.items():
            if items:
                print(f"\n{key} ({len(items)}):")
                for item in items[:20]:
                    if len(str(item)) > 70:
                        item = str(item)[:67] + "..."
                    print(f"  • {item}")
                if len(items) > 20:
                    print(f"  ... and {len(items) - 20} more")


def cmd_context_sources(args):
    """Analyze all context sources in a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Aggregate all context sources
    sources = {
        "file_selections": set(),
        "folder_selections": set(),
        "code_selections": [],
        "terminal_selections": 0,
        "image_attachments": 0,
        "web_links": set(),
        "mentions": [],
        "codebase_searches": 0,
        "web_searches": 0,
        "cursor_rules": [],
    }
    
    for b in bubbles:
        ctx = b.get("context", {})
        if not ctx:
            continue
        
        # File selections
        for sel in ctx.get("fileSelections", []):
            uri = sel.get("uri", {})
            path = uri.get("path", uri.get("fsPath", ""))
            if path:
                sources["file_selections"].add(path)
        
        # Folder selections
        for sel in ctx.get("folderSelections", []):
            path = sel.get("relativePath", "")
            if path:
                sources["folder_selections"].add(path)
        
        # Code selections
        for sel in ctx.get("selections", []):
            text = sel.get("text", "")
            if text and len(text) > 20:
                sources["code_selections"].append({
                    "preview": text[:100],
                    "length": len(text),
                })
        
        # Terminal
        sources["terminal_selections"] += len(ctx.get("terminalSelections", []))
        
        # Images
        sources["image_attachments"] += len(ctx.get("selectedImages", []))
        
        # External links
        for link in ctx.get("externalLinks", []):
            if isinstance(link, dict):
                sources["web_links"].add(link.get("url", ""))
            elif isinstance(link, str):
                sources["web_links"].add(link)
        
        # Mentions
        for mention in ctx.get("mentions", []):
            if mention not in sources["mentions"]:
                sources["mentions"].append(mention)
        
        # Cursor rules
        for rule in ctx.get("cursorRules", []):
            if rule and rule not in sources["cursor_rules"]:
                sources["cursor_rules"].append(str(rule)[:100])
        
        # Tool calls
        tfd = b.get("toolFormerData", {})
        if tfd:
            name = tfd.get("name", "")
            if name == "codebase_search":
                sources["codebase_searches"] += 1
            elif name == "web_search":
                sources["web_searches"] += 1
    
    # Convert sets to lists for output
    sources["file_selections"] = sorted(sources["file_selections"])
    sources["folder_selections"] = sorted(sources["folder_selections"])
    sources["web_links"] = sorted(sources["web_links"])
    
    if get_output_format(args) != "text":
        print(fmt(sources, args))
    else:
        print(f"Context Sources: {target[:24]}...")
        
        print(f"\n📁 File Selections ({len(sources['file_selections'])})")
        for f in sources["file_selections"][:10]:
            print(f"  {f}")
        if len(sources["file_selections"]) > 10:
            print(f"  ... and {len(sources['file_selections']) - 10} more")
        
        print(f"\n📂 Folder Selections ({len(sources['folder_selections'])})")
        for f in sources["folder_selections"][:5]:
            print(f"  {f}")
        
        print(f"\n📝 Code Selections ({len(sources['code_selections'])})")
        for cs in sources["code_selections"][:3]:
            print(f"  [{cs['length']} chars] {cs['preview'][:60]}...")
        
        print(f"\n💻 Terminal Selections: {sources['terminal_selections']}")
        print(f"🖼️  Image Attachments: {sources['image_attachments']}")
        
        print(f"\n🔗 Web Links ({len(sources['web_links'])})")
        for link in list(sources["web_links"])[:5]:
            print(f"  {link[:70]}")
        
        print(f"\n🔍 Codebase Searches: {sources['codebase_searches']}")
        print(f"🌐 Web Searches: {sources['web_searches']}")
        
        if sources["mentions"]:
            print(f"\n📢 Mentions ({len(sources['mentions'])})")
            for m in sources["mentions"][:10]:
                print(f"  {str(m)[:60]}")
        
        if sources["cursor_rules"]:
            print(f"\n📋 Cursor Rules ({len(sources['cursor_rules'])})")
            for r in sources["cursor_rules"][:3]:
                print(f"  {r[:60]}...")


def cmd_request_context(args):
    """Show full context assembled for a message."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    # Find messageRequestContext for this composer
    pattern = f"messageRequestContext:{target}:%"
    if args.message:
        pattern = f"messageRequestContext:{target}:{args.message}%"
    
    rows = cur.execute(
        "SELECT key, value FROM cursorDiskKV WHERE key LIKE ? ORDER BY length(value) DESC LIMIT 5",
        (pattern,)
    ).fetchall()
    conn.close()
    
    if not rows:
        raise NotFoundError(f"No request context found for {target[:16]}...")
    
    contexts = []
    for k, v in rows:
        parts = k.split(":")
        msg_id = parts[2][:16] if len(parts) > 2 else ""
        
        obj = json.loads(decode_blob(v))
        
        ctx = {
            "message_id": msg_id,
            "size_bytes": len(v),
        }
        
        # Parse each field
        for field in obj.keys():
            val = obj[field]
            if isinstance(val, str) and len(val) > 10:
                try:
                    parsed = json.loads(val)
                    ctx[field] = parsed
                except:
                    ctx[field] = val[:200] + "..." if len(val) > 200 else val
            elif isinstance(val, list):
                ctx[field] = {"count": len(val), "items": val[:3]}
            elif val:
                ctx[field] = val
        
        contexts.append(ctx)
    
    if get_output_format(args) != "text":
        print(fmt(contexts, args))
    else:
        for ctx in contexts[:1]:  # Show first/largest
            print(f"Request Context: {ctx['message_id']}... ({ctx['size_bytes']} bytes)")
            
            # IDE state
            if "ideEditorsState" in ctx:
                state = ctx["ideEditorsState"]
                if isinstance(state, dict):
                    visible = state.get("visibleFiles", [])
                    print(f"\n📁 Visible Files ({len(visible)}):")
                    for f in visible[:5]:
                        focus = "→" if f.get("isCurrentlyFocused") else " "
                        print(f"  {focus} {f.get('relativePath', f.get('absolutePath', '?'))}")
                        if f.get("currentLineNumber"):
                            print(f"      Line {f['currentLineNumber']}: {f.get('currentLineText', '')[:50]}")
            
            # Current location
            if "currentFileLocationData" in ctx:
                loc = ctx["currentFileLocationData"]
                if isinstance(loc, dict):
                    print(f"\n📍 Cursor: {loc.get('relativeWorkspacePath')}:{loc.get('lineNumber')}")
            
            # Todos
            if "todos" in ctx:
                todos = ctx["todos"]
                if isinstance(todos, dict) and todos.get("count", 0) > 0:
                    print(f"\n✅ Todos ({todos['count']}):")
                    for t in todos.get("items", []):
                        if isinstance(t, str):
                            try:
                                t = json.loads(t)
                            except:
                                pass
                        if isinstance(t, dict):
                            print(f"  {t.get('status', '?')}: {t.get('content', '')[:50]}")
            
            # Diffs
            if "diffsSinceLastApply" in ctx:
                diffs = ctx["diffsSinceLastApply"]
                if isinstance(diffs, dict) and diffs.get("count", 0) > 0:
                    print(f"\n📝 Pending Diffs ({diffs['count']}):")
                    for d in diffs.get("items", []):
                        if isinstance(d, str):
                            try:
                                d = json.loads(d)
                            except:
                                pass
                        if isinstance(d, dict):
                            status = "✓" if d.get("isAccepted") else "✗" if d.get("isRejected") else "?"
                            print(f"  {status} {d.get('relativeWorkspacePath', '')}")
            
            # Deleted files
            if "deletedFiles" in ctx:
                deleted = ctx["deletedFiles"]
                if isinstance(deleted, dict) and deleted.get("count", 0) > 0:
                    print(f"\n🗑️ Deleted Files ({deleted['count']})")


def cmd_searches(args):
    """Show codebase/web searches in a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    searches = []
    for b in bubbles:
        tfd = b.get("toolFormerData", {})
        if not tfd or not isinstance(tfd, dict):
            continue
        
        name = tfd.get("name", "")
        if args.type == "codebase" and name != "codebase_search":
            continue
        if args.type == "web" and name != "web_search":
            continue
        if name not in ["codebase_search", "web_search"]:
            continue
        
        search = {
            "type": name,
            "timestamp": format_ts(b.get("createdAt", "")),
            "status": tfd.get("status", "unknown"),
        }
        
        # Parse args
        try:
            raw_args = json.loads(tfd.get("rawArgs", "{}"))
            search["query"] = raw_args.get("query", "")
            search["target_dirs"] = raw_args.get("target_directories", [])
            search["explanation"] = raw_args.get("explanation", "")
        except:
            pass
        
        # Parse results
        if args.verbose:
            result = tfd.get("result", "")
            if result:
                try:
                    res = json.loads(result)
                    if name == "codebase_search":
                        code_results = res.get("codeResults", [])
                        search["result_count"] = len(code_results)
                        search["results"] = []
                        for cr in code_results[:5]:
                            cb = cr.get("codeBlock", {})
                            search["results"].append({
                                "path": cb.get("relativeWorkspacePath", ""),
                                "range": cb.get("range", {}),
                                "score": cr.get("score", 0),
                                "preview": cb.get("contents", "")[:100],
                            })
                    elif name == "web_search":
                        refs = res.get("references", [])
                        search["result_count"] = len(refs)
                        search["results"] = []
                        for ref in refs[:3]:
                            search["results"].append({
                                "title": ref.get("title", ""),
                                "chunk": ref.get("chunk", "")[:150],
                            })
                except:
                    pass
        
        searches.append(search)
    
    if get_output_format(args) != "text":
        print(fmt(searches, args))
    else:
        print(f"Searches in {target[:16]}... ({len(searches)} total)")
        print("─" * 100)
        for s in searches:
            icon = "🔍" if s["type"] == "codebase_search" else "🌐"
            print(f"\n{s['timestamp']} {icon} {s['type']}")
            print(f"  Query: {s.get('query', '')[:80]}")
            if s.get("target_dirs"):
                print(f"  Dirs: {s['target_dirs']}")
            if args.verbose and s.get("results"):
                print(f"  Results ({s.get('result_count', 0)}):")
                for r in s["results"]:
                    if "path" in r:
                        print(f"    📄 {r['path']}")
                    elif "title" in r:
                        print(f"    🔗 {r['title']}")


def cmd_indexing(args):
    """Show indexing status and embeddable files."""
    if args.workspace:
        ws_path = resolve_workspace(args.workspace)
        if not ws_path:
            raise NotFoundError(f"Workspace not found: {args.workspace}")
        workspaces = [ws_path]
    else:
        workspaces = [d for d in WORKSPACES_ROOT.iterdir() if d.is_dir()]
    
    results = []
    for ws in workspaces:
        retrieval_dir = ws / "anysphere.cursor-retrieval"
        if not retrieval_dir.exists():
            continue
        
        ws_info = {
            "workspace_hash": ws.name[:20],
            "folder": get_workspace_folder(ws),
        }
        
        # Embeddable files
        embeddable_file = retrieval_dir / "embeddable_files.txt"
        if embeddable_file.exists():
            content = embeddable_file.read_text()
            files = [f for f in content.strip().split("\n") if f]
            ws_info["embeddable_file_count"] = len(files)
            if args.files:
                ws_info["embeddable_files"] = files[:100]
                if len(files) > 100:
                    ws_info["embeddable_files_truncated"] = len(files) - 100
        
        # Folder descriptions
        folder_desc_file = retrieval_dir / "high_level_folder_description.txt"
        if folder_desc_file.exists():
            try:
                desc = json.loads(folder_desc_file.read_text())
                ws_info["folder_desc_timestamp"] = desc.get("timestamp")
                ws_info["important_paths_count"] = len(desc.get("paths", []))
                if args.folders:
                    ws_info["important_paths"] = desc.get("paths", [])[:50]
            except:
                pass
        
        results.append(ws_info)
    
    if get_output_format(args) != "text":
        print(fmt(results, args))
    else:
        print(f"Indexing Status ({len(results)} workspaces with retrieval data)")
        print()
        for r in results[:10]:
            folder = r.get("folder", r["workspace_hash"])
            if len(str(folder)) > 50:
                folder = "..." + str(folder)[-47:]
            print(f"\n{folder}")
            print(f"  Embeddable files: {r.get('embeddable_file_count', 0)}")
            print(f"  Important paths: {r.get('important_paths_count', 0)}")
            if args.files and r.get("embeddable_files"):
                print(f"  Files (first 10):")
                for f in r["embeddable_files"][:10]:
                    print(f"    {f}")
            if args.folders and r.get("important_paths"):
                print(f"  Important paths (first 10):")
                for p in r["important_paths"][:10]:
                    print(f"    {p}")

