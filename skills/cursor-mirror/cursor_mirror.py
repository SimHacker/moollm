#!/usr/bin/env python3
"""
cursor-mirror: See yourself think.

Cursor IDE introspection tool (macOS paths, read-only).

Copyright (c) 2026 Don Hopkins, Leela AI
License: MIT — see LICENSE file
Part of MOOLLM — https://github.com/leela-ai/moollm

51 Commands organized by function:

  # Workspace/Composer Navigation
  list-workspaces   Show workspaces with folder paths and stats (w1, w2...)
  show-workspace    Detailed info about a workspace
  list-composers    List composers in a workspace (c1, c2...)
  show-composer     Detailed info about a composer
  tree              Hierarchical navigation (w3.c2.tools)
  
  # Message Viewing
  tail              Show recent chat messages
  stream            Unified stream of all activity
  transcript        Readable conversation transcript
  watch             Watch conversation replay (timeline)
  
  # Search & Analysis  
  grep              Regex search across chat bubbles
  analyze           Deep analysis of a conversation (boot sequence)
  timeline          Chronological timeline of all activity
  
  # Tool & Agent Inspection
  tools             List tool calls in a conversation
  tool-result       Show full tool result content
  blobs             List cached agentKv blobs
  checkpoints       List file checkpoints
  thinking          Show thinking blocks
  mcp               MCP tool call tracing (--servers, --all, -v)
  
  # Context Assembly & Retrieval (NEW!)
  context           Show context gathered in a conversation
  context-sources   Analyze ALL context sources (files, code, terminal, images)
  request-context   Show full assembled context for a message
  searches          Show codebase/web searches with results
  indexing          Show indexing status and embeddable files
  
  # Files & Todos
  files             Files touched in a conversation
  todos             Show todos/tasks from a conversation
  
  # Image Commands (NEW!)
  images            List cached images from chat sessions
  image-path        Get full path to a cached image
  image-info        Show metadata for a cached image
  image-gallery     Generate narrated image gallery markdown
  
  # Export & Stats
  export-chat       Export composer bubbles as JSON/YAML
  export-prompts    Export prompts/generations for workspace
  models            Model usage analysis
  stats             Summary statistics
  info              Low-level DB inspection
  
  # Status Commands
  status            Overall Cursor status dashboard
  status-config     Server configuration and limits
  status-mcp        MCP servers and status
  status-models     Available models and migrations
  status-features   Feature flags and experiments
  status-privacy    Privacy settings and data sharing
  status-endpoints  Known API endpoints
  
  # Database & SQL Commands (NEW!)
  sql               Run SQL queries on Cursor databases
  dbs               List all databases with sizes
  tables            List tables in a database
  keys              List ItemTable keys with sizes
  find              Find workspaces/composers by name
  which             Resolve reference to full details

REFERENCE SHORTCUTS:
  Workspaces and composers can be referenced by:
  - Full UUID/hash:   769a268960457999e3f29ee8bd3bc640
  - Prefix:           769a26 (minimum unique prefix)
  - Index:            @1, @2, @3 (sorted by size/message count)
  - Name fragment:    moollm, SpaceCraft (searches folder/name)
  - Tree path:        w3.c2 (workspace 3, composer 2)
  
  Examples:
    cursor-mirror list-workspaces            # Shows w1, w2, w3...
    cursor-mirror list-composers moollm      # Shows c1, c2, c3... in moollm
    cursor-mirror tree                       # Browse workspaces
    cursor-mirror tree w3                    # Browse composers in w3
    cursor-mirror tree w3.c2                 # Composer details
    cursor-mirror tree w3.c2.tools           # Tool calls in that chat
    cursor-mirror transcript @1              # Largest composer
    cursor-mirror show-workspace moollm
    cursor-mirror sql --db moollm --keys mcp
    cursor-mirror find cursor-mirror

CONTEXT ASSEMBLY SYSTEM:
  Cursor gathers context from multiple sources:
  - fileSelections:     Files attached via @ mentions
  - folderSelections:   Folders attached via @ mentions
  - selections:         Code selections (highlighted text)
  - terminalSelections: Terminal output selections
  - selectedImages:     Pasted/attached images
  - cursorRules:        .cursorrules file content
  - mentions:           All @ mentions in conversation
  - codebase_search:    Semantic search results (vector embeddings)
  - web_search:         Web search results
  
  Indexing files per workspace:
  - embeddable_files.txt:            List of files for vector embedding
  - high_level_folder_description.txt: Important paths for context

Safe by design: opens SQLite in read-only mode; no writes.

Data schemas: DATA-SCHEMAS.yml
Platform paths: MAC-STORAGE.yml, LINUX-STORAGE.yml, WINDOWS-STORAGE.yml

LIBRARY USAGE:
  This module can be imported and used programmatically.
"""
# BEGIN SNIFFABLE REGION
# Read docstring + main() (~650 lines) to understand the full CLI interface.
# Path constants, all 47 commands, reference shortcuts. Sniff here first.

import argparse
import sys
from pathlib import Path

# PATH CONSTANTS (macOS paths; adapt for Linux/Windows)

GLOBAL_DB = Path.home() / "Library/Application Support/Cursor/User/globalStorage/state.vscdb"
WORKSPACES_ROOT = Path.home() / "Library/Application Support/Cursor/User/workspaceStorage"

# Global DB contains:
#   - cursorDiskKV.*  : All chat messages (bubbles), keyed by bubbleId
#   - ItemTable       : Configuration, MCP servers, model migrations, settings
#
# Workspace DBs (state.vscdb in each workspace folder) contain:
#   - composer.composerData : Conversation metadata (name, timestamps, etc.)
#   - aiService.prompts     : What was sent to LLM
#   - Indexing status, file lists, etc.


# CLI INTERFACE (all 47 commands)

def main() -> None:
    """CLI entry point. Defines all commands and their arguments."""
    ap = argparse.ArgumentParser(
        prog="cursor-mirror",
        description="See yourself think. Inspect Cursor's internal state (read-only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  %(prog)s list-workspaces                   # show all workspaces with folders
  %(prog)s show-workspace <hash>             # detailed workspace info
  %(prog)s list-composers                    # list all conversations
  %(prog)s show-composer <uuid>              # composer details
  %(prog)s tail -n 50                        # last 50 messages
  %(prog)s stream --since 1h                 # all activity in last hour
  %(prog)s transcript <composer>             # readable conversation transcript
  %(prog)s files <composer>                  # files touched in conversation
  %(prog)s models                            # model usage analysis
  %(prog)s grep "error" -i                   # search across all chats
  %(prog)s stats                             # summary statistics

Debug mode:
  %(prog)s --debug <command>                 # Enable verbose debug logging
""",
    )
    # Global debug flag
    ap.add_argument("-d", "--debug", action="store_true",
                    help="Enable verbose debug logging to stderr")
    
    sub = ap.add_subparsers(dest="cmd", required=True)

    # ─── list-workspaces ───
    p = sub.add_parser("list-workspaces", help="List workspaces with folder paths and stats")
    p.add_argument("-n", "--limit", type=int, help="Limit results")
    p.add_argument("--sort", "-s", choices=["size", "date", "name", "chats"], default="size",
                   help="Sort by: size (default), date, name, chats")
    p.add_argument("--oldest", action="store_true", help="Oldest first (with --sort date)")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.set_defaults(func=cmd_list_workspaces)

    # ─── show-workspace ───
    p = sub.add_parser("show-workspace", help="Detailed info about a workspace")
    p.add_argument("workspace", help="Workspace hash (or prefix)")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.set_defaults(func=cmd_show_workspace)

    # ─── list-composers ───
    p = sub.add_parser("list-composers", help="List composers (conversations) with metadata")
    p.add_argument("workspace", nargs="?", help="Workspace filter (name, @index, or hash)")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max to show")
    p.add_argument("--sort", "-s", choices=["msgs", "date", "name"], default="msgs",
                   help="Sort by: msgs (default), date, name")
    p.add_argument("--oldest", action="store_true", help="Oldest first (with --sort date)")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.set_defaults(func=cmd_list_composers)

    # ─── tree ───
    p = sub.add_parser("tree", help="Tree navigation with short IDs (w1, w1.c2)")
    p.add_argument("path", nargs="?", help="Path: empty=workspaces, w1=workspace, w1.c2=composer")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_tree)

    # ─── show-composer ───
    p = sub.add_parser("show-composer", help="Detailed info about a composer")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.set_defaults(func=cmd_show_composer)

    # ─── tail ───
    p = sub.add_parser("tail", help="Show recent chat messages")
    p.add_argument("-n", "--lines", type=int, default=20, help="Number of messages")
    p.add_argument("--composer", help="Filter by composerId")
    p.add_argument("--tools", action="store_true", help="Only agent/tool activity")
    p.add_argument("--user", action="store_true", help="Only user messages")
    p.add_argument("--assistant", action="store_true", help="Only assistant messages")
    p.add_argument("--all", action="store_true", help="Include empty bubbles")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.add_argument("-p", "--pretty", action="store_true", help="Pretty-print JSON")
    p.add_argument("-v", "--verbose", action="store_true", help="Show more details")
    p.set_defaults(func=cmd_tail)

    # ─── stream ───
    p = sub.add_parser("stream", help="Unified stream of all activity")
    p.add_argument("-n", "--lines", type=int, default=100, help="Number of items")
    p.add_argument("--since", help="Time filter: 1h, 30m, 1d, 2024-01-15")
    p.add_argument("--composer", help="Filter by composerId")
    p.add_argument("--type", choices=["user", "assistant", "all"], default="all")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.add_argument("-p", "--pretty", action="store_true", help="Pretty-print JSON")
    p.set_defaults(func=cmd_stream)

    # ─── export-chat ───
    p = sub.add_parser("export-chat", help="Export composer bubbles as JSON/YAML")
    p.add_argument("composer", help="Composer UUID (or prefix/name)")
    p.add_argument("-o", "--out", help="Output file (default: stdout)")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("-p", "--pretty", action="store_true", help="Pretty-print JSON")
    p.set_defaults(func=cmd_export_chat)

    # ─── export-prompts ───
    p = sub.add_parser("export-prompts", help="Export prompts/generations for workspace")
    p.add_argument("workspace", help="Workspace hash (or name/prefix)")
    p.add_argument("-o", "--out", help="Output file (default: stdout)")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("-p", "--pretty", action="store_true", help="Pretty-print JSON")
    p.set_defaults(func=cmd_export_prompts)

    # ─── grep ───
    p = sub.add_parser("grep", help="Regex search in chat bubbles")
    p.add_argument("pattern", help="Regex pattern (or literal with -F)")
    p.add_argument("--composer", help="Filter by composerId")
    p.add_argument("-i", "--ignore-case", action="store_true")
    p.add_argument("-v", "--invert-match", action="store_true")
    p.add_argument("-F", "--fixed-strings", action="store_true", help="Literal string match")
    p.add_argument("-c", "--count", action="store_true", help="Count matches only")
    p.add_argument("-l", "--composers-only", action="store_true", help="List matching composers")
    p.add_argument("-C", "--context", type=int, default=0, metavar="N")
    p.add_argument("-n", "--max-results", type=int)
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.add_argument("-p", "--pretty", action="store_true")
    p.set_defaults(func=cmd_grep)

    # ─── transcript ───
    p = sub.add_parser("transcript", help="Readable conversation transcript")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--context", action="store_true", help="Include context (files, selections)")
    p.add_argument("--thinking", action="store_true", help="Include thinking blocks")
    p.add_argument("--markdown", action="store_true", help="Output as Markdown")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.add_argument("--out", help="Output file")
    p.set_defaults(func=cmd_transcript)

    # ─── files ───
    p = sub.add_parser("files", help="Files touched in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_files)

    # ─── models ───
    p = sub.add_parser("models", help="Model usage analysis")
    p.add_argument("--composer", help="Filter by composer")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_models)

    # ─── tools ───
    p = sub.add_parser("tools", help="List tool calls in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--status", choices=["all", "completed", "error"], default="all")
    p.add_argument("--name", help="Filter by tool name")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true", help="Show results/params")
    p.set_defaults(func=cmd_tools)

    # ─── todos ───
    p = sub.add_parser("todos", help="Show todos/tasks from a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_todos)

    # ─── context ───
    p = sub.add_parser("context", help="Show context gathered in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_context)

    # ─── analyze ───
    p = sub.add_parser("analyze", help="Deep analysis of a conversation (boot sequence)")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_analyze)

    # ─── timeline ───
    p = sub.add_parser("timeline", help="Chronological timeline of all activity")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_timeline)

    # ─── checkpoints ───
    p = sub.add_parser("checkpoints", help="List file checkpoints in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true", help="Show all file details")
    p.set_defaults(func=cmd_checkpoints)

    # ─── blobs ───
    p = sub.add_parser("blobs", help="List cached agentKv blobs (tool results)")
    p.add_argument("-n", "--limit", type=int, default=20, help="Number to show")
    p.add_argument("--min-size", type=int, default=1000, help="Min blob size in bytes")
    p.add_argument("--show", help="Show specific blob by hash prefix")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_blobs)

    # ─── tool-result ───
    p = sub.add_parser("tool-result", help="Show full tool result content")
    p.add_argument("blob_hash", help="Blob hash (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_tool_result)

    # ─── thinking ───
    p = sub.add_parser("thinking", help="Show thinking blocks from a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("-n", "--limit", type=int, default=20, help="Number to show")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_thinking)

    # ─── watch ───
    p = sub.add_parser("watch", help="Watch a conversation replay (timeline)")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--speed", type=float, default=1.0, help="Playback speed multiplier")
    p.add_argument("--from-start", action="store_true", help="Start from beginning")
    p.set_defaults(func=cmd_watch)

    # ─── request-context ───
    p = sub.add_parser("request-context", help="Show full context assembled for a message")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--message", help="Message UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_request_context)

    # ─── searches ───
    p = sub.add_parser("searches", help="Show codebase/web searches in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--type", choices=["codebase", "web", "all"], default="all")
    p.add_argument("-v", "--verbose", action="store_true", help="Show result details")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_searches)

    # ─── indexing ───
    p = sub.add_parser("indexing", help="Show indexing status and embeddable files")
    p.add_argument("workspace", nargs="?", help="Workspace hash (or prefix)")
    p.add_argument("--files", action="store_true", help="List embeddable files")
    p.add_argument("--folders", action="store_true", help="Show folder descriptions")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_indexing)

    # ─── context-sources ───
    p = sub.add_parser("context-sources", help="Analyze all context sources in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_context_sources)

    # ─── mcp ───
    p = sub.add_parser("mcp", help="MCP tool call tracing and analysis")
    p.add_argument("composer", nargs="?", help="Composer UUID (or prefix)")
    p.add_argument("--servers", action="store_true", help="List known MCP servers")
    p.add_argument("--all", action="store_true", help="Show all MCP calls globally")
    p.add_argument("-v", "--verbose", action="store_true", help="Show call details")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_mcp)

    # ─── diff ───
    p = sub.add_parser("diff", help="Show changes between checkpoints")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--from", dest="from_idx", type=int, default=0, help="From checkpoint index")
    p.add_argument("--to", dest="to_idx", type=int, default=-1, help="To checkpoint index (-1 = last)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_diff)

    # ─── export-markdown ───
    p = sub.add_parser("export-markdown", help="Export conversation to readable Markdown")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("-o", "--output", help="Output file (default: stdout)")
    p.add_argument("--thinking", action="store_true", help="Include thinking blocks")
    p.add_argument("--tools", action="store_true", help="Include tool calls")
    p.set_defaults(func=cmd_export_markdown)

    # ─── export-jsonl ───
    p = sub.add_parser("export-jsonl", help="Export to JSONL for training/analysis")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("-o", "--output", help="Output file (default: stdout)")
    p.add_argument("--include", nargs="+", choices=["messages", "tools", "thinking", "context"],
                   default=["messages", "tools"], help="What to include")
    p.set_defaults(func=cmd_export_jsonl)

    # ─── index ───
    p = sub.add_parser("index", help="Generate searchable index of conversations")
    p.add_argument("-o", "--output", help="Output directory or file")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_index)

    # ─── STATUS COMMANDS ───
    p = sub.add_parser("status", help="Overall Cursor status dashboard")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("status-config", help="Server configuration and limits")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status_config)

    p = sub.add_parser("status-mcp", help="MCP servers and status")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status_mcp)

    p = sub.add_parser("status-models", help="Available models and migrations")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status_models)

    p = sub.add_parser("status-features", help="Feature flags and experiments")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status_features)

    p = sub.add_parser("status-privacy", help="Privacy settings and data sharing")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status_privacy)

    p = sub.add_parser("status-endpoints", help="Known API endpoints")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status_endpoints)

    # ─── stats ───
    p = sub.add_parser("stats", help="Summary statistics")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_stats)

    # ─── info ───
    p = sub.add_parser("info", help="Low-level DB inspection")
    p.add_argument("--scope", default="global", help="'global' or workspace hash")
    p.set_defaults(func=cmd_info)

    # ─── SQL COMMANDS ───
    p = sub.add_parser("sql", help="Run SQL query on Cursor databases")
    p.add_argument("query", nargs="?", help="SQL query (or use --file)")
    p.add_argument("--db", default="global", help="'global', workspace ref, or path to .vscdb")
    p.add_argument("--table", help="Shortcut: SELECT * FROM <table> LIMIT N")
    p.add_argument("--key", help="Shortcut: get ItemTable value by key")
    p.add_argument("--keys", help="Shortcut: list keys matching pattern (LIKE)")
    p.add_argument("--limit", type=int, default=20, help="Limit rows (default 20)")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.add_argument("--raw", action="store_true", help="Print raw output")
    p.set_defaults(func=cmd_sql)

    p = sub.add_parser("find", help="Find workspaces/composers by name")
    p.add_argument("pattern", help="Search pattern (name fragment, path, etc.)")
    p.add_argument("--type", "-t", choices=["workspace", "composer", "all"], default="all")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_find)

    p = sub.add_parser("which", help="Resolve workspace/composer reference")
    p.add_argument("ref", help="Reference (@1, hash prefix, name fragment)")
    p.add_argument("--type", "-t", choices=["workspace", "composer"], default="workspace")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_which)

    p = sub.add_parser("dbs", help="List all Cursor databases with sizes")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_dbs)

    p = sub.add_parser("tables", help="List tables in a database")
    p.add_argument("--db", default="global", help="'global' or workspace ref")
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_tables)

    p = sub.add_parser("keys", help="List ItemTable keys with sizes")
    p.add_argument("--db", default="global", help="'global' or workspace ref")
    p.add_argument("--pattern", "-p", help="Filter by key pattern (LIKE)")
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--yaml", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_keys)

    # ─── IMAGE COMMANDS ───
    
    # images
    p = sub.add_parser("images", help="List cached images from chat sessions")
    p.add_argument("composer", nargs="?", help="Filter by composer (optional)")
    p.add_argument("-a", "--all", action="store_true", help="Show all images across workspaces")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max images to show")
    p.add_argument("--sort", choices=["date", "size", "workspace"], default="date",
                   help="Sort by: date (default), size, workspace")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.set_defaults(func=cmd_images)
    
    # image-path
    p = sub.add_parser("image-path", help="Get full path to a cached image")
    p.add_argument("ref", help="Image UUID or filename fragment")
    p.set_defaults(func=cmd_image_path)
    
    # image-info
    p = sub.add_parser("image-info", help="Show metadata for a cached image")
    p.add_argument("ref", help="Image UUID or path")
    p.add_argument("--yaml", action="store_true", help="Output as YAML")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.set_defaults(func=cmd_image_info)
    
    # image-gallery
    p = sub.add_parser("image-gallery", help="Generate narrated image gallery markdown")
    p.add_argument("-o", "--output", help="Output file (default: stdout)")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max images")
    p.add_argument("--sample", type=int, default=10, help="Sample N images for narration hints")
    p.add_argument("--workspace", help="Filter to specific workspace")
    p.set_defaults(func=cmd_image_gallery)

    args = ap.parse_args()
    
    # Initialize debug mode if requested
    if getattr(args, 'debug', False):
        set_debug(True)
        debug("Debug mode enabled")
        debug("Command: %s", args.cmd)
    
    args.func(args)

# END SNIFFABLE REGION
# Below is implementation: exceptions, __all__, logging, cli(), helpers, cmd_*.
# Read if debugging, extending, or learning internals.

# Additional imports
import json
import logging
import re
import sqlite3
import time
from datetime import datetime
from typing import List, Dict, Any, Optional, Iterator, Tuple
from urllib.parse import unquote

import yaml

# Exception Classes (import and catch these)

class CursorMirrorError(Exception):
    """Base exception for cursor-mirror errors."""
    pass

class NotFoundError(CursorMirrorError):
    """Entity not found (workspace, composer, etc.)."""
    pass

class DatabaseError(CursorMirrorError):
    """Database access or query error."""
    pass

class ValidationError(CursorMirrorError):
    """Invalid input or argument."""
    pass

# Public API (what to import when using as library)

__all__ = [
    # Exceptions
    "CursorMirrorError", "NotFoundError", "DatabaseError", "ValidationError",
    # Entry points
    "main", "cli",
    # Path constants
    "GLOBAL_DB", "WORKSPACES_ROOT",
    # Core resolution functions
    "resolve_workspace", "resolve_composer", "resolve_composer_id",
    # Workspace/composer access
    "get_workspace_folder", "get_workspace_composers", "get_all_composers", "get_bubble_counts",
    # Bubble access
    "load_bubbles", "iter_bubbles", "get_bubble_text", "has_content",
    # Database access
    "open_db", "get_item_table_value",
    # Utilities
    "decode_blob", "format_ts", "set_debug",
]

# Logging and Debug

log = logging.getLogger("cursor-mirror")
log.setLevel(logging.WARNING)

DEBUG = False

def debug(msg: str, *args: Any) -> None:
    """Log debug message if DEBUG is enabled."""
    if DEBUG:
        log.debug(msg, *args)

def set_debug(enabled: bool) -> None:
    """Enable or disable debug logging."""
    global DEBUG
    DEBUG = enabled
    if enabled:
        log.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter(
            '%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
            datefmt='%H:%M:%S'
        ))
        log.addHandler(handler)

# CLI Wrapper (entry point that handles exceptions)

def cli() -> int:
    """CLI wrapper that catches exceptions and returns exit codes.
    
    Use this as entry point for CLI. Use main() or individual functions
    for programmatic access (they raise exceptions instead of exiting).
    
    Returns:
        0 on success, 1 on error
    """
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


# Helper Functions

def open_db(path: Path) -> sqlite3.Connection:
    """Open SQLite in read-only mode."""
    debug("open_db: %s", path.name if hasattr(path, 'name') else path)
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def decode_blob(raw) -> str:
    """Decode blob to UTF-8 string."""
    b = raw if isinstance(raw, (bytes, bytearray)) else str(raw).encode()
    return b.decode("utf-8", errors="replace")


def fmt(obj: Any, args) -> str:
    """Format object based on args.yaml/args.json/args.pretty."""
    if getattr(args, "yaml", False):
        return yaml.dump(obj, default_flow_style=False, allow_unicode=True, sort_keys=False)
    pretty = getattr(args, "pretty", False)
    if pretty:
        return json.dumps(obj, ensure_ascii=False, indent=2)
    return json.dumps(obj, ensure_ascii=False)


def parse_since(since: str) -> Optional[str]:
    """Parse --since into ISO timestamp.
    
    Accepts: '1h', '30m', '2d', or ISO date string.
    """
    if not since:
        return None
    now = time.time()
    if since.endswith("h"):
        hours = int(since[:-1])
        return datetime.fromtimestamp(now - hours * 3600).isoformat()
    if since.endswith("m"):
        minutes = int(since[:-1])
        return datetime.fromtimestamp(now - minutes * 60).isoformat()
    if since.endswith("d"):
        days = int(since[:-1])
        return datetime.fromtimestamp(now - days * 86400).isoformat()
    # Assume ISO date
    return since


def resolve_workspace(ref: str) -> Optional[Path]:
    """Resolve workspace reference to full path.
    
    Accepts:
      - Hash prefix: "769a26" or full hash
      - Numeric index: "@1", "@2" (1-based, sorted by size desc)
      - Folder name fragment: "moollm", "SpaceCraft"
      - Full path: "/Users/a2deh/GroundUp/Leela/git/moollm"
    """
    if not ref:
        return None
    
    debug("resolve_workspace: ref=%r", ref)
    
    # Index reference (@1, @2, etc.)
    if ref.startswith("@") and ref[1:].isdigit():
        idx = int(ref[1:]) - 1
        workspaces = sorted(
            [ws for ws in WORKSPACES_ROOT.iterdir() if ws.is_dir()],
            key=lambda w: (w / "state.vscdb").stat().st_size if (w / "state.vscdb").exists() else 0,
            reverse=True
        )
        if 0 <= idx < len(workspaces):
            debug("resolve_workspace: index @%d -> %s", idx + 1, workspaces[idx].name[:8])
            return workspaces[idx]
        debug("resolve_workspace: index @%d out of range (%d workspaces)", idx + 1, len(workspaces))
        return None
    
    # Hash prefix match
    for ws in WORKSPACES_ROOT.iterdir():
        if ws.name.startswith(ref):
            debug("resolve_workspace: hash prefix match -> %s", ws.name[:8])
            return ws
    
    # Folder name/path fragment match
    ref_lower = ref.lower()
    matches: List[Tuple[Path, str]] = []
    for ws in WORKSPACES_ROOT.iterdir():
        if not ws.is_dir():
            continue
        folder = get_workspace_folder(ws)
        if folder:
            # Exact path match
            if folder == ref:
                debug("resolve_workspace: exact path match -> %s", ws.name[:8])
                return ws
            # Fragment match
            if ref_lower in folder.lower():
                matches.append((ws, folder))
    
    if len(matches) == 1:
        debug("resolve_workspace: single fragment match -> %s", matches[0][0].name[:8])
        return matches[0][0]
    elif len(matches) > 1:
        # Return the shortest path match (most specific)
        matches.sort(key=lambda x: len(x[1]))
        debug("resolve_workspace: %d matches, using shortest -> %s", len(matches), matches[0][0].name[:8])
        return matches[0][0]
    
    debug("resolve_workspace: no match found")
    return None


def resolve_composer(ref: str, workspace_ref: Optional[str] = None) -> Optional[Tuple[str, Dict[str, Any]]]:
    """Resolve composer reference to (composerId, metadata).
    
    Accepts:
      - UUID or prefix: "9861c0a4" or full UUID
      - Numeric index: "@1", "@2" (1-based, sorted by message count desc)
      - Name fragment: "cursor-mirror", "moollm"
    """
    if not ref:
        return None
    
    debug("resolve_composer: ref=%r workspace=%r", ref, workspace_ref)
    
    # Use cached all-composers if no workspace filter
    if workspace_ref is None:
        composers_meta = get_all_composers()
    else:
        # Filter by workspace
        target_ws = resolve_workspace(workspace_ref)
        if not target_ws:
            debug("resolve_composer: workspace not found: %s", workspace_ref)
            return None
        
        bubble_counts = get_bubble_counts()
        composers_meta = {}
        for c in get_workspace_composers(target_ws):
            cid = c.get("composerId")
            if cid:
                composers_meta[cid] = c.copy()
                composers_meta[cid]["_workspace"] = target_ws.name
                composers_meta[cid]["_bubble_count"] = bubble_counts.get(cid, 0)
    
    debug("resolve_composer: %d composers to search", len(composers_meta))
    
    # Index reference (@1, @2, etc.)
    if ref.startswith("@") and ref[1:].isdigit():
        idx = int(ref[1:]) - 1
        sorted_composers = sorted(
            composers_meta.items(),
            key=lambda x: x[1].get("_bubble_count", 0),
            reverse=True
        )
        if 0 <= idx < len(sorted_composers):
            cid, meta = sorted_composers[idx]
            debug("resolve_composer: index @%d -> %s", idx + 1, cid[:8])
            return (cid, meta)
        debug("resolve_composer: index @%d out of range", idx + 1)
        return None
    
    # UUID prefix match
    for cid, meta in composers_meta.items():
        if cid.startswith(ref):
            debug("resolve_composer: UUID prefix match -> %s", cid[:8])
            return (cid, meta)
    
    # Name fragment match
    ref_lower = ref.lower()
    matches: List[Tuple[str, Dict[str, Any]]] = []
    for cid, meta in composers_meta.items():
        name = meta.get("name", "") or ""
        if ref_lower in name.lower():
            matches.append((cid, meta))
    
    if len(matches) == 1:
        debug("resolve_composer: single name match -> %s", matches[0][0][:8])
        return matches[0]
    elif len(matches) > 1:
        # Return highest message count
        matches.sort(key=lambda x: x[1].get("_bubble_count", 0), reverse=True)
        debug("resolve_composer: %d name matches, using highest count -> %s", len(matches), matches[0][0][:8])
        return matches[0]
    
    debug("resolve_composer: no match found")
    return None


def get_workspace_folder(ws_path: Path) -> Optional[str]:
    """Get folder path from workspace.json."""
    ws_json = ws_path / "workspace.json"
    if ws_json.exists():
        try:
            data = json.loads(ws_json.read_text())
            folder = data.get("folder", "")
            if folder.startswith("file://"):
                return unquote(folder[7:])
            return folder
        except (json.JSONDecodeError, OSError, KeyError):
            pass
    return None


# Module-level cache for workspace composers (keyed by workspace path string)
_composers_cache: Dict[str, List[Dict[str, Any]]] = {}

def get_workspace_composers(ws_path: Path) -> List[Dict[str, Any]]:
    """Get composers from workspace state.vscdb.
    
    Cached for duration of CLI run.
    """
    cache_key = str(ws_path)
    if cache_key in _composers_cache:
        debug("get_workspace_composers: cache hit for %s", ws_path.name[:8])
        return _composers_cache[cache_key]
    
    debug("get_workspace_composers: loading from %s", ws_path.name[:8])
    db_path = ws_path / "state.vscdb"
    if not db_path.exists():
        _composers_cache[cache_key] = []
        return []
    
    conn = open_db(db_path)
    cur = conn.cursor()
    row = cur.execute("SELECT value FROM ItemTable WHERE key='composer.composerData'").fetchone()
    conn.close()
    
    if not row:
        _composers_cache[cache_key] = []
        return []
    
    data = json.loads(decode_blob(row[0]))
    composers = data.get("allComposers", [])
    if isinstance(composers, dict):
        composers = list(composers.values())
    elif not isinstance(composers, list):
        composers = []
    
    _composers_cache[cache_key] = composers
    debug("get_workspace_composers: cached %d composers for %s", len(composers), ws_path.name[:8])
    return composers


def iter_bubbles(composer_id: Optional[str] = None) -> Iterator[Tuple[str, str, Dict[str, Any]]]:
    """Yield (composer_id, bubble_key, bubble_dict) for all bubbles."""
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    if composer_id:
        rows = cur.execute(
            "SELECT key, value FROM cursorDiskKV WHERE key LIKE ?",
            (f"bubbleId:{composer_id}:%",),
        ).fetchall()
    else:
        rows = cur.execute(
            "SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'"
        ).fetchall()
    conn.close()
    for k, v in rows:
        try:
            obj = json.loads(decode_blob(v))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(obj, dict):
            continue
        parts = k.split(":")
        cid = parts[1] if len(parts) >= 2 else "unknown"
        yield cid, k, obj


def load_bubbles(composer_id: str) -> List[Dict[str, Any]]:
    """Load all bubbles for a composer, sorted by createdAt."""
    bubbles = []
    for cid, k, obj in iter_bubbles(composer_id):
        obj["_key"] = k
        bubbles.append(obj)
    bubbles.sort(key=lambda x: x.get("createdAt") or "")
    return bubbles


def get_bubble_text(obj: Dict[str, Any]) -> str:
    """Extract text content from a bubble."""
    return obj.get("text") or obj.get("content") or ""


def has_content(obj: Dict[str, Any]) -> bool:
    """Check if bubble has meaningful content."""
    return bool(
        get_bubble_text(obj) or
        obj.get("toolCalls") or
        obj.get("toolResults") or
        obj.get("codeBlocks") or
        obj.get("thinking")
    )


def format_ts(ts: Any) -> str:
    """Format timestamp for display."""
    if isinstance(ts, str):
        return ts[:19].replace("T", " ")
    if isinstance(ts, (int, float)):
        return datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S")
    return str(ts)


# Module-level cache for bubble counts (populated once per CLI run)
_bubble_counts_cache: Optional[Dict[str, int]] = None

def get_bubble_counts() -> Dict[str, int]:
    """Get message counts per composer from global DB.
    
    Cached for duration of CLI run (no TTL needed - CLI exits quickly).
    """
    global _bubble_counts_cache
    if _bubble_counts_cache is not None:
        debug("get_bubble_counts: returning cached (%d composers)", len(_bubble_counts_cache))
        return _bubble_counts_cache
    
    debug("get_bubble_counts: loading from DB...")
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    rows = cur.execute("SELECT key FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'").fetchall()
    conn.close()
    
    counts: Dict[str, int] = {}
    for (k,) in rows:
        parts = k.split(":")
        if len(parts) >= 2:
            counts[parts[1]] = counts.get(parts[1], 0) + 1
    
    _bubble_counts_cache = counts
    debug("get_bubble_counts: cached %d composers, %d total bubbles", 
          len(counts), sum(counts.values()))
    return counts


def clear_bubble_cache() -> None:
    """Clear the bubble counts cache (for testing)."""
    global _bubble_counts_cache
    _bubble_counts_cache = None


# Module-level cache for all composers with metadata
_all_composers_cache: Optional[Dict[str, Dict[str, Any]]] = None

def get_all_composers() -> Dict[str, Dict[str, Any]]:
    """Get all composers from all workspaces with metadata.
    
    Returns dict mapping composerId -> metadata (includes _workspace, _bubble_count).
    Cached for duration of CLI run.
    """
    global _all_composers_cache
    if _all_composers_cache is not None:
        debug("get_all_composers: returning cached (%d composers)", len(_all_composers_cache))
        return _all_composers_cache
    
    debug("get_all_composers: loading from all workspaces...")
    bubble_counts = get_bubble_counts()
    composers_meta: Dict[str, Dict[str, Any]] = {}
    
    for ws in iter_workspace_paths():
        folder = get_workspace_folder(ws)
        for c in get_workspace_composers(ws):
            cid = c.get("composerId")
            if cid:
                composers_meta[cid] = c.copy()
                composers_meta[cid]["_workspace"] = ws.name
                composers_meta[cid]["_workspace_folder"] = folder
                composers_meta[cid]["_bubble_count"] = bubble_counts.get(cid, 0)
    
    _all_composers_cache = composers_meta
    debug("get_all_composers: cached %d composers", len(composers_meta))
    return composers_meta


def clear_all_caches() -> None:
    """Clear all module-level caches."""
    global _bubble_counts_cache, _composers_cache, _all_composers_cache
    _bubble_counts_cache = None
    _composers_cache.clear()
    _all_composers_cache = None


def iter_workspace_paths() -> Iterator[Path]:
    """Iterate over all workspace directories."""
    for ws in WORKSPACES_ROOT.iterdir():
        if ws.is_dir():
            yield ws


# Command Implementations (one function per CLI command)

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
    
    if args.yaml or args.json:
        # Remove path for serialization
        output = [{k: v for k, v in w.items() if k != "path"} for w in ws_data]
        print(fmt(output, args))
    else:
        if sort_key == "date":
            print(f"{'IDX':<5} {'SHORT':<10} {'MODIFIED':<20} {'CHATS':>5}  FOLDER")
            print("─" * 90)
            for w in ws_data:
                mtime_str = datetime.fromtimestamp(w["db_mtime"]).strftime("%Y-%m-%d %H:%M") if w["db_mtime"] else "?"
                folder = w["folder"]
                if len(folder) > 40:
                    folder = "..." + folder[-37:]
                print(f"{w['index']:<5} {w['short']:<10} {mtime_str:<20} {w['composer_count']:>5}  {folder}")
        else:
            print(f"{'IDX':<5} {'SHORT':<10} {'SIZE':>10} {'CHATS':>5}  FOLDER")
            print("─" * 85)
            for w in ws_data:
                size_kb = w["db_size"] // 1024
                folder = w["folder"]
                if len(folder) > 45:
                    folder = "..." + folder[-42:]
                print(f"{w['index']:<5} {w['short']:<10} {size_kb:>8}KB {w['composer_count']:>5}  {folder}")


def get_workspace_index() -> List[Dict]:
    """Get indexed list of workspaces sorted by size."""
    ws_list = sorted(
        [ws for ws in WORKSPACES_ROOT.iterdir() if ws.is_dir()],
        key=lambda w: (w / "state.vscdb").stat().st_size if (w / "state.vscdb").exists() else 0,
        reverse=True
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
        if args.yaml or args.json:
            print(fmt([{k: v for k, v in w.items() if k != "path"} for w in workspaces], args))
        else:
            print("WORKSPACES (use 'tree w1' to drill down)")
            print("─" * 70)
            print(f"{'IDX':<5} {'SHORT':<10} {'SIZE':>8} {'CHATS':>5}  FOLDER")
            print("─" * 70)
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
        if args.yaml or args.json:
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
            print("─" * 70)
            print(f"{'IDX':<5} {'SHORT':<10} {'MSGS':>6} {'MODE':<8} NAME")
            print("─" * 70)
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
        
        if args.yaml or args.json:
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
        
        if args.yaml or args.json:
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
        
        if args.yaml or args.json:
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
        if args.yaml or args.json:
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
    
    if args.yaml or args.json:
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
    
    if args.yaml or args.json:
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
            print("─" * 80)
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
    
    if args.yaml or args.json:
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


def cmd_tail(args):
    """Show recent chat messages."""
    bubbles = []
    for cid, k, obj in iter_bubbles(args.composer):
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
    bubbles = bubbles[:args.lines]
    bubbles.reverse()
    
    for obj in bubbles:
        if args.yaml or args.json:
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
    items = items[:args.lines]
    items.reverse()
    
    for ts, obj in items:
        if args.yaml or args.json:
            print(fmt(obj, args))
        else:
            format_bubble_pretty(obj, verbose=False)


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


def cmd_grep(args):
    """Grep-like search in chat bubbles."""
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
    
    for cid, k, obj in iter_bubbles(args.composer):
        text = get_bubble_text(obj)
        found = bool(pattern.search(text))
        if args.invert_match:
            found = not found
        
        if found:
            match_count += 1
            matched_composers.add(cid)
            
            if args.max_results and match_count > args.max_results:
                break
            
            if not args.count and not args.composers_only:
                obj["_key"] = k
                obj["_composer"] = cid
                if args.yaml or args.json:
                    print(fmt(obj, args))
                else:
                    preview = text[:200] + ("..." if len(text) > 200 else "")
                    print(f"[{cid[:8]}] {preview}")
    
    if args.count:
        print(match_count)
    elif args.composers_only:
        for cid in sorted(matched_composers):
            print(cid)


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
    
    if args.yaml or args.json:
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


def cmd_files(args):
    """List files touched in a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Collect file references
    files_seen: Dict[str, Dict[str, int]] = {}
    
    def add_file(path: Any, is_write: bool = False) -> None:
        """Add a file path to the seen files, handling various formats."""
        if not path:
            return
        # Handle dict (e.g., URI objects)
        if isinstance(path, dict):
            path = path.get("fsPath") or path.get("path") or path.get("uri") or ""
        if not isinstance(path, str) or not path:
            return
        files_seen.setdefault(path, {"reads": 0, "writes": 0})
        if is_write:
            files_seen[path]["writes"] += 1
        else:
            files_seen[path]["reads"] += 1
    
    for b in bubbles:
        # From context
        ctx = b.get("context", {})
        for sel in ctx.get("fileSelections", []):
            if isinstance(sel, dict):
                add_file(sel.get("relativePath") or sel.get("uri"))
            else:
                add_file(sel)
        
        # From code blocks (potential writes)
        for cb in b.get("codeBlocks", []):
            if isinstance(cb, dict):
                add_file(cb.get("relativePath"), is_write=True)
        
        # From file links in response
        for fl in b.get("fileLinks", []):
            if isinstance(fl, str):
                try:
                    fl = json.loads(fl)
                except:
                    continue
            if isinstance(fl, dict):
                add_file(fl.get("relativeWorkspacePath") or fl.get("displayName"))
        
        # From symbol links
        for sl in b.get("symbolLinks", []):
            if isinstance(sl, str):
                try:
                    sl = json.loads(sl)
                except:
                    continue
            if isinstance(sl, dict):
                add_file(sl.get("relativeWorkspacePath"))
    
    # Sort by activity
    files_list = [
        {"path": path, **counts}
        for path, counts in sorted(files_seen.items(), key=lambda x: -(x[1]["reads"] + x[1]["writes"]))
    ]
    
    if args.yaml or args.json:
        print(fmt(files_list, args))
    else:
        print(f"Files touched in composer {target[:16]}...")
        print(f"{'PATH':<60} {'READS':>6} {'WRITES':>6}")
        print("─" * 80)
        for f in files_list[:50]:
            path = f["path"]
            if len(path) > 58:
                path = "..." + path[-55:]
            print(f"{path:<60} {f['reads']:>6} {f['writes']:>6}")


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
    
    if args.yaml or args.json:
        print(fmt(models, args))
    else:
        print(f"{'MODEL':<40} {'MESSAGES':>10} {'CHATS':>8}")
        print("─" * 60)
        for m in models:
            print(f"{m['model']:<40} {m['message_count']:>10} {m['conversation_count']:>8}")


def resolve_composer_id(ref: str, workspace_ref: Optional[str] = None) -> Optional[str]:
    """Resolve composer reference to just the UUID string.
    
    Wrapper around resolve_composer for simpler use cases.
    """
    result = resolve_composer(ref, workspace_ref)
    if result:
        return result[0]  # Return just the ID
    return None


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
    
    if args.yaml or args.json:
        print(fmt(tools, args))
    else:
        print(f"Tool calls in {target[:16]}... ({len(tools)} calls)")
        print(f"{'TIME':<20} {'STATUS':<10} {'TOOL':<20} ARGS")
        print("─" * 100)
        for t in tools:
            args_str = json.dumps(t["args"]) if isinstance(t["args"], dict) else str(t["args"])
            if len(args_str) > 50:
                args_str = args_str[:47] + "..."
            print(f"{t['timestamp']:<20} {t['status']:<10} {t['name']:<20} {args_str}")
            if args.verbose and t.get("result_preview"):
                print(f"  → {t['result_preview'][:100]}")


def cmd_todos(args):
    """Show todos/tasks from a conversation."""
    target = resolve_composer_id(args.composer)
    if not target:
        raise NotFoundError(f"Composer not found: {args.composer}")
    
    bubbles = load_bubbles(target)
    
    # Extract todos (take the last non-empty one as current state)
    all_todos = []
    for b in bubbles:
        todos = b.get("todos", [])
        if todos:
            parsed = []
            for t in todos:
                if isinstance(t, str):
                    try:
                        t = json.loads(t)
                    except:
                        continue
                parsed.append(t)
            if parsed:
                all_todos = parsed
    
    if args.yaml or args.json:
        print(fmt(all_todos, args))
    else:
        print(f"Todos in {target[:16]}... ({len(all_todos)} items)")
        print("─" * 60)
        for t in all_todos:
            status = t.get("status", "?")
            icon = {"completed": "✓", "in_progress": "→", "pending": "○"}.get(status, "?")
            content = t.get("content", "")
            print(f"  {icon} [{status:<11}] {content}")


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
    
    if args.yaml or args.json:
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


def cmd_analyze(args):
    """Deep analysis of a conversation (boot sequence)."""
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
    
    if args.yaml or args.json:
        print(fmt(analysis, args))
    else:
        print(f"═══ Analysis: {target[:24]}... ═══")
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
    
    if args.yaml or args.json:
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
    
    if args.yaml or args.json:
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
            if args.yaml or args.json:
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
    
    if args.yaml or args.json:
        print(fmt(blobs, args))
    else:
        print(f"Agent blobs (>= {args.min_size} bytes, top {args.limit})")
        print(f"{'HASH':<34} {'SIZE':>12}")
        print("─" * 50)
        for b in blobs:
            print(f"{b['hash']:<34} {b['size_human']:>12}")
        print(f"\nUse: cursor-mirror blobs --show <hash> to view content")


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
        
        if args.yaml or args.json:
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
    
    if args.yaml or args.json:
        print(fmt(thinking_blocks, args))
    else:
        print(f"Thinking blocks in {target[:16]}... ({len(thinking_blocks)} shown)")
        print("─" * 80)
        for t in thinking_blocks:
            print(f"\n💭 {t['timestamp']} ({t['length']} chars)")
            # Wrap text nicely
            text = t["text"]
            if len(text) > 500:
                text = text[:500] + "..."
            print(text)


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
    
    print(f"═══ Conversation Replay: {target[:24]}... ═══")
    print(f"Messages: {len(bubbles)}")
    print(f"Speed: {args.speed}x (Ctrl+C to stop)")
    print("─" * 80)
    
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
    print("═══ Replay Complete ═══")


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
    
    if args.yaml or args.json:
        print(fmt(contexts, args))
    else:
        for ctx in contexts[:1]:  # Show first/largest
            print(f"═══ Request Context: {ctx['message_id']}... ({ctx['size_bytes']} bytes) ═══")
            
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
    
    if args.yaml or args.json:
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
    
    if args.yaml or args.json:
        print(fmt(results, args))
    else:
        print(f"Indexing Status ({len(results)} workspaces with retrieval data)")
        print("─" * 80)
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


def cmd_mcp(args):
    """MCP tool call tracing and analysis."""
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    
    # --servers: list known MCP servers
    if args.servers:
        row = cur.execute("SELECT value FROM ItemTable WHERE key = 'mcpService.knownServerIds'").fetchone()
        if row:
            servers = json.loads(row[0])
            if args.yaml or args.json:
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
    
    if args.yaml or args.json:
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
    
    if args.yaml or args.json:
        print(fmt(sources, args))
    else:
        print(f"═══ Context Sources: {target[:24]}... ═══")
        
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
    
    if args.yaml or args.json:
        print(fmt(result, args))
    else:
        print(f"═══ Diff: Checkpoint {from_idx} → {to_idx} ═══")
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
    
    if args.output:
        Path(args.output).write_text(output)
        print(f"Exported {len(lines)} records to {args.output}")
    else:
        print(output)


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
    
    if args.yaml or args.json:
        print(fmt(index, args))
    else:
        # Pretty print
        print(f"Cursor Chat Index")
        print(f"Generated: {index['generated']}")
        print(f"Total Conversations: {index['total_conversations']}")
        print("─" * 80)
        
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

def get_item_table_value(key: str) -> Optional[Any]:
    """Get a value from ItemTable, parsing JSON if applicable."""
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    row = cur.execute("SELECT value FROM ItemTable WHERE key = ?", (key,)).fetchone()
    conn.close()
    if not row:
        return None
    try:
        return json.loads(row[0])
    except:
        return row[0]


def get_reactive_storage() -> Dict[str, Any]:
    """Get the reactive storage blob."""
    key = "src.vs.platform.reactivestorage.browser.reactiveStorageServiceImpl.persistentStorage.applicationUser"
    return get_item_table_value(key) or {}


def cmd_status(args):
    """Overall Cursor status dashboard."""
    # Count bubbles and composers
    bubble_counts = get_bubble_counts()
    total_msgs = sum(bubble_counts.values())
    num_composers = len(bubble_counts)
    
    # MCP servers
    mcp_servers = get_item_table_value("mcpService.knownServerIds") or []
    
    # Server config
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    
    # Reactive storage for AI settings
    reactive = get_reactive_storage()
    ai_settings = reactive.get("aiSettings", {})
    
    # Feature config
    feature_config = get_item_table_value("cursorai/featureConfigCache") or {}
    feature_status = get_item_table_value("cursorai/featureStatusCache") or {}
    
    # Privacy
    privacy_mode = get_item_table_value("cursorai/donotchange/privacyMode")
    
    status = {
        "cursor_status": {
            "total_composers": num_composers,
            "total_messages": total_msgs,
            "mcp_servers_registered": len(mcp_servers),
            "privacy_mode": privacy_mode,
        },
        "ai_settings": {
            "composer_model": ai_settings.get("composerModel", "default"),
            "chat_model": ai_settings.get("regularChatModel", "default"),
            "model_override_enabled": ai_settings.get("modelOverrideEnabled", False),
        },
        "limits": {
            "context_tokens": server_config.get("chatConfig", {}).get("fullContextTokenLimit", "?"),
            "max_mcp_tools": server_config.get("chatConfig", {}).get("maxMcpTools", "?"),
            "max_files_indexed": server_config.get("indexingConfig", {}).get("absoluteMaxNumberFiles", "?"),
        },
        "features_enabled": sum(1 for v in feature_status.values() if v),
        "features_total": len(feature_status),
    }
    
    if args.yaml or args.json:
        print(fmt(status, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    CURSOR STATUS DASHBOARD                   ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Composers: {status['cursor_status']['total_composers']:>6}    Messages: {status['cursor_status']['total_messages']:>8}          ║")
        print(f"║  MCP Servers: {status['cursor_status']['mcp_servers_registered']:>4}      Privacy: {'ON' if privacy_mode else 'OFF':>5}                  ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  AI Settings                                                 ║")
        print(f"║    Composer Model: {str(status['ai_settings']['composer_model'])[:35]:35} ║")
        print(f"║    Chat Model:     {str(status['ai_settings']['chat_model'])[:35]:35} ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  Limits                                                      ║")
        print(f"║    Context Tokens:   {str(status['limits']['context_tokens']):>10}                        ║")
        print(f"║    Max MCP Tools:    {str(status['limits']['max_mcp_tools']):>10}                        ║")
        print(f"║    Max Files Index:  {str(status['limits']['max_files_indexed']):>10}                        ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Features: {status['features_enabled']}/{status['features_total']} enabled                                  ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("\nRun 'status-config', 'status-mcp', 'status-models' for details.")


def cmd_status_config(args):
    """Server configuration and limits."""
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    
    config = {
        "indexing": server_config.get("indexingConfig", {}),
        "chat": server_config.get("chatConfig", {}),
        "background_composer": server_config.get("backgroundComposerConfig", {}),
        "tracing": server_config.get("clientTracingConfig", {}),
        "bugbot": server_config.get("bugConfigResponse", {}),
        "config_version": server_config.get("configVersion", "unknown"),
    }
    
    if args.yaml or args.json:
        print(fmt(config, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    SERVER CONFIGURATION                      ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        idx = config.get("indexing", {})
        print("║  Indexing                                                    ║")
        print(f"║    Max Files:          {idx.get('absoluteMaxNumberFiles', '?'):>10}                      ║")
        print(f"║    Concurrent Uploads: {idx.get('maxConcurrentUploads', '?'):>10}                      ║")
        print(f"║    Sync Concurrency:   {idx.get('syncConcurrency', '?'):>10}                      ║")
        print(f"║    Index Period (sec): {idx.get('indexingPeriodSeconds', '?'):>10}                      ║")
        print(f"║    Max Batch Bytes:    {idx.get('maxBatchBytes', '?'):>10}                      ║")
        
        chat = config.get("chat", {})
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Chat                                                        ║")
        print(f"║    Context Token Limit:   {chat.get('fullContextTokenLimit', '?'):>10}                   ║")
        print(f"║    Max Rule Length:       {chat.get('maxRuleLength', '?'):>10}                   ║")
        print(f"║    Max MCP Tools:         {chat.get('maxMcpTools', '?'):>10}                   ║")
        print(f"║    MCP Tools Warning:     {chat.get('warnMcpTools', '?'):>10}                   ║")
        
        bg = config.get("background_composer", {})
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Background Composer                                         ║")
        print(f"║    Enabled:           {str(bg.get('enableBackgroundAgent', '?')):>10}                      ║")
        print(f"║    Max Windows:       {bg.get('maxWindowInWindows', '?'):>10}                      ║")
        print(f"║    Preload Count:     {bg.get('windowInWindowPreloadCount', '?'):>10}                      ║")
        
        print("╠──────────────────────────────────────────────────────────────╣")
        print(f"║  Config Version: {config.get('config_version', 'unknown')[:40]:40} ║")
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_mcp(args):
    """MCP servers and status."""
    mcp_servers = get_item_table_value("mcpService.knownServerIds") or []
    reactive = get_reactive_storage()
    mcp_config = reactive.get("mcpServers", [])
    
    # Categorize servers
    builtin = [s for s in mcp_servers if s.startswith("cursor-")]
    user = [s for s in mcp_servers if s.startswith("user-")]
    project = [s for s in mcp_servers if s.startswith("project-")]
    other = [s for s in mcp_servers if not any(s.startswith(p) for p in ["cursor-", "user-", "project-"])]
    
    result = {
        "total_servers": len(mcp_servers),
        "builtin": builtin,
        "user_configured": user,
        "project_scoped": project,
        "other": other,
    }
    
    if args.yaml or args.json:
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                      MCP SERVERS                             ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Total Registered: {len(mcp_servers):>3}                                       ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        if builtin:
            print("║  Built-in                                                    ║")
            for s in builtin:
                print(f"║    • {s[:54]:54} ║")
        
        if user:
            print("╠──────────────────────────────────────────────────────────────╣")
            print("║  User-Configured                                             ║")
            for s in user:
                display = s.replace("user-", "")
                print(f"║    • {display[:54]:54} ║")
        
        if project:
            print("╠──────────────────────────────────────────────────────────────╣")
            print("║  Project-Scoped                                              ║")
            for s in project[:10]:  # Limit display
                display = s.replace("project-", "")
                print(f"║    • {display[:54]:54} ║")
            if len(project) > 10:
                print(f"║    ... and {len(project) - 10} more                                          ║")
        
        if other:
            print("╠──────────────────────────────────────────────────────────────╣")
            print("║  Other                                                       ║")
            for s in other[:5]:
                print(f"║    • {s[:54]:54} ║")
        
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_models(args):
    """Available models and migrations."""
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    reactive = get_reactive_storage()
    
    available_models = reactive.get("availableDefaultModels2", [])
    ai_settings = reactive.get("aiSettings", {})
    migrations = server_config.get("modelMigrations", [])
    
    # Parse model capabilities
    models_by_capability = {
        "agent": [],
        "thinking": [],
        "images": [],
        "max_mode": [],
        "plan_mode": [],
        "sandboxing": [],
    }
    
    for m in available_models:
        name = m.get("model", m.get("name", "unknown"))
        if m.get("supportsAgent"):
            models_by_capability["agent"].append(name)
        if m.get("supportsThinking"):
            models_by_capability["thinking"].append(name)
        if m.get("supportsImages"):
            models_by_capability["images"].append(name)
        if m.get("supportsMaxMode"):
            models_by_capability["max_mode"].append(name)
        if m.get("supportsPlanMode"):
            models_by_capability["plan_mode"].append(name)
        if m.get("supportsSandboxing"):
            models_by_capability["sandboxing"].append(name)
    
    result = {
        "total_models": len(available_models),
        "current_settings": {
            "composer": ai_settings.get("composerModel", "default"),
            "chat": ai_settings.get("regularChatModel", "default"),
            "openai": ai_settings.get("openAIModel", "default"),
        },
        "models_by_capability": {k: len(v) for k, v in models_by_capability.items()},
        "recent_migrations": [{
            "from": m.get("previousModel"),
            "to": m.get("targetModel"),
            "setting": m.get("modelSetting"),
        } for m in migrations[:5]],
        "all_models": [m.get("model", m.get("name", "?")) for m in available_models],
    }
    
    if args.yaml or args.json:
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                      AI MODELS                               ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Total Available: {len(available_models):>3}                                        ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  Current Settings                                            ║")
        print(f"║    Composer: {str(result['current_settings']['composer'])[:45]:45} ║")
        print(f"║    Chat:     {str(result['current_settings']['chat'])[:45]:45} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Capabilities (model count)                                  ║")
        print(f"║    Agent: {len(models_by_capability['agent']):>3}  Thinking: {len(models_by_capability['thinking']):>3}  Images: {len(models_by_capability['images']):>3}  Max: {len(models_by_capability['max_mode']):>3}  ║")
        print(f"║    Plan: {len(models_by_capability['plan_mode']):>3}   Sandbox: {len(models_by_capability['sandboxing']):>3}                                  ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Recent Migrations                                           ║")
        for m in migrations[:3]:
            fr = m.get("previousModel", "?")[:20]
            to = m.get("targetModel", "?")[:20]
            print(f"║    {fr:20} → {to:20}         ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  All Models                                                  ║")
        model_names = [m.get("model", m.get("name", "?")) for m in available_models]
        # Print 2 per line
        for i in range(0, min(len(model_names), 20), 2):
            m1 = model_names[i][:28]
            m2 = model_names[i+1][:28] if i+1 < len(model_names) else ""
            print(f"║    {m1:28} {m2:28} ║")
        if len(model_names) > 20:
            print(f"║    ... and {len(model_names) - 20} more                                        ║")
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_features(args):
    """Feature flags and experiments."""
    feature_status = get_item_table_value("cursorai/featureStatusCache") or {}
    feature_config = get_item_table_value("cursorai/featureConfigCache") or {}
    reactive = get_reactive_storage()
    
    # Group features
    enabled = {k: v for k, v in feature_status.items() if v}
    disabled = {k: v for k, v in feature_status.items() if not v}
    
    # Interesting reactive toggles
    toggles = {
        "yoloMode": reactive.get("composerState", {}).get("yoloModeEnabled"),
        "isLinterEnabled": reactive.get("isLinterEnabled"),
        "autopilotEnabled": reactive.get("autopilotFeatureEnabled"),
        "bugbotEnabled": reactive.get("bugbotState", {}).get("isEnabled"),
        "semanticSearch": reactive.get("explicitlyEnableSemanticSearch"),
        "memoriesEnabled": reactive.get("cursor/memoriesEnabled"),
    }
    
    result = {
        "feature_flags": {
            "enabled_count": len(enabled),
            "disabled_count": len(disabled),
            "enabled_list": list(enabled.keys()),
        },
        "feature_config": feature_config,
        "reactive_toggles": toggles,
    }
    
    if args.yaml or args.json:
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    FEATURE FLAGS                             ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Enabled: {len(enabled):>3}    Disabled: {len(disabled):>3}                             ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  Reactive Toggles                                            ║")
        for name, val in toggles.items():
            status = "✓" if val else "✗" if val is False else "?"
            print(f"║    [{status}] {name:52} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Enabled Feature Flags                                       ║")
        for f in list(enabled.keys())[:15]:
            print(f"║    • {f[:54]:54} ║")
        if len(enabled) > 15:
            print(f"║    ... and {len(enabled) - 15} more                                          ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Feature Config (Limits)                                     ║")
        for k, v in list(feature_config.items())[:10]:
            print(f"║    {k[:30]:30} = {str(v)[:20]:20} ║")
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_privacy(args):
    """Privacy settings and data sharing."""
    privacy_mode = get_item_table_value("cursorai/donotchange/privacyMode")
    new_privacy = get_item_table_value("newPrivacyMode2")
    partner_share = get_item_table_value("partnerDataShare")
    
    reactive = get_reactive_storage()
    memories_enabled = reactive.get("cursor/memoriesEnabled")
    pending_memories = get_item_table_value("cursorPendingMemories") or []
    
    # Tracing config
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    tracing = server_config.get("clientTracingConfig", {})
    metrics = server_config.get("metricsConfig", {})
    
    result = {
        "privacy_mode": privacy_mode,
        "new_privacy_mode": new_privacy,
        "partner_data_share": partner_share,
        "memories": {
            "enabled": memories_enabled,
            "pending_count": len(pending_memories),
        },
        "telemetry": {
            "traces_sample_rate": tracing.get("tracesSampleRate"),
            "logger_sample_rate": tracing.get("loggerSampleRate"),
            "error_rate_limit": tracing.get("errorRateLimit"),
            "metrics_in_privacy_mode": metrics.get("enabledInPrivacyMode"),
        },
    }
    
    if args.yaml or args.json:
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    PRIVACY SETTINGS                          ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        pm_status = "ENABLED" if privacy_mode else "DISABLED"
        print(f"║  Privacy Mode: {pm_status:>10}                                  ║")
        print(f"║  Partner Data Share: {str(partner_share):>10}                          ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Memories                                                    ║")
        mem_status = "✓ Enabled" if memories_enabled else "✗ Disabled"
        print(f"║    Status: {mem_status:20}                          ║")
        print(f"║    Pending: {len(pending_memories):>5} memories waiting to sync                ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Telemetry Sampling                                          ║")
        print(f"║    Traces:  {tracing.get('tracesSampleRate', '?'):>10}                                 ║")
        print(f"║    Logger:  {tracing.get('loggerSampleRate', '?'):>10}                                 ║")
        print(f"║    Metrics in privacy mode: {str(metrics.get('enabledInPrivacyMode', '?')):>10}              ║")
        print("╚══════════════════════════════════════════════════════════════╝")


# SQL & database commands
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
        
        if args.yaml or args.json:
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
        
        if args.yaml or args.json:
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


def cmd_find(args):
    """Find workspaces/composers by name pattern."""
    pattern = args.pattern.lower()
    results = {"workspaces": [], "composers": []}
    
    if args.type in ("workspace", "all"):
        for ws in WORKSPACES_ROOT.iterdir():
            if not ws.is_dir():
                continue
            folder = get_workspace_folder(ws)
            if folder and pattern in folder.lower():
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
            if pattern in name.lower() or pattern in folder.lower():
                results["composers"].append({
                    "id": cid,
                    "short": cid[:8],
                    "name": name,
                    "messages": c.get("_bubble_count", 0),
                    "workspace": folder,
                    "workspace_hash": c.get("_workspace", "?")[:8],
                })
        
        results["composers"].sort(key=lambda x: x["messages"], reverse=True)
    
    if args.yaml or args.json:
        print(fmt(results, args))
    else:
        if results["workspaces"]:
            print("WORKSPACES")
            print("─" * 80)
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
        
        if args.yaml or args.json:
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
        
        if args.yaml or args.json:
            print(fmt(result, args))
        else:
            print(f"ID:        {result['id']}")
            print(f"Short:     {result['short']}")
            print(f"Name:      {result['name']}")
            print(f"Mode:      {result['mode']}")
            print(f"Created:   {result['created']}")
            print(f"Messages:  {result['messages']}")
            print(f"Workspace: {result['workspace_hash']}")


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
    
    if args.yaml or args.json:
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
    
    if args.yaml or args.json:
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
    
    if args.yaml or args.json:
        print(fmt(keys, args))
    else:
        print(f"Database: {db_path}")
        print("─" * 80)
        print(f"{'KEY':<60} {'SIZE':>12}")
        print("─" * 80)
        for k in keys:
            key_display = k["key"][:58] + ".." if len(k["key"]) > 60 else k["key"]
            size_str = f"{k['size']:,}" if k["size"] < 1024 else f"{k['size']//1024:,}KB"
            print(f"{key_display:<60} {size_str:>12}")
        print(f"\n({len(keys)} keys shown)")


def cmd_status_endpoints(args):
    """Known API endpoints."""
    endpoints = {
        "ai_backends": {
            "primary": "agent.api5.cursor.sh",
            "fallbacks": ["api2.cursor.sh", "api3.cursor.sh", "api4.cursor.sh"],
            "geo_optimized": {
                "us_west": "agent-gcpp-uswest.api5.cursor.sh",
                "eu_central": "agent-gcpp-eucentral.api5.cursor.sh",
            },
        },
        "semantic_search": {
            "primary": "repo42.cursor.sh",
            "purpose": "Codebase embedding and retrieval",
        },
        "telemetry": {
            "metrics": "metrics.cursor.sh",
            "purpose": "Error and performance tracking",
        },
        "marketplace": {
            "primary": "marketplace.cursorapi.com",
            "alternate": "marketplace.cursor.sh",
        },
        "updates": {
            "changelog": "changelog.cursor.com",
            "staging": "dev-staging.cursor.sh",
        },
        "internal": {
            "replay": "anytool.corp.anysphere.co/api/replay-chat",
            "docs": "docs.anysphere.dev",
        },
    }
    
    if args.yaml or args.json:
        print(fmt(endpoints, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    API ENDPOINTS                             ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  AI Backends                                                 ║")
        print(f"║    Primary:    {endpoints['ai_backends']['primary']:44} ║")
        print(f"║    US West:    {endpoints['ai_backends']['geo_optimized']['us_west']:44} ║")
        print(f"║    EU Central: {endpoints['ai_backends']['geo_optimized']['eu_central']:44} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Semantic Search                                             ║")
        print(f"║    {endpoints['semantic_search']['primary']:56} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Telemetry                                                   ║")
        print(f"║    {endpoints['telemetry']['metrics']:56} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Marketplace                                                 ║")
        print(f"║    {endpoints['marketplace']['primary']:56} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Internal (Debug)                                            ║")
        print(f"║    {endpoints['internal']['replay']:56} ║")
        print("╚══════════════════════════════════════════════════════════════╝")


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
    
    if args.yaml or args.json:
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

def iter_image_paths() -> Iterator[Tuple[Path, str, str]]:
    """Iterate all cached images across workspaces.
    
    Yields: (image_path, workspace_hash, workspace_folder)
    """
    for ws_path in iter_workspace_paths():
        img_dir = ws_path / "images"
        if img_dir.exists():
            ws_hash = ws_path.name
            ws_folder = get_workspace_folder(ws_path) or "unknown"
            for img in img_dir.iterdir():
                if img.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
                    yield img, ws_hash, ws_folder


def get_image_metadata(img_path: Path, ws_hash: str, ws_folder: str) -> Dict[str, Any]:
    """Get metadata for an image file."""
    stat = img_path.stat()
    return {
        "path": str(img_path),
        "filename": img_path.name,
        "uuid": img_path.stem.replace("image-", "").replace("Screenshot ", ""),
        "workspace": ws_folder.split("/")[-1] if ws_folder else "unknown",
        "workspace_hash": ws_hash,
        "size_kb": round(stat.st_size / 1024, 1),
        "size_bytes": stat.st_size,
        "modified": datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M'),
        "modified_ts": stat.st_mtime,
    }


def cmd_images(args):
    """List cached images from chat sessions."""
    images = []
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        meta = get_image_metadata(img_path, ws_hash, ws_folder)
        images.append(meta)
    
    # Sort
    if args.sort == "date":
        images.sort(key=lambda x: x["modified_ts"], reverse=True)
    elif args.sort == "size":
        images.sort(key=lambda x: x["size_bytes"], reverse=True)
    elif args.sort == "workspace":
        images.sort(key=lambda x: (x["workspace"], -x["modified_ts"]))
    
    # Limit
    if args.limit:
        images = images[:args.limit]
    
    if args.yaml or args.json:
        print(fmt(images, args))
    else:
        # Group by workspace
        by_ws: Dict[str, List[Dict]] = {}
        for img in images:
            ws = img["workspace"]
            if ws not in by_ws:
                by_ws[ws] = []
            by_ws[ws].append(img)
        
        print(f"Cached Images ({len(images)} total)")
        print("═" * 80)
        
        for ws, imgs in sorted(by_ws.items(), key=lambda x: -len(x[1])):
            total_kb = sum(i["size_kb"] for i in imgs)
            print(f"\n📁 {ws} ({len(imgs)} images, {total_kb:.1f} KB)")
            print("─" * 60)
            for img in imgs[:10]:  # Show first 10 per workspace
                print(f"  {img['modified']}  {img['size_kb']:>7.1f}KB  {img['uuid'][:8]}...")
            if len(imgs) > 10:
                print(f"  ... and {len(imgs) - 10} more")


def cmd_image_path(args):
    """Get full path to a cached image."""
    ref = args.ref.lower()
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        if ref in img_path.name.lower() or ref in str(img_path).lower():
            print(str(img_path))
            return
    
    raise NotFoundError(f"Image not found: {args.ref}")


def cmd_image_info(args):
    """Show metadata for a cached image."""
    ref = args.ref.lower()
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        if ref in img_path.name.lower() or ref in str(img_path).lower():
            meta = get_image_metadata(img_path, ws_hash, ws_folder)
            
            # Try to get dimensions using file header
            try:
                with open(img_path, 'rb') as f:
                    header = f.read(24)
                    if header.startswith(b'\x89PNG'):
                        # PNG: width/height at bytes 16-24
                        import struct
                        w, h = struct.unpack('>II', header[16:24])
                        meta["dimensions"] = {"width": w, "height": h}
            except Exception:
                pass
            
            if args.yaml or args.json:
                print(fmt(meta, args))
            else:
                print(f"Image: {meta['filename']}")
                print("─" * 60)
                print(f"  Path:      {meta['path']}")
                print(f"  UUID:      {meta['uuid']}")
                print(f"  Workspace: {meta['workspace']}")
                print(f"  Size:      {meta['size_kb']:.1f} KB")
                print(f"  Modified:  {meta['modified']}")
                if "dimensions" in meta:
                    print(f"  Dimensions: {meta['dimensions']['width']}x{meta['dimensions']['height']}")
                print(f"\nTo read this image:")
                print(f"  Read: {meta['path']}")
            return
    
    raise NotFoundError(f"Image not found: {args.ref}")


def cmd_image_gallery(args):
    """Generate narrated image gallery markdown."""
    images = []
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        meta = get_image_metadata(img_path, ws_hash, ws_folder)
        images.append(meta)
    
    # Sort by date (newest first)
    images.sort(key=lambda x: x["modified_ts"], reverse=True)
    
    # Filter by workspace if specified
    if args.workspace:
        images = [i for i in images if args.workspace.lower() in i["workspace"].lower()]
    
    # Limit
    if args.limit:
        images = images[:args.limit]
    
    # Group by workspace
    by_ws: Dict[str, List[Dict]] = {}
    for img in images:
        ws = img["workspace"]
        if ws not in by_ws:
            by_ws[ws] = []
        by_ws[ws].append(img)
    
    # Generate markdown
    lines = [
        "# ▎ I-Beam's Image Gallery",
        "# Author: Don Hopkins, Leela AI",
        "",
        "*cursor-mirror extracted cached images from Cursor's workspace storage.*",
        "",
        "---",
        "",
        "## Overview",
        "",
        "```yaml",
        "# IMAGE INVENTORY",
        f"total_images: {len(images)}",
        "workspaces:",
    ]
    
    for ws, imgs in sorted(by_ws.items(), key=lambda x: -len(x[1])):
        total_kb = sum(i["size_kb"] for i in imgs)
        lines.append(f"  {ws}: {len(imgs)} images ({total_kb:.0f} KB)")
    
    if images:
        dates = [i["modified"] for i in images]
        lines.extend([
            "",
            "date_range:",
            f"  oldest: {min(dates)}",
            f"  newest: {max(dates)}",
        ])
    
    lines.extend([
        "```",
        "",
        "---",
        "",
    ])
    
    # Generate sections per workspace
    for ws, imgs in sorted(by_ws.items(), key=lambda x: -len(x[1])):
        total_kb = sum(i["size_kb"] for i in imgs)
        lines.extend([
            f"## {ws}",
            "",
            f"*{len(imgs)} images, {total_kb:.1f} KB total*",
            "",
            "| Date | Size | UUID | Path |",
            "|------|------|------|------|",
        ])
        
        for img in imgs:
            uuid_short = img["uuid"][:8] + "..."
            path_short = f"...{img['path'][-50:]}" if len(img['path']) > 50 else img['path']
            lines.append(f"| {img['modified']} | {img['size_kb']:.0f}KB | `{uuid_short}` | `{path_short}` |")
        
        lines.extend(["", "---", ""])
    
    # Usage section
    lines.extend([
        "## Usage",
        "",
        "To view an image in Cursor chat:",
        "",
        "```",
        "Read: /full/path/to/image.png",
        "```",
        "",
        "To list images:",
        "",
        "```bash",
        "cursor-mirror images --all",
        "cursor-mirror images --sort size",
        "cursor-mirror image-path <uuid>",
        "cursor-mirror image-info <uuid> --yaml",
        "```",
        "",
        "---",
        "",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "*By: cursor-mirror image-gallery*",
    ])
    
    output = "\n".join(lines)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Gallery written to: {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    sys.exit(cli())
