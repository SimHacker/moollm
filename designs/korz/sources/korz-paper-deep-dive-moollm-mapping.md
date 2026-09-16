# Korz — paper deep dive and the MOOLLM mapping

*Analysis of published papers, prompted by Ungar's own pointers (Oct 2025
rollup, and again Aug 2026: "the same entity behaving differently in
different situations... Don't know if it relates"). It relates.
Portrayal standards.*

| Field | Value |
|---|---|
| Papers | *Korz: Simple, Symmetric, Subjective, Context-Oriented Programming*, Ungar, Ossher, Kimelman — Onward! 2014 ([local PDF](https://dl.acm.org/doi/10.1145/2661136.2661147), [ACM](https://dl.acm.org/doi/10.1145/2661136.2661147)); *Subjective, Multidimensional Modularity with Korz*, MODULARITY Companion '15 ([DOI](https://dl.acm.org/doi/10.1145/2735386.2735923)); *A Simple, Symmetric, Subjective Foundation for Object-, Aspect- and Context-Oriented Programming*, FOOL 2014 (local PDF) |
| Lineage | Us (Smith & Ungar's subjective language) grown symmetric and multidimensional; SOP (Harrison & Ossher '93) made dynamic — same Ossher, composing at dispatch time instead of build time |
| Implementation | Prototype interpreter, debugger, and IDE built **in Self, on the Self VM** |
| First pointer | [Oct 2025 email rollup](2025-10-26-korz-email-hn-rollup.md) — "the natural extension of Self to multidimensional (context \| subjectivity)" |

## The name

The Onward! '14 paper, Appendix A, "The Name":

> The name "Korz" comes from Korzybski, whose *Science and Sanity*
> (Korzybski 1933) explained how much one's perspective influences one's
> perceptions and thinking.

Alfred Korzybski, general semantics: **the map is not the territory.** A
language of subjective objects, named for the philosopher of how
perspective constructs perception. (Korz is also an anagram of Zork —
same four letters, *not* a reversal; Korz backwards is "Zrok." Don's
observation, unremarked in the published record — and apt: adventures
and games are where subjective dispatch earns its keep; see
[Don's Korz notes & Q&A](../korz-notes.md).) Two Korzybski
resonances worth keeping: MOOLLM's rebuttal to the map/territory slogan
is that the map *can* be the territory if you make the map a directory —
the [Cross-Platform Troll's soul realms](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/fictional/troll/realms)
are maps of Zork and Adventure that are navigable territories inside him.
And Korzybski's **time-binding** — humans as the class of life that
transmits knowledge across generations through symbols — is the repo-show
thesis, stated in 1933.

## The model in five sentences

Korz combines **implicit arguments** and **multiple dispatch** in a
**slot-based model**. There are no objects: a system is a *sea of slots*
in a multidimensional space, and a slot pertains to any number of
**coordinates** (pure identities) along named **dimensions** rather than
being contained by one object. A message send happens in a **context** —
a set of dimension:coordinate pairs, partly explicit, partly carried
implicitly through the call chain — and dispatch picks the most specific
slot whose **guard** matches the whole context. Slots gather into
"objects" *subjectively*, per situation: the same sea groups one way
along `rcvr`, another way along `assertions`. No dominant decomposition;
no dimension outranks any other.

The worked example: `pop()` defined once with guard
`{rcvr <= stackParent}`; assertion checking added later as a second pop
guarded `{rcvr <= stackParent, assertions <= true}` — more specific, so
it wins when the context carries `assertions: true`. The kicker:
`main()` never mentions assertions; the binding flows through
implicitly. New dimensions of variation arrive without touching
intermediate code — no layers, no aspects, no Visitor refactor.

(Pun shelf: sea of slots → slot soup → the Sea of Holes, per *Yellow
Submarine* — where one hole leads to the Sea of Green, which is to say:
follow an unbound dimension far enough and you surface somewhere else
entirely. Ringo kept a hole in his pocket; every guard is a hole
waiting for a context to fall through it.)

### Unbound dimensions: absence is the mechanism

Does Korz handle null or empty dimensions gracefully? Gracefully is the
wrong word — **absence is the mechanism.** A context binds "some or
all" dimensions, and a guard can take exactly three stances per
dimension. *Unmentioned*: don't-care — the slot matches whether or not
the context binds it (Appendix C draws an explicit "−" don't-care
position on every dimension's axis). *Mentioned bare* (`device` with no
coordinate): the dimension must be present, any value — and it binds
into the method's scope as a named implicit parameter. *Constrained*
(`device ≤ screen`): present and at least that specific. Passing less
context degrades by construction — fewer bindings means only
more-generic slots match, down to the zero-dimensional case, which is
procedural programming.

What Korz lacks is an explicit **null coordinate**: you cannot bind
`location: none` to actively *mask* the more specific slots, or guard
on a dimension being absent. Whether that's a missing feature or a
dodged bullet is a real question. (And it's the pun made literal: an
unbound dimension is a hole in the sea of holes; Korz treats holes as
things don't-cares match, never as values you can dispatch on.)

### Mirrors: disco ball, not funhouse

The paper defines no mirror API — the IDE plays that role, cutting
planes through the symmetric slot space to present asymmetric,
subjective views. But the model dictates what reflection must become: a
mirror on a subjective object has to take a **context as a parameter**,
because "the object" doesn't exist until a context gathers its slots.
So: not a funhouse mirror (one privileged image, distorted) but a
**disco ball** — many small flat mirrors, each honest, each reflecting
from its own angle. Every facet is one context's true view; the
multiplicity is in the ball, not in any distortion. The Korz IDE is a
disco ball you rotate by hand; cursor-mirror is one facet bolted to one
orchestrator. Since Ungar co-authored the mirrors paper (Bracha &
Ungar, OOPSLA '04), the question is his to answer: *what does a mirror
reflect when the object is subjective?*

## Two parents: SOP and COP

Korz names both of its parents, and they answer a question worth asking
precisely: how does context-oriented programming relate to
subject-oriented programming?

**Subject-oriented programming** is the IBM definition — Harrison &
Ossher, *Subject-Oriented Programming: A Critique of Pure Objects*,
OOPSLA '93 (the same Ossher). The critique: there is no single objective
model of an object that serves every application. A **subject** is a
coherent perspective — its own state and behavior for shared objects —
and a system is built by *composing* subjects under composition rules.
It's symmetric (no subject is the privileged base) and it composes at
**build time**. The line continued into Hyper/J and multi-dimensional
separation of concerns (Ossher & Tarr). Aspect-oriented programming
(Kiczales, PARC) is the asymmetric cousin: a privileged base program
plus aspects woven in.

**Context-oriented programming** is Costanza & Hirschfeld's term
(ContextL 2005; the Hirschfeld–Costanza–Nierstrasz JOT 2008 paper is
the canonical statement). Behavioral variations are grouped into
**layers**, activated and deactivated dynamically, per thread, per
control flow — variation selected at **run time** by what is happening.

So SOP decomposes by *who is looking*; COP decomposes by *what is
happening*. Is SOP a case of COP? Neither contains the other cleanly —
SOP composes code statically per perspective, COP activates variations
dynamically per situation — but you can squint SOP into "compile-time
COP where the context is the application's identity." Korz's actual
answer (the FOOL 2014 position paper argues exactly this) is that both
are projections of one smaller mechanism: **a subject is a coordinate
along a viewer dimension, a layer is a guard on any dimension, and
composition rules collapse into dispatch specificity.** Symmetric
multiple dispatch over an implicit multidimensional context subsumes
both, the way Self's slots subsumed Smalltalk's classes.

## The Sims: me and the stack object

SimAntics — The Sims' behavior VM — has an implicit **`me`** (the object
running the behavior tree, like C++'s `this`) and an implicit **stack
object** (the object `me` is currently interacting with: "it").
Subject and object, hardwired into the instruction set.

The famous inversion is grammatical: **the verb lives in the direct
object.** Interactions are behavior trees stored on the thing being
used — the espresso machine carries "make espresso," and the Sim who
runs it is the subject animating a verb it never owned. Add
advertisements and you get the full sentence: objects broadcast verbs,
subjects score them each according to their own personality, motives,
and relationships.

Is The Sims subject-oriented programming in the IBM sense? Not
strictly — there's one shared behavior tree per interaction, not
per-subject composed code modules. The Sims' subjectivity lives in
**data**: every Sim scores the same advertisement differently, every
relationship matrix is one party's *opinion* of the other (deliberately
asymmetric), and personal overlays write private meanings onto shared
media ([MOODY.md](https://github.com/SimHacker/moollm/blob/main/designs/MOODY.md)).
Grammatically subject-oriented, economically subjective,
compositionally shared. In Korz terms the diagnosis is one line: `me`
and `stackObject` are **two hardwired dimensions of the dispatch
context** — a binary multimethod frozen into the VM. Korz generalizes
the same move to N dimensions and lets you add new ones after the fact.

The pronouns carry more weight than they look like they do. C++'s
`this` is a dehumanizing pointer — it points *at* a thing. Self's
`self` is humanizing — the word people use for personhood. The Sims
went first-person: `me`, with the stack object as the grammatical
direct object — "that" for the singular inanimate, "them" when the
direct object deserves personhood (it might be another Sim), and
flexibility beyond that, since pronouns are exactly where one-size
fails. And Korz's `rcvr` is *convention plus a little dot-notation
sugar*, not a privileged concept: the model would happily host a
Sims-shaped dialect with `me` and `it` (or `that`, or `them`) as two
dimensions among many. The dimension names are the pronoun system of
the language — choosing them is choosing who counts as a subject.

## Two senses of "generic" (don't conflate them)

Worth keeping straight, because both show up here and they are
different machines:

1. **Parametric types** — types (or constants) as parameters to other
   types: C++ templates, C#/Java generics, ML and Haskell
   parametric polymorphism. Stepanov's STL sense of "generic
   programming." Compile-time abstraction over *what things are*.
   MOOLLM's analog: [parameterized skills](https://github.com/SimHacker/moollm/blob/main/designs/PARAMETERIZED-SKILLS.md)
   and templated playing pieces — BOTTOMLESS-PIT instantiated into any
   cave.
2. **Generic dispatch** — generic functions selecting methods by the
   runtime classes of (possibly all) arguments: CLOS `defgeneric`,
   Dylan, Kaleida's ScriptX, Julia; Python's stdlib
   `functools.singledispatch` decorator does it on the first argument
   only, with full multiple dispatch via third-party decorator
   libraries. Run-time selection over *what things are doing*.
   MOOLLM's analog: the advertisement auction; Korz dispatch.

Both traditions hit the same wall: **ambiguity**. Multiple inheritance
needs linearization rules (C3/MRO), CLOS needs method combination, Korz
needs its Appendix B specificity legislation, and every one of these is
a deterministic tiebreak imposed because the machine cannot judge. An
LLM can judge: it resolves *which* inherited meaning applies from the
live context, on the fly — and, interlocking, it can inherit from ideas
in latent space and **filter, modulate, and rename what it imports** on
the way in ("Self's clone semantics, but call it `incarnate`, and add
consent"). Ambiguity stops being an error class and becomes a dispatch
surface.

## "Context" in COP and "context" in an LLM call

Two different things wearing one word — but parallel along real
dimensions, and the projection between them is load-bearing:

| Deterministic COP / Korz | LLM completion call |
|---|---|
| Context = finite set of dimension:coordinate bindings | Context = everything in the window (plus the prompt's implied world) |
| Guards: decidable predicates | Guards: judged relevance |
| Specificity rules pick the slot | Attention weighs everything at once |
| Dispatch: deterministic lookup | Dispatch: sampling from a conditioned distribution |
| New dimension = schema change | New dimension = say it in prose |
| Ambiguity legislated away (Appendix B) | Ambiguity interpreted from meaning |

Projecting up: deterministic COP is the **corner case** of LLM COP at
`{temperature: 0, dimensions: enumerable, guards: decidable}` — which is
why the tiered-JIT thesis below works at all: the crystallized subset
means the same thing in both tiers. And going up the projection opens
dimensions that had no classical analog: inheritance from latent space,
semantic conflict resolution, a generative miss handler (unmatched sends
improvise in character), and grounding for Drescher's schema mechanism —
schemas whose context and result conditions can finally be *judged*
rather than merely matched.

This is the step-back Don keeps insisting on: re-evaluate everything we
know in the light of LLMs, because the old reflex "don't do that, it's
not possible" now trips us at exactly the wrong moments. He had a hard
enough time absorbing what it meant that an NCP — then TCP/IP — packet
could cross the country intact, that the reply came back, and that *a
programmer could just do that*. What it was for wasn't obvious at packet
level. Then: over the ARPANET to play Zork on MIT-DM's PDP-10; through a
transatlantic gateway to Essex to play MUD *with other people*; to CMU
for TinyMUD; to PARC for LambdaMOO; then Ultima Online, World of
Warcraft, The Sims Online. Each step was "just a packet," and each step
was a new world. The LLM call is at the packet stage now.

## Why it maps onto MOOLLM

| Korz | MOOLLM / [Game Pieces](https://github.com/SimHacker/moollm/blob/main/designs/GAME-PIECES.md) |
|------|----------------------|
| Same entity behaving differently per situation (subjective objects) | The [Cross-Platform Troll](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/fictional/troll) fronting zork-mind vs adventure-mind per world — a `world` dimension in the dispatch context |
| Slot guards (`{assertions <= true}`) | Buff conditions (`while:`, `expires_when:`) — a disabled buff is a guard that stops matching; nothing is removed |
| Context flows implicitly through the call chain | The current room, game, and season flow into every action without objects passing them along — an LLM context window does this natively |
| Coordinates in a dimension, no fixed object boundary | Side-relative move coordinates: one PAWN/NWAP move-set, interpreted per `side` — dispatch on team frame, not duplicated files |
| Slots gathered into subjective objects per view | [The Hague](https://github.com/SimHacker/moollm/blob/main/skills/experiment/experiments/turing-chess/plugins/revolutionary-chess/house-rules/THE-HAGUE.yml): the same piece is juror, witness, accused, pundit depending on which dimension you group by |
| Most-specific-slot-wins dispatch | Advertisement scoring generalizes this — see the dispatch spectrum below |
| IDE presents asymmetric views of a symmetric space | Semantic pyramid + directory views: the task dictates which dimension dominates the presentation |

## The dispatch spectrum: argmax, find-best-N, softmax

Korz dispatch is **argmax**: most specific slot wins, deterministically;
dispatch ambiguity is a problem the paper legislates with specificity
rules (their Appendix B). The Sims shipped ambiguity as a feature:
autonomous behavior scores all advertisements, then its **find-best-N**
primitive picks *randomly among the top N* — deliberate dither that
makes behavior organic instead of digitally predictable, converting ties
into personality. And an LLM's temperature sampling is find-best-N's
continuous generalization, native to inference.

Why dither at all? Three reasons The Sims discovered in production.
**Epistemics:** advertisement scores are approximations at best and
intentional lies at their cleverest (objects hustle — the fridge's
"open me if hungry" chains to raw food's "cook me" chains to the stove's
hot-meal pitch with an unstated house-fire clause), so argmax over lies
isn't optimization, it's being deterministically conned. **Exploration:**
random picks among strong candidates escape local maxima and, iterated,
find ways out of apparent dead ends — the wide possibility-space coverage
a Drescher schema learner needs. **Teachability:** visible imperfection
leaves room for the player to improve the character by overriding it —
a directed command forces one ad regardless of score, which is
programming by demonstration in disguise; the resulting skill gains
re-weight future auctions until the override becomes the habit. An agent
that always argmaxes cannot be taught by demonstration, because its
teacher has nothing to add. And the override should weigh heavy: a
forced pick is a **strong salience signal** to a Drescher-style schema
learner — the teacher explicitly marking *which* choice mattered, worth
a thousand unattended trials — which implies the unbuilt fourth stage,
**advertisements that learn**: not to be more persuasive but more
appropriate and helpful, re-tuning bids to the hearer's observed
outcomes, with persuasion arriving as earned trust once the hearer
discovers the ads serve the listener rather than the seller.

1. **argmax** — deterministic; compiles to a table lookup
2. **find-best-N** — still crystallizable: scoring table plus a *seeded*
   RNG (log the seed, so replays don't diverge)
3. **softmax** — temperature over judged salience; the LLM's home turf

The Korzish move: make **temperature a context dimension**.
`{temperature: 0}` recovers classical Korz; the party planner runs hot
while the accountant in the same call chain runs cold; a scene sets its
dither once and every dispatch below inherits it implicitly — the
`assertions: true` trick, applied to determinism itself. And the
dimension can be set by the *environment*: ambient heat comes from the
room, and the room inherits it, time-varying, from **moody media**
playing in it — music and video artifacts carrying parameter tracks of
heat per semantic tag, broadcast while they play
([MOODY.md](https://github.com/SimHacker/moollm/blob/main/designs/MOODY.md)).
A room whose implicit context dimensions are written by the stereo is
about as Korz as game design gets.

## The tiered-JIT thesis

The LLM is **tier 0 of a tiered JIT for microworlds**, and the adventure
compiler is the optimizing tier. The shared contract is contextual
dispatch over guarded slots (YAML files: buffs, minds, house rules,
advertisements). The LLM is the maximal interpreter — guards by
inference, unbound dimensions filled from latent space, and a generative
miss handler: unmatched sends improvise in character, then the ruling is
lifted into a slot. The deterministic VM runs the crystallized subset —
gelled schemas whose dimensions are enumerable and whose guards are
decidable compile to dispatch tables and ECS archetypes. Coherence comes
from subset semantics plus monotone extension (everything the VM runs
means the same to the LLM; everything the LLM adds, the VM defaults away,
Postel-style). And when runtime invalidates a compiled assumption —
[Revolutionary Chess](https://github.com/SimHacker/moollm/tree/main/skills/experiment/experiments/turing-chess/plugins/revolutionary-chess)
appends an organelle to the commons — you do what the Self VM does when
an optimized method's assumptions break: **deoptimize to the interpreter
tier**, which now means *re-engage the LLM*, lift the ruling, recompile.
Dynamic pessimization with inference as tier 0.

## Open questions for the conversation

1. Korz picks the most specific slot; The Sims ranks all matching
   advertisements and dithers. Would Korz accept a **scored or
   stochastic dispatch mode** — and would temperature be a dimension?
2. "Deoptimize to the LLM": what does thirty years of Self VM experience
   say about **where the tier boundary wants to sit** and how eagerly to
   recompile?
3. Korz's open problems — global dimension names, merging slot spaces,
   composition richness — MOOLLM has partial answers (directory
   namespaces, Postel + provenance, advertisement merging). Do they
   transfer back?
4. Is SOP a case of COP, or are both projections of Korz's dimensions?
   He co-authored the FOOL paper arguing the latter — does he still
   hold that, ten years on?
5. The Sims hardwired `me` and `stackObject` as exactly two dispatch
   dimensions, with the verb stored in the direct object. Did the Korz
   team know they were generalizing a shipped game VM?
6. What would Korz look like with an **inferential dispatcher** — guards
   judged rather than evaluated, ambiguity resolved by meaning, missing
   slots improvised then lifted?

## More powerful than the sum of its parts

The paper's last sentence:

> It seems that Korz's particular combination of concepts, each
> well-known from the past, is indeed more powerful than the sum of its
> parts.

That is MOOLLM's explicit aspiration too: selfish prototypes, leaning
into the training, YAML jazz, empathic templates, K-lines — each
well-known, each chosen because they reinforce one another harmonically
rather than merely coexist. The biological name for novelty-by-merger is
endosymbiosis, and MOOLLM keeps a specimen cabinet:
[ENDOSYMBIOSIS](https://github.com/SimHacker/moollm/blob/main/designs/object-system/ENDOSYMBIOSIS.md)
— the Cross-Platform Troll with microworlds inside, Wumpus carrying his
own genome in four languages, the coatroom grue metabolizing the host
world's darkness.

Related: [Don's Korz notes & Q&A](../korz-notes.md) ·
[Oct 2025 Korz pointer](2025-10-26-korz-email-hn-rollup.md) ·
Self entry points ·
Don's tiered-JIT note ·
Teaching complicated systems without a manual
