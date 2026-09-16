# Magic: The Gathering's layer system — subjective dispatch, shipped to millions

*Part of the [Korz cauldron](../../README.md). Sidecar: [`mtg-layers.yml`](mtg-layers.yml).
**Spectrum: self-contained** — the published rules are the canon, and you
need no repo mythology to follow them.*

**What this teaches.** [Korz](../../README.md)'s FOOL 2014 position paper argues
that a *layer* is just a **guard** and a *subject* is just a **coordinate**,
so aspect- and context-oriented programming are projections of one smaller
mechanism. Magic: The Gathering is that claim's most severe test, because
Magic contains the largest continuous-effect system ever put into
production — printed on 27,000+ cards, adjudicated by paid judges, and
implemented independently at least half a dozen times. It arrived at
**dimensioned dispatch over a slot sea** without a single reference to
programming language theory, and it hit the two walls Korz has not yet
walked into: effects that **rewrite other effects' guards**, and ambiguity
that is **not allowed to be an error**.

The cast, for cold readers: a *permanent* is a card on the table. A
*continuous effect* is a standing rule some card contributes ("creatures you
control get +1/+1"). Many of them apply at once, to each other, and the game
must produce one answer.

## The rules, in one screen

Comprehensive Rules **613** ([mtg.wiki](https://mtg.wiki/page/Layer),
[judge notes](https://blogs.magicjudges.org/ftw/l2-prep/rules-and-policy/continuous-effects/))
say that every continuous effect applies in exactly one of seven layers,
always in this order:

| Layer | What it changes |
|-------|-----------------|
| 1 | Copy effects — *this permanent is now a copy of that one* |
| 2 | Control — who owns it |
| 3 | Text — rewriting the words on the card |
| 4 | Type — land becomes creature, nonbasic becomes Mountain |
| 5 | Color |
| 6 | Abilities added or removed |
| 7 | Power and toughness, in five sublayers 7a–7e |

Within a layer, order is decided by **timestamp** (613.7, oldest first),
unless a **dependency** exists (613.8), which overrides it. And if the
dependencies form a loop, 613.8b throws the dependency rule out and falls
back to timestamps.

## Base state and projected state: E-Prime, enforced by tournament rules

The Korz README says a Korz entity *is* nothing absolutely — "red lives in
the dispatch, not in the rose." Magic enforces exactly that, on pain of a
judge call. You may not ask what a creature's power *is*. You may only ask
what it projects to, right now, under every applicable effect, recomputed
from the printed card up.

Rules engines discover this shape independently. One recent implementation
writeup describes splitting **base state** (what the card says) from
**projected state** (what players see), with a "state projector" that
reapplies all active continuous effects in layer order whenever anything
changes ([Argentum](https://wingedsheep.com/building-argentum-a-magic-the-gathering-rules-engine/)).
That is a Korz *gather* with a cache in front of it: the sea of slots is the
base state, and an object is a projection along a chosen coordinate.

Note also what the recomputation is **not**. Continuous effects do not use
the stack, do not respond to events, and are re-derived whenever the engine
looks. It's a fixpoint over the whole sea, not a message send — a *pull*
discipline where Korz dispatch is *push*. Same slot sea, two evaluation
strategies, and the CAM6 reading in
[layered-rules.md](layered-rules.md) already met the other one: stages in a
pipeline rather than `if` blocks inlined per engine.

## The wall Korz has not hit: guard-mutating effects

Here is the part that should interest David most.

Korz dimensions are declared, and guards match against coordinates. Magic's
**layers 3 and 4 change what other effects match.** *Blood Moon* makes all
nonbasic lands Mountains with no other abilities; *Urborg, Tomb of Yawgmoth*
is a nonbasic land whose ability makes every land a Swamp. Apply Blood Moon
first and Urborg's ability ceases to exist. Apply Urborg first and you get a
different board. Timestamps cannot settle it, because the question is not
"which is newer" but "which one is still *there* to ask"
([Draftsim's walkthrough](https://draftsim.com/mtg-layers/)).

Magic's answer, 613.8a, is a definition of dependency in terms of guard
mutation: A depends on B if applying B would change A's text, existence,
what it applies to, or what it does. That is a **dispatch rule about slots
that edit the dispatch lattice** — a fixpoint one level up from the one Korz
specifies. And the canonical horror case is self-referential: *Humility*
makes all creatures 1/1 with no abilities, *Opalescence* makes enchantments
into creatures, and Humility is an enchantment. Judges teach it; engines fail
it. One implementation reports handling it by **trial application** —
tentatively apply, watch which outcomes move, derive the order, then apply
for real.

In Korz vocabulary: a slot whose guard is not decidable until you have
provisionally run the other slots. Korz's stated semantics — unique
most-specific match, tie is an error — has no room for that yet, and Magic
proves the case is not academic. Thirty years of errata say it is where the
money is.

## Ambiguity: Korz errors, Magic legislates

Korz says an ambiguous send is an error. Korz′ ([troll-blend.md](troll-blend.md))
adds two softer policies, sample and blend. Magic supplies a third, and it is
the one a **shipped** system is forced into, because a game in progress cannot
raise an exception and a player cannot be told the board is undefined:

**Legislate a total order, in tiers, with a fallback at every tier.** Layer
order first (hand-authored by designers, refined over decades). Dependency
second (derived from guard mutation). Timestamp third (last-write-wins).
Dependency loop — drop back a tier. There is always an answer.

This is [robust-first](https://github.com/SimHacker/moollm/tree/main/skills/robust-first)
applied to dispatch: a crashed game is infinitely wrong, so degrade to a
defensible order instead. Judges even say why out loud — the layer system's
goal is "to make it so the answer to any continuous effects question is what
we would intuitively expect as often as possible." The order is not
principled. It is **tuned to expectation**, which is the honest name for what
specificity heuristics are doing in any dispatcher.

## What the tuning costs

Nobody should read this as a recommendation. Magic's system is the standing
argument that hand-ordered layers are expensive:

- The order must be memorized; judges call it the part people have the most trouble with.
- Implementations diverge under load. A third-party description of the Forge engine's semantics records that it adds an **eighth layer** for rule-changing effects, folds sublayer 7d into 7c, and leaves 7e (power/toughness switching) unimplemented ([manabrew notes on Forge](https://github.com/witchesofthehill/manabrew/blob/main/docs/forge-dsl-semantics.md)). Seven layers is a *lower* bound on a real engine.
- The composite system is Turing complete — Churchill, Biderman and Herrick built a universal machine out of legal cards and a legal board state ⚠ (verify citation before print).

Korz's pitch is that most of this is the price of not having dimensions:
if the specificity lattice were declared rather than legislated, the order
would be derived. The counter-pitch, which deserves to be stated fairly, is
that layers 3, 4 and 6 mean Magic's lattice **changes during play**, and no
declared lattice survives that. Both can be true — which is exactly the
conversation to have.

## Where Korz′ takes it

Two things Magic has that no programming language does.

**The largest prose-to-guard translation corpus in existence.** Every card is
a prose rule; *Oracle text* is its maintained canonical form; the
Comprehensive Rules are the formal semantics; engine DSLs are the compiled
version. Errata are the change history. For Korz′'s **crystallize**
direction — soft prose guards hardening into decidable slots — that is
supervision at a scale no language ecosystem can match, complete with the
governance model (a rules manager, a public errata process, and a judge
program) that a two-tier dispatcher will eventually need.

**A working soft tier with a human in it.** When the rules underdetermine a
board, a judge rules; the ruling is published; the rule sometimes changes.
That is precisely Korz′'s architecture — strict tier for the decidable,
soft tier for everything else, and stable soft rulings crystallizing
downward — running in production since before most working programmers
started, on a corpus of millions of players.

The [Sims advertisement economy](sims-advertisements.md) is the other
shipped dispatcher in this collection, and the pair frames a real design
axis. Sims resolves ambiguity by **scoring and sampling** — advertisements
compete in an auction and find-best-N keeps the dither. Magic resolves it by
**ordering and rewriting** — no scores anywhere, total order all the way
down. Two mass-market systems, same problem, opposite answers, and Korz′
needs a policy that can express both.

## The cheap way out that Magic didn't take

[Fluxx](fluxx-nomic.md) is the control experiment, and it is humbling. Its
rule cards are sorted into categories — Draw, Play, Limit, Other — and **at
most one card of each category may be in play**; a new one discards the one it
contradicts. Declared dimensions, one binding each, rebinding as the only
operation. Conflict cannot be represented, so there is nothing to order, so
there is no layer system, no timestamp, no dependency graph, and no judge
program.

Magic cannot retrofit that: its effects are additive by design ("creatures
you control get +1/+1" must stack with three more of the same), and its
identity is a card pool where any two cards may meet. But the comparison
sharpens the Korz pitch considerably. CR 613 is not the price of continuous
effects. It is the price of letting two effects bind the same dimension.

*See also:* [Dwarf Fortress procedural magic](df-procedural-magic.md), where
the dimensions themselves are generated per world rather than printed on
cards; and [ask-david.md](../../ask-david.md), which now carries the questions
this example raises.
