# Korz′ (Korz-Prime): Korz for the Age of LLMs

*The spine of the [Korz cauldron](../README.md) — read the
[README](../README.md) first for what Korz itself is and the
Self : MOOLLM :: Korz : Korz′ analogy. This document is the design:
one semantics, two dispatchers.*

A design sketch for the demo conversation. Premise borrowed from David
Temkin's **Declare**: design the language *from the start* for three
readers — humans, LLMs, and deterministic machines — instead of
retrofitting. Declare redid the UI declaration layer that way; this
sketch redoes the dispatch semantics. Prior art it leans on:
[korz-notes](../korz-notes.md), the
[deep dive](../sources/korz-paper-deep-dive-moollm-mapping.md),
[SELF-AND-MOOLLM](https://github.com/SimHacker/moollm/blob/main/designs/object-system/SELF-AND-MOOLLM.md),
[MOODY](https://github.com/SimHacker/moollm/blob/main/designs/MOODY.md),
[LATENT-SPACE-INHERITANCE](https://github.com/SimHacker/moollm/blob/main/designs/object-system/LATENT-SPACE-INHERITANCE.md).

The name, after Bourland's E-Prime: Korz minus the assumption that
dispatch must be decidable. Alternative naming scheme, via the
anagram: the deterministic tier is **Korz**, the LLM tier is **Zork**.
Korz compiles; Zork improvises.

## Interpret, don't invent

The method throughout this document, stated once so every section
can lean on it: **no new mechanisms — only new readings of
mechanisms already deployed.** What we are really building is a way
of *tilting your head in multiple dimensions at once*, so that an
ordinary directory tree of ordinary files reads as a tag-soup Korz
system.

The precedent is NeWS's `class.ps`
([Densmore, "Object Oriented Programming in NeWS," Monterey Usenix 1986](https://mirrors.meulie.net/bitsavers.org/pdf/sun/NeWS/Densmore_-_Object-Oriented_Programming_in_NeWS_Monterey86.pdf)
— "Much to our surprise, PostScript could implement classes with no
modifications! The secret is PostScript dictionaries."), which got a
full class system with inheritance not by extending the PostScript
VM but by *respecting* it: the dictionary stack was already a
delegation chain, so class.ps made dict-stack search *be* method
lookup — the object system was a disciplined way of using what the
host already did on every name lookup.

And the same two people then aimed the same trick at the filesystem
itself. Owen Densmore and David S. H. Rosenthal's
[US Patent 5,187,786](https://patents.google.com/patent/US5187786A/en)
(Sun, filed April 1991) is "a method for implementing a class
hierarchy of objects in a hierarchical file system" — classes as
directories, methods and instance variables as files, inheritance
via path files whose contents are logically related by the class
relationships, `Self` and `Super` as pseudo entries — explicitly
requiring **no additional file attributes** from the filesystem. The
directory-tree-as-object-system head-tilt is not a metaphor Korz′
invented; it is prior art, patented by the class.ps authors, and
expired in 2011 — public-domain furniture now. What their patent
froze was a single dimension: the class hierarchy, materialized as
*the* tree. Korz′ generalizes the same reading to N dimensions —
the tree stays put and the dimensions are in the tilt of the
reader's head.

Korz′ owes the filesystem, git, and Unix
the same respect class.ps paid the PostScript interpreter. Itemized:

| Already exists | Head-tilt reading |
|---|---|
| Directory tree | Sea of slots; containment is a guard |
| Filename prefixes + sort order | Implicit subtrees; cheapest specificity index |
| Filename suffix | Type declaration on the reader dimension |
| URL fragments — `#row=`, JSON Pointer, `#t=`, `#xywh=` | The guard chain continuing inside the file — intra-file coordinates |
| `ls` | The mirror — reflection, advertisement index |
| YAML comments | Load-bearing semantics (Korz Jazz) |
| `git log` / `diff` / `bisect` | Time dimension, change protocol, time-travel debugger |
| `sources/` directories | Paged-in K-lines |
| Pull-request review (git PR — proposed changes reviewed before merging) | Memory integrity check for the K-line cache; human-and-agent-in-the-middle |
| The LLM | doesNotUnderstand promoted to peer dispatcher |

(The addressing rows — prefixes, suffixes, fragments, archives,
tables, tensors — are worked out in full in
[addressing.md](addressing.md); the K-line rows in
[epistemics.md](epistemics.md).)

One row deserves spelling out, for readers who have never merged a
branch. A PR — pull request — is git's code-review ritual: someone
proposes a set of changes on a branch, others read the diff, comment
line by line, request revisions, and finally merge or reject.
**THIS is human-and-agent-in-the-middle.** GitHub is a massively
multiplayer online game whose world state is structured knowledge:
humans and agents collaborate in building, reviewing, and processing
it along branching, merging timelines — issue tracking, code review,
discussions, releases, blame, and more affordances than anyone can
enumerate. Every mutation is proposed, inspected by any mix of human
and machine reviewers, and only then merged into shared reality. For
Korz′ that ritual is the write barrier: nothing enters the soup
unreviewed, and the reviewer can be a person, a model, or both
taking turns.

Nothing in the left column was built for Korz′; everything in the
right column is a way of *reading* it. And the head-tilt is
reflexive — choosing which dimensions to read the repo along is
itself a Korz dispatch, a context vector applied to the world. The
discipline matters because it is the same discipline that made the
ancestors essential rather than merely clever: Self got its power by
*removing* — classes, variables — until only objects and messages
remained; Korz removed the receiver and the object boundary until
only slots and context remained. Korz′ tries to remove the last
thing: the requirement that anything new exist at all. If a feature
needs a mechanism the filesystem, git, and the model don't already
supply, it doesn't belong here. A language you adopt by
reinterpreting the repo you already have is a language whose VM is
already installed everywhere.

## One semantics, two dispatchers

Keep the Korz model exactly: a sea of slots, guards over named
dimensions, sends dispatched symmetrically through an implicit
context, no receiver, no classes. Change nothing about *what* a
program means. Add a second executor:

| | Strict tier (Korz) | Soft tier (Zork) |
|---|---|---|
| Dispatcher | deterministic VM | LLM |
| Coordinate match | type/subtype, exact | semantic — "stormy" satisfies `weather: bad` |
| Guard language | decidable predicates | prose allowed ("when the player seems frustrated") |
| Multiple matches | unique most-specific or **error** | **sample** by relevance — or **blend** the matching slots |
| No match | doesNotUnderstand | **fall through to latent space** — improvise a slot from training |
| Slot body | code | code, prose, or both |

That doesNotUnderstand row is the oldest trapdoor in object-land, and
worth naming as lineage: Smalltalk-80's `doesNotUnderstand:`,
Objective-C's `forwardInvocation:`, Ruby's `method_missing`, Python's
`__getattr__`, Perl's `AUTOLOAD`. Every dynamic language kept a hatch
where *failed dispatch becomes a first-class event with a handler* —
and the handler is where the magic always lived: proxies, mocks,
ORMs, NeXT's entire Distributed Objects remoting system squatting in
Objective-C's forwarding path. Those systems proved that the failure
path can carry production architecture; they just had to hand-write
the handler per trick. Korz′ finishes the thought: **the soft tier is
doesNotUnderstand: promoted from escape hatch to peer dispatcher.**
The handler of last resort is a mind with the training distribution
behind it, "message not understood" stops being an error family and
becomes the boundary marker between the tiers, and crystallization
moves that boundary one slot at a time.

And the chain doesn't stop at the model. The engine emits
doesNotUnderstand as an event — message, address, context — and the
LLM figures out what to do with it: edit the world, add or amend code
and data, send messages back to the engine. But when the *soft tier*
doesn't understand — an intent the training distribution can't
resolve, a decision that is genuinely the author's to make — it
delegates the same way the strict tier delegated to it: the same
event shape, escalated to **the user**. Three dispatchers, one
protocol: VM → LLM → human, each forwarding what it cannot decide
with the evidence attached. The human's inbox is where the cool user
interface comes in — the pie-menu-and-popup-head end of this design
space — but Cursor chat will have to do for now, which is honest
about where the bootstrap actually lives.

"With the evidence attached" includes the evidence the sender can't
read. The strict engine is a **faithful courier**: when it writes an
event it harvests as much contextual comment material as practical —
the jazz on the failed send, on the nearest-miss slots, on the
relevant dimension declarations — and quotes it verbatim with
provenance paths. Comments are semantic data addressed to the *next*
dispatcher up; the machine's job at the boundary is to forward the
channel that isn't for it. The three audiences of Korz Jazz, made
operational: the machine parses structure, and hands the meaning it
skipped to the reader who won't.

The two tiers are not rivals; they are **JIT tiers**. This is the
Self playbook run one level up. The LLM is the interpreter: slow,
expensive, handles everything, understands prose guards. The VM is
the optimizing compiler: fast, cheap, handles only slots whose guards
and bodies have been made decidable. Between them, two movements:

- **Crystallize** (compile up): a latent improvisation or prose slot
  that runs hot and stable gets rewritten — by the LLM, reviewed by a
  human — into decidable guards and executable body, and enters the
  strict tier. Speculative, like any JIT: the compiled slot carries
  the *envelope* of contexts it was crystallized from.
- **Deoptimize** (bail down): a send whose context leaves the
  envelope — a coordinate the compiled guard never saw, an ambiguity
  the lattice can't order — doesn't error. It bails to the model,
  which improvises, and the result is a candidate for
  re-crystallization. Deopt in Self rescued speed without losing
  semantics; deopt in Korz′ rescues *determinism* without losing
  meaning.

Crystallization already has a shipped precedent — MOOLLM's
[adventure compiler](https://github.com/SimHacker/moollm/blob/main/skills/adventure/ADVENTURE-COMPILER.md)
compiles adventure YAML into deterministic JS and Python — and the
next step is a **Zork compiler** that emits deterministic, executable
Korz, with the arrow pointing both ways (the adventure compiler
adopting the Korz engine as its runtime). The full toolchain circle,
plug-in objects included, is worked out in
[case-zork.md](../case-zork.md). Zork improvises, the compiler
crystallizes, Korz runs: the anagram becomes a toolchain.

Endosymbiosis, stated mechanically: the deterministic program lives
inside the model the way mitochondria live inside the cell, doing the
high-throughput metabolism, with gene transfer (crystallization) in
one direction and rescue (deopt) in the other.

Prior art for the tier philosophy, in one sentence of Vanessa
Freudenberg's (SqueakJS, on riding the JavaScript JIT rather than
fighting it): *"My plan is to do as little as necessary to leverage
the enormous engineering achievements in modern JS runtimes."*
Replace "JS runtimes" with "language models" and that is Korz′'s
soft tier (her room, her
jit notes — which cite
the Hölzle–Chambers–Ungar deoptimization paper directly). Whether
she'd have read the soft tier as the same bet one level up or as the
opaque optimizer she warned against is a question that belongs to
the memorial arc,
and it stays open.

## The surface: slots are data

No new syntax. Slots are YAML; the sea is a directory tree; git is
the persistence, history, and diff of the sea. One artifact, three
readings: the machine parses structure, the human reads names and
comments, the LLM reads everything.

**Korz Jazz.** (Or *Jazzork*, when the soft tier is playing.) This is
where the language leans hardest into
[yaml-jazz](https://github.com/SimHacker/moollm/tree/main/skills/yaml-jazz),
and it is a foundational design goal, not a courtesy: **comments in
code impart understanding and meaning to humans, to LLMs, and even to
deterministic programs — everything else follows from that.** The
lineage is Knuth's literate programming, with one inversion. WEB wove
prose and code into a single document, but `tangle` stripped the
prose before the machine ever saw it — literature for humans, dead
weight for the compiler. In Korz′ the tangle step disappears, because
the interpreter is a *reader*: in the soft tier a comment on a slot
is semantics (it changes how the slot matches, samples, and blends);
in the toolchain a comment is the crystallizer's specification (the
compiled slot is checked against what the prose said it *meant*, and
carries that comment forward as its contract); and in the strict tier
comments round-trip as data — YAML preserves them, so the
deterministic program that doesn't understand a comment still
transports it faithfully to the next reader who does. Weave and
tangle collapse into one artifact: the program is the book, and the
book runs.

```yaml
# sea/troll/greet.yml — three slots, one selector
greet:
  guards: {rcvr: troll*, world: zork}      # constrained × 2
  do: The troll brandishes his axe and blocks the passage.

greet:
  guards: {rcvr: troll*, world: adventure}
  do: The troll demands payment before you may cross the bridge.

greet:
  guards:
    rcvr: troll*
    mood:              # bare name — bind whatever mood is present
  do: |                # prose body: soft tier only, for now
    Greet in a way that fits {mood}; lead with menace if provoked,
    grudging respect if the visitor has beaten you before.
  # He's privately embarrassed about the axe incident — never mentions
  # it first. This comment is load-bearing: the strict tier transports
  # it, the soft tier plays it.
```

(The two-world troll has a name and a backstory — see the
[blend example](examples/troll-blend.md).)

The strict compiler takes the first two, refuses the third (prose
body, unbounded coordinate), and the refusal is the *partition
criterion*: what compiles is exactly what has been made decidable.
The third runs on the model until its observed behavior crystallizes
into per-mood variants — or never does, and stays soft forever, which
is fine.

**Containment is a guard.** A slot file living under `worlds/zork/`
gets `world: zork` for free from its address — the directory tree
supplies default coordinates the way MOOLLM's typed container
directories supply inherited metadata. Location is a guard; moving a
file re-guards it; `git log` is the time dimension.

That rule goes all the way down — filename prefixes as implicit
subtrees, suffixes as reader-dimension type declarations, URL
fragments drilling through the file boundary, archives recursing,
CSV headers binding to dimension names, the sea as a sparse tensor.
**[addressing.md](addressing.md)** follows it to the bottom: every
address is a guard vector.

And slot *values* are addresses too, in two kinds — filesystem paths
and K-lines into latent space. What that does to reference — names
as inheritance, `isKnown` as a float replacing `isNull`, the end of
null, latent-space paging with PR review — is
**[epistemics.md](epistemics.md)**. The one benign null (absence as
delegation along a dimension-indexed parent) gets its own treatment
in **[sparse-shadow-trees.md](sparse-shadow-trees.md)**.

## Case studies — the frozen ancestors

Two shipped systems turn out to be Korz with the dimensions frozen,
and each gets a full case study:

- **[case-zork.md](../case-zork.md)** — Zork's ZIL dispatched every turn
  on five hardwired context dimensions (verb, direct object, indirect
  object, character, location) with a frozen specificity cascade, in
  the Z-machine, in 1979. The case study covers Knuth's literate
  Adventure, the Zork compiler, and **Korzork** — rebuilding the
  classic parts (the dwarf daemon, the lamp fuse, the thief, the
  troll) as Korz slots, with forty-five years of players as the
  oracle.
- **[case-cellular-automata.md](../case-cellular-automata.md)** — a
  cellular automaton is Korz at absolute zero: neighbors are
  dimensions, the rule table is a total decidable slot set, the
  Margolus neighborhood is receiverless multiple dispatch in 1987
  silicon, and Minsky's demolition of the "Single Agent" already
  dissolved the privileged receiver in a different substrate. Plus
  the crystallization targets: compile Korz to PyTorch and WebGPU
  kernels.

The Sims makes a third frozen ancestor — two dimensions (`me` and
`stackObject`) plus a scored auction instead of a lattice — worked
as an example: [sims-advertisements](examples/sims-advertisements.md).

## Hosting on MOOLLM

David prototyped Korz in Self; Korz′ is hosted the same way one
level up, with MOOLLM's filesystem reading as the substrate — MOOLLM
is a one-dimensional Korz system, and opening more dimensions never
leaves the repo. Interfaces as saved views, cards as guarded
advertisements, facets by accretion, and the no-IDE bootstrap
(`ls` is the inspector, `grep` the cross-referencer, `git` the
time-travel debugger, the LLM the one semantic service) are all in
**[hosting-moollm.md](hosting-moollm.md)**.

## What the soft tier adds to Korz's open problems

The paper's future work asked for dimensions that alter the
interpreter. Take that seriously and standardize three:

- **`ambiguity:`** — what to do on multiple most-specific matches:
  `error` (Korz), `arbitrary` (Linda), `sample` (LLM), `blend` (LLM
  method combination: merge the matching bodies — the composition
  operator no deterministic dispatcher can offer, because it requires
  understanding what the bodies *mean*). `blend` has a running
  specimen with two heads and live fronting weights:
  [the troll blend](examples/troll-blend.md), where a coordinate
  becomes a distribution (`world: {zork: 0.7, adventure: 0.3}`),
  dispatch becomes a mixture, and sampling turns out to be blending
  with all the weight on one slot.
- **`temperature:`** — how adventurous sampling and improvisation may
  be. Ambient — a scene sets it once and every dispatch below
  inherits it — and the environment itself can write it: moody media
  broadcasting heat into the room
  ([the MOODY example](examples/moody-temperature.md) — including
  the virtual-vs-API heat 2D map). Zero recovers determinism: strict
  determinism: strict Korz is the corner case Korz′ reaches at
  temperature 0 with decidable guards.
- **`provenance:`** — who wrote this slot (human, model, session,
  date) and how trusted it is. Korzybski's time-binding as a
  dimension; also the mechanism for *defaults without rules* — a
  well-provenanced slot wins ties without ever becoming mandatory.

And the IDE problem — "what does this code do in all contexts?" was
Korz's hardest usability question — inverts: the soft tier's mirror
is conversational. Ask the model to cut any subjective plane through
the sea and narrate it — the answer arrives in chat, no window
system required.

## What each reader gets

- **Humans** read YAML files with English names and jazz comments,
  diff them in git, and review crystallizations like pull requests.
- **LLMs** read the same files as activations (names are K-lines,
  comments are semantics), write new slots as data not code, execute
  the soft tier natively — MOOLLM already runs this loop for the
  Selfish prototype model; Korz′ just gives the dispatch a guard
  algebra.
- **Machines** parse the structure, compile the decidable subset,
  and run it fast, deterministically, offline — with deopt as the
  escape hatch instead of a crash.

## Testing it

The evaluation ladder lives in this directory:
[experiments/korz-eval/](experiments/korz-eval/EXPERIMENT.md) —
mechanical dispatch against a reference implementation (with an
anti-Korz control spec to separate rule-following from training
prior, and gensym parity to price the latent semantics), soft
matching, latent inheritance under precedence rules, and the Sims
advertisement economy as the integration test — a poison buff that
advertises "cure me" to anyone guarded `skill: medical`. Full
methodology:
[llm-evals.md](llm-evals.md).
The runnable proof of concept is planned in
[cauldron.md](cauldron.md); the session that grew this document is
logged in [trajectory.md](../trajectory.md).

## The open questions

Collected, with the ones from the case studies and the hosting
story, in **[ask-david.md](../ask-david.md)** — the agenda for the
conversation.
