# `schemas/` — Schemapedia data layer

This directory is the **machine- and human-readable data layer** for the MOOLLM **`schema`** skill ([schemapedia](../README.md)). It holds the **registry** of mechanism plugins, **gateways** between mechanisms, **conventions** for how profiles are written, **interchange stubs** at the top level, and **per-mechanism profiles** under [`mechanisms/`](./mechanisms/).

Nothing here is a runtime validator by itself: these files **name**, **cross-link**, and **document** “schema” in every MOOLLM sense (wire formats, Drescher causality, frames, K-lines, SQL, YAML Jazz, shell orchestration, Cursor introspection). Deep theory lives in delegated skills; see each profile’s `delegate` / `deeper_skills`.

---

## Contents at a glance

| File | Role |
|------|------|
| [**registry.yml**](./registry.yml) | **Master index** — registry version, families, all mechanism ids, `profile` paths, `delegate_skills`, one-line summaries. |
| [**plugin-convention.yml**](./plugin-convention.yml) | **Normative rules** — `standalone` vs `ensemble` plugins, `deeper_skills`, optional `cli_tools`. |
| [**gateways.yml**](./gateways.yml) | **Bridges** — JSON↔Zod, XSD↔RNG, JSON↔SQLite, Drescher↔rows, `json-schema`↔`yaml-jazz`, `shell-orchestration`↔`cursor-mirror`, `cursor-mirror`↔`sqlite`, etc. |
| [**json-schema.yml**](./json-schema.yml) | Interchange **JSON Schema** stub — drafts, MOOLLM hooks, `cli_tools` (e.g. jq). |
| [**zod.yml**](./zod.yml) | Interchange **Zod** stub — TS runtime, `cli_tools`. |
| [**drescher-mapping.yml**](./drescher-mapping.yml) | Optional **Drescher ↔ serialized payload** field mapping (not a universal bridge). |
| [**mechanisms/**](./mechanisms/) | **One YAML per plugin** — richer profiles (see [mechanisms/README.md](./mechanisms/README.md)). |

---

## How it fits the parent skill

| Doc | Purpose |
|-----|---------|
| [../SKILL.md](../SKILL.md) | Full protocol: families, plugin shapes, CLI affordances, Cursor notes. |
| [../CARD.yml](../CARD.yml) | File list and interfaces for agents. |
| [../GLANCE.yml](../GLANCE.yml) | Fast orientation. |

---

## Registry (`registry.yml`)

- **Version** is bumped when families or mechanisms change (currently v5: introspection + `cursor-mirror`).
- **`families`** group mechanisms: `interchange`, `causal`, `situational`, `activation`, `relational`, `meta_model`, `notation`, `execution`, `introspection`.
- **`mechanisms.<id>`** points to a **profile** file (either a top-level `.yml` here or under `mechanisms/`).
- **`delegate_skills`** on a mechanism must mirror **`plugin_profile.deeper_skills`** in that profile when the plugin is an **ensemble** (`plugin-convention.yml`).
- **`plugin_convention`** field: path to **`plugin-convention.yml`**.

---

## Gateways (`gateways.yml`)

Cross-mechanism relationships: translation, complementary stacks (e.g. JSON Schema + YAML Jazz), dialect ports, persistence patterns, and **observability** (shell → cursor-mirror). See the file for version and `bridges` list.

---

## Plugin convention (`plugin-convention.yml`)

Defines:

- `standalone` — full value in one profile file; `deeper_skills: []`.
- `ensemble` — profile indexes one or more MOOLLM skills.
- Optional **`cli_tools`**: `{ name, role }` for agents (jq, sqlite3, yq, …).

---

## Top-level interchange stubs

| File | Mechanism id | Notes |
|------|--------------|--------|
| [json-schema.yml](./json-schema.yml) | `json-schema` | Stays at repo root of `schemas/` for short paths in older links. |
| [zod.yml](./zod.yml) | `zod` | Same. |

---

## Subdirectory: `mechanisms/`

All **other** plugin profiles live in **[mechanisms/](mechanisms/)** — a detailed index is in **[mechanisms/README.md](mechanisms/README.md)**.

---

## Related MOOLLM skills (by family)

| Family | Example skills |
|--------|----------------|
| Causal | [`schema-mechanism`](../../schema-mechanism/), [`schema-factory`](../../schema-factory/) |
| Situational | [`knowledge-frames`](../../knowledge-frames/) |
| Activation | [`k-lines`](../../k-lines/) |
| Meta-model | [`society-of-mind`](../../society-of-mind/) |
| Notation | [`yaml-jazz`](../../yaml-jazz/) |
| Execution | [`sister-script`](../../sister-script/), [`plan-then-execute`](../../plan-then-execute/), [`mooco`](../../mooco/), [`runtime`](../../runtime/) |
| Introspection | [`cursor-mirror`](../../cursor-mirror/) |

---

## License

Aligned with the parent skill: MIT (see [../SKILL.md](../SKILL.md)).
