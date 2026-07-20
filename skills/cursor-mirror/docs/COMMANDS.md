# cursor-mirror Command Reference

*Broken out of the cursor-mirror [README](../README.md). The definitive interface is the docstring atop [`scripts/cursor_mirror.py`](../scripts/cursor_mirror.py).*

**73 commands** organized by function. Run `cursor-mirror --help` for full list, or sniff the first 200 lines of `cursor_mirror.py` for the definitive CLI interface.

### Command Categories

| Category | Commands | Purpose |
|----------|----------|---------|
| **Navigation** | `list-workspaces`, `show-workspace`, `list-composers`, `show-composer`, `tree`, `find`, `which` | Browse workspaces and conversations |
| **Messages** | `tail`, `stream`, `transcript`, `watch` | View chat messages |
| **Analysis** | `grep`, `analyze`, `timeline`, `thinking` | Deep-dive into sessions |
| **Tools** | `tools`, `tool-result`, `blobs`, `checkpoints`, `mcp`, `agent-tools`, `mcp-tools` | Inspect tool calls |
| **Context** | `context`, `context-sources`, `request-context`, `searches`, `indexing` | See what context was assembled |
| **Export** | `export-chat`, `export-prompts`, `export-markdown`, `export-jsonl`, `index` | Export conversations |
| **Status** | `status`, `status-config`, `status-mcp`, `status-models`, `status-features`, `status-privacy`, `status-endpoints` | Server config and state |
| **SQL** | `sql`, `dbs`, `tables`, `keys` | Direct database queries |
| **Images** | `images`, `image-path`, `image-info`, `image-gallery` | Cached images from chats |
| **Security** | `secrets`, `deep-snitch`, `full-audit`, `pattern-scan`, `mask-in-place`, `audit` | Scan for secrets/patterns |
| **AI Attribution** | `ai-hashes`, `ai-commits` | Track AI-generated code |
| **Transcripts** | `agent-transcript`, `transcript-index`, `dotcursor-status`, `dotcursor-terminals` | ~/.cursor plaintext data |
| **Extensions** | `extensions` | Installed Cursor extensions |

### Output Formats (-f / --output-format)

Every command supports flexible output formats via the global `-f` flag:

```bash
cursor-mirror -f json status          # Compact JSON
cursor-mirror -f yaml list-workspaces # YAML for configs
cursor-mirror -f csv tools @1         # CSV for spreadsheets
cursor-mirror -f md models            # Markdown tables
cursor-mirror -f jsonl tail @1        # JSON Lines for streaming
cursor-mirror --pretty -f json status # Pretty-printed JSON
```

| Format | Description | Best For |
|--------|-------------|----------|
| `text` | Human-readable tables (default) | Terminal viewing |
| `json` | Compact JSON | API consumption, LLM parsing |
| `jsonl` | JSON Lines (one object per line) | Streaming, log processing |
| `yaml` | YAML format | Config files, readable structured data |
| `csv` | CSV with union of all keys | Spreadsheets, data analysis |
| `md` | Smart markdown (tables + outlines) | Documentation, chat output |

**Smart Markdown**: The `-f md` output adapts to data structure:
- Lists of flat dicts → Tables
- Nested dicts → Headers (`##`) + bullet outlines
- Arrays → Bullet lists
- Long strings → Code blocks

**Union-of-Keys CSV**: When records have different fields, CSV collects ALL keys across ALL records. Missing values become empty cells. Nested objects are JSON-encoded inline.

### Data Sources (--sources)

Add `--sources` to any command to see WHERE the data comes from:

```bash
cursor-mirror --sources -f md list-composers -n 3

# Output includes markdown table PLUS:
# DATA SOURCES — Query these directly for raw access
# 📁 DATABASES: /Users/.../globalStorage/state.vscdb
# 📊 TABLES: ItemTable, cursorDiskKV
# 🔍 SQL: SELECT value FROM ItemTable WHERE key='composer.composerData'
```

This teaches LLMs to fish! They can then query the databases directly.

### Reference Shortcuts

Commands accept flexible references:

| Format | Example | Resolution |
|--------|---------|------------|
| `@N` | `@1` | Nth largest by message count |
| Hash prefix | `769a26` | UUID/hash prefix match |
| Name fragment | `moollm` | Folder or title substring |
| Tree path | `w3.c2` | Workspace 3, composer 2 |

## Example Session

```bash
# Quick health check
$ cursor-mirror status
Workspaces: 23
Composers: 147
Messages: 12,847
Global DB: 89.2 MB
Largest workspace: moollm (15.3 MB)

# Navigate to largest conversation
$ cursor-mirror tree w1.c1
Composer: 9861c0a4-aa93-4992-a23e-93272e8b0017
Name: "Deep code review"
Messages: 142
Tool calls: 47
Files read: 23
Files written: 8

# Inspect reasoning
$ cursor-mirror thinking @1 | head -20
[2026-01-14 10:30:15] Thinking:
The user wants me to reorganize the file to be more sniffable...
I should move the interface definitions up and implementation down...

# Trace context assembly
$ cursor-mirror context-sources @1
fileSelections: 5 files
  - cursor_mirror.py (4537 lines)
  - CARD.yml (744 lines)
  - kernel/drivers/cursor.yml (356 lines)
selections: 2 code blocks
cursorRules: .cursorrules loaded
codebase_search: 3 queries, 15 results

# Direct SQL for edge cases
$ cursor-mirror sql --db global "SELECT key FROM cursorDiskKV WHERE key LIKE 'bubbleId:%' LIMIT 5"
```
