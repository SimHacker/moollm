# Self and MOOLLM — prototypes over the filesystem

MOOLLM's object model is David Ungar and Randall Smith's **Self** (OOPSLA '87, *Self: The Power
of Simplicity*): no classes, no constructors — **objects, slots, and delegation**. Clone a
prototype, override what's different, delegate everything else up an **ordered list of multiple
parents**, first-match-wins.

Siblings: [LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md) — where the parent list
goes beyond the filesystem · [YOUTRACKDB-VS-MOOLLM.md](YOUTRACKDB-VS-MOOLLM.md) —
comparison-for-inheritance case study · [LIVE-OBJECTS-EXAMPLES.md](LIVE-OBJECTS-EXAMPLES.md) —
the system running in public · [ANNOTATED-BIBLIOGRAPHY.md](ANNOTATED-BIBLIOGRAPHY.md) — every
YAML file cited below, annotated as prose · Index: [README.md](README.md).

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

Self is an **object-oriented RISC instruction set** — a small, orthogonal core (clone, override,
delegate) that every CISC-y descendant compiles down to. Simpler than all of them, powerful
enough to express all of them, fast *because* it's minimal — the same bet RISC made against
microcoded instruction sets.

And that's not our metaphor — it's Self's actual parentage, and we inherit the heritage. Before
Self, Ungar was an architect of **SOAR — Smalltalk On A RISC** (Berkeley, 1983–85): David
Patterson and Carlo Séquin's RISC I/II project turned toward running Smalltalk-80 on a reduced
instruction set, with Ungar's thesis (*The Design and Evaluation of a High Performance Smalltalk
System*, 1986 ACM Doctoral Dissertation Award) contributing generation scavenging and the
measurement discipline — find the small set of primitives that carries the whole dynamic object
system, and make those fast. Self is SOAR's lesson applied to language design: strip the object
model itself down to its RISC core. MOOLLM's `parents:` list pulls in that whole tradition —
Patterson, Séquin, Ungar, the SOAR team — by name.

The LLM has seen all the descendants extensively in training data,
and Self's three instructions are the target they all lower to
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

## The Lisp lineage — Flavors, CLOS, and the MOP

The other heritage we inherit by name is the Lisp Machine line — the gloriously CISC end of the
spectrum whose lessons Self's RISC core was partly a reaction to, and which MOOLLM gets back as
*libraries* over that core:

- **Lisp Machine Flavors** (Howard Cannon, MIT, ~1979, named for the mix-in flavors at Steve's
  Ice Cream near MIT) — invented **mixins** and method combination: `:before`/`:after`/`:around`
  daemons composing behavior from multiple parents. MOOLLM's ordered `parents:` list is Flavors'
  mixin list; MOOLLM's ambient skills (no-ai-slop et al., always-on constraints wrapping every
  response) are `:around` methods in everything's combination.
- **New Flavors** (David A. Moon, Symbolics, 1986) and **CommonLoops** (Bobrow, Kiczales et al.,
  Xerox PARC) merged into **CLOS** (Bobrow, DeMichiel, Gabriel, Keene, Kiczales, Moon) — generic
  functions and **multiple dispatch**: methods live outside classes and specialize on *all* their
  arguments. MOOLLM's dispatch is the limit case: the LLM specializes on the entire context —
  every argument, the room, the reading order, the ambient constraints — a generic function over
  the whole world-state.
- **Class precedence lists** — CLOS linearizes the diamond (later refined as Dylan's C3, now in
  Python). MOOLLM keeps the *ordered-parents* idea but drops the linearization metaphysics:
  first-match-wins left to right, and where slots genuinely blend, the reader reconciles in
  context instead of an algorithm picking one ancestor.
- **The MOP** (Kiczales, des Rivières, Bobrow — *The Art of the Metaobject Protocol*, 1991) —
  the object system implemented *in itself*, its classes and dispatch reified as objects you can
  subclass to change how the system works. MOOLLM has an implicit MOP, documented in
  [DIRECTORY-AS-IUNKNOWN §Meta-Object Protocol](../DIRECTORY-AS-IUNKNOWN.md): how interfaces are
  found (file patterns), how inheritance resolves (`inherits:`/`parents:` in YAML), how dispatch
  works (skill loading and composition), how to extend (drop files in extension directories).
  The kernel is the metaobject layer — and it's made of the same stuff as everything else:
  editable files in the same repo, no privileged meta-level substrate. AMOP's dream of an "open
  implementation" arrives trivially when the implementation is prose the interpreter reads.

The same move as everywhere else in this series: we don't reimplement method combination,
multiple dispatch, or metaobject protocols — we **inherit that heritage by saying the names**
(Cannon, Moon, Bobrow, Kiczales; "Flavors mixins", "CLOS generic functions", "AMOP"), and the
latent prototypes come in carrying their whole tradition
([LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md)). ScriptX (Kaleida's CLOS-descended
multimedia language) rides the same K-line.

## Anti-taxonomy

Anti-taxonomy ([prototype GLANCE](../../skills/prototype/GLANCE.yml)): not trees
(`Thing → Animal → Dog → Labrador`) but graphs
(`biscuit ←→ labrador-traits ←→ friendly-traits ←→ palm`). Everything is concrete. Nothing is
abstract — until you need an abstract parent, and then you name one from latent space
([LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md)).

## The Drescher lineage — schemas, and the grounding that finally arrived

The learning-engine side of the heritage runs Piaget → Minsky → Drescher → Leela AI → MOOLLM,
and it's inherited the same way as everything else here: by invoking it in latent space, then
refining and adapting it to the LLM mooniverse as skills.

**Gary Drescher** wrote his PhD under Marvin Minsky at MIT — *Made-Up Minds: A Constructivist
Approach to Artificial Intelligence* (MIT Press, 1991; preceded by *Genetic AI: Translating
Piaget into Lisp*, 1986). The **schema mechanism**: Context → Action → Result units discovered
from experience; **marginal attribution** (does the result follow the action more than chance?);
**spinoff schemas** (add context when a schema is unreliable); **synthetic items** (invent a
hidden-state hypothesis when no observable context explains the pattern — the mechanism
*postulating objects* it cannot see); schema chaining as planning. A robot hand and eye in a
Lisp microworld, learning Piagetian object permanence from scratch.

**Henry Minsky** — Marvin's son — reimplemented the mechanism in Python at **Leela AI**
(co-founded with Cyrus Shaoul and Milan Minsky; *Leela* is Sanskrit for divine play), driving it
into neurosymbolic manufacturing intelligence: ConvNet perception feeding a symbolic schema
core. The full chain is documented in this repo at
[skills/leela-ai/reference/drescher-lineage.yml](../../skills/leela-ai/reference/drescher-lineage.yml)
(annotated in
[ANNOTATED-BIBLIOGRAPHY.md](ANNOTATED-BIBLIOGRAPHY.md#drescher-lineage--the-piaget-to-leela-chain-with-sources)).

**What neither generation had: grounding.** Drescher's items were bit-vectors; the symbol
grounding problem was the wall his Lisp — and any pre-LLM reimplementation — ran into. The
LLM removes the wall: contexts, actions, and results can be natural-language propositions whose
*meaning* the coherence engine evaluates. Marginal attribution over meaning instead of bits.
That's exactly the extension list on
[schema-mechanism](../../skills/schema-mechanism/GLANCE.yml): `symbol_grounding: "Items mean
something"`, `causal_reasoning: "Why patterns hold"`, `natural_explanation: "Communicate
discoveries"` — with lineage line `Piaget → Minsky → Drescher → MOOLLM` and Henry Minsky's
`pyleela.brain` in the credits. This was not possible when Drescher was writing his thesis code,
and not possible when Henry was reimplementing it — the resolver that grounds the symbols didn't
exist yet.

The skills inherit **directly from the thesis in latent space**: "Drescher's schema mechanism"
and "Made-Up Minds" are parent names the LLM resolves richly, refined in-repo rather than
respelled. [schema-factory](../../skills/schema-factory/) is the disciplined half of the hybrid —
deterministic Python (lint, ingest, compose, context bundles) before LLM synthesis, with
[Henry Minsky's blocksworld](../../skills/schema-factory/examples/henry-minsky-blocksworld.yml)
as a worked example and a SCHEMA-SCHEMA that evolves via the same loop it governs. The
[schema](../../skills/schema/) skill's schemapedia files the mechanism alongside JSON-Schema and
Zod as one more schema tradition
([mechanisms/drescher/](../../skills/schema/schemas/mechanisms/drescher/)).

And the Minsky inheritance is doubled, the "Bester" pattern from
[LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md): through Drescher's thesis advisor we
inherit **K-lines** ([skills/k-lines/](../../skills/k-lines/)) — the activation mechanism this
whole object system runs on — and **Society of Mind**
([skills/society-of-mind/](../../skills/society-of-mind/)) — agencies of simple agents, which is
what a MOOLLM session full of skills, characters, and ambient constraints *is*. Marvin's
concepts organize the inheritance system that inherits from him.

## What MOOLLM adds to Anthropic's skill model

Anthropic Skills are documentation-first tool definitions — a solid foundation MOOLLM
gratefully builds on ([skills/skill/](../../skills/skill/SKILL.md) §"Foundation: What We Share
with Anthropic" lists all eight extensions). The ones that matter for the object system:

**Instantiation.** An Anthropic skill is instructions; a MOOLLM skill is a **prototype that
creates instances**. `INSTANTIATE` = clone: `skills/experiment/` carries templates and an
`experiments/` directory of living instances; each run is an object with its own state files,
history, and overrides. The skill is class AND instance the Self way — a full working object
that is also the template ([artifactory](../../skills/artifactory/)).

**Multiple inheritance.** Skills declare ordered `parents:`/`inherits:` (concrete paths and
latent-space names alike) instead of standing alone — the whole subject of
[LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md).

**Multiple interfaces per directory — the COM/OLE/ActiveX reading.** The UPPERCASE marker files
in a directory are its exported interfaces, and checking for one is `QueryInterface`:
`test -e <dir>/CHARACTER.yml` is `QueryInterface(IID_ICharacter, &ptr)`
([file-system-object](../../skills/file-system-object/SKILL.md),
[DIRECTORY-AS-IUNKNOWN](../DIRECTORY-AS-IUNKNOWN.md)). One directory exports SKILL + CARD +
GLANCE + README + CHARACTER + PROTOTYPES simultaneously — classic COM multiple-interface
composition with readable names instead of UUIDs, `ls` as the free type-checker, no registry.
OLE's insight rides along: objects embed in other objects' containers and stay live, the way a
skill instance lives inside another skill's directory.

Why COM needed GUIDs and MOOLLM doesn't: COM's interface names lived in one **flat global
namespace** (the registry), so uniqueness had to be manufactured — 128 random bits, opaque to
every reader, resolvable only through regsvr32 ceremony. MOOLLM's names are **scoped by path**:
`skills/cauldron/CARD.yml` collides with nothing, and git remotes supply the global identity
GUIDs were invented to fake. So the names get to be readable — and readable pays twice. For
humans, `CHARACTER.yml` in a listing needs no lookup. For the LLM, it's the difference between
a K-line and a cache miss: `{F37C775C-...}` activates nothing, while `CHARACTER.yml` pulls in
the entire tradition of what character sheets are. COM's identifiers were hostile to both of its
audiences; the filesystem's namespace discipline lets MOOLLM serve both with one name.

**Interface composition makes new kinds of objects.** Because interfaces are files, dropping one
file into a directory *adds a facet to a live object*. The canonical example: a directory with
`ROOM.yml` is a place; add `CHARACTER.yml` **to the same directory** and it becomes a **character
room** — a room that is somebody. A living room in the Pee-wee's Playhouse sense: like Chairry,
Magic Screen, and Conky, the room itself is a character you can talk to, and it **watches and
remembers what goes on inside it** — its state files (guestbook, photos, session logs, LOG.md)
are its memory slots, appended as the world plays out inside it. Adventure-4's pub is exactly
this: a room-object with a personality interface, whose subdirectories (guestbook, photos,
rooms) are the things it remembers. Aggregation COM never made easy is one `cp` here.

**State files as first-class slots.** Anthropic skills are stateless instructions; MOOLLM
objects persist — `ROOM.yml`, `CHARACTER.yml`, `RUN.yml`, `RELATIONSHIPS.yml`, session logs.
The three-tier split (platform skill → narrative instance → state persistence) means the
prototype, the story, and the memory are separate files with separate lifecycles, all in git.

## CARD.yml — interface definition AND dispatch table, inherited from The Sims

The CARD deserves its own entry, because it's two classical artifacts fused. Read one way, it's
an **interface definition** — the IDL/TypeLib role, dispatch metadata describing methods,
properties, state, and inheritance, binary in COM but human-readable YAML here (the
[card skill's pun stack](../../skills/card/SKILL.md) makes the lineage explicit: HyperCard's
navigable unit, Microsoft's Type Library, Hewitt's actor signature, a dispatchable thread, a
trading card). Read the other way, it's a **dispatch table for behavior selection** — and that
half is inherited from the most successful plug-together object ecosystem ever shipped:
**The Sims' advertisements**.

The Sims mechanic ([sims-object-model](../sims/sims-object-model.md),
[sims-find-best-action](../sims/sims-find-best-action.md)): every object broadcasts
advertisements — "I satisfy hunger," "I provide fun" — with **procedural scoring** against the
Sim's current motives and personality. Autonomous behavior is Find Best Action over the scored
advertisements; **user-driven behavior is the same interaction set surfaced through pie menus**
when you click the object. One declaration, two dispatch paths: the engine scores it for
autonomy, the player picks it from the pie. That's why the ecosystem was plug-together —
a new object drops into any lot and *just works*, because it carries its own advertisement
table; no central registry of behaviors, no engine patch. Thousands of community objects later,
the architecture had proven that advertisement-based dispatch scales socially, not just
technically.

MOOLLM's CARD advertisements are that mechanism, uplifted. Each advertisement carries a
`score:` and a `condition:` ("PET-THE-CAT: score 80, condition: cat is present"), and the card
skill's layout rule — **advertisements first, before methods** — is Sims engine wisdom
translated to attention budgets: the LLM, like a Sim walking a lot, evaluates what's on offer
before it reads how anything works. The two dispatch paths survive intact: the LLM scoring
advertisements in context is Find Best Action (autonomy); a human browsing a CARD and picking an
action is the pie menu (direct manipulation). And the scoring got the same upgrade Drescher's
schemas got: The Sims scored advertisements with arithmetic over motive curves, MOOLLM scores
them with a reader that understands the *situation* — procedural scoring generalized to semantic
scoring, with the numeric `score:` kept as the prior.

The through-line is personal and literal: pie menus in The Sims and advertisements-as-interfaces
both trace to the same hands that built TNT's pie menus and HyperLook (see the NeWS lineage
below) — and Will Wright's advertisement architecture was right in 1996 for the same reason it's
right for LLMs now: **put the dispatch information on the object, in the vocabulary of the
chooser.**

## Reflection is cheap, and that changes behavior

Ungar's point: in a classy language reflection is metaprogramming; in Self it's slot access. In
MOOLLM it's opening a file. "What was the author thinking?" is one file open —
a META-PLAN slot if reified, an absent file (itself information) if not. Because reflection is
cheap, it actually happens. See the constellation model in
[cauldron META-PLAN §1](../../skills/cauldron/META-PLAN.md): reify what's there; absence is
honesty, not a gap.

## Naming and structure as reflection — guiding the LLM's program counter

The conventions aren't housekeeping; they're the **self-describing interface, property, and
capability mechanism**. In a system whose interpreter is a reader, *what things are named and
where they sit* is the dispatch table. Every convention below answers the same question: **what
should the LLM look at next?**

**The hierarchy is the object graph.** Directories nest the way objects contain: repo → area →
skill/room/character → instances → sessions. Containment doubles as inheritance scope — a room's
contents perform in its context, a skill's `examples/` inherit its discipline. The path IS the
identity ([cauldron's `identity_through_location`](ANNOTATED-BIBLIOGRAPHY.md#cauldron-card--identity-through-location-and-the-patron)),
so the hierarchy is also the namespace, the ownership model, and the cd-able world.

**Filenames are K-lines.** From [yaml-jazz](../../skills/yaml-jazz/GLANCE.yml): well-written
filenames are LLM-recognizable activation keys, and **the directory listing IS the advertisement
index — Sims-style "what's available here?"**. `ls` is reflection (the slot dump), but it's also
*attention guidance*: like a Sims object advertising "I satisfy hunger" to passing Sims, a
well-named file advertises what reading it will satisfy. Will Wright was right in 1996 —
advertisement-based dispatch scales, and here the advertisements are free because the names had
to exist anyway.

**Big-endian naming** ([skills/skill CARD, `directories_as_interests`](../../skills/skill/CARD.yml)):
most significant component first — `2026-01-24-description.yml` groups by time, `RUN-001-name.yml`
by sequence, `CARD.yml` by type. Sorted `ls` output becomes a semantic outline for free. The
counter-examples are instructive: `example1.yml` advertises nothing; `fluxx-amsterdam-001.yml`
buries the identifier.

**UPPERCASE is interface, lowercase is content.** The casing convention is the type system:
`SKILL.md`, `CARD.yml`, `GLANCE.yml`, `ROOM.yml`, `CHARACTER.yml` declare *what this directory
responds to* (the QueryInterface reading above); lowercase files are the stuff itself. Duck
typing by filename — [file-system-object](../../skills/file-system-object/SKILL.md) calls it
quack-quack typing: a directory is an object to the degree its marker files quack, and a bare
`CARD.yml` alone is already dispatchable (methods, advertisements, k-lines, navigation all work).

**The pyramid is the reading order — and reading order is method dispatch.** GLANCE (is this
relevant?) → CARD (what can it do?) → SKILL (how does it work?) → README (why was it built?),
never loading a lower level without the one above. This is a **semantic mipmap**: the same
object pre-rendered at every level of detail, exactly as graphics hardware stores a texture at
1×1, 2×2, 4×4… so a distant surface never pays for texels it can't resolve. A skill glimpsed
from across the corpus samples the 70-line GLANCE; walk right up to it and you page in the
1000-line SKILL — and like GPU mip selection, the level is chosen by *distance to the object*
(how central it is to the current task), not by what happens to be loaded. The pyramid is
designed to guide LLMs exactly as much as people, because both readers share the same
constraint: a limited token-and-attention budget that must never be spent rendering detail the
query can't see. It's also the attention-budget analog of first-match-wins delegation: most
queries resolve at GLANCE depth and never page in the rest. The LLM's "program counter" moves
through the corpus guided entirely by names, listings, and mip levels — which is why MOOLLM
needs no registry, no index server, and no schema catalog. The structure is the schema; the
names are the query planner; the pyramid is the LOD system.

**`goto` for attention: `lookto` and `thinkto`.** In a von Neumann machine, `goto` transfers
control. In a machine whose interpreter is a reader, the transferable resource is attention —
so the jump instructions are different. A **`lookto`** is an attention jump with I/O: a name,
listing, or advertisement moves the program counter to a file or directory and pages content
in. A **`thinkto`** is the latent-space jump, no I/O at all: a K-line — "Self's object
system," "US5187786A," "a taco, overflowing" — lands the program counter somewhere in the
training data instead of somewhere on disk. Every convention in this section compiles down to
one or the other: big-endian names and marker files emit `lookto`s; K-lines emit `thinkto`s;
the pyramid decides how *far* a `lookto` pages in. Dijkstra taught that `goto` is harmful
because unstructured control flow can't be audited — the conventions here are exactly the
structured-programming discipline for attention jumps: named, sorted, levelled, greppable.
And The Sims' advertisements are the missing third instruction, the one INTERCAL proposed as
a joke: **`COMEFROM`**. An advertisement is control transfer declared at the *destination* —
the stove announces "come to me when hungry" and the scheduler decides who actually comes.
`COMEFROM` is madness in deterministic code, which is why INTERCAL had it; with procedural
scoring arbitrating the candidates it becomes the right primitive for an attention economy —
a *weighted* `COMEFROM`, which is what a directory listing full of well-named files is. The
gradient all three instructions follow has an established name: **information scent**, from
Pirolli and Card's information-foraging theory — developed at Xerox PARC, the same building
as LambdaMOO. Foragers follow scent cues toward information patches; well-named K-lines are
concentrated scent.

**The meta-programming ladder — and what its upper rungs emit.** Classic metaprogramming
(Lisp macros, the MOP, C++ templates) emits *code*, executed by a deterministic machine.
MOOLLM's generator stack — [cauldron](../../skills/cauldron/) plans,
[artifactory](../../skills/artifactory/) protocols, [prototype](../../skills/prototype/)
instantiation, the naming conventions above — climbs one rung higher: tools that generate
code, then **tools that generate the instructions and structures that guide code-generating
tools**. What the upper rungs emit is not an instruction stream but *attention guidance* —
plans, names, listings, pyramids, advertisements: `lookto`s, `thinkto`s, and weighted
`COMEFROM`s laid down in advance. The artifact is a bias on the object-tool's search through
latent space, which is why a well-named directory listing is metaprogramming in this system,
and why the MOP move (an object system for designing object systems) reappears here as a
plan system for designing plan-following systems. The hedge against the meta-tower failure
mode is the same as everywhere else in MOOLLM: instance-first, play-learn-lift — every rung
up must be lifted from something running below it.

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

**OpenLaszlo and instance-first programming (Laszlo Systems, 2001→).** The thread continues past
NeWS: at Laszlo Systems, Don worked with **Oliver Steele** and **Henry Minsky** (the same Henry
of the Drescher lineage above — the parents keep reappearing) on OpenLaszlo, prototype-based
LZX with push constraints. Steele's
[*Classes and Prototypes*](https://blog.osteele.com/2004/03/classes-and-prototypes/) (2004)
named the methodology this whole object system practices: **instance-first development** —
"implement functionality for a single instance, then refactor the instance into a class… This
avoids premature abstraction… It's easier to generalize from two examples than from one." The
**Instance Substitution Principle** made the refactor free: an instance can be replaced by its
own class definition without changing semantics, because instance-member and class-member
definitions are syntactically parallel — prototype-based, à la Self. **Defer abstraction until
the problem's shape is known and you have working instance prototypes in hand.** MOOLLM
institutionalized this as [play-learn-lift](../../skills/play-learn-lift/SKILL.md) (PLAY with a
concrete instance, LEARN its seams, LIFT it into a skill only when a second real caller exists),
and the Garnet doc draws the full line:
[Sketchpad → Garnet → OpenLaszlo → Svelte → MOOLLM](../GARNET-AMULET-PROTOTYPE-SYSTEM.md).
Anti-taxonomy above is the same law stated statically; instance-first is its process form.

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
