#!/usr/bin/env python3
"""
cursor-mirror: See yourself think.

Cursor IDE introspection tool (read-only). macOS validated; Linux/Windows paths
from universal model but not yet tested.

Copyright (c) 2026 Don Hopkins, Leela AI
License: MIT -- see LICENSE file
Part of MOOLLM -- https://github.com/SimHacker/moollm

FOR LLM AGENTS -- READ THIS FIRST

QUICK START:
  cursor-mirror tail @1              # Last messages from CURRENT chat
  cursor-mirror analyze @1           # Stats for current chat
  cursor-mirror tools @1 --limit 10  # Recent tool calls
  cursor-mirror tree                 # Browse all workspaces/composers
  cursor-mirror grep "error"         # Search across ALL chats

REFERENCE SYNTAX (use anywhere a composer/workspace is needed):
  @1, @2, @3     -> By recency (most recent first, like bash !-1)
  fe18, 769a     -> Hash prefix (4+ hex chars)
  moollm         -> Name/folder fragment search
  w1.c2          -> Tree path (workspace 1, composer 2)

WHAT'S WHERE:
  ~/.cursor/                           -> Config, MCP, extensions
  ~/Library/Application Support/Cursor -> Databases (state.vscdb)
  ~/.cursor/projects/*/agent-transcripts/ -> Plaintext chat logs

73 commands organized by function:

  # Workspace/Composer Navigation
  list-workspaces show-workspace list-composers show-composer tree

  # Message Viewing
  tail stream transcript watch

  # Search & Analysis
  grep analyze timeline tgrep

  # Tool & Agent Inspection
  tools tool-result blobs checkpoints thinking mcp mcp-tools agent-tools

  # Context Assembly
  context context-sources request-context searches indexing

  # Files & Todos
  files todos

  # Images
  images image-path image-info image-gallery

  # Export & Stats
  export-chat export-prompts export-markdown export-jsonl
  models models-info stats info diff index

  # Status
  status status-config status-mcp status-models status-features
  status-privacy status-endpoints

  # Database & SQL
  sql dbs tables keys find which

  # ~/.cursor Inspection
  dotcursor-status ai-hashes ai-commits agent-transcript
  transcript-index events dotcursor-terminals extensions

  # Security Audit
  secrets commits scrub deep-snitch exfil-audit pattern-scan
  audit mask-in-place full-audit url-audit

REFERENCE SHORTCUTS:
  @1, @2, @3  -> index by recency (most recent first)
  fe18, 769a  -> hash prefix match (4+ chars)
  moollm      -> name/folder fragment search
  w1.c2       -> tree path (workspace 1, composer 2)

Safe by design: opens SQLite in read-only mode; no writes.

LIBRARY USAGE:
  import sys; sys.path.insert(0, 'path/to/cursor-mirror')
  from lib import resolve_workspace, load_bubbles, get_bubble_text
"""

import argparse
import sys
from pathlib import Path

# Add skill root to path so lib/ is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.paths import GLOBAL_DB, WORKSPACES_ROOT
from lib.debug_util import set_debug, debug
from lib.sources import set_sources_mode, print_sources
from lib.exceptions import CursorMirrorError, NotFoundError, DatabaseError, ValidationError

from lib.commands.workspaces import cmd_list_workspaces, cmd_show_workspace, cmd_tree
from lib.commands.composers_cmd import cmd_list_composers, cmd_show_composer
from lib.commands.messages import cmd_tail, cmd_stream, cmd_transcript, cmd_watch
from lib.commands.search import cmd_grep, cmd_analyze, cmd_timeline, cmd_tgrep
from lib.commands.tools_cmd import (
    cmd_tools, cmd_tool_result, cmd_thinking, cmd_mcp,
    cmd_blobs, cmd_checkpoints, cmd_mcp_tools, cmd_agent_tools,
)
from lib.commands.context_cmd import (
    cmd_context, cmd_context_sources, cmd_request_context,
    cmd_searches, cmd_indexing,
)
from lib.commands.files_todos import cmd_files, cmd_todos
from lib.commands.images import cmd_images, cmd_image_path, cmd_image_info, cmd_image_gallery
from lib.commands.export import (
    cmd_export_chat, cmd_export_prompts, cmd_export_markdown, cmd_export_jsonl,
    cmd_models, cmd_models_info, cmd_stats, cmd_info, cmd_diff, cmd_index,
)
from lib.commands.status_cmd import (
    cmd_status, cmd_status_config, cmd_status_mcp, cmd_status_models,
    cmd_status_features, cmd_status_privacy, cmd_status_endpoints,
)
from lib.commands.db_cmd import cmd_sql, cmd_dbs, cmd_tables, cmd_keys, cmd_find, cmd_which
from lib.commands.audit_cmd import (
    cmd_secrets, cmd_commits, cmd_scrub, cmd_deep_snitch,
    cmd_exfil_audit, cmd_pattern_scan, cmd_audit,
    cmd_mask_in_place, cmd_full_audit, cmd_url_audit,
)
from lib.commands.dotcursor_cmd import (
    cmd_dotcursor_status, cmd_ai_hashes, cmd_ai_commits,
    cmd_agent_transcript, cmd_transcript_index, cmd_events,
    cmd_dotcursor_terminals, cmd_extensions,
)


def main() -> None:
    """CLI entry point. Argparse + dispatch to lib.commands.*"""
    ap = argparse.ArgumentParser(
        prog="cursor-mirror",
        description="See yourself think. Inspect Cursor's internal state (read-only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Run '%(prog)s <command> --help' for command-specific help.",
    )
    ap.add_argument("-d", "--debug", action="store_true",
                    help="Enable verbose debug logging to stderr")
    ap.add_argument("--sources", action="store_true",
                    help="Show data source paths (databases, files) for LLM self-service")
    ap.add_argument("-f", "--output-format", dest="output_format", metavar="FMT",
                    help="Output format: text (default), json, jsonl, yaml, csv, md")
    ap.add_argument("--json", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--yaml", action="store_true", help=argparse.SUPPRESS)

    sub = ap.add_subparsers(dest="cmd", required=True)

    # Workspace/Composer Navigation
    p = sub.add_parser("list-workspaces", help="List workspaces with folder paths and stats")
    p.add_argument("-n", "--limit", type=int, help="Limit results")
    p.add_argument("--sort", "-s", choices=["size", "date", "name", "chats"], default="size")
    p.add_argument("--oldest", action="store_true")
    p.set_defaults(func=cmd_list_workspaces)

    p = sub.add_parser("show-workspace", help="Workspace details")
    p.add_argument("workspace", help="Workspace ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_show_workspace)

    p = sub.add_parser("list-composers", help="List composers (conversations)")
    p.add_argument("workspace", nargs="?", help="Workspace filter")
    p.add_argument("-n", "--limit", type=int, default=50)
    p.add_argument("--sort", "-s", choices=["msgs", "date", "name"], default="msgs")
    p.add_argument("--oldest", action="store_true")
    p.set_defaults(func=cmd_list_composers)

    p = sub.add_parser("show-composer", help="Composer details")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_show_composer)

    p = sub.add_parser("tree", help="Tree navigation (w1, w1.c2, w1.c2.tools)")
    p.add_argument("path", nargs="?")
    p.set_defaults(func=cmd_tree)

    # Message Viewing
    p = sub.add_parser("tail", help="Show recent chat messages")
    p.add_argument("composer", nargs="?")
    p.add_argument("-n", "--limit", type=int, default=20)
    p.add_argument("--tools", action="store_true")
    p.add_argument("--user", action="store_true")
    p.add_argument("--assistant", action="store_true")
    p.add_argument("--all", action="store_true")
    p.add_argument("-p", "--pretty", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=cmd_tail)

    p = sub.add_parser("stream", help="Unified stream of all activity")
    p.add_argument("-n", "--limit", type=int, default=100)
    p.add_argument("--since", help="Time filter: 1h, 30m, 1d")
    p.add_argument("--composer", help="Filter by composerId")
    p.add_argument("--type", choices=["user", "assistant", "all"], default="all")
    p.add_argument("-p", "--pretty", action="store_true")
    p.set_defaults(func=cmd_stream)

    p = sub.add_parser("transcript", help="Readable conversation transcript")
    p.add_argument("composer")
    p.add_argument("--context", action="store_true")
    p.add_argument("--thinking", action="store_true")
    p.add_argument("--markdown", action="store_true")
    p.add_argument("--out", help="Output file")
    p.set_defaults(func=cmd_transcript)

    p = sub.add_parser("watch", help="Watch conversation replay")
    p.add_argument("composer")
    p.add_argument("--speed", type=float, default=1.0)
    p.add_argument("--from-start", action="store_true")
    p.set_defaults(func=cmd_watch)

    # Search & Analysis
    p = sub.add_parser("grep", help="Regex search in chat bubbles")
    p.add_argument("pattern")
    p.add_argument("--composer")
    p.add_argument("-i", "--ignore-case", action="store_true")
    p.add_argument("-v", "--invert-match", action="store_true")
    p.add_argument("-F", "--fixed-strings", action="store_true")
    p.add_argument("-c", "--count", action="store_true")
    p.add_argument("-l", "--composers-only", action="store_true")
    p.add_argument("-C", "--context", type=int, default=0, metavar="N")
    p.add_argument("-n", "--limit", type=int)
    p.add_argument("-p", "--pretty", action="store_true")
    p.set_defaults(func=cmd_grep)

    p = sub.add_parser("analyze", help="Deep analysis of a conversation")
    p.add_argument("composer")
    p.set_defaults(func=cmd_analyze)

    p = sub.add_parser("timeline", help="Chronological timeline")
    p.add_argument("composer")
    p.set_defaults(func=cmd_timeline)

    p = sub.add_parser("tgrep", help="Transcript-aware grep")
    p.add_argument("pattern")
    p.add_argument("files", nargs="*")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("-B", "--before", type=int, default=0)
    p.add_argument("-A", "--after", type=int, default=0)
    p.add_argument("-C", "--context", type=int)
    p.add_argument("--section")
    p.add_argument("--refs-only", action="store_true")
    p.add_argument("--excerpt", action="store_true")
    p.add_argument("--meta", action="store_true")
    p.add_argument("-i", "--ignorecase", action="store_true")
    p.add_argument("-F", "--fixed", action="store_true")
    p.add_argument("-g", "--glob", action="store_true")
    p.add_argument("-w", "--word", action="store_true")
    p.add_argument("--invert", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=50)
    p.set_defaults(func=cmd_tgrep)

    # Tool & Agent Inspection
    p = sub.add_parser("tools", help="List tool calls in a conversation")
    p.add_argument("composer")
    p.add_argument("--status", choices=["all", "completed", "error"], default="all")
    p.add_argument("--name", help="Filter by tool name")
    p.add_argument("-n", "--limit", type=int)
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=cmd_tools)

    p = sub.add_parser("tool-result", help="Show full tool result")
    p.add_argument("blob_hash")
    p.set_defaults(func=cmd_tool_result)

    p = sub.add_parser("thinking", help="Show thinking blocks")
    p.add_argument("composer")
    p.add_argument("-n", "--limit", type=int, default=20)
    p.set_defaults(func=cmd_thinking)

    p = sub.add_parser("mcp", help="MCP tool call tracing")
    p.add_argument("composer", nargs="?")
    p.add_argument("--servers", action="store_true")
    p.add_argument("--all", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=cmd_mcp)

    p = sub.add_parser("blobs", help="List cached agentKv blobs")
    p.add_argument("composer", nargs="?")
    p.add_argument("-n", "--limit", type=int, default=20)
    p.add_argument("--min-size", type=int, default=1000)
    p.add_argument("--show")
    p.set_defaults(func=cmd_blobs)

    p = sub.add_parser("checkpoints", help="List file checkpoints")
    p.add_argument("composer")
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=cmd_checkpoints)

    p = sub.add_parser("mcp-tools", help="MCP tool schemas from ~/.cursor")
    p.add_argument("--workspace")
    p.add_argument("--server")
    p.add_argument("--show")
    p.set_defaults(func=cmd_mcp_tools)

    p = sub.add_parser("agent-tools", help="Cached tool results")
    p.add_argument("composer", nargs="?")
    p.add_argument("--workspace")
    p.add_argument("--show")
    p.add_argument("-n", "--limit", type=int, default=20)
    p.set_defaults(func=cmd_agent_tools)

    # Context Assembly
    p = sub.add_parser("context", help="Show context gathered")
    p.add_argument("composer")
    p.set_defaults(func=cmd_context)

    p = sub.add_parser("context-sources", help="Analyze all context sources")
    p.add_argument("composer")
    p.set_defaults(func=cmd_context_sources)

    p = sub.add_parser("request-context", help="Show assembled context for a message")
    p.add_argument("composer")
    p.add_argument("--message")
    p.set_defaults(func=cmd_request_context)

    p = sub.add_parser("searches", help="Show codebase/web searches")
    p.add_argument("composer")
    p.add_argument("--type", choices=["codebase", "web", "all"], default="all")
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=cmd_searches)

    p = sub.add_parser("indexing", help="Show indexing status")
    p.add_argument("workspace", nargs="?")
    p.add_argument("--files", action="store_true")
    p.add_argument("--folders", action="store_true")
    p.set_defaults(func=cmd_indexing)

    # Files & Todos
    p = sub.add_parser("files", help="Files touched in a conversation")
    p.add_argument("composer")
    p.set_defaults(func=cmd_files)

    p = sub.add_parser("todos", help="Show todos/tasks")
    p.add_argument("composer")
    p.add_argument("--status", choices=["all", "pending", "in_progress", "completed", "cancelled"], default="all")
    p.add_argument("--search")
    p.set_defaults(func=cmd_todos)

    # Images
    p = sub.add_parser("images", help="List cached images")
    p.add_argument("composer", nargs="?")
    p.add_argument("-a", "--all", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=50)
    p.add_argument("--sort", choices=["date", "size", "workspace"], default="date")
    p.set_defaults(func=cmd_images)

    p = sub.add_parser("image-path", help="Get full path to a cached image")
    p.add_argument("ref")
    p.set_defaults(func=cmd_image_path)

    p = sub.add_parser("image-info", help="Show image metadata")
    p.add_argument("ref")
    p.set_defaults(func=cmd_image_info)

    p = sub.add_parser("image-gallery", help="Generate narrated image gallery")
    p.add_argument("-o", "--output")
    p.add_argument("-n", "--limit", type=int, default=100)
    p.add_argument("--sample", type=int, default=10)
    p.add_argument("--workspace")
    p.set_defaults(func=cmd_image_gallery)

    # Export & Stats
    p = sub.add_parser("export-chat", help="Export composer bubbles as JSON/YAML")
    p.add_argument("composer")
    p.add_argument("-o", "--out")
    p.add_argument("-p", "--pretty", action="store_true")
    p.set_defaults(func=cmd_export_chat)

    p = sub.add_parser("export-prompts", help="Export prompts/generations")
    p.add_argument("workspace")
    p.add_argument("-o", "--out")
    p.add_argument("-p", "--pretty", action="store_true")
    p.set_defaults(func=cmd_export_prompts)

    p = sub.add_parser("export-markdown", help="Export to Markdown")
    p.add_argument("composer")
    p.add_argument("-o", "--output")
    p.add_argument("--thinking", action="store_true")
    p.add_argument("--tools", action="store_true")
    p.set_defaults(func=cmd_export_markdown)

    p = sub.add_parser("export-jsonl", help="Export to JSONL")
    p.add_argument("composer")
    p.add_argument("-o", "--output")
    p.add_argument("--include", nargs="+", choices=["messages", "tools", "thinking", "context"],
                   default=["messages", "tools"])
    p.set_defaults(func=cmd_export_jsonl)

    p = sub.add_parser("models", help="Model usage analysis")
    p.add_argument("--composer")
    p.set_defaults(func=cmd_models)

    p = sub.add_parser("models-info", help="Model info: config + usage + pricing")
    p.add_argument("--usage", action="store_true")
    p.add_argument("--config", action="store_true")
    p.add_argument("--migrations", action="store_true")
    p.add_argument("--all", action="store_true")
    p.set_defaults(func=cmd_models_info)

    p = sub.add_parser("stats", help="Summary statistics")
    p.add_argument("composer", nargs="?")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("info", help="Low-level DB inspection")
    p.add_argument("--scope", default="global")
    p.set_defaults(func=cmd_info)

    p = sub.add_parser("diff", help="Show changes between checkpoints")
    p.add_argument("composer")
    p.add_argument("--from", dest="from_idx", type=int, default=0)
    p.add_argument("--to", dest="to_idx", type=int, default=-1)
    p.set_defaults(func=cmd_diff)

    p = sub.add_parser("index", help="Generate searchable index")
    p.add_argument("-o", "--output")
    p.set_defaults(func=cmd_index)

    # Status
    p = sub.add_parser("status", help="Overall Cursor status dashboard")
    p.set_defaults(func=cmd_status)
    p = sub.add_parser("status-config", help="Server configuration and limits")
    p.set_defaults(func=cmd_status_config)
    p = sub.add_parser("status-mcp", help="MCP servers and status")
    p.set_defaults(func=cmd_status_mcp)
    p = sub.add_parser("status-models", help="Available models and migrations")
    p.set_defaults(func=cmd_status_models)
    p = sub.add_parser("status-features", help="Feature flags and experiments")
    p.set_defaults(func=cmd_status_features)
    p = sub.add_parser("status-privacy", help="Privacy settings")
    p.set_defaults(func=cmd_status_privacy)
    p = sub.add_parser("status-endpoints", help="Known API endpoints")
    p.set_defaults(func=cmd_status_endpoints)

    # Database & SQL
    p = sub.add_parser("sql", help="Run SQL query on Cursor databases")
    p.add_argument("query", nargs="?")
    p.add_argument("--db", default="global")
    p.add_argument("--table")
    p.add_argument("--key")
    p.add_argument("--keys")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--raw", action="store_true")
    p.set_defaults(func=cmd_sql)

    p = sub.add_parser("find", help="Find workspaces/composers by name")
    p.add_argument("pattern")
    p.add_argument("--type", "-t", choices=["workspace", "composer", "all"], default="all")
    p.set_defaults(func=cmd_find)

    p = sub.add_parser("which", help="Resolve reference to full details")
    p.add_argument("ref")
    p.add_argument("--type", "-t", choices=["workspace", "composer"], default="workspace")
    p.set_defaults(func=cmd_which)

    p = sub.add_parser("dbs", help="List all databases with sizes")
    p.set_defaults(func=cmd_dbs)

    p = sub.add_parser("tables", help="List tables in a database")
    p.add_argument("--db", default="global")
    p.set_defaults(func=cmd_tables)

    p = sub.add_parser("keys", help="List ItemTable keys with sizes")
    p.add_argument("--db", default="global")
    p.add_argument("--pattern", "-p")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=cmd_keys)

    # ~/.cursor Inspection
    p = sub.add_parser("dotcursor-status", help="Overview of ~/.cursor directory")
    p.add_argument("--workspace")
    p.set_defaults(func=cmd_dotcursor_status)

    p = sub.add_parser("ai-hashes", help="Query AI code tracking database")
    p.add_argument("--since")
    p.add_argument("--model")
    p.add_argument("--file")
    p.add_argument("--source", choices=["composer", "tab"])
    p.add_argument("-n", "--limit", type=int, default=20)
    p.add_argument("--stats", action="store_true")
    p.set_defaults(func=cmd_ai_hashes)

    p = sub.add_parser("ai-commits", help="Git commits scored for AI attribution")
    p.add_argument("--since")
    p.add_argument("--branch")
    p.add_argument("-n", "--limit", type=int, default=20)
    p.set_defaults(func=cmd_ai_commits)

    p = sub.add_parser("agent-transcript", help="Read plaintext transcript from ~/.cursor")
    p.add_argument("composer")
    p.add_argument("--workspace")
    p.add_argument("--tail", type=int)
    p.add_argument("--head", type=int)
    p.add_argument("--prompts", action="store_true")
    p.add_argument("--responses", action="store_true")
    p.add_argument("--tools", action="store_true")
    p.add_argument("--thinking", action="store_true")
    p.add_argument("--format", choices=["auto", "txt", "json"], default="auto")
    p.add_argument("--json-out", action="store_true")
    p.set_defaults(func=cmd_agent_transcript)

    p = sub.add_parser("transcript-index", help="Index a transcript with line-range K-REFs")
    p.add_argument("composer")
    p.add_argument("--workspace")
    p.add_argument("--min-lines", type=int, default=5)
    p.add_argument("--types")
    p.set_defaults(func=cmd_transcript_index)

    p = sub.add_parser("events", help="Scan for actionable events")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--since")
    p.add_argument("--types")
    p.add_argument("--severity", choices=["info", "warn", "error"])
    p.add_argument("-n", "--limit", type=int, default=50)
    p.set_defaults(func=cmd_events)

    p = sub.add_parser("dotcursor-terminals", help="Terminal state from ~/.cursor")
    p.add_argument("--workspace")
    p.add_argument("--show")
    p.set_defaults(func=cmd_dotcursor_terminals)

    p = sub.add_parser("extensions", help="Cursor extensions")
    p.add_argument("--sort", choices=["date", "name", "publisher", "size"], default="date")
    p.add_argument("-n", "--limit", type=int)
    p.set_defaults(func=cmd_extensions)

    # Security Audit
    p = sub.add_parser("secrets", help="Scan for potential secrets/credentials")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--since")
    p.add_argument("-C", "--context", type=int, default=1)
    p.add_argument("--refs-only", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=100)
    p.set_defaults(func=cmd_secrets)

    p = sub.add_parser("commits", help="Find git commits in transcripts")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--refs-only", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=50)
    p.set_defaults(func=cmd_commits)

    p = sub.add_parser("scrub", help="Redact sensitive content (QUIT CURSOR FIRST)")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--pattern")
    p.add_argument("--secrets", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--backup", action="store_true", default=True)
    p.add_argument("--no-backup", action="store_true")
    p.add_argument("--redact-text", default="[REDACTED]")
    p.set_defaults(func=cmd_scrub)

    p = sub.add_parser("deep-snitch", help="Deep security audit")
    p.add_argument("composer", nargs="?")
    p.add_argument("--workspace")
    p.add_argument("--since")
    p.add_argument("--category")
    p.add_argument("--severity", choices=["critical", "high", "medium", "low", "info"])
    p.add_argument("--files", action="store_true")
    p.add_argument("--endpoints", action="store_true")
    p.add_argument("--mcp", action="store_true")
    p.add_argument("--models", action="store_true")
    p.add_argument("--patterns", action="store_true")
    p.add_argument("--all", action="store_true")
    p.add_argument("--summary", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=200)
    p.add_argument("--emit-kref", action="store_true")
    p.set_defaults(func=cmd_deep_snitch)

    p = sub.add_parser("exfil-audit", help="Secret exfiltration audit")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--since")
    p.add_argument("--tool")
    p.add_argument("--summary", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=100)
    p.set_defaults(func=cmd_exfil_audit)

    p = sub.add_parser("pattern-scan", help="Find UUIDs, hashes, secrets")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--pattern")
    p.add_argument("--uuids", action="store_true")
    p.add_argument("--hashes", action="store_true")
    p.add_argument("--secrets", action="store_true")
    p.add_argument("--all", action="store_true")
    p.add_argument("--emit-redact", action="store_true")
    p.add_argument("--emit-sed", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=100)
    p.set_defaults(func=cmd_pattern_scan)

    p = sub.add_parser("audit", help="Composable audit: surfaces x patterns")
    p.add_argument("--surface", action="append", dest="surfaces")
    p.add_argument("--patterns", action="append", dest="pattern_sets")
    p.add_argument("--pattern")
    p.add_argument("--pattern-file")
    p.add_argument("--pattern-type", choices=["regex", "literal", "glob", "fuzzy", "prefix", "suffix", "contains"], default="regex")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--emit-redact", action="store_true")
    p.add_argument("--emit-kref", action="store_true")
    p.add_argument("--mask", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--preserve-ws", action="store_true", default=True)
    p.add_argument("--no-preserve-ws", action="store_true")
    p.add_argument("--cursor-stopped", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=100)
    p.set_defaults(func=cmd_audit)

    p = sub.add_parser("mask-in-place", help="Mask secrets in-place (same length)")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--pattern")
    p.add_argument("--secrets", action="store_true")
    p.add_argument("--uuids", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--mask-char", default="*")
    p.add_argument("--backup", action="store_true", default=True)
    p.add_argument("--no-backup", action="store_true")
    p.add_argument("--cursor-stopped", action="store_true")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_mask_in_place)

    p = sub.add_parser("full-audit", help="Full communication audit -- ALL vectors")
    p.add_argument("--composer")
    p.add_argument("--workspace")
    p.add_argument("--since")
    p.add_argument("--vector")
    p.add_argument("--summary", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=100)
    p.set_defaults(func=cmd_full_audit)

    p = sub.add_parser("url-audit", help="Find URLs in tool calls")
    p.add_argument("composer", nargs="?")
    p.add_argument("--workspace")
    p.add_argument("--pattern")
    p.add_argument("--secrets-only", action="store_true")
    p.add_argument("-n", "--limit", type=int, default=50)
    p.set_defaults(func=cmd_url_audit)

    # Parse and dispatch
    args = ap.parse_args()

    if getattr(args, "debug", False):
        set_debug(True)
        debug("Debug mode enabled")
        debug("Command: %s", args.cmd)

    if getattr(args, "sources", False):
        set_sources_mode(True)

    args.func(args)

    if getattr(args, "sources", False):
        print_sources()


def cli() -> int:
    """CLI wrapper: catches exceptions, returns exit codes."""
    try:
        main()
        return 0
    except NotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValidationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except DatabaseError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except CursorMirrorError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nInterrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(cli())
