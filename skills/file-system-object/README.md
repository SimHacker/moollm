# file-system-object — MOOLLM's OO Grammar for Directories and Files

> 📂 **Directories are classes. UPPERCASE files are interfaces. Plural-named directories declare their element type.**

The grammar rules that make MOOLLM's filesystem object-oriented. Every other meta-skill (skill, card, prototype, schema) uses these rules; this skill names them explicitly so newcomers can read MOOLLM directory trees fluently.

## Reading order (Semantic Image Pyramid)

| Resolution | File | When |
|---|---|---|
| 👁️ **GLANCE** | [GLANCE.yml](GLANCE.yml) | "What's the grammar?" — rules + COM analogy in 60 lines |
| 📇 **CARD** | [CARD.yml](CARD.yml) | "What interfaces does MOOLLM already define?" — canonical list of `SKILL`, `CARD`, `GLANCE`, `MECHANISM`, `ALERT`, `PROTOTYPES`, `EXPORTS`, `CHARACTER`, etc. |
| 📜 **SKILL** | [SKILL.md](SKILL.md) | "Full protocol" — three rules, COM analogy, examples from MOOLLM + Leela, reading protocol, authoring protocol, edge cases |

## The rules, in one paragraph each

1. A directory named `<things>/` declares "the things in here are of type `<thing>`." (`skills/` → each child is a skill.)
2. A file named `FOO.md` or `FOO.yml` at a directory's root declares that the directory **exports the FOO interface**. Multiple UPPERCASE files = multiple interfaces implemented by one directory-as-class.
3. The directory name is the implementation class name. No UUIDs — the filename IS the identifier.
4. **Serialization:** YAML is preferred, JSON is welcome (for tooling), comments are encouraged. Narrative interfaces (SKILL.md, README.md) use Markdown. `yaml-jazz`-style commenting is the MOOLLM house style.
5. **Empathic templates:** a plural container `<things>/` often ships with `<THING>.yml.template` — a copy-fill-strip scaffold with inline guidance and sensible defaults. Instances override only where they differ; defaults resolve via Self-style prototype delegation. A template that gets reused across unrelated contexts should be **lifted** to its own skill.
6. **Nested skills are categorized skills:** `skills/<parent>/skills/<child>/` places `<child>` in the `<parent>` category automatically. No separate category type is needed — the parent skill IS the category. Lift a sub-skill to top-level when it becomes reusable across unrelated contexts.

## COM in one sentence

Multiple interfaces per implementation class, just like COM — but the filename is the interface name, the directory name is the class name, no GUIDs, and `ls` is the QueryInterface.

## Why this skill exists

The grammar was implicit throughout MOOLLM before this skill existed. Explicit naming gives future skills, future biomes, future branch-as-object patterns, and future readers a shared reference to point at instead of re-deriving the pattern each time. Inspired by don@leela-ai.com's observation (2026-04-24) that our existing skill/biome layouts are already obeying a COM-like multi-interface-per-class grammar — we just hadn't said it out loud.

## Historical lineage (oldest first)

**Smalltalk** (Xerox PARC, 1970s) → **Self** (Ungar & Smith, 1987) → **NeWS** (Gosling & Rosenthal, Sun, 1986) → **TNT: The NeWS Toolkit** (Densmore & Rosenthal, Sun, late 1980s) → **COM / XPCOM** (Microsoft / Mozilla, 1990s) → **MOOLLM DOP + this skill** (2026).

The Densmore/Rosenthal TNT work — and the patent that came out of it — is the direct conceptual ancestor of "treat the file system as an OO class hierarchy." NeWS proved lightweight prototype delegation in production system software; TNT added a class hierarchy on top by filesystem/namespace convention. Full credit and references in [`SKILL.md` § Historical Lineage](SKILL.md#historical-lineage--where-this-came-from).

## See also

- [`../skill/`](../skill/) — meta-skill that uses this grammar to define what a MOOLLM skill IS
- [`../skill/delegation-object-protocol.md`](../skill/delegation-object-protocol.md) — DOP; `PROTOTYPES.yml` is an interface export under this grammar
- [`../prototype/`](../prototype/) — Self-style prototypes; directories as objects
- [`../schema/`](../schema/) — schemapedia; every mechanism uses this grammar
- [`../schema/schemas/mechanisms/com-xpcom/`](../schema/schemas/mechanisms/com-xpcom/) — COM / XPCOM structural ancestor
- [`../schema/schemas/mechanisms/self/`](../schema/schemas/mechanisms/self/) — Self mechanism profile
- [`../yaml-jazz/`](../yaml-jazz/) — the serialization style: comments as first-class semantic data
