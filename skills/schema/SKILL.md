---
name: schema
description: Schemapedia — schema plugins, families, gateways, formats.yml, mechanism_relations; self-object kernel; delegates to sibling skills.
allowed-tools: [read, grep, glob]
---

# Schema (schemapedia)

MOOLLM **schemapedia** is unrelated to the legacy **Schemapedia** product listed on the W3C Wiki ([Ontology repositories](https://www.w3.org/wiki/Ontology_repositories)).

**“Schema”** is overloaded. This skill is the **single index** for MOOLLM: **families** of mechanisms (interchange, notation, causal, situational, activation, relational, execution, **introspection**, **component_interop**, meta-model, **registry_meta**), **nomenclature**, **spec and skill pointers**, optional **CLI affordances** per plugin, and **gateways** between senses. It **registers** `cursor-mirror` with the **Cursor SQLite + YAML data model** (`CURSOR-SQLITE-MODEL.yml`, `DATA-SCHEMAS.yml`, …) alongside JSON Schema, SQLite, shell orchestration, and **com-xpcom** (COM / XPCOM history).

**Supersession (multi-axis + relations):** **[`schemas/supersession-suggestions.yml`](schemas/supersession-suggestions.yml)** lists **legacy clusters** with axes **`toward_now`**, **`upwardish`**, **`sideways`**, **`roots_downward`**, plus **`relation_semantics`** defining predicates (**replaces**, **variant_of**, **ancestor_of**, **complementary_to**, **opposite_of**, **intersects**, …) and per-cluster **`why`** blocks (**removes** / **adds** / **trades_away**). Goal-relative, not a universal ranking. Complements **`gateways.yml`**, not a replacement.

Treat schemapedia as a **network topology**: **mechanisms** in [`registry.yml`](schemas/registry.yml) are **nodes**; **[`gateways.yml`](schemas/gateways.yml)** bridges and optional **`mechanism_relations`** in each `MECHANISM.yml` are **edges** (translations, complements, application bridges). That graph is meant to drive **code generation**, **validation** across layers (wire payloads, world models, plans), and **execution** composition—provided every edge’s **fidelity** and **canonical source of truth** stay explicit.

## Part of MOOLLM

Repo [README](../../README.md), [skills/README.md](../README.md), [README.md](./README.md) (narrative).

## Families (what the registry sorts)

| Family | What it covers | Delegates to (examples) |
|--------|----------------|-------------------------|
| **interchange** | Wire/instance shapes and validators | JSON Schema, Zod, RELAX NG, XSD profiles |
| **notation** | Authoring YAML with semantic comments (YAML Jazz) | `yaml-jazz` skill — **schema plugin** in this registry |
| **causal** | Drescher Context → Action → Result | `schema-mechanism`, `schema-factory` |
| **situational** | Minsky frames (slots, defaults) | `knowledge-frames` |
| **activation** | K-lines / protocol symbols | `k-lines`, `PROTOCOLS.yml` |
| **prototype** | Self object model: delegation, receivers (Ungar & crew); MOOLLM kernel | `self` mechanism → **`prototype`** skill (DOP, ordered `PROTOTYPES.yml`, multiple parents including Self as lineage) |
| **relational** | Tables, constraints, dialects, DDL | `sql`, **`postgres`**, `sqlite`, **`datasette`** — skills wrap **CLI + file ecosystems**; **`datasette`** = SQLite publish (incl. **cursor-mirror** export); **`postgres-optimization`** (advanced PG tuning) |
| **execution** | Shell + sister scripts + orchestration (bash-shaped automation) | `shell-orchestration` → `sister-script`, `plan-then-execute`, `mooco`, `runtime` |
| **introspection** | Cursor session DB + reverse-engineered model | **`cursor-mirror`** → `cursor-mirror` skill + `reference/universal/CURSOR-SQLITE-MODEL.yml` et al. |
| **vcs** | Version control, commit DAG, diffs, hooks, provenance | **`git`** — object model and repo timeline |
| **collaboration** | Forges: APIs, issues/PRs, social graph, CI over git | **`github`** — REST/GraphQL + multi-facet hub; branch-as-object and **`Issue_<id>`** delegated to **moocroworld** + **moo** |
| **component_interop** | Binary component models (COM, XPCOM), IDL-era interfaces | **`com-xpcom`** — Microsoft COM / Mozilla XPCOM; deCOM history (see mechanism README) |
| **meta_model** | Society of Mind (agents, architecture) | `society-of-mind` |
| **registry_meta** | Schemapedia plugin model (MECHANISM.yml, augment, templates) | `mechanism` → this skill |

Deep theory stays in sibling skills; **registry.yml** holds ids, summaries, **`delegate_skills`**.

## Interchange vs notation vs causal vs relational

- **Interchange** — wire/config bytes; **JSON** (RFC 8259) is tree-only, **no comment syntax** (by design). **XML** / lexical **HTML** have lexical **`<!-- -->`** comments and a **DOM** that can keep comments and (per infoset/HTML rules) whitespace—unlike JSON-only APIs.
- **Notation** — **`yaml-jazz`**: same YAML tree as interchange for data, plus **COP** in comments (comment-preserving parsers). Pair with JSON Schema via **`gateways.yml`** `json-schema-with-yaml-jazz`. For **document-shaped** artifacts, **XML** or **HTML** can be the practical move when markup-native tooling matters.
- **Causal** — Drescher-style pipelines; **`schema-factory`**.
- **Relational** — **`sql`**, **`sqlite`**; **`postgres`** is not its own row—use **`sql`** + **`postgres-optimization`** for deep PG tuning. Here: docs and **gateway** patterns, not shipping engines.

## Pantheon: self-object system, formats, COP, and XML

**Self-object system:** skills are **prototypes**; repo **files**/**dirs** **instantiate** them. Schemapedia is **composition** over mechanism families, **on top of** that kernel.

**COP:** not a registry row; **`yaml-jazz`** carries **COP** in YAML comments. **PostScript DSC** (`%%` comments, `%!PS-Adobe-`) is the same **pattern**: parallel lane beside the executable. **XML**/**HTML**: lexical comments + DOM—**not** yaml-jazz, same **idea**. Details: [`schemas/formats.yml`](schemas/formats.yml) `comment_oriented_programming`.

**Literate vs COP:** Literate **WEB**-style weave/tangle makes prose and code **co-primary**; YAML Jazz keeps the **tree** authoritative and **comments** as a **second channel** (closer to **DSC** than to weave). **Fenced** Markdown blocks + plugins (**MDX**, **Quarto**, …) are **polyglot at block scope**—**not** COP-in-YAML, same family: human surface beside machine fragments.

**Documents vs payloads:** Prefer **XML**/**HTML** when the artifact is **markup-first**; **Svelte** `.svelte` is the same **shape** (regions + script/style).

**Formats ↔ mechanisms:** **[`schemas/formats.yml`](schemas/formats.yml)** maps lexical formats (text, **CSV**, **JSON**, **YAML**, **XML**, **SGML**) → **mechanism ids** (interchange, **`yaml-jazz`**, relational, …).

**Policy:** **Mechanisms** = **`registry.yml`** vertices with **`schemas/mechanisms/<id>/MECHANISM.yml`**. **Formats** = syntax; **do not** duplicate e.g. **JSON** as a row when **`json-schema`** is the contract. **CSV** = format + **relational** + project rules until a real interchange layer warrants a plugin. **`formats_index`** in **`registry.yml`**.

**CLI toolchains:** **`formats.yml`** `interoperable_toolchains` — `jq`, `ajv-cli`, `yq`, `xmllint`, `jing`, `trang`, … aligned with **`gateways.yml`**.

**XML:** one syntax; **many** mechanisms (**`xml-schema`**, **`relax-ng`**, …); **`gateways.yml`** has bridges—**do not** treat “XML” as one schema.

**Git / GitHub:** **`git`** (**vcs**), **`github`** (**collaboration**); see **`systems.yml`**, **[`schemas/mechanisms/github/MECHANISM.yml`](schemas/mechanisms/github/MECHANISM.yml)**.

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
| [templates/MECHANISM.yml](templates/MECHANISM.yml) | Template for `MECHANISM.yml`: layout, defaults, facets, hooks (see file header). |
| [schemas/registry.yml](schemas/registry.yml) | Master index: families + mechanisms. |
| [schemas/gateways.yml](schemas/gateways.yml) | Cross-mechanism bridges (including relational). |
| `schemas/mechanisms/<id>/MECHANISM.yml` | Per-mechanism profile; optional **`SCHEMAPEDIA-*-AUGMENT.yml`** (extended refs + improvisation). |
| [schemas/plugin-convention.yml](schemas/plugin-convention.yml) | Normative: standalone vs ensemble, `deeper_skills`, optional `cli_tools`. |
| [schemas/drescher-mapping.yml](schemas/drescher-mapping.yml) | Optional Drescher ↔ interchange serialization. |
| [schemas/formats.yml](schemas/formats.yml) | Formats ↔ mechanisms; self-object system; COP placement; XML many grammars. |
| [schemas/systems.yml](schemas/systems.yml) | Systems beyond formats—git, GitHub, facets (VCS, APIs, social, timelines). |

Add mechanisms by **new directory** `schemas/mechanisms/<id>/` with **`MECHANISM.yml`** + **registry entry** under the right `family`.

## Plugin shapes: one directory, depth optional

A **mechanism plugin** is always **`schemas/mechanisms/<id>/MECHANISM.yml`**. The directory name matches the registry id. What varies is whether that file is **enough on its own** or **indexes deeper work**:

| Shape | Meaning | `deeper_skills` |
|--------|---------|-----------------|
| **Standalone** | Specs, nomenclature, and hooks live in this file; no MOOLLM skill is required for the registry to be useful. | `[]` (empty or omitted) |
| **Ensemble** | The theory is bigger than a single schema-type plugin; this file **points at** one or more MOOLLM skills (single or ensemble) for full depth. | One or more skill ids (same list mirrored as `delegate_skills` on the mechanism in `registry.yml`). |

Normative: **`schemas/plugin-convention.yml`**. Keep **`registry.yml`** **`delegate_skills`** and **`MECHANISM.yml`** **`deeper_skills`** aligned.

**Mechanism ↔ mechanism:** a peer mechanism is not placed inside another mechanism’s directory (shared mechanisms are referenced by id; many profiles may point at the same bridge). Use **`gateways.yml`** for the canonical list of bridges (`from`, `to`, tools, fidelity). Each **`MECHANISM.yml`** may also declare **`mechanism_relations`** (see **`plugin-convention.yml`**) with: `target` mechanism id, `kind`, **`protocol`** (human-readable contract), optional **`gateway_ref`** (same id as a bridge in `gateways.yml`), and optional **`parameters`** (knobs, boundaries, ordering).

## Mechanism relations (composition protocols)

**`mechanism_relations`** in each **`MECHANISM.yml`** declare how mechanisms **compose** (complements, bridges, parameters)—**meta wiring**, not a replacement for **`gateways.yml`** or validators.

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
| `mechanism` | registry_meta | Meta: plugin shape, `templates/MECHANISM.yml`, `plugin-convention.yml`; delegates here (`schema` skill). |
| `sql`, `sqlite` | relational | DDL; `sqlite3`, dialect clients. |
| `yaml-jazz` | notation | Semantic YAML; `yq` when transforming. |
| `shell-orchestration` | execution | **Cursor / terminal agents:** compose docs → commands → scripts; ensemble below. |
| `cursor-mirror` | introspection | **Cursor SQLite + model YAML:** chats, tools, thinking, context; see `schemas/mechanisms/cursor-mirror/MECHANISM.yml`. |
| `git` | vcs | Objects, DAG, hooks, diffs; repo timeline—pairs with `shell-orchestration` for hooks. |
| `github` | collaboration | APIs, issues/PRs, social, Actions—`gateways.yml` `github-over-git`, `github-api-json-schema`; **`delegate_skills`**: moocroworld, moo. |
| `com-xpcom` | component_interop | COM / XPCOM binary interfaces; Mozilla decomification / decomtamination—curated links in `mechanisms/com-xpcom/README.md`. |

**`shell-orchestration` ensemble:** `sister-script`, `plan-then-execute`, `mooco`, `runtime` — see **`schemas/mechanisms/shell-orchestration/MECHANISM.yml`**.

## CLI affordances

**`cli_tools`** in **`MECHANISM.yml`**: `{ name, role }` per **`plugin-convention.yml`** (e.g. **jq**, **sqlite3**, **yq**).

## Credits

MOOLLM registry. SQL/SQLite specs: ISO/ANSI, sqlite.org.

**License:** MIT

**Tags:** schemapedia, registry, interchange, execution, cli_tools, drescher, frames, k-lines, sql, sqlite, gateways

**Related skills:** schema-mechanism, schema-factory, knowledge-frames, k-lines, society-of-mind, yaml-jazz, sister-script, plan-then-execute, mooco, runtime, cursor-mirror
