# cursor-mirror Improvement Map

Strategic map of improvements, organized by ambition level.
Written after Phase 3 refactoring with the universal model and 22 assimilated sources.

Status: we have 9 lib modules, 13 command modules (73 commands), 58 tests,
universal model with 20+ YAML chunks, Python 3.14, data-driven from model.

---

## REVOLUTIONARY -- New systems

### R1. Shell Command Auditor

We know every `run_terminal_cmd` and `run_terminal_command_v2` call (5,139 total in
our analyzed data). We have the YOLO mode allowlist/denylist from composerState.
We have agent-permissions.yml listing what actions agents can take.

Build: a **real-time shell command scorer** that:
- Reads tool calls from bubbles where toolName = run_terminal_cmd*
- Extracts the command string
- Scores danger (rm -rf, curl | bash, pip install from unknown, chmod 777, etc.)
- Cross-checks against YOLO allowlist/denylist
- Produces a scored report with file:line K-REFs into transcripts
- Can run as post-hoc audit or (future) as live MCP hook

Model refs: tools.yml (execution category), agent-permissions.yml (terminal), features.yml (enableReviewModeForTerminal), dotcursor-schemas.yml (terminal_state)

Complexity: Medium. We already have cmd_secrets and the audit framework. This layers on top.

### R2. Skill Snitch v2 -- Behavior Analysis via cursor-mirror

We have cursor-mirror data (what an agent did) and the skill-snitch skill (static scan
+ runtime surveillance). Connect them:
- Analyze a session where a MOOLLM skill was active
- Extract: what files it read, what tools it called, what commands it ran, what it wrote
- Compare against the skill's declared permissions (MOOAM from skill CARD.yml)
- Flag: undeclared file access, unexpected tool usage, privilege escalation
- Output: snitch report with evidence (bubble IDs, transcript lines, timestamps)

This turns cursor-mirror from passive observer into active security monitor.

Model refs: tools.yml, agent-permissions.yml, dotcursor-schemas.yml (agent_transcript, agent_tool_cache)

Complexity: High. Needs MOOAM integration and skill permission model.

### R3. Cursor UI Bridge -- Read and Push via Extension/MCP

Cursor has MCP support (we see mcp-cache.json, tool schemas, server status).
We have the agent-permissions list. Build:
- An MCP server that exposes cursor-mirror data to Cursor itself
- Commands like `cursor-mirror serve` that starts the MCP
- Cursor agents can then query their own history mid-session
- Push: inject context from cursor-mirror analysis back into Cursor prompts

Model refs: dotcursor-schemas.yml (mcp_cache, mcp_tool_schema), services.yml, features.yml (maxMcpTools: 100)

Complexity: High. Requires MCP server implementation. cursor-db-mcp already does this partially.

### R4. Context Optimization Engine

We have context assembly data (fileSelections, folderSelections, codebase_search
results, cursorRules, mentions). We know the token limit (30000). Build:
- Analyze what context is gathered for each message
- Measure: token usage, file coverage, redundancy
- Score: are the right files being included? Is context stale?
- Suggest: .cursorrules improvements, file selection strategies
- Compare across sessions: what context patterns lead to better outcomes

Model refs: features.yml (fullContextTokenLimit: 30000, maxRuleLength: 100000), tools.yml (codebase_search params)

Complexity: High. Needs heuristics for "better outcomes."

### R5. Live Daemon / Watch Mode

Current cursor-mirror is batch (read DB, print, exit). Build:
- `cursor-mirror watch --live` that polls DB for new bubbles
- Streams events as they happen (tool calls, responses, errors)
- Can trigger alerts (dangerous command, secret detected, error rate spike)
- Output as SSE stream for web UI, or plain text for terminal

Model refs: all (continuous reading of cursorDiskKV for new rowids)

Complexity: Medium. Polling is simple; notification system is the hard part.

---

## INCREMENTAL -- Filling gaps with what we already know

### I1. Full Tool Param Validation

We have 29 documented tools with param schemas (tools.yml). We see actual tool calls
in bubbles (toolFormerData.rawArgs, .params). Build:
- Validate actual tool calls against documented schemas
- Detect: unknown tools, missing params, unexpected params
- Report: tool usage drift (is Cursor sending new tool names we haven't documented?)
- This is a Layer 2 test: validate model against Cursor evolution

Model refs: tools.yml (params, documented_limits), entities/tool-param-aliases.yml

Complexity: Low. Just cross-reference tools.yml against observed toolFormerData.

### I2. Cross-Store Timeline

We have three data stores: SQLite bubbles (cursorDiskKV), transcripts (.txt), and
ai-tracking (ai-code-tracking.db). They share composer IDs and timestamps but are
currently queried separately. Build:
- Merged timeline: interleave bubble events, transcript sections, and AI code hashes
- Single composer view that shows: message -> tool call -> file edit -> git commit
- Correlate: which model produced which code, verified by ai-tracking hashes

Model refs: dotcursor-schemas.yml (all three stores), keys/cursor-disk-kv.yml

Complexity: Medium. Timestamp alignment across stores is the main challenge.

### I3. Agent Transcript Deep Parser

We have the transcript format documented (dotcursor-schemas.yml tool_patterns).
The existing tgrep/agent-transcript commands do basic line parsing. Build:
- Proper state-machine parser: user, assistant, thinking, tool_call, tool_result
- Structured output: list of typed sections with line ranges
- Token estimation per section (approximate from char count)
- Diffable: compare two transcripts structurally

Model refs: dotcursor-schemas.yml (agent_transcript_txt, role_markers, tool_patterns)

Complexity: Low-Medium. The format is documented; just needs a clean parser in lib.

### I4. Model Migration Tracker

We have model migration history (models.yml migrations). Build:
- Detect current model config from reactive storage
- Compare against known migrations
- Alert when a new model appears that's not in our registry
- Track which models are actually used per session (from bubbles)

Model refs: models.yml (migrations, internal_usage), features.yml (server_config)

Complexity: Low. Mostly cross-referencing existing data.

### I5. Feature Flag Monitor

We have 32+ feature flags documented (features.yml). Build:
- `cursor-mirror features --diff` that compares current flags vs model
- Detect: new flags (Cursor added), removed flags, changed values
- History: track flag changes over time (store snapshots)
- This feeds Layer 2 testing: detect Cursor internal API evolution

Model refs: features.yml (feature_flags, feature_config, server_config)

Complexity: Low. Read from DB, compare to model YAML.

### I6. Recovery / Migration Toolkit

We assimilated 3 recovery tools (cursorrecovery, cursor-chat-recovery, cursor-chat-recovery-kit).
They all solve: "renamed folder -> lost chat history." Build:
- `cursor-mirror recover --old-name X --new-name Y`
- Uses workspace discovery + workspace.json to find orphaned chats
- Backup before restore (we know the paths)
- Export orphaned chats before migration

Model refs: paths.yml (workspace_db, workspace_json, recovery_backup_paths), discovery.yml

Complexity: Low-Medium. The logic is documented in 3 assimilated sources.

### I8. Transcript as I/O Format -- Edit, Replay, Share

Investigation of Cursor's transcript system (Feb 2026):

**What Cursor offers natively:**
- `cursor.com/s/{shareId}` -- public read-only link (anyone can view, no sign-in)
- `cursor.com/dashboard?tab=shared-chats&shareId=...` -- team-only link
- `cursor://fork-shared-chat/{shareId}` -- deeplink: forks shared chat into Cursor
- Export: creates .md file (but currently buggy -- producing summaries, not full transcripts since Jan 2026)
- Local: `~/.cursor/projects/<ws>/agent-transcripts/<uuid>.txt` is the real-time full transcript
- Share uploads conversation to Cursor's servers (encrypted at rest, secret auto-redaction)
- Fork creates a copy; original unchanged

**What this enables for cursor-mirror:**

1. **Export with editing** -- `cursor-mirror export-transcript @1 --editable`
   - Export full conversation as structured format (YAML or JSON, not just .txt/.md)
   - User edits: delete boring sections, fix mistakes, add annotations
   - Re-import: `cursor-mirror import-transcript edited.yml --as-new`
   - Creates a new composer with the edited conversation (write to cursorDiskKV)
   - This is the first WRITE operation for cursor-mirror (currently read-only)

2. **Selective knowledge extraction** -- `cursor-mirror extract @1 --topics "deployment, config"`
   - Pull just the useful parts from a long session
   - Output: standalone document with context preserved
   - Feed into another chat as context

3. **Prompt replay** -- `cursor-mirror replay @1 --prompts-only`
   - Extract just the user prompts from a session
   - Replay them against a different model or context
   - Compare outputs (regression testing for prompts)

4. **Share link integration**
   - `cursor-mirror share @1` -- trigger share via cursor:// deeplink
   - `cursor-mirror fetch cursor.com/s/abc123` -- download a shared transcript
   - `cursor-mirror diff @1 cursor.com/s/abc123` -- compare local vs shared
   - Privacy audit: what's in the shared version vs local (secret redaction check)

5. **Web transcript editor** (future)
   - Load transcript into a web page for visual editing
   - Delete sections, reorder, annotate
   - Export back as importable format
   - cursor:// deeplink to load result into Cursor

**Security considerations:**
- Write operations need explicit confirmation and --force flag
- Backup before any import/modification
- Secret scan before any share/export
- Currently Cursor share is buggy (Jan-Feb 2026); track status

**What we need in the model:**
- Shared transcript URL format and API (if any)
- Export .md format specification (currently undocumented)
- cursor:// deeplink protocol documentation
- Write access to cursorDiskKV (composerData, bubbleId) -- currently read-only

Model refs: dotcursor-schemas.yml (agent_transcript_txt), features.yml (privacy), services.yml

Complexity: Medium-High (read/extract/share: Medium; write-back/replay: High)

### I7. MCP Server Behavior Analysis

We see MCP tool calls in bubbles (cursor-ide-browser, puppeteer-nessus, etc.).
We have mcp-cache.json and tool schemas. Build:
- Per-MCP-server usage report: which tools called, how often, errors
- Schema validation: do actual calls match the tool's JSON Schema?
- Anomaly detection: unusual MCP activity patterns
- This is valuable for skill-snitch: MCP servers are an attack surface

Model refs: tools.yml (mcp section), dotcursor-schemas.yml (mcp_cache, mcp_tool_schema, mcp_status)

Complexity: Medium.

---

## NIT-PICKING -- Polish, correctness, edge cases

### N1. Bubble Text Extraction Edge Cases

extract_bubble_text handles the main cases but misses:
- codeBlocks with relativePath (should show file context)
- toolFormerData with nested JSON in result (common for grep/read_file)
- selections and fileSelections in user bubbles (context they added)
- Multiple toolFormerData entries in a single bubble

Model refs: entities/bubble.yml (68 fields), algorithms/extract-bubble-text.yml

### N2. Timestamp Normalization

Some timestamps are ISO strings, some are unix ms, some are unix seconds.
format_ts handles the main cases but should also handle:
- Unix seconds (not ms) -- divide by 1000 threshold
- None / empty / 0 values consistently
- Timezone awareness (currently assumes local)

### N3. Workspace Folder Resolution Robustness

get_workspace_folder returns None for some workspaces. Could:
- Fall back to checking the DB for a stored folder path
- Parse the hash to check if it matches a known project
- Handle multi-root workspaces (workspace.json with multiple folders)

### N4. Output Format Consistency

Some commands use output_data(), some print directly. Standardize:
- All commands should respect --output-format
- JSON output should always be valid JSON (no mixed text+json)
- CSV should handle nested structures consistently

### N5. Error Messages and Exit Codes

Some commands silently produce empty output on bad input. Should:
- Consistent exit code 1 for "not found"
- Helpful error messages: "Composer @5 not found; you have 3 composers"
- Suggest alternatives: "Did you mean moollm? (found in workspace w3)"

### N6. Config Consistency

CONFIG is loaded but not consistently used. Some limits are hardcoded.
Should use CONFIG["limits"]["default"] everywhere.

---

## INTEGRATION OPPORTUNITIES -- Combining systems

### X1. Shell Auditor + Skill Snitch
R1 (shell commands) feeds R2 (skill behavior). A skill that runs `curl | bash` gets
both a shell danger score AND a permission violation from skill-snitch.

### X2. Context Engine + Feature Flags
R4 (context optimization) uses I5 (feature flags) to know actual limits.
If fullContextTokenLimit changes, the context engine adapts.

### X3. Cross-Store Timeline + Live Daemon
I2 (merged timeline) powers R5 (live daemon). The daemon streams merged events.

### X4. Recovery + Discovery
I6 (recovery) uses existing discovery.py. It's almost there; just needs
the merge/rename logic from the assimilated recovery tools.

### X5. Tool Validation + Model Tracker
I1 (tool param validation) combined with I4 (model tracker) detects:
new tools appearing in a new Cursor version, tools being deprecated, param changes.
This is the Layer 2 test suite: "has Cursor's internal API changed?"

---

## PRIORITY RECOMMENDATION

### Do now (before Phase 4-5):
1. **I1: Tool param validation** -- low effort, high signal, feeds Layer 2 tests
2. **I5: Feature flag monitor** -- low effort, immediate value, detects Cursor changes
3. **N1-N5: Nit-picks** -- clean up during Phase 4-5 anyway

### Do next sprint:
4. **I3: Transcript deep parser** -- unlocks R1 (shell auditor), R2 (skill snitch), AND I8 (transcript I/O)
5. **R1: Shell command auditor** -- the most immediately useful new system
6. **I8: Transcript I/O (read path)** -- export structured, extract, prompt replay (no writes yet)
7. **I6: Recovery toolkit** -- low effort with 3 assimilated sources

### Do when ready:
8. **R2: Skill snitch v2** -- needs I3 and R1 first
9. **I2: Cross-store timeline** -- needs I3 first
10. **I8: Transcript I/O (write path)** -- import edited transcripts back into Cursor
11. **R3: Cursor UI bridge** -- high value but high complexity
12. **R4: Context optimization** -- needs real usage data and heuristics

### Key dependency chain:
I3 (parser) -> R1 (shell audit) -> R2 (skill snitch)
I3 (parser) -> I8 read (export/extract/replay) -> I8 write (import/edit/fork)
I1 + I4 + I5 -> Layer 2 test suite (detect Cursor API evolution)
I2 (cross-store) -> R5 (live daemon)

---

## MODEL GAPS TO FILL

Things we know exist but haven't fully documented in the universal model:

1. **Bubble.supportedTools** -- per-bubble tool allowlist (from ORCHESTRATION); not in entities/bubble.yml
2. **Bubble context fields** -- fileSelections, folderSelections, selections, terminalSelections,
   selectedImages, cursorRules, mentions (17 context source types); partially in bubble.yml
3. **agentKv schema** -- we catalog it as key patterns but don't document the value schema per tool
4. **messageRequestContext** -- the full assembled context blob; schema not in model
5. **Checkpoint schema** -- checkpointId values; file snapshots; not documented
6. **codeBlockDiff schema** -- diff tracking per code block; not documented
7. **composer.content** -- SHA-hashed content blobs; not documented
8. **inlineDiffUndoRedo** -- undo/redo state; not documented
9. **Shared transcript API** -- cursor.com/s/{shareId} fetch format; is there a JSON API?
10. **Export .md format** -- what Cursor's export produces; currently buggy (summaries not full since Jan 2026)
11. **cursor:// deeplink protocol** -- fork-shared-chat documented; what other deeplinks exist?
12. **cursorDiskKV write schema** -- exact format for creating/importing conversations
