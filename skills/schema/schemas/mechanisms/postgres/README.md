# PostgreSQL (schemapedia: `postgres`)

**Relational family.** **Server** PostgreSQL — **extensions** (`CREATE EXTENSION`), **roles**, **MVCC**, **`psql`**, backups. **Not** the same as the **`sql`** mechanism (language family) or **`sqlite`** (embedded engine).

## Delegates to

| Skill | Role |
|-------|------|
| **[postgres](../../../../postgres/README.md)** | Operations, migrations, Timescale, pgvector, introspection |
| **postgres-optimization** | Advanced index and query tuning |

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [sql](../sql/README.md) | Abstract **SQL** dialect; **postgres** is one engine. |
| [sqlite](../sqlite/README.md) | **Embedded** vs **server** — see **`skills/sqlite`** and **`skills/postgres`**. |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Augment: [`SCHEMAPEDIA-POSTGRES-AUGMENT.yml`](./SCHEMAPEDIA-POSTGRES-AUGMENT.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
