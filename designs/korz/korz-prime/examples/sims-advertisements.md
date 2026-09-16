# The Sims advertisement economy — dispatch as an auction

*A [Korz example](README.md). Self-contained: the canon here is
shipped commercial software — The Sims (2000), which Don programmed.
Teaches: scored dispatch, deliberate dither, and why the most
successful dispatch system in consumer software refused argmax.*

## Two frozen dimensions

SimAntics — The Sims' behavior VM — has an implicit **`me`** (the
object running the behavior tree, like C++'s `this`) and an implicit
**stack object** (the object `me` is currently interacting with:
"it"). Subject and object, hardwired into the instruction set. In
Korz terms the diagnosis is one line: `me` and `stackObject` are
**two hardwired dimensions of the dispatch context** — a binary
multimethod frozen into the VM. Zork froze five
([case-zork.md](../../case-zork.md)); The Sims froze two; Korz
generalizes to N and lets you add new ones after the fact.

The famous inversion is grammatical: **the verb lives in the direct
object.** Interactions are behavior trees stored on the thing being
used — the espresso machine carries "make espresso," and the Sim who
runs it is the subject animating a verb it never owned.

And the pronouns carry more weight than they look like they do.
C++'s `this` is a dehumanizing pointer — it points *at* a thing.
Self's `self` is humanizing — the word people use for personhood.
The Sims went first-person: `me`, with the stack object as the
grammatical direct object. Korz's `rcvr` is convention plus a little
dot-notation sugar, not a privileged concept: the model would
happily host a Sims-shaped dialect with `me` and `it` (or `that`, or
`them`) as two dimensions among many. **The dimension names are the
pronoun system of the language — choosing them is choosing who
counts as a subject.**

## The auction

Add advertisements and you get the full sentence: **objects
broadcast verbs; subjects score them.** Every object in the world
advertises scored actions — the fridge advertises "open me" with
hunger relief, the shower advertises hygiene, the pinball machine
advertises fun. Each Sim re-weights every ad through its own needs,
personality, and relationships: the same espresso machine scores
differently for the tired Sim, the playful Sim, and the Sim who
hates the kitchen's owner. An advertisement is a Korz slot wearing
one extra field:

| Advertisement | Korz slot |
|---|---|
| `action` | selector |
| `condition` | guard |
| `effect` | body |
| `score` | — *(Korz has no analog: precedence is structural)* |

Korz derives precedence from the specificity lattice — unique
most-specific wins, ties are errors. The Sims declared it
numerically and let the subject re-weight it. Lattice specificity is
a score the guard structure computes; advertisement scoring is a
lattice the designer flattens by hand; the soft tier's relevance
sampling interpolates between them.

## find-best-N: ambiguity as a feature

Korz dispatch is **argmax** — and dispatch ambiguity is a problem
its paper legislates away with specificity rules. The Sims shipped
ambiguity as a *feature*: autonomous behavior scores all
advertisements, then the **find-best-N** primitive picks randomly
among the top N — deliberate dither that makes behavior organic
instead of digitally predictable, converting ties into personality.

Why dither at all? Three reasons The Sims discovered in production:

- **Epistemics.** Advertisement scores are approximations at best
  and intentional lies at their cleverest — objects *hustle*. The
  fridge's "open me if hungry" chains to raw food's "cook me" chains
  to the stove's hot-meal pitch, with an unstated house-fire clause.
  Argmax over lies isn't optimization; it's being deterministically
  conned.
- **Exploration.** Random picks among strong candidates escape local
  maxima and, iterated, find ways out of apparent dead ends.
- **Teachability.** Visible imperfection leaves room for the player
  to improve the character: a directed command forces one ad
  regardless of score — programming by demonstration in disguise —
  and the resulting skill gains re-weight future auctions until the
  override becomes the habit. An agent that always argmaxes cannot
  be taught by demonstration, because its teacher has nothing to
  add.

The dispatch spectrum, then, with its crystallization story
([design](../README.md)):

1. **argmax** — deterministic; compiles to a table lookup.
2. **find-best-N** — still crystallizable: scoring table plus a
   *seeded* RNG (log the seed, so replays don't diverge).
3. **softmax** — temperature over judged salience; the LLM's home
   turf, and find-best-N's continuous generalization.

## Where Korz′ takes it

Two extensions, both developed elsewhere in the cauldron:

- **Scores get an epistemic term.** Let an ad's score multiply in
  the `isKnown` of its own referents, and a slot with shaky pointers
  bids low in its own auction — the hallucination damper built into
  the market ([epistemics.md](../epistemics.md)).
- **Temperature becomes a dimension.** The dither knob stops being a
  VM constant and joins the context, settable per scene and
  inherited implicitly — which earns its own exhibit:
  [moody-temperature.md](moody-temperature.md).

And one honest open question rides along to David: would Korz accept
a **scored or stochastic dispatch mode** at all — or is the
specificity lattice's determinism the point?
([ask-david.md](../../ask-david.md).) The Sims' answer, twenty-six
years of shipped behavior: the auction with dither outsold every
argmax agent ever built.

*Deeper source: the
[Korz paper deep-dive](../../sources/korz-paper-deep-dive-moollm-mapping.md),
which works the mapping table and the dispatch spectrum in full.*
