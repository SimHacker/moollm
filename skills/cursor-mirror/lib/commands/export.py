# Export and stats commands
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


def cmd_export_chat(args):
    """Export composer bubbles."""
    composer_id = resolve_composer_id(args.composer)
    if not composer_id:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    debug("cmd_export_chat: exporting %s", composer_id[:8])
    bubbles = load_bubbles(composer_id)
    out = open(args.out, "w", encoding="utf-8") if args.out else sys.stdout
    for b in bubbles:
        print(fmt(b, args), file=out)
    if args.out:
        out.close()
        debug("cmd_export_chat: wrote %d bubbles to %s", len(bubbles), args.out)


def cmd_export_prompts(args):
    """Export prompts/generations for workspace."""
    ws = resolve_workspace(args.workspace)
    if not ws:
        raise NotFoundError(f"Workspace not found: {args.workspace}")
    
    db_path = ws / "state.vscdb"
    conn = open_db(db_path)
    cur = conn.cursor()
    data = {}
    for key in ("aiService.prompts", "aiService.generations"):
        row = cur.execute("SELECT value FROM ItemTable WHERE key=?", (key,)).fetchone()
        if row:
            try:
                data[key] = json.loads(decode_blob(row[0]))
            except:
                data[key] = decode_blob(row[0])
    conn.close()
    
    out = open(args.out, "w", encoding="utf-8") if args.out else sys.stdout
    args.pretty = True  # always pretty for this
    print(fmt(data, args), file=out)
    if args.out:
        out.close()


def cmd_export_markdown(args):
    """Export conversation to readable Markdown."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    bubbles.sort(key=lambda x: x.get("createdAt", ""))
    
    lines = []
    lines.append(f"# Conversation: {target[:16]}...")
    lines.append(f"\n**Messages**: {len(bubbles)}")
    lines.append(f"**Exported**: {datetime.now().isoformat()}")
    lines.append("\n---\n")
    
    for b in bubbles:
        btype = b.get("type")
        text = get_bubble_text(b)
        ts = format_ts(b.get("createdAt", ""))
        
        if btype == 1 and text:
            lines.append(f"\n## 👤 User ({ts})\n")
            lines.append(text)
        
        elif btype == 2:
            # Tool calls
            if args.tools:
                tfd = b.get("toolFormerData")
                if tfd and isinstance(tfd, dict) and tfd.get("name"):
                    name = tfd.get("name")
                    status = tfd.get("status", "?")
                    icon = "✅" if status == "completed" else "❌"
                    lines.append(f"\n> {icon} **Tool**: `{name}`")
                    try:
                        raw_args = json.loads(tfd.get("rawArgs", "{}"))
                        if raw_args:
                            lines.append(f"> Args: `{json.dumps(raw_args)[:100]}`")
                    except:
                        pass
            
            # Thinking
            if args.thinking:
                thinking = b.get("thinking")
                if thinking:
                    if isinstance(thinking, dict):
                        t_text = thinking.get("text", "")
                    else:
                        t_text = str(thinking)
                    if t_text and len(t_text) > 10:
                        lines.append(f"\n<details><summary>💭 Thinking</summary>\n")
                        lines.append(t_text[:500])
                        lines.append("\n</details>\n")
            
            # Text response
            if text:
                lines.append(f"\n## 🤖 Assistant ({ts})\n")
                lines.append(text)
    
    output = "\n".join(lines)
    
    if args.output:
        Path(args.output).write_text(output)
        print(f"Exported to {args.output}")
    else:
        print(output)


def cmd_export_jsonl(args):
    """Export to JSONL for training/analysis."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    bubbles.sort(key=lambda x: x.get("createdAt", ""))
    
    include = set(args.include)
    lines = []
    
    for b in bubbles:
        btype = b.get("type")
        text = get_bubble_text(b)
        ts = b.get("createdAt", "")
        
        # Messages
        if "messages" in include:
            if btype == 1 and text:
                lines.append(json.dumps({
                    "type": "user_message",
                    "timestamp": ts,
                    "content": text
                }))
            elif btype == 2 and text:
                lines.append(json.dumps({
                    "type": "assistant_message",
                    "timestamp": ts,
                    "content": text
                }))
        
        # Tools
        if "tools" in include:
            tfd = b.get("toolFormerData")
            if tfd and isinstance(tfd, dict) and tfd.get("name"):
                try:
                    raw_args = json.loads(tfd.get("rawArgs", "{}"))
                except:
                    raw_args = {}
                lines.append(json.dumps({
                    "type": "tool_call",
                    "timestamp": ts,
                    "tool": tfd.get("name"),
                    "status": tfd.get("status"),
                    "args": raw_args
                }))
        
        # Thinking
        if "thinking" in include:
            thinking = b.get("thinking")
            if thinking:
                if isinstance(thinking, dict):
                    t_text = thinking.get("text", "")
                else:
                    t_text = str(thinking)
                if t_text:
                    lines.append(json.dumps({
                        "type": "thinking",
                        "timestamp": ts,
                        "content": t_text
                    }))
        
        # Context
        if "context" in include:
            ctx = b.get("context")
            if ctx and isinstance(ctx, dict):
                lines.append(json.dumps({
                    "type": "context",
                    "timestamp": ts,
                    "context": ctx
                }))
    
    output = "\n".join(lines)
    if lines:
        output += "\n"  # Trailing newline for proper wc -l count

    if args.output:
        Path(args.output).write_text(output)
        print(f"Exported {len(lines)} records to {args.output}")
    else:
        print(output)


def cmd_models(args):
    """Analyze model usage across conversations."""
    model_stats = {}
    
    for cid, k, obj in iter_bubbles(args.composer):
        model_info = obj.get("modelInfo", {})
        model = model_info.get("modelName", "unknown")
        if model == "unknown" and obj.get("type") != 2:
            continue  # only count assistant messages
        
        if model not in model_stats:
            model_stats[model] = {"count": 0, "composers": set()}
        model_stats[model]["count"] += 1
        model_stats[model]["composers"].add(cid)
    
    # Convert sets to counts for output
    models = [
        {
            "model": m,
            "message_count": s["count"],
            "conversation_count": len(s["composers"]),
        }
        for m, s in sorted(model_stats.items(), key=lambda x: -x[1]["count"])
    ]
    
    if get_output_format(args) != "text":
        print(fmt(models, args))
    else:
        print(f"{'MODEL':<40} {'MESSAGES':>10} {'CHATS':>8}")
        print("─" * 60)
        for m in models:
            print(f"{m['model']:<40} {m['message_count']:>10} {m['conversation_count']:>8}")


def cmd_models_info(args):
    """Model info: config + usage + pricing (JOINs both data stores)."""
    import re
    from collections import defaultdict
    
    show_all = args.all or not (args.usage or args.config or args.migrations)
    
    report = {
        "server_config": {},
        "model_migrations": [],
        "usage_stats": {},
        "transcript_mentions": defaultdict(int),
    }
    
    # 1. Get server config from state.vscdb (ItemTable)
    global_db = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/state.vscdb")
    if os.path.isfile(global_db):
        try:
            conn = sqlite3.connect(f"file:{global_db}?mode=ro", uri=True)
            cursor = conn.cursor()
            
            # Get serverConfig
            cursor.execute("SELECT value FROM ItemTable WHERE key = 'cursorai/serverConfig'")
            row = cursor.fetchone()
            if row:
                server_config = json.loads(row[0])
                
                # Extract model-related config
                if show_all or args.config:
                    report["server_config"] = {
                        "chat_config": {
                            "fullContextTokenLimit": server_config.get("chatConfig", {}).get("fullContextTokenLimit"),
                            "maxRuleLength": server_config.get("chatConfig", {}).get("maxRuleLength"),
                            "maxMcpTools": server_config.get("chatConfig", {}).get("maxMcpTools"),
                        },
                        "config_version": server_config.get("configVersion"),
                        "auto_context": server_config.get("autoContextConfig", {}),
                    }
                
                # Extract model migrations
                if show_all or args.migrations:
                    report["model_migrations"] = server_config.get("modelMigrations", [])
            
            # Get feature config
            cursor.execute("SELECT value FROM ItemTable WHERE key = 'cursorai/featureConfigCache'")
            row = cursor.fetchone()
            if row:
                feature_config = json.loads(row[0])
                report["server_config"]["feature_limits"] = {
                    "readFilesToolMaxLines": feature_config.get("readFilesToolMaxLines"),
                    "readFileToolMaxChars": feature_config.get("readFileToolMaxChars"),
                    "editFileToolMaxFileSizeInLines": feature_config.get("editFileToolMaxFileSizeInLinesBeforeSwitchingToSearchReplace"),
                }
            
            conn.close()
        except Exception as e:
            report["server_config"]["error"] = str(e)
    
    # 2. Get usage stats from ai-code-tracking.db
    if (show_all or args.usage) and os.path.isfile(DOTCURSOR_AI_TRACKING):
        try:
            conn = sqlite3.connect(f"file:{DOTCURSOR_AI_TRACKING}?mode=ro", uri=True)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Get model usage stats
            cursor.execute("""
                SELECT source, model, COUNT(*) as count,
                       MIN(datetime(createdAt/1000, 'unixepoch', 'localtime')) as first_use,
                       MAX(datetime(createdAt/1000, 'unixepoch', 'localtime')) as last_use
                FROM ai_code_hashes
                GROUP BY source, model
                ORDER BY count DESC
            """)
            
            usage = []
            for row in cursor.fetchall():
                usage.append({
                    "source": row["source"],
                    "model": row["model"] or "unknown",
                    "code_blocks": row["count"],
                    "first_use": row["first_use"],
                    "last_use": row["last_use"],
                })
            report["usage_stats"]["by_model"] = usage
            
            # Get extension stats
            cursor.execute("""
                SELECT fileExtension, COUNT(*) as count
                FROM ai_code_hashes
                GROUP BY fileExtension
                ORDER BY count DESC
                LIMIT 15
            """)
            report["usage_stats"]["by_extension"] = [
                {"ext": row[0], "count": row[1]} for row in cursor.fetchall()
            ]
            
            # Get total stats
            cursor.execute("SELECT COUNT(*) FROM ai_code_hashes")
            report["usage_stats"]["total_code_blocks"] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM scored_commits")
            report["usage_stats"]["scored_commits"] = cursor.fetchone()[0]
            
            conn.close()
        except Exception as e:
            report["usage_stats"]["error"] = str(e)
    
    # 3. Scan transcripts for model mentions
    if show_all or args.usage:
        model_pattern = re.compile(r'(claude-[a-z0-9\-_.]+|gpt-[a-z0-9\-_.]+|gemini-[a-z0-9\-_.]+)', re.I)
        
        workspaces = get_dotcursor_workspaces()
        for ws in workspaces[:5]:  # Limit to avoid long scan
            trans_dir = os.path.join(ws["path"], "agent-transcripts")
            if not os.path.isdir(trans_dir):
                continue
            
            for fname in os.listdir(trans_dir)[:10]:  # Sample
                if not fname.endswith('.txt'):
                    continue
                fpath = os.path.join(trans_dir, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    for match in model_pattern.finditer(content):
                        model = match.group(1).lower()
                        report["transcript_mentions"][model] += 1
                except:
                    pass
        
        report["transcript_mentions"] = dict(
            sorted(report["transcript_mentions"].items(), key=lambda x: -x[1])[:20]
        )
    
    # Output
    if args.yaml:
        print(yaml.dump(report, default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps(report, indent=2))
    else:
        print("=" * 70)
        print("📊 MODEL INFO (JOINed from both data stores)")
        print("=" * 70)
        
        if show_all or args.config:
            print("\n⚙️  SERVER CONFIG (from state.vscdb)")
            print("-" * 50)
            cfg = report.get("server_config", {})
            if cfg.get("chat_config"):
                print(f"  Context token limit: {cfg['chat_config'].get('fullContextTokenLimit')}")
                print(f"  Max rule length: {cfg['chat_config'].get('maxRuleLength')}")
                print(f"  Max MCP tools: {cfg['chat_config'].get('maxMcpTools')}")
            if cfg.get("feature_limits"):
                fl = cfg["feature_limits"]
                print(f"  Read file max lines: {fl.get('readFilesToolMaxLines')}")
                print(f"  Read file max chars: {fl.get('readFileToolMaxChars')}")
        
        if show_all or args.migrations:
            print("\n🔄 MODEL MIGRATIONS")
            print("-" * 50)
            for mig in report.get("model_migrations", [])[:5]:
                print(f"  {mig.get('previousModel')} → {mig.get('targetModel')} ({mig.get('modelSetting')})")
            if len(report.get("model_migrations", [])) > 5:
                print(f"  ... and {len(report['model_migrations']) - 5} more")
        
        if show_all or args.usage:
            print("\n📈 USAGE STATS (from ai-code-tracking.db)")
            print("-" * 50)
            stats = report.get("usage_stats", {})
            if stats.get("total_code_blocks"):
                print(f"  Total AI code blocks: {stats['total_code_blocks']:,}")
                print(f"  Scored git commits: {stats.get('scored_commits', 0):,}")
            
            print("\n  By Model:")
            for u in stats.get("by_model", [])[:8]:
                print(f"    {u['source']}/{u['model']}: {u['code_blocks']:,} blocks")
            
            print("\n  By Extension:")
            for e in stats.get("by_extension", [])[:5]:
                print(f"    {e['ext']}: {e['count']:,}")
        
        if show_all:
            print("\n💬 TRANSCRIPT MENTIONS (sampled)")
            print("-" * 50)
            for model, count in list(report.get("transcript_mentions", {}).items())[:10]:
                print(f"  {model}: {count}")
        
        print()


def cmd_stats(args):
    """Summary statistics."""
    # Count bubbles and composers
    bubble_counts = get_bubble_counts()
    total_bubbles = sum(bubble_counts.values())
    total_composers = len(bubble_counts)
    
    # Count workspaces
    workspace_count = sum(1 for _ in iter_workspace_paths())
    
    # DB sizes
    global_size = GLOBAL_DB.stat().st_size if GLOBAL_DB.exists() else 0
    ws_total = sum(
        (ws / "state.vscdb").stat().st_size
        for ws in iter_workspace_paths()
        if (ws / "state.vscdb").exists()
    )
    
    stats = {
        "total_bubbles": total_bubbles,
        "total_composers": total_composers,
        "total_workspaces": workspace_count,
        "global_db_size_mb": round(global_size / 1024 / 1024, 1),
        "workspace_dbs_total_mb": round(ws_total / 1024 / 1024, 1),
    }
    
    if get_output_format(args) != "text":
        print(fmt(stats, args))
    else:
        print("Cursor Chat Statistics")
        print("─" * 40)
        for k, v in stats.items():
            print(f"  {k}: {v}")


def cmd_info(args):
    """Low-level DB inspection."""
    if args.scope == "global":
        db_path = GLOBAL_DB
    else:
        ws = resolve_workspace(args.scope)
        if not ws:
            raise NotFoundError(f"Workspace not found: {args.scope}")
        db_path = ws / "state.vscdb"
    
    conn = open_db(db_path)
    cur = conn.cursor()
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print(f"Tables: {[t[0] for t in tables]}")
    
    print("\nTop ItemTable keys by size:")
    rows = cur.execute(
        "SELECT key, length(value) FROM ItemTable ORDER BY length(value) DESC LIMIT 20"
    ).fetchall()
    for k, size in rows:
        print(f"  {size:>10}  {k}")
    
    conn.close()


# IMAGE COMMANDS


def cmd_diff(args):
    """Show changes between checkpoints."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    # Get all checkpoints for this composer
    pattern = f"checkpointId:{target}:%"
    rows = cur.execute(
        "SELECT key, value FROM cursorDiskKV WHERE key LIKE ? ORDER BY key",
        (pattern,)
    ).fetchall()
    conn.close()
    
    if not rows:
        raise NotFoundError(f"No checkpoints found for {target[:16]}...")
    
    checkpoints = []
    for k, v in rows:
        try:
            obj = json.loads(decode_blob(v))
            parts = k.split(":")
            
            # Extract file paths from files list (each item has uri.path)
            files_data = obj.get("files", [])
            if isinstance(files_data, list):
                file_paths = set()
                for f in files_data:
                    if isinstance(f, dict):
                        uri = f.get("uri", {})
                        path = uri.get("path", uri.get("fsPath", ""))
                        if path:
                            file_paths.add(path)
            else:
                file_paths = set(files_data.keys()) if isinstance(files_data, dict) else set()
            
            checkpoints.append({
                "id": parts[2][:12] if len(parts) > 2 else "",
                "files": file_paths,
                "deleted": set(obj.get("nonExistentFiles", [])),
                "created": set(obj.get("newlyCreatedFolders", [])),
                "raw": obj
            })
        except:
            pass
    
    if len(checkpoints) < 2:
        raise ValidationError("Need at least 2 checkpoints to diff")
    
    from_idx = args.from_idx
    to_idx = args.to_idx if args.to_idx >= 0 else len(checkpoints) - 1
    
    if from_idx >= len(checkpoints) or to_idx >= len(checkpoints):
        raise ValidationError(f"Invalid checkpoint index (max: {len(checkpoints) - 1})")
    
    cp_from = checkpoints[from_idx]
    cp_to = checkpoints[to_idx]
    
    # Compute diffs
    added = cp_to["files"] - cp_from["files"]
    removed = cp_from["files"] - cp_to["files"]
    common = cp_from["files"] & cp_to["files"]
    
    # Check for content changes in common files
    # Build path->content maps
    def get_file_contents(raw_data):
        contents = {}
        files_data = raw_data.get("files", [])
        if isinstance(files_data, list):
            for f in files_data:
                if isinstance(f, dict):
                    uri = f.get("uri", {})
                    path = uri.get("path", uri.get("fsPath", ""))
                    # Content might be in originalModelDiffWrtV0 or elsewhere
                    if path:
                        contents[path] = str(f)  # Use full object as content proxy
        return contents
    
    from_contents = get_file_contents(cp_from["raw"])
    to_contents = get_file_contents(cp_to["raw"])
    
    modified = []
    for f in common:
        if from_contents.get(f) != to_contents.get(f):
            modified.append(f)
    
    result = {
        "from_checkpoint": from_idx,
        "to_checkpoint": to_idx,
        "added": sorted(added),
        "removed": sorted(removed),
        "modified": sorted(modified),
    }
    
    if get_output_format(args) != "text":
        print(fmt(result, args))
    else:
        print(f"Diff: Checkpoint {from_idx} -> {to_idx}")
        print(f"From: {cp_from['id']}  To: {cp_to['id']}")
        print()
        
        if added:
            print(f"➕ Added ({len(added)}):")
            for f in sorted(added)[:20]:
                print(f"  {f}")
        
        if removed:
            print(f"\n➖ Removed ({len(removed)}):")
            for f in sorted(removed)[:20]:
                print(f"  {f}")
        
        if modified:
            print(f"\n📝 Modified ({len(modified)}):")
            for f in sorted(modified)[:20]:
                print(f"  {f}")
        
        if not added and not removed and not modified:
            print("No changes detected between checkpoints.")


def cmd_index(args):
    """Generate searchable index of conversations."""
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    # Get all composers
    rows = cur.execute("SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'").fetchall()
    conn.close()
    
    # Group by composer
    by_composer = {}
    for k, v in rows:
        parts = k.split(":")
        if len(parts) < 2:
            continue
        composer_id = parts[1]
        if composer_id not in by_composer:
            by_composer[composer_id] = []
        try:
            obj = json.loads(decode_blob(v))
            by_composer[composer_id].append(obj)
        except:
            pass
    
    # Build index
    index = {
        "generated": datetime.now().isoformat(),
        "total_conversations": len(by_composer),
        "conversations": []
    }
    
    for composer_id, bubbles in by_composer.items():
        if not bubbles:
            continue
        
        # Sort by timestamp
        bubbles.sort(key=lambda x: x.get("createdAt", ""))
        
        # Extract metadata
        first_ts = bubbles[0].get("createdAt", "") if bubbles else ""
        last_ts = bubbles[-1].get("createdAt", "") if bubbles else ""
        
        user_msgs = [get_bubble_text(b) for b in bubbles if b.get("type") == 1]
        asst_msgs = [get_bubble_text(b) for b in bubbles if b.get("type") == 2]
        
        # Get first user message as title
        title = ""
        for msg in user_msgs:
            if msg and len(msg) > 5:
                title = msg[:100]
                break
        
        # Extract tools used
        tools_used = set()
        for b in bubbles:
            tfd = b.get("toolFormerData", {})
            if tfd and isinstance(tfd, dict):
                name = tfd.get("name")
                if name:
                    tools_used.add(name)
        
        # Extract keywords from first few user messages
        keywords = set()
        for msg in user_msgs[:5]:
            if msg:
                # Simple word extraction
                words = re.findall(r'\b[a-zA-Z]{4,}\b', msg.lower())
                keywords.update(words[:10])
        
        conv = {
            "id": composer_id,
            "title": title,
            "started": format_ts(first_ts),
            "ended": format_ts(last_ts),
            "message_count": len(bubbles),
            "user_messages": len(user_msgs),
            "assistant_messages": len(asst_msgs),
            "tools_used": sorted(tools_used),
            "keywords": sorted(list(keywords)[:20])
        }
        index["conversations"].append(conv)
    
    # Sort by start time
    index["conversations"].sort(key=lambda x: x.get("started", ""), reverse=True)
    
    if get_output_format(args) != "text":
        print(fmt(index, args))
    else:
        # Pretty print
        print(f"Cursor Chat Index")
        print(f"Generated: {index['generated']}")
        print(f"Total Conversations: {index['total_conversations']}")
        print()
        
        for conv in index["conversations"][:20]:
            print(f"\n{conv['id'][:16]}...")
            print(f"  📝 {conv['title'][:60]}...")
            print(f"  📅 {conv['started']} → {conv['ended']}")
            print(f"  💬 {conv['user_messages']} user / {conv['assistant_messages']} assistant")
            if conv['tools_used']:
                print(f"  🔧 {', '.join(conv['tools_used'][:5])}")
    
    if args.output:
        out_path = Path(args.output)
        if out_path.suffix == ".yml" or out_path.suffix == ".yaml":
            out_path.write_text(yaml.dump(index, default_flow_style=False, allow_unicode=True))
        else:
            out_path.write_text(json.dumps(index, indent=2))
        print(f"\nIndex saved to {args.output}")


# Status commands

