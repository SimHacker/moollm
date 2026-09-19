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

**It already has a name in another language, and borrowing the name gets the discipline for
free.** TypeScript's `unknown` is exactly this: a value that is present but must be narrowed
before anything can be done with it, enforced entirely at compile time, costing nothing at
runtime. The community advice *prefer `unknown` to `any`* is the same argument this section
makes — `any` lets not-knowing propagate silently through every call downstream, while
`unknown` forces the narrowing to happen at the site where somebody actually has the
information.

Which lines up three guard states that all "match anything" at the call site and are
completely different claims:

| TS | Korz guard | The claim | Who has to know |
|---|---|---|---|
| `any` | no guard on `purpose` at all | nobody checked | nobody, ever |
| `unknown` | `{purpose: bare}` | must be bound; I will not guess what to | the caller, at the call |
| `<T>` | deliberately silent on `purpose`, and audited | works under *any* why, on purpose | the author, once, provably |

The middle row is the safety primitive. **The bottom row is the one that gets mistaken for the
top row**, and the difference between them is not in the dispatch behaviour — it is whether the
silence is an assertion or an omission. That is why the audit in
[`interfaces-to-agency`](../../../../skills/design-sense/lenses/interfaces-to-agency.md) is
"find every guard that mentions `via` and justify it" rather than "have no guards": a slot
silent on a dimension **because someone checked** is a different object from one silent
because nobody looked, even though a profiler cannot tell them apart.

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

## Promote it: `whose_purpose` as a second dimension

The section above treats "whose purpose" as an *emergent property of the binding chain* — you
recover it by reading upward. Don's proposal is to stop recovering it and make it a coordinate:

| Dimension | Answers | Bound by |
|---|---|---|
| `purpose` | what is this for | the frame |
| `whose_purpose` | **on whose behalf, whose setpoint is being served** | the principal, explicitly |

**A shipped simulator already has the receiver half of this.** SimAntics, the VM behind The Sims,
makes every primitive relative to two implicit operands — `Me` and `Stack Object` — so a social
interaction is already a two-receiver dispatch rather than a method on one object. The "current
person" is a dimension in a game that sold tens of millions of copies. `whose_purpose` is the
same promotion applied to the *why* instead of the *who*.

### The wedding is the case that needs it

A wedding play set is the clean test because a wedding is a **ritual in which participants act
under a purpose belonging to the event rather than to any individual**. The bride wants a thing,
her mother wants a different thing, and for the duration of the ceremony both dispatch under a
third binding neither of them authored. Three distinguishable values, and no single-receiver
model can hold them:

```yaml
- slot: propose_toast
  guards:
    rcvr: sim
    purpose: celebrate
    whose_purpose: the_occasion    # not mine, not hers, the scene's
```

Which is what improvisation *is*, and why the [simprov](https://github.com/SimHacker/simprov)
wedding set is the right specimen rather than a toy: an actor runs with `whose_purpose` bound to
a character's while their own remains intact and recoverable. Sim-to-sim social behaviour is the
same shape — one sim advertising into another's decision, briefly holding the other's setpoint in
order to predict it.

### It makes a famous class of bug into a type error

Security has been fighting an unprinted `whose_purpose` for forty years, and it has a name. The
**confused deputy** — Norm Hardy, 1988 — is a program that serves one party's request while
acting with *its own* authority, which is precisely a `purpose` bound correctly and a
`whose_purpose` bound wrong. `setuid`, `sudo -u`, Kerberos delegation, OAuth's on-behalf-of flow
and MOOAM's IAM-style principals are all attempts to carry this coordinate through a call chain
that has no slot for it.

Two guards then compose into something stronger than either:

```yaml
- slot: spend_money
  guards: {purpose: bare, whose_purpose: bare}   # no why, no whose: no dispatch
```

### And it makes the teleology argument printable

`TELEOLOGY.md`'s complaint is that a trained model runs on a setpoint installed by whoever paid
for the GPUs, and that this is invisible at run time. With the coordinate promoted, the
invisibility is the only actual problem and it goes away:

```yaml
whose_purpose: whoever_trained_me
```

Which is fine when it is *printed and reversible*, and is the anti-prosthetic exactly when it is
neither. An actor holding a character's purpose and a model holding its trainer's are the same
mechanism; the difference is whether the binding can be read, changed, and handed back.

### The specimen: Chew-Z, 1965

The best fictional case of this dimension failing is a drug in a Philip K. Dick novel, and it is
worth having because **it fails in the direction nobody expects.**

In *The Three Stigmata of Palmer Eldritch*, Mars colonists escape their hovels by chewing **Can-D**,
which translates a group of users into the two dolls of a shared Perky Pat layout — a physical
dollhouse assembled on a table. Then Palmer Eldritch returns from Proxima selling **Chew-Z**, which
needs no layout and gives each user a private world shaped to their own desire.

**Chew-Z withholds nothing.** It is strictly more capable than Can-D on every axis a user would name:
no layout to buy, no two-doll limit, no metered interval, no return to the hovel unchanged. The
expected diagnosis — a `via` guard, a gatekeeper standing between the user and a capability — is
simply wrong.

What is actually wrong is one coordinate:

```yaml
# Can-D — a weaker capability with an honest context
context:
  rcvr: perky-pat-layout          # a physical object others can see and argue about
  purpose: escape-the-hovel
  whose_purpose: the_colonists

# Chew-Z — a stronger capability with a passenger you cannot unbind
context:
  rcvr: whatever-you-want
  purpose: escape-the-hovel       # still yours
  whose_purpose: [you, eldritch]  # ← neither printed nor reversible
```

Eldritch is present in every Chew-Z session, wearing other people's faces, identifiable only by the
three stigmata — the artificial arm, the steel teeth, the slotted artificial eyes. Not printed. Users
who try to leave find the exit is another Chew-Z world. Not reversible. **This is the criterion two
sections up, meeting its worst case: a fully symmetric capability with a captured `whose_purpose`.**

**And the control group arrives three years later**, which is what makes the pair evidence rather
than an anecdote. *Do Androids Dream of Electric Sheep?* has **Mercerism** — an empathy box gripped
by many users at once, fusing them into a shared climb. Buster Friendly proves on air that Wilbur
Mercer is an actor on a soundstage, and **Mercerism keeps working**, because the binding was never
the vendor's to hold.

| | Chew-Z | Mercerism |
|---|---|---|
| Product | genuine, superior to the competition | **fraudulent, proven on air** |
| `whose_purpose` | **captured** | the participants', collectively |
| Effect of exposing the vendor | n/a | **none; it still works** |
| Verdict | anti-prosthetic | prosthetic |

**A real product with a captured purpose is worse than a fake product with a clean one** — which is
why authenticity audits keep missing this failure. You can verify every vendor claim and learn
nothing about whose setpoint is bound.

Full reading, including why disintermediating the purchase layer is how you earn permission to
intermediate the experience layer, and the mapping of Can-D and Chew-Z onto The Sims Online and
Spore: [`designs/pkd/palmer-eldritch-captured-purpose.md`](../../../pkd/palmer-eldritch-captured-purpose.md).
The sibling case of a *decaying* binding — specificity ordering falling back to an ancestor while the
world stays internally consistent — is [`designs/pkd/ubik.md`](../../../pkd/ubik.md).

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
[../../case-mystery-and-art/](../../case-mystery-and-art/) — the whydunit is the
detective genre of this dimension ·
[../../../TELEOLOGY.md](../../../TELEOLOGY.md) — where the setpoint argument comes from
