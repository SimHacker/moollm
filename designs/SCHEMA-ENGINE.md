# The schema engine: Minsky's censors on Drescher's schemas

*The full design of `censor_sim.py`: every rule it follows, every command,
what was wrong with it and was fixed, and what it still can't do. For the
short version, read [`skills/schema-mechanism/OVERVIEW.md`](../skills/schema-mechanism/OVERVIEW.md)
first. The tutorial with exercises is [`CENSORS-ON-SCHEMAS.md`](CENSORS-ON-SCHEMAS.md);
the construction kit of reusable parts is
[`censors/BRAINBALL.md`](../skills/schema-mechanism/censors/BRAINBALL.md).*

---

## 1. What it is, in one breath

A made-up mind is a set of named facts (*items*) that are on, off or
unknown; a table of how much it wants each one (*values*); a list of
*schemas*, each saying "in this context, this action tends to produce this
result, this reliably"; and a list of *censors*, which are schemas with the
sign flipped. Given a record of what an agent actually did, the engine runs
the mind through the same events and reports whether it does the same
things, which of its parts the record needs, and how much the answer
depends on weights somebody guessed.

The mind learns the way Drescher's does: it can start from bare schemas,
knowing only which actions it has, and spin off what each action does from
what follows it (section 6). The same mechanism runs over a record from
outside, as `learn`. The engine is built to run in a loop with a language
model in a tool like Cursor. The engine proposes schemas from the evidence
and keeps only the ones that improve the fit. The model says what a kept
schema means, adds the outcome events a record is missing, and proposes
schemas of its own. `try` keeps or rejects each of those by the same test.
Each round starts from the last one's layers (section 10).

It is about 1,850 lines of Python 3 with one dependency (PyYAML). It never
calls a language model, never touches the network, and gives the same
output for the same input and seed on any machine. It runs about 20,000
simulations a second on a laptop, which is what makes the statistics in
section 9 cheap.

**It is a Pretend Intelligence, and says so.** The term is Richard
Stallman's, from his Georgia Tech talk of 23 January 2026
([video](https://youtu.be/YDxPJs1EPS4?t=641); essay:
[`PRETEND-INTELLIGENCE.md`](PRETEND-INTELLIGENCE.md)): a system that can't
know or understand statements in a domain is not intelligent in it, only
pretending. The engine uses the term twice, and keeps the two apart:

1. **Language-model output is PI, labeled as PI.** The engine never asks a
   model anything. When it needs words it can't compute, it prints a
   request (section 10). If a model answers, every line it wrote is marked
   `[PI]` in the output and is a hypothesis until a record supports it.
2. **The mind is a pretend mind, on purpose.** Like a Sim, it pretends to
   have motives so you can see what follows from them. Its only claim is
   checkable: *this mechanism reproduces this record; these parts were
   needed; this is how fragile that is.* Drescher's own title for the
   theory is *Made-Up Minds*.

## 2. Where each idea comes from, and where it lives in the code

| Idea | Source | In the engine |
|---|---|---|
| Schema: context, action, result, reliability | Drescher, *Made-Up Minds* (MIT, 1991), after Piaget | `Schema`; `schema_for` picks the most specific matching schema |
| Bare schemas: an agent starts knowing only its actions | Drescher | `agent.learn_schemas: true`; no schema is a starting state, not a request |
| Result spinoff: an item that follows an action more than it follows the others | Drescher | `Mind.spin_off`, during a run; `learn`, over a record |
| Context spinoff: an item before the action that makes the result likelier | Drescher | `Mind.spin_off`; for censors, `discriminating` |
| Marginal attribution over pain | Drescher's mechanism, applied to Minsky's censors | `attribute`, `discriminating`; offline, `induce` |
| Overriding conditions: items that make a reliable action fail | Drescher | `induce` labels them `overriding`, and writes them as censors |
| Synthetic items: states you can't see but must posit | Drescher | `propose` |
| Composite actions and planning over schemas | Drescher | `Mind.plan`, the `plan` command |
| Censors suppress faulty reasoning, not forbidden wishes | Minsky, AI Memo 603, "Jokes and the Logic of the Cognitive Unconscious" (1980) | `Censor` |
| Two kinds: "stop thinking that" and "don't even think that" | Memo 603 | `suppressor` and `precursor` |
| Patch a general rule with a specific exception | Memo 603: "it hardly ever pays to alter a general mechanism to correct a particular bug" | `anecdotal: true`; anecdotal censors outrank the general ones they patch |
| Jokes train censors | Memo 603 | `joke:` events: `exposes` and `lesson` |
| The cognitive unconscious | Memo 603 | two traces: inner and observer |
| Find Best Action: objects advertise, the agent takes the best offer | The Sims (Jamie Doornbos, 1997) | `decide`, `predicted_value`; `score: change` is the delta scoring The Sims uses |
| The model should fit in the player's head | Will Wright's games; SimCity, freed as Micropolis for OLPC | everything is a small YAML file; `lineage`, `where`, `diff` |
| Deterministic code first, a model only for what it can't compute, through readable files | MOOLLM | the event bus and its patches (section 10) |
| Make the mechanism visible so nobody has to trust appearances | Weizenbaum, after ELIZA and DOCTOR | the observer trace, `ablate`, `sweep` |

**The join.** Memo 603 described censors and never said how one is built.
Drescher described how a schema is learned and never had a negative one.
Put together: a censor is a schema with its result marked harmful and its
response *don't*, and marginal attribution over your own bad outcomes is how
it is learned. That join is the whole engine.

**The people.** Gary Drescher did the work as Marvin Minsky's and Seymour
Papert's student at the MIT AI Lab. Henry Minsky, Marvin's son, co-founded
Leela AI and implemented the schema mechanism as a real learner over video,
with Drescher advising; Don Hopkins works there. That code is far more
serious than this one and isn't public. This engine is a small, separate,
public re-telling of the idea, aimed at reading people's choices. Don also
worked on The Sims at Maxis and got SimCity's source released under the GPL
as Micropolis; the engine's decision loop is The Sims', and its
look-inside-the-model habit is SimCity's.

## 3. The data model

Everything is YAML. A scenario is one file plus whatever it inherits.

**Items** are three-valued: `on`, `off`, or absent (unknown). A condition
`x` holds when x is on; `!x` holds when x is off. Unknown satisfies
neither, so a mind can be ignorant, not just wrong.

```yaml
agent:
  name: "{self}"
  items:  { letter-from-dentist: off, knows-bad-news: off, calm: on }
  values: { informed: 5, knows-bad-news: -3, calm: 1 }
  contradictions: [[knows-bad-news, all-is-well]]   # both on = a conflict
  score: earned          # or: change   (section 5)
  losses_hurt: false     # section 6
```

**Schemas** say what an action does:

```yaml
schemas:
  - { id: read, action: read-letter, context: [letter-from-dentist],
      result: { informed: on, knows-bad-news: on }, reliability: 0.9 }
```

Several schemas can share an action. The one used is the matching schema
with the longest context, then the highest reliability: the most specific
knowledge wins, as with Drescher's context spinoffs.

**Censors** have a `kind`:

```yaml
censors:
  - id: too-long            # precursor: vetoes an action before it runs
    kind: precursor
    action: read-letter
    context: [letter-from-dentist]
    harm: [knows-bad-news]  # what it guards against
    cover: "I'll open it when I have a quiet minute."
    source: "tier0: claude"  # who wrote the cover
    anecdotal: false
    reliability: 1.0
  - id: reframe             # suppressor: re-files a state after it forms
    kind: suppressor
    context: []
    state: [knows-bad-news]
    refile: { knows-bad-news: off, needs-checkup: on }
    cover: "It's just a routine checkup."
```

A censor entry *without* a `kind` is a **patch**: words or fields waiting
for a censor that will be learned at run time. `{id: learned-read-letter,
cover: "..."}` gives the learned censor its cover the moment it's minted.

**Events** are the record, ordered by `t` (any number, so `4.1` slots
between 4 and 5):

```yaml
events:
  - t: 3
    set: { letter-from-dentist: on }     # the world changes
    say: "A second letter arrives."      # what the agent hears
    joke: { exposes: learned-read-letter, text: "...", discount: 0.5 }
    offers: [read-letter, put-aside]     # the moves open to it
    observed: put-aside                  # what it actually did
    response: "..."                      # its own words, if real
    source: "..."                        # where that is recorded
```

**Runs** are hypotheses about the same record. Each can override weights
and items, add or drop censors and schemas, add events, and state what it
expects:

```yaml
runs:
  - name: avoidance
    expect: { fit: 4/4, final: { informed: off } }
  - name: no-censor
    add_censors: [{ id: too-long, drop: true }]
  - name: calm-first
    agent: { values: { calm: 6 } }
  - name: what-if
    counterfactual: true                 # not scored against the record
```

`who:` names the cast, and `{name}` placeholders in every string are
filled from it, so one part can be anyone's.

## 4. Composition: how minds are built from parts

`inherits: [file, ...]` pulls in other files, relative to the file that
names them, recursively, any number. The chain is *linearized*: base first,
each file once. A part two parents share is merged where it first appears,
so it can't come back later and undo an override.

**Merge rules**, applied file by file in that order:

| Shape | Rule |
|---|---|
| dict | merge key by key, recursively |
| list of entries with `id` (schemas, censors) | merge by id; a new id appends; `drop: true` deletes |
| list of entries with `t` (events) | merge by t |
| list of pairs (contradictions) | accumulate, without duplicates |
| anything else | the later value replaces the earlier |

`imports: [{from: FILE, take: [id, values.KEY]}]` takes single traits out of
an archetype without the rest of it.

On top of the files: `--layer FILE` (repeatable) merges more layers last;
`--who k=v` recasts; `--set a.b.c=value` sets one field, addressing id'd
list entries by id (`--set censors.too-long.cover=...`). `resolve` prints
the merged result, `lineage` lists the files in merge order, and
`where FILE PATTERN` says which layer defined a thing.

The convention that makes the kit reusable: **logic** parts (what actions
do) carry no weights and no censors; **drive** parts carry only weights;
**censor** parts carry one censor each with a template cover; an
**archetype** is a list of inherits. Two people who share logic agree on
every schema and can still act differently, because they weigh results
differently and carry different censors. `diff A B` shows exactly that.

## 5. One step of the loop

For each event, in order of `t`:

1. **set**: observed items change.
2. **say**: the agent hears it (inner and observer trace).
3. **joke**: section 8.
4. **offers**: if the event offers moves, the agent:
   1. **decides** (below);
   2. records the fit, if the event has an `observed` move;
   3. **applies** the chosen action's schema: its result items are set;
   4. runs **suppressors** over the new state;
   5. runs **marginal attribution** on what just happened (section 6).

**Deciding.** For each offered action, collect the precursor censors that
veto it now. A censor vetoes when its action is this one and its context
holds, *unless* it has been exposed by a joke and its reliability has
fallen below 0.6 (the agent can see it and no longer trusts it), or every
harm it guards against has already happened (nothing left to guard).
Anecdotal censors are listed before general ones; the first one is the one
that's reported. A vetoed action is dropped, and its censor's cover is what
the agent tells itself. Of the rest, the agent takes the one with the
highest predicted value. If everything is vetoed, it does nothing.

**Predicted value** of an action is the sum, over its schema's result, of
each item's value (positive for turning it on, negative for turning it off),
times the schema's reliability. Two modes:

- `score: earned` (default): every result pays every time, as if the motive
  had decayed back between choices. A mind that values applause gets it
  again with each amplification.
- `score: change`: only results that change an item pay, as in The Sims'
  Find Best Action, which scores how much an advertisement would move a
  motive. Without decay this makes repeated choices worthless, which broke
  17 of 30 scenarios when tried as the default; it stays an option for
  minds that model decay elsewhere.

**Suppressors** fire when their context holds and every item of their
`state` is on. They apply their `refile`, so a forbidden state is filed
under another name, and the agent thinks the cover.

## 6. Learning: marginal attribution over pain

After each action the engine asks whether it hurt. **Pain** is any of:

- an item with negative value that is on now and wasn't before;
- a conflict (both sides of a contradiction on) that this action created.
  A conflict that was already standing isn't this action's fault;
- with `losses_hurt: true`, an item with positive value that was on and is
  now off. Off by default, since most parts name a loss as its own bad item.

Every action's trials are kept: the items before it, and whether it hurt.
Once an action has hurt twice (`learn_threshold`), the engine mints a
precursor censor `learned-<action>`. Its context starts from the positive
schema's own context (a censor is that schema with the sign flipped), and
adds every item whose state separates painful trials from painless ones by
at least 0.5 in probability (`!item` if its being off is what predicts
pain). An item that never varied carries no evidence and is left out. If
the censor exists and a later trial changes the discriminating context, the
context is refined in place: Drescher's context spinoff, applied to a
censor. A patch with the same id, if any, supplies its cover.

The mind never sees this happen. The observer trace says *marginal
attribution mints censor learned-read-letter*; the inner trace says nothing
until the censor fires, and then only the cover.

### Learning what actions do: result and context spinoffs

With `agent.learn_schemas: true` the mind can start with no positive
schemas at all. An action with no schema is worth nothing yet, and taking
it is how the mind finds out. After each action the mind opens a window.
Every item the world changes before the next choice (an event's `set`)
is recorded as having followed that action, compared with the state
before it. The first change counts, and a later reset doesn't erase it.
The window closes when the next choice comes.

Once an action has `learn_threshold` trials (2), marginal attribution
looks at each item that followed it. If the item followed the action at
least that many times, in at least half the trials, and in a share at
least 0.5 higher than after the other actions, it is a **result spinoff**.
The mind mints `learned-<action>` with those results, at the observed
rate as its reliability. Then a **context spinoff**: an item whose state
before the action separates the trials where the results came from the
trials where they didn't, by at least 0.5, joins the context. The mind
mints `learned-<action>-when-<item>` with the reliability of that subset,
and the general schema's reliability is revised to the overall rate. A
hand-written schema with the same context is extended with the new
results, never overwritten. Each spinoff appears in the observer trace,
not the inner one: the mind uses what it learned without watching itself
learn it.

The worked example is
[`learning-toddler.yml`](../skills/schema-mechanism/censors/examples/learning-toddler.yml):
a toddler with two actions and no schemas cries twice, is scolded twice,
spins off *cry → scolded*, then asks, gets a snack twice, and spins off
*ask → snack*. When the parent goes out and asking stops working, the
context spinoff narrows it to *ask → snack when the parent is home*. The
learning mind fits all 7 choices; the same mind with learning off fits 2.

**Over a record, `learn`** replays the record with spinoffs on, learning
from what the person did (the world's answers in a record followed the
real action, not the model's). It proposes every schema it learned, and
gates each one: kept only if the model with it fits the record better.
Kept schemas feed the next round, until a round keeps nothing. Each kept
schema raises a request for the other tier to say what it means, or to
drop it as an artifact of how the record was written. On the toddler,
`learn` takes the knows-nothing mind from 2/7 to 5/7 with one schema,
*ask → snack*. The two remaining misses are the cries before the child
had learned anything, and only a mind that learns during the run fits
those. The record of a learner is fit by a learner.

## 7. The two traces

Every log line goes to the observer trace. It also goes to the inner trace
only if the agent could know it: what it heard, what it did, what it told
itself. A censor that fires unseen is in the observer trace only, marked
`[unconscious]`. The difference between the two traces is what Memo 603
called the cognitive unconscious, made literal.

A real person's quote (`response:`) prints only beside the action they
actually took. If the model does something else, the quote is withheld, so
a counterfactual can never put words in anyone's mouth.

## 8. Jokes

Memo 603's claim is that humor is how censors are trained: a joke holds an
absurdity in view long enough for the mind to notice it. Two kinds:

- `exposes: CENSOR` makes an existing censor visible and multiplies its
  reliability by `discount` (default 0.5). Below 0.6 a visible censor can
  be overridden, so the agent can now take the action it had been avoiding,
  knowingly. Exposing a censor that doesn't exist yet is a miss and a
  warning.
- `lesson: {...}` installs a new anecdotal precursor censor, the joke's
  moral as an exception. With no `exposes` it is installed unseen; a joke
  that exposes one censor and teaches another leaves the new one visible.
  A miss that carries a lesson still teaches it.

## 9. Reading a record

Each command answers one question. All read the same files.

| Command | Question it answers |
|---|---|
| `test` | Does every run fit its record and expectations? Exit 2 if not |
| `run` | What did the mind do, think, and hide, step by step? |
| `ablate` | Which censors (and lesson jokes) does the record actually need? |
| `sweep` | Do the conclusions survive moving every guessed weight up to ±50%? |
| `bounds` | Which weightings make every observed choice, and what range does that leave each weight? |
| `predict` | What does each hypothesis do at an event that hasn't happened? |
| `argue` | Which argument, said first, moves each hypothesis toward a goal? |
| `induce` | Which observed items made each recorded choice likelier or less likely? |
| `propose` | Did a choice switch once with nothing observed to explain it? |
| `drift` | Does the fit hold over time, or only in total? |
| `plan` | What plan can the agent think of, and what plan can an observer see? |
| `diff` | Same logic, different priorities: where do two minds differ? |
| `duet` | Two minds on one stage: what does each one's move do to the other? |
| `suite` | Lint and test every scenario under some paths |

**`ablate`** drops each censor in turn and re-scores. A censor whose
removal costs nothing is *not needed*: the values alone explain the
choices, and the censor is at most the agent's account of them. This is
the most important honesty check in the engine. In Andersen's *Emperor's
New Clothes* the Emperor needs no censor: he is calculating, not
repressing, which is what the story says.

**`sweep`** draws N weightings, each weight multiplied by a uniform factor
in [1 − spread, 1 + spread], and reports the share of weightings in which
each run reaches each fit and each sequence of choices. Weights a run sets
for itself are perturbed too, after its overrides. The order of weights is
fixed (shared ones in file order, then run-only ones sorted), so a seed
means the same draws everywhere. For the dentist, about 30% of weightings
never form the censor at all: those minds value calm over knowing and never
open the first letter. A censor forms only in a mind that would otherwise
go where it hurts.

**`bounds`** turns the question around. `sweep` asks how far the guessed
weights can move before the conclusions change; `bounds` asks which weights
the record allows at all. It replays the record taking what the person
did, and at every choice writes down what that choice implies: the action
taken scored at least as well as each alternative that wasn't vetoed, and
strictly better when a tie would have gone to the alternative. With the
censors held where the replay left them, predicted value is a sum of
weight × sign × reliability over each schema's results, so every choice is
a linear inequality in the weights. The weightings that make the whole
record are a polytope, and a linear program gives each weight's minimum
and maximum over it.

Scale is free (doubling every weight changes no choice), so one weight is
held at its current value as the anchor, by default the largest, and the
rest are boxed in ±10. Each weight is then reported as *must be positive*,
*must be negative*, *bounded*, or *the record doesn't constrain it*. Also
reported: whether the current weights make every choice, the weighting
deepest inside the polytope (the center of the largest ball that fits,
with its radius), and the choices no weighting can fit. Choices are added
in time order; one that can't join the ones before it is named, with the
earlier choice it contradicts. The solver is a small two-phase simplex in
the script itself; the unit tests check it against scipy.

What it says about the examples:

- Toddler: given that a snack is worth 5, the record needs only that being
  scolded counts against crying. Any negative value fits.
- The vain mayor: applause must be worth at least 2.5, half of his name on
  the clinic. The deal is unconstrained: no choice in the record depends on
  it. His third choice contradicts his second under every weighting.
- The beekeepers: no weight is constrained. Their record is decided by
  structure (which schemas exist, which censors form), not by weights.
- The quiet secretary: her silences at t=5 to 8 contradict her defenses at
  t=1 to 4 under every weighting of the declared values. Something changed
  that the values can't see, which is the hidden state the example's answer
  layer supplies.
- When the polytope is flat, some choices hold only at an exact tie won by
  offer order: the person switched with nothing the model sees changing in
  between. `bounds` names those choices rather than reporting a weighting
  that depends on the order of `offers`.

`--free-all` also solves for result items that have no declared value;
`--anchor` and `--box` set the scale.

**`predict`** adds one event at the next `t`, with the offered moves and
any items set, and reports each run's choice over N weightings. Committing
the output before the event happens makes it a preregistration. Example,
public, from WillWrightShowForFood: on Trump's TrumpCare record, if a bill
reaches his desk, sign 75% where the name on it pays and veto 87% where it
doesn't.

**`argue`** is plan validation by simulation: before suggesting an argument
to a real person, run it. Each argument is an event (say, set, joke) placed
just before the next choice. It reports the probability of the goal under
each hypothesis, the lift over no argument, and the *split* between
hypotheses. An argument with a large split is a test: trying it tells you
which hypothesis is right.

**`induce`** runs marginal attribution over the *record*, not the model:
for each offered action, how much likelier the person was to take it with
an item on than off. A positive gap proposes a context; a negative one is
Drescher's overriding condition, which is what a censor looks like from
outside. `--patch` writes the missing ones as learned censors, coverless.

**`propose`** looks for Drescher's synthetic items: an action taken, taken,
taken, then refused from some point on, where no observed item explains the
switch better than the switch itself. It proposes a latent item that turns
on between the two times, and a request asking what happened then.

**`drift`** weights hits by recency (half-life in choices) and reports
where the unbroken run of hits at the end begins. People change; a
hypothesis that fit the first ten choices and missed the last three is
worse than its total.

**`plan`** is Drescher's planner with Minsky's censors in the search:
Dijkstra over states, each step costing 1 − log(reliability), so a long
sure plan can beat a short gamble. It runs twice: once pruning any step a
precursor vetoes in the state where it would be taken (the plan the agent
can think of), once without (the plan an observer can see). `walk` replays
the observer's plan and names the censor that hid each step. If no plan
exists at all, it requests the missing schema.

```
plan for appointment (run avoidance, at end; on: calm, letter-from-dentist, tooth-aches, tooth-worse):
  agent sees:    none found
  observer sees: read-letter → book-appointment   cost 2.105
  hidden: 'read-letter' is vetoed by censor learned-read-letter
```

### Two minds: `duet`

A record is one mind facing a world. A duet is two minds facing each
other. The file names the seats (each a mind file and one of its runs),
the world's starting items, and the turns:

```yaml
seats:
  reformer: { mind: name-on-the-clinic.yml, run: goal }
  mayor:    { mind: mayor-thorne.yml, run: vain }
world:   { goal-blocked: on }
effects:                       # a move becomes news for every seat
  offer-credit: { offer-on-table: on }
  repost-offer: { target-signaled: on }
turns:
  - { t: 1, seat: reformer, offers: [offer-credit, mock-target, refuse-to-deal] }
  - { t: 2, seat: mayor, offers: [repost-offer, attack-offer, ignore-offer], when: [offer-on-table] }
  - { t: 3, set: { bill-on-desk: on }, when: [talks-open] }    # the world, if it got there
```

A turn with a `seat` is that mind choosing, by the same `decide` as
always, censors and all. A turn without one is the world changing. An
action listed in `effects` sets items for every seat, and a turn with
`when` happens only if the world got there. The mind files' own records
are not used: **a duet plays the minds, not the record.** If one seat's
model does something the real person didn't, the other seat reacts to
the model's move, and the story diverges. Turns can still carry
`observed`, and the output marks each move "as observed" or not, so you
can see where the divergence starts.

`--n N` draws each seat's weights independently N times and tallies the
joint sequences and the share of runs that end with each `watch` item on.
`expect: {moves, world}` makes a duet testable, and `suite` runs it.

In the fictional example the clinic gets signed only when both minds are
what the offer assumes: 78% of 2,000 joint weightings with the default
pair, none with a taunting reformer (she mocks him the moment he bites)
or an indifferent mayor (he attacks the offer and the later turns never
happen). That's a finding no single record could give: whether a move
works depends on the mind it lands in, and the duet says how much.

## 10. Two tiers, and the bus

The engine is the deterministic tier. What it can't compute, it asks for.

- **stdout** carries the data you asked for (`--format text|md|yaml|json`).
- **stderr** carries one JSON event per line: `REQUEST`, `ERROR`,
  `WARNING`, `INFO`, `RESULT`, `TELEMETRY`. A request's id is a hash of
  what is being asked, so the same open question has the same id in every
  invocation, and any number of threads can be followed from outside with
  `jq` or `grep`.

Each request carries a **patch**: the YAML layer that would answer it. A
person, another program, or a language model in a chat fills it in, and
it comes back as `--layer FILE` or is merged into a file with `apply`.
Requests are made for a schema nobody wrote (what does this action do?), a
cover for a censor that fired without one, a latent item `propose` found,
and a plan with no schema to reach it, and for the meaning of each schema
`learn` kept. The loop lives outside the tool, so it composes: files in,
files out, filters in between. Exit 3 under `--strict` means requests are
still open.

### The loop

In a tool like Cursor, the language model runs the commands and answers
the requests; the engine does the counting and the gating. One round:

1. `learn FILE --patch > learned.yml` proposes schemas from the record,
   keeping only those that improve the fit, and asks what each means.
2. The model answers in a layer: a `note` for each kept schema, or a
   `drop: true` for an artifact. It may also propose things the counts
   can't: outcome events the record is missing (with sources, for a real
   person), a schema for an action nobody described, or a latent item to
   explain a schema that works only sometimes. All of it is marked
   `tier0`, which means `[PI]`.
3. `try FILE --layer answers.yml` is the gate. It rejects a layer that
   makes any run fit worse or adds a lint error, and reports whether it
   helped. The record decides, not the model.
4. Kept layers are merged with `apply` or passed as `--layer` to the next
   round, and `ablate`, `sweep` and `propose` run on the result.

The rounds stop when `learn` keeps nothing and the requests are closed.
This is Drescher's learner with a division of labor. Counting, attribution
and the fit test are deterministic and repeatable. Naming, and noticing
what a record left out, go to the tier that can produce words, and every
word it produces has to pass the same test as a count.

On the public-figure records `learn` currently finds nothing worth keeping.
Those records describe the situation before each choice and reset it
after, but rarely record what followed (applause, criticism, a deal). The
resets look like results and the gate rejects them. Adding sourced outcome
events is the model's part of the loop, and it is what would let those
minds learn what their moves do.

A cover whose `source` starts with `tier0` was generated, and prints with
`[PI]`.

## 11. Real people

A model of a real person is held to rules the engine enforces:

- `real: [self]` (or `real_person: true`): lint fails on any censor cover
  that is a template or has no source. The words have to be theirs.
- `real: [ally, ...]`, a real person elsewhere in the cast: lint fails on
  any event with words and no source.
- Quotes print only beside the action the person actually took (section 7).
- The censors and weights are the modeler's hypotheses, labeled so.
  `ablate` says which of them the record doesn't need.

The policy around the engine, in the
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md):
a model of a living private person's mind stays private until they've seen
it, and they can change or delete any of it. A public figure acting in
public is modeled from a verbatim, sourced public record, with no claim of
intent and an invitation to correct.

## 12. How the engine is tested

- `scripts/test_censor_sim.py`: 37 unit tests of merging, conditions,
  value modes, censor and schema learning, `learn`'s gate, planning, run
  overrides, lint, duets, the simplex (against scipy on 200 random
  problems when scipy is installed), `bounds` on three examples, and the
  dentist example end to end, including the JSON event stream.
- `suite PATH...` lints and tests every scenario, with its answer layer if
  it has one. Across the public kit, WillWrightShowForFood and Don's
  private characters it runs 37 scenarios, two of them duets, all
  passing, with no lint errors.
- `scripts/regen_runs.py` regenerates the committed `RUN.md` outputs, with
  timings stripped; `--check` exits 1 if any is stale.

## 13. What was wrong, and what changed (24 November 2026)

A round of testing found real bugs. Some changed published findings; those
were corrected where they were published.

| Bug | Effect | Fix |
|---|---|---|
| A conflict already standing counted as new pain for every later action | Censors looked necessary that weren't. The baron's crowd: the loyal friend, the fan and the ironist were reported as needing censors | Only a conflict the action creates counts. Corrected: none of the crowd needs a censor; their belonging explains them. The beekeepers' friend needs four |
| `sweep` and `predict` never perturbed weights a run set for itself | Robustness was overstated for runs with their own weights | Factors apply after each run's overrides. Published shares were regenerated and corrected where they moved |
| A joke-installed censor could be mistaken for a learned one | Learning could stop early | Learned censors are found by id, `learned-<action>` |
| A joke that missed its target dropped its lesson too | A lesson never landed | A miss still teaches |
| `lint` and `ablate` ignored censors and jokes a run added itself | Unchecked, unablated parts | Both cover run-level censors and lesson jokes |
| Scoring by change, tried as the default | 17 of 30 scenarios broke: without decay, repeating an action pays nothing | Kept as `score: change`, opt-in |
| Losses as pain, tried as the default | Changed a fit in a public-figure model | Kept as `losses_hurt: true`, opt-in |

New in the same round: schema learning (`learn_schemas`, `learn`, `try`), `plan`, `duet`, `bounds`, the unit tests, `regen_runs.py`, and the
dentist's `book-appointment` schema so planning has somewhere to go.

## 14. Limits

- **It doesn't understand anything.** Items are names. Meaning lives in the
  names, the comments, and the reader.
- **It learns only from what a record records.** A result can be learned
  only if an event sets the item between one choice and the next. Most
  real records describe situations, not outcomes, so the loop's other tier
  has to add sourced outcome events before there is anything to learn.
- **Learning during a run on a record can misattribute.** If the model
  chooses differently from the person, the world's next events answered
  the person's action, not the model's. `learn` replays the observed
  actions for that reason; in a duet the world answers the model, so the
  problem doesn't arise.
- **Unreliable schemas don't yet propose synthetic items.** Drescher posits
  a hidden state when a schema works only sometimes. `propose` does that
  for choices; for schemas it is a request to the other tier.
- **Weights are guesses.** `sweep` measures how much the conclusions depend
  on them; `bounds` says what range the record leaves each one. Neither
  makes them right.
- **`bounds` holds the censors fixed.** Which censors form depends on the
  weights (pain is a loss of value), so the polytope is exact only for
  weightings that form the same censors as the current one. A weighting
  far from the current one should be checked with `test --set`.
- **Ties go to the first offered action.** Two actions with equal value are
  decided by the order of `offers`. Records should list the moves in a
  neutral order, and close calls should be read through `sweep`, where ties
  are rare.
- **A fit is one account, not the account.** When two hypotheses fit,
  the engine says so and `argue` says what would separate them. It never
  reports intent.
- **Items don't decay, and time is just order.** A motive that recovers
  over hours is not modeled; `score: earned` stands in for it.
- **Duets are scripted.** `duet` puts two minds on one stage, but the turn
  order, what each move does to the world, and which turns depend on what
  are written by hand. Nobody chooses when to move.
- **Small records.** Most real records are 4 to 10 choices. The statistics
  are honest about that, but they can't make it more.

## 15. Next

- Duets with more than two seats, and minds that choose when to move.
- `propose` for more than one switch per action.
- Synthetic items for unreliable learned schemas, proposed by the engine.
- Outcome events for the public-figure records, so `learn` has results to find.
- Multi-step `argue`: a sequence of arguments, not one.
- Longer public-figure records, and words grounded in what was actually
  said rather than in item names.

## 16. References

- Marvin Minsky, "Jokes and the Logic of the Cognitive Unconscious", MIT
  AI Lab Memo 603, 1980.
  [Full text](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/marvin-minsky/sources/papers/AIM-603-jokes-cognitive-unconscious-1980.md)
- Gary L. Drescher, *Made-Up Minds: A Constructivist Approach to Artificial
  Intelligence*, MIT Press, 1991.
- Marvin Minsky, *The Society of Mind*, Simon & Schuster, 1986.
- Joseph Weizenbaum, *Computer Power and Human Reason*, W. H. Freeman, 1976.
- Richard Stallman, talk at Georgia Tech, 23 January 2026, on "Pretend
  Intelligence" ([video at 10:41](https://youtu.be/YDxPJs1EPS4?t=641));
  [`PRETEND-INTELLIGENCE.md`](PRETEND-INTELLIGENCE.md).
- The Sims, Find Best Action: [`sims/sims-find-best-action.md`](sims/sims-find-best-action.md).
- Micropolis, SimCity's GPL source: [github.com/SimHacker/micropolis](https://github.com/SimHacker/micropolis).
- The engine: [`skills/schema-mechanism/scripts/censor_sim.py`](../skills/schema-mechanism/scripts/censor_sim.py);
  the manual: [`censors/README.md`](../skills/schema-mechanism/censors/README.md).
