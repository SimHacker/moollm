# `mechanisms/` — One directory per plugin

Each subdirectory **`schemas/mechanisms/<registry-id>/`** holds the canonical profile **`MECHANISM.yml`**, a **README.md** (pedia entry), and optionally **`SCHEMAPEDIA-<REGISTRY-ID-UPPER>-AUGMENT.yml`** — big-endian filename: extended links, standards-body rows, cross-cutting problem-space narrative, and YAML Jazz improvisation (see **[../plugin-convention.yml](../plugin-convention.yml)** `schemapedia_augment`). **`moollm_hooks.augment`** in `MECHANISM.yml` points at the augment file. The registry id and directory name match (kebab-case). Copy **[../templates/MECHANISM.yml](../templates/MECHANISM.yml)** when adding a new plugin.

Profiles may be **standalone** (specs + hooks only) or **ensemble** (they `delegate` to MOOLLM skills). See [`../plugin-convention.yml`](../plugin-convention.yml).

Optional **`mechanism_relations`** lists how this mechanism **relates to other registered mechanisms**: `target`, `kind`, **`protocol`**, optional **`gateway_ref`** (id in [`../gateways.yml`](../gateways.yml)), optional **`parameters`**. That is the per-plugin view of composition; **`gateways.yml`** remains the canonical bridge list.

**Peer mechanisms** are not nested: e.g. many pipelines reference **json-schema** without owning it; shared bridges live in **`gateways.yml`** and may be mirrored in each side’s **`mechanism_relations`**.

**Convention:** `plugin_profile.kind` is `standalone` or `ensemble`; `deeper_skills` lists skill ids; optional `cli_tools` lists `{ name, role }` for terminal tooling.

---

## Index of mechanisms

| Path | Registry id | Family | Ensemble → skills | One-line purpose |
|------|---------------|--------|-------------------|------------------|
| [cursor-mirror/MECHANISM.yml](./cursor-mirror/MECHANISM.yml) | `cursor-mirror` | introspection | [`cursor-mirror`](../../../cursor-mirror/) | Cursor SQLite stores + YAML data model (`CURSOR-SQLITE-MODEL`, `DATA-SCHEMAS`, …); `cursor_mirror.py`. |
| [com-xpcom/MECHANISM.yml](./com-xpcom/MECHANISM.yml) | `com-xpcom` | component_interop | — (standalone) | Microsoft COM; Mozilla XPCOM; decomification / decomtamination—see [README](./com-xpcom/README.md). |
| [drescher/MECHANISM.yml](./drescher/MECHANISM.yml) | `drescher` | causal | [`schema-mechanism`](../../../schema-mechanism/), [`schema-factory`](../../../schema-factory/) | Drescher Context → Action → Result; causal learning, not wire validation. |
| [git/MECHANISM.yml](./git/MECHANISM.yml) | `git` | vcs | — (standalone) | Distributed VCS: DAG, objects, hooks, diffs; repo timeline and provenance. |
| [github/MECHANISM.yml](./github/MECHANISM.yml) | `github` | collaboration | [`moocroworld`](../../../moocroworld/), [`moo`](../../../moo/) | Forge + branch-as-object / Issue_<id> / moorls (theory moocroworld, CLI moo). |
| [json-schema/MECHANISM.yml](./json-schema/MECHANISM.yml) | `json-schema` | interchange | — (standalone) | JSON Schema — wire validation, OpenAPI, tool IO. |
| [k-lines/MECHANISM.yml](./k-lines/MECHANISM.yml) | `k-lines` | activation | [`k-lines`](../../../k-lines/) | Protocol symbols / K-lines; PROTOCOLS/INDEX. |
| [mechanism/MECHANISM.yml](./mechanism/MECHANISM.yml) | `mechanism` | registry_meta | [`schema`](../../../SKILL.md) | Meta: schemapedia plugin shape—MECHANISM.yml, augment, templates, relations. |
| [minsky-frame/MECHANISM.yml](./minsky-frame/MECHANISM.yml) | `minsky-frame` | situational | [`knowledge-frames`](../../../knowledge-frames/) | Minsky frames — slots and defaults for situations. |
| [relax-ng/MECHANISM.yml](./relax-ng/MECHANISM.yml) | `relax-ng` | interchange | — (standalone) | RELAX NG for XML; compact/XML syntax. |
| [shell-orchestration/MECHANISM.yml](./shell-orchestration/MECHANISM.yml) | `shell-orchestration` | execution | [`sister-script`](../../../sister-script/), [`plan-then-execute`](../../../plan-then-execute/), [`mooco`](../../../mooco/), [`runtime`](../../../runtime/) | Doc-first automation, gated plans, orchestrator, dual runtime; pairs with **cursor-mirror** for post-run inspection. |
| [society-of-mind/MECHANISM.yml](./society-of-mind/MECHANISM.yml) | `society-of-mind` | meta_model | [`society-of-mind`](../../../society-of-mind/) | SoM architecture skill — not a file format. |
| [sql/MECHANISM.yml](./sql/MECHANISM.yml) | `sql` | relational | — (standalone) | ANSI SQL DDL/DML family; dialect notes. |
| [sqlite/MECHANISM.yml](./sqlite/MECHANISM.yml) | `sqlite` | relational | — (standalone) | Embedded DB, `sqlite_master`, migrations, JSON1. |
| [xml-schema/MECHANISM.yml](./xml-schema/MECHANISM.yml) | `xml-schema` | interchange | — (standalone) | W3C XSD. |
| [yaml-jazz/MECHANISM.yml](./yaml-jazz/MECHANISM.yml) | `yaml-jazz` | notation | [`yaml-jazz`](../../../yaml-jazz/) | Semantic YAML — comments as data; complements JSON Schema. |
| [zod/MECHANISM.yml](./zod/MECHANISM.yml) | `zod` | interchange | — (standalone) | Zod — TypeScript-first runtime schemas. |

---

## Families represented here

```
interchange   → json-schema, zod, relax-ng, xml-schema
causal        → drescher
situational   → minsky-frame
activation    → k-lines
relational    → sql, sqlite
meta_model    → society-of-mind
registry_meta → mechanism
notation      → yaml-jazz
execution     → shell-orchestration
introspection → cursor-mirror
vcs           → git
collaboration → github
component_interop → com-xpcom
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

- [`../README.md`](../README.md) — `schemas/` directory overview (root vs `mechanisms/`).
- [`../registry.yml`](../registry.yml) — authoritative mechanism list and ids.
