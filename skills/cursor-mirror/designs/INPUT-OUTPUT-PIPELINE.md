# Full import/export pipeline (vision)

Once we **completely understand** Cursor's SQLite and state layout (tables, keys, schemas, semantics), we can treat the Cursor database as a **first-class input/output** artifact: read it, transform it (including with LLMs), then write it back. Full import/export.

---

## Prerequisites

- **Complete model** -- Universal model (Stage 2) plus validation (Stage 3) so every table, key, and value type is documented and verified.
- **Cursor quit** -- Cursor must be **closed** during read/write so the DB is not locked and we avoid corruption. The pipeline assumes exclusive access to `state.vscdb` (global and/or workspace).

---

## Pipeline shape

1. **Quit Cursor** -- User or script ensures the Cursor app is not running.
2. **Read** -- Load full state: global `state.vscdb` (ItemTable + cursorDiskKV), optionally workspace DBs. Parse into canonical in-memory representation (same schema as format entourage: keys, entities, blobs).
3. **Transform** -- Apply edits: filter, redact, merge, rewrite bubbles, summarize, translate, or run LLM passes over conversations (e.g. summarize all chats, extract todos, anonymize, migrate format). Input and output stay in the same logical schema so round-trip is well-defined.
4. **Write** -- Serialize back to SQLite: update or overwrite `state.vscdb` (and workspace DBs if applicable). Preserve WAL/shm semantics if required; optionally backup before write.
5. **Reopen Cursor** -- User starts Cursor again; it sees the updated DB.

This is an **input/output pipeline**: Cursor DB ↔ canonical format ↔ transforms (deterministic or LLM) ↔ Cursor DB.

---

## Use cases

- **Export** -- Dump full state to YAML/JSON/CSV for backup, analysis, or migration to another machine.
- **Import** -- Restore from a backup or merge in state from another Cursor instance.
- **Bulk edit** -- Redact sensitive data, rename workspaces, delete old sessions, normalize bubble format.
- **LLM passes** -- Summarize conversations, extract structured data, translate, or rewrite content; write results back into bubbles or new keys.
- **Migration** -- When Cursor changes schema, read old DB, transform to new schema, write new DB (with a one-off or versioned transform).

---

## Risks and caveats

- **Cursor reserves the right to change format** (Forum caveat). A transform that works today may break after an update; the universal model and validation tests help detect drift.
- **Integrity** -- Writing a bad value can break Cursor or lose data. Validate before write; backup; consider a dry-run or diff mode before actual write.
- **Auth and sensitive keys** -- ItemTable holds tokens and secrets. Transform steps must handle them carefully (redact, never log, optional strip on export).

---

## Relation to current work

- **Format entourage** -- Load/validate/process/eval/**apply** already describes "emit to format"; apply today is to our own exports (chunk dir, JSON, CSV). The full pipeline extends apply to **Cursor's live SQLite** as the output target, with Cursor quit.
- **Assimilation** -- Understanding is the bottleneck. Stage 1--3 and the universal model are the foundation; once stable, the read/transform/write pipeline is the next step.
- **Validation** -- Before any write-back, validate the transformed payload against the universal model and run structure/drift tests so we never write invalid state.

---

## Implementation order (later)

1. Complete universal model and validation (Stage 2--3).
2. **Read path** -- Tool that dumps global (and optional workspace) state.vscdb to canonical YAML/JSON/chunk dir; schema-safe.
3. **Transform API** -- Script or library: load dump -> apply transform (plugin or LLM) -> produce in-memory state; no write yet.
4. **Write path** -- Tool that takes canonical state and writes to state.vscdb (Cursor quit, backup, then write). Start with a single table or key namespace to de-risk.
5. **Orchestration** -- Single command or workflow: quit Cursor -> read -> transform -> write -> (user reopens Cursor). Optional: integrate with skill-test or cursor-mirror as a guarded, explicit command.

This doc is the **vision**; implementation follows once understanding is complete and we are ready to own the full I/O loop.
