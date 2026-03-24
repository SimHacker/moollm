# SQLite (schemapedia: `sqlite`)

**Relational family.** Embedded **single-file** (or `:memory:`) SQL engine; schema in **`sqlite_master`**; [JSON1](https://www.sqlite.org/json1.html) bridges object-shaped fields and SQL.

## Why it matters here

SQLite is the default **local persistence** for many agents and tools—including **Cursor** session stores surfaced by [cursor-mirror](../cursor-mirror/README.md). The mechanism records **type affinity**, **STRICT** tables, and migration practice so you do not confuse it with “generic SQL” alone ([sql](../sql/README.md)).

## What’s distinctive

- **Serverless**: no separate process; library + file.
- **Pragmas**, **WAL**, **JSON1**: capabilities that matter for JSON-in-SQL and tooling.
- **Porting** to Postgres often touches concurrency and types—plan explicitly.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [cursor-mirror](../cursor-mirror/README.md) | Cursor’s DBs are SQLite; mirror documents tables—[`../../gateways.yml`](../../gateways.yml): `cursor-mirror-to-sqlite`. |
| [json-schema](../json-schema/README.md) | Validate HTTP JSON; persist with DDL—two contracts. |
| [drescher](../drescher/README.md) | Causal logs as tables—project DDL, not automatic from JSON Schema. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Docs | [SQLite](https://www.sqlite.org/) — [SQL syntax](https://www.sqlite.org/lang.html), [schema table](https://www.sqlite.org/schematab.html) |
| Overview | [Wikipedia: SQLite](https://en.wikipedia.org/wiki/SQLite) |
| CLI | `sqlite3` REPL (`.schema`, `.dump`)—[`MECHANISM.yml`](./MECHANISM.yml) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
