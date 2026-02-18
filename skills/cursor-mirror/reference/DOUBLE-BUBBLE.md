# Double bubble — reverse-engineered full bubble database

**Double bubble** (or **dubble**): a cursor-mirror artifact that merges Cursor’s bubble store (state.vscdb) with agent transcripts to produce a single, queryable index of “complete” bubbles. Two incomplete sources → one merged index. Name: double bubble trouble → **double bubble** / **dubble**.

## Why not transcript-only?

We can’t ignore the partial DB: it has data the transcript doesn’t.

- **Composer catalog**: Names, `createdAt`, `lastUpdatedAt`, subtitle, `contextUsagePercent`, isStarred, composerMode live in workspace ItemTable (`composer.composerData`). Transcripts are one file per composer; you get composer IDs from filenames but not titles or timestamps without the DB.
- **Stable IDs**: Bubble IDs, message indices, and tool call IDs (UUIDs) are in the DB. Needed to correlate with agentKv, Cursor UI, or dedup. Transcript doesn’t expose these.
- **Tool results**: agentKv stores full result blobs (25k+ keys). Transcript has `[Tool result]` blocks but may truncate or omit large output; DB can have the complete result.
- **Context assembly**: messageRequestContext (ide state, current file, todos, diffs, project layouts) and bubble context (selections, file refs, lints) are only in the DB, not in the transcript.
- **Edits and checkpoints**: codeBlockDiff, checkpoints, inline-diff state. Not in transcript.

So: use **transcript as source of truth for tool args and command text** when the DB is missing them; use the **DB for catalog, IDs, context, and full/structured results**. Merge both in the dubble.

## Purpose

- **Bubbles alone**: often missing `rawArgs` and full tool payloads (see [TOOL-ARGS-MISSING.md](TOOL-ARGS-MISSING.md)).
- **Transcript alone**: has full tool args and command text but no structured DB.
- **Double bubble**: one SQLite (or set of SQLites) that holds **metadata only** and **pointers** to where full text lives (transcript path + line or byte range). No copy of message bodies; minimal storage, full queryability.

## Storage

- **Location**: `.moollm/skills/cursor-mirror/dubble/` (or `bubble-db/`). Under the cursor-mirror skill dir so it stays with the tooling; `.moollm` is already transient/local.
- **Format**: separate SQLite DBs per workspace (e.g. `dubble/<workspace-hash>.db`) or one global DB with a `workspace_id` column. Choice depends on how cursor-mirror discovers workspaces vs global state.

## Incremental updates

- Track what’s already indexed: e.g. `(composer_id, last_message_id)` or `state.vscdb` mtime + transcript mtime per composer.
- On each run: only (1) open state.vscdb and list new/changed `bubbleId:<composerId>:*` since last run, (2) for each composer with new bubbles or updated transcript, re-parse that composer’s transcript and merge, (3) write only new/updated rows into the dubble DB.
- Avoid re-scanning full cursorDiskKV every time; use cursor-mirror’s existing workspace/composer discovery and limit reads to changed composers.

## Schema (metadata + pointers only)

- **No full text stored.** Only:
  - Identifiers: `composer_id`, `message_id`, `bubble_id`, `tool_call_id` (when applicable).
  - Metadata: `type` (user/assistant), `created_at`, `tool_name`, `status`, etc.
  - Source: `raw_args_from_db` (JSON string or null when missing), `raw_args_from_transcript` (JSON string or null), or a single merged `raw_args` with a `source` column: `db` | `transcript` | `merged`.
  - **Pointer to chat**: `transcript_path` (absolute or relative to workspace), `transcript_line_start`, `transcript_line_end` (or byte offsets if preferred). Optional: `transcript_byte_start`, `transcript_byte_end` for exact substring.
- Optional tables: `composers` (composer_id, workspace_id, name, created_at, last_updated_at), `tools` (tool_call_id, bubble_id, tool_name, status, raw_args_source, transcript_path, transcript_line_start, transcript_line_end). Keep tables normalised so queries stay simple and space stays small.

## Command (cursor-mirror)

- **Build/update**: e.g. `cursor-mirror dubble build [--workspace PATH]` or `cursor-mirror dubble update`. Build = full rebuild; update = incremental (only new/changed composers and their transcripts).
- **Query**: e.g. `cursor-mirror dubble query "SELECT ..."` or subcommands like `cursor-mirror dubble tools <composer_ref>` that read from the dubble DB and resolve transcript pointers when the user wants full command text.

## Summary

| Term        | Meaning |
|------------|---------|
| **Double bubble** | The reverse-engineered, merged bubble index (bubbles + transcript). |
| **Dubble**        | Short alias for double bubble. |
| **Pointer**       | `transcript_path` + line (or byte) range; no copy of message/tool text. |
| **Incremental**  | Only process new/changed composers and transcripts; avoid full rescan. |

Implementing this in cursor_mirror.py gives a single place to query “all tool calls with full args” and then follow pointers into the transcript when the full text is needed.
