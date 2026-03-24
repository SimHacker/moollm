# `mechanisms/` — Per-plugin profiles

Each file here is **one schemapedia mechanism plugin**: a single YAML profile that **registers** under an id in [`../registry.yml`](../registry.yml). Profiles may be **standalone** (specs + hooks only) or **ensemble** (they `delegate` to MOOLLM skills). See [`../plugin-convention.yml`](../plugin-convention.yml).

**Convention:** `plugin_profile.kind` is `standalone` or `ensemble`; `deeper_skills` lists skill ids; optional `cli_tools` lists `{ name, role }` for terminal tooling.

---

## Index of mechanism profiles

| File | Registry id | Family | Ensemble → skills | One-line purpose |
|------|-------------|--------|-------------------|------------------|
| [cursor-mirror.yml](./cursor-mirror.yml) | `cursor-mirror` | introspection | [`cursor-mirror`](../../../cursor-mirror/) | Cursor SQLite stores + YAML data model (`CURSOR-SQLITE-MODEL`, `DATA-SCHEMAS`, …); `cursor_mirror.py`. |
| [drescher.yml](./drescher.yml) | `drescher` | causal | [`schema-mechanism`](../../../schema-mechanism/), [`schema-factory`](../../../schema-factory/) | Drescher Context → Action → Result; causal learning, not wire validation. |
| [k-lines.yml](./k-lines.yml) | `k-lines` | activation | [`k-lines`](../../../k-lines/) | Protocol symbols / K-lines; PROTOCOLS/INDEX. |
| [minsky-frames.yml](./minsky-frames.yml) | `minsky-frame` | situational | [`knowledge-frames`](../../../knowledge-frames/) | Minsky frames — slots and defaults for situations. |
| [relax-ng.yml](./relax-ng.yml) | `relax-ng` | interchange | — (standalone) | RELAX NG for XML; compact/XML syntax. |
| [shell-orchestration.yml](./shell-orchestration.yml) | `shell-orchestration` | execution | [`sister-script`](../../../sister-script/), [`plan-then-execute`](../../../plan-then-execute/), [`mooco`](../../../mooco/), [`runtime`](../../../runtime/) | Doc-first automation, gated plans, orchestrator, dual runtime; pairs with **cursor-mirror** for post-run inspection. |
| [society-of-mind.yml](./society-of-mind.yml) | `society-of-mind` | meta_model | [`society-of-mind`](../../../society-of-mind/) | SoM architecture skill — not a file format. |
| [sql.yml](./sql.yml) | `sql` | relational | — (standalone) | ANSI SQL DDL/DML family; dialect notes. |
| [sqlite.yml](./sqlite.yml) | `sqlite` | relational | — (standalone) | Embedded DB, `sqlite_master`, migrations, JSON1. |
| [xml-schema.yml](./xml-schema.yml) | `xml-schema` | interchange | — (standalone) | W3C XSD. |
| [yaml-jazz.yml](./yaml-jazz.yml) | `yaml-jazz` | notation | [`yaml-jazz`](../../../yaml-jazz/) | Semantic YAML — comments as data; complements JSON Schema. |

> **Note:** `minsky-frame` in the registry points to profile path `schemas/mechanisms/minsky-frames.yml` — the file name is **`minsky-frames.yml`** (plural).

---

## Families represented here

```
interchange   → relax-ng, xml-schema
causal        → drescher
situational   → minsky-frames
activation    → k-lines
relational    → sql, sqlite
meta_model    → society-of-mind
notation      → yaml-jazz
execution     → shell-orchestration
introspection → cursor-mirror
```

---

## Notable cross-links

| Topic | Where |
|-------|--------|
| Gateway **shell → cursor-mirror** | [`../gateways.yml`](../gateways.yml) (`shell-then-mirror`) |
| Gateway **cursor-mirror → sqlite** | [`../gateways.yml`](../gateways.yml) (`cursor-mirror-to-sqlite`) |
| Gateway **JSON Schema ↔ YAML Jazz** | [`../gateways.yml`](../gateways.yml) (complementary) |
| Full schemapedia protocol | [`../../SKILL.md`](../../SKILL.md) |
| Parent skill README | [`../../README.md`](../../README.md) |

---

## Cursor-mirror data model (pointers inside the skill)

The **cursor-mirror** profile references documentation under the skill repo, for example:

- [`../../../cursor-mirror/reference/universal/CURSOR-SQLITE-MODEL.yml`](../../../cursor-mirror/reference/universal/CURSOR-SQLITE-MODEL.yml)
- [`../../../cursor-mirror/reference/reverse-engineered/DATA-SCHEMAS.yml`](../../../cursor-mirror/reference/reverse-engineered/DATA-SCHEMAS.yml)
- [`../../../cursor-mirror/reference/reverse-engineered/DOTCURSOR-SCHEMAS.yml`](../../../cursor-mirror/reference/reverse-engineered/DOTCURSOR-SCHEMAS.yml)
- [`../../../cursor-mirror/reference/universal/model/dotcursor-schemas.yml`](../../../cursor-mirror/reference/universal/model/dotcursor-schemas.yml)

---

## Related

- [`../README.md`](../README.md) — `schemas/` directory overview.
- [`../registry.yml`](../registry.yml) — authoritative mechanism list and ids.
