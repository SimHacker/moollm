# Why many tool calls have no command/args in cursor-mirror

## What cursor-mirror reads

- **Tool list and args** come only from **bubbles**: `cursorDiskKV` keys `bubbleId:<composerId>:<messageId>`. Each bubble is a JSON blob that may contain `toolFormerData` with `rawArgs` (JSON string of the tool’s request payload).
- **agentKv** keys store tool **results** (blobs), not the request args. So we do not get `command` or other request fields from agentKv.

## What you see

- **`tools <ref> --name run_terminal_cmd`** (or run_terminal_command_v2): often shows 161 rows but **args empty** (`{}`) for most. A small number (e.g. 11) may have args; the rest have no command text in the data cursor-mirror reads from the DB.

## Why args are missing

Cursor (the IDE/backend) decides what to persist in each bubble. Observed behaviour:

1. **Not persisted**: For many tool invocations, the backend either does not write `rawArgs` into the bubble at all, or writes an empty object. So the data is “dropped” or never stored in state.vscdb—we are not losing it in cursor-mirror; it was never in the DB.
2. **Possible reasons** (to infer by experimentation):
   - **Tool-type policy**: e.g. terminal/shell args not stored for privacy or size.
   - **Size or truncation**: Very large payloads might be omitted or replaced with a reference.
   - **Batch/streaming**: Only some bubbles (e.g. first few, or those that triggered a “save”) get full tool payloads.
   - **Version/schema**: Different Cursor versions or session types might persist different fields.
3. **Transcript has it**: The plaintext agent transcript (`~/.cursor/projects/.../agent-transcripts/<composer>.txt`) is written in real time as the conversation runs. It contains `[Tool call] run_terminal_command_v2` and the next indented lines, e.g. `  command: "..."`, `  description: "..."`. So the **full command text is in the transcript**; it is not lost, only not stored in the bubble DB.

## Pattern

- **DB (bubbles)**: often has `toolFormerData.name` and `toolFormerData.status` (and maybe result), but **rawArgs often empty** for run_terminal_* and possibly other tools.
- **Transcript (.txt)**: has tool name and the actual args in the form `  key: value` lines after each `[Tool call]`.

So the pattern is: **Cursor does not persist request args for many tool calls in the bubble store; the canonical source for “everything” is the agent transcript.**

## How to get “everything”

1. **Use the transcript for terminal commands**: Parse the agent-transcript file for that composer: find every `[Tool call] run_terminal_command` (and variants), then read the following indented lines to extract `command:`, `description:`, etc. That gives you the full list of commands regardless of DB.
2. **Implement `terminal-commands` in cursor-mirror**: A command that (a) from DB: list run_terminal_* with timestamp/status/args when present; (b) from transcript: parse the same tool blocks and extract command/description; (c) merge so every invocation has at least transcript-sourced command when DB args are empty. Then “all 161 commands” are available from one place.
3. **Experiment to confirm the rule**: In a fresh short session, run 5–10 terminal commands and immediately run `cursor-mirror tools @1 --name run_terminal`. If rawArgs is still empty, it confirms Cursor is not persisting these args in bubbles; if some have args, compare (e.g. by position, size, or tool variant) to infer when it does persist.

## What we cannot control

- We cannot force Cursor to write `rawArgs` into the bubble blob. Persistence is entirely on the IDE/backend side. Our control is only in cursor-mirror: **treat transcript as source of truth when DB args are missing**, and provide a single command (e.g. terminal-commands) that merges both sources so you get everything.

## Double bubble (reverse-engineered full bubble DB)

A **double bubble** (or **dubble**) is a cursor-mirror artifact: a separate SQLite DB (or DBs) under `.moollm/skills/cursor-mirror/dubble/` that merges bubbles + transcripts into one index. It stores **metadata and pointers only** (e.g. `transcript_path`, `transcript_line_start`/`transcript_line_end`) so full message/tool text is not duplicated—just references into the chat transcript. Incremental updates: only new/changed composers and transcripts are processed each run. Full spec: [DOUBLE-BUBBLE.md](DOUBLE-BUBBLE.md).
