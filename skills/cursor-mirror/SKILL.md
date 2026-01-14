---
name: cursor-mirror
tier: skill
type: utility
protocol: CURSOR-MIRROR
aliases: [cursor, cursor-chat, cursor-workspace, cursor-inspect, watch-yourself-think]
audience: ["operators", "devs", "agents"]
platforms: ["cursor-macos", "cursor-linux", "cursor-windows"]
author: Don Hopkins, Leela AI
license: MIT
state:
  creates:
    - MAC-STORAGE.yml
    - DATA-SCHEMAS.yml
    - KEY-CATALOG.yml
    - CURSOR-EXTENSIONS.yml
    - EXTERNAL-SERVICES.yml
    - MODELS.yml
  scripts:
    - cursor_mirror.py  # 47-command CLI inspector (4480+ lines)
tools:
  required: [read_file, terminal]
  optional: [grep, glob]
invoke_when:
  - "Need to review past Cursor chats"
  - "Analyzing MOOLLM boot sequences"
  - "Watching yourself think"
  - "Optimizing kernel/cursor driver"
  - "Understanding context assembly"
  - "Tracing MCP tool calls"
  - "Debugging agent behavior"
  - "Designing a custom orchestrator"
---

# Philosophy: Watch Yourself Think

> *"You can't think about thinking without thinking about thinking about something."*
> — Seymour Papert, *Mindstorms*

This skill enables **meta-cognition** — the ability to observe your own reasoning processes. By analyzing chat transcripts, tool calls, thinking blocks, and context assembly, you can:

1. **Understand boot sequences** — Trace exactly what happens when MOOLLM initializes
2. **Optimize context assembly** — See what files, code, and context Cursor gathers
3. **Debug agent behavior** — Identify patterns in tool usage and decision-making
4. **Improve kernel/drivers** — Use insights to refine the cursor.yml driver
5. **Design orchestrators** — Learn what makes effective context management

## The Introspection Loop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           YOUR SESSION                                       │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  Thinking → Tools → Output → Thinking → Tools → Output → ...           │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                    ↓                                         │
│                      cursor_mirror.py                                  │
│                                    ↓                                         │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  • analyze      → Deep stats on what happened                          │ │
│  │  • thinking     → Your reasoning blocks                                │ │
│  │  • timeline     → Chronological event stream                           │ │
│  │  • context      → What context was assembled                           │ │
│  │  • tools        → Tool call patterns                                   │ │
│  │  • status       → Current configuration and limits                     │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                    ↓                                         │
│               Insights → Optimize kernel/drivers/cursor.yml                  │
│               Insights → Improve bootstrap/working-set                       │
│               Insights → Design better orchestration                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

```bash
# Status dashboard — quick health check
cursor-mirror status

# Navigate hierarchically
cursor-mirror tree                    # All workspaces (w1, w2...)
cursor-mirror tree w3                 # Composers in workspace 3
cursor-mirror tree w3.c2              # Details of composer 2
cursor-mirror tree w3.c2.tools        # Tool calls in that chat

# Reference shortcuts work everywhere
cursor-mirror transcript @1           # Largest composer by message count
cursor-mirror analyze "Cursor chat"   # Find by name fragment
cursor-mirror show-workspace moollm   # Find by folder name

# Watch yourself think
cursor-mirror thinking @1             # See reasoning blocks
cursor-mirror timeline @1             # Chronological view
cursor-mirror watch @1 --speed 0      # Instant replay

# Trace context assembly
cursor-mirror context-sources @1      # What context was gathered
cursor-mirror searches @1 -v          # Search queries with results
cursor-mirror indexing                # Vector embedding status

# Debug mode
cursor-mirror --debug tree w3         # See cache hits, resolution, queries
```

---

## Reference Shortcuts

All commands accept flexible references instead of raw UUIDs:

| Format | Example | Meaning |
|--------|---------|---------|
| `@N` | `@1`, `@2` | Index by size (workspaces) or messages (composers) |
| Prefix | `769a26`, `9861c0` | Hash/UUID prefix match |
| Name | `moollm`, `Cursor chat` | Folder or title fragment (case-insensitive) |
| Tree | `w3.c2` | Workspace 3, composer 2 |
| Full | `769a268960457999e3f29ee8bd3bc640` | Exact match |

---

## Command Categories

### 1. Navigation (discover what exists)

| Command | Purpose |
|---------|---------|
| `list-workspaces` | Tabular listing with indices (w1, w2...) |
| `list-composers` | Conversations in a workspace (c1, c2...) |
| `show-workspace` | Detailed workspace info |
| `show-composer` | Detailed composer info |
| `tree` | Hierarchical drill-down with short IDs |
| `find` | Search by pattern across all data |
| `which` | Resolve any reference to full details |

### 2. Message Viewing (see what was said)

| Command | Purpose |
|---------|---------|
| `tail` | Recent messages (like `tail -f` for chats) |
| `stream` | Unified activity stream |
| `transcript` | Readable conversation transcript |
| `watch` | Terminal replay with timing |

### 3. Analysis (understand what happened)

| Command | Purpose |
|---------|---------|
| `analyze` | Deep stats: tools, models, files, duration |
| `timeline` | Chronological event stream |
| `thinking` | Agent reasoning blocks (meta-cognition) |
| `grep` | Regex search across bubbles |

### 4. Tool & Agent Inspection

| Command | Purpose |
|---------|---------|
| `tools` | All tool calls in a conversation |
| `tool-result` | Full result content for a tool call |
| `blobs` | Cached agentKv blobs (tool results) |
| `checkpoints` | File state snapshots |
| `mcp` | MCP server and tool call tracing |

### 5. Context Assembly

| Command | Purpose |
|---------|---------|
| `context` | Context gathered in conversation |
| `context-sources` | ALL context sources (files, code, terminal) |
| `request-context` | Full assembled context for a message |
| `searches` | Codebase/web searches with results |
| `indexing` | Embeddable files and indexing status |

### 6. Status (check current state)

| Command | Purpose |
|---------|---------|
| `status` | Overall dashboard |
| `status-config` | Server limits (context tokens, files) |
| `status-mcp` | MCP server inventory |
| `status-models` | Available AI models |
| `status-features` | Feature flags |
| `status-privacy` | Privacy settings |
| `status-endpoints` | Known API endpoints |

### 7. Database (direct access)

| Command | Purpose |
|---------|---------|
| `sql` | Run SQL queries on any database |
| `dbs` | List all databases with sizes |
| `tables` | Show tables in a database |
| `keys` | List ItemTable keys |

### 8. Export (get data out)

| Command | Purpose |
|---------|---------|
| `export-chat` | Raw bubbles as JSON/YAML |
| `export-markdown` | Readable Markdown |
| `export-jsonl` | Training/analysis format |
| `export-prompts` | Prompts and generations |
| `index` | Searchable conversation index |
| `stats` | Summary statistics |
| `models` | Model usage analysis |

---

## Optimizing the Kernel/Cursor Driver

Use this skill to improve `kernel/drivers/cursor.yml`:

### 1. Discover Actual Tool Names

```bash
# See what tools Cursor actually calls
cursor-mirror tools @1 -v

# Common discoveries:
#   read_file_v2    (not read_file)
#   edit_file_v2    (not search_replace)
#   SemanticSearch  (not codebase_search)
```

Update `kernel/drivers/cursor.yml` tools section accordingly:

```yaml
tools:
  read_file:
    tool: "read_file_v2"
    fallback: "read_file"
    
  semantic_search:
    tool: "SemanticSearch"
    fallback: "codebase_search"
```

### 2. Check Server Configuration

```bash
cursor-mirror status-config
```

Discovered limits to add to driver:

```yaml
limits:
  context:
    fullContextTokenLimit: 30000
    maxRuleLength: 100000
    maxMcpTools: 100
  indexing:
    absoluteMaxNumberFiles: 250000
    indexingPeriodSeconds: 272
  composer:
    maxBackgroundComposers: 10
```

### 3. Trace MCP Servers

```bash
cursor-mirror status-mcp
cursor-mirror mcp --all -v
```

Add to driver:

```yaml
mcp:
  builtin_servers:
    cursor-ide-browser:
      description: "Browser automation"
      tools: [browser_navigate, browser_click, browser_snapshot]
    svelte:
      description: "Svelte MCP"
      tools: [list-sections, get-documentation, svelte-autofixer]
```

### 4. Analyze Context Assembly

```bash
cursor-mirror context-sources @1
cursor-mirror request-context @1 --yaml
```

Document in driver:

```yaml
context_assembly:
  sources:
    fileSelections: "Files via @ mentions"
    selections: "Highlighted code"
    cursorRules: ".cursorrules content"
    codebase_search: "Semantic search results"
```

---

## Integration with Bootstrap Skill

### Trace Boot Sequences

```bash
# Find MOOLLM boot conversations
cursor-mirror find "MOOLLM" -t composer
cursor-mirror find "bootstrap" -t composer

# Analyze what happened
cursor-mirror analyze @1
cursor-mirror timeline @1 | head -100
cursor-mirror tools @1
```

### Optimize Working-Set Selection

```bash
# See what Cursor actually focused on
cursor-mirror context-sources @1

# Compare with your working-set.yml
cat .moollm/working-set.yml

# Generate working-set from actual focus (reverse mode!)
cursor-mirror context-sources @1 --yaml > .moollm/working-set.yml
```

### Hot/Cold Advisory Mode

On Cursor, `hot.yml`, `cold.yml`, and `working-set.yml` are **ADVISORY**:

```yaml
# These files are SUGGESTIONS, not commands
# Cursor manages context via its own algorithms
# Use introspection to see what Cursor actually focuses on

# REVERSE GENERATION: Generate these from actual focus
cursor-mirror context-sources @1 --yaml > .moollm/working-set.yml
```

---

## Vector Search Optimization

### Understand Semantic Search

```bash
# See embeddable files
cursor-mirror indexing moollm --files

# Check important paths  
cursor-mirror indexing moollm --folders

# Analyze search queries and results
cursor-mirror searches @1 -v

# Direct query for retrieval data
cursor-mirror sql --db moollm --keys retrieval
```

### Files Affecting Vector Search

| File | Location | Purpose |
|------|----------|---------|
| `embeddable_files.txt` | `anysphere.cursor-retrieval/` | Files indexed for semantic search |
| `high_level_folder_description.txt` | `anysphere.cursor-retrieval/` | Important paths for retrieval |
| `.cursorrules` | Project root | Rules included in every context |

---

## K-Lines and Protocol Symbols

This skill activates the introspection K-line. Related protocols:

| K-Line | Activation |
|--------|------------|
| `CURSOR-CHAT` | `cursor-mirror <command>` |
| `WATCH-YOURSELF-THINK` | `cursor-mirror thinking @1` |
| `BOOTSTRAP` | Use with `cursor-mirror analyze` to trace |
| `FILES-AS-STATE` | All data is in SQLite files |
| `HOT-COLD` | Advisory hints, use introspection to verify |
| `WORKING-SET` | Generate from `context-sources` |

---

## Debug Mode

Enable verbose logging to understand internal behavior:

```bash
cursor-mirror --debug tree w3
```

Output shows:
- Cache hits/misses for bubble counts, composers
- Database opens and queries
- Reference resolution steps
- Timing information

Use this to:
- Verify caching is working
- Debug reference resolution
- Understand performance characteristics
- Trace what the script is doing

---

## Caching Architecture

The script uses multi-level caching (no TTL — CLI exits quickly):

```python
_bubble_counts_cache    # Message counts per composer (loaded once)
_composers_cache        # Composers per workspace (per-workspace)
_all_composers_cache    # All composers globally (loaded once)
```

This means:
- First command may be slower (loading caches)
- Subsequent operations in same run are fast
- `get_all_composers()` loads everything once for global searches

---

## Safety

- **Read-only** — SQLite opened with `?mode=ro`
- **No mutations** — Never writes to Cursor data stores
- **Gitignored artifacts** — Derived data goes to `.moollm/`
- **Privacy** — Sanitize before sharing externally

---

## Designing Your Own Orchestrator

Use the insights from this skill to design a custom orchestrator:

### 1. Understand Context Assembly

```bash
# How Cursor builds prompts
cursor-mirror request-context @1 --yaml

# Key patterns:
# - fileSelections: @ mentioned files
# - selections: highlighted code  
# - cursorRules: rules always included
# - codebase_search: semantic search results
```

### 2. Learn from Limits

```bash
cursor-mirror status-config

# Important limits:
# - 30K context tokens
# - 100 max MCP tools
# - 250K max indexed files
```

### 3. Study Tool Patterns

```bash
cursor-mirror tools @1 -v

# Observe:
# - Tool naming (_v2 suffixes)
# - Parameter patterns
# - Result formats
```

### 4. Trace MCP Protocol

```bash
cursor-mirror mcp --all -v

# Learn:
# - How MCP servers register
# - Tool call format
# - Result handling
```

---

## Related Skills

| Skill | Integration |
|-------|-------------|
| `bootstrap` | Use cursor-mirror to trace boot sequences |
| `session-log` | Export conversations for documentation |
| `summarize` | Summarize for cold storage |
| `debugging` | Debug agent behavior |
| `k-lines` | Protocol symbol activation |

---

## Protocol Symbol

```
CURSOR-CHAT
```

**Aliases:** `CHAT-REFLECT`, `CURSOR-INSPECT`, `WATCH-YOURSELF-THINK`

Invoke when: Self-introspection, boot analysis, driver optimization, orchestrator design.

See: [PROTOCOLS.yml](../../PROTOCOLS.yml)

---

## License

MIT License — Copyright (c) 2026 Don Hopkins, Leela AI. Use freely, credit required.

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| 📜 Index | [PROTOCOLS.yml](../../PROTOCOLS.yml) |
| 🧠 Core | [kernel/constitution-core.md](../../kernel/constitution-core.md) |
| 🚀 Bootstrap | [bootstrap/](../bootstrap/) |
| 🔧 Driver | [kernel/drivers/cursor.yml](../../kernel/drivers/cursor.yml) |

---

*Watch yourself think. The filesystem is your memory. Introspection is power.*
