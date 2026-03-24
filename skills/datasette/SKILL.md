---
name: datasette
description: Datasette — serve SQLite over HTTP with metadata YAML, JSON API, plugins; MOOLLM path from cursor-mirror export.
license: MIT
tier: 1
allowed-tools: [read, grep, glob, run_terminal_cmd]
related: [sqlite, cursor-mirror, schema]
tags: [moollm, datasette, sqlite, http, json-api]
---

# Datasette

Part of MOOLLM · [skills/datasette/](https://github.com/SimHacker/moollm/tree/main/skills/datasette)

**Datasette** ([datasette.io](https://datasette.io/)) is the **CLI and runtime** for publishing **SQLite** files as a **read-only** web application and **JSON API**. It sits on top of the same **`.db` file format** as the **`sqlite`** engine: this skill is the **tooling and ecosystem** layer (serve, metadata, plugins, CORS), not a second database engine.

**sqlite → datasette:** you pass the **same path** as `sqlite3 my.db`. Datasette does **not** build a second on-disk database for serving—**read-only HTTP** over that file. That is the usual sense of **“zero copy” live publishing** here: no duplicate `.db` artifact; refreshes see **committed** data from other writers when the file uses a normal **WAL** setup. For a static snapshot, serve a copy or use **`--immutable`** on a file you do not change.

## What you get

- **`datasette`** — local web server; table browse, filters, **Custom SQL**, export links.
- **Metadata YAML** — per-database titles, **facets**, **sortable columns**, **canned queries** (named SQL with optional `:parameters`).
- **`--crossdb`** — attach multiple SQLite files; run SQL that references more than one database (see Datasette docs for exact SQL shape).
- **Plugins** — ecosystem extends CSV export, maps, full-text helpers, etc. ([Plugin directory](https://datasette.io/plugins)).
- **JSON API** — append `.json` to many URLs for programmatic use ([JSON API](https://docs.datasette.io/en/stable/json_api.html)).

Official documentation: **https://docs.datasette.io/**

## Install

Use **pip** / **pipx** / your OS package manager per current Datasette docs. You need the `datasette` command on `PATH`.

## Basic serve

```bash
datasette mydata.db
```

Opens a local port (default in docs) with table list and row browsing.

## Metadata

Point at a YAML file with **`-m` / `--metadata`**. It can define `title`, `description`, per-**`databases`**, per-**`tables`** (facets, labels), and **`queries`** (canned SQL surfaced in the UI).

## cursor-mirror integration

MOOLLM’s **cursor-mirror** skill ships a **consolidated export** and a **large metadata file** tuned for introspection:

| Artifact | Role |
|----------|------|
| **`lib/datasette_export.py`** → **`export_datasette(output_path)`** | Builds a single **`cursor-mirror.db`** with tables such as `composers`, `transcript_sections`, `shell_commands`, `tool_calls`, `usage_events`, `feature_flags` (see module docstring). |
| **`reference/universal/datasette-metadata.yml`** | Datasette metadata: **canned queries** (tool usage, shell audit, cost, timelines), **facets**, **cross-database** layout for **`cursor-mirror`** + **`cursor-model`**. |
| **`reference/universal/TIME-INDEXED-TABLES.md`** | Notes on **time columns** for bucketing and correlating with other SQLite DBs in the same Datasette process. |

**Typical flow**

1. From the **cursor-mirror** skill directory (or with `PYTHONPATH` set so `lib` imports resolve), run Python to call **`export_datasette(Path("cursor-mirror.db"))`** (see **`datasette_export.py`** for parameters and defaults).
2. Ensure **`cursor-model.db`** exists if you want the **universal model** side (same metadata file names both databases).
3. Serve with **cross-database** and metadata:

```bash
datasette cursor-mirror.db cursor-model.db --crossdb \
  -m reference/universal/datasette-metadata.yml \
  --cors -p 8001
```

Adjust paths to your checkout. Extra SQLite files (e.g. other Cursor history DBs) can be **additional** positional arguments; they appear as separate databases and can be joined in **Custom SQL** when timestamps align (see **`TIME-INDEXED-TABLES.md`**).

**Security:** Datasette is powerful; do **not** expose it on untrusted networks without authentication and threat modeling. Treat exported DBs as **sensitive** (chat content, tool history, shell commands).

## Relationship to other skills

| Skill | Role |
|-------|------|
| **sqlite** | Engine and **`.db`** file semantics; **`sqlite3`** CLI for direct SQL. |
| **cursor-mirror** | Source data and **export**; mirror CLI and YAML model docs. |
| **schema** | Schemapedia **`datasette`** mechanism points here. |

## Related skills

- **`sqlite`** — file format, pragmas, JSON1 when you edit the DB outside Datasette.
- **`cursor-mirror`** — full introspection protocol and mirror commands.

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/datasette/](https://github.com/SimHacker/moollm/tree/main/skills/datasette)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
