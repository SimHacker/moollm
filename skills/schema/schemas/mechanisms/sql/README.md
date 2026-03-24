# SQL (relational) (schemapedia: `sql`)

**Relational family.** **DDL/DML** as usually meant: `CREATE TABLE`, constraints, views, migrations—**portable SQL** is a subset; every engine extends types and DDL ([sqlite](../sqlite/README.md), Postgres, MySQL, …).

## Why it matters here

The schemapedia names **SQL** separately from [sqlite](../sqlite/README.md): SQL is the **language family**; SQLite is one embedded engine with its own affinity rules and extensions. API bodies validated with [json-schema](../json-schema/README.md) still need an explicit **row/table** contract—see [`../../gateways.yml`](../../gateways.yml).

## What’s distinctive

- **ISO/IEC 9075** defines the core standard; vendors diverge on JSON types, upsert, etc.
- **Migrations** are the practical “schema evolution” story—tooling (Flyway, Sqitch, ORMs) is part of real projects.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [sqlite](../sqlite/README.md) | SQLite speaks SQL; not identical to “ANSI SQL in the large.” |
| [json-schema](../json-schema/README.md) | HTTP body schema ≠ `CREATE TABLE`—bridge at app boundary. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Standard | [ISO/IEC 9075](https://www.iso.org/standard/76583.html) (paid; summaries abound) |
| Overview | [Wikipedia: SQL](https://en.wikipedia.org/wiki/SQL) |
| Tooling | `psql`, `mysql` clients—see [`MECHANISM.yml`](./MECHANISM.yml) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Gateways: [`../../gateways.yml`](../../gateways.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
