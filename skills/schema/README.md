# Schema — a Veritable **Schemapedia**

If an encyclopedia is a **circle of general knowledge**, consider this a **schemapedia**—a circle drawn around *schema* in **every MOOLLM sense** that needs a name and a shelf:

**Not the W3C-listed ontology directory:** The W3C Wiki page [Ontology repositories](https://www.w3.org/wiki/Ontology_repositories) catalogs sites such as BioPortal and Prefix.cc and includes a legacy entry **Schemapedia** (`schemapedia.com`) described there as another ontology directory. That is **unrelated** to MOOLLM: this repo’s **schemapedia** is the **in-tree** mechanism registry and graph ([`registry.yml`](./schemas/registry.yml), [`gateways.yml`](./schemas/gateways.yml), mechanism plugins under [`schemas/mechanisms/`](./schemas/mechanisms/)). Same word, different system.

Concretely, it includes **interchange** shapes ([JSON Schema](./schemas/mechanisms/json-schema/MECHANISM.yml), [Zod](./schemas/mechanisms/zod/MECHANISM.yml), RELAX NG, XSD), **notation** ([YAML Jazz](../yaml-jazz/SKILL.md) is itself a registered schema plugin here), **prototype** kernel ([Self](./schemas/mechanisms/self/MECHANISM.yml) → [prototype](../prototype/SKILL.md): skills-as-prototypes, DOP), **execution** ([shell-orchestration](./schemas/mechanisms/shell-orchestration/MECHANISM.yml)), **introspection** ([cursor-mirror](../cursor-mirror/SKILL.md): Cursor SQLite + YAML data model under [`skills/cursor-mirror/reference/`](../cursor-mirror/reference/universal/CURSOR-SQLITE-MODEL.yml)), **causal** units ([Drescher](./schemas/mechanisms/drescher/MECHANISM.yml)), **situational** structure ([Minsky frames](./schemas/mechanisms/minsky-frame/MECHANISM.yml)), **activation** symbols ([K-lines](./schemas/mechanisms/k-lines/MECHANISM.yml)), the **Society of Mind** meta-model ([SoM](./schemas/mechanisms/society-of-mind/MECHANISM.yml)), **registry_meta** ([mechanism](./schemas/mechanisms/mechanism/MECHANISM.yml) — the schemapedia plugin model itself), and **relational** artifacts ([SQL](./schemas/mechanisms/sql/MECHANISM.yml), [SQLite](./schemas/mechanisms/sqlite/MECHANISM.yml)). Each mechanism is **`schemas/mechanisms/<id>/MECHANISM.yml`**; profiles may list **`cli_tools`** (for example `jq`, `sqlite3`, `yq`). **Gateways** and **drescher-mapping** live at **`schemas/*.yml`** because they cross-cut many mechanisms. **Delegation** to MOOLLM skills uses `deeper_skills`; referencing another *mechanism* does not nest directories—peers share ids and [`gateways.yml`](./schemas/gateways.yml).

### Where the threads land

Wire formats **won** the network (**JSON** first, XML’s many grammars beside it). **Databases** won durable shape (**SQL**, **SQLite**). **Desktop** history left us **COM** / **OLE** lessons (binary surfaces, not JSON). **Lisp** gave **CLOS** and **generic dispatch**; **Self** gave **prototype delegation**; **Minsky** gave **frames** and **K-lines**; **YAML Jazz** folds **human intent** beside the parse tree. None of those stories **replaces** the others—**schemapedia** is the **map**: each family gets a **row** in [`registry.yml`](./schemas/registry.yml), **gateways** mark where pipelines **touch**, and **blend-space** / **supersession** admit that “progress” is **not** a single ladder. The **near future** work is whatever crosses those bridges next—**shell** runs feeding **Cursor** introspection, **JSON Schema** paired with **YAML Jazz**, **git** timelines beside **GitHub** APIs—without pretending one mechanism **is** the kernel unless it **is** ( **`self`** names the prototype bedrock; **`json-schema`** names the wire).

**SQLite** and **SQL** are first-class rows in [`registry.yml`](./schemas/registry.yml): DDL, `sqlite_master`, migrations, JSON1, and the usual split between “API body schema” and “table schema” are exactly the kind of cross-cutting question the schemapedia is for.

## What this skill is for

The **`schema`** skill is MOOLLM’s **single cross-family index** for anything “schema-shaped”: wire formats, semantic YAML, causal logs, frames, activation bundles, SQL engines, shell pipelines, and Cursor session introspection. It does **not** replace validators or ORMs; it **names** mechanisms, **sorts** them into [families](#families-and-typical-delegates), **links** to the skills that carry full theory, and records **gateways** where two mechanisms meet in real work.

Reach for it when you need to:

- Choose or document a schema-like mechanism without conflating interchange, notation, causal, or relational senses ([`GLANCE.yml`](./GLANCE.yml) `when_to_use`).
- Relate APIs, YAML Jazz files, Drescher units, frames, K-lines, or DB DDL in one vocabulary ([`SKILL.md`](./SKILL.md)).
- Find **who owns depth** for a topic (`delegate_skills` in [`registry.yml`](./schemas/registry.yml), `deeper_skills` in each mechanism profile and in [`plugin-convention.yml`](./schemas/plugin-convention.yml)).

## Semantic Image Pyramid (reading order)

MOOLLM reads skills from shallow to deep. For **`schema`**, use this order:

| Step | File | Question |
|------|------|----------|
| 1 | [`GLANCE.yml`](./GLANCE.yml) | Is this the skill I need? |
| 2 | [`CARD.yml`](./CARD.yml) | What version, interfaces, and files exist? |
| 3 | [`SKILL.md`](./SKILL.md) | What is the protocol: families, registry, plugins, gateways, checklist? |
| 4 | **This README** | How does the schemapedia sit in the repo, and where do I click next? |
| 5 | [`schemas/README.md`](./schemas/README.md) | What lives under `schemas/`, file by file? |
| 6 | [`schemas/mechanisms/README.md`](./schemas/mechanisms/README.md) | What is each mechanism plugin, and how do they link out? |

The pyramid fields in [`GLANCE.yml`](./GLANCE.yml) (`pyramid.glance` / `card` / `skill`) mirror that order.

## Where the canonical data lives

| Piece | Role |
|--------|------|
| [`schemas/README.md`](./schemas/README.md) | Directory tour and index of top-level YAML under `schemas/`. |
| [`schemas/mechanisms/README.md`](./schemas/mechanisms/README.md) | Full index of mechanism dirs (`schemas/mechanisms/<id>/MECHANISM.yml`). |
| [`templates/MECHANISM.yml`](./templates/MECHANISM.yml) | Prototype file for new mechanism plugins. |
| [`schemas/registry.yml`](./schemas/registry.yml) | Master index by **family** (interchange, causal, situational, activation, **prototype**, relational, execution, introspection, **vcs**, **collaboration**, component_interop, meta_model, **registry_meta**, notation). |
| [`schemas/plugin-convention.yml`](./schemas/plugin-convention.yml) | Normative: **standalone** vs **ensemble**, `deeper_skills`, **`mechanism_relations`** (peer protocols + `gateway_ref`), optional `cli_tools`. |
| [`schemas/gateways.yml`](./schemas/gateways.yml) | Bridges between mechanisms (wire↔wire, JSON↔SQLite, Drescher↔rows, shell↔introspection, …). |
| [`schemas/drescher-mapping.yml`](./schemas/drescher-mapping.yml) | Optional Drescher ↔ serialized interchange notes (cross-cutting). |
| [`schemas/formats.yml`](./schemas/formats.yml) | Formats ↔ mechanisms; self-object system; COP; XML’s many grammars. |
| [`schemas/systems.yml`](./schemas/systems.yml) | **git**, **GitHub** — VCS, APIs, timelines, social layers. |

## Families and typical delegates

The registry sorts every mechanism into a **family**. Deep theory lives in **sibling skills**; the registry carries **ids**, **summaries**, and **`delegate_skills`** pointers. This table matches the narrative in [`SKILL.md`](./SKILL.md#families-what-the-registry-sorts).

| Family | Covers | Often delegates to |
|--------|--------|---------------------|
| **interchange** | Wire/instance shapes and validators | Mechanism YAML + external specs; tools like `jq` / `ajv-cli` where listed. |
| **notation** | Semantic YAML (YAML Jazz) | [`yaml-jazz`](../yaml-jazz/SKILL.md) |
| **causal** | Drescher Context → Action → Result | [`schema-mechanism`](../schema-mechanism/SKILL.md), [`schema-factory`](../schema-factory/SKILL.md) |
| **situational** | Minsky-style frames | [`knowledge-frames`](../knowledge-frames/SKILL.md) |
| **activation** | K-lines / protocol symbols | [`k-lines`](../k-lines/SKILL.md), repo [`PROTOCOLS.yml`](../../PROTOCOLS.yml) |
| **prototype** | Self lineage: delegation, receivers; MOOLLM kernel | [`self/MECHANISM.yml`](./schemas/mechanisms/self/MECHANISM.yml) → [`prototype`](../prototype/SKILL.md) |
| **relational** | Tables, constraints, dialects | [`sql/MECHANISM.yml`](./schemas/mechanisms/sql/MECHANISM.yml), [`sqlite/MECHANISM.yml`](./schemas/mechanisms/sqlite/MECHANISM.yml) |
| **execution** | Shell and orchestration | [`shell-orchestration/MECHANISM.yml`](./schemas/mechanisms/shell-orchestration/MECHANISM.yml) ensemble: [`sister-script`](../sister-script/SKILL.md), [`plan-then-execute`](../plan-then-execute/SKILL.md), [`mooco`](../mooco/SKILL.md), [`runtime`](../runtime/SKILL.md) |
| **introspection** | Cursor session DB + model YAML | [`cursor-mirror`](../cursor-mirror/SKILL.md) skill and [`cursor-mirror/MECHANISM.yml`](./schemas/mechanisms/cursor-mirror/MECHANISM.yml) |
| **vcs** | Distributed version control (DAG, commits, hooks) | [`git/MECHANISM.yml`](./schemas/mechanisms/git/MECHANISM.yml) |
| **collaboration** | Forges, APIs, social graph over repos | [`github/MECHANISM.yml`](./schemas/mechanisms/github/MECHANISM.yml) |
| **component_interop** | Binary COM / XPCOM (historical component models) | [`com-xpcom/MECHANISM.yml`](./schemas/mechanisms/com-xpcom/MECHANISM.yml) |
| **meta_model** | Society of Mind | [`society-of-mind`](../society-of-mind/SKILL.md) |
| **registry_meta** | The plugin shape itself (`MECHANISM.yml`, augments, templates) | [`mechanism/MECHANISM.yml`](./schemas/mechanisms/mechanism/MECHANISM.yml) → this **`schema`** skill |

## Gateways

When two mechanisms meet in a pipeline (for example JSON Schema at an HTTP boundary vs rows in SQLite, or shell runs followed by SQLite inspection), the **bridge** belongs in [`gateways.yml`](./schemas/gateways.yml). [`SKILL.md`](./SKILL.md) describes when to extend gateways alongside new mechanism profiles.

## Introspection: cursor-mirror anchor files

The **`cursor-mirror`** mechanism is registered here and implemented under [`skills/cursor-mirror/`](../cursor-mirror/). Useful entry points for the **SQLite + YAML** story:

- [`reference/universal/CURSOR-SQLITE-MODEL.yml`](../cursor-mirror/reference/universal/CURSOR-SQLITE-MODEL.yml)
- [`reference/reverse-engineered/DATA-SCHEMAS.yml`](../cursor-mirror/reference/reverse-engineered/DATA-SCHEMAS.yml)
- [`reference/universal/model/tables.yml`](../cursor-mirror/reference/universal/model/tables.yml)
- [`schemas/mechanisms/cursor-mirror/MECHANISM.yml`](./schemas/mechanisms/cursor-mirror/MECHANISM.yml) (how this skill registers the plugin)

## Related skills (delegation, not duplication)

[`CARD.yml`](./CARD.yml) lists **`related`**: [schema-mechanism](../schema-mechanism/SKILL.md), [schema-factory](../schema-factory/SKILL.md), [knowledge-frames](../knowledge-frames/SKILL.md), [k-lines](../k-lines/SKILL.md), [prototype](../prototype/SKILL.md), [society-of-mind](../society-of-mind/SKILL.md), [yaml-jazz](../yaml-jazz/SKILL.md). [`GLANCE.yml`](./GLANCE.yml) also names [cursor-mirror](../cursor-mirror/SKILL.md) under `related_skills`. Use those skills for full protocols; use **`schema`** to **orient and wire** families, registry rows, and gateways.

## Ecosystem pointers

- [Skills index (`INDEX.md`)](../INDEX.md) — full skill catalog and narrative links.
- [Skills `INDEX.yml`](../INDEX.yml) — machine-oriented skill list.
- [Repository `README.md`](../../README.md) — MOOLLM at repo level.

## Part of MOOLLM

See [skills/README.md](../README.md) and the repo [README](../../README.md).

## License

MIT (see [SKILL.md](./SKILL.md)).
