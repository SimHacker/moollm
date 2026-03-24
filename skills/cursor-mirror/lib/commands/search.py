# Search and analysis commands: grep, analyze, timeline, tgrep
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
from ..exceptions import NotFoundError, ValidationError
from .dotcursor_cmd import get_dotcursor_workspaces
from ..debug_util import debug
from ..sources import register_source


def cmd_grep(args):
    """Grep-like regex search across ALL chat messages.

    Searches the cursorDiskKV bubble store (the live data Cursor uses).
    
    Usage:
      grep "error"              # Case-sensitive search
      grep -i "warning"         # Case-insensitive
      grep "def.*init" -n 20    # Regex, limit 20 results
      grep -F "exact match"     # Fixed string (no regex)
      
    Output format: [composer_prefix] message_preview...
    
    For searching plaintext transcripts instead, use 'tgrep' command.
    With --composer, only that chat is scanned (use hash prefix or full UUID).
    """
    flags = re.IGNORECASE if args.ignore_case else 0
    if args.fixed_strings:
        pattern = re.compile(re.escape(args.pattern), flags)
    else:
        try:
            pattern = re.compile(args.pattern, flags)
        except re.error as e:
            raise ValidationError(f"Invalid regex: {e}")
    
    match_count = 0
    matched_composers = set()

    composer_filter = None
    if args.composer:
        composer_filter = resolve_composer_id(args.composer)
        if not composer_filter:
            raise NotFoundError(f"Composer not found: {args.composer}")

    for cid, k, obj in iter_bubbles(composer_filter):
        text = get_bubble_text(obj)
        found = bool(pattern.search(text))
        if args.invert_match:
            found = not found
        
        if found:
            match_count += 1
            matched_composers.add(cid)

            if args.limit and match_count > args.limit:
                break
            
            if not args.count and not args.composers_only:
                obj["_key"] = k
                obj["_composer"] = cid
                if get_output_format(args) != "text":
                    print(fmt(obj, args))
                else:
                    preview = text[:200] + ("..." if len(text) > 200 else "")
                    print(f"[{cid[:8]}] {preview}")
    
    if args.count:
        print(match_count)
    elif args.composers_only:
        for cid in sorted(matched_composers):
            print(cid)


def cmd_analyze(args):
    """Deep analysis of a conversation - the go-to overview command.

    Shows:
      - Message counts (user vs assistant)
      - Duration and timespan
      - Models used
      - Tool call breakdown (with error counts)
      - Context usage
      
    Usage:
      analyze @1        # Analyze current/most recent chat
      analyze fe18      # Analyze by hash prefix
      analyze --yaml    # Output as YAML for parsing
      
    This is often the first command to run on an unfamiliar composer.
    """
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Gather comprehensive stats
    analysis = {
        "composer_id": target,
        "bubble_count": len(bubbles),
        "user_messages": 0,
        "assistant_messages": 0,
        "with_text": 0,
        "with_thinking": 0,
        "with_tools": 0,
        "with_code_blocks": 0,
        "with_todos": 0,
        "tool_calls": [],
        "tool_summary": {},
        "models_used": {},
        "files_read": set(),
        "files_written": set(),
        "todos_final": [],
        "first_message": None,
        "last_message": None,
        "duration_seconds": 0,
    }
    
    for b in bubbles:
        btype = b.get("type")
        if btype == 1:
            analysis["user_messages"] += 1
        elif btype == 2:
            analysis["assistant_messages"] += 1
        
        if get_bubble_text(b):
            analysis["with_text"] += 1
        
        thinking = b.get("thinking", "")
        if thinking and len(thinking) > 10:
            analysis["with_thinking"] += 1
        
        # Tool calls
        tfd = b.get("toolFormerData")
        if tfd and isinstance(tfd, dict) and tfd.get("name"):
            analysis["with_tools"] += 1
            name = tfd.get("name")
            status = tfd.get("status", "unknown")
            
            analysis["tool_summary"].setdefault(name, {"count": 0, "success": 0, "error": 0})
            analysis["tool_summary"][name]["count"] += 1
            if status == "completed":
                analysis["tool_summary"][name]["success"] += 1
            elif status == "error":
                analysis["tool_summary"][name]["error"] += 1
            
            # Track files (handle v2 tool names too)
            try:
                raw_args = json.loads(tfd.get("rawArgs", "{}"))
                if name in ["read_file", "read_file_v2"]:
                    path = raw_args.get("target_file", raw_args.get("file_path", ""))
                    if path:
                        analysis["files_read"].add(path)
                elif name in ["edit_file", "edit_file_v2", "create_file", "write_file", "write", "search_replace"]:
                    path = raw_args.get("target_file", raw_args.get("file_path", ""))
                    if path:
                        analysis["files_written"].add(path)
            except:
                pass
            
            analysis["tool_calls"].append({
                "name": name,
                "status": status,
                "timestamp": b.get("createdAt", ""),
            })
        
        # Code blocks
        if b.get("codeBlocks"):
            analysis["with_code_blocks"] += 1
        
        # Todos
        todos = b.get("todos", [])
        if todos:
            analysis["with_todos"] += 1
            parsed = []
            for t in todos:
                if isinstance(t, str):
                    try:
                        t = json.loads(t)
                    except:
                        continue
                parsed.append(t)
            if parsed:
                analysis["todos_final"] = parsed
        
        # Models
        model = b.get("modelInfo", {}).get("modelName")
        if model:
            analysis["models_used"].setdefault(model, 0)
            analysis["models_used"][model] += 1
        
        # Timestamps
        created = b.get("createdAt", "")
        if created:
            if not analysis["first_message"]:
                analysis["first_message"] = created
            analysis["last_message"] = created
    
    # Calculate duration
    if analysis["first_message"] and analysis["last_message"]:
        try:
            from datetime import datetime
            t1 = datetime.fromisoformat(analysis["first_message"].replace("Z", "+00:00"))
            t2 = datetime.fromisoformat(analysis["last_message"].replace("Z", "+00:00"))
            analysis["duration_seconds"] = int((t2 - t1).total_seconds())
        except:
            pass
    
    # Convert sets to lists for output
    analysis["files_read"] = sorted(analysis["files_read"])
    analysis["files_written"] = sorted(analysis["files_written"])
    
    if get_output_format(args) != "text":
        print(fmt(analysis, args))
    else:
        print(f"Analysis: {target[:24]}...")
        print(f"\nMessages: {analysis['bubble_count']} total")
        print(f"  User: {analysis['user_messages']}")
        print(f"  Assistant: {analysis['assistant_messages']}")
        print(f"  With text: {analysis['with_text']}")
        print(f"  With thinking: {analysis['with_thinking']}")
        print(f"  With tools: {analysis['with_tools']}")
        print(f"  With code: {analysis['with_code_blocks']}")
        
        print(f"\nDuration: {analysis['duration_seconds']}s")
        print(f"  Start: {format_ts(analysis['first_message'])}")
        print(f"  End: {format_ts(analysis['last_message'])}")
        
        if analysis["models_used"]:
            print(f"\nModels used:")
            for m, c in sorted(analysis["models_used"].items(), key=lambda x: -x[1]):
                print(f"  {c:>4}x {m}")
        
        if analysis["tool_summary"]:
            print(f"\nTool calls ({len(analysis['tool_calls'])} total):")
            for name, stats in sorted(analysis["tool_summary"].items(), key=lambda x: -x[1]["count"]):
                err = f" ({stats['error']} err)" if stats["error"] else ""
                print(f"  {stats['count']:>4}x {name}{err}")
        
        if analysis["files_read"]:
            print(f"\nFiles read ({len(analysis['files_read'])}):")
            for f in analysis["files_read"][:15]:
                print(f"  • {f}")
            if len(analysis["files_read"]) > 15:
                print(f"  ... and {len(analysis['files_read']) - 15} more")
        
        if analysis["files_written"]:
            print(f"\nFiles written ({len(analysis['files_written'])}):")
            for f in analysis["files_written"][:15]:
                print(f"  • {f}")
        
        if analysis["todos_final"]:
            print(f"\nFinal todos ({len(analysis['todos_final'])}):")
            for t in analysis["todos_final"]:
                status = t.get("status", "?")
                icon = {"completed": "✓", "in_progress": "→", "pending": "○"}.get(status, "?")
                print(f"  {icon} {t.get('content', '')[:60]}")


def cmd_timeline(args):
    """Chronological timeline of all activity."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Build timeline entries
    timeline = []
    for b in bubbles:
        ts = b.get("createdAt", "")
        btype = b.get("type")
        text = get_bubble_text(b)
        
        # User message
        if btype == 1 and text:
            timeline.append({
                "timestamp": ts,
                "type": "user_message",
                "preview": text[:100] + ("..." if len(text) > 100 else ""),
            })
        
        # Tool call
        tfd = b.get("toolFormerData")
        if tfd and isinstance(tfd, dict) and tfd.get("name"):
            try:
                raw_args = json.loads(tfd.get("rawArgs", "{}"))
            except:
                raw_args = {}
            timeline.append({
                "timestamp": ts,
                "type": "tool_call",
                "tool": tfd.get("name"),
                "status": tfd.get("status"),
                "args": raw_args,
            })
        
        # Assistant response with text
        if btype == 2 and text:
            timeline.append({
                "timestamp": ts,
                "type": "assistant_message",
                "preview": text[:100] + ("..." if len(text) > 100 else ""),
            })
        
        # Code blocks
        cbs = b.get("codeBlocks", [])
        if cbs:
            for cb in cbs[:5]:
                timeline.append({
                    "timestamp": ts,
                    "type": "code_block",
                    "language": cb.get("languageId") or cb.get("language"),
                    "path": cb.get("relativePath", ""),
                })
        
        # Thinking
        thinking = b.get("thinking", "")
        if thinking and len(thinking) > 10:
            timeline.append({
                "timestamp": ts,
                "type": "thinking",
                "duration_ms": b.get("thinkingDurationMs", 0),
                "preview": thinking[:80] + "...",
            })
    
    # Sort by timestamp
    timeline.sort(key=lambda x: x["timestamp"])
    
    if get_output_format(args) != "text":
        print(fmt(timeline, args))
    else:
        print(f"Timeline for {target[:24]}... ({len(timeline)} events)")
        print("─" * 100)
        for e in timeline:
            ts = format_ts(e["timestamp"])
            etype = e["type"]
            
            if etype == "user_message":
                print(f"{ts}  📝 USER: {e['preview']}")
            elif etype == "assistant_message":
                print(f"{ts}  🤖 ASST: {e['preview']}")
            elif etype == "tool_call":
                args_str = json.dumps(e.get("args", {}))
                if len(args_str) > 50:
                    args_str = args_str[:47] + "..."
                status_icon = "✓" if e.get("status") == "completed" else "✗" if e.get("status") == "error" else "?"
                print(f"{ts}  🔧 {status_icon} {e['tool']}: {args_str}")
            elif etype == "code_block":
                print(f"{ts}  📝 CODE [{e.get('language')}]: {e.get('path', '(inline)')}")
            elif etype == "thinking":
                print(f"{ts}  💭 THINK ({e.get('duration_ms', 0)}ms): {e.get('preview', '')}")


def cmd_tgrep(args):
    """Transcript-aware grep with structured output and section recognition."""
    import re
    import fnmatch
    
    pattern = args.pattern
    flags = re.IGNORECASE if args.ignorecase else 0
    
    # Build matcher based on mode
    if args.fixed:
        # Literal string match
        if args.ignorecase:
            def matcher(line):
                return pattern.lower() in line.lower()
        else:
            def matcher(line):
                return pattern in line
    elif args.glob:
        # Glob/fnmatch pattern
        if args.ignorecase:
            pat_lower = pattern.lower()
            def matcher(line):
                return fnmatch.fnmatch(line.lower(), f"*{pat_lower}*")
        else:
            def matcher(line):
                return fnmatch.fnmatch(line, f"*{pattern}*")
    else:
        # Regex (default)
        if args.word:
            pattern = rf'\b{pattern}\b'
        try:
            regex = re.compile(pattern, flags)
        except re.error as e:
            print(f"Invalid regex: {e}")
            return
        def matcher(line):
            return regex.search(line) is not None
    
    # Invert if requested
    if args.invert:
        orig_matcher = matcher
        def matcher(line):
            return not orig_matcher(line)
    
    before = args.context if args.context else args.before
    after = args.context if args.context else args.after
    
    # Collect files to search
    files_to_search = []
    
    if args.files:
        files_to_search = [os.path.abspath(f) for f in args.files if os.path.isfile(f)]
    else:
        # Default: search transcripts
        workspaces = get_dotcursor_workspaces()
        if args.workspace:
            workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
        
        for ws in workspaces:
            trans_dir = os.path.join(ws["path"], "agent-transcripts")
            if os.path.isdir(trans_dir):
                for fname in os.listdir(trans_dir):
                    if fname.endswith('.txt'):
                        if args.composer and not fname.startswith(args.composer):
                            continue
                        files_to_search.append(os.path.join(trans_dir, fname))
    
    if not files_to_search:
        print("No files to search")
        return
    
    # Section detection patterns
    section_patterns = {
        "user": re.compile(r'^user:\s*$'),
        "assistant": re.compile(r'^assistant:\s*$'),
        "thinking": re.compile(r'^\[Thinking\]'),
        "tool_call": re.compile(r'^\[Tool call\]'),
        "tool_result": re.compile(r'^\[Tool result\]'),
        "user_query": re.compile(r'^<user_query>'),
        "user_query_end": re.compile(r'^</user_query>'),
        "thinking_tag": re.compile(r'^<thinking>'),
        "thinking_tag_end": re.compile(r'^</thinking>'),
        "yaml_start": re.compile(r'^---\s*$'),
        "yaml_block": re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*:\s'),
    }
    
    matches = []
    
    for fpath in files_to_search:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except:
            continue
        
        # Track current section state
        current_section = None
        section_start = 0
        in_tag = None
        in_yaml = False
        
        for i, line in enumerate(lines):
            line_stripped = line.rstrip('\n\r')
            lineno = i + 1  # 1-indexed
            
            # Update section state
            for sec_type, sec_pattern in section_patterns.items():
                if sec_pattern.match(line_stripped):
                    if sec_type == "yaml_start":
                        in_yaml = not in_yaml
                    elif sec_type == "user_query":
                        in_tag = "user_query"
                    elif sec_type == "user_query_end":
                        in_tag = None
                    elif sec_type == "thinking_tag":
                        in_tag = "thinking"
                    elif sec_type == "thinking_tag_end":
                        in_tag = None
                    elif sec_type in ("user", "assistant", "thinking", "tool_call", "tool_result"):
                        current_section = sec_type
                        section_start = lineno
                    break
            
            # Determine effective section
            if in_tag:
                effective_section = in_tag
            elif in_yaml:
                effective_section = "yaml"
            elif current_section:
                effective_section = current_section
            else:
                effective_section = "text"
            
            # Filter by section if specified
            if args.section:
                allowed = args.section.split(',')
                if effective_section not in allowed:
                    continue
            
            # Search for pattern
            if matcher(line_stripped):
                # Calculate excerpt window
                start_line = max(0, i - before)
                end_line = min(len(lines), i + after + 1)
                
                excerpt_lines = []
                if args.excerpt or (not args.refs_only):
                    excerpt_lines = [l.rstrip('\n\r') for l in lines[start_line:end_line]]
                
                match_info = {
                    "path": fpath,
                    "line": lineno,
                    "start": start_line + 1,
                    "end": end_line,
                    "section": effective_section,
                    "match": line_stripped[:200],
                }
                
                if args.meta:
                    match_info["section_start"] = section_start
                    match_info["in_tag"] = in_tag
                    match_info["in_yaml"] = in_yaml
                
                if excerpt_lines:
                    match_info["excerpt"] = excerpt_lines
                
                matches.append(match_info)
                
                if len(matches) >= args.limit:
                    break
        
        if len(matches) >= args.limit:
            break
    
    # Output
    if args.yaml:
        print(yaml.dump({"matches": matches, "count": len(matches)}, 
                       default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps({"matches": matches, "count": len(matches)}, indent=2))
    elif args.refs_only:
        for m in matches:
            print(f"{m['path']}:{m['start']}-{m['end']} # {m['section']} | {m['match'][:80]}")
    else:
        # Rich output with excerpts
        for m in matches:
            print(f"\n{m['path']}:{m['start']}-{m['end']} # {m['section']}")
            if m.get("excerpt"):
                print("-" * 60)
                for j, eline in enumerate(m["excerpt"]):
                    actual_line = m["start"] + j
                    marker = ">>>" if actual_line == m["line"] else "   "
                    print(f"{marker} {actual_line:5d} | {eline[:120]}")
        print(f"\n# Total: {len(matches)} matches")


# Secret patterns for detection
SECRET_PATTERNS = [
    # API Keys
    (r'sk-[a-zA-Z0-9]{20,}', 'openai_key'),
    (r'sk-proj-[a-zA-Z0-9]{20,}', 'openai_project_key'),
    (r'AKIA[0-9A-Z]{16}', 'aws_access_key'),
    (r'(?i)aws[_-]?secret[_-]?access[_-]?key["\s:=]+[A-Za-z0-9/+=]{40}', 'aws_secret'),
    (r'ghp_[a-zA-Z0-9]{36}', 'github_pat'),
    (r'gho_[a-zA-Z0-9]{36}', 'github_oauth'),
    (r'github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}', 'github_fine_grained'),
    (r'glpat-[a-zA-Z0-9\-]{20}', 'gitlab_pat'),
    (r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24}', 'slack_token'),
    (r'(?i)bearer\s+[a-zA-Z0-9\-_.]{20,}', 'bearer_token'),
    
    # Passwords and secrets
    (r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'password'),
    (r'(?i)passwd[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'passwd'),
    (r'(?i)secret[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'secret'),
    (r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'api_key'),
    (r'(?i)auth[_-]?token[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'auth_token'),
    
    # Private keys
    (r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 'private_key'),
    (r'-----BEGIN PGP PRIVATE KEY BLOCK-----', 'pgp_private'),
    
    # Database connection strings
    (r'(?i)mongodb(?:\+srv)?://[^\s]+', 'mongodb_uri'),
    (r'(?i)postgres(?:ql)?://[^\s]+', 'postgres_uri'),
    (r'(?i)mysql://[^\s]+', 'mysql_uri'),
    (r'(?i)redis://[^\s]+', 'redis_uri'),
    
    # Other
    (r'(?i)npm_[a-zA-Z0-9]{36}', 'npm_token'),
    (r'(?i)pypi-[a-zA-Z0-9]{32,}', 'pypi_token'),
    (r'AIza[0-9A-Za-z\-_]{35}', 'google_api_key'),
]

