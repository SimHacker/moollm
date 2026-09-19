# `purpose:` — the dimension that answers *why*

*A [Korz example](README.md). Teaches: ambient setpoints, guard lattices over goals,
escalation as the right answer to a value conflict, and why the outsourcing of purpose is
only a problem when it is hidden. Sibling of [moody-temperature](moody-temperature.md) —
mood is how the room feels, purpose is what the scene is for.*

## The proposal

Korz's paper names `rcvr`, `assertions`, `device`, `user`. Between them they answer *what
am I operating on*, *what mode am I in*, *what am I running on*, and *who is looking*.
None of them answers **what this is for**.

```yaml
context:
  rcvr: stack          # what
  user: teacher        # who is looking
  device: tablet       # where
  purpose: teaching    # why          ← the proposal
```

`rcvr` answers *what* the way `self` did in Self. `purpose` is the *why*, and it has never
had a place to live in any language, which is why programs currently smuggle it through
global configuration, a thread-local, a mode flag threaded through forty signatures, or —
most often — not at all, leaving each layer to guess from context it does not have.

## Why the mechanism fits, in three properties

### 1. Implicit propagation is exactly what a setpoint needs

The paper's load-bearing demonstration is `assertions`: `main()` binds it, **no
intermediate code mentions it**, and every send underneath sees it. A purpose has that
shape natively. You establish *why* once, at the top —

```yaml
main:
  purpose: fire-evacuation
```

— and a hundred frames down, a decision that has never heard of evacuations dispatches
correctly anyway. `assertions` is a debug flag. This is the thing programs actually lack.

### 2. It makes the cybernetics mapping literal instead of analogical

[`../../../TELEOLOGY.md`](../../../TELEOLOGY.md) reconstructs the 1943 move —
Rosenblueth, Wiener and Bigelow — as *purpose is a reference signal plus negative feedback
plus error reduction*. In Korz terms:

| Cybernetics | Korz |
|---|---|
| reference signal (setpoint) | the bound `purpose` coordinate |
| the pursuit, where all the science is | dispatch |
| error reduction | specificity ordering — the most specific behavior available *for this why* wins |

Wiener's move lands in Ungar's lattice with nothing left over. Purpose stops being a thing
a system mysteriously *has* and becomes a thing a context *carries*.

### 3. The guard lattice already exists, and you already wrote one

Guards need a partial order (`purpose ≤ teaching` must match both `teaching-a-child` and
`teaching-an-expert`). Goals have one natively, and
[robust-first](https://github.com/SimHacker/moollm/tree/main/skills/robust-first) ships it:

```text
survive  ≥  heal  ≥  function  ≥  optimize  ≥  adapt  ≥  reproduce
```

Hierarchical goal decomposition is the oldest structure in planning. The lattice is not
something you would be inventing.

## What it buys

### Variants selected by *why* instead of by *what*

```yaml
- slot: explain
  guards: {rcvr: ≤ perceptron}
  body: "weights, bias, activation, the update rule"

- slot: explain
  guards: {rcvr: ≤ perceptron, purpose: ≤ teaching}
  body: "one neuron that leans toward a guess and gets corrected"

- slot: explain
  guards: {rcvr: ≤ perceptron, purpose: ≤ teaching-a-child}
  body: "duplicate the sprite to add a layer — no hidden magic, this is it"

- slot: explain
  guards: {rcvr: ≤ perceptron, purpose: ≤ debugging}
  body: "dump the gradient at each layer and say which one saturated"
```

No conditional, no mode parameter, no strategy object, no visitor. Jens Mönig's keynote is
that dispatch table: one perceptron, explained at whatever level the room is for, and the
room's level is a coordinate rather than a branch
([closing-keynote-jens-neural-networks.md](../../../snap/snapcon-2025/closing-keynote-jens-neural-networks.md)).

### The advertisement economy gets the half it was missing

In The Sims an object's advertisement is scored against the receiver's motives, and the
receiver is the only source of context
([sims-advertisements.md](sims-advertisements.md)). With purpose ambient:

```yaml
- slot: advertise
  guards: {rcvr: ≤ fridge}
  body: {hunger: 40}

- slot: advertise
  guards: {rcvr: ≤ fridge, purpose: ≤ fire-evacuation}
  body: {}                      # a fridge advertises nothing during an evacuation
```

No motive override, no special case, no code between the alarm and the fridge. Mood
already proved the pattern works as a dimension; purpose is mood's sibling and the more
load-bearing one.

### Refusing to act without knowing why, for the cost of one guard

A **bare-name** guard means *must be bound to something*:

```yaml
- slot: launch
  guards: {purpose: bare}       # will not dispatch in a context with no why
```

That is a safety primitive with no runtime, no checker, and no policy engine. The absence
of a purpose becomes a dispatch failure instead of a silent default.

## The three places it breaks

### Ties stop being compile errors and become dilemmas

Korz's rule is that an ambiguous match is an error, which is correct for a compiler and
wrong for ethics. Two equally specific slots under `purpose ≤ safety` and
`purpose ≤ honesty` is the genuinely hard case, and specificity has no opinion.

Korz′ already contains the answer: a tie is a **deoptimization event**. It escalates from
the strict tier to the soft tier, gets resolved by judgment, and leaves a record
([../README.md](../README.md)).

```yaml
dispatch:
  context: {purpose: [safety, honesty]}
  matched: [tell-the-truth, protect-the-patient]
  specificity: tie
  action: deopt          # upstairs, with the tie in the transcript
```

Which is the right escalation policy stated as a mechanism rather than as a principle. A
value conflict should go up and leave a trace; it should not be settled by whoever
happened to write a narrower guard.

### Purpose may not be one axis

Sims motives are a *vector*; real goals are simultaneous and weighted. A Korz context
binds one coordinate per dimension. Three options, none obviously right:

1. **One axis, one purpose at a time.** Cheapest, and loses simultaneity — which may be
   fine, since a scene usually *is* for one thing at a time and the rest are constraints.
2. **Split the family:** `purpose`, `constraint`, `audience`, `deadline`. More dimensions,
   each with a clean lattice, and the interactions move into specificity where they are
   at least visible.
3. **A composite coordinate** with its own ordering — a weighted goal vector compared by a
   domination relation. Most expressive, and the first place `specificity: tie` stops
   being rare.

This is the question for David rather than something to settle in an example file. Logged
in [ask-david.md](../../ask-david.md).

### "Whose purpose" becomes structural — which is the good news

If the binding flows implicitly, **whoever binds it at the top owns the telos of
everything beneath**. That is precisely the outsourcing that
[`TELEOLOGY.md`](../../../TELEOLOGY.md) identifies in a loss function: a setpoint installed
from outside, at training time, by whoever paid for the GPUs, leaving a system with no
telos of its own at run time.

The difference, and it is the entire argument for doing this in Korz′ rather than in
weights: **the binding is a coordinate in a context you can print.** Any frame can be
asked what it is for; you can see who bound it and where it changed. The outsourcing is not
the problem. Hiding it is.

## Two consequences worth noting

**The stack trace explains itself.** A conventional trace says how you got here. A
purpose-bound context says what each level was *for*, and where the why changed — which
is where Kay's unsolved automatic inverter wants to live. An inverter needs to know what a
change was *for* in order to run the mapping backwards, and this puts that information at
the site instead of requiring it to be reconstructed after the fact
([`TELEOLOGY.md` open questions](../../../TELEOLOGY.md)).

**Alignment becomes lookup rather than exhortation.** An agent asking *should I?* is
dispatching against the currently bound purpose, not consulting a rulebook — and the
answer changes with context without anyone editing the agent.

## E-Prime for teleology

Korz is E-Prime for objects ([../../README.md](../../README.md)): the rose is not red,
redness lives in the dispatch. Purpose as a dimension is **E-Prime for teleology**: the act
is not good, goodness lives in the dispatch against a bound purpose.

Which relocates the standing objection rather than dismissing it. Haig Shahinian's demand
in the Kay thread is for purpose to be *intrinsic* — a property a subjective unity
possesses — and Korzybski's whole argument is that the intrinsic reading is the error. The
structural form of his question survives the translation and improves:

> Not *is someone in there*, but **can a system bind its own purpose coordinate?**

Which is autopoietic closure, which is the argument he had available on the merits, and
which is now a yes-or-no question about mechanism. For MOOLLM today the answer is no, and
saying so is the honest limit already recorded in `TELEOLOGY.md`.

**See also:** [moody-temperature.md](moody-temperature.md) — the room writes the bindings ·
[sims-advertisements.md](sims-advertisements.md) — what purpose modulates ·
[../../case-mystery-and-art.md](../../case-mystery-and-art.md) — the whydunit is the
detective genre of this dimension ·
[../../../TELEOLOGY.md](../../../TELEOLOGY.md) — where the setpoint argument comes from
