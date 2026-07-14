# Self and MOOLLM — prototypes over the filesystem

MOOLLM's object model is David Ungar and Randall Smith's **Self** (OOPSLA '87, *Self: The Power
of Simplicity*): no classes, no constructors — **objects, slots, and delegation**. Clone a
prototype, override what's different, delegate everything else up an **ordered list of multiple
parents**, first-match-wins.

Sibling doc: [LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md) — where the parent list
goes beyond the filesystem. Index: [README.md](README.md).

## The mapping

| Self | MOOLLM |
|------|--------|
| Object | Directory (or a single YAML file) |
| Slot | File in the directory (or key in the YAML) |
| Parent slot | `parents:` / `inherits:` entry |
| Clone | `cp -r` |
| Reflection | `ls` — slot access, not metaprogramming |
| Message send | Read the slot; if absent, follow parents in order |
| The world | The repo; git history is time travel |

A character clones the character prototype. A room clones the room prototype. A cauldron brew
clones the cauldron discipline. Each instance contains **only its overrides** — small, DRY,
diffable against its prototype ([empathic-templates](../../skills/empathic-templates/) makes the
schema side of this concrete: instances inherit from prototype schemas and carry only deltas,
which is also the audit trail — see
[SKILL-SECURITY-ARCHITECTURE](../SKILL-SECURITY-ARCHITECTURE.md)).

Identity is location: `docs/configuration/` IS that brew. Moving the directory renames the
instance; copying it instantiates a sibling
([cauldron CARD, "identity_through_location"](../../skills/cauldron/CARD.yml)).

## Why Self and not any of its descendants

Self is **microcode for object-oriented programming** — simpler than every descendant, powerful
enough to express all of them. The LLM has seen all the descendants extensively in training data,
and Self's clone/override/delegate is the substrate that unifies them
(from [SKILL-SECURITY-ARCHITECTURE](../SKILL-SECURITY-ARCHITECTURE.md)):

- **Java / modern JS class syntax** — prototype becomes the class, clones become instances
- **Original JS prototype chain** — `Object.create()` is literally Self delegation (Eich took
  Self's core idea and crippled it: single parent, `new`, `this` confusion)
- **HyperCard** — button → card → stack delegation; MOOLLM object → room → parent directory
- **CLOS / ScriptX generics** — multiple dispatch falls out of multiple parent slots
- **Lisp Machine Flavors** — mixins are just multiple parents
- **COM/IUnknown** — `QueryInterface` is checking whether a slot exists
  ([DIRECTORY-AS-IUNKNOWN](../DIRECTORY-AS-IUNKNOWN.md))
- **Lua metatables** — `__index` delegation, same idea

The LLM doesn't need any one language's ceremony because the underlying move is always the same.
When context calls for a class hierarchy it produces one; when it calls for HyperCard-style
containment delegation it produces that — all compiled down to clone, override, delegate.

## Multiple parents, ordered

Unlike JavaScript's single chain, MOOLLM parents are a **list** —
[`skills/prototype/`](../../skills/prototype/SKILL.md) (*"Self is one of this skill's
prototypes"*) and `PROTOTYPES.yml` define ordered multiple parents with first-match-wins.
A skill can inherit from a character prototype and a room prototype simultaneously. Flavors-style
mixins with none of the MRO metaphysics: sweep the list left to right, first slot found wins.

Anti-taxonomy ([prototype GLANCE](../../skills/prototype/GLANCE.yml)): not trees
(`Thing → Animal → Dog → Labrador`) but graphs
(`biscuit ←→ labrador-traits ←→ friendly-traits ←→ palm`). Everything is concrete. Nothing is
abstract — until you need an abstract parent, and then you name one from latent space
([LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md)).

## Reflection is cheap, and that changes behavior

Ungar's point: in a classy language reflection is metaprogramming; in Self it's slot access. In
MOOLLM it's opening a file. "What was the author thinking?" is one file open —
a META-PLAN slot if reified, an absent file (itself information) if not. Because reflection is
cheap, it actually happens. See the constellation model in
[cauldron META-PLAN §1](../../skills/cauldron/META-PLAN.md): reify what's there; absence is
honesty, not a gap.

## Prior art in the filesystem-as-object-graph

[DIRECTORY-AS-OBJECT](../../kernel/DIRECTORY-AS-OBJECT.md) cites the Densmore–Rosenthal patent
([US5187786A, 1991](https://patents.google.com/patent/US5187786A/en)) — NeWS-era proof the shape
works. [GARNET-AMULET-PROTOTYPE-SYSTEM](../GARNET-AMULET-PROTOTYPE-SYSTEM.md) traces the
constraint/prototype lineage through Garnet and Amulet. [MOO-HERITAGE](../MOO-HERITAGE.md) traces
the LambdaMOO thread: live objects, in-world building, delegation.

## The one-line summary

Self gave us the smallest possible object model. MOOLLM runs it on the largest possible
substrates: the filesystem for state, git for time, and — the part Self couldn't have —
**the LLM's latent space for every prototype nobody has bothered to write down**. That last move
is the subject of [LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md).
