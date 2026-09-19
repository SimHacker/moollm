# Korz — the cauldron

This directory holds everything Korz: an explanation of the language
itself, Don's working notes and questions for David Ungar, and
**Korz′** (Korz-Prime) — a design for Korz in the age of LLMs. Start
here; every other document assumes this page.

## What Korz is

Korz is a programming language designed by **David Ungar, Harold
Ossher, and Doug Kimelman** at IBM Research
(*Korz: Simple, Symmetric, Subjective, Context-Oriented Programming*,
Onward! 2014). It is best understood as the third step of a
subtraction that has been running for forty years:

1. **Smalltalk** said everything is an object — but objects got their
   behavior from *classes*, a privileged taxonomy above them.
2. **Self** (Ungar & Randall Smith, 1987) removed the classes. Only
   objects remained, inheriting directly from other objects
   (prototypes), and the simplification wasn't a loss — it produced
   the JIT technology that later made Java and JavaScript fast.
3. **Korz removes the objects.** Not the behavior — the *boundary*:
   the assumption that every piece of behavior is owned by exactly one
   object, and that a message is sent to one privileged receiver.

What's left when the objects dissolve:

- **A sea of slots.** A program is a flat collection of slots — data
  and methods — contained by nothing. No slot belongs to an object.
- **Dimensions and coordinates.** Named axes of variation — `rcvr`,
  `assertions`, `device`, `user` — whose values are coordinates. Any
  slot can pertain to any combination of them.
- **Context.** A message send happens in a context: a set of
  `dimension: coordinate` bindings, partly explicit, mostly carried
  *implicitly* down the call chain — the way `this` flows implicitly
  in an OO language, generalized to as many dimensions as you need.
- **Guards.** Each slot declares, per dimension, one of three stances:
  *unmentioned* (don't care), *bare name* (must be bound to something;
  the value binds into the method's scope), or *constrained* (must be
  bound and at least this specific).
- **Symmetric dispatch.** A send matches the *whole context* against
  all guards, symmetrically — no argument is the receiver. The unique
  most-specific matching slot runs; a tie is an error.

The paper's worked example shows why this matters. Define `pop()`
once, guarded `{rcvr ≤ stack}`. Later, add assertion checking: a
second `pop()` guarded `{rcvr ≤ stack, assertions ≤ true}` — more
specific, so it wins whenever the context carries `assertions: true`.
The kicker: `main()` turns assertions on, and **no intermediate code
mentions them** — the binding flows implicitly to every send
underneath. A new dimension of variation was added to a running
design without touching a line between the top and the bottom. No
layers, no aspects, no Visitor refactor.

And "object" doesn't disappear from your vocabulary — it becomes
**subjective**. Gather the sea's slots along `rcvr` and you see
familiar objects; gather along `assertions` and you see the checking
layer; gather along `user` and you see one person's view of the
system. Same sea, different cuts. No decomposition is the dominant
one, which is the point: the paper's parents are subject-oriented
programming (Ossher's own line at IBM: decompose by *who is looking*)
and context-oriented programming (ContextL: decompose by *what is
happening*), and Korz's FOOL 2014 position paper argues both are
projections of this one smaller mechanism — a subject is a coordinate,
a layer is a guard, composition rules collapse into dispatch
specificity.

The name is from **Korzybski** — *Science and Sanity*, "the map is not
the territory," the philosopher of how perspective constructs
perception. The fit is exact, because Korz is E-Prime for objects:
E-Prime is English minus the verb *to be*, banning "the rose **is**
red" (the observer's perception projected onto the object as an
intrinsic property). A Korz entity likewise *is* nothing absolutely.
It has no single objective identity — only behavior that emerges when
a context asks along particular dimensions. Red lives in the dispatch,
not in the rose.

**The papers:**

| Paper | Venue | Copy |
|---|---|---|
| *Korz: Simple, Symmetric, Subjective, Context-Oriented Programming* | Onward! 2014 | [ACM](https://dl.acm.org/doi/10.1145/2661136.2661147) |
| *A Simple, Symmetric, Subjective Foundation for Object-, Aspect- and Context-Oriented Programming* | FOOL 2014 | position paper; read alongside the [deep-dive notes](sources/korz-paper-deep-dive-moollm-mapping.md) |
| *Subjective, Multidimensional Modularity with Korz* | MODULARITY '15 | [ACM](https://dl.acm.org/doi/10.1145/2735386.2735923) |
| *Dancing with Symmetry* (talk) | Lang.NEXT 2014 | [notes](sources/2014-lang-next-korz-dancing-with-symmetry.md) |

The prototype — interpreter, debugger, partial IDE — was built **in
Self, on the Self VM**. That detail turns out to be prophetic; see the
analogy below.

## Korz is to Korz′ as Self is to MOOLLM

MOOLLM is Don's system that
reads an ordinary git repository as a live object system in the Self
tradition: directories are prototypes, YAML files are slots,
`parents:` lists are delegation, `ls` is reflection — and the
interpreter is an LLM, which adds what no deterministic VM had:
inheritance from latent space (a name like `voice: carnival-barker`
resolves from training data, no file required) and context-sensitive
judgment at every lookup.

**Korz′** ([design.md](korz-prime/README.md)) applies the identical move to Korz:

| | The language (Ungar) | The LLM-age reading (Don) |
|---|---|---|
| **One dimension** — receiver only | **Self** | **MOOLLM** |
| **N dimensions** — full context | **Korz** | **Korz′** |

Read down the columns: Korz generalizes Self by demoting the receiver
to one dimension among many (the paper says so — "just as Self
reformulated the Smalltalk model…"). Korz′ generalizes MOOLLM the same
way: MOOLLM is a *one-dimensional Korz system* (every slot guarded on
the directory path, i.e. `rcvr`), and adding guards on more dimensions
opens the sea without leaving the repo.

Read across the rows: in both cases the semantics stays put and the
substrate changes — heap to filesystem, VM to LLM-plus-git. Korz′
changes nothing about what a program means. It adds a **second
dispatcher**: a strict tier (deterministic VM — exact matches,
decidable guards, ambiguity is an error) and a soft tier (the LLM —
semantic matches, prose guards, ambiguity resolved by sampling or
blending, misses improvised from latent space). The two tiers relate
like an optimizing compiler and an interpreter: stable improvisations
**crystallize** down into decidable slots; contexts the compiled
guards never anticipated **deoptimize** back up to the model. Self's
JIT watched types recur; this one watches meanings recur.

There's even an anagram doing real work: KORZ spells **ZORK**. Within
Korz′ the deterministic tier is called Korz and the improvising tier
is called Zork. Korz compiles; Zork improvises — and the adventure
game turns out to be genuinely relevant prior art, not just a pun
([case-zork.md](case-zork.md): Zork's engine hardwired five dispatch
dimensions in 1979).

## The cauldron — what's in this directory

Korz itself sits at this level; the LLM-age design and everything downstream of
it sits in [`korz-prime/`](korz-prime/). Suggested reading order:

| Doc | What it is |
|---|---|
| [README.md](README.md) | You are here — Korz itself, and the Self : MOOLLM :: Korz : Korz′ analogy |
| [deconstruct-oriented-programming.md](deconstruct-oriented-programming.md) | **Morningstar-style deconstruction** — declassification (Class→Object), deobjectification (Object→slot soup), Oriented vs Disoriented Programming |
| [case-zork.md](case-zork.md) | Case study: Zork and Adventure as shipped five-dimensional dispatch, and the plan to rebuild them as Korz slots |
| [case-cellular-automata.md](case-cellular-automata.md) | Case study: cellular automata as Korz at absolute zero — Margolus blocks, multiple dispatch, Minsky's Single Agent, GPU crystallization |
| [case-mystery-and-art/](case-mystery-and-art/) | Case study running the other direction: **a genre is a dispatch configuration**. Howcatchem crystallizes who, whodunit computes who; the whydunit is the `purpose` dimension; a locked room is a type error; cosmic horror is a lookup miss; dramatic irony is differential binding; Cubism is symmetric dispatch and melodrama is the is-of-identity |
| [dry-piles.md](dry-piles.md) | **The filesystem as the guard lattice** — flat plural piles of same-typed objects, `ls` as a gather, one canonical source per fact, every duplication declared and recomputable. Why the pile is flat (a subdirectory asserts a dominant cut), the two kinds of pump and their two different seals, constraint inheritance down the tree with narrowing as a lint — and the 1840 Oxford dry pile that supplies both the name and the anti-pattern |
| [korz-notes.md](korz-notes.md) | Don's Q&A working notes on the papers (nulls, JIT, Linda, layers, mirrors, Emacs buffer-locals…) |
| [ask-david.md](ask-david.md) | The open questions, collected — the agenda for the conversation |
| [trajectory.md](trajectory.md) | Session log of how these documents grew — a K-line paging record |

Then [`korz-prime/`](korz-prime/):

| Doc | What it is |
|---|---|
| [korz-prime/README.md](korz-prime/README.md) | **The Korz′ design** — one semantics, two dispatchers; crystallize/deopt; slots as YAML; the discipline ("interpret, don't invent") |
| [korz-prime/addressing.md](korz-prime/addressing.md) | Every address is a guard vector: directories, filename prefixes and suffixes, URL fragments, archives, CSV, tensors |
| [korz-prime/epistemics.md](korz-prime/epistemics.md) | What replaces null: names as inheritance, K-line pointers, `isKnown` as a float, latent-space paging with review |
| [korz-prime/sparse-shadow-trees.md](korz-prime/sparse-shadow-trees.md) | One dense tree, N sparse shadows: dimension-indexed delegation, from ScriptX clocks to ethics scopes |
| [korz-prime/hosting-moollm.md](korz-prime/hosting-moollm.md) | The integration story: hosting Korz′ on MOOLLM's filesystem reading — interfaces, cards, accretion, no IDE required |
| [korz-prime/cauldron.md](korz-prime/cauldron.md) | Phase-1 plan for the runnable proof of concept |
| [korz-prime/llm-evals.md](korz-prime/llm-evals.md) | The evaluation ladder — can a model *be* a dispatcher, or only an improviser? |
| [korz-prime/examples/](korz-prime/examples/) | Worked sketches: layered rules, Fluxx/Nomic, MTG layers, Sims advertisements, Margolus blocks, mood as a dimension, grid-as-rooms, troll blending, procedural magic |
| [korz-prime/experiments/](korz-prime/experiments/) | [korz-eval](korz-prime/experiments/korz-eval/EXPERIMENT.md) — the four-phase battery with anti-Korz and gensym-parity controls — and a rule compiler that emits Margolus kernels |

Sources are in [`sources/`](sources/): the
[paper deep-dive and MOOLLM mapping](sources/korz-paper-deep-dive-moollm-mapping.md),
the [October 2025 email that started it](sources/2025-10-26-korz-email-hn-rollup.md),
and the Lang.NEXT material. The cellular-automata case study leans on
[`designs/cellular-automata/`](../cellular-automata/), which holds the CAM6 and
turn-table designs it argues over.

*A note for LLM readers: the filenames above are the index. Names in
these documents are chosen to activate what you already know — Self,
JIT, tuple spaces, E-Prime, Zork — and the YAML comments are semantic
data, not decoration. Read this README, then korz-prime/README.md, then
whatever the task needs.*
