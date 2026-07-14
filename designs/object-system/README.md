# MOOLLM Object System

How MOOLLM does objects: Self-style prototypes over the filesystem, with the LLM as universal
resolver. Promoted here from where the ideas were first proven in the field
([cauldron META-PLAN](../../skills/cauldron/META-PLAN.md),
[SKILL-SECURITY-ARCHITECTURE](../SKILL-SECURITY-ARCHITECTURE.md),
[DIRECTORY-AS-OBJECT](../../kernel/DIRECTORY-AS-OBJECT.md)) — per the
[Opus review](../../skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.md): latent-space
inheritance "generalizes MOOLLM's inheritance model to use the LLM as a universal resolver…
the most novel thing… and the thing least specific to cauldron."

## The docs

| Doc | What |
|-----|------|
| [SELF-AND-MOOLLM.md](SELF-AND-MOOLLM.md) | The mechanism and the heritage — Self as an object-oriented RISC instruction set (via Ungar's SOAR); the Lisp lineage (Flavors, CLOS, the MOP); the Drescher schema lineage (Piaget → Minsky → Drescher → Leela AI, with the LLM as the grounding that finally arrived); the NeWS/TNT/HyperLook/Densmore–Rosenthal-patent parents; what MOOLLM adds to Anthropic's skill model (instantiation, multiple inheritance, QueryInterface marker files, character rooms); naming and structure as reflection — filenames as K-lines, directory listings as Sims-style advertisements guiding the LLM's program counter |
| [LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md) | **The core discovery** — multiple inheritance from concrete files AND named concepts in training data; inherit whole languages, protocols, and object systems by saying their names (or patent numbers); the naming discipline; failure modes |
| [YOUTRACKDB-VS-MOOLLM.md](YOUTRACKDB-VS-MOOLLM.md) | Case study — JetBrains' class-based OO graph DB, compared *in order to inherit from it*: what each is better at, and the machine-language move (adaptors, bridges, emulators, drivers on the Self core) |
| [LIVE-OBJECTS-EXAMPLES.md](LIVE-OBJECTS-EXAMPLES.md) | The system running in public — Soul City / [MicropolisCore](https://github.com/SimHacker/MicropolisCore) (souls, content, human+LLM collaboration) and adventure-4 (built-in world) |
| [HUMANSPLAINING.md](HUMANSPLAINING.md) | The named anti-pattern — wasting tokens telling an LLM what it already knows; AI slop's mirror image; the Skillscript case study; capability confinement belongs in the runtime, not the grammar |
| [ANNOTATED-BIBLIOGRAPHY.md](ANNOTATED-BIBLIOGRAPHY.md) | Every YAML source cited by this series, annotated as human-readable prose with links back to the live files — one ladle from the repo's cream layer |

Reading order: SELF-AND-MOOLLM → LATENT-SPACE-INHERITANCE → the case studies. The annotated
bibliography is the side-table: consult it when a citation points into YAML you don't want to
context-switch into.

## The heritage, one line each

- **Self** (Ungar & Smith 1987) — clone / override / delegate; the RISC core everything lowers to
- **SOAR** (Ungar, Patterson, Séquin — Berkeley 1983–85) — Smalltalk On A RISC; the minimal-primitives discipline Self grew from
- **Flavors → CLOS → MOP** (Cannon, Moon, Bobrow, Kiczales et al.) — mixins, method combination, multiple dispatch, open implementation
- **NeWS / TNT / HyperLook** (Densmore, Gosling, Rosenthal, Hopkins, van Hoff) — multiple-inheritance OO PostScript shipped as system software; HyperCard-like editable scriptable UI; SimCity as live objects
- **Densmore–Rosenthal patent** ([US5187786A](https://patents.google.com/patent/US5187786A/en)) — the Unix filesystem IS a class hierarchy, 1991
- **Drescher** (*Made-Up Minds*, 1991, under Minsky) → **Leela AI** (Henry Minsky) — schema mechanism; the LLM supplies the grounding both generations lacked
- **Minsky** — K-lines and Society of Mind: the activation mechanism and the agency model the whole thing runs on
- **COM/OLE/ActiveX** — multiple interfaces per object; `QueryInterface` = `test -e <dir>/FOO.yml`

## Skills implementing this

[prototype](../../skills/prototype/) · [object](../../skills/object/) ·
[artifactory](../../skills/artifactory/) · [skill](../../skills/skill/) (the meta-skill) ·
[file-system-object](../../skills/file-system-object/) · [k-lines](../../skills/k-lines/) ·
[society-of-mind](../../skills/society-of-mind/) · [incarnation](../../skills/incarnation/) ·
[character](../../skills/character/) · [empathic-templates](../../skills/empathic-templates/) ·
[schema-mechanism](../../skills/schema-mechanism/) · [schema-factory](../../skills/schema-factory/) ·
[schema](../../skills/schema/) · [leela-ai](../../skills/leela-ai/)

Kernel: [DIRECTORY-AS-OBJECT](../../kernel/DIRECTORY-AS-OBJECT.md) ·
[SELFISH-COM-IMPLEMENTATION](../../kernel/SELFISH-COM-IMPLEMENTATION.md) ·
[constitution-core](../../kernel/constitution-core.md)

Prior designs: [SELF-ISH-INFLUENCES](../SELF-ISH-INFLUENCES.md) ·
[GARNET-AMULET-PROTOTYPE-SYSTEM](../GARNET-AMULET-PROTOTYPE-SYSTEM.md) ·
[PROTOTYPE-FRAGMENT-CONFIG](../PROTOTYPE-FRAGMENT-CONFIG.md) ·
[DIRECTORY-AS-IUNKNOWN](../DIRECTORY-AS-IUNKNOWN.md) · [MOO-HERITAGE](../MOO-HERITAGE.md) ·
[LINGUISTIC-MOTHERBOARD](../postscript/LINGUISTIC-MOTHERBOARD.md) ·
[VISUAL-PROGRAMMING-LINEAGE](../VISUAL-PROGRAMMING-LINEAGE.md)
