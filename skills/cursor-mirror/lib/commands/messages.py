# Message viewing commands: tail, stream, transcript, watch
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


def format_bubble_pretty(obj: Dict[str, Any], verbose: bool = False):
    """Pretty-print a bubble."""
    cid = obj.get("_composer", "?")[:8]
    btype = obj.get("type", "?")
    type_label = {1: "USER", 2: "ASST"}.get(btype, f"T{btype}")
    created = format_ts(obj.get("createdAt", ""))
    text = get_bubble_text(obj)
    
    agent_flag = " 🤖" if obj.get("isAgentic") else ""
    print(f"─── [{cid}] {type_label} {created}{agent_flag} ───")
    
    # Thinking
    thinking = obj.get("thinking")
    if thinking:
        duration = obj.get("thinkingDurationMs", 0)
        # Handle thinking as string or dict
        if isinstance(thinking, dict):
            thinking_text = thinking.get("text", "") or thinking.get("content", "") or str(thinking)
        else:
            thinking_text = str(thinking)
        preview = thinking_text[:150].replace("\n", " ")
        if len(thinking_text) > 150:
            preview += "..."
        print(f"  💭 Thinking ({duration}ms): {preview}")
    
    # Tool calls
    for tc in (obj.get("toolCalls") or [])[:5]:
        name = tc.get("name", "?")
        status = tc.get("status", "")
        print(f"  🔧 {name} [{status}]")
    
    # Tool results
    for tr in (obj.get("toolResults") or [])[:5]:
        success = "✓" if tr.get("success") else "✗"
        output = str(tr.get("output", ""))[:80].replace("\n", "\\n")
        print(f"  📋 {success} {output}")
    
    # Code blocks
    cbs = obj.get("codeBlocks") or []
    if cbs:
        print(f"  📝 {len(cbs)} code blocks")
        if verbose:
            for cb in cbs[:3]:
                lang = cb.get("languageId") or cb.get("language", "?")
                print(f"     [{lang}] {(cb.get('content') or '')[:50]}")
    
    # Text
    if text:
        lines = text.split("\n")
        if len(text) > 300:
            print(f"  {lines[0][:200]}")
            print(f"  ... ({len(text)} chars, {len(lines)} lines)")
        else:
            for line in lines[:8]:
                print(f"  {line}")
            if len(lines) > 8:
                print(f"  ... ({len(lines)-8} more lines)")
    
    print()


def cmd_tail(args):
    """Show recent chat messages (like unix tail for chats).

    Usage:
      tail              # Last 20 messages across ALL chats
      tail @1           # Last 20 messages from most recent chat
      tail fe18 -n 50   # Last 50 from specific composer
      tail --user       # Only user messages
      tail --tools      # Only messages with tool calls

    Empty output? Check: composer exists, has messages, filters aren't too strict.
    """
    # Resolve composer reference (@1, prefix, name) to full ID
    composer_id = None
    if args.composer:
        composer_id = resolve_composer_id(args.composer)
        if not composer_id:
            print(f"Composer not found: {args.composer}", file=sys.stderr)
            return
    
    bubbles = []
    for cid, k, obj in iter_bubbles(composer_id):
        obj["_key"] = k
        obj["_composer"] = cid
        
        btype = obj.get("type")
        if args.user and btype != 1:
            continue
        if args.assistant and btype != 2:
            continue
        if not args.all and not has_content(obj):
            continue
        if args.tools and not (
            obj.get("toolCalls") or obj.get("toolResults") or
            obj.get("isAgentic") or obj.get("codeBlocks") or obj.get("thinking")
        ):
            continue
        
        bubbles.append(obj)
    
    bubbles.sort(key=lambda x: x.get("createdAt") or "", reverse=True)
    bubbles = bubbles[:args.limit]
    bubbles.reverse()
    
    for obj in bubbles:
        if get_output_format(args) != "text":
            print(fmt(obj, args))
        else:
            format_bubble_pretty(obj, verbose=args.verbose)


def cmd_stream(args):
    """Unified stream of all activity sorted by time."""
    since = parse_since(args.since) if args.since else None
    
    items = []
    
    # Gather bubbles
    for cid, k, obj in iter_bubbles(args.composer):
        created = obj.get("createdAt", "")
        if since and created < since:
            continue
        
        btype = obj.get("type")
        if args.type == "user" and btype != 1:
            continue
        if args.type == "assistant" and btype != 2:
            continue
        
        obj["_key"] = k
        obj["_composer"] = cid
        obj["_type"] = "bubble"
        items.append((created, obj))
    
    # Sort by time
    items.sort(key=lambda x: x[0], reverse=True)
    items = items[:args.limit]
    items.reverse()
    
    for ts, obj in items:
        if get_output_format(args) != "text":
            print(fmt(obj, args))
        else:
            format_bubble_pretty(obj, verbose=False)


def cmd_transcript(args):
    """Generate readable conversation transcript."""
    # Find composer
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Build transcript - skip empty bubbles
    transcript = []
    for b in bubbles:
        btype = b.get("type")
        text = get_bubble_text(b)
        thinking = b.get("thinking", "")
        cbs = b.get("codeBlocks", [])
        
        # Skip bubbles with no content
        if not text and not (thinking and len(thinking) > 10) and not cbs:
            continue
        
        created = format_ts(b.get("createdAt", ""))
        
        entry = {
            "role": "user" if btype == 1 else "assistant",
            "timestamp": created,
            "text": text,
        }
        
        # Include model info
        model = b.get("modelInfo", {}).get("modelName")
        if model:
            entry["model"] = model
        
        # Include thinking if requested and non-empty
        if args.thinking and thinking and len(thinking) > 10:
            entry["thinking"] = thinking
            entry["thinking_duration_ms"] = b.get("thinkingDurationMs")
        
        # Include context if requested
        if args.context:
            ctx = b.get("context", {})
            if ctx:
                file_sels = ctx.get("fileSelections", [])
                term_sels = ctx.get("terminalSelections", [])
                selections = ctx.get("selections", [])
                if file_sels or term_sels or selections:
                    entry["context"] = {
                        "file_selections": len(file_sels),
                        "terminal_selections": len(term_sels),
                        "code_selections": len(selections),
                    }
            
            # Include code blocks
            if cbs:
                entry["code_blocks"] = [
                    {"lang": cb.get("languageId"), "path": cb.get("relativePath")}
                    for cb in cbs[:10]
                ]
        
        transcript.append(entry)
    
    out = open(args.out, "w", encoding="utf-8") if args.out else sys.stdout
    
    if get_output_format(args) != "text":
        print(fmt(transcript, args), file=out)
    elif args.markdown:
        # Markdown format
        print(f"# Conversation Transcript\n", file=out)
        print(f"**Composer:** {target}\n", file=out)
        for e in transcript:
            role = "**User**" if e["role"] == "user" else "**Assistant**"
            print(f"### {role} ({e['timestamp']})\n", file=out)
            if e.get("model"):
                print(f"*Model: {e['model']}*\n", file=out)
            if e.get("thinking"):
                print(f"<details><summary>Thinking ({e.get('thinking_duration_ms', 0)}ms)</summary>\n", file=out)
                print(f"```\n{e['thinking'][:2000]}\n```\n</details>\n", file=out)
            if e.get("text"):
                print(f"{e['text']}\n", file=out)
            print("---\n", file=out)
    else:
        # Plain text
        for e in transcript:
            role = "USER" if e["role"] == "user" else "ASST"
            print(f"─── {role} {e['timestamp']} ───")
            if e.get("model"):
                print(f"  [Model: {e['model']}]")
            if e.get("thinking"):
                preview = e["thinking"][:150].replace("\n", " ")
                print(f"  💭 {preview}...")
            if e.get("text"):
                for line in e["text"].split("\n")[:15]:
                    print(f"  {line}")
                if len(e["text"].split("\n")) > 15:
                    print(f"  ... ({len(e['text'])} chars total)")
            print()
    
    if args.out:
        out.close()


def cmd_watch(args):
    """Watch a conversation replay (timeline view)."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Sort by timestamp
    bubbles.sort(key=lambda x: x.get("createdAt", ""))
    
    if not bubbles:
        print("No messages found.")
        return
    
    print(f"Conversation Replay: {target[:24]}...")
    print(f"Messages: {len(bubbles)}")
    print(f"Speed: {args.speed}x (Ctrl+C to stop)")
    print()
    
    prev_time = None
    for b in bubbles:
        btype = b.get("type")
        text = get_bubble_text(b)
        ts_str = b.get("createdAt", "")
        ts = format_ts(ts_str)
        
        # Calculate delay (scaled by speed)
        if prev_time and ts_str:
            try:
                from datetime import datetime
                t1 = datetime.fromisoformat(prev_time.replace("Z", "+00:00"))
                t2 = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                delay = (t2 - t1).total_seconds() / args.speed
                # Cap delay at 5 seconds for practical replay
                delay = min(delay, 5.0)
                if delay > 0.1:
                    time.sleep(delay)
            except:
                pass
        prev_time = ts_str
        
        # Display based on type
        if btype == 1 and text:
            print(f"\n📝 USER [{ts}]")
            print(f"   {text[:200]}{'...' if len(text) > 200 else ''}")
        
        elif btype == 2:
            # Check for tool activity
            tfd = b.get("toolFormerData")
            if tfd and isinstance(tfd, dict) and tfd.get("name"):
                name = tfd.get("name")
                status = tfd.get("status", "?")
                icon = "✓" if status == "completed" else "✗" if status == "error" else "⋯"
                try:
                    raw_args = json.loads(tfd.get("rawArgs", "{}"))
                    args_str = json.dumps(raw_args)[:60]
                except:
                    args_str = str(tfd.get("rawArgs", ""))[:60]
                print(f"   🔧 {icon} {name}: {args_str}")
            
            # Check for thinking
            thinking = b.get("thinking")
            if thinking:
                if isinstance(thinking, dict):
                    t_text = thinking.get("text", "")[:100]
                else:
                    t_text = str(thinking)[:100]
                if t_text:
                    print(f"   💭 {t_text}...")
            
            # Text response
            if text:
                print(f"\n🤖 ASST [{ts}]")
                print(f"   {text[:200]}{'...' if len(text) > 200 else ''}")
    
    print("\n" + "─" * 80)
    print("Replay Complete")

