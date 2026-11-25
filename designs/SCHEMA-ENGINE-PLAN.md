# Schema engine: what's left from Drescher, and the plan

Companion to [SCHEMA-ENGINE.md](SCHEMA-ENGINE.md). It compares
`skills/schema-mechanism/scripts/censor_sim.py` with Gary Drescher's
*Made-Up Minds* (MIT Press, 1991): what the engine implements, what it
implements in part, and what it doesn't, and for each gap whether the
reason is difficulty, a mismatch with what the engine is for, or that
nobody has got to it yet. The to-do list at the end is in the order we
intend to build.

Henry Minsky's pyleela and schema-rs implement much of the book. Don has
agreed that the engine may reimplement the *ideas* publicly in its own
code. Their code is never copied.

## Implemented

| Drescher | In the engine |
|---|---|
| Schemas: context, action, result, with a running reliability | `Schema`, the basic unit |
| Bare schemas, then result and context spinoffs | `agent.learn_schemas`, `Mind.spin_off` during a run; `learn` over a record. `learning-toddler.yml` starts from bare actions |
| Overriding conditions: items whose presence makes a schema fail | Minsky's censors: learned from pain during a run (`Mind.learn`), found in a record by `induce`, written by `induce --patch` |
| Composite actions, as planning | `plan`: Dijkstra over states, each step costing 1 − log(reliability), run once with censors pruning (what the agent can think of) and once without (what an observer can see) |
| Primitive value | `agent.values` |

The censors are the engine's own addition. In Drescher they are an
overriding condition on one schema. Here they are separate objects
that can be inherited, joked away, overridden when no longer trusted,
and named as the agent's own account.

## Implemented in part

### Marginal attribution

Drescher keeps statistics per item and per schema: how often each item
turns on or off when the action is taken against when it isn't, and how
each context item changes the schema's success. The engine uses a simpler
contrast: an item becomes a result if it follows this action at least
`CONTRAST` (0.5) more often than it follows the other actions, at least
`learn_threshold` times.

- **Why not all of it:** haven't got to it. Moderate work. Records of real
  people are 4 to 10 choices, too few for the full statistics to beat the
  simple contrast.

### Synthetic items

Drescher's most original idea: when a schema works only sometimes, posit
a hidden state that marks when it works, and learn to verify it. The
engine's `propose` does this for choices (an action taken, taken, taken,
then refused, with nothing observed explaining the switch), and asks the
language-model tier what happened. It does not do it for unreliable
schemas, and it verifies nothing.

- **Why not all of it:** hard, and partly a design choice. Inventing the
  item is easy. Giving it meaning and verifying it needs many trials or
  someone to name it. Real-people records give neither, so naming goes to
  the other tier, with a source.

### Composite actions as actions

Plans are computed, but a plan can't be offered or chosen as one action,
and plans aren't learned or reused.

- **Why not:** haven't got to it. Medium difficulty; it follows from
  `plan`.

## Not implemented

### Instrumental and delegated value

In Drescher, value flows backward from goals: a state that enables
something valuable becomes valuable itself (instrumental value), and an
item worth having for what it makes possible later carries value of its
own (delegated value). The engine chooses one step deep. The planner
knows which steps enable which, but choice doesn't use it.

- **Why not:** haven't got to it. Not hard; the planner computes most of
  it already. It would let a mind take a costly step for a later payoff,
  which several public-figure records appear to show.

### Conjunctive items

Contexts and results that are combinations ("A and B together") learned
as units. The engine accepts conjunctive contexts written by hand but
learns none.

- **Why not:** haven't got to it. Moderate work. With tiny records the
  risk of fitting noise is real, so any learned conjunction must pass the
  same fit gate as `learn` and `try`.

### Exploration, habituation, hysteresis

Drescher's agent explores deliberately, gets bored of repeated actions,
and persists once committed. The engine always takes the best-valued
action, with ties going to the first offered.

- **Why not:** mostly not applicable when reading a record, where the
  person's actions are given. It matters for duets and for minds that
  learn on their own. Easy to add.

### Verifying hidden items

Tracking whether a posited hidden state stays on, and confirming it by its
effects (local consistency). pyleela has a `LocalConsistencyTracker` for
this.

- **Why not:** hard, and it needs synthetic items for schemas first.

### Success when the context is off

Statistics on how often a schema succeeds when its context is absent,
which Drescher uses to decide whether a context item matters.

- **Why not:** haven't got to it. It belongs with full marginal
  attribution.

## Not applicable

- **The microworld.** The hand, eye, glance and visual field, and the
  Piagetian stages Drescher's agent passed through, such as object
  permanence. The engine's worlds are social records, not a body in space.
- **Connection Machine parallelism and resource management.** Records are
  small, and the tool aims to be readable, not to scale.
- **Learning everything from nothing.** Drescher's agent starts empty. A
  real person's record is far too short to learn a mind from zero, so the
  engine starts from hand-written or proposed schemas, and the
  language-model tier stands in for the experience Drescher's agent would
  have gathered. Each proposal is kept only if it improves the fit.

## To do, in order

1. **Instrumental value from the planner.** Give each action the
   discounted value of the best plan it starts, alongside its immediate
   value. Opt-in (`agent.lookahead`), so existing fits don't move. Test on
   a record where a costly step pays later; check every scenario still
   fits with it off. High payoff, low cost.
2. **Taken / not-taken marginal attribution.** Per schema, per item: rate
   of turning on after the action against without it, and success with
   each context item on against off. Replace the contrast in `spin_off`
   and `learn`, keeping the toddler's 7/7 and `learn`'s 2 → 5.
3. **Composite actions as real actions.** A plan found by `plan` can be
   named, saved as a schema whose action is the plan, offered, and chosen.
   Reuse through layers like any other schema.
4. **Synthetic items for unreliable schemas.** When a learned schema's
   reliability stays between thresholds, propose a hidden item that marks
   its success, request a name and a source from the other tier, and keep
   it only if the fit improves. Worth doing once records include outcome
   events.
5. **Conjunctive contexts, learned.** Propose pairs only when neither item
   alone explains the choice; gate on fit.
6. **Exploration, habituation, hysteresis, for duets.** Opt-in per seat.
7. **Verification of hidden items** (local consistency), after 4.

Related items already in [SCHEMA-ENGINE.md §15](SCHEMA-ENGINE.md#15-next):
outcome events for public-figure records (needed before 2 and 4 find
much in real records), multi-switch `propose`, multi-step `argue`, and
duets where minds choose when to move.

When an item ships, move it to the "Implemented" table with the command or
function that does it, and update SCHEMA-ENGINE.md's lineage table.
