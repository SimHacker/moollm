---
name: schema
description: Schemapedia — schema plugins, families, gateways, optional mechanism_relations (protocols to peers); delegates to sibling skills.
allowed-tools: [read, grep, glob]
---

# Schema (schemapedia)

**“Schema”** is overloaded. This skill is the **single index** for MOOLLM: **families** of mechanisms (interchange, notation, causal, situational, activation, relational, execution, **introspection**, meta-model), **nomenclature**, **spec and skill pointers**, optional **CLI affordances** per plugin, and **gateways** between senses. It **registers** `cursor-mirror` with the **Cursor SQLite + YAML data model** (`CURSOR-SQLITE-MODEL.yml`, `DATA-SCHEMAS.yml`, …) alongside JSON Schema, SQLite, and shell orchestration.

## Part of MOOLLM

See [skills/README.md](../README.md) and the repo [README](../../README.md). For narrative and the **schemapedia** metaphor, see [README.md](./README.md).

## Families (what the registry sorts)

| Family | What it covers | Delegates to (examples) |
|--------|----------------|-------------------------|
| **interchange** | Wire/instance shapes and validators | JSON Schema, Zod, RELAX NG, XSD profiles |
| **notation** | Authoring YAML with semantic comments (YAML Jazz) | `yaml-jazz` skill — **schema plugin** in this registry |
| **causal** | Drescher Context → Action → Result | `schema-mechanism`, `schema-factory` |
| **situational** | Minsky frames (slots, defaults) | `knowledge-frames` |
| **activation** | K-lines / protocol symbols | `k-lines`, `PROTOCOLS.yml` |
| **relational** | Tables, constraints, dialects | `sql`, `sqlite` mechanism profiles |
| **execution** | Shell + sister scripts + orchestration (bash-shaped automation) | `shell-orchestration` → `sister-script`, `plan-then-execute`, `mooco`, `runtime` |
| **introspection** | Cursor session DB + reverse-engineered model | **`cursor-mirror`** → `cursor-mirror` skill + `reference/universal/CURSOR-SQLITE-MODEL.yml` et al. |
| **meta_model** | Society of Mind (agents, architecture) | `society-of-mind` |

Deep theory stays in those skills; **registry.yml** holds stable ids, one-line summaries, and `delegate_skills` where applicable.

## Interchange vs notation vs causal vs relational

- **Interchange** — bytes on the wire or in config files; good for APIs and tool I/O. **JSON** carries a parsed tree only—**no comment channel**—so it cannot hold YAML Jazz’s semantic layer.
- **Notation** — **YAML Jazz** is a **registered schema plugin** (`yaml-jazz` in `registry.yml`): same YAML tree as interchange for the data, plus **Comment Oriented Programming (COP)**—comments as instance-specific code and data (constraints, transforms to maintain, procedural intent) that travel with the file—parallel lenses, doc-by-example. YAML text can round-trip commentary only with **comment-preserving** YAML tooling (implementations differ). Pair with JSON Schema when you need both **validated shape** and **authored meaning**; see **`mechanism_relations`** on `yaml-jazz` ↔ `json-schema` and **`gateways.yml`** `json-schema-with-yaml-jazz`.
- **Causal** — what the agent learned fires when; good for **schema-factory** pipelines.
- **Relational** — durable shape in a database engine; **SQLite** is a strong fit for embedded apps, tests, and single-file deploys. Support here means **documentation and gateway patterns**: migrations, `sqlite_master`, JSON1, ORM mapping—not shipping a SQL engine in the skill.

## SQL and SQLite in MOOLLM

**How well we support them:** as **first-class registry entries** with stubs you extend (`schemas/mechanisms/sql/MECHANISM.yml`, `schemas/mechanisms/sqlite/MECHANISM.yml`). Typical integrations:

- **DDL + migrations** as the schema artifact; link to interchange (JSON Schema) at **boundaries** (HTTP body vs row).
- **SQLite** specifically: type affinity, STRICT, `sqlite_master`, pragma `user_version`, JSON1 for hybrid document-in-table.
- **Gateways** in `gateways.yml`: JSON Schema ↔ table design, `sql` ↔ `sqlite` dialect, optional Drescher logs → tables.

**What we do not claim:** one automatic mapping from JSON Schema to correct SQLite DDL for every domain—that remains application design.

## Registry layout

| File | Purpose |
|------|---------|
| [schemas/README.md](schemas/README.md) | Directory tour: root `schemas/*.yml` vs `mechanisms/<id>/`. |
| [schemas/mechanisms/README.md](schemas/mechanisms/README.md) | Index of every mechanism (`MECHANISM.yml` per directory). |
| [templates/MECHANISM.yml](templates/MECHANISM.yml) | Prototype for new mechanism plugins. |
| [schemas/registry.yml](schemas/registry.yml) | Master index: families + mechanisms. |
| [schemas/gateways.yml](schemas/gateways.yml) | Cross-mechanism bridges (including relational). |
| `schemas/mechanisms/<id>/MECHANISM.yml` | Per-mechanism profile; see **Plugin shapes** below. |
| [schemas/plugin-convention.yml](schemas/plugin-convention.yml) | Normative: standalone vs ensemble, `deeper_skills`, optional `cli_tools`. |
| [schemas/drescher-mapping.yml](schemas/drescher-mapping.yml) | Optional Drescher ↔ interchange serialization. |

Add mechanisms by **new directory** `schemas/mechanisms/<id>/` with **`MECHANISM.yml`** + **registry entry** under the right `family`.

## Plugin shapes: one directory, depth optional

A **mechanism plugin** is always **`schemas/mechanisms/<id>/MECHANISM.yml`**. The directory name matches the registry id. What varies is whether that file is **enough on its own** or **indexes deeper work**:

| Shape | Meaning | `deeper_skills` |
|--------|---------|-----------------|
| **Standalone** | Specs, nomenclature, and hooks live in this file; no MOOLLM skill is required for the registry to be useful. | `[]` (empty or omitted) |
| **Ensemble** | The theory is bigger than a single schema-type plugin; this file **points at** one or more MOOLLM skills (single or ensemble) for full depth. | One or more skill ids (same list mirrored as `delegate_skills` on the mechanism in `registry.yml`). |

**Zero deeper skills** — valid: the plugin is self-contained documentation and pointers to external standards only.

**Several deeper skills** — valid: e.g. causal work split across **theory** (`schema-mechanism`) and **tooling** (`schema-factory`); meta-models that need both **knowledge-frames** and **k-lines** for different facets. Order in the list can imply **reading order** when narrative sequence matters.

Normative field names and examples: **`schemas/plugin-convention.yml`**. When you add or remove a depth link, keep **`registry.yml`** `delegate_skills` and **`MECHANISM.yml`** **`deeper_skills`** aligned.

**Mechanism ↔ mechanism:** a peer mechanism is not placed inside another mechanism’s directory (shared mechanisms are referenced by id; many profiles may point at the same bridge). Use **`gateways.yml`** for the canonical list of bridges (`from`, `to`, tools, fidelity). Each **`MECHANISM.yml`** may also declare **`mechanism_relations`** (see **`plugin-convention.yml`**) with: `target` mechanism id, `kind`, **`protocol`** (human-readable contract), optional **`gateway_ref`** (same id as a bridge in `gateways.yml`), and optional **`parameters`** (knobs, boundaries, ordering).

## Mechanism relations (composition protocols)

MOOLLM **skills** are reusable **prototypes** (GLANCE → CARD → SKILL). **Files and directories** in the repo **instantiate** those prototypes in a concrete history (commits, diffs). The **schemapedia registry** plus per-mechanism **`mechanism_relations`** are **declarative composition protocols**: they state how **classes of schema mechanism** may be used together (or with themselves in another role)—which pairs are complementary, which are translation or persistence bridges, and what parameters separate layers (e.g. parsed tree vs source text). That is **meta-level wiring** about schema shapes, not a substitute for validators or for `gateways.yml` as the shared bridge index.

## Plugin checklist

1. Pick **family** and **id** (kebab-case).
2. Copy **[templates/MECHANISM.yml](templates/MECHANISM.yml)** to **`schemas/mechanisms/<id>/MECHANISM.yml`** and edit.
3. Choose **standalone** vs **ensemble**; set **`deeper_skills`** and registry **`delegate_skills`** accordingly.
4. Add **profile** path and **summary** in `registry.yml`.
5. Extend **gateways.yml** when two mechanisms meet in real pipelines; add matching **`mechanism_relations`** rows on each side (with **`gateway_ref`**) when the edge is stable.
6. For relational engines, document **dialect**, **artifacts**, and **migration** tool examples in the profile.
7. Optionally list **`cli_tools`** (name + role) so agents know which CLIs pair with the plugin (`jq`, `sqlite3`, `yq`, …).

## Current plugins (registry mechanisms)

| id | family | Notes |
|----|--------|--------|
| `json-schema`, `zod` | interchange | Wire validation; see `cli_tools` in profiles (e.g. `jq`, `ajv-cli`). |
| `relax-ng`, `xml-schema` | interchange | XML stacks; `xmllint`, `trang`, etc. |
| `drescher` | causal | Ensemble: `schema-mechanism`, `schema-factory`. |
| `minsky-frame` | situational | `knowledge-frames`. |
| `k-lines` | activation | `k-lines` skill. |
| `society-of-mind` | meta_model | `society-of-mind` skill. |
| `sql`, `sqlite` | relational | DDL; `sqlite3`, dialect clients. |
| `yaml-jazz` | notation | Semantic YAML; `yq` when transforming. |
| `shell-orchestration` | execution | **Cursor / terminal agents:** compose docs → commands → scripts; ensemble below. |
| `cursor-mirror` | introspection | **Cursor SQLite + model YAML:** chats, tools, thinking, context; see `schemas/mechanisms/cursor-mirror/MECHANISM.yml`. |

**`shell-orchestration` ensemble (especially useful for Cursor LLMs):** `sister-script` (doc-first automation), `plan-then-execute` (approval gate before destructive shell), `mooco` (orchestrator), `runtime` (Python/JS adventure runtime duality). This is the closest MOOLLM pattern to “compose skills + scripts + **just-in-time** bash”—still **human/agent judgment**, not a compiler.

## CLI affordances

Mechanism profiles may declare **`cli_tools`**: a list of `{ name, role }` for binaries agents should consider (see `plugin-convention.yml`). Examples already on disk: **jq** + JSON Schema, **sqlite3** + SQLite, **yq** + YAML Jazz. Extend per project.

## Related

- `schema-mechanism` — Drescher theory.
- `schema-factory` — lint, ingest, compose Drescher schemas.
- `knowledge-frames` — frames vs Drescher vs interchange vs K-lines.
- `k-lines` — activation bundles.
- `society-of-mind` — Minsky’s architecture skill.
- `yaml-jazz` — semantic YAML; documentation by example; parallel lenses on the same tree.
- `sister-script`, `plan-then-execute`, `mooco`, `runtime` — shell-orchestration ensemble (see `schemas/mechanisms/shell-orchestration/MECHANISM.yml`).
- `cursor-mirror` — **registered plugin** (`cursor-mirror` mechanism); SQLite stores + data model YAML; gateway from `shell-orchestration` for post-run inspection.

## Credits

MOOLLM registry; SQL and SQLite specifications are owned by ISO/ANSI and sqlite.org respectively.

---

## Standard metadata

**License:** MIT

**Tags:** schemapedia, registry, interchange, execution, cli_tools, drescher, frames, k-lines, sql, sqlite, gateways

**Related skills:** schema-mechanism, schema-factory, knowledge-frames, k-lines, society-of-mind, yaml-jazz, sister-script, plan-then-execute, mooco, runtime, cursor-mirror (introspection plugin)
