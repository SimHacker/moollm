# cursor-mirror.py Refactoring Plan

Deep review and refactoring plan for the cursor-mirror Python script. **No code changes in this document** — plan only. Goals: organized, focused modules; sniffable top-level CLI; reusable library; clean mapping from universal model (and reverse-engineered sources) to Python; alignment with MOOLLM philosophies (yaml-jazz, extensibility, sniffable Python).

---

## 1. Current State

### 1.1 Single-file layout

- **Path:** `skills/cursor-mirror/scripts/cursor_mirror.py`
- **Size:** ~9,883 lines (~400k characters)
- **Structure:**
  - **Lines 1–803:** Sniffable region — docstring, path constants, `main()` (argparse: 47+ commands, subparsers, `set_defaults(func=cmd_*)`).
  - **Lines 807–821:** Exceptions (`CursorMirrorError`, `NotFoundError`, `DatabaseError`, `ValidationError`).
  - **Lines 839–1023:** Audit framework — `Severity`, `MatchType`, `AuditPattern`, `Finding`, `AuditSurface` (Transcript, Sqlite, Config), `AuditRunner`; YAML pattern loading; file-in-use / Cursor-running checks; masking.
  - **Lines 1025–1180:** Audit helpers (`is_file_in_use`, `check_cursor_running`, `mask_preserving_whitespace`, `load_patterns_from_yaml`).
  - **Lines 1181–1513:** Finding dataclass; surface implementations (transcript, SQLite, config).
  - **Lines 1514–1718:** `AuditRunner` (scan, report).
  - **Lines 1719–1809:** Debug and sources-mode (register_source, print_sources).
  - **Lines 1810–2110:** Output format (get_output_format, output_data, text/json/yaml/csv/md).
  - **Lines 2112–2183:** `cli()` wrapper and config loading.
  - **Lines 2185–2655:** Core library — `open_db`, `decode_blob`, `resolve_workspace`, `resolve_composer`, `get_workspace_folder`, `get_workspace_composers`, `iter_bubbles`, `load_bubbles`, `get_bubble_text`, `has_content`, `format_ts`, `get_bubble_counts`, `get_all_composers`, cache clear, `iter_workspace_paths`, `get_workspace_index`, `get_composer_index`.
  - **Lines 2658–~5450:** Command implementations (`cmd_list_workspaces`, `cmd_show_workspace`, … ~47 `cmd_*`).
  - **Lines 5451+:** Global ItemTable helpers (`get_item_table_value`, composer_state, status commands pulling config/features/MCP from global DB), then more cmd_* and entrypoint.

### 1.2 Hardcoded vs model

- **Paths:** `GLOBAL_DB`, `WORKSPACES_ROOT` are literal macOS paths; universal model has `paths.yml` (darwin/win32/linux, recovery_backup_paths, vscdb_note).
- **Keys:** `composer.composerData`, `allComposers`, `bubbleId:*`, `composerData:*`, ItemTable/cursorDiskKV — in code as string literals; universal model has `keys/workspace-itemtable.yml`, `keys/cursor-disk-kv.yml`, and SQL files.
- **Bubble extraction:** `get_bubble_text`, tool/thinking handling scattered in cmd_*; universal model has `algorithms/extract-bubble-text.yml` and `entities/bubble.yml`, `entities/tool-result-parse.yml`.
- **SQL:** Queries inlined in `get_workspace_composers`, `iter_bubbles`, `get_bubble_counts`, status commands; universal model has `sql/*.sql` (list-sessions-workspace, full-session, list-composers-global, count-bubbles, composer-state, agent-kv-for-composer, etc.).

### 1.3 What works well

- Single entrypoint and rich docstring (sniffable “read this first”).
- Clear `main()` → `args.func(args)` dispatch.
- Public `__all__` and library-style functions (resolve_*, get_*, load_bubbles, open_db) usable by other tools.
- Audit framework is already abstract (surfaces × patterns).
- `--sources` and output formats (text/json/yaml/csv/md) are reusable concepts.

### 1.4 Pain points

- **Monolith:** One file is too large for LLM or human “sniff” of implementation; hard to navigate and test in isolation.
- **No model sync:** Paths, keys, and SQL are not loaded from reference YAML/SQL; changing the universal model does not automatically affect the script.
- **Mixed concerns:** CLI parsing, DB access, resolution, formatting, audit, and 47 commands live in one namespace.
- **Reuse barrier:** Building another tool (e.g. export-only, or MCP server) would require copying or importing the whole file.
- **Testing:** No natural unit boundaries; mocking and fixtures are harder.

---

## 2. Goals

1. **Sniffable Python:** Top-level CLI file is short and readable; docstring + `main()` (+ maybe a small command registry) tell the full story; implementation lives in modules.
2. **Reusable, composable library:** Other tools can import `lib.paths`, `lib.db`, `lib.bubbles`, `lib.resolve` without pulling in CLI or audit.
3. **Single source of truth:** Paths, keys, and SQL align with `reference/universal/model/` (and thus with reverse-engineered KEY-CATALOG, DATA-SCHEMAS, etc.); where possible, load from YAML/SQL or generate code from them.
4. **Clear model ↔ code mapping:** Each universal-model concept (paths, tables, keys, entities, algorithms, sql) maps to a known Python module or module section, so we can keep code in sync with “uni mod” and assimilated sources.
5. **MOOLLM alignment:** yaml-jazz (comments and structure as data; three audiences); extensibility (new commands or surfaces without touching core); directory-as-advertisement (package layout is discoverable); robust-first (graceful degradation, no silent wrong behavior).

---

## 3. Universal Model → Python Mapping

| Universal model (reference/universal/model/) | Python artifact | Notes |
|---------------------------------------------|------------------|--------|
| **meta.yml** | Package version / schema version; optional validation | Read once at startup or from a single `model_meta` module. |
| **paths.yml** | `paths` module | Base dirs, global_db, workspace_storage, workspace_db pattern, cursor_agent, recovery_backup_paths. Platform (darwin/win32/linux) from `sys.platform`. |
| **tables.yml** | `db` or `tables` module | ItemTable, cursorDiskKV schema and “where” semantics; table names as constants. |
| **keys/workspace-itemtable.yml** | `keys` module or `keys/workspace_itemtable.py` | session_list_priority keys, prompts, generations. |
| **keys/global-itemtable.yml** | Same | composer_state_key, notable keys. |
| **keys/cursor-disk-kv.yml** | Same | key_pattern, entries (bubbleId, agentKv, composerData, …). |
| **entities/bubble.yml** | `entities/bubble.py` or `bubbles` module | type 1/2, core_fields; used by extract_bubble_text and bubble iteration. |
| **entities/composer-meta.yml** | `entities/composer_meta.py` or `composers` module | Fields and storage (session_list vs composerData:id). |
| **entities/tool-result-parse.yml** | `entities/tool_result_parse.py` or inside `bubbles` | By-tool result extraction, is_error. |
| **entities/tool-param-aliases.yml** | Optional | Param name normalization for display (can stay YAML, read when needed). |
| **algorithms/extract-bubble-text.yml** | `algorithms/extract_bubble_text.py` or `bubbles.extract_text` | Priority: assistant (toolFormerData → text+codeBlocks → thinking → …), user; is_error. |
| **sql/*.sql** | `sql` module or loaded queries | list_sessions_workspace, full_session, list_composers_global, count_bubbles, composer_state, agent_kv_for_composer, table_check_cursor_disk_kv, search_keys_prefix, list_itemtable_keys. Either load .sql files from reference or embed as named strings from same source. |
| **discovery.yml** | `discovery` module | list_workspaces, project_name_from_uri, folder_to_path; used by resolve and workspace iteration. |
| **legacy-vs-new.yml** | `legacy` or inside `keys` | Which keys are legacy vs new; migration note. |
| **tools.yml, models.yml, features.yml, …** | Optional readers | Status commands can load these for display; not required for core DB/bubble flow. |

Reverse-engineered sources (KEY-CATALOG, DATA-SCHEMAS, storage/*) remain the human/LLM docs; the universal model is the normalized schema. Python should prefer the universal model paths/keys/sql; where a key or query is only in KEY-CATALOG or DATA-SCHEMAS, the Python code can still reference that in comments or a small “sources” list in the module.

---

## 4. Proposed Directory Layout

**Decision: package = `lib/`, relative imports internally.**

Why not `cursor_mirror/`? The script is `cursor_mirror.py` — same name causes import
shadowing when both are on sys.path. `lib/` is scoped to the skill directory; relative
imports inside make the package self-contained. The script uses a 3-line sys.path preamble.

**Decision: no `entities/` or `algorithms/` subpackages in Phase 1.**

Bubble type enum, extract_bubble_text, and tool_result_parse are small (< 50 lines each).
They live in `bubbles.py` until Phase 4 (model-driven loading) gives reason to split.

**Decision: `format_util.py` not `format.py`.**

`format` is a Python builtin; naming a module `format.py` invites confusion.

```
skills/cursor-mirror/
  scripts/
    cursor_mirror.py          # Sniffable CLI: docstring, sys.path preamble, argparse, dispatch
    cursor_mirror_old.py      # Frozen reference copy of pre-refactor monolith
  lib/                        # Internal package; relative imports; not pip-installable (yet)
    __init__.py               # Re-exports (from .paths, .db, etc.)
    exceptions.py             # CursorMirrorError, NotFoundError, DatabaseError, ValidationError
    paths.py                  # Platform paths from model paths.yml (or default)
    db.py                     # open_db, decode_blob, get_item_table_value; table names
    keys.py                   # Session list keys, cursor_disk_kv patterns, global ItemTable keys
    sql.py                    # Named queries (from reference/universal/model/sql/*.sql or embed)
    discovery.py              # iter_workspace_paths, get_workspace_folder, folder_uri_to_path
    resolve.py                # resolve_workspace, resolve_composer, resolve_composer_id
    composers.py              # get_workspace_composers, get_all_composers, get_bubble_counts, caches
    bubbles.py                # iter_bubbles, load_bubbles, get_bubble_text, has_content, extract_bubble_text
    format_util.py            # format_ts, output_data, get_output_format, format_not_supported
    audit/
      __init__.py
      patterns.py             # AuditPattern, MatchType, Severity, load_patterns_from_yaml
      surfaces.py             # AuditSurface, TranscriptSurface, SqliteSurface, ConfigSurface
      runner.py               # AuditRunner, Finding
      utils.py                # is_file_in_use, check_cursor_running, mask_preserving_whitespace
    commands/                 # Command implementations (each cmd_* → one module or grouped)
      __init__.py
      workspaces.py           # cmd_list_workspaces, cmd_show_workspace
      composers_cmd.py        # cmd_list_composers, cmd_show_composer, cmd_tree
      messages.py             # cmd_tail, cmd_stream, cmd_transcript, cmd_watch
      search.py               # cmd_grep, cmd_analyze, cmd_timeline
      tools_cmd.py            # cmd_tools, cmd_tool_result, cmd_thinking, cmd_mcp, ...
      context_cmd.py          # cmd_context, cmd_context_sources, cmd_request_context, ...
      files_todos.py          # cmd_files, cmd_todos
      images.py               # cmd_images, cmd_image_path, cmd_image_info, cmd_image_gallery
      export.py               # cmd_export_chat, cmd_export_prompts, cmd_models, cmd_stats, cmd_info
      status_cmd.py           # cmd_status, cmd_status_config, cmd_status_mcp, ...
      db_cmd.py               # cmd_sql, cmd_dbs, cmd_tables, cmd_keys, cmd_find, cmd_which
      audit_cmd.py            # cmd_secrets, cmd_deep_snitch, cmd_full_audit
    config.py                 # load_config, limits, resolution
    sources.py                # register_source, print_sources, SOURCES_MODE
    debug_util.py             # debug(), set_debug(), log
  reference/                  # Unchanged: universal model, assimilated, reverse-engineered
  designs/
    CURSOR-MIRROR-PY-REFACTORING-PLAN.md  # This file
```

**Script preamble** (scripts/cursor_mirror.py):
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.paths import GLOBAL_DB, WORKSPACES_ROOT
from lib.commands.workspaces import cmd_list_workspaces
```

Phase 4 may later split `bubbles.py` into `entities/` and `algorithms/` subpackages
when model-driven YAML loading warrants separate files.

---

## 5. Module Responsibilities and Model Ref

| Module | Responsibility | Universal model ref |
|--------|----------------|---------------------|
| **meta** | Version, schema version; optionally load meta.yml | meta.yml |
| **paths** | Platform-specific base dirs, global_db, workspace_storage, workspace_db pattern; recovery paths | paths.yml |
| **db** | Open SQLite read-only, decode_blob, get_item_table_value( key, db_path? ); table name constants | tables.yml, keys (which table per key) |
| **keys** | Session list key list, cursor_disk_kv key patterns (bubbleId, composerData, agentKv), global ItemTable keys | keys/workspace-itemtable.yml, keys/global-itemtable.yml, keys/cursor-disk-kv.yml |
| **sql** | Named queries: list_sessions_workspace, full_session, list_composers_global, count_bubbles, composer_state, agent_kv_for_composer, table_check_cursor_disk_kv, etc. | sql/*.sql |
| **discovery** | iter_workspace_paths (from paths), get_workspace_folder (workspace.json), folder_uri_to_path | discovery.yml, paths.yml |
| **resolve** | resolve_workspace(ref), resolve_composer(ref, workspace_ref?), resolve_composer_id; uses discovery + composers + bubble_counts | discovery.yml, keys (session list), composers/bubbles |
| **composers** | get_workspace_composers(ws_path), get_all_composers(), get_bubble_counts(); caches; uses db + keys + sql | keys/workspace-itemtable, sql/list_sessions_workspace (concept), cursor_disk_kv for counts |
| **bubbles** | iter_bubbles(composer_id), load_bubbles(composer_id), get_bubble_text(obj), has_content(obj); extract_bubble_text(bubble) per algorithm | entities/bubble.yml, algorithms/extract-bubble-text.yml, entities/tool-result-parse.yml |
| **bubbles** (includes entity + algo) | Bubble type enum, extract_bubble_text priority, tool_result_parse by tool name, is_error | entities/bubble.yml, algorithms/extract-bubble-text.yml, entities/tool-result-parse.yml |
| **format_util** | format_ts, get_output_format(args), output_data(data, fmt, …), format_not_supported | — |
| **audit/** | Patterns, surfaces, runner, utils (file-in-use, Cursor running, mask) | — (security/audit; can later drive from YAML patterns in reference) |
| **commands/** | Each cmd_* implementation; call into lib (resolve, composers, bubbles, db, format, audit) | Per-command use of model (e.g. status_* use features, models, keys) |
| **config** | load_config(), limits, resolution min_hash_prefix | — |
| **sources** | register_source, print_sources, _data_sources, SOURCES_MODE | — |
| **exceptions** | CursorMirrorError, NotFoundError, DatabaseError, ValidationError | — |

---

## 6. Sniffable CLI (scripts/cursor_mirror.py)

Target: **one short file** (on the order of 200–400 lines) that:

1. Keeps the **full docstring** (quick start, reference syntax, gotchas, security caveat, what’s where, 47 commands, reference shortcuts, context assembly, library usage).
2. Declares **path constants** only as re-exports from `lib.paths` (e.g. `from lib.paths import GLOBAL_DB, WORKSPACES_ROOT`) so the docstring and “what’s where” stay accurate but the real source is paths.yml-driven.
3. Builds **argparse** in `main()` and registers subparsers; each subparser’s `set_defaults(func=...)` points to a function in `lib.commands.*` (e.g. `from lib.commands.workspaces import cmd_list_workspaces`).
4. After parsing: apply global flags (debug, sources), then call `args.func(args)`.
5. **No** DB logic, no resolution logic, no bubble logic in this file — only CLI wiring and dispatch.
6. **Entrypoint:** `if __name__ == "__main__": sys.exit(cli())` with `cli()` in lib (or in script) catching exceptions and returning 0/1/130.

This preserves “read docstring + main() to understand the full CLI” (sniffable Python) while moving all implementation into lib.

---

## 7. Loading Model from YAML/SQL (Extensibility and YAML-Jazz)

- **paths:** Either (a) ship default paths in code derived from paths.yml at build time, or (b) at runtime load `reference/universal/model/paths.yml` (and select darwin/win32/linux). Option (b) keeps code in sync with the model with one read at startup.
- **keys:** Same idea: load workspace_itemtable and cursor_disk_kv key lists/patterns from `reference/universal/model/keys/*.yml` so that new keys or priority order changes don’t require code edits.
- **sql:** Either (a) embed query strings in Python with a comment “# from reference/universal/model/sql/list-sessions-workspace.sql”, or (b) load .sql files from the reference dir. Option (b) gives a single source of truth and fits yaml-jazz “structure and files as data.”
- **extract_bubble_text:** Priority rules can live in YAML and be interpreted in Python (algorithms/extract-bubble-text.yml), so behavior stays aligned with the documented algorithm.

Prefer loading from reference when the skill is run from the repo (e.g. `MOOLLM_SKILL_ROOT` or relative to `cursor_mirror/__file__`); fallback to built-in defaults when running from a bundle or installed package.

---

## 8. Refactoring Phases (No Code Yet)

**Phase 1 — Extract library core (no CLI split yet)**  
- Add `lib/` (or `cursor_mirror/` package) under the skill.  
- Move exceptions, paths (as constants first), db (open_db, decode_blob), keys (constants from current code), sql (inline named queries), discovery, resolve, composers, bubbles, entities/algorithms into the lib.  
- Keep a single `cursor_mirror.py` that imports from lib and still contains all cmd_* and main().  
- Ensure existing CLI and `__all__` API still work.  
- Add a simple test that resolves a workspace and loads bubbles using the lib.

**Phase 2 — Split commands**  
- Move each `cmd_*` into `lib/commands/*` (grouped by domain: workspaces, composers, messages, search, tools, context, files_todos, images, export, status, db, audit).  
- `main()` only imports and wires subparsers to these command functions.  
- No change to behavior; only file layout.

**Phase 3 — Sniffable CLI**  
- Shrink `scripts/cursor_mirror.py` to docstring + path re-exports + argparse + dispatch.  
- All implementation in lib.  
- Optionally add a small command registry (list of (name, parser, func)) so the script stays minimal.

**Phase 4 — Model-driven config**  
- Introduce loading of paths.yml, keys/*.yml, and optionally sql/*.sql from `reference/universal/model/` (with fallback to built-in defaults).  
- Replace hardcoded key names and query strings with model-backed constants or accessors.  
- Document the mapping in this plan and in module docstrings (yaml-jazz: comments as data).

**Phase 5 — Audit and polish**  
- Move audit framework into `lib/audit/` if not already.  
- Add module-level docstrings that reference the universal model (e.g. “Keys from reference/universal/model/keys/workspace-itemtable.yml”).  
- Optional: add a small `cursor_mirror.model` or `cursor_mirror.ref` that exposes “which YAML/SQL files this package uses” for tools and docs.

---

## 9. MOOLLM Alignment Summary

- **YAML Jazz:** Comments and structure in YAML are first-class; Python reads paths, keys, and optionally SQL from reference so that “why” and “what” live in the model; module docstrings cite model files.
- **Sniffable Python:** Top-level script is short and descriptive; implementation is in focused modules; directory layout is discoverable (directory-as-advertisement).
- **Extensibility:** New commands = new module or new function in an existing command module; new surfaces (audit) = new surface class; new keys = edit YAML and reload (or restart).
- **Robust-first:** Keep read-only DB access; degrade gracefully on missing keys or malformed JSON; no silent wrong behavior (e.g. resolve returns None instead of guessing).
- **Single source of truth:** Universal model (and reverse-engineered docs) are the authority; Python stays in sync via loading or code generation from the same files.

---

## 10. File Count and Line Budget (Rough)

- **scripts/cursor_mirror.py:** ~250–400 lines (docstring + argparse + dispatch).  
- **lib:** ~15–20 modules/packages; core (paths, db, keys, sql, discovery, resolve, composers, bubbles) on the order of 800–1200 lines total; commands split across ~10 files, ~300–600 lines each depending on command; audit ~400–500 lines; format/config/sources/exceptions ~200–300.  
- Total lines should be similar to current (no feature growth in this refactor); navigation and testability improve.

---

## 11. Next Steps

1. Review this plan with the skill owner; adjust module names or phase order if needed.  
2. Create the directory layout (empty `lib/` and subpackages) and add `__init__.py` re-exports.  
3. Execute Phase 1 (extract library core, single script still intact).  
4. Proceed through Phases 2–5, with tests and CLI smoke checks at each step.  
5. Update SKILL.md and CARD.yml to mention the lib and the model ↔ code mapping (and this design doc).

End of plan. No code changes in this document.
