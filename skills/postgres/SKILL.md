---
name: postgres
description: Server PostgreSQL operations — connect, migrate, Timescale, pgvector, introspection; delegates deep tuning to postgres-optimization.
license: MIT
tier: 1
allowed-tools: [read, grep, glob, run_terminal_cmd]
related: [postgres-optimization, sqlite, schema, robust-first, plan-then-execute]
benefits_from: [postgres-optimization]
tags: [moollm, postgres, sql, timescale, pgvector, migrations, psql]
---

# PostgreSQL

Part of MOOLLM · [skills/postgres/](https://github.com/SimHacker/moollm/tree/main/skills/postgres)

Treat this skill as the **MOOLLM wrapper** around **PostgreSQL’s full stack**: the **`psql`** client, **`pg_dump` / `pg_restore`**, connection libraries, **extension packages**, and the **on-disk / managed-server** ecosystem—not a reimplementation of the engine. The **`postgres`** schemapedia mechanism points here; **`sql`** remains the abstract **language** family.

This skill covers **operating** PostgreSQL: getting connected, **migrations**, **extensions** (including **TimescaleDB** and **pgvector**), catalog introspection, and operational vocabulary. **Index design, constraint tricks, and deep `EXPLAIN` work** live in **`postgres-optimization`** — use this skill first for wiring and safety, then delegate when the problem is plan-level.

## When to use

- New service or container needs a **repeatable** way to apply DDL.
- Choosing **extensions**: time-series (Timescale), embeddings (**pgvector**), query stats (**pg_stat_statements**), text (**pg_trgm**, **citext**).
- Debugging **connection** issues (URI vs env vars, SSL, roles).
- **Not** the first stop for “this one query is slow” — use **`postgres-optimization`** after you have a query and schema.

## Connection: URI and environment

**Single URI** (typical in apps):

```text
postgresql://user:password@host:5432/dbname?sslmode=require
```

`psql` accepts a URI:

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -c "
SELECT current_database(), current_user, version();
"
```

If tooling uses **`PG_CONNECTION_STRING`** instead of **`DATABASE_URL`**, normalize in shell:

```bash
psql "${DATABASE_URL:-$PG_CONNECTION_STRING}" -v ON_ERROR_STOP=1 -f ./migrations/001_apply.sql
```

**Split variables** (classic DBA style): `PGHOST`, `PGPORT`, `PGUSER`, `PGDATABASE`, `PGPASSWORD`. `psql` picks these up when no URI is passed.

## Safe DDL and scripts

- **`-v ON_ERROR_STOP=1`** — stop the script on first error (essential for migrations).
- **Transactions** — wrap multi-statement deploys when appropriate; know that some DDL takes stronger locks.
- **Idempotent** patterns — `CREATE TABLE IF NOT EXISTS`, `CREATE EXTENSION IF NOT EXISTS` — avoid blind rewrites in production without review.

## Migrations (practice)

- **Single source of truth** — one ordered apply path, or a migration tool (Flyway, Sqitch, Alembic, Liquibase, ORM) with explicit version table.
- **Roles and grants** — separate “superuser bootstrap” from application DDL where possible.
- **Rollback story** — forward-only migrations are common; document how to recover (restore from backup, or compensating migration).

## Introspection (starter queries)

**Version and extensions:**

```sql
SELECT version();
SELECT extname, extversion FROM pg_extension ORDER BY 1;
```

**Table sizes (rough):**

```sql
SELECT relname, pg_total_relation_size(oid) AS bytes
FROM pg_class
WHERE relkind = 'r' AND relnamespace = 'public'::regnamespace
ORDER BY bytes DESC
LIMIT 20;
```

**Load `pg_stat_statements`** (if installed) and read the **PostgreSQL docs** for setup — then inspect top queries by total time.

## TimescaleDB (time-series)

Timescale extends **PostgreSQL** with **hypertables** (time-partitioned tables), **compression**, **retention policies**, and **continuous aggregates** (rollup views). **Read the product docs** before turning this on in production: chunk intervals, retention, and compression interact with query patterns.

Canonical entry points:

- https://docs.timescale.com/
- Hypertables: https://docs.timescale.com/use-timescale/latest/hypertables/
- Continuous aggregates: https://docs.timescale.com/use-timescale/latest/continuous-aggregates/

Typical enable: `CREATE EXTENSION IF NOT EXISTS timescaledb;` then `create_hypertable(...)` per **current** API in your Timescale version.

## pgvector (embeddings)

**pgvector** stores **vectors** in-table and supports **nearest-neighbor** search with distance operators. Install the extension package for your **Postgres major**, then:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Details and operator list: **https://github.com/pgvector/pgvector**

## Extension catalog

See **[EXTENSIONS.md](EXTENSIONS.md)** for a **link table** (Timescale, pgvector, `pg_stat_statements`, `pg_trgm`, PostGIS, and core manual links).

## Backup and restore vocabulary

- **Logical dump**: `pg_dump` / `pg_restore` — portable, version-sensitive.
- **Base backups**: file-system level + WAL archiving — **streaming replication** and **PITR** territory; follow your platform’s runbook.
- Do **not** paste real credentials into chat logs; use env vars and secret stores.

## Relationship to other skills

| Skill | Role |
|-------|------|
| **postgres-optimization** | Unconventional and advanced **performance** (indexes, `EXPLAIN`, plans). |
| **sqlite** | Embedded **file** database — when to stay local vs move to Postgres. |
| **schema** | Schemapedia **registry** — **`sql`** language family, **`postgres`** mechanism. |

## Related skills

- **`postgres-optimization`** — use when this skill’s connection and ops context is not enough and the bottleneck is **query or index** design.
- **`sqlite`** — compare **embedded** vs **server** tradeoffs.
- **`schema`** — mechanism **`postgres`** in the registry points here.

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/postgres/](https://github.com/SimHacker/moollm/tree/main/skills/postgres)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
