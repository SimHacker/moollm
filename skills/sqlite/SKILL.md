---
name: sqlite
description: Embedded SQLite — sqlite3 CLI, pragmas, JSON1, WAL, migrations; pairs with cursor-mirror; server DBs use postgres.
license: MIT
tier: 1
allowed-tools: [read, grep, glob, run_terminal_cmd]
related: [postgres, schema, cursor-mirror, datasette, robust-first]
tags: [moollm, sqlite, embedded, json1, wal, migrations, datasette]
---

# SQLite

Part of MOOLLM · [skills/sqlite/](https://github.com/SimHacker/moollm/tree/main/skills/sqlite)

**SQLite** is an **embedded** SQL engine: library + file (or `:memory:`). No separate server process. **MOOLLM** uses the **`sqlite`** mechanism in schemapedia for the **engine**; the **`sql`** mechanism names the **SQL language** family shared with Postgres and others.

This skill is the **wrapper** around the **SQLite ecosystem**: the **`sqlite3`** CLI, **C API** and language bindings, **JSON1**, **WAL**, migration runners, and **file format** documentation—not a fork of SQLite. For **read-only web exploration and JSON API** over `.db` files, use the **`datasette`** skill and schemapedia **`datasette`** mechanism (including the **cursor-mirror** export path).

## When to use

- **Local persistence** for tools, agents, tests, and single-user apps.
- **Cursor** session stores (see **cursor-mirror**) — SQLite under the hood.
- **Prototyping** a schema before committing to **PostgreSQL** for multi-user production.

Use **`postgres`** when you need **server-side** roles, **connection pooling**, **Timescale**, **pgvector**, or **HA** patterns.

## CLI: sqlite3

```bash
sqlite3 ./app.db
```

Useful interactive commands:

- `.tables` — list tables
- `.schema [table]` — show DDL
- `.headers on` / `.mode column` — readable output
- `.dump` — SQL text export

**Exit: `CTRL+D` or `.quit`**

## Catalog: sqlite_master

Metadata lives in **`sqlite_master`** (and internal schema tables). Inspect:

```sql
SELECT type, name, tbl_name, sql FROM sqlite_master ORDER BY type, name;
```

## Pragmas that matter

- **`journal_mode`** — **`WAL`** is often right for **read-heavy** concurrent access; understand **locking** (writers still serialize).
- **`foreign_keys`** — `PRAGMA foreign_keys = ON;` for **referential** checks (must be enabled per connection in many drivers).
- **`synchronous`** — durability vs speed tradeoff; **never** weaken without understanding **data loss** risk.
- **`user_version`** — integer **you** own for **migration** versioning.

Official pragma reference: https://www.sqlite.org/pragma.html

## JSON1

**JSON1** adds SQL functions for JSON in columns — `json_extract`, `json_each`, etc.

https://www.sqlite.org/json1.html

## Types: affinity and STRICT

SQLite uses **dynamic typing** with **type affinity**. **STRICT** tables (optional) reject invalid types on insert. Read: https://www.sqlite.org/stricttables.html

## Migrations

- **Ordered SQL files** applied by a runner, or **ORM** migrations (Drizzle, Prisma, Alembic, …).
- Track **`user_version`** or use a **schema_migrations** table — pick one convention per project.
- **sqldiff** (when installed) can compare databases — https://www.sqlite.org/sqldiff.html

## Full-text search (FTS5)

**FTS5** is SQLite’s **full-text** engine for **search** indexes — separate virtual tables from ordinary rows.

https://www.sqlite.org/fts5.html

## Interop with PostgreSQL

| Concern | SQLite | PostgreSQL |
|---------|--------|------------|
| Concurrency | Single writer; WAL helps readers | MVCC; server tuning |
| Extensions | JSON1, FTS5 built-in | Timescale, pgvector, … |
| Deploy | Single file | Host + roles + backups |

**Porting** often requires **type** and **locking** semantics review — not a mechanical rename.

## Datasette (HTTP layer on the same `.db` files)

**[Datasette](../datasette/SKILL.md)** publishes SQLite files as a **read-only** web UI and **JSON API** using the **`datasette`** CLI, optional **metadata YAML**, and **`--crossdb`** for multiple databases. It does not replace **`sqlite3`** for DDL or bulk writes. MOOLLM wires **cursor-mirror** to Datasette via **`export_datasette`** and **`reference/universal/datasette-metadata.yml`** — see the **datasette** skill for the full integration protocol.

## cursor-mirror

**Cursor** stores **SQLite** databases locally. The **cursor-mirror** skill documents **table shapes** and **YAML** models — see **`schemas/mechanisms/cursor-mirror`** in the registry.

## Related skills

- **`postgres`** — server **Postgres** operations and extensions.
- **`schema`** — schemapedia **`sqlite`** mechanism profile.
- **`cursor-mirror`** — introspection over **Cursor** SQLite data.

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/sqlite/](https://github.com/SimHacker/moollm/tree/main/skills/sqlite)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
