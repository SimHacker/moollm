# PostgreSQL extensions — curated links

Use `CREATE EXTENSION IF NOT EXISTS name;` (requires appropriate privileges). Match extension **package** versions to your **PostgreSQL major** and OS images.

## Time-series (TimescaleDB)

| Topic | URL |
|-------|-----|
| Documentation hub | https://docs.timescale.com/ |
| Hypertables | https://docs.timescale.com/use-timescale/latest/hypertables/ |
| Continuous aggregates | https://docs.timescale.com/use-timescale/latest/continuous-aggregates/ |
| Compression | https://docs.timescale.com/use-timescale/latest/compression/ |
| Data retention | https://docs.timescale.com/use-timescale/latest/data-retention/ |
| GitHub (engine) | https://github.com/timescale/timescaledb |

## Vectors (pgvector)

| Topic | URL |
|-------|-----|
| Repository and build | https://github.com/pgvector/pgvector |
| PGXN | https://pgxn.org/dist/vector/ |

Enable: `CREATE EXTENSION vector;` — then `vector(n)` columns and distance operators (`<->`, `<#>`, `<=>` per docs).

## Observability and text (common in production)

| Extension | Role | URL |
|-----------|------|-----|
| **pg_stat_statements** | Top SQL by time and calls | https://www.postgresql.org/docs/current/pgstatstatements.html |
| **pg_trgm** | Trigram similarity and `LIKE` acceleration | https://www.postgresql.org/docs/current/pgtrgm.html |
| **citext** | Case-insensitive text type | https://www.postgresql.org/docs/current/citext.html |

## Crypto and IDs

| Extension | Role | URL |
|-----------|------|-----|
| **pgcrypto** | Digests, `gen_random_uuid()` | https://www.postgresql.org/docs/current/pgcrypto.html |
| **uuid-ossp** | UUID functions | https://www.postgresql.org/docs/current/uuid-ossp.html |

## Federation and search helpers

| Extension | Role | URL |
|-----------|------|-----|
| **postgres_fdw** | Query remote Postgres | https://www.postgresql.org/docs/current/postgres-fdw.html |
| **unaccent** | Accent-insensitive search | https://www.postgresql.org/docs/current/unaccent.html |

## Geo (distinct from vectors)

| Extension | Role | URL |
|-----------|------|-----|
| **PostGIS** | Geometry and geography | https://postgis.net/documentation/ |

## Core docs

| Topic | URL |
|-------|-----|
| PostgreSQL manual (current) | https://www.postgresql.org/docs/current/ |
| SQL commands index | https://www.postgresql.org/docs/current/sql.html |
