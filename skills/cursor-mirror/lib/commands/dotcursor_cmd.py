# Dotcursor and transcript commands
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
import sqlite3

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


def get_dotcursor_workspaces() -> List[Dict[str, Any]]:
    """List all workspace directories in ~/.cursor/projects/"""
    workspaces = []
    if not os.path.isdir(DOTCURSOR_PROJECTS):
        return workspaces
    
    for name in os.listdir(DOTCURSOR_PROJECTS):
        ws_path = os.path.join(DOTCURSOR_PROJECTS, name)
        if not os.path.isdir(ws_path):
            continue
        
        # Calculate size
        total_size = 0
        for root, dirs, files in os.walk(ws_path):
            for f in files:
                try:
                    total_size += os.path.getsize(os.path.join(root, f))
                except:
                    pass
        
        # Count contents
        transcripts = []
        transcript_dir = os.path.join(ws_path, "agent-transcripts")
        if os.path.isdir(transcript_dir):
            transcripts = [f for f in os.listdir(transcript_dir) if f.endswith('.txt') or f.endswith('.json')]
        
        tools = []
        tools_dir = os.path.join(ws_path, "agent-tools")
        if os.path.isdir(tools_dir):
            tools = [f for f in os.listdir(tools_dir) if f.endswith('.txt')]
        
        terminals = []
        term_dir = os.path.join(ws_path, "terminals")
        if os.path.isdir(term_dir):
            terminals = [f for f in os.listdir(term_dir) if f.endswith('.txt')]
        
        workspaces.append({
            "name": name,
            "path": ws_path,
            "size_kb": total_size / 1024,
            "transcripts": len(transcripts),
            "tools": len(tools),
            "terminals": len(terminals),
        })
    
    return sorted(workspaces, key=lambda x: -x["size_kb"])


def resolve_dotcursor_workspace(ref: Optional[str]) -> Optional[str]:
    """Resolve workspace reference to full path in ~/.cursor/projects/"""
    if not ref:
        return None
    
    # Direct path match
    for ws in get_dotcursor_workspaces():
        if ref == ws["name"] or ref in ws["name"]:
            return ws["path"]
    
    return None


def parse_time_filter(time_str: str) -> Optional[int]:
    """Parse time filter like '1h', '30m', '1d' into timestamp."""
    import re
    now = int(time.time() * 1000)
    
    # Relative time
    match = re.match(r'^(\d+)([hmd])$', time_str)
    if match:
        val = int(match.group(1))
        unit = match.group(2)
        if unit == 'h':
            return now - (val * 3600 * 1000)
        elif unit == 'm':
            return now - (val * 60 * 1000)
        elif unit == 'd':
            return now - (val * 86400 * 1000)
    
    # ISO date
    try:
        dt = datetime.fromisoformat(time_str)
        return int(dt.timestamp() * 1000)
    except:
        pass
    
    return None


if __name__ == "__main__":
    sys.exit(cli())


def cmd_dotcursor_status(args):
    """Overview of ~/.cursor directory."""
    result = {
        "path": DOTCURSOR_BASE,
        "exists": os.path.isdir(DOTCURSOR_BASE),
    }
    
    if not result["exists"]:
        print(f"~/.cursor directory not found at: {DOTCURSOR_BASE}")
        return
    
    # Config files
    config_files = {}
    for name in ["argv.json", "mcp.json", "settings.json", "ide_state.json", "unified_repo_list.json"]:
        path = os.path.join(DOTCURSOR_BASE, name)
        if os.path.isfile(path):
            config_files[name] = {
                "size": os.path.getsize(path),
                "exists": True
            }
    result["config_files"] = config_files
    
    # AI tracking
    if os.path.isfile(DOTCURSOR_AI_TRACKING):
        try:
            conn = sqlite3.connect(f"file:{DOTCURSOR_AI_TRACKING}?mode=ro", uri=True)
            cursor = conn.cursor()
            
            ai_tracking = {
                "path": DOTCURSOR_AI_TRACKING,
                "size_mb": os.path.getsize(DOTCURSOR_AI_TRACKING) / (1024 * 1024),
                "tables": {}
            }
            
            for table in ["ai_code_hashes", "scored_commits", "tracking_state", "conversation_summaries"]:
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    ai_tracking["tables"][table] = cursor.fetchone()[0]
                except:
                    pass
            
            # Model breakdown
            try:
                cursor.execute("""
                    SELECT model, COUNT(*) as cnt FROM ai_code_hashes 
                    GROUP BY model ORDER BY cnt DESC LIMIT 5
                """)
                ai_tracking["top_models"] = [{"model": r[0] or "(unknown)", "count": r[1]} for r in cursor.fetchall()]
            except:
                pass
            
            conn.close()
            result["ai_tracking"] = ai_tracking
        except Exception as e:
            result["ai_tracking"] = {"error": str(e)}
    
    # Extensions
    if os.path.isdir(DOTCURSOR_EXTENSIONS):
        ext_json = os.path.join(DOTCURSOR_EXTENSIONS, "extensions.json")
        ext_count = len([d for d in os.listdir(DOTCURSOR_EXTENSIONS) if os.path.isdir(os.path.join(DOTCURSOR_EXTENSIONS, d))])
        result["extensions"] = {
            "path": DOTCURSOR_EXTENSIONS,
            "count": ext_count,
            "manifest_exists": os.path.isfile(ext_json)
        }
    
    # Projects (workspaces)
    workspaces = get_dotcursor_workspaces()
    total_transcripts = sum(ws["transcripts"] for ws in workspaces)
    total_tools = sum(ws["tools"] for ws in workspaces)
    total_size = sum(ws["size_kb"] for ws in workspaces)
    
    result["projects"] = {
        "path": DOTCURSOR_PROJECTS,
        "workspaces": len(workspaces),
        "total_transcripts": total_transcripts,
        "total_tools": total_tools,
        "total_size_mb": total_size / 1024,
        "workspace_list": [{"name": ws["name"], "size_kb": ws["size_kb"], "transcripts": ws["transcripts"]} for ws in workspaces[:10]]
    }
    
    if args.yaml:
        print(yaml.dump(result, default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"~/.cursor Status")
        print("=" * 60)
        print(f"Path: {DOTCURSOR_BASE}")
        print()
        print("Config Files:")
        for name, info in config_files.items():
            print(f"  {name}: {info['size']} bytes")
        print()
        if "ai_tracking" in result:
            ai = result["ai_tracking"]
            if "error" not in ai:
                print(f"AI Tracking: {ai['size_mb']:.1f} MB")
                for table, count in ai.get("tables", {}).items():
                    print(f"  {table}: {count:,} rows")
                if "top_models" in ai:
                    print("  Top models:")
                    for m in ai["top_models"][:3]:
                        print(f"    {m['model']}: {m['count']:,}")
        print()
        print(f"Extensions: {result.get('extensions', {}).get('count', 0)} installed")
        print()
        print(f"Projects: {len(workspaces)} workspaces, {total_transcripts} transcripts, {total_size/1024:.1f} MB")
        for ws in workspaces[:5]:
            print(f"  {ws['name'][:50]}...: {ws['size_kb']:.0f} KB, {ws['transcripts']} transcripts")


def cmd_ai_hashes(args):
    """Query AI code tracking database."""
    if not os.path.isfile(DOTCURSOR_AI_TRACKING):
        print(f"AI tracking database not found: {DOTCURSOR_AI_TRACKING}")
        return
    
    conn = sqlite3.connect(f"file:{DOTCURSOR_AI_TRACKING}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if args.stats:
        # Statistics only
        cursor.execute("SELECT COUNT(*) FROM ai_code_hashes")
        total = cursor.fetchone()[0]
        
        cursor.execute("""
            SELECT source, model, COUNT(*) as cnt 
            FROM ai_code_hashes 
            GROUP BY source, model 
            ORDER BY cnt DESC
        """)
        by_source_model = [dict(r) for r in cursor.fetchall()]
        
        cursor.execute("""
            SELECT fileExtension, COUNT(*) as cnt 
            FROM ai_code_hashes 
            GROUP BY fileExtension 
            ORDER BY cnt DESC LIMIT 10
        """)
        by_ext = [dict(r) for r in cursor.fetchall()]
        
        result = {
            "total": total,
            "by_source_model": by_source_model,
            "by_extension": by_ext
        }
        
        if args.yaml:
            print(yaml.dump(result, default_flow_style=False, sort_keys=False))
        elif args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"AI Code Hashes: {total:,} total")
            print()
            print("By Source/Model:")
            for row in by_source_model[:10]:
                print(f"  {row['source'] or '?'}/{row['model'] or '?'}: {row['cnt']:,}")
            print()
            print("By Extension:")
            for row in by_ext:
                print(f"  .{row['fileExtension'] or '?'}: {row['cnt']:,}")
        return
    
    # Build query
    conditions = []
    params = []
    
    if args.since:
        since_ts = parse_time_filter(args.since)
        if since_ts:
            conditions.append("createdAt >= ?")
            params.append(since_ts)
    
    if args.model:
        conditions.append("model LIKE ?")
        params.append(args.model.replace("*", "%"))
    
    if args.file:
        conditions.append("fileName LIKE ?")
        params.append(f"%{args.file}%")
    
    if args.source:
        conditions.append("source = ?")
        params.append(args.source)
    
    where = " AND ".join(conditions) if conditions else "1=1"
    
    cursor.execute(f"""
        SELECT hash, source, fileExtension, fileName, model, 
               datetime(createdAt/1000, 'unixepoch', 'localtime') as created
        FROM ai_code_hashes
        WHERE {where}
        ORDER BY createdAt DESC
        LIMIT ?
    """, params + [args.limit])
    
    results = [dict(r) for r in cursor.fetchall()]
    conn.close()
    
    if args.yaml:
        print(yaml.dump(results, default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"AI Code Hashes ({len(results)} results)")
        print("-" * 80)
        for r in results:
            fname = r["fileName"] or ""
            fname_short = "..." + fname[-40:] if len(fname) > 40 else fname
            print(f"{r['created']} | {r['source']:8} | {r['model'] or '?':30} | {fname_short}")


def cmd_ai_commits(args):
    """Git commits scored for AI attribution."""
    if not os.path.isfile(DOTCURSOR_AI_TRACKING):
        print(f"AI tracking database not found: {DOTCURSOR_AI_TRACKING}")
        return
    
    conn = sqlite3.connect(f"file:{DOTCURSOR_AI_TRACKING}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    conditions = []
    params = []
    
    if args.since:
        since_ts = parse_time_filter(args.since)
        if since_ts:
            conditions.append("scoredAt >= ?")
            params.append(since_ts)
    
    if args.branch:
        conditions.append("branchName LIKE ?")
        params.append(f"%{args.branch}%")
    
    where = " AND ".join(conditions) if conditions else "1=1"
    
    cursor.execute(f"""
        SELECT commitHash, branchName, 
               datetime(scoredAt/1000, 'unixepoch', 'localtime') as scored
        FROM scored_commits
        WHERE {where}
        ORDER BY scoredAt DESC
        LIMIT ?
    """, params + [args.limit])
    
    results = [dict(r) for r in cursor.fetchall()]
    conn.close()
    
    if args.yaml:
        print(yaml.dump(results, default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"Scored Commits ({len(results)} results)")
        print("-" * 70)
        for r in results:
            print(f"{r['scored']} | {r['commitHash'][:12]} | {r['branchName']}")


def cmd_agent_transcript(args):
    """Read plaintext transcript from ~/.cursor."""
    composer_id = args.composer
    
    # Find transcript file
    transcript_path = None
    transcript_format = args.format
    
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for f in os.listdir(trans_dir):
            if f.startswith(composer_id):
                candidate = os.path.join(trans_dir, f)
                if transcript_format == "auto":
                    # Prefer JSON if available
                    if f.endswith(".json"):
                        transcript_path = candidate
                        transcript_format = "json"
                        break
                    elif f.endswith(".txt") and transcript_path is None:
                        transcript_path = candidate
                        transcript_format = "txt"
                elif transcript_format == "json" and f.endswith(".json"):
                    transcript_path = candidate
                    break
                elif transcript_format == "txt" and f.endswith(".txt"):
                    transcript_path = candidate
                    break
        if transcript_path:
            break
    
    if not transcript_path:
        print(f"Transcript not found for composer: {composer_id}")
        return
    
    # Read and optionally filter
    with open(transcript_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if args.tail:
        lines = content.split('\n')
        content = '\n'.join(lines[-args.tail:])
    elif args.head:
        lines = content.split('\n')
        content = '\n'.join(lines[:args.head])
    
    # Filtering for txt format
    if transcript_format == "txt" and (args.prompts or args.responses or args.tools or args.thinking):
        lines = content.split('\n')
        filtered = []
        in_section = None
        
        for line in lines:
            if line.strip() == "user:":
                in_section = "user"
            elif line.strip() == "assistant:":
                in_section = "assistant"
            elif line.startswith("[Thinking]"):
                in_section = "thinking"
            elif line.startswith("[Tool call]") or line.startswith("[Tool result]"):
                in_section = "tool"
            
            if args.prompts and in_section == "user":
                filtered.append(line)
            elif args.responses and in_section == "assistant":
                filtered.append(line)
            elif args.tools and in_section == "tool":
                filtered.append(line)
            elif args.thinking and in_section == "thinking":
                filtered.append(line)
        
        content = '\n'.join(filtered)
    
    # Output
    if args.yaml or getattr(args, 'json_out', False):
        result = {
            "path": transcript_path,
            "format": transcript_format,
            "lines": len(content.split('\n')),
            "content": content if len(content) < 50000 else content[:50000] + "\n... (truncated)"
        }
        if args.yaml:
            print(yaml.dump(result, default_flow_style=False, sort_keys=False, allow_unicode=True))
        else:
            print(json.dumps(result, indent=2))
    else:
        print(f"# Transcript: {transcript_path}")
        print(f"# Format: {transcript_format}, Lines: {len(content.split(chr(10)))}")
        print("-" * 60)
        print(content)


def cmd_transcript_index(args):
    """Scan transcript and emit line-range pointers for LLM navigation."""
    composer_id = args.composer
    
    # Find transcript file (prefer .txt for line-based indexing)
    transcript_path = None
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
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
        print(f"Transcript not found for composer: {composer_id}")
        return
    
    # Parse type filters
    type_filter = None
    if args.types:
        type_filter = set(args.types.lower().split(','))
    
    # Read and index
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    sections = []
    current = None
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Detect section boundaries
        section_type = None
        summary = None
        
        if stripped == "user:":
            section_type = "user"
            summary = "user prompt"
        elif stripped == "assistant:":
            section_type = "assistant"
            summary = "assistant response"
        elif stripped.startswith("[Thinking]"):
            section_type = "thinking"
            summary = "thinking block"
        elif stripped.startswith("[Tool call]"):
            section_type = "tool"
            # Extract tool name
            parts = stripped.split()
            if len(parts) >= 3:
                summary = f"tool call: {parts[2]}"
            else:
                summary = "tool call"
        elif stripped.startswith("[Tool result]"):
            section_type = "tool_result"
            parts = stripped.split()
            if len(parts) >= 3:
                summary = f"tool result: {parts[2]}"
            else:
                summary = "tool result"
        elif "error" in stripped.lower() or "Error" in stripped:
            if current and current["type"] not in ("error",):
                section_type = "error"
                summary = f"error: {stripped[:60]}..."
        
        # Handle section transitions
        if section_type:
            if current:
                current["end"] = i - 1
                if current["end"] - current["start"] + 1 >= args.min_lines:
                    sections.append(current)
            current = {
                "type": section_type,
                "start": i,
                "end": i,
                "summary": summary
            }
        elif current:
            current["end"] = i
            # Enhance summary with first meaningful content
            if current["type"] == "user" and len(stripped) > 5:
                # Skip XML tags, get actual user text
                if not stripped.startswith('<') and not stripped.startswith('</') and not current.get("content_preview"):
                    current["content_preview"] = stripped[:100]
            elif current["type"] == "assistant" and len(stripped) > 10:
                if not stripped.startswith('[') and not current.get("content_preview"):
                    current["content_preview"] = stripped[:80]
    
    # Close last section
    if current:
        current["end"] = len(lines)
        if current["end"] - current["start"] + 1 >= args.min_lines:
            sections.append(current)
    
    # Apply type filter
    if type_filter:
        sections = [s for s in sections if s["type"] in type_filter]
    
    # Output
    if args.yaml:
        result = {
            "path": transcript_path,
            "total_lines": len(lines),
            "sections": sections
        }
        print(yaml.dump(result, default_flow_style=False, sort_keys=False))
    elif args.json:
        result = {
            "path": transcript_path,
            "total_lines": len(lines),
            "sections": sections
        }
        print(json.dumps(result, indent=2))
    else:
        print(f"# Transcript: {transcript_path}")
        print(f"# Total lines: {len(lines)}, Sections: {len(sections)}")
        print()
        for s in sections:
            preview = s.get("content_preview", "")
            if preview:
                preview = f" | {preview}"
            print(f"{transcript_path}:{s['start']}-{s['end']} # {s['summary']}{preview}")


def cmd_events(args):
    """Scan for actionable events, emit file:line pointers for LLM iteration loop."""
    events = []
    
    # Parse filters
    type_filter = set(args.types.split(',')) if args.types else None
    since_ts = parse_time_filter(args.since) if args.since else None
    severity_order = {"info": 0, "warn": 1, "error": 2}
    min_severity = severity_order.get(args.severity, 0) if args.severity else 0
    
    # Get workspaces
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    # Scan transcripts for events
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            
            # Filter by composer if specified
            if args.composer and not fname.startswith(args.composer):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            
            # Check modification time
            if since_ts:
                mtime = os.path.getmtime(fpath) * 1000
                if mtime < since_ts:
                    continue
            
            # Scan file for events
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
            except:
                continue
            
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                event = None
                
                # Detect actual runtime errors and failures
                # Skip lines that look like code patterns
                is_code_pattern = stripped.startswith('except ') or stripped.startswith('raise ') or \
                          stripped.startswith('+') or stripped.startswith('-') or \
                          stripped.startswith('print(f') or stripped.startswith('old_string:') or \
                          stripped.startswith('new_string:') or 'except ' in stripped.lower()
                
                # Real runtime errors in execution
                if 'NameError:' in line or 'TypeError:' in line or 'SyntaxError:' in line or \
                   'AttributeError:' in line or 'KeyError:' in line or 'IndexError:' in line:
                    event = {
                        "type": "error",
                        "severity": "error",
                        "path": fpath,
                        "line": i,
                        "context": stripped[:120]
                    }
                
                # Tool/command failures
                elif 'FAILED' in line or 'failed with' in line or 'Exit code: 1' in line:
                    if not is_code_pattern:
                        event = {
                            "type": "tool_fail",
                            "severity": "error",
                            "path": fpath,
                            "line": i,
                            "context": stripped[:120]
                        }
                
                # Actual crashes or unhandled issues
                elif 'Traceback' in line or 'crashed' in line.lower():
                    event = {
                        "type": "tool_fail",
                        "severity": "error",
                        "path": fpath,
                        "line": i,
                        "context": stripped[:120]
                    }
                
                # Explicit TODOs in assistant responses
                elif 'TODO:' in line or 'FIXME:' in line:
                    event = {
                        "type": "todo",
                        "severity": "warn",
                        "path": fpath,
                        "line": i,
                        "context": stripped[:120]
                    }
                
                # Incomplete indicators
                elif 'not yet implemented' in line.lower() or 'placeholder' in line.lower():
                    event = {
                        "type": "todo",
                        "severity": "info",
                        "path": fpath,
                        "line": i,
                        "context": stripped[:120]
                    }
                
                # User prompts (for context)
                elif stripped == "user:":
                    # Look ahead for the actual prompt
                    if i + 2 < len(lines):
                        prompt_line = lines[i + 1].strip()
                        if prompt_line.startswith('<user_query>') and i + 2 < len(lines):
                            prompt_text = lines[i + 2].strip()
                        else:
                            prompt_text = prompt_line
                        if prompt_text and not prompt_text.startswith('<'):
                            event = {
                                "type": "prompt",
                                "severity": "info",
                                "path": fpath,
                                "line": i,
                                "end_line": min(i + 10, len(lines)),
                                "context": prompt_text[:100]
                            }
                
                if event:
                    # Apply filters
                    if type_filter and event["type"] not in type_filter:
                        continue
                    if severity_order.get(event["severity"], 0) < min_severity:
                        continue
                    
                    events.append(event)
                    
                    if len(events) >= args.limit:
                        break
            
            if len(events) >= args.limit:
                break
        
        if len(events) >= args.limit:
            break
    
    # Also scan AI tracking for recent activity
    if os.path.isfile(DOTCURSOR_AI_TRACKING) and (not type_filter or "checkpoint" in type_filter):
        try:
            conn = sqlite3.connect(f"file:{DOTCURSOR_AI_TRACKING}?mode=ro", uri=True)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Recent commits that might need review
            cursor.execute("""
                SELECT commitHash, branchName, 
                       datetime(scoredAt/1000, 'unixepoch', 'localtime') as scored
                FROM scored_commits
                ORDER BY scoredAt DESC
                LIMIT 5
            """)
            for row in cursor.fetchall():
                if len(events) >= args.limit:
                    break
                if min_severity <= severity_order["info"]:
                    events.append({
                        "type": "checkpoint",
                        "severity": "info",
                        "source": "ai-tracking",
                        "context": f"commit {row['commitHash'][:12]} on {row['branchName']} ({row['scored']})"
                    })
            conn.close()
        except:
            pass
    
    # Output
    if args.yaml:
        print(yaml.dump({"events": events, "count": len(events)}, default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps({"events": events, "count": len(events)}, indent=2))
    else:
        print(f"# Events: {len(events)}")
        print()
        for e in events:
            sev_icon = {"error": "E", "warn": "W", "info": "I"}.get(e["severity"], "?")
            if "path" in e:
                end = e.get("end_line", e["line"] + 5)
                print(f"[{sev_icon}] {e['path']}:{e['line']}-{end} # {e['type']} | {e['context']}")
            else:
                print(f"[{sev_icon}] {e.get('source', '?')} # {e['type']} | {e['context']}")


def cmd_dotcursor_terminals(args):
    """Terminal state from ~/.cursor."""
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    if args.show:
        # Show specific terminal
        for ws in workspaces:
            term_dir = os.path.join(ws["path"], "terminals")
            if not os.path.isdir(term_dir):
                continue
            for f in os.listdir(term_dir):
                if f.startswith(args.show) or f == f"{args.show}.txt":
                    term_path = os.path.join(term_dir, f)
                    with open(term_path, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                    print(f"# Terminal: {f}")
                    print(f"# Path: {term_path}")
                    print("-" * 60)
                    print(content)
                    return
        print(f"Terminal not found: {args.show}")
        return
    
    # List all terminals
    results = []
    for ws in workspaces:
        term_dir = os.path.join(ws["path"], "terminals")
        if not os.path.isdir(term_dir):
            continue
        
        for f in os.listdir(term_dir):
            if f.endswith('.txt'):
                term_path = os.path.join(term_dir, f)
                try:
                    with open(term_path, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                    # Parse YAML front matter
                    cwd = ""
                    last_cmd = ""
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            try:
                                meta = yaml.safe_load(parts[1])
                                cwd = meta.get("cwd", "")
                                last_cmd = meta.get("last_command", "")
                            except:
                                pass
                except:
                    cwd = ""
                    last_cmd = ""
                
                results.append({
                    "id": f.replace('.txt', ''),
                    "workspace": ws["name"],
                    "cwd": cwd,
                    "last_command": last_cmd
                })
    
    if args.yaml:
        print(yaml.dump(results, default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"Terminals ({len(results)} results)")
        print("-" * 80)
        for r in results:
            print(f"{r['id']:15} | {r['cwd'][:40]:40} | {r['last_command'][:30]}")


def cmd_extensions(args):
    """Cursor extensions from ~/.cursor."""
    ext_json = os.path.join(DOTCURSOR_EXTENSIONS, "extensions.json")
    
    if not os.path.isfile(ext_json):
        print(f"Extensions manifest not found: {ext_json}")
        return
    
    with open(ext_json, 'r') as f:
        extensions = json.load(f)
    
    results = []
    for ext in extensions:
        ident = ext.get("identifier", {})
        meta = ext.get("metadata", {})
        
        results.append({
            "id": ident.get("id", ""),
            "version": ext.get("version", ""),
            "publisher": meta.get("publisherDisplayName", ""),
            "installed": datetime.fromtimestamp(meta.get("installedTimestamp", 0) / 1000).strftime("%Y-%m-%d") if meta.get("installedTimestamp") else "",
            "platform": meta.get("targetPlatform", ""),
        })
    
    # Sort
    if args.sort == "date":
        results.sort(key=lambda x: x["installed"], reverse=True)
    elif args.sort == "name":
        results.sort(key=lambda x: x["id"])
    elif args.sort == "publisher":
        results.sort(key=lambda x: x["publisher"])
    
    if args.limit:
        results = results[:args.limit]
    
    if args.yaml:
        print(yaml.dump(results, default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"Extensions ({len(results)} installed)")
        print("-" * 90)
        for r in results:
            print(f"{r['installed']} | {r['id']:45} | {r['version']:12} | {r['publisher'][:20]}")

