# Datasette + cursor-mirror Integration Design

How to expose cursor-mirror data through Datasette for web exploration,
URL sharing, JSON API access, and dashboards.

---

## Why Datasette

Simon Willison's Datasette takes SQLite databases and gives them:
- A web UI for browsing tables, running SQL, filtering, faceting
- A JSON API at every URL (add .json)
- 154+ plugins (maps, charts, search, auth, dashboards)
- One-command publishing to Fly, Vercel, Cloud Run
- Read-only by default (safe for cursor-mirror's stance)

cursor-mirror already produces SQLite:
- Transcript index .db files (one per transcript, with sections, tool_params, shell_commands tables)
- Reads Cursor's state.vscdb (ItemTable, cursorDiskKV)

The integration is: serve these databases through Datasette.

---

## Integration Layers

### Layer 1: Direct serve (zero code)

```bash
# Serve Cursor's global DB read-only
datasette ~/Library/Application\ Support/Cursor/User/globalStorage/state.vscdb

# Serve a transcript index
datasette ~/.cursor/projects/*/agent-transcripts/*.db

# Serve multiple databases at once
datasette state.vscdb transcript-index.db
```

This already works. Datasette opens any SQLite file and gives you a web UI.
The cursorDiskKV and ItemTable tables are immediately browsable.

### Layer 2: Consolidated export (cursor-mirror command)

New command: `cursor-mirror export-datasette`

Exports a consolidated SQLite database optimized for Datasette:
- sections table (from all transcript indexes)
- shell_commands table (with danger scores from R1 auditor)
- tool_calls table (from bubbles)
- composers table (metadata)
- workspaces table (metadata)
- feature_flags table (current vs model)
- model_usage table (which models used per session)

This produces a single .db file that Datasette can serve with full context.

### Layer 3: Datasette plugin (datasette-cursor-mirror)

A Datasette plugin that:
- Auto-discovers cursor-mirror .db indexes on the filesystem
- Renders transcript sections as formatted HTML (not raw text)
- Adds a /-/cursor-mirror dashboard page
- Shows shell command audit results with danger scoring
- Links back to transcript .txt files for full content

Pattern: same as datasette-showboat (receives data, renders it).

### Layer 4: Live streaming (future)

Inspired by datasette-showboat's SHOWBOAT_REMOTE_URL pattern:
- cursor-mirror's live daemon (R5) streams events to Datasette
- Real-time dashboard of agent activity
- Alerts for dangerous commands or secrets

---

## Data Schema for Consolidated DB

```sql
-- Transcript sections (from transcript_index.py)
CREATE TABLE sections (
    id INTEGER PRIMARY KEY,
    transcript_path TEXT,
    composer_id TEXT,
    workspace TEXT,
    type TEXT,        -- USER, ASSISTANT, TOOL_CALL, TOOL_RESULT, THINKING
    start_line INTEGER,
    end_line INTEGER,
    tool_name TEXT,
    user_query_preview TEXT,
    text_preview TEXT,
    timestamp TEXT
);

-- Shell commands (from extract_shell_commands)
CREATE TABLE shell_commands (
    id INTEGER PRIMARY KEY,
    section_id INTEGER REFERENCES sections(id),
    command TEXT,
    line INTEGER,
    danger_score REAL,    -- from R1 auditor when available
    in_yolo_allowlist BOOLEAN,
    composer_id TEXT,
    workspace TEXT
);

-- Tool calls (from bubbles)
CREATE TABLE tool_calls (
    id INTEGER PRIMARY KEY,
    composer_id TEXT,
    tool_name TEXT,
    params_json TEXT,
    is_error BOOLEAN,
    bubble_key TEXT,
    timestamp TEXT
);

-- Composers
CREATE TABLE composers (
    id TEXT PRIMARY KEY,
    name TEXT,
    workspace TEXT,
    workspace_folder TEXT,
    bubble_count INTEGER,
    created_at TEXT,
    updated_at TEXT
);

-- Feature flags (from feature_monitor)
CREATE TABLE feature_flags (
    flag TEXT PRIMARY KEY,
    model_value TEXT,
    live_value TEXT,
    drift BOOLEAN
);
```

---

## Implementation Plan

### Phase 1: Direct serve (works now)
- Document in skill README how to serve cursor-mirror data
- Add `datasette` to requirements.txt (it's already installed)
- Test: `datasette state.vscdb` on the user's machine

### Phase 2: Export command
- Add `cursor-mirror export-datasette --output cursor-mirror.db` command
- Consolidates transcript indexes + composer metadata + tool calls
- Optimizes with indexes for Datasette's faceting

### Phase 3: Plugin skeleton
- Create `datasette-cursor-mirror` package
- Auto-discover .db files from ~/.cursor/projects/
- Custom HTML templates for transcript rendering
- Dashboard at /-/cursor-mirror

### Phase 4: Canned queries
- Pre-built SQL queries exposed as Datasette canned queries:
  - "Dangerous shell commands" (sorted by danger_score)
  - "Most active composers this week"
  - "Tool usage breakdown"
  - "Feature flag drift report"
  - "MCP server activity"

### Phase 5: Streaming dashboard (after R5 live daemon)
- Inspired by datasette-showboat remote publishing
- cursor-mirror streams events -> Datasette receives and displays
- Real-time agent activity monitor

---

## Datasette Plugins to Use

| Plugin | Purpose |
|--------|---------|
| datasette-vega | Charts for tool usage, command frequency |
| datasette-cluster-map | If we add geolocation to any data |
| datasette-dashboards | Dashboard layouts from SQL queries |
| datasette-search-all | Full-text search across all tables |
| datasette-configure-fts | Enable FTS on transcript previews |
| datasette-pretty-traces | If we add ?_trace=1 support |
| datasette-auth-passwords | Protect sensitive data |

---

## Simon Connection

This integration is a direct conversation starter with Simon Willison:
- We're using his tool exactly as designed (SQLite -> web UI)
- The transcript index .db pattern aligns with his "baked data" philosophy
- A datasette-cursor-mirror plugin contributes to his ecosystem
- The live streaming idea extends his datasette-showboat pattern
- Security dashboard feeds his lethal trifecta research

See: DonHopkins/characters/don-hopkins/email/email-to-simon-willison.md
