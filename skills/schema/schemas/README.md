# `schemas/` — Schemapedia data layer

This directory is the **machine- and human-readable data layer** for the MOOLLM **`schema`** skill ([schemapedia](../README.md)). It splits into two layers:

| Layer | What lives here | Role |
|-------|-----------------|------|
| **`schemas/*.yml` (root)** | [registry.yml](./registry.yml), [plugin-convention.yml](./plugin-convention.yml), [gateways.yml](./gateways.yml), [drescher-mapping.yml](./drescher-mapping.yml) | **Cross-cutting**: master index, norms, bridges between mechanisms, optional Drescher↔payload shape notes. **Not** owned by a single mechanism. |
| **`schemas/mechanisms/<id>/`** | Each mechanism’s [MECHANISM.yml](./mechanisms/json-schema/MECHANISM.yml) (same filename everywhere) | **One plugin per directory** — interchange stubs (including JSON Schema and Zod), causal, situational, relational, execution, introspection, meta-model. Deep theory stays in delegated skills; optional future assets (examples, snippets) can sit beside `MECHANISM.yml`. |

**json-schema** and **zod** are **mechanisms** (interchange family), same as RELAX NG and XSD. They live under [`mechanisms/json-schema/`](./mechanisms/json-schema/MECHANISM.yml) and [`mechanisms/zod/`](./mechanisms/zod/MECHANISM.yml), not at the `schemas/` root, so every registered mechanism has a uniform path pattern.

Nothing here is a runtime validator by itself: these files **name**, **cross-link**, and **document** “schema” in every MOOLLM sense. **Delegation to MOOLLM skills** uses `plugin_profile.deeper_skills` in each `MECHANISM.yml`. **Delegation between mechanisms** (one mechanism acting as a *peer* or stack layer for another) does **not** use nested directories — the same mechanism directory is shared; use [gateways.yml](./gateways.yml) for formal bridges and narrative cross-refs inside profiles.

---

## Contents at a glance

| File | Role |
|------|------|
| [**registry.yml**](./registry.yml) | **Master index** — registry version, families, all mechanism ids, `profile` paths (`…/MECHANISM.yml`), `delegate_skills`, one-line summaries. |
| [**plugin-convention.yml**](./plugin-convention.yml) | **Normative rules** — `standalone` vs `ensemble` plugins, `deeper_skills`, optional `cli_tools`, directory layout. |
| [**gateways.yml**](./gateways.yml) | **Bridges** — JSON↔Zod, XSD↔RNG, JSON↔SQLite, Drescher↔rows, `json-schema`↔`yaml-jazz`, `shell-orchestration`↔`cursor-mirror`, `cursor-mirror`↔`sqlite`, etc. |
| [**drescher-mapping.yml**](./drescher-mapping.yml) | Optional **Drescher ↔ serialized payload** field mapping (not a universal bridge). |
| [**mechanisms/**](./mechanisms/) | **One subdirectory per mechanism** — see [mechanisms/README.md](./mechanisms/README.md). |
| [**templates/MECHANISM.yml**](../templates/MECHANISM.yml) | **Prototype** for new mechanism plugins (copy into `mechanisms/<id>/MECHANISM.yml`). |

---

## How it fits the parent skill

| Doc | Purpose |
|-----|---------|
| [../SKILL.md](../SKILL.md) | Full protocol: families, plugin shapes, CLI affordances, Cursor notes. |
| [../CARD.yml](../CARD.yml) | File list and interfaces for agents. |
| [../GLANCE.yml](../GLANCE.yml) | Fast orientation. |

---

## Registry (`registry.yml`)

- **Version** is bumped when families, mechanism layout, or cross-cutting files change (currently v6: per-mechanism `…/MECHANISM.yml` layout).
- **`families`** group mechanisms: `interchange`, `causal`, `situational`, `activation`, `relational`, `meta_model`, `notation`, `execution`, `introspection`.
- **`mechanisms.<id>`** points to **`profile`**: `schemas/mechanisms/<id>/MECHANISM.yml`.
- **`delegate_skills`** on a mechanism must mirror **`plugin_profile.deeper_skills`** in that `MECHANISM.yml` when the plugin is an **ensemble** (`plugin-convention.yml`).
- **`plugin_convention`** field: path to **`plugin-convention.yml`**.

---

## Gateways (`gateways.yml`)

Cross-mechanism relationships: translation, complementary stacks (e.g. JSON Schema + YAML Jazz), dialect ports, persistence patterns, and **observability** (shell → cursor-mirror). See the file for version and `bridges` list.

---

## Plugin convention (`plugin-convention.yml`)

Defines:

- `standalone` — full value in one `MECHANISM.yml`; `deeper_skills: []`.
- `ensemble` — profile indexes one or more MOOLLM skills.
- Optional **`cli_tools`**: `{ name, role }` for agents (jq, sqlite3, yq, …).
- Optional **`mechanism_relations`** on any `MECHANISM.yml`: outgoing edges to other mechanism ids (`target`, `kind`, **`protocol`**, optional **`gateway_ref`**, optional **`parameters`**). Align **`gateway_ref`** with [`gateways.yml`](./gateways.yml) when a bridge exists.
- **Directory rule**: `schemas/mechanisms/<id>/MECHANISM.yml` only; no flat `mechanisms/foo.yml`.

---

## Subdirectory: `mechanisms/`

Every registered mechanism has **`schemas/mechanisms/<registry-id>/MECHANISM.yml`**. The detailed index is in **[mechanisms/README.md](mechanisms/README.md)**.

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
