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
- **NeWS object-oriented PostScript / TNT** — dict-stack delegation, ordered `/Parents` lists,
  multiple inheritance in production window-system code (see the lineage section below)
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

## The NeWS lineage — parents MOOLLM inherits from literally

MOOLLM doesn't just cite this prior art; it delegates to it, in the Self-reflective sense. The
people are named parents in the `parents:` sense — and two of them (Don Hopkins, David
Rosenthal) are incarnated characters in the very repos that run on this object model.

**The Densmore–Rosenthal patent
([US5187786A, 1991](https://patents.google.com/patent/US5187786A/en))** — *"Method and apparatus
for implementing a class hierarchy of objects in a hierarchical file system"* (Sun). Owen
Densmore and David Rosenthal proved in 1991 that the Unix filesystem IS a class hierarchy:
directories as classes and instances, PATH files encoding inheritance chains, message sends via
shell (`SEND aF001 methodA args`). This is the direct ancestor of
[DIRECTORY-AS-OBJECT](../../kernel/DIRECTORY-AS-OBJECT.md) and the
[file-system-object](../../skills/file-system-object/SKILL.md) grammar — not an analogy MOOLLM
discovered, but a shape it inherited.

**NeWS object-oriented PostScript (Densmore, Sun, 1986→).** Owen Densmore built the class system
for NeWS (Gosling & Rosenthal's PostScript window system): class dictionaries on the dict stack,
method lookup walking the chain, instance dicts holding per-object state. NeWS 1.0 delegated
through a single `ParentDict`; TNT later added ordered `/Parents` lists and **multiple
inheritance** with flatten caches — ordered multiple parents, first-match-wins, the exact shape
of MOOLLM's `PROTOTYPES.yml`
([LINGUISTIC-MOTHERBOARD](../postscript/LINGUISTIC-MOTHERBOARD.md) §"Owen Densmore";
[Densmore's 1986 Monterey paper](https://donhopkins.com/home/monterey86.pdf);
[The NeWS Book](https://donhopkins.com/home/The_NeWS_Book_1989.pdf), ch. 6).

**TNT — The NeWS Toolkit (Densmore, Gosling, Hopkins et al., Sun, 1988→).** A full UI toolkit
built in that object system: windows, buttons, menus, canvases, pie menus, an X11 window manager.
Proof that prototype/multiple-inheritance PostScript wasn't a curiosity — it shipped system
software.

**HyperLook (Arthur van Hoff & Don Hopkins, Turing Institute, Glasgow, 1989–92).** Van Hoff's PdB
compiled C to object-oriented PostScript (subclass PostScript classes from C and vice versa);
with TNT it became HyperLook, née HyperNeWS née GoodNeWS — a HyperCard-like editable, scriptable,
**networked** UI environment
([Hopkins' HyperLook history](https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4)).
HyperCard's button→card→stack delegation, but with real multiple-inheritance objects and
PostScript graphics underneath.

**SimCity for HyperLook (Hopkins, 1990–92).** Don dogfooded HyperLook by porting Will Wright's
SimCity to it — the game as a stack of live, editable, scriptable objects. The thread runs
straight through: NeWS objects → HyperLook cards → The Sims' object advertisements → MOOLLM
directories advertising slots ([don-hopkins-projects](../don-hopkins-projects.md);
[VISUAL-PROGRAMMING-LINEAGE](../VISUAL-PROGRAMMING-LINEAGE.md)).

Adjacent threads: [GARNET-AMULET-PROTOTYPE-SYSTEM](../GARNET-AMULET-PROTOTYPE-SYSTEM.md)
(Myers/Hopkins at CMU — constraints + prototypes in Lisp) and [MOO-HERITAGE](../MOO-HERITAGE.md)
(LambdaMOO: live objects, in-world building, delegation).

The reflexive kicker: the patent's co-author has a character directory in WillWrightShowForFood
(`characters/david-rosenthal/`), and Don Hopkins has one in
[adventure-4](../../examples/adventure-4/characters/real-people/don-hopkins/). The system whose
object model descends from their work now instantiates them as objects in it. Inheritance in the
Self-reflective sense: the parents are in the world.

## The one-line summary

Self gave us the smallest possible object model. MOOLLM runs it on the largest possible
substrates: the filesystem for state, git for time, and — the part Self couldn't have —
**the LLM's latent space for every prototype nobody has bothered to write down**. That last move
is the subject of [LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md).
