# cursor-mirror Internals: What You Can Inspect, and Where It Lives

*Broken out of the cursor-mirror [README](../README.md). Schemas in [reference/](../reference/).*

### Conversation Structure

Cursor stores conversations in `cursorDiskKV` table (global SQLite DB):

```
Key: bubbleId:<composerId>:<bubbleId>
Value: JSON blob containing:
  - type: 1 (user) | 2 (assistant)
  - text: message content
  - codeBlocks: [{code, language, uri}]
  - selections: [{text, uri, startLine, endLine}]
  - toolCalls: [{name, parameters, result, status}]
  - thinking: {text} | string
  - context: {fileSelections, mentions, ...}
```

Example query:
```bash
cursor-mirror tail -n 10 --yaml
```

### Context Assembly

Cursor's context assembly pulls from multiple sources. The `messageRequestContext` key stores the full assembled context:

```
Key: messageRequestContext:<composerId>:<bubbleId>
Value: JSON with:
  - fileSelections: [{uri, contents, relevanceScore}]
  - selections: [{text, uri, range}]
  - terminalSelections: [{text}]
  - cursorRules: string (from .cursorrules)
  - codebase_search: [{path, contents, score}]
  - web_search: [{title, url, snippet}]
```

Example:
```bash
cursor-mirror context-sources @1 --yaml
```

### Tool Execution

Every tool call is recorded with parameters and results:

```bash
cursor-mirror tools @1 -v

# Output:
# read_file_v2: 31 calls
#   params: {path: "kernel/drivers/cursor.yml", ...}
#   result: {content: "...", lines: 356}
# edit_file_v2: 12 calls
# SemanticSearch: 5 calls
```

### Server Configuration

Cursor's server pushes configuration to `ItemTable`:

```bash
cursor-mirror status-config --yaml

# Output:
# fullContextTokenLimit: 30000
# maxRuleLength: 100000
# maxMcpTools: 100
# absoluteMaxNumberFiles: 250000
# indexingPeriodSeconds: 272
```

These aren't documented. They're extracted by reading the database.

### MCP Servers

Model Context Protocol servers are tracked in `mcpService.knownServerIds`:

```bash
cursor-mirror status-mcp

# Output:
# cursor-ide-browser (builtin)
# svelte (user-configured)
```

## Architecture

### Data Locations (macOS)

Cursor maintains **two separate data stores**:

**1. Application Support (Structured SQLite):**

| Path | Content |
|------|---------|
| `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb` | Global: all conversations, tool results, config |
| `~/Library/Application Support/Cursor/User/workspaceStorage/<hash>/state.vscdb` | Per-workspace: composer metadata, prompts |
| `~/Library/Application Support/Cursor/User/workspaceStorage/<hash>/anysphere.cursor-retrieval/` | Indexing: embeddable files, folder descriptions |

**2. ~/.cursor (Plaintext Projects):**

| Path | Content |
|------|---------|
| `~/.cursor/ai-tracking/ai-code-tracking.db` | AI code attribution (80MB) |
| `~/.cursor/extensions/` | Cursor extensions (1.3GB) |
| `~/.cursor/projects/<workspace>/agent-transcripts/` | **Real-time plaintext transcripts!** |
| `~/.cursor/projects/<workspace>/agent-tools/` | Cached tool result outputs |
| `~/.cursor/projects/<workspace>/terminals/` | Terminal state snapshots |
| `~/.cursor/projects/<workspace>/mcps/` | MCP tool schemas (JSON) |

The composer UUID is the primary key across both systems. Cross-reference with:
```bash
cursor-mirror dotcursor-status          # Overview
cursor-mirror agent-transcript <id>     # Read transcript
cursor-mirror ai-hashes --stats         # AI code attribution
```

### Database Schema

**cursorDiskKV** (key-value store):
```sql
CREATE TABLE cursorDiskKV (key TEXT PRIMARY KEY, value BLOB);
```

Key patterns:
- `bubbleId:<cid>:<bid>` — Chat messages
- `agentKv:blob:<sha256>` — Cached tool results (content-addressed)
- `checkpointId:<cid>:<uuid>` — File snapshots before edits
- `messageRequestContext:<cid>:<bid>` — Full assembled context

**ItemTable** (VS Code settings):
```sql  
CREATE TABLE ItemTable (key TEXT PRIMARY KEY, value BLOB);
```

Key patterns:
- `cursorai/serverConfig` — Server-pushed limits
- `mcpService.knownServerIds` — MCP server registry
- `modelMigration/*` — Model routing rules

### Safety

All database access uses SQLite URI mode with read-only flag:

```python
sqlite3.connect(f"file:{path}?mode=ro", uri=True)
```

No writes possible. The script cannot corrupt Cursor's data.
