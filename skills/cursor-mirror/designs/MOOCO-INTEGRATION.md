# MOOCO integration: turbocharging MOOLLM and skills

**MOOCO** (custom orchestrator, `skills/mooco/`) can turbocharge MOOLLM by **directly supporting it** -- skills especially. cursor-mirror and its assimilated knowledge feed into that: precise context management, k-line diffusion, and the advanced orchestration we've designed.

---

## Why MOOCO + cursor-mirror

- **MOOCO** -- Deterministic orchestration, explicit context control, safe tool execution. Hosts MOOLLM skills; tick-based "magic dictionary" kernel; context paging, skill containment, shared core (see MOOCO CARD, designs/raw-chats kernel contract).
- **cursor-mirror** -- Introspection and traceability (MOOCO CARD: related ref). Provides keys, schemas, universal model, bubbles, transcripts. When MOOCO runs skills, it needs to know what context to inject and what state is available.
- **Assimilated data** -- KEY-CATALOG, BORG, S2thend/cursor-history, etc. are the **source of truth** for Cursor's SQLite and transcript shape. That same data can drive MOOCO's context assembly and k-line diffusion so skills get the right slice of state.

---

## Precise context management

- Universal model (chunk dir or single file) can be **loaded by MOOCO's context assembler** and sliced per skill or per turn.
- Keys, SQL snippets, and entity schemas from assimilated sources define **what** is available; MOOCO decides **when** and **how much** to inject (context paging, token budgets).
- cursor-mirror commands (list, show, export, status) can be exposed as **tools** MOOCO offers to skills, so skills can query Cursor state without reimplementing DB access.

---

## K-line diffusion

- **K-lines** in MOOLLM are symbolic activators; key names (composerData, bubbleId, composer.composerData, etc.) are domain K-lines for cursor-mirror.
- MOOCO's registry and mounts (e.g. kernel/mooco WORLD.yml, FUSE-for-LLMs style) can **diffuse** these: directory-as-advertisement, semantic YAML. Skills see "what's here" via the same nomenclature as KEY-CATALOG and BORG.
- Assimilated files document that nomenclature; MOOCO can read them to populate or validate its own skill-facing surface.

---

## Advanced orchestration

- **Tick-based magic dictionary** -- Write a value, tick; something happens; another value changes. cursor-mirror data (e.g. universal model, latest bubble count, cost metrics) can be exposed as MOOCO-readable state so other skills or the orchestrator itself react to Cursor state changes.
- **Skill containment** -- Skills run with explicit context and tool boundaries. cursor-mirror's reference docs (KEY-CATALOG, DATA-SCHEMAS) define the boundary of "Cursor state" that a skill is allowed to see or use when MOOCO gates access.
- **Shared core** -- One canonical model, many formats (format entourage). MOOCO can consume the same chunk dir or JSON export that cursor-mirror produces, so all skills share one representation of Cursor state.

---

## Where it's documented in assimilated files

Assimilated YAMLs can include a **mooco_interpolation** section (see "How each assimilated source feeds MOOCO" below). Example: **S2THEND-CURSOR-HISTORY.yml** -- orchestrator ref, supports_moollm, precise_context, k_line_diffusion, advanced (tick, mounts, design_refs). Add the same pattern to other assimilated files when the source is relevant to context assembly, k-lines, or MOOCO's kernel contract.

---

## Concrete: K-line ↔ MOOCO mount

Assimilated key names and entity names become K-lines MOOCO can advertise. Example mapping (KEY-CATALOG / BORG nomenclature -> what MOOCO exposes in registry or WORLD.yml):

| K-line (source) | MOOCO-facing name | Meaning |
|-----------------|-------------------|--------|
| composer.composerData | cursor_session_list | Workspace session list; try this key first (S2thend priority) |
| bubbleId:{id}:* | cursor_bubbles | Full message list for composer id |
| composerData:{id} | cursor_composer_meta | Name, createdAt, updatedAt, workspaceUri |
| composerState.* (tarq) | cursor_policy | useYoloMode, allowlist, denylist, defaultMode2, mcpAllowedTools |
| cursorAuth/accessToken | (internal only) | Never diffuse; MOOCO uses for API client if skill is allowed |
| workbench.panel.aichat... | cursor_legacy_chat | Fallback session key for older Cursor |

Directory-as-advertisement: a mount like `/pub/cursor/` can list these names (or a small YAML) so skills discover "cursor_session_list", "cursor_bubbles", "cursor_policy" without reading KEY-CATALOG. Nomenclature stays aligned so context assembler and skills share one vocabulary.

---

## Concrete: cursor-mirror as MOOCO tools

MOOCO can expose cursor-mirror commands as tools so skills query Cursor state without touching SQLite. Example mapping:

| cursor_mirror command | MOOCO tool name | What the skill gets |
|-----------------------|-----------------|---------------------|
| list-workspaces | cursor_list_workspaces | Workspace ids, paths, stats (w1, w2, ...) |
| list-composers @1 | cursor_list_composers | Composer ids, names for workspace or @N |
| tail @1 --limit 20 | cursor_tail | Recent messages (user/assistant/tool/thinking) |
| tools @1 --limit 10 | cursor_tool_calls | Recent tool invocations and args |
| status | cursor_status | Health, config, MCP, models |
| export-chat @1 --format json | cursor_export_chat | Full session as JSON (or YAML) |

MOOCO invokes the CLI (or a thin library that shares cursor_mirror logic) and returns stdout/parsed result. Skill containment: only skills that declare `cursor_*` in their allowed tools see these; others get no Cursor state. Same discovery and keys as BORG/S2thend.

---

## Concrete: tick state example

Tick-based magic dictionary: an adapter (or cursor_mirror in "daemon" mode) writes Cursor-derived state each tick; other skills read it.

| Key (in WORLD.yml or magic dict) | Written by | Read by | Meaning |
|-----------------------------------|------------|---------|--------|
| cursor_bubble_count | Adapter (SQL or cursor_mirror) | Skills, MOOCO | Total bubbles in current or selected composer |
| cursor_last_composer_id | Adapter / user selection | Skills | "Current" composer for this run |
| cursor_policy_allowlist | Adapter (tarq key) | Skills that run shell | Allowed commands; MOOCO can enforce before run_terminal |
| cursor_session_list_cached | Adapter | Context assembler | Snapshot of session list; avoid hitting DB every turn |

Write -> tick -> read: e.g. skill asks "how many messages in current chat?"; MOOCO reads cursor_bubble_count from last tick. Or: adapter writes cursor_policy_allowlist on load; skill requests "run npm test"; MOOCO checks allowlist before invoking. Universal model and assimilated sources define where that data comes from (which key, which query).

---

## MOOCO-in-the-middle: Cursor as UI and chat-stream interposition

(MOOCO-in-the-middle rhymes with Malcolm-in-the-Middle. Ayyyyeeeee.)

**Idea:** MOOCO piggybacks on Cursor -- the user's auth, API, tools, MCP, terminal, and **the Composer chat stream** -- so Cursor becomes MOOCO's UI. MOOCO sits in the middle: it **watches** what the user is doing and what Cursor is "thinking" (via cursor-mirror / state.vscdb), and it **acts** through Cursor (via cursor-rpc + same auth). Agents "just know" and can interact with Cursor as their UI via chat.

**Watch:** cursor-mirror (and the universal model) give MOOCO read access to the same state the IDE uses: bubbles, composer state, tool calls, thinking blocks. So MOOCO's skills see the same stream the user sees -- who said what, what tools ran, what Cursor is reasoning.

**Act:** cursor-rpc (everestmz) proves credentials live in state.vscdb; MOOCO can read them and open an RPC client. So MOOCO can call Cursor's API: StreamChat, ClientSideToolV2 (read_file, edit_file, run_terminal, ...). From the user's perspective, Cursor is the UI; from MOOCO's perspective, Cursor is the front-end it drives. One chat stream, one terminal, one editor -- shared.

**Interpose in the chat stream:** The goal is to be a **plug-in interactive outpost** in that stream -- like Facebook apps in the social feed. Third-party logic (MOOCO or a skill) that sees the same context and can **contribute**: inject messages, react to turns, or drive Cursor via RPC so agent replies appear as Cursor's. Possible technical paths: (1) MOOCO in the loop: user message -> MOOCO -> Cursor API (MOOCO can augment, redirect, or reply as "Cursor"); (2) a future Cursor extension or MCP that allows injecting bubbles into the Composer; (3) a MOOCO sidecar UI (separate window or panel) that stays in sync with the same composer context via cursor-mirror. The assimilated EVERESTMZ-CURSOR-RPC and S2thend/BORG/cursor-mirror stack are the foundation: watch from state.vscdb, act from RPC + auth.

**Local model + snitch + protocol trace (play--learn--lift):** In the middle, MOOCO can run a **quick free local model** over what it sees -- same stream (bubbles, thinking, tool calls) as input. No Cursor API cost: summarize, annotate, suggest, or react locally. **Back and forth:** local model output can feed back into the stream (e.g. sidecar annotations, suggested edits) or into MOOCO's own protocol. **Skill-snitch** can virus-scan and analyze the stream: run snitch on each turn or on the live trace -- body and spirit audit of what's flowing through (tool args, prompts, responses). Build up a **protocol trace and summary over time**: persistent record of the session (who said what, what ran, what was thought), plus rolling summaries (per turn, per session). The protocol is **editable each way**: MOOCO can edit the trace (annotate, redact, add meta) and optionally feed edits back (e.g. inject a summary bubble, or gate what goes to Cursor). **Play--learn--lift:** the trace and summary become the material for MOOLLM's loop -- play (explore the stream), learn (extract patterns, detect drift, snitch findings), lift (skillify, document, share). So MOOCO-in-the-middle is not only watch+act; it's also local inference, security audit, and a living protocol that improves from use.

---

## How each assimilated source feeds MOOCO

| Source | What it contributes | MOOCO use |
|--------|---------------------|-----------|
| **S2THEND-CURSOR-HISTORY** | Keys (composer.composerData, bubbleId, composerData), bubble schema, tool param aliases, extractBubbleText | Context assembler vocabulary; k-line names; tool result parsing so MOOCO can present "last tool call" in context |
| **JBDAMASK-CURSOR-DB-MCP** | cursor:// resources, query_table, workspace discovery (folder URI -> project name) | MCP as MOOCO tool layer; list projects / get composer without SQLite; same discovery for cursor_mirror and MOOCO |
| **TARQ-COMPOSER-STATE** | Single ItemTable key, composerState.* (YOLO allowlist/denylist, modes4, defaultMode2) | Policy slice per skill; MOOCO checks allowlist before run_terminal; "current mode" in context |
| **CURSOR-FORUM-STATE-VSCDB** | Official caveat, paths, troubleshooting | Tag context as "reverse-engineered"; robust_first (backup, degrade); path discovery |
| **TENSORZERO-CURSOR-LLM-CLIENT** | System/user prompt shape, citation format, apply-model hierarchy | Context assembly shape (sections, citation format); skills that generate edits know apply-model contract |
| **EVERESTMZ-CURSOR-RPC** | Auth keys, state.vscdb path, ClientSideToolV2/BuiltinTool enums, API base | MOOCO credential slice for skills that may call Cursor API; tool enum mapping; schema extraction for drift detection. **MOOCO-in-the-middle:** act half (RPC + auth); watch half = cursor-mirror/state.vscdb. Enables Cursor-as-UI and chat-stream interposition (see section above). |

Each assimilated file has a **mooco_interpolation** section (reference/assimilated/*.yml). Together they form the contract: what MOOCO can inject, what it can gate, and what K-lines it can diffuse.

---

## Refs

- **MOOCO CARD** -- skills/mooco/CARD.yml (k-lines: CONTEXT-PAGING, SKILL-CONTAINMENT, etc.; related: cursor-mirror).
- **MOOCO design** -- designs/raw-chats (kernel contract, REGISTRY, MAGIC-PORT, FUSE-FOR-LLMS); MOOLLM-MANIFESTO (mooco tier).
- **Assimilation** -- designs/ASSIMILATION-PROCESS.md Stage 1 (mooco_interpolation optional); all reference/assimilated/*.yml (mooco_interpolation present).
