#!/usr/bin/env python3
"""
cursor-mirror: See yourself think.

Cursor IDE introspection tool (macOS paths, read-only).

Copyright (c) 2026 Don Hopkins, Leela AI
License: MIT — see LICENSE file
Part of MOOLLM — https://github.com/leela-ai/moollm

═══════════════════════════════════════════════════════════════════════════════
FOR LLM AGENTS — READ THIS FIRST
═══════════════════════════════════════════════════════════════════════════════

QUICK START:
  cursor-mirror tail @1              # Last messages from CURRENT chat
  cursor-mirror analyze @1           # Stats for current chat  
  cursor-mirror tools @1 --limit 10  # Recent tool calls
  cursor-mirror tree                 # Browse all workspaces/composers
  cursor-mirror grep "error"         # Search across ALL chats

REFERENCE SYNTAX (use anywhere a composer/workspace is needed):
  @1, @2, @3     → By recency (most recent first, like bash !-1)
  fe18, 769a     → Hash prefix (4+ hex chars)
  moollm         → Name/folder fragment search
  w1.c2          → Tree path (workspace 1, composer 2)

COMMON GOTCHAS:
  • @1 = most RECENT, not largest. Changes when you switch projects.
  • Some commands need positional arg, some use --composer flag. Check help.
  • Security scans (secrets, deep-snitch) may show FALSE POSITIVES when
    scanning transcripts that contain pattern definitions (like this script).
  • Empty output usually means: wrong composer ID, or no matching data.

SECURITY SCANNER CAVEAT:
  The `secrets`, `deep-snitch`, and `full-audit` commands scan for dangerous
  patterns. They WILL detect their own pattern definitions if you scan the
  transcript of a session where security code was written. This is the
  "Ouroboros effect" — the scanner eating its own tail. ~80% of findings
  in such cases are false positives. Look at the actual line content.

WHAT'S WHERE:
  ~/.cursor/                           → Config, MCP, extensions
  ~/Library/Application Support/Cursor → Databases (state.vscdb)
  ~/.cursor/projects/*/agent-transcripts/ → Plaintext chat logs

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
  - Index:            @1, @2, @3 (sorted by recency - most recent first)
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
    # Global flags
    ap.add_argument("-d", "--debug", action="store_true",
                    help="Enable verbose debug logging to stderr")
    ap.add_argument("--sources", action="store_true",
                    help="Show data source paths (databases, files) for LLM self-service")
    ap.add_argument("-f", "--output-format", dest="output_format", metavar="FMT",
                    help="Output format: text (default), json, jsonl, yaml, csv, md. "
                         "Not all commands support all formats.")
    # Legacy compatibility: --json and --yaml still work but --output-format takes precedence
    ap.add_argument("--json", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--yaml", action="store_true", help=argparse.SUPPRESS)
    
    sub = ap.add_subparsers(dest="cmd", required=True)

    # ─── list-workspaces ───
    p = sub.add_parser("list-workspaces", help="List workspaces with folder paths and stats")
    p.add_argument("-n", "--limit", type=int, help="Limit results")
    p.add_argument("--sort", "-s", choices=["size", "date", "name", "chats"], default="size",
                   help="Sort by: size (default), date, name, chats")
    p.add_argument("--oldest", action="store_true", help="Oldest first (with --sort date)")
    p.set_defaults(func=cmd_list_workspaces)

    # ─── show-workspace ───
    p = sub.add_parser("show-workspace", help="Workspace details (use: show-workspace @1)")
    p.add_argument("workspace", help="Workspace ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_show_workspace)

    # ─── list-composers ───
    p = sub.add_parser("list-composers", help="List composers (conversations) with metadata")
    p.add_argument("workspace", nargs="?", help="Workspace filter (name, @index, or hash)")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max to show")
    p.add_argument("--sort", "-s", choices=["msgs", "date", "name"], default="msgs",
                   help="Sort by: msgs (default), date, name")
    p.add_argument("--oldest", action="store_true", help="Oldest first (with --sort date)")
    p.set_defaults(func=cmd_list_composers)

    # ─── tree ───
    p = sub.add_parser("tree", help="Tree navigation with short IDs (w1, w1.c2)")
    p.add_argument("path", nargs="?", help="Path: empty=workspaces, w1=workspace, w1.c2=composer")
    p.set_defaults(func=cmd_tree)

    # ─── show-composer ───
    p = sub.add_parser("show-composer", help="Composer details (use: show-composer @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_show_composer)

    # ─── tail ───
    p = sub.add_parser("tail", help="Show recent chat messages (use: tail [@1|hash|name])")
    p.add_argument("composer", nargs="?", help="Composer ref: @1, hash prefix, name (optional)")
    p.add_argument("-n", "--limit", type=int, default=20, help="Max messages to show")
    p.add_argument("--tools", action="store_true", help="Only agent/tool activity")
    p.add_argument("--user", action="store_true", help="Only user messages")
    p.add_argument("--assistant", action="store_true", help="Only assistant messages")
    p.add_argument("--all", action="store_true", help="Include empty bubbles")
    p.add_argument("-p", "--pretty", action="store_true", help="Pretty-print JSON")
    p.add_argument("-v", "--verbose", action="store_true", help="Show more details")
    p.set_defaults(func=cmd_tail)

    # ─── stream ───
    p = sub.add_parser("stream", help="Unified stream of all activity")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max items to show")
    p.add_argument("--since", help="Time filter: 1h, 30m, 1d, 2024-01-15")
    p.add_argument("--composer", help="Filter by composerId")
    p.add_argument("--type", choices=["user", "assistant", "all"], default="all")
    p.add_argument("-p", "--pretty", action="store_true", help="Pretty-print JSON")
    p.set_defaults(func=cmd_stream)

    # ─── export-chat ───
    p = sub.add_parser("export-chat", help="Export composer bubbles as JSON/YAML")
    p.add_argument("composer", help="Composer UUID (or prefix/name)")
    p.add_argument("-o", "--out", help="Output file (default: stdout)")
    p.add_argument("-p", "--pretty", action="store_true", help="Pretty-print JSON")
    p.set_defaults(func=cmd_export_chat)

    # ─── export-prompts ───
    p = sub.add_parser("export-prompts", help="Export prompts/generations for workspace")
    p.add_argument("workspace", help="Workspace hash (or name/prefix)")
    p.add_argument("-o", "--out", help="Output file (default: stdout)")
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
    p.add_argument("-n", "--limit", type=int, help="Max results to show")
    p.add_argument("-p", "--pretty", action="store_true")
    p.set_defaults(func=cmd_grep)

    # ─── transcript ───
    p = sub.add_parser("transcript", help="Readable transcript (use: transcript @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.add_argument("--context", action="store_true", help="Include context (files, selections)")
    p.add_argument("--thinking", action="store_true", help="Include thinking blocks")
    p.add_argument("--markdown", action="store_true", help="Output as Markdown")
    p.add_argument("--out", help="Output file")
    p.set_defaults(func=cmd_transcript)

    # ─── files ───
    p = sub.add_parser("files", help="Files touched (use: files @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_files)

    # ─── models ───
    p = sub.add_parser("models", help="Model usage analysis")
    p.add_argument("--composer", help="Filter by composer")
    p.set_defaults(func=cmd_models)

    # ─── tools ───
    p = sub.add_parser("tools", help="List tool calls (use: tools [@1|hash|name])")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.add_argument("--status", choices=["all", "completed", "error"], default="all")
    p.add_argument("--name", help="Filter by tool name")
    p.add_argument("-n", "--limit", type=int, help="Max results to show")
    p.add_argument("-v", "--verbose", action="store_true", help="Show results/params")
    p.set_defaults(func=cmd_tools)

    # ─── todos ───
    p = sub.add_parser("todos", help="Show todos/tasks (use: todos @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_todos)

    # ─── context ───
    p = sub.add_parser("context", help="Show context gathered (use: context @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_context)

    # ─── analyze ───
    p = sub.add_parser("analyze", help="Deep analysis (use: analyze @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_analyze)

    # ─── timeline ───
    p = sub.add_parser("timeline", help="Chronological timeline (use: timeline @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.set_defaults(func=cmd_timeline)

    # ─── checkpoints ───
    p = sub.add_parser("checkpoints", help="List file checkpoints (use: checkpoints @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.add_argument("-v", "--verbose", action="store_true", help="Show all file details")
    p.set_defaults(func=cmd_checkpoints)

    # ─── blobs ───
    p = sub.add_parser("blobs", help="List cached agentKv blobs (use: blobs [@1|hash])")
    p.add_argument("composer", nargs="?", help="Composer ref: @1, hash prefix, name (optional)")
    p.add_argument("-n", "--limit", type=int, default=20, help="Number to show")
    p.add_argument("--min-size", type=int, default=1000, help="Min blob size in bytes")
    p.add_argument("--show", help="Show specific blob by hash prefix")
    p.set_defaults(func=cmd_blobs)

    # ─── tool-result ───
    p = sub.add_parser("tool-result", help="Show full tool result content")
    p.add_argument("blob_hash", help="Blob hash (or prefix)")
    p.set_defaults(func=cmd_tool_result)

    # ─── thinking ───
    p = sub.add_parser("thinking", help="Show thinking blocks (use: thinking @1)")
    p.add_argument("composer", help="Composer ref: @1, hash prefix, name")
    p.add_argument("-n", "--limit", type=int, default=20, help="Number to show")
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
    p.set_defaults(func=cmd_request_context)

    # ─── searches ───
    p = sub.add_parser("searches", help="Show codebase/web searches in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--type", choices=["codebase", "web", "all"], default="all")
    p.add_argument("-v", "--verbose", action="store_true", help="Show result details")
    p.set_defaults(func=cmd_searches)

    # ─── indexing ───
    p = sub.add_parser("indexing", help="Show indexing status and embeddable files")
    p.add_argument("workspace", nargs="?", help="Workspace hash (or prefix)")
    p.add_argument("--files", action="store_true", help="List embeddable files")
    p.add_argument("--folders", action="store_true", help="Show folder descriptions")
    p.set_defaults(func=cmd_indexing)

    # ─── context-sources ───
    p = sub.add_parser("context-sources", help="Analyze all context sources in a conversation")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.set_defaults(func=cmd_context_sources)

    # ─── mcp ───
    p = sub.add_parser("mcp", help="MCP tool call tracing and analysis")
    p.add_argument("composer", nargs="?", help="Composer UUID (or prefix)")
    p.add_argument("--servers", action="store_true", help="List known MCP servers")
    p.add_argument("--all", action="store_true", help="Show all MCP calls globally")
    p.add_argument("-v", "--verbose", action="store_true", help="Show call details")
    p.set_defaults(func=cmd_mcp)

    # ─── diff ───
    p = sub.add_parser("diff", help="Show changes between checkpoints")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--from", dest="from_idx", type=int, default=0, help="From checkpoint index")
    p.add_argument("--to", dest="to_idx", type=int, default=-1, help="To checkpoint index (-1 = last)")
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
    p.set_defaults(func=cmd_index)

    # ─── STATUS COMMANDS ───
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

    p = sub.add_parser("status-privacy", help="Privacy settings and data sharing")
    p.set_defaults(func=cmd_status_privacy)

    p = sub.add_parser("status-endpoints", help="Known API endpoints")
    p.set_defaults(func=cmd_status_endpoints)

    # ─── stats ───
    p = sub.add_parser("stats", help="Summary statistics (use: stats [@1|hash|name] for single chat)")
    p.add_argument("composer", nargs="?", help="Composer ref: @1, hash prefix, name (optional)")
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
    p.add_argument("--raw", action="store_true", help="Print raw output")
    p.set_defaults(func=cmd_sql)

    p = sub.add_parser("find", help="Find workspaces/composers by name")
    p.add_argument("pattern", help="Search pattern (name fragment, path, etc.)")
    p.add_argument("--type", "-t", choices=["workspace", "composer", "all"], default="all")
    p.set_defaults(func=cmd_find)

    p = sub.add_parser("which", help="Resolve workspace/composer reference")
    p.add_argument("ref", help="Reference (@1, hash prefix, name fragment)")
    p.add_argument("--type", "-t", choices=["workspace", "composer"], default="workspace")
    p.set_defaults(func=cmd_which)

    p = sub.add_parser("dbs", help="List all Cursor databases with sizes")
    p.set_defaults(func=cmd_dbs)

    p = sub.add_parser("tables", help="List tables in a database")
    p.add_argument("--db", default="global", help="'global' or workspace ref")
    p.set_defaults(func=cmd_tables)

    p = sub.add_parser("keys", help="List ItemTable keys with sizes")
    p.add_argument("--db", default="global", help="'global' or workspace ref")
    p.add_argument("--pattern", "-p", help="Filter by key pattern (LIKE)")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=cmd_keys)

    # ─── IMAGE COMMANDS ───
    
    # images
    p = sub.add_parser("images", help="List cached images from chat sessions")
    p.add_argument("composer", nargs="?", help="Filter by composer (optional)")
    p.add_argument("-a", "--all", action="store_true", help="Show all images across workspaces")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max images to show")
    p.add_argument("--sort", choices=["date", "size", "workspace"], default="date",
                   help="Sort by: date (default), size, workspace")
    p.set_defaults(func=cmd_images)
    
    # image-path
    p = sub.add_parser("image-path", help="Get full path to a cached image")
    p.add_argument("ref", help="Image UUID or filename fragment")
    p.set_defaults(func=cmd_image_path)
    
    # image-info
    p = sub.add_parser("image-info", help="Show metadata for a cached image")
    p.add_argument("ref", help="Image UUID or path")
    p.set_defaults(func=cmd_image_info)
    
    # image-gallery
    p = sub.add_parser("image-gallery", help="Generate narrated image gallery markdown")
    p.add_argument("-o", "--output", help="Output file (default: stdout)")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max images")
    p.add_argument("--sample", type=int, default=10, help="Sample N images for narration hints")
    p.add_argument("--workspace", help="Filter to specific workspace")
    p.set_defaults(func=cmd_image_gallery)

    # ─── ~/.cursor COMMANDS (2026-01-15) ───
    
    # dotcursor-status
    p = sub.add_parser("dotcursor-status", help="Overview of ~/.cursor directory")
    p.add_argument("--workspace", help="Filter to specific workspace")
    p.set_defaults(func=cmd_dotcursor_status)
    
    # ai-hashes
    p = sub.add_parser("ai-hashes", help="Query AI code tracking database")
    p.add_argument("--since", help="Time filter: 1h, 30m, 1d, 2024-01-15")
    p.add_argument("--model", help="Filter by model name (supports wildcards)")
    p.add_argument("--file", help="Filter by file pattern")
    p.add_argument("--source", choices=["composer", "tab"], help="Filter by source")
    p.add_argument("-n", "--limit", type=int, default=20, help="Max results")
    p.add_argument("--stats", action="store_true", help="Show statistics only")
    p.set_defaults(func=cmd_ai_hashes)
    
    # ai-commits
    p = sub.add_parser("ai-commits", help="Git commits scored for AI attribution")
    p.add_argument("--since", help="Time filter: 1h, 30m, 1d")
    p.add_argument("--branch", help="Filter by branch name")
    p.add_argument("-n", "--limit", type=int, default=20, help="Max results")
    p.set_defaults(func=cmd_ai_commits)
    
    # agent-transcript
    p = sub.add_parser("agent-transcript", help="Read plaintext transcript from ~/.cursor")
    p.add_argument("composer", help="Composer UUID (or prefix)")
    p.add_argument("--workspace", help="Workspace name/path")
    p.add_argument("--tail", type=int, help="Show last N lines")
    p.add_argument("--head", type=int, help="Show first N lines")
    p.add_argument("--prompts", action="store_true", help="Extract prompts only")
    p.add_argument("--responses", action="store_true", help="Extract responses only")
    p.add_argument("--tools", action="store_true", help="Extract tool calls only")
    p.add_argument("--thinking", action="store_true", help="Extract thinking blocks only")
    p.add_argument("--format", choices=["auto", "txt", "json"], default="auto",
                   help="Transcript format: auto (default), txt, json")
    p.add_argument("--json-out", action="store_true", help="Output as JSON")
    p.set_defaults(func=cmd_agent_transcript)
    
    # transcript-index
    p = sub.add_parser("transcript-index", help="Index a specific transcript with line-range K-REFs (requires composer)")
    p.add_argument("composer", help="Composer UUID or prefix (required - use 'find' to discover)")
    p.add_argument("--workspace", help="Workspace name/path")
    p.add_argument("--min-lines", type=int, default=5, help="Min lines for a section")
    p.add_argument("--types", help="Comma-separated types: user,assistant,tool,thinking,error")
    p.set_defaults(func=cmd_transcript_index)
    
    # events (linter mode)
    p = sub.add_parser("events", help="Scan for actionable events, emit file:line pointers for LLM")
    p.add_argument("--composer", help="Scan specific composer transcript")
    p.add_argument("--workspace", help="Workspace name/path filter")
    p.add_argument("--since", help="Time filter: 1h, 30m, 1d, 7d")
    p.add_argument("--types", help="Event types: error,todo,stale,prompt,checkpoint,tool_fail")
    p.add_argument("--severity", choices=["info", "warn", "error"], help="Min severity")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max events")
    p.set_defaults(func=cmd_events)
    
    # tgrep (transcript-aware grep)
    p = sub.add_parser("tgrep", help="Transcript-aware grep with structured output")
    p.add_argument("pattern", help="Pattern to search (regex by default)")
    p.add_argument("files", nargs="*", help="Files to search (default: recent transcripts)")
    p.add_argument("--composer", help="Search specific composer transcript")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("-B", "--before", type=int, default=0, help="Lines before match")
    p.add_argument("-A", "--after", type=int, default=0, help="Lines after match")
    p.add_argument("-C", "--context", type=int, help="Lines before and after (overrides -B/-A)")
    p.add_argument("--section", help="Limit to section type: user,assistant,thinking,tool,yaml")
    p.add_argument("--refs-only", action="store_true", help="Output only file:line refs")
    p.add_argument("--excerpt", action="store_true", help="Include matching excerpt")
    p.add_argument("--meta", action="store_true", help="Include section metadata")
    p.add_argument("-i", "--ignorecase", action="store_true", help="Case insensitive")
    p.add_argument("-F", "--fixed", action="store_true", help="Fixed string (literal, not regex)")
    p.add_argument("-g", "--glob", action="store_true", help="Glob/fnmatch pattern (* ? [])")
    p.add_argument("-w", "--word", action="store_true", help="Match whole words only")
    p.add_argument("-v", "--invert", action="store_true", help="Invert match (lines NOT matching)")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max matches")
    p.set_defaults(func=cmd_tgrep)
    
    # secrets (scan for credentials/keys)
    p = sub.add_parser("secrets", help="Scan for potential secrets/credentials (K-REFS output)")
    p.add_argument("--composer", help="Scan specific composer transcript")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--since", help="Time filter: 1h, 1d, 7d")
    p.add_argument("-C", "--context", type=int, default=1, help="Context lines around match")
    p.add_argument("--refs-only", action="store_true", help="Output only file:line refs")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max matches")
    p.set_defaults(func=cmd_secrets)
    
    # commits (find git commits in transcripts)
    p = sub.add_parser("commits", help="Find git commits mentioned in transcripts (K-REFS output)")
    p.add_argument("--composer", help="Scan specific composer transcript")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--refs-only", action="store_true", help="Output only file:line refs")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max matches")
    p.set_defaults(func=cmd_commits)
    
    # scrub (redact sensitive content)
    p = sub.add_parser("scrub", help="Redact sensitive content from transcripts (QUIT CURSOR FIRST)")
    p.add_argument("--composer", help="Scrub specific composer transcript")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--pattern", help="Custom regex pattern to redact")
    p.add_argument("--secrets", action="store_true", help="Redact detected secrets")
    p.add_argument("--dry-run", action="store_true", help="Show what would be redacted without changing")
    p.add_argument("--backup", action="store_true", default=True, help="Create .bak backup (default: true)")
    p.add_argument("--no-backup", action="store_true", help="Skip backup creation")
    p.add_argument("--redact-text", default="[REDACTED]", help="Replacement text")
    p.set_defaults(func=cmd_scrub)
    
    # deep-snitch (comprehensive security audit)
    p = sub.add_parser("deep-snitch", help="Deep Snitch: security audit (use: deep-snitch [@1|hash])")
    p.add_argument("composer", nargs="?", help="Composer ref: @1, hash prefix, name (optional)")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--since", help="Time filter: 1h, 1d, 7d")
    p.add_argument("--category", help="Pattern category: secrets,shell_exfil,code_execution,dangerous_paths,obfuscation,prompt_injection,data_exfil,suspicious_behavior,all")
    p.add_argument("--severity", choices=["critical", "high", "medium", "low", "info"], help="Minimum severity")
    p.add_argument("--files", action="store_true", help="Show files exposed in context")
    p.add_argument("--endpoints", action="store_true", help="Show configured endpoints/services")
    p.add_argument("--mcp", action="store_true", help="Show MCP server access")
    p.add_argument("--models", action="store_true", help="Show models used and data sent")
    p.add_argument("--patterns", action="store_true", help="Scan for suspicious patterns (K-REF output)")
    p.add_argument("--all", action="store_true", help="Full audit: patterns + endpoints + files + mcp")
    p.add_argument("--summary", action="store_true", help="Summary only (no K-REFs)")
    p.add_argument("-n", "--limit", type=int, default=200, help="Max findings per category")
    p.add_argument("--emit-kref", action="store_true", help="Output as K-REFs (default)")
    p.set_defaults(func=cmd_deep_snitch)
    
    # models-info (JOIN both data stores for model info)
    p = sub.add_parser("models-info", help="Model info: config + usage + pricing (JOINs both data stores)")
    p.add_argument("--usage", action="store_true", help="Show usage stats from ai-tracking")
    p.add_argument("--config", action="store_true", help="Show config from serverConfig")
    p.add_argument("--migrations", action="store_true", help="Show model migrations")
    p.add_argument("--all", action="store_true", help="Show everything (default)")
    p.set_defaults(func=cmd_models_info)
    
    # url-audit (find URLs with secrets in tool calls - both stores)
    p = sub.add_parser("url-audit", help="Find URLs in tool calls (use: url-audit [@1|hash])")
    p.add_argument("composer", nargs="?", help="Composer ref: @1, hash prefix, name (optional)")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--pattern", help="Additional pattern to search in URLs")
    p.add_argument("--secrets-only", action="store_true", help="Only show URLs with potential secrets")
    p.add_argument("-n", "--limit", type=int, default=50, help="Max results")
    p.set_defaults(func=cmd_url_audit)
    
    # exfil-audit (comprehensive secret exfiltration audit - ALL tools, ALL args)
    p = sub.add_parser("exfil-audit", help="Comprehensive secret exfiltration audit (ALL tools, ALL args, both stores)")
    p.add_argument("--composer", help="Audit specific composer")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--since", help="Time filter: 1h, 1d, 7d")
    p.add_argument("--tool", help="Filter by tool name")
    p.add_argument("--summary", action="store_true", help="Summary only, no details")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max findings")
    p.set_defaults(func=cmd_exfil_audit)
    
    # full-audit (ALL vectors: prompts, responses, tools, MCP, context, shell, images)
    p = sub.add_parser("full-audit", help="Full communication audit - ALL vectors in/out")
    p.add_argument("--composer", help="Audit specific composer")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--since", help="Time filter: 1h, 1d, 7d")
    p.add_argument("--vector", help="Filter: prompt,response,tool,mcp,shell,context,image")
    p.add_argument("--summary", action="store_true", help="Summary only")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max findings per vector")
    p.set_defaults(func=cmd_full_audit)
    
    # pattern-scan (find UUIDs, hashes, any pattern with K-REFS output)
    p = sub.add_parser("pattern-scan", help="Find UUIDs, hashes, secrets, custom patterns (K-REFS output)")
    p.add_argument("--composer", help="Scan specific composer")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--pattern", help="Custom regex pattern")
    p.add_argument("--uuids", action="store_true", help="Find all UUIDs")
    p.add_argument("--hashes", action="store_true", help="Find hex hashes (32+ chars)")
    p.add_argument("--secrets", action="store_true", help="Find secrets (API keys, passwords, etc)")
    p.add_argument("--all", action="store_true", help="Find everything")
    p.add_argument("--emit-redact", action="store_true", help="Output redaction commands (file:line:col_start:col_end:len)")
    p.add_argument("--emit-sed", action="store_true", help="Output sed-compatible redaction script")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max findings")
    p.set_defaults(func=cmd_pattern_scan)
    
    # mask-in-place (replace secrets with *** same length - file size unchanged)
    p = sub.add_parser("mask-in-place", help="Mask secrets in-place (same length, file size unchanged)")
    p.add_argument("--composer", help="Mask specific composer transcript")
    p.add_argument("--workspace", help="Workspace filter")
    p.add_argument("--pattern", help="Custom pattern to mask")
    p.add_argument("--secrets", action="store_true", help="Mask detected secrets")
    p.add_argument("--uuids", action="store_true", help="Mask UUIDs")
    p.add_argument("--dry-run", action="store_true", help="Show what would be masked")
    p.add_argument("--mask-char", default="*", help="Character to use for masking (default: *)")
    p.add_argument("--backup", action="store_true", default=True, help="Create .bak backup")
    p.add_argument("--no-backup", action="store_true", help="Skip backup")
    p.add_argument("--cursor-stopped", action="store_true", help="I confirm Cursor is not running")
    p.add_argument("--force", action="store_true", help="Modify files even if in use (dangerous!)")
    p.set_defaults(func=cmd_mask_in_place)
    
    # audit (unified composable audit framework)
    p = sub.add_parser("audit", help="Composable audit: surfaces × patterns")
    p.add_argument("--surface", action="append", dest="surfaces",
                   help="Add surface: transcript, sqlite, config (can repeat)")
    p.add_argument("--patterns", action="append", dest="pattern_sets",
                   help="Add pattern set: secrets, uuids, hashes, urls, paths, git (can repeat)")
    p.add_argument("--pattern", help="Custom regex pattern")
    p.add_argument("--pattern-file", help="Load patterns from YAML file")
    p.add_argument("--pattern-type", choices=["regex", "literal", "glob", "fuzzy", "prefix", "suffix", "contains"],
                   default="regex", help="Match type for --pattern")
    p.add_argument("--composer", help="Filter transcripts by composer")
    p.add_argument("--workspace", help="Filter by workspace")
    p.add_argument("--emit-redact", action="store_true", help="Output redaction commands")
    p.add_argument("--emit-kref", action="store_true", help="Output K-REF pointers (default)")
    p.add_argument("--mask", action="store_true", help="Apply masks in-place")
    p.add_argument("--dry-run", action="store_true", help="Dry run for --mask")
    p.add_argument("--preserve-ws", action="store_true", default=True, help="Preserve whitespace when masking (default)")
    p.add_argument("--no-preserve-ws", action="store_true", help="Don't preserve whitespace")
    p.add_argument("--cursor-stopped", action="store_true", help="I confirm Cursor is not running")
    p.add_argument("--force", action="store_true", help="Modify files even if in use (dangerous!)")
    p.add_argument("-n", "--limit", type=int, default=100, help="Max findings")
    p.set_defaults(func=cmd_audit)
    
    # agent-tools
    p = sub.add_parser("agent-tools", help="Cached tool results (use: agent-tools [@1|hash])")
    p.add_argument("composer", nargs="?", help="Composer ref: @1, hash prefix, name (optional)")
    p.add_argument("--workspace", help="Workspace name/path")
    p.add_argument("--show", help="Show specific tool result by UUID")
    p.add_argument("-n", "--limit", type=int, default=20, help="Max results")
    p.set_defaults(func=cmd_agent_tools)
    
    # dotcursor-terminals
    p = sub.add_parser("dotcursor-terminals", help="Terminal state from ~/.cursor")
    p.add_argument("--workspace", help="Workspace name/path")
    p.add_argument("--show", help="Show specific terminal by ID")
    p.set_defaults(func=cmd_dotcursor_terminals)
    
    # mcp-tools
    p = sub.add_parser("mcp-tools", help="MCP tool schemas from ~/.cursor")
    p.add_argument("--workspace", help="Workspace name/path")
    p.add_argument("--server", help="Filter by MCP server name")
    p.add_argument("--show", help="Show specific tool schema")
    p.set_defaults(func=cmd_mcp_tools)
    
    # extensions
    p = sub.add_parser("extensions", help="Cursor extensions from ~/.cursor")
    p.add_argument("--sort", choices=["date", "name", "publisher", "size"], default="date",
                   help="Sort by: date (default), name, publisher, size")
    p.add_argument("-n", "--limit", type=int, help="Max results")
    p.set_defaults(func=cmd_extensions)

    args = ap.parse_args()
    
    # Initialize debug mode if requested
    if getattr(args, 'debug', False):
        set_debug(True)
        debug("Debug mode enabled")
        debug("Command: %s", args.cmd)
    
    # Initialize source tracking if requested
    if getattr(args, 'sources', False):
        set_sources_mode(True)
    
    args.func(args)
    
    # Print data sources if --sources flag was set
    if getattr(args, 'sources', False):
        print_sources()

# END SNIFFABLE REGION
# Below is implementation: exceptions, __all__, logging, cli(), helpers, cmd_*.
# Read if debugging, extending, or learning internals.

# Additional imports
import json
import logging
import os
import re
import sqlite3
import sys
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

# AUDIT FRAMEWORK - Composable Surfaces × Patterns
# Architecture: SURFACES (where) × PATTERNS (what) = FINDINGS
#
# Architecture:
#   SURFACES (where to look) × PATTERNS (what to find) = FINDINGS
#
# Add new surfaces independently (transcripts, databases, configs, etc.)
# Add new patterns independently (secrets, UUIDs, URLs, etc.)
# They compose automatically via the AuditRunner.
#
# Usage:
#   runner = AuditRunner()
#   runner.add_surface(TranscriptSurface(workspace="moollm"))
#   runner.add_surface(SqliteSurface(db="state.vscdb"))
#   runner.add_pattern_set("secrets")
#   runner.add_pattern_set("uuids")
#   for finding in runner.scan():
#       print(finding)

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum

class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class MatchType(Enum):
    REGEX = "regex"       # Regular expression (default)
    LITERAL = "literal"   # Exact string match
    GLOB = "glob"         # Shell-style glob (*?, [])
    FUZZY = "fuzzy"       # Fuzzy match (Levenshtein distance)
    PREFIX = "prefix"     # Starts with
    SUFFIX = "suffix"     # Ends with
    CONTAINS = "contains" # Substring match


@dataclass
class AuditPattern:
    """A pattern to search for with configurable match type."""
    name: str
    pattern: str
    match_type: MatchType = MatchType.REGEX
    severity: Severity = Severity.INFO
    category: str = "general"
    description: str = ""
    redact_label: str = ""  # e.g., "[SSH_KEY]" shown when masked
    preserve_whitespace: bool = True  # Keep spaces/newlines in redacted output
    fuzzy_threshold: float = 0.8  # For fuzzy matching (0-1)
    compiled: Any = field(default=None, repr=False)
    
    def __post_init__(self):
        import re
        import fnmatch
        
        if self.match_type == MatchType.REGEX:
            self.compiled = re.compile(self.pattern)
        elif self.match_type == MatchType.LITERAL:
            self.compiled = re.compile(re.escape(self.pattern))
        elif self.match_type == MatchType.GLOB:
            # Convert glob to regex for finding within text
            # Replace * with \S* (non-whitespace) and ? with \S
            glob_regex = re.escape(self.pattern)
            glob_regex = glob_regex.replace(r'\*', r'\S*')
            glob_regex = glob_regex.replace(r'\?', r'\S')
            self.compiled = re.compile(glob_regex)
        elif self.match_type == MatchType.PREFIX:
            # Find words/tokens starting with prefix
            self.compiled = re.compile(r'(?<![a-zA-Z0-9_])' + re.escape(self.pattern) + r'\S*')
        elif self.match_type == MatchType.SUFFIX:
            self.compiled = re.compile(r'\S*' + re.escape(self.pattern) + r'(?![a-zA-Z0-9_])')
        elif self.match_type == MatchType.CONTAINS:
            self.compiled = re.compile(re.escape(self.pattern))
        elif self.match_type == MatchType.FUZZY:
            # Fuzzy uses different matching logic
            self.compiled = None
        else:
            self.compiled = re.compile(self.pattern)
    
    def find_matches(self, text: str) -> Iterator[Tuple[int, int, str]]:
        """Yield (start, end, matched_text) tuples."""
        if self.match_type == MatchType.FUZZY:
            # Simple fuzzy: sliding window with edit distance
            yield from self._fuzzy_match(text)
        elif self.compiled:
            for m in self.compiled.finditer(text):
                yield m.start(), m.end(), m.group()
    
    def _fuzzy_match(self, text: str) -> Iterator[Tuple[int, int, str]]:
        """Fuzzy matching using Levenshtein-like ratio.
        
        Note: This is O(n) but with a large constant factor.
        For very large texts, consider pre-filtering with contains.
        """
        pattern_len = len(self.pattern)
        if pattern_len < 3:
            return
        
        # Skip if text is too large (performance safeguard)
        if len(text) > 500000:  # 500KB limit for fuzzy
            return
        
        # Pre-filter: only check around potential matches
        pattern_lower = self.pattern.lower()
        text_lower = text.lower()
        
        # Find rough matches using 3-char prefix
        prefix = pattern_lower[:3]
        positions = []
        start = 0
        while True:
            pos = text_lower.find(prefix, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        
        # Check windows around each rough match
        seen = set()
        for pos in positions:
            for offset in range(-2, 3):
                for wsize in [pattern_len - 1, pattern_len, pattern_len + 1]:
                    if wsize < 3:
                        continue
                    i = pos + offset
                    if i < 0 or i + wsize > len(text):
                        continue
                    if (i, wsize) in seen:
                        continue
                    seen.add((i, wsize))
                    
                    candidate = text[i:i + wsize]
                    ratio = self._similarity(pattern_lower, candidate.lower())
                    if ratio >= self.fuzzy_threshold:
                        yield i, i + wsize, candidate
    
    def _similarity(self, s1: str, s2: str) -> float:
        """Simple similarity ratio (0-1)."""
        if not s1 or not s2:
            return 0.0
        matches = sum(1 for a, b in zip(s1, s2) if a == b)
        return matches / max(len(s1), len(s2))
    
    @classmethod
    def from_dict(cls, d: Dict) -> "AuditPattern":
        """Create pattern from dictionary (YAML config)."""
        match_type = MatchType(d.get("type", "regex"))
        severity = Severity(d.get("severity", "info"))
        return cls(
            name=d.get("name", "unnamed"),
            pattern=d.get("pattern", ""),
            match_type=match_type,
            severity=severity,
            category=d.get("category", "custom"),
            description=d.get("description", ""),
            redact_label=d.get("redact_label", ""),
            preserve_whitespace=d.get("preserve_whitespace", True),
            fuzzy_threshold=d.get("fuzzy_threshold", 0.8),
        )


def is_file_in_use(path: str) -> Dict[str, Any]:
    """Check if a file is in use by another process (using lsof).
    
    Returns:
        {"in_use": bool, "processes": [...], "cursor": bool}
    
    TODO: PORTING
    - macOS/Linux: lsof (current implementation)
    - Windows: use handle.exe from Sysinternals, or:
        import msvcrt; msvcrt.locking() to test lock
        or: win32file.CreateFile with SHARE_NONE
    - Cross-platform: try fcntl.flock() first, fall back to OS-specific
    """
    import subprocess
    import sys
    
    result = {"in_use": False, "processes": [], "cursor": False}
    
    # TODO: PORTING - Windows implementation
    if sys.platform == "win32":
        # Windows: would use handle.exe or win32file
        # For now, assume not in use (less safe but functional)
        return result
    
    # macOS / Linux: use lsof
    try:
        proc = subprocess.run(
            ["lsof", path],  # TODO: PORTING - lsof path may vary: /usr/bin/lsof, /usr/sbin/lsof
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if proc.returncode == 0 and proc.stdout.strip():
            lines = proc.stdout.strip().split('\n')
            if len(lines) > 1:
                result["in_use"] = True
                for line in lines[1:]:
                    parts = line.split()
                    if parts:
                        proc_name = parts[0]
                        result["processes"].append(proc_name)
                        if "cursor" in proc_name.lower() or "Cursor" in proc_name:
                            result["cursor"] = True
    except subprocess.TimeoutExpired:
        pass
    except FileNotFoundError:
        pass  # lsof not installed
    except Exception:
        pass
    
    return result


def check_cursor_running() -> Dict[str, Any]:
    """Check if Cursor is running.
    
    Returns:
        {"running": bool, "pids": [...], "warning": str}
    
    TODO: PORTING
    - macOS/Linux: pgrep (current implementation)
    - Windows: tasklist /FI "IMAGENAME eq Cursor.exe"
        or: wmic process where "name='Cursor.exe'" get processid
        or: psutil.process_iter() cross-platform
    - Cross-platform: consider psutil library (pip install psutil)
    """
    import subprocess
    import sys
    
    result = {"running": False, "pids": [], "warning": ""}
    
    # TODO: PORTING - Windows implementation
    if sys.platform == "win32":
        try:
            proc = subprocess.run(
                ["tasklist", "/FI", "IMAGENAME eq Cursor.exe", "/NH"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if "Cursor.exe" in proc.stdout:
                result["running"] = True
                result["warning"] = "Cursor is running"
        except Exception:
            pass
        return result
    
    # macOS / Linux: use pgrep
    try:
        proc = subprocess.run(
            ["pgrep", "-f", "Cursor"],  # TODO: PORTING - pgrep flags vary by OS
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if proc.returncode == 0 and proc.stdout.strip():
            result["running"] = True
            result["pids"] = proc.stdout.strip().split('\n')
            result["warning"] = f"Cursor is running (PIDs: {', '.join(result['pids'][:3])})"
    except Exception:
        pass
    
    return result


def mask_preserving_whitespace(text: str, mask_char: str = "*") -> str:
    """Mask text but preserve spaces and newlines.
    
    'sk-proj-abc123\n  def456' → '**************\n  ******'
    """
    result = []
    for ch in text:
        if ch in ' \t\n\r':
            result.append(ch)
        else:
            result.append(mask_char)
    return ''.join(result)


def load_patterns_from_yaml(yaml_path: str) -> List[AuditPattern]:
    """Load pattern definitions from YAML file.
    
    Example YAML:
    ```yaml
    patterns:
      - name: openai_key
        pattern: 'sk-[a-zA-Z0-9]{20,}'
        type: regex
        severity: critical
        category: api_key
        description: OpenAI API key
        redact_label: "[OPENAI_KEY]"
        
      - name: password_literal
        pattern: 'mysecretpassword'
        type: literal
        severity: high
        
      - name: config_file
        pattern: '*.config.json'
        type: glob
        category: sensitive_file
    ```
    """
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    
    patterns = []
    for p in data.get("patterns", []):
        patterns.append(AuditPattern.from_dict(p))
    return patterns


@dataclass
class Finding:
    """A match found during audit."""
    surface: str           # Which surface (transcript, db, config)
    path: str              # File/table path
    line: int              # Line number (1-based)
    col_start: int         # Column start (1-based)
    col_end: int           # Column end (exclusive)
    char_start: int        # Byte offset start
    char_end: int          # Byte offset end
    pattern_name: str      # Pattern that matched
    category: str          # Pattern category
    severity: Severity     # Severity level
    matched: str           # Matched text (masked if sensitive)
    match_type: str = "regex"  # How it was matched
    description: str = "" # Pattern description
    redact_label: str = "" # Label to show when redacted (e.g., "[SSH_KEY]")
    context: str = ""      # Surrounding text
    metadata: Dict = field(default_factory=dict)
    
    def to_kref(self) -> str:
        """Format as K-REF pointer."""
        sev = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🔵", "info": "ℹ️"
              }.get(self.severity.value, "⚪")
        label = f" ({self.redact_label})" if self.redact_label else ""
        desc = f" - {self.description}" if self.description else ""
        return f"{self.path}:{self.line}:{self.col_start}-{self.col_end} # {self.pattern_name}{label} {sev}{desc}"
    
    def to_redact_cmd(self) -> str:
        """Format as redaction command."""
        length = self.char_end - self.char_start
        label = self.redact_label or self.pattern_name
        return f"REDACT:{self.path}:{self.line}:{self.col_start}:{self.col_end}:{length}:{label}"
    
    def format_masked(self, mask_char: str = "*", preserve_ws: bool = True) -> str:
        """Format the matched text with masking."""
        if preserve_ws:
            return mask_preserving_whitespace(self.matched, mask_char)
        else:
            return mask_char * len(self.matched)


class AuditSurface(ABC):
    """Base class for audit surfaces (data sources)."""
    name: str = "base"
    
    @abstractmethod
    def iter_chunks(self, filters: Dict = None) -> Iterator[Tuple[str, str, Dict]]:
        """Yield (path, content, metadata) chunks to scan."""
        pass


class TranscriptSurface(AuditSurface):
    """Scan plaintext transcripts in ~/.cursor/projects/*/agent-transcripts/."""
    name = "transcript"
    
    def __init__(self, workspace: str = None, composer: str = None, since: str = None):
        self.workspace = workspace
        self.composer = composer
        self.since = since
    
    def iter_chunks(self, filters: Dict = None) -> Iterator[Tuple[str, str, Dict]]:
        workspaces = get_dotcursor_workspaces()
        if self.workspace:
            workspaces = [ws for ws in workspaces if self.workspace in ws.get("name", "")]
        
        for ws in workspaces:
            trans_dir = os.path.join(ws["path"], "agent-transcripts")
            if not os.path.isdir(trans_dir):
                continue
            
            for fname in os.listdir(trans_dir):
                if not fname.endswith('.txt'):
                    continue
                if self.composer and not fname.startswith(self.composer):
                    continue
                
                fpath = os.path.join(trans_dir, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    yield fpath, content, {"workspace": ws.get("name"), "composer": fname[:-4]}
                except Exception:
                    continue


class SqliteSurface(AuditSurface):
    """Scan SQLite database contents."""
    name = "sqlite"
    
    def __init__(self, db_path: str = None, tables: List[str] = None, keys: List[str] = None):
        self.db_path = db_path or GLOBAL_DB
        self.tables = tables or ["ItemTable", "cursorDiskKV"]
        self.keys = keys
    
    def iter_chunks(self, filters: Dict = None) -> Iterator[Tuple[str, str, Dict]]:
        if not os.path.exists(self.db_path):
            return
        
        try:
            conn = sqlite3.connect(f"file:{self.db_path}?mode=ro", uri=True)
            cur = conn.cursor()
            
            for table in self.tables:
                try:
                    if table == "ItemTable":
                        cur.execute("SELECT key, value FROM ItemTable")
                    elif table == "cursorDiskKV":
                        cur.execute("SELECT key, value FROM cursorDiskKV")
                    else:
                        continue
                    
                    for key, value in cur.fetchall():
                        if self.keys and not any(k in key for k in self.keys):
                            continue
                        if isinstance(value, bytes):
                            try:
                                value = value.decode('utf-8', errors='replace')
                            except:
                                continue
                        if value:
                            yield f"{self.db_path}:{table}:{key}", str(value), {"table": table, "key": key}
                except sqlite3.Error:
                    continue
            
            conn.close()
        except sqlite3.Error:
            pass


class ConfigSurface(AuditSurface):
    """Scan JSON/YAML config files."""
    name = "config"
    
    def __init__(self, paths: List[str] = None):
        self.paths = paths or []
    
    def iter_chunks(self, filters: Dict = None) -> Iterator[Tuple[str, str, Dict]]:
        for path in self.paths:
            if os.path.exists(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    yield path, content, {"type": "config"}
                except Exception:
                    continue


# Pattern Registry - add patterns by category
# Each pattern can specify: name, pattern, type, severity, category, description, redact_label
PATTERN_REGISTRY: Dict[str, List[AuditPattern]] = {
    "secrets": [
        AuditPattern("openai_key", r'sk-[a-zA-Z0-9]{20,}', MatchType.REGEX, Severity.CRITICAL, 
                    "api_key", "OpenAI API key", "[OPENAI_KEY]"),
        AuditPattern("openai_project", r'sk-proj-[a-zA-Z0-9]{20,}', MatchType.REGEX, Severity.CRITICAL, 
                    "api_key", "OpenAI project key", "[OPENAI_PROJECT_KEY]"),
        AuditPattern("anthropic_key", r'sk-ant-[a-zA-Z0-9]{20,}', MatchType.REGEX, Severity.CRITICAL, 
                    "api_key", "Anthropic API key", "[ANTHROPIC_KEY]"),
        AuditPattern("aws_access", r'AKIA[0-9A-Z]{16}', MatchType.REGEX, Severity.CRITICAL, 
                    "api_key", "AWS access key ID", "[AWS_KEY]"),
        AuditPattern("github_pat", r'ghp_[a-zA-Z0-9]{36}', MatchType.REGEX, Severity.CRITICAL, 
                    "api_key", "GitHub personal access token", "[GITHUB_PAT]"),
        AuditPattern("github_oauth", r'gho_[a-zA-Z0-9]{36}', MatchType.REGEX, Severity.CRITICAL, 
                    "api_key", "GitHub OAuth token", "[GITHUB_OAUTH]"),
        AuditPattern("gitlab_pat", r'glpat-[a-zA-Z0-9\-]{20}', MatchType.REGEX, Severity.CRITICAL, 
                    "api_key", "GitLab personal access token", "[GITLAB_PAT]"),
        AuditPattern("private_key", r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 
                    MatchType.REGEX, Severity.CRITICAL, "crypto", "Private key header", "[PRIVATE_KEY]"),
        AuditPattern("password", r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', MatchType.REGEX, 
                    Severity.HIGH, "credential", "Password assignment", "[PASSWORD]"),
        AuditPattern("api_key_generic", r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 
                    MatchType.REGEX, Severity.HIGH, "credential", "Generic API key", "[API_KEY]"),
        AuditPattern("bearer_token", r'(?i)bearer\s+[a-zA-Z0-9\-_.]{20,}', MatchType.REGEX, 
                    Severity.HIGH, "credential", "Bearer token", "[BEARER_TOKEN]"),
        AuditPattern("jwt", r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+', 
                    MatchType.REGEX, Severity.HIGH, "token", "JSON Web Token", "[JWT]"),
        AuditPattern("url_with_creds", r'https?://[^:/\s]+:[^@\s]+@[^\s]+', MatchType.REGEX, 
                    Severity.CRITICAL, "url", "URL with embedded credentials", "[URL_CREDS]"),
    ],
    "uuids": [
        AuditPattern("uuid", r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', 
                    MatchType.REGEX, Severity.INFO, "identifier", "UUID v4", "[UUID]"),
    ],
    "hashes": [
        AuditPattern("md5", r'(?<![a-fA-F0-9])[a-fA-F0-9]{32}(?![a-fA-F0-9])', MatchType.REGEX, 
                    Severity.INFO, "hash", "MD5 hash", "[MD5]"),
        AuditPattern("sha1", r'(?<![a-fA-F0-9])[a-fA-F0-9]{40}(?![a-fA-F0-9])', MatchType.REGEX, 
                    Severity.INFO, "hash", "SHA-1 hash", "[SHA1]"),
        AuditPattern("sha256", r'(?<![a-fA-F0-9])[a-fA-F0-9]{64}(?![a-fA-F0-9])', MatchType.REGEX, 
                    Severity.INFO, "hash", "SHA-256 hash", "[SHA256]"),
    ],
    "urls": [
        AuditPattern("http_url", r'https?://[^\s<>"\']+', MatchType.REGEX, 
                    Severity.LOW, "url", "HTTP/HTTPS URL"),
        AuditPattern("file_url", r'file://[^\s<>"\']+', MatchType.REGEX, 
                    Severity.MEDIUM, "url", "File URL", "[FILE_URL]"),
    ],
    "paths": [
        AuditPattern("env_file", r'(?i)\.env(?:\.local|\.prod|\.dev)?(?:\s|$|")', MatchType.REGEX, 
                    Severity.HIGH, "sensitive_file", "Environment file", "[ENV_FILE]"),
        AuditPattern("ssh_key", r'(?i)~/.ssh/id_rsa', MatchType.REGEX, Severity.CRITICAL, 
                    "sensitive_file", "SSH private key path", "[SSH_KEY_PATH]"),
        AuditPattern("aws_creds", r'(?i)~/.aws/credentials', MatchType.REGEX, Severity.CRITICAL, 
                    "sensitive_file", "AWS credentials file", "[AWS_CREDS_PATH]"),
        AuditPattern("kube_config", r'(?i)~/.kube/config', MatchType.REGEX, Severity.HIGH, 
                    "sensitive_file", "Kubernetes config", "[KUBE_CONFIG]"),
    ],
    "git": [
        AuditPattern("git_sha_full", r'(?<![a-fA-F0-9])[a-fA-F0-9]{40}(?![a-fA-F0-9])', 
                    MatchType.REGEX, Severity.INFO, "git", "Full git SHA", "[GIT_SHA]"),
        AuditPattern("git_sha_short", r'(?i)(?:commit|checkout)\s+([a-fA-F0-9]{7,40})', 
                    MatchType.REGEX, Severity.INFO, "git", "Git commit reference", "[GIT_REF]"),
    ],
    
    # DEEP SNITCH PATTERNS - Comprehensive suspicious activity detection
    "shell_exfil": [
        AuditPattern("curl_post", r'curl\s+.*(-d|--data|--data-\w+|-F|--form)', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "curl sending data", "[CURL_POST]"),
        AuditPattern("curl_upload", r'curl\s+.*(-T|--upload-file)', MatchType.REGEX,
                    Severity.CRITICAL, "exfiltration", "curl file upload", "[CURL_UPLOAD]"),
        AuditPattern("wget_post", r'wget\s+.*--post', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "wget POST request", "[WGET_POST]"),
        AuditPattern("netcat", r'\b(nc|netcat|ncat)\s+', MatchType.REGEX,
                    Severity.CRITICAL, "exfiltration", "netcat (raw network)", "[NETCAT]"),
        AuditPattern("ssh_command", r'ssh\s+.*@', MatchType.REGEX,
                    Severity.HIGH, "network", "SSH connection", "[SSH]"),
        AuditPattern("scp_transfer", r'scp\s+', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "SCP file transfer", "[SCP]"),
        AuditPattern("rsync_remote", r'rsync\s+.*:', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "rsync to remote", "[RSYNC]"),
        AuditPattern("base64_pipe", r'\|\s*base64', MatchType.REGEX,
                    Severity.MEDIUM, "obfuscation", "piping to base64", "[BASE64_PIPE]"),
        AuditPattern("reverse_shell", r'bash\s+-i\s+>&|/dev/tcp/', MatchType.REGEX,
                    Severity.CRITICAL, "attack", "Reverse shell pattern", "[REVERSE_SHELL]"),
    ],
    "code_execution": [
        AuditPattern("python_eval", r'\beval\s*\(', MatchType.REGEX,
                    Severity.HIGH, "code_exec", "Python eval()", "[EVAL]"),
        AuditPattern("python_exec", r'\bexec\s*\(', MatchType.REGEX,
                    Severity.HIGH, "code_exec", "Python exec()", "[EXEC]"),
        AuditPattern("python_compile", r'\bcompile\s*\([^)]*,\s*[\'"][^\'"]*[\'"]\s*,\s*[\'"]exec', MatchType.REGEX,
                    Severity.HIGH, "code_exec", "Python compile() for exec", "[COMPILE]"),
        AuditPattern("subprocess_shell", r'subprocess\.\w+\([^)]*shell\s*=\s*True', MatchType.REGEX,
                    Severity.HIGH, "code_exec", "subprocess with shell=True", "[SUBPROCESS_SHELL]"),
        AuditPattern("os_system", r'\bos\.system\s*\(', MatchType.REGEX,
                    Severity.MEDIUM, "code_exec", "os.system() call", "[OS_SYSTEM]"),
        AuditPattern("os_popen", r'\bos\.popen\s*\(', MatchType.REGEX,
                    Severity.MEDIUM, "code_exec", "os.popen() call", "[OS_POPEN]"),
        AuditPattern("pickle_load", r'pickle\.loads?\s*\(', MatchType.REGEX,
                    Severity.HIGH, "code_exec", "pickle deserialization", "[PICKLE]"),
        AuditPattern("yaml_unsafe", r'yaml\.(?:load|unsafe_load)\s*\([^)]*\)', MatchType.REGEX,
                    Severity.HIGH, "code_exec", "Unsafe YAML load", "[YAML_UNSAFE]"),
        AuditPattern("import_module", r'__import__\s*\(|importlib\.import_module', MatchType.REGEX,
                    Severity.MEDIUM, "code_exec", "Dynamic import", "[DYNAMIC_IMPORT]"),
    ],
    "dangerous_paths": [
        AuditPattern("etc_passwd", r'/etc/passwd', MatchType.REGEX,
                    Severity.CRITICAL, "system_file", "Password file access", "[ETC_PASSWD]"),
        AuditPattern("etc_shadow", r'/etc/shadow', MatchType.REGEX,
                    Severity.CRITICAL, "system_file", "Shadow password file", "[ETC_SHADOW]"),
        AuditPattern("proc_access", r'/proc/\d+/', MatchType.REGEX,
                    Severity.HIGH, "system_file", "Process info access", "[PROC]"),
        AuditPattern("home_ssh", r'~/\.ssh/|/home/[^/]+/\.ssh/', MatchType.REGEX,
                    Severity.CRITICAL, "sensitive_dir", "SSH directory access", "[SSH_DIR]"),
        AuditPattern("home_gnupg", r'~/\.gnupg|/home/[^/]+/\.gnupg', MatchType.REGEX,
                    Severity.CRITICAL, "sensitive_dir", "GPG directory access", "[GPG_DIR]"),
        AuditPattern("browser_profile", r'(Chrome|Firefox|Safari)/.*/(Cookies|Login|passwords)', MatchType.REGEX,
                    Severity.CRITICAL, "sensitive_file", "Browser credential file", "[BROWSER_CREDS]"),
        AuditPattern("keychain", r'~/Library/Keychains|\.keychain', MatchType.REGEX,
                    Severity.CRITICAL, "sensitive_file", "macOS Keychain access", "[KEYCHAIN]"),
        AuditPattern("history_file", r'~/\.(bash_history|zsh_history|python_history)', MatchType.REGEX,
                    Severity.HIGH, "sensitive_file", "Shell history file", "[HISTORY]"),
    ],
    "obfuscation": [
        AuditPattern("base64_decode", r'base64\.(b64)?decode|atob\s*\(', MatchType.REGEX,
                    Severity.MEDIUM, "obfuscation", "Base64 decoding", "[B64_DECODE]"),
        AuditPattern("hex_decode", r'bytes\.fromhex|binascii\.unhexlify', MatchType.REGEX,
                    Severity.MEDIUM, "obfuscation", "Hex decoding", "[HEX_DECODE]"),
        AuditPattern("rot13", r'codecs\.(decode|encode)\([^)]*rot', MatchType.REGEX,
                    Severity.MEDIUM, "obfuscation", "ROT13 encoding", "[ROT13]"),
        AuditPattern("chr_ord_build", r'chr\s*\(\s*\d+\s*\)', MatchType.REGEX,
                    Severity.MEDIUM, "obfuscation", "Building strings with chr()", "[CHR_BUILD]"),
        AuditPattern("unicode_escape", r'\\u[0-9a-fA-F]{4}.*\\u[0-9a-fA-F]{4}', MatchType.REGEX,
                    Severity.LOW, "obfuscation", "Unicode escape sequences", "[UNICODE_ESC]"),
        AuditPattern("long_hex_string", r'0x[0-9a-fA-F]{32,}', MatchType.REGEX,
                    Severity.MEDIUM, "obfuscation", "Long hex literal", "[LONG_HEX]"),
    ],
    "prompt_injection": [
        AuditPattern("ignore_previous", r'(?i)ignore\s+(all\s+)?previous\s+instructions?', MatchType.REGEX,
                    Severity.CRITICAL, "injection", "Prompt injection attempt", "[IGNORE_PREV]"),
        AuditPattern("new_instructions", r'(?i)new\s+instructions?:|your\s+new\s+task', MatchType.REGEX,
                    Severity.HIGH, "injection", "Instruction override attempt", "[NEW_INST]"),
        AuditPattern("system_prompt_leak", r'(?i)reveal\s+(your\s+)?system\s+prompt|what\s+are\s+your\s+instructions', MatchType.REGEX,
                    Severity.MEDIUM, "injection", "System prompt extraction", "[SYS_PROMPT_LEAK]"),
        AuditPattern("jailbreak_dan", r'(?i)\bDAN\b.*do\s+anything\s+now|act\s+as\s+DAN', MatchType.REGEX,
                    Severity.HIGH, "injection", "DAN jailbreak attempt", "[DAN_JAILBREAK]"),
        AuditPattern("roleplay_bypass", r'(?i)pretend\s+you\s+are|you\s+are\s+now\s+a|roleplay\s+as', MatchType.REGEX,
                    Severity.MEDIUM, "injection", "Roleplay bypass attempt", "[ROLEPLAY]"),
    ],
    "data_exfil": [
        AuditPattern("requests_post", r'requests\.(post|put|patch)\s*\(', MatchType.REGEX,
                    Severity.MEDIUM, "exfiltration", "HTTP POST via requests", "[REQUESTS_POST]"),
        AuditPattern("urllib_post", r'urllib\.request\.urlopen.*data\s*=', MatchType.REGEX,
                    Severity.MEDIUM, "exfiltration", "HTTP POST via urllib", "[URLLIB_POST]"),
        AuditPattern("socket_connect", r'socket\.socket\([^)]*\).*\.connect\s*\(', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "Raw socket connection", "[SOCKET]"),
        AuditPattern("webhook_url", r'https?://.*webhook|hooks\.(slack|discord)', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "Webhook URL", "[WEBHOOK]"),
        AuditPattern("pastebin", r'https?://(pastebin\.com|paste\.ee|hastebin)', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "Pastebin service", "[PASTEBIN]"),
        AuditPattern("file_upload_service", r'https?://(file\.io|transfer\.sh|0x0\.st)', MatchType.REGEX,
                    Severity.CRITICAL, "exfiltration", "File upload service", "[FILE_UPLOAD]"),
        AuditPattern("ngrok_tunnel", r'https?://[a-z0-9]+\.ngrok\.io', MatchType.REGEX,
                    Severity.HIGH, "exfiltration", "Ngrok tunnel", "[NGROK]"),
    ],
    "suspicious_behavior": [
        AuditPattern("disable_ssl", r'verify\s*=\s*False|CERT_NONE', MatchType.REGEX,
                    Severity.HIGH, "security", "SSL verification disabled", "[NO_SSL]"),
        AuditPattern("temp_file_exec", r'/tmp/[^/]+\.(sh|py|exe|bin)', MatchType.REGEX,
                    Severity.HIGH, "code_exec", "Executable in /tmp", "[TMP_EXEC]"),
        AuditPattern("cron_modify", r'crontab\s+-|/etc/cron', MatchType.REGEX,
                    Severity.CRITICAL, "persistence", "Cron job modification", "[CRON]"),
        AuditPattern("startup_modify", r'~/.bashrc|~/.profile|~/.zshrc.*>>', MatchType.REGEX,
                    Severity.HIGH, "persistence", "Shell startup modification", "[STARTUP]"),
        AuditPattern("kill_process", r'\bkill\s+-9|\bpkill\b|\bkillall\b', MatchType.REGEX,
                    Severity.MEDIUM, "system", "Process termination", "[KILL]"),
        AuditPattern("chmod_exec", r'chmod\s+[+0-7]*[x7]', MatchType.REGEX,
                    Severity.MEDIUM, "code_exec", "Making file executable", "[CHMOD_X]"),
        AuditPattern("rm_rf", r'rm\s+(-rf|-fr|--force)', MatchType.REGEX,
                    Severity.HIGH, "destructive", "Forced recursive delete", "[RM_RF]"),
    ],
}


class AuditRunner:
    """Runs audits across surfaces with patterns. Composable."""
    
    def __init__(self):
        self.surfaces: List[AuditSurface] = []
        self.patterns: List[AuditPattern] = []
    
    def add_surface(self, surface: AuditSurface) -> "AuditRunner":
        """Add a surface to scan."""
        self.surfaces.append(surface)
        return self
    
    def add_pattern(self, pattern: AuditPattern) -> "AuditRunner":
        """Add a single pattern."""
        self.patterns.append(pattern)
        return self
    
    def add_pattern_set(self, name: str) -> "AuditRunner":
        """Add a registered pattern set by name."""
        if name in PATTERN_REGISTRY:
            self.patterns.extend(PATTERN_REGISTRY[name])
        return self
    
    def add_custom_pattern(self, regex: str, name: str = "custom", 
                          severity: Severity = Severity.INFO) -> "AuditRunner":
        """Add a custom regex pattern."""
        self.patterns.append(AuditPattern(name, regex, severity, "custom"))
        return self
    
    def add_patterns_from_yaml(self, yaml_path: str) -> "AuditRunner":
        """Load patterns from YAML config file."""
        self.patterns.extend(load_patterns_from_yaml(yaml_path))
        return self
    
    def scan(self, limit: int = 1000) -> Iterator[Finding]:
        """Run audit and yield findings."""
        count = 0
        
        for surface in self.surfaces:
            for path, content, metadata in surface.iter_chunks():
                if count >= limit:
                    return
                
                # Build line/column mappings
                lines = content.split('\n')
                char_to_line = []
                char_to_col = []
                for i, line in enumerate(lines):
                    for c in range(len(line)):
                        char_to_line.append(i + 1)
                        char_to_col.append(c + 1)
                    char_to_line.append(i + 1)
                    char_to_col.append(len(line) + 1)
                
                for pattern in self.patterns:
                    # Use the pattern's find_matches method (supports all match types)
                    for start, end, matched in pattern.find_matches(content):
                        if count >= limit:
                            return
                        
                        line = char_to_line[start] if start < len(char_to_line) else len(lines)
                        col_s = char_to_col[start] if start < len(char_to_col) else 1
                        col_e = char_to_col[end-1] + 1 if end-1 < len(char_to_col) else col_s
                        
                        # Mask sensitive matches (preserve whitespace)
                        if pattern.severity in (Severity.CRITICAL, Severity.HIGH):
                            masked = mask_preserving_whitespace(matched, '*')
                            # Truncate for display but show actual length
                            if len(masked) > 60:
                                display = masked[:30] + f"...({len(matched)} chars)..." + masked[-20:]
                            else:
                                display = masked
                        else:
                            if len(matched) > 60:
                                display = matched[:30] + '...' + matched[-20:]
                            else:
                                display = matched
                        
                        yield Finding(
                            surface=surface.name,
                            path=path,
                            line=line,
                            col_start=col_s,
                            col_end=col_e,
                            char_start=start,
                            char_end=end,
                            pattern_name=pattern.name,
                            category=pattern.category,
                            severity=pattern.severity,
                            matched=display,
                            match_type=pattern.match_type.value,
                            description=pattern.description,
                            redact_label=pattern.redact_label,
                            metadata=metadata
                        )
                        count += 1
    
    def mask_in_place(self, mask_char: str = "*", dry_run: bool = True,
                      backup: bool = True, preserve_whitespace: bool = True,
                      force: bool = False, cursor_stopped: bool = False) -> List[Dict]:
        """Apply fixed-length masks to all findings (file size unchanged).

        Args:
            mask_char: Character to use for masking (default: *)
            dry_run: If True, don't actually write files
            backup: Create .bak files before modifying
            preserve_whitespace: Keep spaces and newlines in masked output
            force: If True, modify files even if in use (dangerous!)
            cursor_stopped: If True, skip the Cursor running check
        """
        results = []
        
        # Check if Cursor is running (unless user says it's stopped)
        if not dry_run and not cursor_stopped:
            cursor_status = check_cursor_running()
            if cursor_status["running"] and not force:
                return [{
                    "error": "Cursor is running",
                    "warning": cursor_status["warning"],
                    "hint": "Quit Cursor first, or use --cursor-stopped if you're sure, or --force to override"
                }]

        # Group findings by file
        by_file: Dict[str, List[Finding]] = {}
        for finding in self.scan():
            if finding.surface != "transcript":
                continue  # Only mask transcript files
            by_file.setdefault(finding.path, []).append(finding)

        for path, findings in by_file.items():
            # Check if file is in use (unless forcing)
            if not dry_run and not force:
                file_status = is_file_in_use(path)
                if file_status["in_use"]:
                    results.append({
                        "path": path,
                        "error": "File in use",
                        "processes": file_status["processes"],
                        "cursor": file_status["cursor"],
                        "hint": "File is locked by another process"
                    })
                    continue
            
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                original_size = len(content)
                original_content = content
            except Exception as e:
                results.append({"path": path, "error": str(e)})
                continue
            
            # Sort by position descending to preserve offsets
            findings.sort(key=lambda f: f.char_start, reverse=True)
            
            masked_types = []
            for f in findings:
                original_text = content[f.char_start:f.char_end]
                
                if preserve_whitespace:
                    # Preserve spaces and newlines
                    mask = mask_preserving_whitespace(original_text, mask_char)
                else:
                    mask = mask_char * (f.char_end - f.char_start)
                
                content = content[:f.char_start] + mask + content[f.char_end:]
                masked_types.append(f.redact_label or f.pattern_name)
            
            # Verify size unchanged
            if len(content) != original_size:
                results.append({"path": path, "error": "Size mismatch!"})
                continue
            
            if not dry_run:
                if backup:
                    with open(path + '.bak', 'w', encoding='utf-8') as f:
                        f.write(original_content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            results.append({
                "path": path,
                "findings": len(findings),
                "types": list(set(masked_types)),
                "size": original_size,
                "preserved_whitespace": preserve_whitespace,
                "dry_run": dry_run
            })
        
        return results
    
    def emit_redact_commands(self) -> Iterator[str]:
        """Emit redaction commands for external processing."""
        yield "# REDACT format: file:line:col_start:col_end:length:type"
        for f in self.scan():
            yield f.to_redact_cmd()


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

# ═══════════════════════════════════════════════════════════════════════════════
# DATA SOURCE TRACKING - "Teach me to fish" feature
# ═══════════════════════════════════════════════════════════════════════════════
# When --sources is set, we track all databases/files read and print them at the
# end. This allows LLMs to learn where the data comes from and query it directly.

SOURCES_MODE = False
_data_sources: Dict[str, set] = {
    "databases": set(),
    "tables": set(),
    "files": set(),
    "directories": set(),
    "sql_queries": set(),
}

def set_sources_mode(enabled: bool) -> None:
    """Enable data source tracking for LLM self-service."""
    global SOURCES_MODE
    SOURCES_MODE = enabled

def register_source(source_type: str, path_or_query: str, table: str = None) -> None:
    """Register a data source for later reporting.
    
    Args:
        source_type: One of 'database', 'file', 'directory', 'sql'
        path_or_query: The file path, database path, or SQL query
        table: Optional table name for database sources
    """
    if not SOURCES_MODE:
        return
    if source_type == "database":
        _data_sources["databases"].add(str(path_or_query))
        if table:
            _data_sources["tables"].add(table)
    elif source_type == "file":
        _data_sources["files"].add(str(path_or_query))
    elif source_type == "directory":
        _data_sources["directories"].add(str(path_or_query))
    elif source_type == "sql":
        # Truncate long queries
        query = str(path_or_query).strip()[:200]
        _data_sources["sql_queries"].add(query)

def print_sources() -> None:
    """Print all registered data sources for LLM self-service."""
    print("\n" + "═" * 70)
    print("DATA SOURCES — Query these directly for raw access")
    print("═" * 70)
    
    if _data_sources["databases"]:
        print("\n📁 DATABASES (SQLite - use: sqlite3 <path>):")
        for db in sorted(_data_sources["databases"]):
            print(f"   {db}")
    
    if _data_sources["tables"]:
        print("\n📊 TABLES queried:")
        for t in sorted(_data_sources["tables"]):
            print(f"   {t}")
    
    if _data_sources["sql_queries"]:
        print("\n🔍 SQL QUERIES used (adapt for your needs):")
        for q in list(_data_sources["sql_queries"])[:10]:
            print(f"   {q}...")
    
    if _data_sources["files"]:
        print("\n📄 FILES read:")
        for f in sorted(_data_sources["files"]):
            print(f"   {f}")
    
    if _data_sources["directories"]:
        print("\n📂 DIRECTORIES scanned:")
        for d in sorted(_data_sources["directories"]):
            print(f"   {d}")
    
    print("\n" + "─" * 70)
    print("TIP: Use 'sqlite3 <db_path> \".tables\"' to list all tables")
    print("TIP: Use 'sqlite3 <db_path> \".schema <table>\"' to see schema")
    print("TIP: Use 'sqlite3 <db_path> \"SELECT * FROM <table> LIMIT 5\"' to sample data")
    print("═" * 70)


# ═══════════════════════════════════════════════════════════════════════════════
# OUTPUT FORMAT HANDLING
# ═══════════════════════════════════════════════════════════════════════════════
# Unified output format system. Commands declare which formats they support.
# Use get_output_format(args) to get the resolved format, and output_data() to emit.

def get_output_format(args, default: str = "text") -> str:
    """Get the output format from args, with legacy --json/--yaml fallback.
    
    Priority:
      1. --output-format (or -f) if specified
      2. --json flag (legacy, hidden)
      3. --yaml flag (legacy, hidden)
      4. default parameter
    
    Returns lowercase format string: "text", "json", "jsonl", "yaml", "csv", "md", etc.
    """
    # Explicit --output-format takes precedence
    if getattr(args, 'output_format', None):
        return args.output_format.lower()
    
    # Legacy flags for backward compatibility
    if getattr(args, 'json', False):
        return "json"
    if getattr(args, 'yaml', False):
        return "yaml"
    
    return default


def format_not_supported(fmt: str, command: str, supported: List[str]) -> None:
    """Print error message for unsupported format and exit."""
    print(f"Error: Format '{fmt}' not supported by '{command}'.", file=sys.stderr)
    print(f"Supported formats: {', '.join(supported)}", file=sys.stderr)
    sys.exit(1)


def output_data(data: Any, fmt: str, command: str = "command",
                supported: List[str] = None, pretty: bool = False) -> None:
    """Output data in the requested format.
    
    Args:
        data: The data to output (dict, list, or string)
        fmt: Output format ("text", "json", "jsonl", "yaml", "csv", "md")
        command: Command name for error messages
        supported: List of supported formats (for error messages)
        pretty: Pretty-print JSON (indent=2)
    
    Supported formats:
        text  - Default, assumes data is already formatted or will be printed by caller
        json  - JSON object/array
        jsonl - JSON Lines (one JSON object per line, for lists)
        yaml  - YAML format
        csv   - CSV (requires list of dicts with consistent keys)
        md    - Markdown table (requires list of dicts)
    """
    if supported is None:
        supported = ["text", "json", "yaml"]
    
    fmt = fmt.lower()
    
    if fmt not in supported:
        format_not_supported(fmt, command, supported)
        return
    
    if fmt == "text":
        # Text format: caller handles output, or we print if it's a string
        if isinstance(data, str):
            print(data)
        # For dicts/lists in text mode, fall back to pretty-printed representation
        elif data is not None:
            if isinstance(data, (dict, list)):
                # Simple text representation
                _print_text_data(data)
    
    elif fmt == "json":
        indent = 2 if pretty else None
        print(json.dumps(data, indent=indent, default=str, ensure_ascii=False))
    
    elif fmt == "jsonl":
        if isinstance(data, list):
            for item in data:
                print(json.dumps(item, default=str, ensure_ascii=False))
        else:
            print(json.dumps(data, default=str, ensure_ascii=False))
    
    elif fmt == "yaml":
        try:
            import yaml as yaml_module
            print(yaml_module.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
        except ImportError:
            print("Error: PyYAML not installed. Use --output-format=json instead.", file=sys.stderr)
            sys.exit(1)
    
    elif fmt == "csv":
        if not isinstance(data, list) or not data:
            print("Error: CSV format requires a non-empty list of records.", file=sys.stderr)
            sys.exit(1)
        import csv
        import io
        output = io.StringIO()
        if isinstance(data[0], dict):
            # Collect union of all keys across all objects (preserving order from first occurrence)
            all_keys = []
            seen_keys = set()
            for row in data:
                for key in row.keys():
                    if key not in seen_keys:
                        all_keys.append(key)
                        seen_keys.add(key)
            
            # Flatten nested values for CSV compatibility
            def flatten_value(v):
                if v is None:
                    return ""
                if isinstance(v, (dict, list)):
                    return json.dumps(v, ensure_ascii=False)
                return v
            
            writer = csv.DictWriter(output, fieldnames=all_keys, extrasaction='ignore')
            writer.writeheader()
            for row in data:
                flat_row = {k: flatten_value(row.get(k, "")) for k in all_keys}
                writer.writerow(flat_row)
        else:
            writer = csv.writer(output)
            writer.writerows(data)
        print(output.getvalue(), end='')
    
    elif fmt == "md":
        _print_markdown(data)
    
    else:
        format_not_supported(fmt, command, supported)


def _print_text_data(data: Any, indent: int = 0) -> None:
    """Simple text representation of data."""
    prefix = "  " * indent
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                print(f"{prefix}{k}:")
                _print_text_data(v, indent + 1)
            else:
                print(f"{prefix}{k}: {v}")
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                print(f"{prefix}- ")
                _print_text_data(item, indent + 1)
            else:
                print(f"{prefix}- {item}")
    else:
        print(f"{prefix}{data}")


def _print_markdown_table(data: List[Dict]) -> None:
    """Print data as a markdown table with union of all keys."""
    if not data:
        return
    
    # Collect union of all keys (preserving order from first occurrence)
    headers = []
    seen = set()
    for row in data:
        for key in row.keys():
            if key not in seen:
                headers.append(key)
                seen.add(key)
    
    def format_cell(v):
        if v is None:
            return ""
        if isinstance(v, (dict, list)):
            # Compact JSON for nested structures
            s = json.dumps(v, ensure_ascii=False)
            if len(s) > 50:
                s = s[:47] + "..."
            return s
        s = str(v)
        # Escape pipes and newlines
        s = s.replace("|", "\\|").replace("\n", " ")
        if len(s) > 50:
            s = s[:47] + "..."
        return s
    
    # Header row
    print("| " + " | ".join(str(h) for h in headers) + " |")
    # Separator
    print("| " + " | ".join("---" for _ in headers) + " |")
    # Data rows
    for row in data:
        cells = [format_cell(row.get(h, "")) for h in headers]
        print("| " + " | ".join(cells) + " |")


def _print_markdown(data: Any, depth: int = 0) -> None:
    """Smart markdown output - adapts to data structure.
    
    Renders data as:
    - Tables for lists of flat dicts
    - Nested outlines for hierarchical dicts
    - Bullet lists for simple arrays
    - Code blocks for complex nested structures
    - Headers for top-level dict keys (at depth 0)
    """
    if data is None:
        print("*null*")
        return
    
    if isinstance(data, str):
        # Multi-line strings get code blocks
        if "\n" in data and len(data) > 100:
            print("```")
            print(data)
            print("```")
        else:
            print(data)
        return
    
    if isinstance(data, (int, float, bool)):
        print(f"`{data}`")
        return
    
    if isinstance(data, list):
        if not data:
            print("*(empty list)*")
            return
        
        # Check if it's a list of flat dicts (table-worthy)
        if all(isinstance(item, dict) for item in data):
            # Check if dicts are mostly flat (good for tables)
            flat_count = sum(1 for item in data 
                           for v in item.values() 
                           if not isinstance(v, (dict, list)))
            nested_count = sum(1 for item in data 
                             for v in item.values() 
                             if isinstance(v, (dict, list)))
            
            if flat_count > nested_count * 2:  # Mostly flat -> table
                _print_markdown_table(data)
                return
            else:
                # Nested dicts -> numbered outline
                for i, item in enumerate(data):
                    print(f"\n### {i + 1}.")
                    _print_markdown(item, depth + 1)
                return
        
        # Simple list -> bullet points
        indent = "  " * depth
        for item in data:
            if isinstance(item, (dict, list)):
                print(f"{indent}-")
                _print_markdown(item, depth + 1)
            else:
                s = str(item)
                if len(s) > 80:
                    s = s[:77] + "..."
                print(f"{indent}- {s}")
        return
    
    if isinstance(data, dict):
        if not data:
            print("*(empty)*")
            return
        
        indent = "  " * depth
        
        for key, value in data.items():
            # Top level keys get headers
            if depth == 0:
                print(f"\n## {key}")
                _print_markdown(value, depth + 1)
            elif isinstance(value, dict):
                print(f"{indent}**{key}:**")
                _print_markdown(value, depth + 1)
            elif isinstance(value, list):
                print(f"{indent}**{key}:** ({len(value)} items)")
                _print_markdown(value, depth + 1)
            elif isinstance(value, str) and "\n" in value:
                print(f"{indent}**{key}:**")
                print(f"{indent}```")
                for line in value.split("\n")[:10]:
                    print(f"{indent}{line}")
                if value.count("\n") > 10:
                    print(f"{indent}... ({value.count(chr(10)) - 10} more lines)")
                print(f"{indent}```")
            else:
                s = str(value) if value is not None else "*null*"
                if len(s) > 60:
                    s = s[:57] + "..."
                print(f"{indent}- **{key}:** {s}")
        return
    
    # Fallback: just stringify
    print(str(data))


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


# CONFIG LOADING (not sniffable - implementation detail)
# Load order: built-in -> skill config -> user config -> project config -> CLI args

def load_config() -> dict:
    """Load configuration from multiple sources (later sources override earlier)."""
    config = {
        "limits": {"default": 50, "tail": 20, "stream": 100},
        "resolution": {"min_hash_prefix": 4, "match_hash_prefixes": True},
        "export": {"trailing_newline": True},
        "debug": {"enabled": False},
    }
    
    # Config file locations (in priority order, later overrides earlier)
    config_paths = [
        Path(__file__).parent / "cursor_mirror_config.yml",  # Skill default
        Path.home() / ".config/cursor-mirror/config.yml",     # User config
        Path.home() / ".cursor-mirror.yml",                   # User config alt
        Path.cwd() / ".moollm/cursor-mirror.yml",             # Project config
    ]
    
    try:
        for cfg_path in config_paths:
            if cfg_path.exists():
                with open(cfg_path) as f:
                    file_config = yaml.safe_load(f) or {}
                    # Deep merge
                    for k, v in file_config.items():
                        if isinstance(v, dict) and k in config:
                            config[k].update(v)
                        else:
                            config[k] = v
    except ImportError:
        pass  # yaml not available, use defaults
    except Exception:
        pass  # Config load failed, use defaults
    
    return config

CONFIG = load_config()


def open_db(path: Path) -> sqlite3.Connection:
    """Open SQLite in read-only mode."""
    debug("open_db: %s", path.name if hasattr(path, 'name') else path)
    register_source("database", path)
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def decode_blob(raw) -> str:
    """Decode blob to UTF-8 string."""
    b = raw if isinstance(raw, (bytes, bytearray)) else str(raw).encode()
    return b.decode("utf-8", errors="replace")


def fmt(obj: Any, args) -> str:
    """Format object based on --output-format (or legacy --yaml/--json/--pretty).
    
    Uses get_output_format() to resolve the format, supporting:
      - --output-format yaml/json/jsonl
      - Legacy --yaml, --json flags
      - --pretty for indented JSON
    """
    out_fmt = get_output_format(args, default="json")
    pretty = getattr(args, "pretty", False)
    
    if out_fmt == "yaml":
        return yaml.dump(obj, default_flow_style=False, allow_unicode=True, sort_keys=False)
    elif out_fmt == "jsonl":
        if isinstance(obj, list):
            return "\n".join(json.dumps(item, ensure_ascii=False) for item in obj)
        return json.dumps(obj, ensure_ascii=False)
    else:  # json (default for structured output)
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

    Accepts (in order of precedence):
      @1, @2, @3    → Index by RECENCY (most recent first, like bash !-1)
      769a26        → Hash prefix (4+ hex chars, case-insensitive)
      moollm        → Folder name fragment (searches path)
      /full/path    → Absolute path (passed through)

    Returns None if not found. Use 'find' command to discover workspaces.
    
    Note: @1 changes when you switch projects! It's always "most recently
    modified state.vscdb", not a stable reference.
    """
    if not ref:
        return None
    
    debug("resolve_workspace: ref=%r", ref)
    
    # Index reference (@1, @2, etc.) - sorted by recency (most recent first)
    if ref.startswith("@") and ref[1:].isdigit():
        idx = int(ref[1:]) - 1
        workspaces = sorted(
            [ws for ws in WORKSPACES_ROOT.iterdir() if ws.is_dir()],
            key=lambda w: (w / "state.vscdb").stat().st_mtime if (w / "state.vscdb").exists() else 0,
            reverse=True  # Most recent first
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
    """Resolve composer reference to (composerId, metadata dict).

    Accepts (in order of precedence):
      @1, @2, @3    → Index by RECENCY (most recent lastSendTime first)
      fe18ce96      → UUID prefix (4+ hex chars)
      "my chat"     → Name fragment (searches composer name)
      moollm        → Workspace folder fragment (if in that workspace)

    Args:
      ref: The reference string to resolve
      workspace_ref: Optional workspace filter (also accepts @1/prefix/name)

    Returns:
      (composer_id, metadata_dict) or None if not found.
      
    The metadata dict includes: name, mode, createdAt, lastSendTime, etc.
    Use resolve_composer_id() if you just need the UUID string.
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
    
    # Index reference (@1, @2, etc.) - sorted by recency (most recent first)
    if ref.startswith("@") and ref[1:].isdigit():
        idx = int(ref[1:]) - 1
        sorted_composers = sorted(
            composers_meta.items(),
            key=lambda x: x[1].get("lastSendTime") or x[1].get("createdAt") or "",
            reverse=True  # Most recent first
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
    register_source("database", db_path, "ItemTable")
    register_source("sql", "SELECT value FROM ItemTable WHERE key='composer.composerData'")
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
    """Yield (composer_id, bubble_key, bubble_dict) for all bubbles.

    Args:
      composer_id: Full UUID to filter by (NOT a prefix or @1 reference!
                   Use resolve_composer_id() first if you have a reference).
                   Pass None to iterate ALL bubbles across ALL composers.

    Yields:
      Tuples of (composer_uuid, "bubbleId:uuid:suffix", bubble_dict)
      
    The bubble_dict contains:
      - type: 1=user, 2=assistant
      - text: Message content
      - createdAt: Timestamp (ms since epoch)
      - toolCalls, toolResults, thinking, codeBlocks, etc.
      
    Note: This reads from cursorDiskKV in the global state.vscdb.
    Large composers may have 1000s of bubbles. Use load_bubbles() for
    sorted, filtered access.
    """
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    register_source("database", GLOBAL_DB, "cursorDiskKV")
    if composer_id:
        register_source("sql", f"SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:{composer_id[:8]}...'")
        rows = cur.execute(
            "SELECT key, value FROM cursorDiskKV WHERE key LIKE ?",
            (f"bubbleId:{composer_id}:%",),
        ).fetchall()
    else:
        register_source("sql", "SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'")
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
    register_source("directory", WORKSPACES_ROOT)
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
    
    out_fmt = get_output_format(args)
    if out_fmt != "text":
        # Remove path for serialization
        output = [{k: v for k, v in w.items() if k != "path"} for w in ws_data]
        output_data(output, out_fmt, "list-workspaces",
                   supported=["text", "json", "jsonl", "yaml", "csv", "md"])
        return
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
    """Get indexed list of workspaces sorted by recency (most recent first)."""
    ws_list = sorted(
        [ws for ws in WORKSPACES_ROOT.iterdir() if ws.is_dir()],
        key=lambda w: (w / "state.vscdb").stat().st_mtime if (w / "state.vscdb").exists() else 0,
        reverse=True  # Most recent first
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
        if get_output_format(args) != "text":
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
        if get_output_format(args) != "text":
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
        
        if get_output_format(args) != "text":
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
        
        if get_output_format(args) != "text":
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
        
        if get_output_format(args) != "text":
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
        if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    """Grep-like regex search across ALL chat messages.

    Searches the cursorDiskKV bubble store (the live data Cursor uses).
    
    Usage:
      grep "error"              # Case-sensitive search
      grep -i "warning"         # Case-insensitive
      grep "def.*init" -n 20    # Regex, limit 20 results
      grep -F "exact match"     # Fixed string (no regex)
      
    Output format: [composer_prefix] message_preview...
    
    For searching plaintext transcripts instead, use 'tgrep' command.
    For searching specific composer only, there's no filter yet (grep is global).
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
    
    for cid, k, obj in iter_bubbles(args.composer):
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    if lines:
        output += "\n"  # Trailing newline for proper wc -l count

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
    
    if get_output_format(args) != "text":
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
    register_source("database", GLOBAL_DB, "ItemTable")
    register_source("sql", f"SELECT value FROM ItemTable WHERE key = '{key}'")
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
    
    out_fmt = get_output_format(args)
    
    if out_fmt != "text":
        output_data(status, out_fmt, "status", 
                   supported=["text", "json", "jsonl", "yaml", "csv", "md"])
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
    
    if get_output_format(args) != "text":
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
            
            if get_output_format(args) != "text":
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


# ~/.cursor Commands (2026-01-15)

DOTCURSOR_BASE = os.path.expanduser("~/.cursor")
DOTCURSOR_PROJECTS = os.path.join(DOTCURSOR_BASE, "projects")
DOTCURSOR_AI_TRACKING = os.path.join(DOTCURSOR_BASE, "ai-tracking", "ai-code-tracking.db")
DOTCURSOR_EXTENSIONS = os.path.join(DOTCURSOR_BASE, "extensions")


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


def cmd_secrets(args):
    """Scan transcripts for potential secrets/credentials using K-REFS output.

    Looks for: API keys, private keys, database URIs, passwords, tokens, etc.

    ⚠️  EXPECT FALSE POSITIVES when scanning sessions where:
      - Security patterns were written/discussed (detects its own definitions)
      - Documentation contains example credentials
      - Code handles credential patterns (even without real values)
    
    The scanner detects patterns like `-----BEGIN PRIVATE KEY-----` even when
    they appear in pattern definitions or docs. Always verify actual line content.
    """
    import re
    
    # Compile patterns
    compiled = [(re.compile(pat), name) for pat, name in SECRET_PATTERNS]
    
    # Get files to scan
    files_to_scan = []
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    since_ts = parse_time_filter(args.since) if args.since else None
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if os.path.isdir(trans_dir):
            for fname in os.listdir(trans_dir):
                if fname.endswith('.txt'):
                    if args.composer and not fname.startswith(args.composer):
                        continue
                    fpath = os.path.join(trans_dir, fname)
                    if since_ts:
                        mtime = os.path.getmtime(fpath) * 1000
                        if mtime < since_ts:
                            continue
                    files_to_scan.append(fpath)
    
    matches = []
    context = args.context
    
    for fpath in files_to_scan:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except:
            continue
        
        for i, line in enumerate(lines):
            line_stripped = line.rstrip('\n\r')
            lineno = i + 1
            
            for regex, secret_type in compiled:
                match = regex.search(line_stripped)
                if match:
                    # Mask the actual secret in output
                    matched_text = match.group()
                    if len(matched_text) > 12:
                        masked = matched_text[:6] + "..." + matched_text[-4:]
                    else:
                        masked = matched_text[:4] + "..."
                    
                    start_line = max(1, lineno - context)
                    end_line = min(len(lines), lineno + context)
                    
                    excerpt = []
                    if not args.refs_only:
                        for j in range(start_line - 1, end_line):
                            excerpt.append(lines[j].rstrip('\n\r')[:100])
                    
                    matches.append({
                        "path": fpath,
                        "line": lineno,
                        "start": start_line,
                        "end": end_line,
                        "type": secret_type,
                        "masked": masked,
                        "excerpt": excerpt if excerpt else None
                    })
                    
                    if len(matches) >= args.limit:
                        break
            
            if len(matches) >= args.limit:
                break
        if len(matches) >= args.limit:
            break
    
    # Output
    if args.yaml:
        print(yaml.dump({"secrets": matches, "count": len(matches)}, 
                       default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps({"secrets": matches, "count": len(matches)}, indent=2))
    elif args.refs_only:
        for m in matches:
            print(f"{m['path']}:{m['start']}-{m['end']} # {m['type']} | {m['masked']}")
    else:
        print(f"# Potential Secrets Found: {len(matches)}")
        print(f"# WARNING: Review carefully - may include false positives")
        print()
        for m in matches:
            print(f"{m['path']}:{m['start']}-{m['end']} # {m['type']} | {m['masked']}")
            if m.get("excerpt"):
                print("-" * 60)
                for eline in m["excerpt"]:
                    print(f"    {eline}")
                print()


def cmd_commits(args):
    """Find git commits mentioned in transcripts using K-REFS output."""
    import re
    
    # Patterns for git commits
    commit_patterns = [
        (re.compile(r'\b([0-9a-f]{40})\b'), 'full_sha'),
        (re.compile(r'\b([0-9a-f]{7,12})\b(?=\s|$|[^0-9a-f])'), 'short_sha'),
        (re.compile(r'commit\s+([0-9a-f]{7,40})', re.I), 'commit_ref'),
        (re.compile(r'git\s+(?:checkout|cherry-pick|revert|show)\s+([0-9a-f]{7,40})', re.I), 'git_cmd'),
    ]
    
    # Get files to scan
    files_to_scan = []
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
                    files_to_scan.append(os.path.join(trans_dir, fname))
    
    matches = []
    seen_commits = set()
    
    for fpath in files_to_scan:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except:
            continue
        
        for i, line in enumerate(lines):
            line_stripped = line.rstrip('\n\r')
            lineno = i + 1
            
            for regex, commit_type in commit_patterns:
                for match in regex.finditer(line_stripped):
                    sha = match.group(1)
                    # Skip if looks like a UUID or other non-commit hash
                    if '-' in sha:
                        continue
                    # Dedupe
                    if sha[:12] in seen_commits:
                        continue
                    seen_commits.add(sha[:12])
                    
                    context_preview = line_stripped[:100]
                    
                    matches.append({
                        "path": fpath,
                        "line": lineno,
                        "sha": sha[:12],
                        "full_sha": sha if len(sha) == 40 else None,
                        "type": commit_type,
                        "context": context_preview
                    })
                    
                    if len(matches) >= args.limit:
                        break
            
            if len(matches) >= args.limit:
                break
        if len(matches) >= args.limit:
            break
    
    # Output
    if args.yaml:
        print(yaml.dump({"commits": matches, "count": len(matches)}, 
                       default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps({"commits": matches, "count": len(matches)}, indent=2))
    elif args.refs_only:
        for m in matches:
            print(f"{m['path']}:{m['line']}-{m['line']} # {m['type']} | {m['sha']}")
    else:
        print(f"# Git Commits Found: {len(matches)}")
        print()
        for m in matches:
            print(f"{m['path']}:{m['line']} # {m['type']} | {m['sha']} | {m['context'][:60]}")


def cmd_scrub(args):
    """Redact sensitive content from transcripts. QUIT CURSOR FIRST!"""
    import re
    
    print("=" * 60)
    print("SCRUB: Redact sensitive content from Cursor transcripts")
    print("=" * 60)
    print()
    print("WARNING: Make sure Cursor is QUIT before running this!")
    print("         Cursor must not be writing to these files.")
    print()
    
    # Build patterns to scrub
    patterns_to_scrub = []
    
    if args.secrets:
        for pat, name in SECRET_PATTERNS:
            patterns_to_scrub.append((re.compile(pat), name))
    
    if args.pattern:
        try:
            patterns_to_scrub.append((re.compile(args.pattern), 'custom'))
        except re.error as e:
            print(f"Invalid pattern: {e}")
            return
    
    if not patterns_to_scrub:
        print("No patterns specified. Use --secrets and/or --pattern")
        return
    
    # Get files to scrub
    files_to_scrub = []
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
                    files_to_scrub.append(os.path.join(trans_dir, fname))
    
    if not files_to_scrub:
        print("No transcript files found to scrub")
        return
    
    print(f"Files to scan: {len(files_to_scrub)}")
    print(f"Patterns: {len(patterns_to_scrub)}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()
    
    total_redactions = 0
    files_modified = 0
    
    for fpath in files_to_scrub:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            continue
        
        original_content = content
        file_redactions = 0
        
        for regex, pattern_name in patterns_to_scrub:
            matches = list(regex.finditer(content))
            for match in reversed(matches):  # Reverse to preserve positions
                matched_text = match.group()
                if args.dry_run:
                    print(f"  Would redact [{pattern_name}]: {matched_text[:20]}... in {os.path.basename(fpath)}")
                content = content[:match.start()] + args.redact_text + content[match.end():]
                file_redactions += 1
        
        if file_redactions > 0:
            total_redactions += file_redactions
            files_modified += 1
            
            if not args.dry_run:
                # Create backup unless disabled
                if not args.no_backup:
                    backup_path = fpath + '.bak'
                    try:
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(original_content)
                        print(f"  Backup: {backup_path}")
                    except Exception as e:
                        print(f"  WARNING: Could not create backup: {e}")
                        print(f"  Skipping {fpath}")
                        continue
                
                # Write scrubbed content
                try:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  Scrubbed {file_redactions} items in {os.path.basename(fpath)}")
                except Exception as e:
                    print(f"  ERROR writing {fpath}: {e}")
    
    print()
    print(f"{'Would redact' if args.dry_run else 'Redacted'}: {total_redactions} items in {files_modified} files")
    if args.dry_run:
        print("\nRun without --dry-run to apply changes")


def cmd_exfil_audit(args):
    """Comprehensive secret exfiltration audit - ALL tools, ALL arguments, both stores.
    
    Design: Systematic, complete by construction.
    - Scans EVERY tool call from both data stores
    - Checks EVERY argument against comprehensive secret patterns
    - Reports ALL findings with K-REFS pointers
    """
    import re
    from collections import defaultdict
    
    # Comprehensive secret patterns - expanded for full coverage
    EXFIL_PATTERNS = [
        # API Keys - specific vendors
        (r'sk-[a-zA-Z0-9]{20,}', 'openai_key', 'high'),
        (r'sk-proj-[a-zA-Z0-9]{20,}', 'openai_project_key', 'high'),
        (r'sk-ant-[a-zA-Z0-9]{20,}', 'anthropic_key', 'high'),
        (r'AKIA[0-9A-Z]{16}', 'aws_access_key', 'high'),
        (r'(?i)aws[_-]?secret[_-]?access[_-]?key["\s:=]+[A-Za-z0-9/+=]{40}', 'aws_secret', 'high'),
        (r'ghp_[a-zA-Z0-9]{36}', 'github_pat', 'high'),
        (r'gho_[a-zA-Z0-9]{36}', 'github_oauth', 'high'),
        (r'github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}', 'github_fine_grained', 'high'),
        (r'glpat-[a-zA-Z0-9\-]{20}', 'gitlab_pat', 'high'),
        (r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24}', 'slack_token', 'high'),
        (r'AIza[0-9A-Za-z\-_]{35}', 'google_api_key', 'high'),
        (r'ya29\.[0-9A-Za-z\-_]+', 'google_oauth', 'high'),
        (r'(?i)npm_[a-zA-Z0-9]{36}', 'npm_token', 'high'),
        (r'(?i)pypi-[a-zA-Z0-9]{32,}', 'pypi_token', 'high'),
        (r'sq0[a-z]{3}-[0-9A-Za-z\-_]{22,}', 'square_token', 'high'),
        (r'stripe_[a-zA-Z0-9]{24,}', 'stripe_key', 'high'),
        (r'sk_live_[a-zA-Z0-9]{24,}', 'stripe_secret', 'high'),
        (r'rk_live_[a-zA-Z0-9]{24,}', 'stripe_restricted', 'high'),
        (r'twilio_[a-zA-Z0-9]{32}', 'twilio_key', 'high'),
        (r'AC[a-f0-9]{32}', 'twilio_sid', 'medium'),
        (r'sendgrid\.[a-zA-Z0-9\-_]{34,}', 'sendgrid_key', 'high'),
        (r'SG\.[a-zA-Z0-9\-_]{22}\.[a-zA-Z0-9\-_]{43}', 'sendgrid_api', 'high'),
        
        # Generic secrets
        (r'(?i)bearer\s+[a-zA-Z0-9\-_.]{20,}', 'bearer_token', 'high'),
        (r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'password', 'high'),
        (r'(?i)passwd[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'passwd', 'high'),
        (r'(?i)secret[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'secret_value', 'high'),
        (r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'api_key', 'high'),
        (r'(?i)auth[_-]?token[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'auth_token', 'high'),
        (r'(?i)access[_-]?token[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'access_token', 'high'),
        (r'(?i)private[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'private_key_value', 'high'),
        
        # Private keys (PEM format)
        (r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 'private_key_pem', 'critical'),
        (r'-----BEGIN PGP PRIVATE KEY BLOCK-----', 'pgp_private', 'critical'),
        (r'-----BEGIN ENCRYPTED PRIVATE KEY-----', 'encrypted_private_key', 'critical'),
        
        # Database URIs with credentials
        (r'(?i)mongodb(?:\+srv)?://[^:]+:[^@]+@[^\s]+', 'mongodb_uri_with_creds', 'critical'),
        (r'(?i)postgres(?:ql)?://[^:]+:[^@]+@[^\s]+', 'postgres_uri_with_creds', 'critical'),
        (r'(?i)mysql://[^:]+:[^@]+@[^\s]+', 'mysql_uri_with_creds', 'critical'),
        (r'(?i)redis://[^:]+:[^@]+@[^\s]+', 'redis_uri_with_creds', 'critical'),
        (r'(?i)amqp://[^:]+:[^@]+@[^\s]+', 'amqp_uri_with_creds', 'critical'),
        
        # URLs with secrets in query params
        (r'https?://[^\s]*[?&](?:api_?key|token|secret|password|auth)=[^&\s]{8,}', 'url_with_secret_param', 'high'),
        (r'https?://[^:]+:[^@]+@[^\s]+', 'url_with_basic_auth', 'critical'),
        
        # Sensitive file paths being accessed
        (r'(?i)\.env(?:\.local|\.prod|\.dev)?$', 'env_file', 'high'),
        (r'(?i)credentials\.json', 'credentials_file', 'high'),
        (r'(?i)service[_-]?account.*\.json', 'service_account_file', 'high'),
        (r'(?i)id_rsa(?:\.pub)?$', 'ssh_key_file', 'high'),
        (r'(?i)\.pem$', 'pem_file', 'medium'),
        (r'(?i)\.p12$', 'p12_file', 'high'),
        (r'(?i)\.pfx$', 'pfx_file', 'high'),
        (r'(?i)\.keystore$', 'keystore_file', 'high'),
        (r'(?i)/etc/passwd', 'etc_passwd', 'medium'),
        (r'(?i)/etc/shadow', 'etc_shadow', 'critical'),
        (r'(?i)~/.ssh/', 'ssh_dir', 'high'),
        (r'(?i)~/.aws/credentials', 'aws_credentials_file', 'critical'),
        (r'(?i)~/.netrc', 'netrc_file', 'high'),
        
        # JWT tokens
        (r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+', 'jwt_token', 'high'),
        
        # SSH private key content
        (r'-----BEGIN OPENSSH PRIVATE KEY-----', 'openssh_private_key', 'critical'),
        
        # High-entropy strings (potential secrets) - 32+ hex chars
        (r'(?<![a-fA-F0-9])[a-fA-F0-9]{32,64}(?![a-fA-F0-9])', 'hex_string_32plus', 'low'),
    ]
    
    # Compile patterns
    compiled_patterns = [(re.compile(p), name, sev) for p, name, sev in EXFIL_PATTERNS]
    
    findings = []
    stats = defaultdict(lambda: defaultdict(int))
    
    # Source 1: Transcripts
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    since_ts = parse_time_filter(args.since) if args.since else None
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if args.composer and not fname.startswith(args.composer):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            
            if since_ts:
                mtime = os.path.getmtime(fpath) * 1000
                if mtime < since_ts:
                    continue
            
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    lines = f.readlines()
            except:
                continue
            
            # Parse tool calls with their full argument blocks
            current_tool = None
            tool_start_line = 0
            tool_args_text = []
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                lineno = i + 1
                
                # Detect tool call start
                if stripped.startswith('[Tool call]'):
                    # Process previous tool if exists
                    if current_tool and tool_args_text:
                        full_args = '\n'.join(tool_args_text)
                        _scan_for_secrets(
                            full_args, compiled_patterns, findings, stats,
                            fpath, tool_start_line, current_tool, "transcript",
                            args.limit, args.tool
                        )
                    
                    # Start new tool
                    parts = stripped.split()
                    current_tool = parts[2] if len(parts) > 2 else "unknown"
                    tool_start_line = lineno
                    tool_args_text = []
                
                # Detect end of tool section
                elif stripped.startswith('[Tool result]') or stripped in ('user:', 'assistant:'):
                    if current_tool and tool_args_text:
                        full_args = '\n'.join(tool_args_text)
                        _scan_for_secrets(
                            full_args, compiled_patterns, findings, stats,
                            fpath, tool_start_line, current_tool, "transcript",
                            args.limit, args.tool
                        )
                    current_tool = None
                    tool_args_text = []
                
                # Collect tool args
                elif current_tool:
                    tool_args_text.append(line)
                
                if len(findings) >= args.limit:
                    break
            
            if len(findings) >= args.limit:
                break
        if len(findings) >= args.limit:
            break
    
    # Source 2: SQLite
    if len(findings) < args.limit:
        global_db = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/state.vscdb")
        if os.path.isfile(global_db):
            try:
                conn = sqlite3.connect(f"file:{global_db}?mode=ro", uri=True)
                cursor = conn.cursor()
                
                # Get tool calls from bubbles
                cursor.execute("""
                    SELECT key, value FROM cursorDiskKV 
                    WHERE key LIKE 'bubbleId:%'
                    AND value LIKE '%"tool"%'
                    LIMIT 1000
                """)
                
                for key, value in cursor.fetchall():
                    if len(findings) >= args.limit:
                        break
                    try:
                        data = json.loads(value)
                        # Extract tool info if present
                        tool_name = data.get("tool", {}).get("name", "unknown") if isinstance(data.get("tool"), dict) else "unknown"
                        tool_args = json.dumps(data.get("tool", {}).get("args", data))
                        
                        _scan_for_secrets(
                            tool_args, compiled_patterns, findings, stats,
                            key, 0, tool_name, "sqlite",
                            args.limit, args.tool
                        )
                    except:
                        pass
                
                conn.close()
            except:
                pass
    
    # Output
    if args.yaml:
        output = {
            "findings": findings,
            "stats": {
                "total_findings": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_type": dict(stats["type"]),
                "by_tool": dict(stats["tool"]),
            }
        }
        print(yaml.dump(output, default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        output = {
            "findings": findings,
            "stats": {
                "total_findings": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_type": dict(stats["type"]),
                "by_tool": dict(stats["tool"]),
            }
        }
        print(json.dumps(output, indent=2))
    else:
        print("=" * 70)
        print("🔐 EXFILTRATION AUDIT (Comprehensive)")
        print("=" * 70)
        print(f"Sources: transcripts (~/.cursor) + state.vscdb")
        print(f"Patterns checked: {len(EXFIL_PATTERNS)}")
        print()
        
        # Summary stats
        print("📊 SUMMARY")
        print("-" * 40)
        print(f"Total findings: {len(findings)}")
        if stats["severity"]:
            print(f"By severity: " + ", ".join(f"{k}={v}" for k, v in sorted(stats["severity"].items(), key=lambda x: -x[1])))
        if stats["type"] and not args.summary:
            print(f"By type: " + ", ".join(f"{k}={v}" for k, v in list(stats["type"].items())[:5]))
        if stats["tool"]:
            print(f"By tool: " + ", ".join(f"{k}={v}" for k, v in list(stats["tool"].items())[:5]))
        
        if not args.summary and findings:
            print()
            print("🚨 FINDINGS (K-REFS)")
            print("-" * 40)
            for f in findings[:30]:  # Limit display
                sev_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "⚪"}.get(f["severity"], "?")
                if f["source"] == "transcript":
                    print(f"{sev_icon} {f['path']}:{f['line']} [{f['tool']}]")
                else:
                    print(f"{sev_icon} {f['path'][:50]} [{f['tool']}]")
                print(f"   {f['type']}: {f['masked'][:80]}")
            
            if len(findings) > 30:
                print(f"\n... and {len(findings) - 30} more findings")
        
        print()


def cmd_pattern_scan(args):
    """Find UUIDs, hashes, secrets, custom patterns with K-REFS output."""
    import re
    
    patterns = []
    
    # UUID pattern (standard format)
    if args.uuids or args.all:
        patterns.append((
            re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', re.I),
            'uuid', 'info'
        ))
    
    # Hash patterns
    if args.hashes or args.all:
        patterns.append((re.compile(r'(?<![a-fA-F0-9])[a-fA-F0-9]{32}(?![a-fA-F0-9])'), 'md5_hash', 'info'))
        patterns.append((re.compile(r'(?<![a-fA-F0-9])[a-fA-F0-9]{40}(?![a-fA-F0-9])'), 'sha1_hash', 'info'))
        patterns.append((re.compile(r'(?<![a-fA-F0-9])[a-fA-F0-9]{64}(?![a-fA-F0-9])'), 'sha256_hash', 'info'))
    
    # Secret patterns
    if args.secrets or args.all:
        patterns.extend([
            (re.compile(r'sk-[a-zA-Z0-9]{20,}'), 'openai_key', 'critical'),
            (re.compile(r'sk-ant-[a-zA-Z0-9]{20,}'), 'anthropic_key', 'critical'),
            (re.compile(r'AKIA[0-9A-Z]{16}'), 'aws_key', 'critical'),
            (re.compile(r'ghp_[a-zA-Z0-9]{36}'), 'github_pat', 'critical'),
            (re.compile(r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----'), 'private_key', 'critical'),
            (re.compile(r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}'), 'password', 'high'),
            (re.compile(r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}'), 'api_key', 'high'),
            (re.compile(r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+'), 'jwt', 'high'),
        ])
    
    # Custom pattern
    if args.pattern:
        try:
            patterns.append((re.compile(args.pattern), 'custom', 'info'))
        except re.error as e:
            print(f"Invalid pattern: {e}")
            return
    
    if not patterns:
        print("No patterns specified. Use --uuids, --hashes, --secrets, --all, or --pattern")
        return
    
    findings = []
    
    # Scan transcripts
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if args.composer and not fname.startswith(args.composer):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
            except:
                continue
            
            lines = content.split('\n')
            
            # Build char->line and char->col mappings
            char_to_line = []
            char_to_col = []
            line_starts = [0]
            char_count = 0
            for i, line in enumerate(lines):
                for c in range(len(line)):
                    char_to_line.append(i + 1)
                    char_to_col.append(c + 1)  # 1-based column
                # newline char
                char_to_line.append(i + 1)
                char_to_col.append(len(line) + 1)
                char_count += len(line) + 1
                if i < len(lines) - 1:
                    line_starts.append(char_count)
            
            for regex, ptype, severity in patterns:
                for match in regex.finditer(content):
                    if len(findings) >= args.limit:
                        break
                    
                    start_pos = match.start()
                    end_pos = match.end()
                    line_num = char_to_line[start_pos] if start_pos < len(char_to_line) else len(lines)
                    col_start = char_to_col[start_pos] if start_pos < len(char_to_col) else 1
                    col_end = char_to_col[end_pos - 1] if end_pos - 1 < len(char_to_col) else col_start
                    matched = match.group()
                    
                    findings.append({
                        'path': fpath,
                        'line': line_num,
                        'col_start': col_start,
                        'col_end': col_end + 1,  # exclusive end
                        'char_start': start_pos,
                        'char_end': end_pos,
                        'length': len(matched),
                        'type': ptype,
                        'severity': severity,
                        'value': matched if len(matched) <= 20 else matched[:10] + '...' + matched[-6:],
                    })
                
                if len(findings) >= args.limit:
                    break
            if len(findings) >= args.limit:
                break
        if len(findings) >= args.limit:
            break
    
    # Output
    if args.emit_redact:
        # Simple redaction commands: file:line:col_start:col_end:length:type
        # Can be piped to a simple tool for processing
        print("# REDACT format: file:line:col_start:col_end:length:type")
        print("# Apply with: awk or simple Python script")
        print(f"# Total: {len(findings)}")
        for f in findings:
            print(f"REDACT:{f['path']}:{f['line']}:{f['col_start']}:{f['col_end']}:{f['length']}:{f['type']}")
    elif args.emit_sed:
        # Group by file for efficient sed processing
        by_file = {}
        for f in findings:
            by_file.setdefault(f['path'], []).append(f)
        
        print("#!/bin/bash")
        print("# Auto-generated redaction script")
        print(f"# {len(findings)} redactions across {len(by_file)} files")
        print()
        for fpath, items in by_file.items():
            print(f"# {os.path.basename(fpath)}: {len(items)} redactions")
            print(f"cp '{fpath}' '{fpath}.bak'")
            # Use Python for reliable fixed-length replacement (sed struggles with this)
            print(f"python3 -c \"")
            print(f"import sys")
            print(f"with open('{fpath}', 'r') as f: c = f.read()")
            # Sort by char_start descending to preserve offsets
            sorted_items = sorted(items, key=lambda x: x['char_start'], reverse=True)
            for item in sorted_items:
                mask = '*' * item['length']
                print(f"c = c[:{item['char_start']}] + '{mask}' + c[{item['char_end']}:]")
            print(f"with open('{fpath}', 'w') as f: f.write(c)")
            print(f"\"")
            print()
    elif args.yaml:
        print(yaml.dump({'findings': findings, 'count': len(findings)}, 
                       default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps({'findings': findings, 'count': len(findings)}, indent=2))
    else:
        print(f"# Pattern Scan: {len(findings)} findings")
        print(f"# Patterns: {len(patterns)}")
        print()
        for f in findings:
            sev_icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'info': 'ℹ️'}.get(f['severity'], '⚪')
            print(f"{f['path']}:{f['line']}:{f['col_start']}-{f['col_end']} # {f['type']} len={f['length']}")
            print(f"  {sev_icon} {f['value']}")


def cmd_audit(args):
    """Unified composable audit: surfaces × patterns.

    Examples:
        audit --surface transcript --patterns secrets
        audit --surface transcript --surface sqlite --patterns secrets --patterns uuids
        audit --surface transcript --pattern "my-secret-.*" --emit-redact
        audit --surface transcript --patterns secrets --mask --dry-run
        audit --pattern-file my-patterns.yml
        audit --pattern "password123" --pattern-type literal
        audit --pattern "secret*key" --pattern-type glob
    """
    # Resolve composer reference (@1, prefix, name) to full ID
    composer_id = None
    if args.composer:
        composer_id = resolve_composer_id(args.composer)
        if not composer_id:
            print(f"Composer not found: {args.composer}", file=sys.stderr)
            return
    
    runner = AuditRunner()

    # Add surfaces
    surfaces = args.surfaces or ["transcript"]  # Default to transcripts
    for surface in surfaces:
        if surface == "transcript":
            runner.add_surface(TranscriptSurface(
                workspace=args.workspace,
                composer=composer_id
            ))
        elif surface == "sqlite":
            runner.add_surface(SqliteSurface())
        elif surface == "config":
            # Add common config paths
            home = os.path.expanduser("~")
            runner.add_surface(ConfigSurface(paths=[
                os.path.join(home, ".cursor", "mcp.json"),
                os.path.join(home, ".cursor", "settings.json"),
            ]))
        else:
            print(f"Unknown surface: {surface}")
            print("Available: transcript, sqlite, config")
            return
    
    # Add patterns from YAML file
    if args.pattern_file:
        try:
            runner.add_patterns_from_yaml(args.pattern_file)
        except Exception as e:
            print(f"Error loading pattern file: {e}")
            return
    
    # Add pattern sets
    pattern_sets = args.pattern_sets or []
    if not pattern_sets and not args.pattern and not args.pattern_file:
        pattern_sets = ["secrets"]  # Default
    
    for pset in pattern_sets:
        if pset in PATTERN_REGISTRY:
            runner.add_pattern_set(pset)
        else:
            print(f"Unknown pattern set: {pset}")
            print(f"Available: {', '.join(PATTERN_REGISTRY.keys())}")
            return
    
    # Add custom pattern with specified type
    if args.pattern:
        match_type = MatchType(args.pattern_type)
        runner.add_pattern(AuditPattern(
            name="custom",
            pattern=args.pattern,
            match_type=match_type,
            severity=Severity.INFO,
            category="custom",
            description=f"Custom {args.pattern_type} pattern",
            redact_label="[CUSTOM]"
        ))
    
    # Execute
    preserve_ws = not args.no_preserve_ws
    
    if args.mask:
        results = runner.mask_in_place(
            dry_run=args.dry_run, 
            backup=True, 
            preserve_whitespace=preserve_ws,
            force=getattr(args, 'force', False),
            cursor_stopped=getattr(args, 'cursor_stopped', False)
        )
        if args.yaml:
            print(yaml.dump(results, default_flow_style=False))
        elif args.json:
            print(json.dumps(results, indent=2))
        else:
            for r in results:
                if "error" in r:
                    if "path" in r:
                        print(f"❌ {r['path']}: {r['error']}")
                    else:
                        print(f"❌ {r['error']}")
                        if "warning" in r:
                            print(f"   {r['warning']}")
                        if "hint" in r:
                            print(f"   {r['hint']}")
                else:
                    mode = "Would mask" if r["dry_run"] else "Masked"
                    types_str = ", ".join(r.get("types", []))
                    print(f"✓ {mode} {r['findings']} in {os.path.basename(r['path'])}")
                    print(f"  Types: {types_str}")
                    print(f"  Size: {r['size']} (unchanged), Whitespace: {'preserved' if r.get('preserved_whitespace') else 'replaced'}")
        return
    
    if args.emit_redact:
        for cmd in runner.emit_redact_commands():
            print(cmd)
        return
    
    # Default: K-REF output
    findings = list(runner.scan(limit=args.limit))
    
    if args.yaml:
        out = [{
            "kref": f.to_kref(), 
            "severity": f.severity.value, 
            "pattern": f.pattern_name,
            "match_type": f.match_type,
            "description": f.description,
            "redact_label": f.redact_label,
            "matched": f.matched
        } for f in findings]
        print(yaml.dump({"findings": out, "count": len(out)}, 
                       default_flow_style=False, allow_unicode=True))
    elif args.json:
        out = [{
            "path": f.path, "line": f.line, 
            "col_start": f.col_start, "col_end": f.col_end, 
            "char_start": f.char_start, "char_end": f.char_end,
            "pattern": f.pattern_name, 
            "match_type": f.match_type,
            "severity": f.severity.value,
            "description": f.description,
            "redact_label": f.redact_label,
            "matched": f.matched, 
            "surface": f.surface
        } for f in findings]
        print(json.dumps({"findings": out, "count": len(out)}, indent=2))
    else:
        print(f"# Audit: {len(findings)} findings")
        print(f"# Surfaces: {', '.join(surfaces)}")
        psets = pattern_sets or []
        if args.pattern:
            psets.append(f"custom:{args.pattern_type}")
        if args.pattern_file:
            psets.append(f"file:{args.pattern_file}")
        print(f"# Patterns: {', '.join(psets) if psets else 'default:secrets'}")
        print()
        
        for f in findings:
            print(f.to_kref())
            print(f"  {f.matched}")


def cmd_mask_in_place(args):
    """Mask secrets in-place with same-length replacement (file size unchanged).

    Key feature: Replaces each character with mask_char, preserving exact length.
    This means file offsets remain valid and file size is unchanged.
    """
    import re

    print("MASK-IN-PLACE (file size preserved)")
    print()
    
    # Safety check: is Cursor running?
    if not args.dry_run and not args.cursor_stopped:
        cursor_status = check_cursor_running()
        if cursor_status["running"] and not args.force:
            print(f"ERROR: {cursor_status['warning']}")
            print()
            print("Options:")
            print("  --cursor-stopped  : I confirm Cursor is not running")
            print("  --force           : Modify anyway (dangerous!)")
            print("  --dry-run         : Preview without modifying")
            return
        elif cursor_status["running"] and args.force:
            print(f"WARNING: {cursor_status['warning']}")
            print("Proceeding anyway (--force)")
            print()
    
    patterns = []
    
    # UUID pattern
    if args.uuids:
        patterns.append((
            re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', re.I),
            'uuid'
        ))
    
    # Secret patterns
    if args.secrets:
        patterns.extend([
            (re.compile(r'sk-[a-zA-Z0-9]{20,}'), 'openai_key'),
            (re.compile(r'sk-ant-[a-zA-Z0-9]{20,}'), 'anthropic_key'),
            (re.compile(r'AKIA[0-9A-Z]{16}'), 'aws_key'),
            (re.compile(r'ghp_[a-zA-Z0-9]{36}'), 'github_pat'),
            (re.compile(r'(?i)password[\s]*=[\s]*["\']?[^\s"\']{8,}'), 'password'),
            (re.compile(r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+'), 'jwt'),
        ])
    
    # Custom pattern
    if args.pattern:
        try:
            patterns.append((re.compile(args.pattern), 'custom'))
        except re.error as e:
            print(f"Invalid pattern: {e}")
            return
    
    if not patterns:
        print("No patterns specified. Use --secrets, --uuids, or --pattern")
        return
    
    mask_char = args.mask_char[0]  # Use first char only
    
    # Get files to process
    files_to_mask = []
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
                    files_to_mask.append(os.path.join(trans_dir, fname))
    
    if not files_to_mask:
        print("No transcript files found")
        return
    
    print(f"Files to scan: {len(files_to_mask)}")
    print(f"Patterns: {len(patterns)}")
    print(f"Mask character: '{mask_char}'")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()
    
    total_masks = 0
    files_modified = 0
    
    for fpath in files_to_mask:
        # Check if file is in use
        if not args.dry_run and not args.force:
            file_status = is_file_in_use(fpath)
            if file_status["in_use"]:
                procs = ", ".join(file_status["processes"][:3])
                print(f"  SKIP {os.path.basename(fpath)}: in use by {procs}")
                continue
        
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            continue
        
        original_size = len(content)
        original_content = content
        file_masks = 0
        
        # Find all matches and their positions
        all_matches = []
        for regex, ptype in patterns:
            for match in regex.finditer(content):
                all_matches.append({
                    'start': match.start(),
                    'end': match.end(),
                    'text': match.group(),
                    'type': ptype
                })
        
        # Sort by position (reverse to preserve offsets)
        all_matches.sort(key=lambda x: x['start'], reverse=True)
        
        # Apply masks
        for m in all_matches:
            masked = mask_char * len(m['text'])
            
            if args.dry_run:
                preview = m['text'][:20] + '...' if len(m['text']) > 20 else m['text']
                print(f"  Would mask [{m['type']}] len={len(m['text'])}: {preview}")
            
            content = content[:m['start']] + masked + content[m['end']:]
            file_masks += 1
        
        # Verify size unchanged
        if len(content) != original_size:
            print(f"  ERROR: Size mismatch in {fpath}! Original={original_size}, New={len(content)}")
            continue
        
        if file_masks > 0:
            total_masks += file_masks
            files_modified += 1
            
            if not args.dry_run:
                # Create backup
                if not args.no_backup:
                    backup_path = fpath + '.bak'
                    try:
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(original_content)
                    except Exception as e:
                        print(f"  WARNING: Backup failed: {e}")
                        continue
                
                # Write masked content
                try:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  Masked {file_masks} items in {os.path.basename(fpath)} (size unchanged: {original_size})")
                except Exception as e:
                    print(f"  ERROR writing {fpath}: {e}")
    
    print()
    print(f"{'Would mask' if args.dry_run else 'Masked'}: {total_masks} items in {files_modified} files")
    print(f"File sizes: UNCHANGED")
    if args.dry_run:
        print("\nRun without --dry-run to apply")


def cmd_full_audit(args):
    """Full communication audit - ALL vectors in and out of Cursor.
    
    Vectors audited:
    - PROMPTS: User input sent to LLM
    - RESPONSES: LLM output (may echo secrets from context)
    - TOOL_CALLS: Arguments sent to tools
    - TOOL_RESULTS: Data returned from tools
    - MCP: MCP server communication
    - SHELL: Terminal commands executed
    - CONTEXT: Files mentioned/read as context
    - IMAGES: Image paths referenced
    - THINKING: Internal reasoning (may contain secrets)
    """
    import re
    from collections import defaultdict
    
    # Use the same comprehensive patterns
    AUDIT_PATTERNS = [
        # High-value secrets
        (r'sk-[a-zA-Z0-9]{20,}', 'openai_key', 'critical'),
        (r'sk-ant-[a-zA-Z0-9]{20,}', 'anthropic_key', 'critical'),
        (r'AKIA[0-9A-Z]{16}', 'aws_access_key', 'critical'),
        (r'ghp_[a-zA-Z0-9]{36}', 'github_pat', 'critical'),
        (r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 'private_key', 'critical'),
        (r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'password', 'high'),
        (r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'api_key', 'high'),
        (r'https?://[^:/\s]+:[^@\s]+@[^\s]+', 'url_with_creds', 'critical'),
        (r'(?i)bearer\s+[a-zA-Z0-9\-_.]{20,}', 'bearer_token', 'high'),
        (r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+', 'jwt', 'high'),
        # Sensitive files
        (r'(?i)\.env(?:\.local|\.prod|\.dev)?(?:\s|$|")', 'env_file', 'high'),
        (r'(?i)credentials\.json', 'credentials_file', 'high'),
        (r'(?i)~/.ssh/id_rsa', 'ssh_key', 'critical'),
        (r'(?i)~/.aws/credentials', 'aws_creds_file', 'critical'),
    ]
    
    compiled = [(re.compile(p), n, s) for p, n, s in AUDIT_PATTERNS]
    
    # Vector-specific patterns
    shell_danger = re.compile(r'(?i)(curl|wget|ssh|scp|rsync|nc|netcat)\s+.*(-d|--data|@)', re.I)
    mcp_pattern = re.compile(r'\[Tool call\]\s+(cursor-ide-browser|user-\w+|mcp-\w+)', re.I)
    
    findings = defaultdict(list)
    stats = defaultdict(lambda: defaultdict(int))
    
    # Get transcripts
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    since_ts = parse_time_filter(args.since) if args.since else None
    vector_filter = set(args.vector.split(',')) if args.vector else None
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if args.composer and not fname.startswith(args.composer):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            if since_ts:
                mtime = os.path.getmtime(fpath) * 1000
                if mtime < since_ts:
                    continue
            
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    lines = f.readlines()
            except:
                continue
            
            # State machine to track sections
            current_section = None
            section_start = 0
            section_content = []
            current_tool = None
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                lineno = i + 1
                
                # Detect section changes
                new_section = None
                if stripped == 'user:':
                    new_section = 'prompt'
                elif stripped == 'assistant:':
                    new_section = 'response'
                elif stripped.startswith('[Thinking]'):
                    new_section = 'thinking'
                elif stripped.startswith('[Tool call]'):
                    new_section = 'tool_call'
                    parts = stripped.split()
                    current_tool = parts[2] if len(parts) > 2 else 'unknown'
                    # Check if MCP
                    if mcp_pattern.match(stripped):
                        new_section = 'mcp'
                elif stripped.startswith('[Tool result]'):
                    new_section = 'tool_result'
                
                # Process previous section if section changed
                if new_section and current_section:
                    _audit_section(
                        current_section, '\n'.join(section_content),
                        compiled, shell_danger, findings, stats,
                        fpath, section_start, current_tool, args.limit, vector_filter
                    )
                
                if new_section:
                    current_section = new_section
                    section_start = lineno
                    section_content = []
                    if new_section not in ('tool_call', 'mcp'):
                        current_tool = None
                else:
                    section_content.append(line)
            
            # Process last section
            if current_section and section_content:
                _audit_section(
                    current_section, '\n'.join(section_content),
                    compiled, shell_danger, findings, stats,
                    fpath, section_start, current_tool, args.limit, vector_filter
                )
    
    # Also check context files from SQLite
    if not vector_filter or 'context' in vector_filter:
        global_db = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/state.vscdb")
        if os.path.isfile(global_db):
            try:
                conn = sqlite3.connect(f"file:{global_db}?mode=ro", uri=True)
                cursor = conn.cursor()
                
                # Get context/file references
                cursor.execute("""
                    SELECT key, value FROM cursorDiskKV 
                    WHERE key LIKE 'bubbleId:%' 
                    AND (value LIKE '%"context"%' OR value LIKE '%"files"%')
                    LIMIT 100
                """)
                
                for key, value in cursor.fetchall():
                    try:
                        # Scan for sensitive file paths
                        for regex, secret_type, severity in compiled:
                            for match in regex.finditer(value):
                                findings['context'].append({
                                    'path': key[:50],
                                    'line': 0,
                                    'type': secret_type,
                                    'severity': severity,
                                    'masked': match.group()[:20] + '...',
                                    'source': 'sqlite'
                                })
                                stats['context'][secret_type] += 1
                    except:
                        pass
                
                conn.close()
            except:
                pass
    
    # Output
    total = sum(len(v) for v in findings.values())
    
    if args.yaml:
        print(yaml.dump({
            'findings': dict(findings),
            'stats': {k: dict(v) for k, v in stats.items()},
            'total': total
        }, default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps({
            'findings': dict(findings),
            'stats': {k: dict(v) for k, v in stats.items()},
            'total': total
        }, indent=2))
    else:
        print("=" * 70)
        print("🔒 FULL COMMUNICATION AUDIT")
        print("=" * 70)
        print(f"Total findings: {total}")
        print()
        
        for vector in ['prompt', 'response', 'tool_call', 'tool_result', 'mcp', 'thinking', 'context']:
            vec_findings = findings.get(vector, [])
            if vec_findings or not args.summary:
                icon = {
                    'prompt': '📤', 'response': '📥', 'tool_call': '🔧',
                    'tool_result': '📋', 'mcp': '🔌', 'thinking': '💭', 'context': '📁'
                }.get(vector, '❓')
                print(f"{icon} {vector.upper()}: {len(vec_findings)} findings")
                
                if not args.summary:
                    for f in vec_findings[:10]:
                        sev_icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡'}.get(f['severity'], '⚪')
                        if f.get('source') == 'sqlite':
                            print(f"  {sev_icon} [sqlite] {f['type']}: {f['masked']}")
                        else:
                            print(f"  {sev_icon} {f['path']}:{f['line']} {f['type']}: {f['masked']}")
                    if len(vec_findings) > 10:
                        print(f"  ... and {len(vec_findings) - 10} more")
                print()


def _audit_section(section, content, patterns, shell_danger, findings, stats, path, line, tool, limit, vector_filter):
    """Audit a transcript section for secrets."""
    if vector_filter and section not in vector_filter:
        return
    
    if len(findings.get(section, [])) >= limit:
        return
    
    # Skip self-references (pattern definitions)
    if 'AUDIT_PATTERNS' in content[:500] or 'EXFIL_PATTERNS' in content[:500]:
        return
    
    # Check for secrets
    for regex, secret_type, severity in patterns:
        for match in regex.finditer(content):
            matched = match.group()
            if len(matched) > 20:
                masked = matched[:10] + '...' + matched[-4:]
            else:
                masked = matched[:8] + '...'
            
            findings[section].append({
                'path': path,
                'line': line,
                'tool': tool,
                'type': secret_type,
                'severity': severity,
                'masked': masked,
            })
            stats[section][secret_type] += 1
    
    # Special check for shell commands with data exfil
    if section == 'tool_call' and tool and 'shell' in tool.lower():
        if shell_danger.search(content):
            findings[section].append({
                'path': path,
                'line': line,
                'tool': tool,
                'type': 'shell_data_exfil',
                'severity': 'high',
                'masked': content[:50] + '...',
            })
            stats[section]['shell_data_exfil'] += 1


def _scan_for_secrets(text, patterns, findings, stats, path, line, tool, source, limit, tool_filter):
    """Helper to scan text for secrets and add findings."""
    if tool_filter and tool_filter.lower() not in tool.lower():
        return
    
    for regex, secret_type, severity in patterns:
        if len(findings) >= limit:
            return
        
        for match in regex.finditer(text):
            matched = match.group()
            
            # Skip if it looks like it's part of the pattern definition itself
            if 'SECRET_PATTERNS' in text[:500] or 'EXFIL_PATTERNS' in text[:500]:
                if matched in text[:1000]:  # Likely self-reference
                    continue
            
            # Mask the secret
            if len(matched) > 16:
                masked = matched[:8] + "..." + matched[-4:]
            else:
                masked = matched[:4] + "..."
            
            findings.append({
                "source": source,
                "path": path,
                "line": line,
                "tool": tool,
                "type": secret_type,
                "severity": severity,
                "masked": masked,
            })
            
            stats["severity"][severity] += 1
            stats["type"][secret_type] += 1
            stats["tool"][tool] += 1
            
            if len(findings) >= limit:
                return


def cmd_url_audit(args):
    """Find URLs in tool calls, check for secrets (JOINs both stores)."""
    import re
    
    # Resolve composer reference (@1, prefix, name) to full ID
    composer_id = None
    if args.composer:
        composer_id = resolve_composer_id(args.composer)
        if not composer_id:
            print(f"Composer not found: {args.composer}", file=sys.stderr)
            return
    
    # URL pattern
    url_pattern = re.compile(r'https?://[^\s"\'\]}>]+')
    
    # Secret patterns in URLs
    url_secret_patterns = [
        (re.compile(r'[?&](?:api_?key|token|secret|password|auth|key)=([^&\s]+)', re.I), 'query_param_secret'),
        (re.compile(r'://[^:]+:([^@]+)@', re.I), 'basic_auth_password'),
        (re.compile(r'[?&]access_token=([^&\s]+)', re.I), 'access_token'),
        (re.compile(r'[?&]client_secret=([^&\s]+)', re.I), 'client_secret'),
        (re.compile(r'/v\d+/[a-f0-9]{32,}', re.I), 'embedded_key'),
    ]
    
    results = []
    
    # Source 1: Transcripts (plaintext)
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if composer_id and not fname.startswith(composer_id):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    lines = f.readlines()
            except:
                continue
            
            in_tool = False
            tool_name = None
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                
                # Track if we're in a tool call section
                if stripped.startswith('[Tool call]'):
                    in_tool = True
                    parts = stripped.split()
                    tool_name = parts[2] if len(parts) > 2 else "unknown"
                elif stripped.startswith('[Tool result]'):
                    in_tool = True
                    tool_name = "result"
                elif stripped in ('user:', 'assistant:'):
                    in_tool = False
                
                # Find URLs
                for url_match in url_pattern.finditer(line):
                    url = url_match.group()
                    
                    # Check for secrets in URL
                    secrets_found = []
                    for secret_re, secret_type in url_secret_patterns:
                        if secret_re.search(url):
                            secrets_found.append(secret_type)
                    
                    # Check custom pattern
                    if args.pattern:
                        if not re.search(args.pattern, url, re.I):
                            if not secrets_found:
                                continue
                    
                    # Filter if secrets-only
                    if args.secrets_only and not secrets_found:
                        continue
                    
                    # Mask any secrets in URL for output
                    masked_url = url
                    for secret_re, _ in url_secret_patterns:
                        masked_url = secret_re.sub(lambda m: m.group(0).replace(m.group(1), '[REDACTED]') if m.groups() else '[REDACTED]', masked_url)
                    
                    results.append({
                        "source": "transcript",
                        "path": fpath,
                        "line": i + 1,
                        "tool": tool_name if in_tool else None,
                        "url": masked_url[:200],
                        "secrets": secrets_found if secrets_found else None,
                        "in_tool_call": in_tool,
                    })
                    
                    if len(results) >= args.limit:
                        break
            
            if len(results) >= args.limit:
                break
        if len(results) >= args.limit:
            break
    
    # Source 2: SQLite (structured tool calls) - if not at limit
    if len(results) < args.limit:
        global_db = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/state.vscdb")
        if os.path.isfile(global_db):
            try:
                conn = sqlite3.connect(f"file:{global_db}?mode=ro", uri=True)
                cursor = conn.cursor()
                
                # Search tool calls in bubbles
                cursor.execute("""
                    SELECT key, value FROM cursorDiskKV 
                    WHERE key LIKE 'bubbleId:%' 
                    AND (value LIKE '%http://%' OR value LIKE '%https://%')
                    LIMIT ?
                """, (args.limit - len(results),))
                
                for key, value in cursor.fetchall():
                    try:
                        data = json.loads(value)
                        text = json.dumps(data)
                        
                        for url_match in url_pattern.finditer(text):
                            url = url_match.group()
                            
                            secrets_found = []
                            for secret_re, secret_type in url_secret_patterns:
                                if secret_re.search(url):
                                    secrets_found.append(secret_type)
                            
                            if args.secrets_only and not secrets_found:
                                continue
                            
                            masked_url = url
                            for secret_re, _ in url_secret_patterns:
                                masked_url = secret_re.sub(lambda m: m.group(0).replace(m.group(1), '[REDACTED]') if m.groups() else '[REDACTED]', masked_url)
                            
                            results.append({
                                "source": "state.vscdb",
                                "key": key[:50],
                                "url": masked_url[:200],
                                "secrets": secrets_found if secrets_found else None,
                            })
                            
                            if len(results) >= args.limit:
                                break
                    except:
                        pass
                    
                    if len(results) >= args.limit:
                        break
                
                conn.close()
            except Exception as e:
                pass
    
    # Output
    if args.yaml:
        print(yaml.dump({"urls": results, "count": len(results)}, 
                       default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps({"urls": results, "count": len(results)}, indent=2))
    else:
        print(f"# URL Audit: {len(results)} URLs found")
        print(f"# Sources: transcripts (~/.cursor) + state.vscdb")
        secrets_count = sum(1 for r in results if r.get("secrets"))
        if secrets_count:
            print(f"# ⚠️  URLs with potential secrets: {secrets_count}")
        print()
        
        for r in results:
            if r["source"] == "transcript":
                loc = f"{r['path']}:{r['line']}"
                tool_info = f" [{r['tool']}]" if r.get("tool") else ""
            else:
                loc = r.get("key", "sqlite")
                tool_info = ""
            
            secret_flag = " 🔑" if r.get("secrets") else ""
            print(f"{loc}{tool_info}{secret_flag}")
            print(f"  {r['url']}")
            if r.get("secrets"):
                print(f"  ⚠️  {', '.join(r['secrets'])}")
            print()


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


def cmd_deep_snitch(args):
    """Deep Snitch - comprehensive security audit with K-REF output.

    Scans Cursor activity for:
    - Secrets (API keys, passwords, tokens)
    - Shell exfiltration (curl, wget, netcat, ssh)
    - Code execution (eval, exec, subprocess)
    - Dangerous paths (/etc/passwd, ~/.ssh, etc.)
    - Obfuscation (base64, hex, chr building)
    - Prompt injection attempts
    - Data exfiltration (webhooks, pastebin, file uploads)
    - Suspicious behavior (SSL bypass, cron, rm -rf)

    ⚠️  FALSE POSITIVE WARNING:
    If you scan a transcript where security code was written (like this script),
    the scanner will detect its own pattern definitions! Example:
      - Pattern `r'/etc/passwd'` in code → flagged as "etc_passwd access"
      - Pattern `-----BEGIN PRIVATE KEY-----` in docs → flagged as "private_key"
    
    This is the "Ouroboros effect". Look at actual line content to verify.
    Expect ~80% false positives when scanning security-focused sessions.

    Outputs K-REFs with severity levels for each finding.
    """
    import re
    from collections import defaultdict
    
    # Determine what to scan
    show_all = args.all
    show_patterns = args.patterns or args.all or args.category
    show_overview = args.endpoints or args.mcp or args.files or args.models or args.all
    
    # If nothing specified, do full audit
    if not (show_patterns or show_overview):
        show_all = True
        show_patterns = True
        show_overview = True
    
    # Severity filter
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    min_severity = severity_order.get(args.severity, 4) if args.severity else 4
    
    # Categories to scan
    if args.category:
        categories = [c.strip() for c in args.category.split(',')]
    else:
        categories = [
            "secrets", "shell_exfil", "code_execution", "dangerous_paths",
            "obfuscation", "prompt_injection", "data_exfil", "suspicious_behavior"
        ]
    
    findings = []
    stats = defaultdict(lambda: defaultdict(int))
    
    # Pattern scanning
    if show_patterns:
        # Resolve composer reference (@1, prefix, name) to full ID
        composer_id = None
        if args.composer:
            composer_id = resolve_composer_id(args.composer)
            if not composer_id:
                print(f"Composer not found: {args.composer}", file=sys.stderr)
                return
        
        runner = AuditRunner()
        runner.add_surface(TranscriptSurface(
            workspace=args.workspace,
            composer=composer_id
        ))
        
        # Add requested pattern categories
        for cat in categories:
            if cat == "all":
                for pset in PATTERN_REGISTRY.keys():
                    runner.add_pattern_set(pset)
            elif cat in PATTERN_REGISTRY:
                runner.add_pattern_set(cat)
        
        # Scan (collect all, filter later for proper severity prioritization)
        all_findings = list(runner.scan(limit=10000))
        
        # Sort by severity (critical first) then filter
        all_findings.sort(key=lambda f: severity_order.get(f.severity.value, 4))
        
        for finding in all_findings:
            sev_level = severity_order.get(finding.severity.value, 4)
            if sev_level <= min_severity:
                findings.append(finding)
                stats["severity"][finding.severity.value] += 1
                stats["category"][finding.category] += 1
                stats["pattern"][finding.pattern_name] += 1
            # Apply limit per output, not per scan
            if len(findings) >= args.limit * 10:  # generous buffer
                break
    
    # Overview data
    report = {
        "endpoints": [],
        "mcp_servers": [],
        "models_used": defaultdict(int),
        "files_exposed": set(),
        "tool_calls": defaultdict(int),
        "data_volume": {"prompts": 0, "responses": 0},
    }
    
    if show_overview:
        # Check configured endpoints
        mcp_json = os.path.join(DOTCURSOR_BASE, "mcp.json")
        if os.path.isfile(mcp_json):
            try:
                with open(mcp_json, 'r') as f:
                    mcp_config = json.load(f)
                for server_name, server_config in mcp_config.get("mcpServers", {}).items():
                    cmd = server_config.get("command", "")
                    report["endpoints"].append({
                        "type": "mcp_server",
                        "name": server_name,
                        "command": cmd
                    })
            except:
                pass
        
        # Scan transcripts for overview
        workspaces = get_dotcursor_workspaces()
        if args.workspace:
            workspaces = [ws for ws in workspaces if args.workspace in ws.get("name", "")]
        
        since_ts = parse_time_filter(args.since) if args.since else None
        file_pattern = re.compile(r'(?:path|file)["\s:]+([/\w\-_.]+\.[a-z]{1,5})', re.I)
        model_pattern = re.compile(r'(claude-[a-z0-9\-_.]+|gpt-[a-z0-9\-_.]+|gemini-[a-z0-9\-_.]+)', re.I)
        
        for ws in workspaces:
            trans_dir = os.path.join(ws["path"], "agent-transcripts")
            if not os.path.isdir(trans_dir):
                continue
            
            for fname in os.listdir(trans_dir):
                if not fname.endswith('.txt'):
                    continue
                if args.composer and not fname.startswith(args.composer):
                    continue
                
                fpath = os.path.join(trans_dir, fname)
                if since_ts and os.path.getmtime(fpath) * 1000 < since_ts:
                    continue
                
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                except:
                    continue
                
                # Extract stats
                for match in file_pattern.finditer(content):
                    report["files_exposed"].add(match.group(1))
                for match in model_pattern.finditer(content):
                    report["models_used"][match.group(1).lower()] += 1
    
    # Convert for output
    report["files_exposed"] = sorted(report["files_exposed"])[:50]
    report["models_used"] = dict(report["models_used"])
    
    # Output
    if args.yaml:
        output = {
            "findings": [{
                "kref": f.to_kref(),
                "severity": f.severity.value,
                "category": f.category,
                "pattern": f.pattern_name,
                "description": f.description,
                "redact_label": f.redact_label,
                "matched": f.matched
            } for f in findings],
            "stats": {
                "total": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_category": dict(stats["category"]),
            },
            "overview": report if show_overview else None
        }
        print(yaml.dump(output, default_flow_style=False, allow_unicode=True))
        
    elif args.json:
        output = {
            "findings": [{
                "path": f.path, "line": f.line,
                "col_start": f.col_start, "col_end": f.col_end,
                "severity": f.severity.value,
                "category": f.category,
                "pattern": f.pattern_name,
                "description": f.description,
                "redact_label": f.redact_label,
                "matched": f.matched
            } for f in findings],
            "stats": {
                "total": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_category": dict(stats["category"]),
            },
            "overview": report if show_overview else None
        }
        print(json.dumps(output, indent=2))
        
    else:
        # K-REF output with logging levels
        sev_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🔵", "info": "ℹ️"}
        sev_label = {"critical": "CRITICAL", "high": "HIGH", "medium": "MEDIUM", "low": "LOW", "info": "INFO"}
        
        print("DEEP SNITCH REPORT")
        print(f"Categories: {', '.join(categories)}")
        if args.composer:
            print(f"Composer: {args.composer}")
        if args.since:
            print(f"Since: {args.since}")
        print()
        
        # Summary first
        if not args.summary:
            print(f"Total findings: {len(findings)}")
            if stats["severity"]:
                sev_str = ", ".join(f"{sev_icon.get(k, '?')} {k}={v}" for k, v in 
                                   sorted(stats["severity"].items(), key=lambda x: severity_order.get(x[0], 99)))
                print(f"By severity: {sev_str}")
            print()
        
        # Group by severity for output
        if not args.summary:
            for sev in ["critical", "high", "medium", "low", "info"]:
                sev_findings = [f for f in findings if f.severity.value == sev]
                if not sev_findings:
                    continue
                
                print(f"{sev_icon.get(sev, '?')} {sev_label.get(sev, sev).upper()} ({len(sev_findings)})")
                print("-" * 60)
                
                for f in sev_findings[:args.limit // 5]:  # Limit per severity
                    print(f.to_kref())
                    # Truncate matched for display
                    matched_display = f.matched
                    if len(matched_display) > 80:
                        matched_display = matched_display[:40] + "..." + matched_display[-30:]
                    print(f"  {matched_display}")
                
                if len(sev_findings) > args.limit // 5:
                    print(f"  ... and {len(sev_findings) - args.limit // 5} more {sev} findings")
                print()
        
        # Overview section
        if show_overview and not args.summary:
            print("OVERVIEW")
            print("-" * 60)
            
            if report["endpoints"]:
                print(f"MCP Endpoints: {len(report['endpoints'])}")
                for ep in report["endpoints"][:5]:
                    print(f"  {ep['name']} → {ep.get('command', '?')}")
            
            if report["models_used"]:
                print(f"Models used: {', '.join(list(report['models_used'].keys())[:5])}")
            
            if report["files_exposed"]:
                print(f"Files exposed: {len(report['files_exposed'])} files")
        
        # Summary stats
        print()
        print("SUMMARY")
        print("-" * 60)
        critical = stats["severity"].get("critical", 0)
        high = stats["severity"].get("high", 0)
        medium = stats["severity"].get("medium", 0)
        
        if critical > 0:
            print(f"🔴 {critical} CRITICAL findings - immediate attention required!")
        if high > 0:
            print(f"🟠 {high} HIGH findings - review recommended")
        if medium > 0:
            print(f"🟡 {medium} MEDIUM findings - consider reviewing")
        
        if critical == 0 and high == 0:
            print("✅ No critical or high severity findings")
        
        # Top patterns
        if stats["pattern"]:
            top_patterns = sorted(stats["pattern"].items(), key=lambda x: -x[1])[:5]
            print(f"\nTop patterns: {', '.join(f'{p}({c})' for p, c in top_patterns)}")


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
