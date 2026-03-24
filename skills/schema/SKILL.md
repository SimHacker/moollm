---
name: schema
description: Schemapedia — schema plugins, families, gateways, formats.yml, mechanism_relations; self-object kernel; delegates to sibling skills.
allowed-tools: [read, grep, glob]
---

# Schema (schemapedia)

**“Schema”** is overloaded. This skill is the **single index** for MOOLLM: **families** of mechanisms (interchange, notation, causal, situational, activation, relational, execution, **introspection**, **component_interop**, meta-model, **registry_meta**), **nomenclature**, **spec and skill pointers**, optional **CLI affordances** per plugin, and **gateways** between senses. It **registers** `cursor-mirror` with the **Cursor SQLite + YAML data model** (`CURSOR-SQLITE-MODEL.yml`, `DATA-SCHEMAS.yml`, …) alongside JSON Schema, SQLite, shell orchestration, and **com-xpcom** (COM / XPCOM history).

**Supersession (multi-axis + relations):** **[`schemas/supersession-suggestions.yml`](schemas/supersession-suggestions.yml)** lists **legacy clusters** with axes **`toward_now`**, **`upwardish`**, **`sideways`**, **`roots_downward`**, plus **`relation_semantics`** defining predicates (**replaces**, **variant_of**, **ancestor_of**, **complementary_to**, **opposite_of**, **intersects**, …) and per-cluster **`why`** blocks (**removes** / **adds** / **trades_away**). Goal-relative, not a universal ranking. Complements **`gateways.yml`**, not a replacement.

Treat schemapedia as a **network topology**: **mechanisms** in [`registry.yml`](schemas/registry.yml) are **nodes**; **[`gateways.yml`](schemas/gateways.yml)** bridges and optional **`mechanism_relations`** in each `MECHANISM.yml` are **edges** (translations, complements, application bridges). That graph is meant to drive **code generation**, **validation** across layers (wire payloads, world models, plans), and **execution** composition—provided every edge’s **fidelity** and **canonical source of truth** stay explicit.

**Blend space (simplicial + barycentric):** **[`schemas/blend-space.yml`](schemas/blend-space.yml)** lifts the graph to a **simplicial complex**: **joint** mechanisms in one workflow are **higher simplices** (triangles, …); **barycentric coordinates** are nonnegative weights on the vertices of a chosen simplex (summing to 1)—**navigation** = retuning that blend. **Supersession** axes live in a **different** explanatory space (legacy clusters), not as coords on the deployed simplex.

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
| **vcs** | Version control, commit DAG, diffs, hooks, provenance | **`git`** — object model and repo timeline |
| **collaboration** | Forges: APIs, issues/PRs, social graph, CI over git | **`github`** — REST/GraphQL + multi-facet hub; branch-as-object and **`Issue_<id>`** delegated to **moocroworld** + **moo** |
| **component_interop** | Binary component models (COM, XPCOM), IDL-era interfaces | **`com-xpcom`** — Microsoft COM / Mozilla XPCOM; deCOM history (see mechanism README) |
| **meta_model** | Society of Mind (agents, architecture) | `society-of-mind` |
| **registry_meta** | Schemapedia plugin model (MECHANISM.yml, augment, templates) | `mechanism` → this skill |

Deep theory stays in those skills; **registry.yml** holds stable ids, one-line summaries, and `delegate_skills` where applicable.

## Interchange vs notation vs causal vs relational

- **Interchange** — bytes on the wire or in config files; good for APIs and tool I/O. **JSON** carries a parsed tree only—**no comment channel**—so it cannot hold YAML Jazz’s semantic layer.
- **Notation** — **YAML Jazz** is a **registered schema plugin** (`yaml-jazz` in `registry.yml`): same YAML tree as interchange for the data, plus **Comment Oriented Programming (COP)**—comments as instance-specific code and data (constraints, transforms to maintain, procedural intent) that travel with the file—parallel lenses, doc-by-example. YAML text can round-trip commentary only with **comment-preserving** YAML tooling (implementations differ). Pair with JSON Schema when you need both **validated shape** and **authored meaning**; see **`mechanism_relations`** on `yaml-jazz` ↔ `json-schema` and **`gateways.yml`** `json-schema-with-yaml-jazz`.
- **Causal** — what the agent learned fires when; good for **schema-factory** pipelines.
- **Relational** — durable shape in a database engine; **SQLite** is a strong fit for embedded apps, tests, and single-file deploys. Support here means **documentation and gateway patterns**: migrations, `sqlite_master`, JSON1, ORM mapping—not shipping a SQL engine in the skill.

## Pantheon: self-object system, formats, COP, and XML

**Self-object system (MOOLLM core):** skills are **prototypes**; **files and directories** in the repo **instantiate** them (activation context, git history). The schemapedia is **meta-programming over schema mechanisms**—how interchange, notation, relational, and other families compose. It sits **on top of** the self-object kernel, not in place of it.

**Where COP fits:** **Comment Oriented Programming (COP)** is **not** its own registry mechanism. It lives in the **notation** family, expressed by **`yaml-jazz`**: the comment channel is the programming surface beside the parsed tree. **JSON** and other **interchange-only** shapes **have no COP layer** (no comment channel). See [`schemas/formats.yml`](schemas/formats.yml) `comment_oriented_programming`.

**Formats ↔ mechanisms:** Common **file formats** (plain text, **CSV**, **JSON**, **YAML**, **XML**, **SGML**) align with one or more **mechanism ids** depending on layer—interchange validators, notation (YAML only for COP in this registry), relational import, etc. The index is **[`schemas/formats.yml`](schemas/formats.yml)**.

**Interoperable CLI toolchains:** **[`schemas/formats.yml`](schemas/formats.yml)** `interoperable_toolchains` names **open-source, scriptable** tools (e.g. `jq`, `ajv-cli`, `yq`, `xmllint`, `jing`, `trang`, `xsltproc`, Saxon-HE) aligned with **mechanism ids** and **`gateways.yml`**—a practical layer for **shell-orchestration** skills and automation without pretending every bridge is one binary.

**XML and many grammars:** **XML** is one syntax family; **multiple schema mechanisms interoperate** on it (e.g. **W3C XML Schema** `xml-schema`, **RELAX NG** `relax-ng`, DTDs, instance-level rules). The registry lists the interchange mechanisms we stub; **`gateways.yml`** records bridges (e.g. `xsd-relax-ng`, `xml-json`). Do not collapse “XML” to a single schema—pick mechanisms and document gateways.

**Git and GitHub (and more):** **`git`** is a **vcs** mechanism—DAG, objects, hooks, timeline—not only “a format.” **`github`** is a **collaboration** mechanism: **interchange** (JSON APIs), **timeline** (issues, PRs, commits), **social** (stars, follows), **execution** (Actions), all over **`git`**. Typed **orphan branches** (`ClassName_ObjectID`, e.g. **`Issue_<IssueID>`**) as parallel object filesystems with history are specified in **moocroworld**; **moo** implements moorls and the CLI. See [`schemas/mechanisms/github/MECHANISM.yml`](schemas/mechanisms/github/MECHANISM.yml) and [`schemas/systems.yml`](schemas/systems.yml); add other forges the same way.

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
| [templates/MECHANISM.yml](templates/MECHANISM.yml) | Empathic prototype for `MECHANISM.yml`: comments bind layout, defaults, optional facets, and hooks (see file header). |
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
| `mechanism` | registry_meta | Meta: plugin shape, `templates/MECHANISM.yml`, `plugin-convention.yml`; delegates here (`schema` skill). |
| `sql`, `sqlite` | relational | DDL; `sqlite3`, dialect clients. |
| `yaml-jazz` | notation | Semantic YAML; `yq` when transforming. |
| `shell-orchestration` | execution | **Cursor / terminal agents:** compose docs → commands → scripts; ensemble below. |
| `cursor-mirror` | introspection | **Cursor SQLite + model YAML:** chats, tools, thinking, context; see `schemas/mechanisms/cursor-mirror/MECHANISM.yml`. |
| `git` | vcs | Objects, DAG, hooks, diffs; repo timeline—pairs with `shell-orchestration` for hooks. |
| `github` | collaboration | APIs, issues/PRs, social, Actions—`gateways.yml` `github-over-git`, `github-api-json-schema`; **`delegate_skills`**: moocroworld, moo. |
| `com-xpcom` | component_interop | COM / XPCOM binary interfaces; Mozilla decomification / decomtamination—curated links in `mechanisms/com-xpcom/README.md`. |

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
