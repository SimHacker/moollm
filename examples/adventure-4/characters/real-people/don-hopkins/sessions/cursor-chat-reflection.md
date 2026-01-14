 # Session Log: Cursor Chat Reflection & Skill Bootstrap
 ## Session — Cursor Chat Retrocon
 
 **Player**: Don Hopkins  
 **Context**: Cursor IDE live chat (this session)  
 **Goal**: Retrocon the Cursor chat into narrative, and seed a MOOLLM skill + sister scripts for reflecting on and managing Cursor chats.
 
 ---
 
 <details open>
 <summary><h2>⭐ Session Highlights & Intent</h2></summary>
 
 - Convened an ethically sourced hero-familiar party (Engelbart, Nelson, Shneiderman, Tesler, Liskov, Victor, Freudenberg, Wright) to guide chat reflection tooling.
 - Decided to write a new session log that itself becomes seed data for a Cursor-chat reflection skill.
 - Noted we need the actual Cursor chat export (Cursor data directory TBD) to ingest, index, and replay.
 - Committed to append-only storytelling; schemas and code will follow.
 
 </details>
 
 ---
 
 ## Cast: Hero Familiars (Tribute Roles)
 
 - **Doug Engelbart** — augmentation sage; keeps us pointed at shared views and collaborative uplift.
 - **Ted Nelson** — transclusion trickster; demands visible links, no silos, and branching-undo for chats.
 - **Ben Shneiderman** — first-magic steward; insists the chat reviewer feels obvious and humane.
 - **Larry Tesler** — mode-free guardian; hunts hidden modes in chat triage UX.
 - **Barbara Liskov** — contract architect; locks in schemas for chat artifacts (indexes, thread refs, citations).
 - **Bret Victor** — time-travel designer; wants scrubbable timelines and live previews of chat slices.
 - **Vanessa Freudenberg** — live-system caretaker; watches persistence and LLM-dependency footguns.
 - **Will Wright** — playtest conductor; treats the tool as a simulation to tune via emergent behavior.
 
 ---
 
 ## Scene 1 — The Prompt in Cursor
 
 We’re inside Cursor, building a skill to reflect on Cursor chats. The meta is the point: this very conversation becomes Exhibit A. The party assembles around the pie table, reading the current log and plotting how to bottle it.
 
 ---
 
 ## Needs & Sources
 
 - **Chat export needed**: Cursor chat log file (data directory path TBD). Once located, we’ll ingest for indexing/summarization.
 - **Artifacts to produce**:  
   - `skills/cursor-chat/` (CARD.yml, SKILL.md, README.md)  
   - Sister scripts (Python) to extract, index, search, and summarize chat logs (likely under `.moollm/` for local use).  
   - Session narratives (this file) to serve as living test data.
 - **Ethics**: Tribute style; no impersonation. Treat real people as inspirations, not puppets.
 
 ---
 
 ## Scene 2 — Design Beats (spoken around the table)
 
 - Doug: “Start with shared state — one indexed corpus of chats, many coordinated views.”
 - Ted: “Expose transclusions; every quote knows its origin. Branching-undo for edits.”
 - Ben: “Default view shows status and lets you act in one gesture; no mystery meat.”
 - Larry: “No hidden modes. Commands stay consistent whether browsing or annotating.”
 - Barbara: “Define schemas now: chat message records, threads, citations, summaries.”
 - Bret: “Add a timeline scrubber; previews update live as you move.”
 - Vanessa: “Keep the pipeline debuggable; don’t bury persistence behind LLM fog.”
 - Will: “Playtest the flows; watch what emergent behaviors show up in real use.”
 
 ---
 
 ## Scene 3 — Plan Sketch (v0)
 
 1) Locate Cursor chat data directory and export this session.  
 2) Write extraction + indexing sister script (Python) to produce:  
    - message JSONL,  
    - summary shards,  
    - citation map (message → file/line).  
 3) Draft `skills/cursor-chat/` CARD + SKILL to wrap operations: LIST, VIEW, SEARCH, SUMMARIZE, CITE.  
 4) Generate working-set/hot hints for Cursor (advisory).  
 5) Bake this narrative as seed test data; rerun the pipeline to validate.  
 
 ---
 
 ## Open Questions
 
 - Where exactly is Cursor storing the current chat transcript on this machine? (Once we have the path, we’ll pull a copy into `.moollm/` for local processing; source of truth stays in Cursor’s data dir.)
 - Preferred output shapes? (Markdown summaries, JSONL indexes, citation-ready snippets?)
 
 ---
 
 ## Next Hooks
 
 - After the export path is known: run sister script to ingest and attach citations back into this log.
 - Spin up `skills/cursor-chat/` skeletons next (CARD/README/SKILL) with the party’s principles embedded.
 
 ---
 
 *Session recorded as part of the Cursor-chat reflection skill birth. Append-only; future updates will extend this log once the raw chat export is in hand.*

---

## Scene 4 — Summoning Cursor (self) to locate the chat log

- Invited **Cursor (embodied IDE)** to the table to ask: “Where do you keep our chat transcripts on macOS?”
- Cursor answers by peeking into its own library:
  - Found global storage DB at `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb` (tables: `ItemTable`, `cursorDiskKV`).
  - Keys mentioning chat exist (e.g., `chat.participantNameRegistry`, `chat.setupContext`, many `workbench.panel.composerChatViewPane.*` flags), but no message bodies surfaced yet.
  - Workspace hash for this repo located: `~/Library/Application Support/Cursor/User/workspaceStorage/5f84080d5e3d62d2b51c5314ef1c508d/` (contains `anysphere.cursor-retrieval` metadata).
  - Next likely hiding spots: `User/Local Storage/leveldb/` and `workspaceStorage/<hash>/*` LevelDB or JSON blobs; also possible blobs in `Session Storage/` or `WebStorage/`.
- Ask Cursor-familiar to keep poking (via terminal/sqlite) for keys like `chatSession`, `conversation`, `composer` within LevelDB and per-workspace state. Once found, we’ll copy a readonly export into `.moollm/` for processing (source of truth stays in Cursor data dir).

---

## Scene 5 — Transparent spelunking log (commands + findings)

We dropped marker `CURSOR_CHAT_MARKER_2026_01_14_X7` in this chat, then hunted for it and other clues. Commands and results:

```shell
# Recent files under Cursor support (last 24h)
python - <<'PY'
import os, time, pathlib
root = pathlib.Path(os.path.expanduser('~/Library/Application Support/Cursor'))
cutoff = time.time() - 24*3600
entries = []
for dirpath, dirnames, filenames in os.walk(root):
    for name in filenames:
        p = pathlib.Path(dirpath)/name
        try: st = p.stat()
        except OSError: continue
        if st.st_mtime >= cutoff:
            entries.append((st.st_mtime, p))
entries.sort(reverse=True)
for ts, p in entries[:40]:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts)), p)
PY
```
- Highlights: updated `User/globalStorage/state.vscdb`, `workspaceStorage/5f84080d5e3d62d2b51c5314ef1c508d/state.vscdb`, multiple Cursor logs, and GPU/Cache artifacts. No obvious chat transcript yet.

```shell
# Marker scan across Cursor support dir
rg -a "CURSOR_CHAT_MARKER_2026_01_14_X7" "~/Library/Application Support/Cursor"
```
- Result: no hits (marker not persisted in accessible files).

```shell
# LevelDB strings keyword scan
python - <<'PY'
import os, subprocess, pathlib, re
level = pathlib.Path(os.path.expanduser('~/Library/Application Support/Cursor/Local Storage/leveldb'))
if not level.exists():
    print('leveldb dir missing'); raise SystemExit
files = sorted([p for p in level.iterdir() if p.is_file()])
keys = re.compile(rb'chat|conversation|composer|transcript|history', re.IGNORECASE)
for p in files:
    try:
        data = subprocess.check_output(['strings', str(p)], stderr=subprocess.DEVNULL)
    except Exception:
        continue
    if keys.search(data):
        print(f"HIT in {p.name}")
PY
```
- Hit: `000003.log`

```shell
# Inspect the hit
strings "~/Library/Application Support/Cursor/Local Storage/leveldb/000003.log" | rg -n "chat|conversation|composer|transcript|history"
```
- Findings: only `pdfjs.history` entries (PDF viewer state), not chat messages.

Status: Still no chat transcript located. Next probes: scan `User/workspaceStorage/*/state.vscdb` for message-like blobs; inspect `History/` subdirs; check `Local Storage/leveldb` further for other logs; watch for new files during active chat.

---

## Scene 6 — Deeper probes (du, workspace sqlite, big keys)

```shell
# Disk usage snapshot of key Cursor dirs
du -sh ~/Library/Application\\ Support/Cursor/{User,Local\\ Storage,Session\\ Storage,WebStorage,Cache,Workspaces}
```
- User: 18G, Local Storage: 76K, Session Storage: 28K, WebStorage: 180M, Cache: 183M, Workspaces: 4K.

```shell
# List workspace state databases
find ~/Library/Application\\ Support/Cursor/User/workspaceStorage -name '*.vscdb'
```
- Many hashes; active workspace: `5f84080d5e3d62d2b51c5314ef1c508d/state.vscdb`.

```shell
# Chat-ish keys in active workspace state.vscdb
sqlite3 ".../workspaceStorage/5f84080d5e3d62d2b51c5314ef1c508d/state.vscdb" "PRAGMA table_info('ItemTable'); SELECT key FROM ItemTable WHERE key LIKE '%chat%' LIMIT 20;"
```
- Only view counters: `workbench.panel.aichat.<uuid>.numberOfVisibleViews`.

```shell
# Large entries in workspace state
sqlite3 -readonly ".../state.vscdb" "SELECT key, length(value) FROM ItemTable WHERE length(value) > 1024 ORDER BY length(value) DESC LIMIT 20;"
```
- Largest: `aiService.prompts` (217,809 bytes), `aiService.generations` (69,849), `history.entries` (31,507), `composer.composerData` (20,907), plus memento/workbench* and find/history caches.

```shell
# Peek payload heads
sqlite3 -readonly ".../state.vscdb" "SELECT substr(value,1,1000) FROM ItemTable WHERE key='history.entries';"
sqlite3 -readonly ".../state.vscdb" "SELECT substr(value,1,1000) FROM ItemTable WHERE key='composer.composerData';"
sqlite3 -readonly ".../state.vscdb" "SELECT substr(value,1,800) FROM ItemTable WHERE key='aiService.generations';"
```
- `history.entries`: recent editor URIs.
- `composer.composerData`: composer heads (ids, names, timestamps, context usage, subtitles). No message bodies seen in the head slice.
- `aiService.generations`: generation request summaries (type=composer, textDescription). Not full transcripts.

Takeaway: Workspace `state.vscdb` holds meta (composer heads, generation summaries), not the chat message bodies. Next: scan other workspace hashes, inspect `User/History/*/entries.json`, and keep watching for other SQLite/LevelDB stores that might contain the full conversations.

---

## Scene 7 — Title note for this chat

- Cursor chat title observed: **“Cursor chat data management tools”**. Keep this as a label when hunting in composer metadata or future exports.

---

## Scene 8 — More digging: History snapshots, global state, recent files

```shell
# Most recent files in History (24h)
python - <<'PY'
import os, time, pathlib
root = pathlib.Path(os.path.expanduser('~/Library/Application Support/Cursor/User/History'))
cutoff = time.time() - 24*3600
entries = []
for dirpath, dirnames, filenames in os.walk(root):
    for name in filenames:
        p = pathlib.Path(dirpath)/name
        try: st = p.stat()
        except OSError: continue
        if st.st_mtime >= cutoff:
            entries.append((st.st_mtime, p))
entries.sort(reverse=True)
for ts, p in entries[:30]:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts)), p)
PY
```
- Fresh files under `History/-6d468580/`, including `entries.json` and markdown copies (`BfeM.md`, `wIHN.md`, `c77J.md`) of our session log—these are file-history snapshots, not chat transcripts.

```shell
# Inspect latest entries.json and a markdown snapshot
python - <<'PY'
import json, pathlib
p = pathlib.Path('/Users/a2deh/Library/Application Support/Cursor/User/History/-6d468580/entries.json')
print(p.read_text()[:400])
PY
```
- Shows `resource` pointing to our session log file and a single entry from “Undo Accept Diff”. No chat content.

```shell
# Global state heavy keys
sqlite3 -readonly "~/Library/Application Support/Cursor/User/globalStorage/state.vscdb" "SELECT key, length(value) FROM ItemTable WHERE length(value)>50000 ORDER BY length(value) DESC LIMIT 20;"
```
- Largest: `aiCodeTrackingLines` (2.4MB), `workbench.experiments.statsigBootstrap`, `iconThemeData`, `...reactiveStorage...`. Not chat.

```shell
# Composer-related keys in global state
sqlite3 -readonly "~/Library/Application Support/Cursor/User/globalStorage/state.vscdb" "SELECT key, length(value) FROM ItemTable WHERE key LIKE '%composer%' ORDER BY length(value) DESC LIMIT 20;"
``]
- Only hidden/view flags for composer panes; no message bodies.

Status update:
- History/ contains snapshots of edited files (including this session log) but not chat text.
- Workspace `state.vscdb` contains composer metadata and generation summaries but not conversations.
- Global `state.vscdb` has config/experiments and composer pane flags; no chat bodies.

Next moves:
- Probe other workspace hashes’ `state.vscdb` for similar keys and sizes.
- Scan `History/*/*.md` for actual chat text (so far, file snapshots only).
- Watch for LevelDB/other sqlite files updated during chat; consider live tailing modified files while the chat runs.

---

## Scene 9 — More hunts: sqlite/db, conversationId, web search claim

```shell
# Look for sqlite/db files under Cursor support
find ~/Library/Application\\ Support/Cursor -type f \\( -name '*.sqlite' -o -name '*.db' -o -name '*.sqlite3' -o -name '*.vscode-sqlite' \\)
```
- No results (aside from known `state.vscdb` files).

```shell
# Search for conversationId across Cursor/User
rg "conversationId" ~/Library/Application\\ Support/Cursor/User
```
- Hits point to code/history snapshots (e.g., `History/3bc63418/*.ts` logger code) and embeddable_files listings—these are project artifacts, not stored chat transcripts. They reference writing `conversation-<id>.jsonl` to debug dirs, but those files were not found.

```shell
# Web search (external) said: ~/Library/Application Support/Cursor/chat_logs
ls "~/Library/Application Support/Cursor/chat_logs"
```
- Path does **not** exist on this machine; likely outdated/incorrect for current Cursor builds.

Takeaway: Still no chat body store located. Promising lead is the `conversation-<id>.jsonl` logger pattern mentioned in history code; need to discover where (if anywhere) those logs are emitted in this install. Continued watch on newly modified files and workspace sqlite/LevelDB remains the plan.

---

## Scene 10 — Open files spelunk (lsof) and new leads

```shell
# Open files for Cursor processes (filtered)
lsof -c Cursor 2>/dev/null | rg -i "chat|conversation|workspaceStorage|History|vscdb|leveldb|sqlite|jsonl"
```
- Open handles:
  - `Local Storage/leveldb/{LOG, MANIFEST-000001, 000003.log}` (pdfjs history only so far).
  - Multiple workspace `state.vscdb`: `5f84080d5e3d62d2b51c5314ef1c508d` (active), `2a366cf7...`, `8151f5e...`, `c58ffab5...`, `769a2689...`.
  - **Global** `User/globalStorage/state.vscdb` open — ~9 GB (main KV store).
  - HTTP storages sqlite trio: `/Users/a2deh/Library/HTTPStorages/com.todesktop.230313mzl4w4u92/httpstorages.sqlite` (+wal, +shm).

```shell
# Global state targeted queries
sqlite3 -readonly "~/Library/Application Support/Cursor/User/globalStorage/state.vscdb" \
  "SELECT key, length(value) FROM ItemTable WHERE key LIKE '%conversation%' ORDER BY length(value) DESC LIMIT 50;"
sqlite3 -readonly "~/Library/Application Support/Cursor/User/globalStorage/state.vscdb" \
  "SELECT key, length(value) FROM ItemTable WHERE key LIKE '%chat%' ORDER BY length(value) DESC LIMIT 50;"
```
- `conversation%`: only `conversationClassificationScoredConversations` (tiny).
- `chat%`: pane visibility flags + `chat.participantNameRegistry` (~1.3 KB). No message bodies.

```shell
# HTTP storages sqlite tables
sqlite3 "/Users/a2deh/Library/HTTPStorages/com.todesktop.230313mzl4w4u92/httpstorages.sqlite" ".tables"
```
- Only `alt_services` (likely network alt-svc cache; no chat content).

Status: The largest open file (`globalStorage/state.vscdb`) still presents config/flags, not conversations; workspace `state.vscdb` carries composer metadata; LevelDB shows pdfjs history; HTTPStorages not relevant. Still no chat transcripts in sight.

Next: sample other workspace `state.vscdb` for big blobs; live-tail modified files during chat; continue hunting for any `conversation-*.jsonl` files or new LevelDB logs created mid-chat.

---

## Scene 11 — Map & classify stores (current reverse-engineer pass)

```yaml
stores:
  globalStorage/state.vscdb:
    type: sqlite (ItemTable, cursorDiskKV)
    size: ~9 GB (open)
    content: configs/flags/registries; chat pane visibility; participantNameRegistry; no chat bodies found
  workspaceStorage/<hash>/state.vscdb:
    type: sqlite (ItemTable)
    observed: composer heads (metadata), aiService.prompts/generations, history.entries (editor URIs); no message bodies
    open_hashes_seen:
      - 5f84080d5e3d62d2b51c5314ef1c508d (active repo)
      - 2a366cf7..., 8151f5e..., c58ffab5..., 769a2689..., others
  Local Storage/leveldb:
    files: LOG, MANIFEST-000001, 000003.log (open)
    content_seen: pdfjs.history only; no chat
  Session Storage:
    status: TODO (no hits yet)
  WebStorage:
    size: ~180 MB; status: TODO
  HTTPStorages/com.todesktop.230313mzl4w4u92/httpstorages.sqlite(+wal,+shm):
    tables: alt_services
    content: network alt-svc cache; no chat
  History/*:
    content: file edit snapshots (including our session log copies); not chat
  Missing:
    - No `conversation-*.jsonl` files found
    - No chat_logs/ directory
    - No chat bodies in examined sqlite/leveldb so far
next_hunts:
  - Sample other workspace state.vscdb for large blobs or message-like KVs
  - Live-tail modified files during active chat for new writes
  - Scan WebStorage/Session Storage for message text
  - Re-run lsof while sending messages to catch newly opened files
```

---

## Scene 12 — Sniffing top keys in workspace state (evidence)

Active workspace `state.vscdb` (`5f84080d5...`), top keys by size and snippets:
- `aiService.prompts` (217,809 bytes): JSON array of prompt texts/commands (e.g., “focus on sniffing all the skill cards…”).
- `aiService.generations` (69,849 bytes): JSON array of generation requests (type=composer, textDescription).
- `memento/workbench.editors.files.textFileEditor` (55,430 bytes): editor view state JSON.
- `history.entries` (31,507 bytes): list of recently opened file URIs.
- `memento/workbench.parts.editor` (27,606 bytes): editor layout state JSON.
- `composer.composerData` (20,907 bytes): composer heads (ids, names, timestamps, subtitles, context usage).
- Others: targetStorageMarker, auxiliarybar view state, terminal env collections, ms-python settings.

Large workspace `c58ffab5...` shows same pattern (bigger prompts/generations; composer heads; history). No chat message bodies observed in any of these values. Table schema in global/workspace DBs is flat K/V: `ItemTable(key TEXT UNIQUE, value BLOB)` and `cursorDiskKV(key, value)`.

---

## Scene 13 — User Messages from THIS Chat (9861c0a4)

**RETCON**: The data below was from a different workspace. The actual user prompts from THIS chat (`bubbleId:9861c0a4%`, type=1) — **52 messages**:

```
2026-01-14T00:18:15  BOOT and assemble a party of eight most relevent software designers...
2026-01-14T00:22:40  make a new don hopkins session cursor-chat-reflection.md and retrocon...
2026-01-14T00:26:30  Now let's create the new skills/cursor-chat skill and make yaml files...
2026-01-14T00:31:35  The title of this chat is "Cursor chat data management tools" FWIW
2026-01-14T00:47:10  well keep looking stop giving up! USE THE SQLITE TOOL TO LOOK AT SCHEMAS!
2026-01-14T01:05:57  how should we design the sister script for inspecting cursor workspaces...
2026-01-14T01:11:38  put main as first function that define cli api as per sniffable python
2026-01-14T01:32:03  we will ALWAYS have yaml do NOT be so defensive
2026-01-14T01:34:57  ok make this more robust and featureful and production ready!
2026-01-14T02:44:34  yes expose much more! i want to analyze a moollm boot sequence
2026-01-14T02:51:43  ok keep hacking!
```

**Key discovery**: `aiService.prompts` contains prompts from ALL chats in that workspace (mixed sessions). The actual per-conversation messages live in `cursorDiskKV` with `bubbleId:<composerId>:<messageId>` keys — which is what we needed to find!

---

## Scene 14 — THE BREAKTHROUGH: cursorDiskKV bubbleId keys

**Discovery**: Chat messages live in `globalStorage/state.vscdb` table `cursorDiskKV`, not `ItemTable`!

```shell
# Found the gold
sqlite3 -readonly "~/Library/.../globalStorage/state.vscdb" \
  "SELECT key FROM cursorDiskKV WHERE key LIKE 'bubbleId:%' LIMIT 5;"
```
- Keys follow pattern: `bubbleId:<composerId>:<messageId>`
- Values are JSON blobs with `text`, `type` (1=user, 2=assistant), `createdAt`, and rich metadata

**Key structures discovered**:
```yaml
bubble_keys:
  pattern: "bubbleId:<composerId>:<bubbleId>"
  value_fields:
    - text: message content
    - type: 1=user, 2=assistant
    - createdAt: ISO timestamp
    - bubbleId: unique message ID
    - toolFormerData: tool calls with name/args/result/status
    - thinking: extended thinking content
    - codeBlocks: array of {languageId, content, relativePath}
    - selections: user code selections
    - lints: attached linter errors
    - context: {fileSelections, terminalSelections, cursorRules, mentions...}
    - todos: task list state
    - modelInfo: {modelName, ...}
    - isAgentic: boolean agent mode flag
    - checkpointId: file state tracking
```

**Other important keys**:
- `composer.composerData` in workspace `ItemTable` → conversation heads (IDs, names, timestamps)
- `aiService.prompts/generations` → prompt and generation summaries
- `agentKv:blob:<hex>` → cached context blobs (some hex-encoded)
- `messageRequestContext:<composerId>` → full context snapshots

---

## Scene 15 — cursor_chat_inspect.py Sister Script

Built a comprehensive Python CLI tool with 18+ commands:

```
cursor-chat list-workspaces     # Show workspaces with folders & stats
cursor-chat show-workspace      # Detailed workspace info
cursor-chat list-composers      # List conversations with metadata
cursor-chat show-composer       # Composer details + message counts

cursor-chat tail -n 50          # Last N messages, pretty printed
cursor-chat stream --since 1h   # Unified activity stream
cursor-chat grep "pattern" -i   # Regex search across chats
cursor-chat transcript <id>     # Readable conversation transcript

cursor-chat tools <id> -v       # List all tool calls with results
cursor-chat todos <id>          # Show task list state
cursor-chat context <id>        # Context gathered (files, terminal, rules)
cursor-chat analyze <id>        # Deep analysis: tools, files, models, duration
cursor-chat timeline <id>       # Chronological timeline of all events

cursor-chat files <id>          # Files touched in conversation
cursor-chat models              # Model usage analysis
cursor-chat stats               # Summary statistics
cursor-chat export-chat <id>    # Export as JSON/YAML
```

**Design principles** (from the hero familiars):
- **Sniffable Python**: CLI API defined at top of script
- **Read-only**: Never modifies Cursor data
- **YAML Jazz**: `--yaml` output for all commands
- **Pretty printing**: 🔧 tools, 💭 thinking, 📝 code, ⚠️ lints

---

## Scene 16 — DATA-SCHEMAS.yml (Platform-Neutral Documentation)

Created `skills/cursor-chat/DATA-SCHEMAS.yml` documenting all JSON structures:

```yaml
models:
  bubble:           # Single chat message
  composer:         # Conversation container (head metadata)
  prompt:           # User prompt record
  generation:       # AI generation request
  message_request_context: # Full context snapshot

embedded_objects:
  selection:        # Code selection (uri, range, content)
  lint:             # Linter error (message, severity, range)
  code_block:       # Code block (languageId, content, path)
  file_reference:   # File ref (uri, reason, type)
  tool_call:        # Tool invocation (name, args, status)
  tool_result:      # Tool output (callId, content, success)
  context:          # Context bundle (files, terminal, rules, mentions)
  symbol:           # Code symbol (name, kind, location)

enums:
  lint_severity:    [error, warning, information, hint]
  tool_status:      [pending, running, completed, error, cancelled]
  composer_mode:    [chat, agent, edit, review]
```

---

## Scene 17 — Analyzing a MOOLLM Boot Sequence

Used `cursor-chat analyze 2c95d1a3` on the adventure-4 boot session:

```
═══ Analysis: 2c95d1a3-a760-416a-a807-... ═══

Messages: 1374 total
  User: 86
  Assistant: 1287
  With tools: 532
  With code: 392

Duration: 23104s (6+ hours)
  Start: 2026-01-10 00:05:24
  End: 2026-01-10 06:30:28

Models used:
   174x claude-4.5-opus-high-thinking

Tool calls (532 total):
   257x search_replace (8 err)
   103x read_file
    57x write
    42x grep
    31x run_terminal_cmd
    19x todo_write
    13x list_dir
     6x web_search
     4x glob_file_search

Files read (53): startup.yml, PROTOCOLS.yml, ADVENTURE.yml...
Files written: session files, CHARACTER.yml, ROOM.yml...

Final todos (8):
  ✓ adventure.py lint
  ✓ Added --format outputs
  → adventure.py compile (in progress)
  ○ adventure.py serve (pending)
```

**Timeline sample** (boot sequence):
```
2026-01-10 00:05:24  📝 USER: BOOT MOOLLM!
2026-01-10 00:05:28  🔧 ✓ read_file: startup.yml
2026-01-10 00:05:29  🔧 ✓ read_file: PROTOCOLS.yml
2026-01-10 00:05:30  🔧 ✓ read_file: working-set.yml
2026-01-10 00:05:36  🔧 ✓ read_file: cursor.yml (driver)
2026-01-10 00:05:38  🔧 ✓ read_file: ADVENTURE.yml
2026-01-10 00:05:57  🤖 ASST: # 🚀 MOOLLM BOOT SEQUENCE COMPLETE
```

---

## Scene 18 — This Session's Stats

`cursor-chat analyze 9861c0a4` (the cursor-chat skill bootstrap session):

```
═══ Analysis: 9861c0a4-aa93-4992-a23e-... ═══

Messages: 628 total
  User: 49
  Assistant: 579
  With tools: 300

Duration: ~2.5 hours

Models used:
    34x gpt-5.1-codex-max
     8x claude-4.5-opus-high-thinking

Tool calls (300 total):
   125x run_terminal_command_v2
    87x edit_file_v2 (8 err)
    44x read_file_v2
    22x ripgrep_raw_search
     9x list_dir_v2
     9x web_search
     4x glob_file_search
```

---

## Goals & Next Steps

### Completed ✓
- [x] Located Cursor chat data (`globalStorage/state.vscdb` → `cursorDiskKV`)
- [x] Documented storage layout (`MAC-STORAGE.yml`, `LINUX-STORAGE.yml`, `WINDOWS-STORAGE.yml`)
- [x] Documented JSON schemas (`DATA-SCHEMAS.yml`)
- [x] Built `cursor_chat_inspect.py` with **24 commands** (~1900 lines)
- [x] Added boot sequence analysis (`analyze`, `timeline`, `tools`, `todos`)
- [x] Added context inspection (`context`, `files`)
- [x] Added search capabilities (`grep`, `tail`, `stream`)
- [x] Decoded `agentKv:blob:` keys → `blobs` + `tool-result` commands (full tool output recovery!)
- [x] Parsed `checkpointId` for file state tracking → `checkpoints` command
- [x] Added `thinking` command to show model reasoning blocks
- [x] Added `watch` command for conversation replay with timeline

### In Progress →
- [ ] Add `diff` command to show changes between checkpoints
- [ ] Create MOOLLM skill card (`CARD.yml`) for chat reflection

### Pending ○
- [ ] Build index/summary generation for chat archives
- [ ] Export conversations to Markdown/JSONL archives
- [ ] Integrate with session log generation (auto-document conversations)

---

## Session 13b — Final Tool Summary

**24 Commands** organized by function:

```
# Navigation
list-workspaces, show-workspace, list-composers, show-composer

# Message Viewing  
tail, stream, transcript, watch

# Search & Analysis
grep, analyze, timeline

# Tool & Agent Inspection
tools, tool-result, blobs, checkpoints, thinking

# Context & Files
context, files, todos

# Export & Stats
export-chat, export-prompts, models, stats, info
```

**Stats at session end:**
- 50,180 bubbles across 28 conversations
- 8.7GB global database indexed
- 730+ messages in this session alone
- Full introspection into Cursor's thinking and tool calls

---

## Scene 19 — Context Assembly Deep Dive

**Goal**: Understand how Cursor gathers and assembles context before each AI request.

### Discovery: `messageRequestContext`

Found rich context snapshots in `cursorDiskKV` under key `messageRequestContext:<composerId>:<messageId>`:

```yaml
# Full IDE state captured per message
ideEditorsState:
  visibleFiles:
    - relativePath: "designs/stanza-notes.md"
      isCurrentlyFocused: true
      currentLineNumber: 83
      lineCount: 963
  recentlyViewedFiles: [...]

currentFileLocationData:
  relativeWorkspacePath: "designs/stanza-notes.md"
  lineNumber: 83

todos: [...]           # Current task list
diffsSinceLastApply: [...]  # Pending code changes
deletedFiles: [...]    # Recently deleted files
```

### Discovery: `bubble.context` Field

Every user message (`bubble.type = 1`) carries attached context:

| Field | Count | Description |
|-------|-------|-------------|
| `mentions` | 3,274 | All @ mention types |
| `selections` | 348 | Code highlights |
| `terminalSelections` | 226 | Terminal output |
| `fileSelections` | 91 | @file mentions |
| `selectedImages` | 57 | Pasted images |
| `folderSelections` | 47 | @folder mentions |
| `externalLinks` | 24 | Web URLs |

### Discovery: Semantic Search System

```
workspaceStorage/<hash>/anysphere.cursor-retrieval/
├── embeddable_files.txt     # 9,442 files for embedding
└── high_level_folder_description.txt  # 100 "important" paths
```

**Indexing logs** reveal:
- Merkle tree computation (~20ms)
- Sync with `repo42.cursor.sh` backend
- Simhash vectors (256-dimensional)
- Per-file embedding uploads

**`codebase_search` results**:
```json
{"codeResults": [
  {"codeBlock": {
    "relativeWorkspacePath": "scripts/templates_py/ui_menu.py",
    "range": {"startPosition": {}, "endPosition": {"line": 29}},
    "contents": "class CustomMenu(bpy.types.Menu)..."
  }, "score": 0.87}
]}
```

### New Commands Added

| Command | Purpose |
|---------|---------|
| `context-sources <composer>` | Aggregate ALL context sources |
| `request-context <composer>` | Full assembled context for message |
| `searches <composer> -v` | Codebase + web searches with results |
| `indexing [workspace]` | Embeddable files + important paths |

---

## Scene 20 — MCP Tool Tracing

**Goal**: Trace Model Context Protocol (MCP) tool calls across sessions.

### Discovery: Known MCP Servers

Found in `ItemTable` under `mcpService.knownServerIds`:

```
[user   ] hackernews-bigquery
[user   ] leela-bigquery
[user   ] svelte
[user   ] puppeteer-nessus
[user   ] cursor-ide-browser
[project] svelte
```

### MCP Tool Naming Pattern

```
mcp_<server-name>_<tool-name>

Examples:
  mcp_cursor-ide-browser_browser_navigate
  mcp_puppeteer-nessus_browser_snapshot
  mcp_svelte_user-svelte-list-sections
```

### MCP Tool Call Structure

```yaml
toolFormerData:
  name: "mcp_cursor-ide-browser_browser_navigate"
  toolCallId: "uuid"
  status: "completed"
  rawArgs: '{"url": "https://..."}'
  result: '{"selectedTool": "browser_navigate", "result": {...}}'
```

### MCP Stats

```
$ cursor-chat mcp --all
MCP Tool Calls (89) - all conversations

🔌 cursor-ide-browser (76 calls)
  2026-01-10 08:34:45 ✓ browser_navigate

🔌 puppeteer-nessus (13 calls)
  2025-11-30 20:27:52 ✓ browser_press_key
```

### New Command Added

```bash
cursor-chat mcp --servers        # List known MCP servers
cursor-chat mcp --all -v         # All MCP calls globally
cursor-chat mcp <composer> -v    # MCP calls in conversation
```

---

## Updated Goals & Stats

### Completed ✓
- [x] Located Cursor chat data (`globalStorage/state.vscdb` → `cursorDiskKV`)
- [x] Documented storage layout (`MAC-STORAGE.yml`, `LINUX-STORAGE.yml`, `WINDOWS-STORAGE.yml`)
- [x] Documented JSON schemas (`DATA-SCHEMAS.yml` - 915 lines)
- [x] Built `cursor_chat_inspect.py` with **29 commands** (~2,500 lines)
- [x] Added boot sequence analysis (`analyze`, `timeline`, `tools`, `todos`)
- [x] Added context inspection (`context`, `files`)
- [x] Added search capabilities (`grep`, `tail`, `stream`)
- [x] Decoded `agentKv:blob:` keys → `blobs` + `tool-result` commands
- [x] Parsed `checkpointId` for file state tracking → `checkpoints` command
- [x] Added `thinking` command to show model reasoning blocks
- [x] Added `watch` command for conversation replay
- [x] **NEW**: Context assembly deep dive → `context-sources`, `request-context`, `searches`, `indexing`
- [x] **NEW**: MCP tool tracing → `mcp` command with `--servers`, `--all`, `-v`

### Pending ○
- [ ] Add `diff` command to show changes between checkpoints
- [ ] Create MOOLLM skill card (`CARD.yml`) for chat reflection
- [ ] Build index/summary generation for chat archives
- [ ] Export conversations to Markdown/JSONL archives

---

## Session 20 — Final Tool Summary

**29 Commands** organized by function:

```
# Navigation
list-workspaces, show-workspace, list-composers, show-composer

# Message Viewing  
tail, stream, transcript, watch

# Search & Analysis
grep, analyze, timeline

# Tool & Agent Inspection
tools, tool-result, blobs, checkpoints, thinking, mcp

# Context Assembly & Retrieval
context, context-sources, request-context, searches, indexing

# Files & Todos
files, todos

# Export & Stats
export-chat, export-prompts, models, stats, info
```

**Stats at session end:**
- 50,301 bubbles across 28 conversations
- 8.7GB global database indexed
- 89 MCP tool calls traced
- 14 known MCP servers
- 9,442 embeddable files per workspace
- Full introspection into Cursor's context assembly pipeline

---

---

## Scene 21 — The "WHY" Field: Tool Explanation Survey

**Insight**: The `explanation` parameter in `codebase_search` is Cursor's "WHY" field — capturing agent intent alongside action!

### Survey Results: 29 Unique Tools, 19,789 Total Calls

**4 Tools with `explanation` parameter:**

| Tool | Calls | Purpose of Explanation |
|------|-------|------------------------|
| `codebase_search` | 61 | "Search for Menu class definition and layout usage patterns" |
| `web_search` | 330 | "Search for when pie menus were officially added to Blender" |
| `run_terminal_cmd` | 3,737 | "Extract node metadata (idname, ui_name, description)" |
| `delete_file` | 65 | "Delete old file since content is now integrated elsewhere" |

### Pattern Analysis

The `explanation` field appears on tools that:
1. **Have side effects** (`delete_file`) - audit trail for destructive ops
2. **Make external calls** (`web_search`) - capture search intent
3. **Require semantic understanding** (`codebase_search`) - document WHY
4. **Execute arbitrary commands** (`run_terminal_cmd`) - explain purpose

### Tool Categories by Usage

```
file_ops:    12,153 calls  (read, write, search_replace, edit, delete)
execution:    5,139 calls  (run_terminal_cmd, run_terminal_command_v2)
search:       2,399 calls  (grep, rg, codebase_search)
web:            330 calls  (web_search)
meta:           334 calls  (todo_write, switch_mode)
mcp:             89 calls  (browser tools)
```

### Top 10 Most Used Tools

```
1. search_replace      4,941 calls
2. read_file           4,041 calls
3. run_terminal_cmd    3,737 calls
4. grep                1,444 calls
5. run_terminal_cmd_v2 1,402 calls
6. write               1,139 calls
7. edit_file_v2        1,042 calls
8. apply_patch         1,007 calls
9. read_file_v2          675 calls
10. rg                   501 calls
```

### MCP Tools Discovered

```
cursor-ide-browser (76 calls):
  browser_navigate (70), browser_click (3), browser_type (1),
  browser_select_option (1), browser_snapshot (1)

puppeteer-nessus (13 calls):
  browser_navigate (10), browser_click (1), browser_press_key (1),
  browser_snapshot (1)
```

### New File Created

`skills/cursor-chat/TOOLS-CATALOG.yml` — Complete tool survey with:
- All 29 tools with parameter schemas
- Explanation field analysis
- MCP tool documentation
- Usage statistics by category

---

## Updated Goals & Stats

### Completed ✓
- [x] Located Cursor chat data
- [x] Documented storage layout (3 platform files)
- [x] Documented JSON schemas (`DATA-SCHEMAS.yml` - 915 lines)
- [x] Built `cursor_chat_inspect.py` with **29 commands** (~2,500 lines)
- [x] Context assembly deep dive (4 new commands)
- [x] MCP tool tracing (`mcp` command)
- [x] **NEW**: Tool survey with "WHY" field analysis (`TOOLS-CATALOG.yml`)

### Stats
- 29 unique tools cataloged
- 19,789 total tool calls analyzed
- 4 tools with `explanation` (WHY) parameter
- 89 MCP tool calls traced

---

---

## Scene 22 — Completing the Pending Tasks

**Goal**: Implement all pending features from the task list.

### Task 1: `diff` Command ✓

Shows changes between file checkpoints in a conversation:

```bash
$ cursor-chat diff c7bf68cd --from 0 --to 10
═══ Diff: Checkpoint 0 → 10 ═══
From: 00c1a388-890  To: 08fea736-4e9

➖ Removed (12):
  /Users/a2deh/Blender/notes/PieMenuHistory.md
  /Users/a2deh/.../cocosynth/__init__.py
  ...
```

### Task 2: Updated CARD.yml ✓

Comprehensive skill card with all 33 methods documented:
- Navigation (4): list-workspaces, show-workspace, list-composers, show-composer
- Message Viewing (4): tail, stream, transcript, watch
- Search & Analysis (3): grep, analyze, timeline
- Tool & Agent Inspection (7): tools, tool-result, blobs, checkpoints, diff, thinking, mcp
- Context Assembly (5): context, context-sources, request-context, searches, indexing
- Files & Todos (2): files, todos
- Export & Stats (8): export-chat, export-markdown, export-jsonl, export-prompts, models, stats, info, index

### Task 3: `index` Command ✓

Generates searchable index of all conversations:

```yaml
$ cursor-chat index --yaml
generated: '2026-01-14T04:24:34'
total_conversations: 28
conversations:
- id: 9861c0a4-aa93-4992-a23e-93272e8b0017
  title: 'BOOT and assemble a party of eight...'
  started: '2026-01-14 00:18:15'
  message_count: 930
  tools_used: [edit_file_v2, glob_file_search, ...]
  keywords: [cursor, designers, session, ...]
```

### Task 4: Export Commands ✓

**`export-markdown`** - Readable Markdown with optional tools/thinking:
```bash
$ cursor-chat export-markdown 9861c0a4 --tools -o session.md
```

**`export-jsonl`** - JSONL for training/analysis:
```bash
$ cursor-chat export-jsonl 9861c0a4 --include messages tools thinking
{"type": "user_message", "timestamp": "...", "content": "BOOT MOOLLM!"}
{"type": "tool_call", "tool": "read_file_v2", "status": "completed", ...}
{"type": "assistant_message", "timestamp": "...", "content": "# 🚀 MOOLLM..."}
```

---

## Final Stats

### Skill Files

| File | Lines | Purpose |
|------|-------|---------|
| `cursor_chat_inspect.py` | 2,920 | Main inspector (33 commands) |
| `DATA-SCHEMAS.yml` | 916 | JSON schema documentation |
| `TOOLS-CATALOG.yml` | 398 | Tool survey with WHY field |
| `CARD.yml` | 285 | MOOLLM skill interface |
| `MAC-STORAGE.yml` | 205 | macOS path documentation |
| **Total** | ~5,000 | Complete skill package |

### Command Summary

```
33 Commands organized by function:

# Navigation
list-workspaces, show-workspace, list-composers, show-composer

# Message Viewing  
tail, stream, transcript, watch

# Search & Analysis
grep, analyze, timeline

# Tool & Agent Inspection
tools, tool-result, blobs, checkpoints, diff, thinking, mcp

# Context Assembly & Retrieval
context, context-sources, request-context, searches, indexing

# Files & Todos
files, todos

# Export & Stats
export-chat, export-markdown, export-jsonl, export-prompts, 
models, stats, info, index
```

### Data Surveyed

| Metric | Value |
|--------|-------|
| Total tool calls analyzed | 19,789 |
| Unique tools cataloged | 29 |
| Tools with `explanation` (WHY) | 4 |
| MCP servers traced | 14 |
| MCP tool calls | 89 |
| Conversations indexed | 28 |
| Bubbles (messages) | 50,301 |
| Global DB size | 8.7 GB |

---

## All Goals Complete ✓

- [x] Located Cursor chat data (`globalStorage/state.vscdb` → `cursorDiskKV`)
- [x] Documented storage layout (3 platform files)
- [x] Documented JSON schemas (`DATA-SCHEMAS.yml` - 916 lines)
- [x] Built `cursor_chat_inspect.py` with **33 commands** (~2,920 lines)
- [x] Context assembly deep dive (5 new commands)
- [x] MCP tool tracing (`mcp` command)
- [x] Tool survey with "WHY" field analysis (`TOOLS-CATALOG.yml`)
- [x] **`diff` command** - Show changes between checkpoints
- [x] **Updated `CARD.yml`** - Full MOOLLM skill interface
- [x] **`index` command** - Searchable conversation index
- [x] **`export-markdown`** - Readable Markdown export
- [x] **`export-jsonl`** - Training/analysis JSONL export

---

---

## Scene 23 — Orchestration Deep Dive

**Goal**: Understand Cursor's orchestration internals for MOOLLM bootstrap/probe/driver design.

### Discovery: 68-Field Bubble Structure

Every message (bubble) in Cursor captures **68 fields** — the complete snapshot of agent state:

```yaml
# Identity
bubbleId, type, createdAt, requestId, isAgentic, unifiedMode

# Context Sources (17 fields!)
attachedCodeChunks, attachedFolders, codebaseContextChunks,
cursorRules, docsReferences, projectLayouts, webReferences,
knowledgeItems, relevantFiles, summarizedComposers...

# Tool Integration
toolFormerData: {name, rawArgs, result, status, toolCallId}
supportedTools, mcpDescriptors, toolResults

# AI Features
thinking: {text, signature}
allThinkingBlocks, aiWebSearchResults, interpreterResults

# Capabilities (12 numeric types!)
capabilities, capabilityType, capabilityStatuses, capabilityContexts
```

### Discovery: Feature Configuration

**Runtime Limits** (`cursorai/featureConfigCache`):
```yaml
readFilesToolMaxLines: 1500
readFileToolMaxChars: 100000
editFileToolMaxFileSizeInLinesBeforeSwitchingToSearchReplace: 3500
listDirV2ClientSideCharacterBudget: 2500
fileSearchToolMaxResults: 10
composerMaxOpenTabs: 5
```

**Feature Flags** (`cursorai/featureStatusCache`):
```yaml
# Enabled
enableAgentWebSearch: True
clientSideParallelToolCalls: True
enableProjectLayoutsInSystemPrompt: True
autoSaveAgenticEdits: True

# Disabled
chatUsesTools: False
enableGitCheckpoints: False
debug_mode_enabled: False
```

### Discovery: Server Configuration

**Chat Limits** (`cursorai/serverConfig`):
```yaml
fullContextTokenLimit: 30000
maxRuleLength: 100000
maxMcpTools: 100
warnMcpTools: 80
numFilesForMemoryGeneration: 999999
```

**Indexing**:
```yaml
absoluteMaxNumberFiles: 250000
maxConcurrentUploads: 64
indexingPeriodSeconds: 272
maxBatchBytes: 2097152
```

### Discovery: Memory System

Cursor has persistent memories similar to MOOLLM's hot.yml!

```yaml
# ItemTable: cursorPendingMemories
- id: "cdcb43b6-..."
  title: "Custom metadata file convention"
  memory: "Project convention: all LLM-generated metadata is written into item-custom.json..."
  timestamp: 1752414225239
  
- id: "278c0550-..."
  title: "User dislikes hardcoding"
  memory: "The user hates hardcoding custom metadata fields..."
```

### Discovery: Data Store Summary

| Store | Key Pattern | Count | Purpose |
|-------|-------------|-------|---------|
| `bubbleId` | `bubbleId:<composer>:<msg>` | 50,467 | Messages |
| `agentKv` | `agentKv:blob:<hash>` | 25,544 | Tool results |
| `checkpointId` | `checkpointId:<composer>:<uuid>` | 10,019 | File state |
| `codeBlockDiff` | `codeBlockDiff:<composer>:<block>` | 6,865 | Code changes |
| `messageRequestContext` | `messageRequestContext:<composer>:<msg>` | 3,185 | Full context |
| `composerData` | `composerData:<composer>` | 36 | Conversation meta |

### New File Created

`ORCHESTRATION.yml` (380 lines) — Complete orchestration analysis:
- Bubble schema (68 fields documented)
- Feature configuration (runtime limits)
- Feature flags (enabled/disabled)
- Server configuration (token limits, indexing)
- Memory system (persistent memories)
- MOOLLM implications and recommendations

### MOOLLM Implications

**For Probe**:
- Capture feature flags like Cursor does
- Detect available tools (supportedTools pattern)
- Track context token usage

**For Bootstrap**:
- Implement memory persistence (like cursorPendingMemories)
- Add checkpoint system for state recovery
- Track files read/written for working-set

**For Kernel Driver Cursor**:
- Read feature flags from `cursorai/featureStatusCache`
- Respect runtime limits from `featureConfigCache`
- Integrate with Cursor's memory system

**For Orchestrator Design**:
- Token budget tracking (30,000 limit)
- Automatic context summarization
- Memory extraction from conversations
- File state checkpointing

---

## Scene 24 — Full Key Type Catalog

Agent performs complete histogram of all key types in cursorDiskKV and ItemTable stores.

### cursorDiskKV Histogram (102,724 keys, 11 patterns)

| Count | Percent | Key Type |
|------:|--------:|----------|
| 50,567 | 49.23% | `bubbleId:*` — Chat message bubbles |
| 25,819 | 25.13% | `agentKv:*` — Tool results/blobs |
| 10,019 | 9.75% | `checkpointId:*` — File state snapshots |
| 6,865 | 6.68% | `codeBlockDiff:*` — Code block changes |
| 5,179 | 5.04% | `codeBlockPartialInlineDiffFates:*` — Inline diff tracking |
| 3,185 | 3.10% | `messageRequestContext:*` — Full context snapshots |
| 975 | 0.95% | `composer.content.*` — Content cache by hash |
| 56 | 0.05% | `inlineDiffUndoRedo-*` — Undo/redo state |
| 36 | 0.04% | `composerData:*` — Conversation metadata |
| 13 | 0.01% | `inlineDiffs-*` — Inline diff tracking |
| 2 | 0.002% | `composer.autoAccept.*` — Git HEAD tracking |

### ItemTable Hidden Gems (382 keys, 165 prefixes)

**AI Code Tracking** (attribution analytics):
- `aiCodeTrackingLines` — 10,000 entries, 2.4MB! Tracks every AI-written line with hash + metadata
- `aiCodeTrackingScoredCommits` — 500 analyzed commits
- `aiCodeTracking.recentCommit` — Last commit with `aiPercentage` breakdown
- `aiCodeTracking.dailyStats.v1.5.DATE` — 34 days of daily stats

**Stats & Counters**:
- `freeBestOfN.promptCount` — **3,383** best-of-N prompts used!
- `languageStatus.interactCount`
- `commandPalette.mru.counter`

**MCP State**:
- `mcpService.knownServerIds` — Array of known MCP servers

**Privacy Mode**:
- `cursorai/donotchange/newPrivacyMode2` — `{"privacyMode":"PRIVACY_MODE_NO_TRAINING"}`
- `cursorai/donotchange/partnerDataShare` — false

**Terminal History**:
- `terminal.history.entries.commands` — 14KB of command history
- `terminal.history.entries.dirs` — 8KB of directory history

**Layout State**:
- `agentLayout.shared.v6` — Agent window dimensions and visibility
- `workbench.panel.*` — 159 per-panel visibility states

### New File: KEY-CATALOG.yml

Created comprehensive catalog documenting all key types, schemas, and MOOLLM integration notes.

---

## Final Session Stats

### Files Created/Updated

| File | Lines | Purpose |
|------|-------|---------|
| `cursor_chat_inspect.py` | 2,924 | 33 commands |
| `DATA-SCHEMAS.yml` | 916 | JSON schemas |
| `ORCHESTRATION.yml` | 380 | Orchestration internals |
| `KEY-CATALOG.yml` | ~400 | Complete key inventory |
| `MODELS.yml` | ~250 | AI model catalog |
| `MAC-CURSOR-APP.yml` | 425 | App bundle deep map |
| `TOOLS-CATALOG.yml` | 398 | Tool survey |
| `CARD.yml` | 310 | Skill interface |
| `MAC-STORAGE.yml` | 205 | User data paths |
| **Total** | ~6,200+ | Complete skill |

### Key Discoveries

- **68 fields** per message (bubble)
- **102,724 keys** in cursorDiskKV
- **11 distinct key patterns** cataloged
- **30,000 token** context limit
- **100 MCP tools** maximum
- **250,000 files** max indexing
- **10,000 lines** tracked for AI attribution
- **3,383 best-of-N** prompts used
- **Memory persistence** like hot.yml
- **12 capability types** (numeric)
- **Checkpointing** for file state recovery
- **34 days** of daily AI code stats

---

*Session continues. Cursor's complete internal state now documented for MOOLLM development.*
