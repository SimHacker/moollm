# Tool inspection commands: tools, tool-result, thinking, mcp, blobs, checkpoints
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


def cmd_tools(args):
    """List tool calls in a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Extract tool calls from toolFormerData
    tools = []
    for b in bubbles:
        tfd = b.get("toolFormerData")
        if not tfd or not isinstance(tfd, dict):
            continue
        
        name = tfd.get("name", "unknown")
        status = tfd.get("status", "unknown")
        
        # Filter
        if args.status != "all" and status != args.status:
            continue
        if args.name and args.name.lower() not in name.lower():
            continue
        
        tool = {
            "name": name,
            "status": status,
            "timestamp": format_ts(b.get("createdAt", "")),
            "toolCallId": tfd.get("toolCallId", "")[:20],
        }
        
        # Parse args
        try:
            raw_args = json.loads(tfd.get("rawArgs", "{}"))
            tool["args"] = raw_args
        except:
            tool["args"] = tfd.get("rawArgs", "")
        
        if args.verbose:
            # Include result preview
            result = tfd.get("result", "")
            if isinstance(result, str) and len(result) > 200:
                tool["result_preview"] = result[:200] + "..."
            else:
                tool["result"] = result
        
        tools.append(tool)
    
    # Apply limit if specified
    total = len(tools)
    if args.limit:
        tools = tools[:args.limit]
    
    out_fmt = get_output_format(args)
    if out_fmt != "text":
        output_data(tools, out_fmt, "tools",
                   supported=["text", "json", "jsonl", "yaml", "csv", "md"])
    else:
        shown = f" (showing {len(tools)})" if args.limit and args.limit < total else ""
        print(f"Tool calls in {target[:16]}... ({total} calls{shown})")
        print(f"{'TIME':<20} {'STATUS':<10} {'TOOL':<20} ARGS")
        print("─" * 100)
        for t in tools:
            args_str = json.dumps(t["args"]) if isinstance(t["args"], dict) else str(t["args"])
            if len(args_str) > 50:
                args_str = args_str[:47] + "..."
            print(f"{t['timestamp']:<20} {t['status']:<10} {t['name']:<20} {args_str}")
            if args.verbose and t.get("result_preview"):
                print(f"  → {t['result_preview'][:100]}")


def cmd_tool_result(args):
    """Show full tool result content."""
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    row = cur.execute(
        "SELECT key, value FROM cursorDiskKV WHERE key LIKE ?",
        (f"agentKv:blob:{args.blob_hash}%",)
    ).fetchone()
    conn.close()
    
    if not row:
        raise NotFoundError(f"Blob not found: {args.blob_hash}")
    
    k, v = row
    content = decode_blob(v)
    
    try:
        obj = json.loads(content)
        
        # Extract tool result details
        result = {
            "blob_hash": k.replace("agentKv:blob:", "")[:32],
            "size_bytes": len(v),
            "role": obj.get("role"),
        }
        
        # Parse content array
        content_arr = obj.get("content", [])
        for item in content_arr:
            if isinstance(item, dict) and item.get("type") == "tool-result":
                result["tool_name"] = item.get("toolName")
                result["tool_call_id"] = item.get("toolCallId", "")[:40]
                
                # Parse the result text
                tool_result = item.get("result", "")
                if isinstance(tool_result, str):
                    result["result_preview"] = tool_result[:500]
                    result["result_length"] = len(tool_result)
                    
                    # Try to parse if it's JSON
                    try:
                        parsed = json.loads(tool_result)
                        result["result_parsed"] = parsed
                    except:
                        pass
        
        if get_output_format(args) != "text":
            print(fmt(obj, args))
        else:
            print(f"Tool Result: {result.get('tool_name', 'unknown')}")
            print(f"Blob: {result['blob_hash']}...")
            print(f"Size: {result['size_bytes']} bytes")
            print("─" * 60)
            
            if result.get("result_preview"):
                print(result["result_preview"])
                if result.get("result_length", 0) > 500:
                    print(f"\n... ({result['result_length'] - 500} more bytes)")
                    print(f"\nUse --json or --yaml to see full content")
    
    except json.JSONDecodeError:
        print(f"Raw content ({len(content)} bytes):")
        print(content[:2000])


def cmd_thinking(args):
    """Show thinking blocks from a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Extract thinking blocks
    thinking_blocks = []
    for b in bubbles:
        thinking = b.get("thinking")
        if thinking:
            # Thinking can be a dict with 'text' key or a string
            if isinstance(thinking, dict):
                text = thinking.get("text", "")
                signature = thinking.get("signature", "")
            else:
                text = str(thinking)
                signature = ""
            
            if text and len(text) > 20:
                thinking_blocks.append({
                    "timestamp": format_ts(b.get("createdAt", "")),
                    "length": len(text),
                    "text": text,
                    "signature": signature[:50] if signature else "",
                })
    
    # Sort by timestamp and limit
    thinking_blocks.sort(key=lambda x: x["timestamp"])
    thinking_blocks = thinking_blocks[-args.limit:]
    
    if get_output_format(args) != "text":
        print(fmt(thinking_blocks, args))
    else:
        print(f"Thinking blocks in {target[:16]}... ({len(thinking_blocks)} shown)")
        print()
        for t in thinking_blocks:
            print(f"\n💭 {t['timestamp']} ({t['length']} chars)")
            # Wrap text nicely
            text = t["text"]
            if len(text) > 500:
                text = text[:500] + "..."
            print(text)


def cmd_mcp(args):
    """MCP tool call tracing and analysis."""
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    # --servers: list known MCP servers
    if args.servers:
        row = cur.execute("SELECT value FROM ItemTable WHERE key = 'mcpService.knownServerIds'").fetchone()
        if row:
            servers = json.loads(row[0])
            if get_output_format(args) != "text":
                print(fmt({"servers": servers}, args))
            else:
                print(f"Known MCP Servers ({len(servers)}):")
                print("─" * 50)
                for s in servers:
                    # Parse server ID format: user-<name> or project-<n>-<user>-<name>
                    if s.startswith("user-"):
                        name = s[5:]
                        scope = "user"
                    elif s.startswith("project-"):
                        parts = s.split("-", 3)
                        name = parts[3] if len(parts) > 3 else s
                        scope = "project"
                    else:
                        name = s
                        scope = "?"
                    print(f"  [{scope:7}] {name}")
        conn.close()
        return
    
    # Get all MCP tool calls
    rows = cur.execute("SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'").fetchall()
    conn.close()
    
    mcp_calls = []
    for k, v in rows:
        try:
            parts = k.split(":")
            composer_id = parts[1] if len(parts) > 1 else ""
            
            # Filter by composer if specified
            if args.composer and not args.all:
                target = resolve_composer_id(args.composer)
                if target and not composer_id.startswith(target[:8]):
                    continue
            
            obj = json.loads(decode_blob(v))
            tfd = obj.get("toolFormerData", {})
            if not tfd:
                continue
            
            name = tfd.get("name", "")
            if not name.startswith("mcp_"):
                continue
            
            # Parse MCP tool name: mcp_<server>_<tool>
            parts = name.split("_", 2)
            server = parts[1] if len(parts) > 1 else ""
            tool = parts[2] if len(parts) > 2 else ""
            
            call = {
                "timestamp": format_ts(obj.get("createdAt", "")),
                "composer": composer_id[:16],
                "server": server,
                "tool": tool,
                "status": tfd.get("status", "unknown"),
            }
            
            # Parse args
            try:
                raw_args = json.loads(tfd.get("rawArgs", "{}"))
                call["args"] = raw_args
            except:
                call["args"] = {}
            
            # Parse result
            if args.verbose:
                result = tfd.get("result", "")
                if result:
                    try:
                        res = json.loads(result)
                        call["result"] = res
                    except:
                        call["result_preview"] = result[:200]
            
            mcp_calls.append(call)
        except:
            pass
    
    # Sort by timestamp
    mcp_calls.sort(key=lambda x: x.get("timestamp", ""))
    
    if get_output_format(args) != "text":
        print(fmt(mcp_calls, args))
    else:
        scope = f"composer {args.composer[:16]}..." if args.composer else "all conversations"
        print(f"MCP Tool Calls ({len(mcp_calls)}) - {scope}")
        print("─" * 100)
        
        # Group by server
        by_server = {}
        for c in mcp_calls:
            server = c["server"]
            if server not in by_server:
                by_server[server] = []
            by_server[server].append(c)
        
        for server, calls in sorted(by_server.items()):
            print(f"\n🔌 {server} ({len(calls)} calls)")
            for c in calls[-10:]:  # Last 10 per server
                status_icon = "✓" if c["status"] == "completed" else "✗" if c["status"] == "error" else "⋯"
                print(f"  {c['timestamp']} {status_icon} {c['tool']}")
                if args.verbose and c.get("args"):
                    for k, v in list(c["args"].items())[:3]:
                        val = str(v)[:60] if v else ""
                        print(f"      {k}: {val}")
                if args.verbose and c.get("result_preview"):
                    print(f"      → {c['result_preview'][:60]}...")


def cmd_blobs(args):
    """List cached agentKv blobs (tool results)."""
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    if args.show:
        # Show specific blob
        row = cur.execute(
            "SELECT key, value FROM cursorDiskKV WHERE key LIKE ?",
            (f"agentKv:blob:{args.show}%",)
        ).fetchone()
        conn.close()
        
        if not row:
            raise NotFoundError(f"Blob not found: {args.show}")
        
        k, v = row
        content = decode_blob(v)
        try:
            obj = json.loads(content)
            if get_output_format(args) != "text":
                print(fmt(obj, args))
            else:
                print(f"Blob: {k}")
                print(f"Size: {len(v)} bytes")
                print("─" * 60)
                print(json.dumps(obj, indent=2)[:5000])
                if len(content) > 5000:
                    print(f"\n... ({len(content) - 5000} more bytes)")
        except:
            print(f"Raw content ({len(content)} bytes):")
            print(content[:2000])
        return
    
    # List blobs by size
    rows = cur.execute(
        """SELECT key, length(value) FROM cursorDiskKV 
           WHERE key LIKE 'agentKv:blob:%' AND length(value) >= ?
           ORDER BY length(value) DESC LIMIT ?""",
        (args.min_size, args.limit)
    ).fetchall()
    conn.close()
    
    blobs = []
    for k, sz in rows:
        blob_hash = k.replace("agentKv:blob:", "")[:32]
        blobs.append({
            "hash": blob_hash,
            "size_bytes": sz,
            "size_human": f"{sz/1024:.1f}KB" if sz > 1024 else f"{sz}B",
        })
    
    if get_output_format(args) != "text":
        print(fmt(blobs, args))
    else:
        print(f"Agent blobs (>= {args.min_size} bytes, top {args.limit})")
        print(f"{'HASH':<34} {'SIZE':>12}")
        print("─" * 50)
        for b in blobs:
            print(f"{b['hash']:<34} {b['size_human']:>12}")
        print(f"\nUse: cursor-mirror blobs --show <hash> to view content")


def cmd_checkpoints(args):
    """List file checkpoints in a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    # Get all checkpoints for this composer
    rows = cur.execute(
        "SELECT key, value FROM cursorDiskKV WHERE key LIKE ?",
        (f"checkpointId:{target}:%",)
    ).fetchall()
    conn.close()
    
    checkpoints = []
    for k, v in rows:
        parts = k.split(":")
        checkpoint_id = parts[2] if len(parts) > 2 else ""
        
        try:
            obj = json.loads(decode_blob(v))
            files = obj.get("files", [])
            new_folders = obj.get("newlyCreatedFolders", [])
            non_existent = obj.get("nonExistentFiles", [])
            inline_diffs = obj.get("activeInlineDiffs", [])
            
            if files or new_folders or non_existent or inline_diffs or args.verbose:
                cp = {
                    "checkpoint_id": checkpoint_id[:16],
                    "files_modified": len(files),
                    "new_folders": len(new_folders),
                    "deleted_files": len(non_existent),
                    "inline_diffs": len(inline_diffs),
                }
                
                if args.verbose or args.yaml or args.json:
                    cp["files"] = []
                    for f in files:
                        if isinstance(f, dict):
                            path = f.get("path", f.get("uri", str(f)))
                            cp["files"].append(path)
                        else:
                            cp["files"].append(str(f))
                    if new_folders:
                        cp["new_folder_paths"] = new_folders
                    if non_existent:
                        cp["deleted_file_paths"] = non_existent
                
                checkpoints.append(cp)
        except:
            pass
    
    if get_output_format(args) != "text":
        print(fmt(checkpoints, args))
    else:
        print(f"Checkpoints in {target[:16]}... ({len(checkpoints)} with changes)")
        print(f"{'ID':<18} {'FILES':<8} {'NEW':<6} {'DEL':<6} {'DIFFS':<6}")
        print("─" * 50)
        for cp in checkpoints:
            print(f"{cp['checkpoint_id']:<18} {cp['files_modified']:<8} {cp['new_folders']:<6} {cp['deleted_files']:<6} {cp['inline_diffs']:<6}")
            if args.verbose and cp.get("files"):
                for f in cp["files"][:5]:
                    print(f"  → {f}")
                if len(cp.get("files", [])) > 5:
                    print(f"  ... and {len(cp['files']) - 5} more")


def cmd_mcp_tools(args):
    """MCP tool schemas from ~/.cursor."""
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    results = []
    
    for ws in workspaces:
        mcps_dir = os.path.join(ws["path"], "mcps")
        if not os.path.isdir(mcps_dir):
            continue
        
        for server in os.listdir(mcps_dir):
            server_path = os.path.join(mcps_dir, server)
            if not os.path.isdir(server_path):
                continue
            
            if args.server and args.server not in server:
                continue
            
            tools_dir = os.path.join(server_path, "tools")
            prompts_dir = os.path.join(server_path, "prompts")
            
            tools = []
            if os.path.isdir(tools_dir):
                for f in os.listdir(tools_dir):
                    if f.endswith('.json'):
                        tool_path = os.path.join(tools_dir, f)
                        try:
                            with open(tool_path, 'r') as fp:
                                tool_data = json.load(fp)
                            tools.append({
                                "name": tool_data.get("name", f.replace('.json', '')),
                                "description": tool_data.get("description", "")[:100]
                            })
                            
                            if args.show and args.show in tool_data.get("name", ""):
                                if args.yaml:
                                    print(yaml.dump(tool_data, default_flow_style=False))
                                elif args.json:
                                    print(json.dumps(tool_data, indent=2))
                                else:
                                    print(yaml.dump(tool_data, default_flow_style=False))
                                return
                        except:
                            pass
            
            prompts = []
            if os.path.isdir(prompts_dir):
                for f in os.listdir(prompts_dir):
                    if f.endswith('.json'):
                        prompts.append(f.replace('.json', ''))
            
            results.append({
                "workspace": ws["name"],
                "server": server,
                "tools": len(tools),
                "prompts": len(prompts),
                "tool_list": tools
            })
    
    if args.show:
        print(f"Tool not found: {args.show}")
        return
    
    if args.yaml:
        print(yaml.dump(results, default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"MCP Tools ({len(results)} servers)")
        print("-" * 80)
        for r in results:
            print(f"{r['server']:30} | {r['tools']:3} tools | {r['prompts']:2} prompts | {r['workspace'][:30]}")
            for t in r["tool_list"][:5]:
                print(f"    - {t['name']}")


def cmd_agent_tools(args):
    """Cached tool results from ~/.cursor."""
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    if args.show:
        # Show specific tool result
        for ws in workspaces:
            tools_dir = os.path.join(ws["path"], "agent-tools")
            if not os.path.isdir(tools_dir):
                continue
            for f in os.listdir(tools_dir):
                if f.startswith(args.show) and f.endswith('.txt'):
                    tool_path = os.path.join(tools_dir, f)
                    with open(tool_path, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                    print(f"# Tool: {f}")
                    print(f"# Path: {tool_path}")
                    print("-" * 60)
                    print(content)
                    return
        print(f"Tool result not found: {args.show}")
        return
    
    # List all tool results
    results = []
    for ws in workspaces:
        tools_dir = os.path.join(ws["path"], "agent-tools")
        if not os.path.isdir(tools_dir):
            continue
        
        for f in os.listdir(tools_dir):
            if f.endswith('.txt'):
                tool_path = os.path.join(tools_dir, f)
                try:
                    size = os.path.getsize(tool_path)
                    with open(tool_path, 'r', encoding='utf-8') as fp:
                        preview = fp.read(200).replace('\n', ' ')[:100]
                except:
                    size = 0
                    preview = ""
                
                results.append({
                    "uuid": f.replace('.txt', ''),
                    "workspace": ws["name"],
                    "size": size,
                    "preview": preview
                })
    
    results = sorted(results, key=lambda x: -x["size"])[:args.limit]
    
    if args.yaml:
        print(yaml.dump(results, default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"Agent Tools ({len(results)} results)")
        print("-" * 80)
        for r in results:
            print(f"{r['uuid'][:36]} | {r['size']:>8} bytes | {r['preview'][:50]}...")

