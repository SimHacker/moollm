# Datasette (schemapedia: `datasette`)

**Relational family (tooling).** **Datasette** publishes **SQLite** files as a read-only **web** app and **JSON API**. It is **not** a separate storage engine: it **specializes** the **`sqlite`** mechanism for **HTTP**, **metadata YAML**, and **plugins**.

## Delegates to

| Skill | Role |
|-------|------|
| **[datasette](../../../../datasette/README.md)** | CLI, metadata, crossdb, **cursor-mirror** export path |

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [sqlite](../sqlite/README.md) | Same **`.db`** path—no second published file; **sqlite3** for writes; Datasette for read-only HTTP/API (“zero copy” in the no-duplicate-file sense; see **`gateways.yml`** `sqlite-to-datasette`). |
| [cursor-mirror](../cursor-mirror/README.md) | **`export_datasette`** + **`datasette-metadata.yml`** — see **`skills/datasette/SKILL.md`**. |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Augment: [`SCHEMAPEDIA-DATASETTE-AUGMENT.yml`](./SCHEMAPEDIA-DATASETTE-AUGMENT.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
