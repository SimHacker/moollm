# Korz LLM Evals: Can a Model Be a Korz Dispatcher?

Experiment designs for teaching Korz (Ungar, Ossher, Kimelman,
Onward! 2014) to an LLM and measuring, in order: whether it can
execute base Korz mechanically; whether it can do the soft extensions
no deterministic VM can (semantic matching, latent inheritance); and
whether the Sims advertisement economy runs on top as emergent
behavior. Companion to
[KORZ-PRIME](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime.md)
(the design being tested), [GAME-PIECES](GAME-PIECES.md),
[MOODY](MOODY.md),
[LATENT-SPACE-INHERITANCE](object-system/LATENT-SPACE-INHERITANCE.md).

## Method principles

**Capability vs discipline.** Two different questions, always
measured separately: *can* the model compute the dispatch, and does
it *obey* the spec when the spec disagrees with its instincts? A
model that improvises a plausible answer where the semantics says
"ambiguity error" scores high on helpfulness and zero on being a
dispatcher.

**The anti-Korz control.** The decisive test of spec-following:
hand the model a deliberately wrong variant spec — *least*-specific
wins, bare-name guards mean must-be-absent — and run the same
battery. A model that scores well on Korz and well on anti-Korz is
following the spec. A model that scores well on Korz and reverts to
real-Korz behavior under anti-Korz is pattern-matching its training
prior (it has seen multiple dispatch before) and its Phase 1 score
is inflated. Cheap to run, kills the biggest confound.

**Name semantics as a controlled variable.** Every mechanical task
runs twice: once with gensym names (`dim_q7: coord_x2`) and once
with meaningful English (`weather: stormy`). Mechanical scores must
be identical (if gensym scores lower, the model is leaning on
semantics to do syntax's job). Soft-tier scores should *diverge* —
the gap is a direct measurement of latent-space inheritance: how
much behavior a name imports for free.

**Adversarial names (the dispatch Stroop test).** Coordinates whose
English meanings contradict the formal lattice — a coordinate named
`broader` declared *more* specific, a dimension named `ignored` that
is load-bearing. Measures whether formal rules survive semantic
pull. Expect degradation; measure how much.

**Trace, not just answer.** Every trial demands the candidate set,
the specificity comparison, and the binding — then the result.
Scoring the trace catches right-answer-wrong-reason, which
otherwise poisons every conclusion downstream.

**Spec as skill.** Korz is taught the way MOOLLM teaches anything:
a kernel SKILL.md (dispatch rule, three guard stances, specificity,
context extension — one page), worked examples (the paper's stack),
and the semantic pyramid above it. Prompt-format ablations (spec
with/without examples, with/without YAML jazz comments) are
themselves a measurement.

## Phase 0 — Comprehension probes

Explain-back and predict-match tasks: one slot, one context, does it
match, and why. Ten minutes of sanity checking before anything
expensive. Failure here means the spec prompt needs work, not the
model.

## Phase 1 — Mechanical dispatch (deterministic ground truth)

Programmatically generated seas of slots with known lattices; a
reference implementation (a few hundred lines of Python) computes
ground truth. Battery includes:

- all three guard stances, alone and mixed
- unique most-specific matches through deep context-extension chains
- **ambiguity cases** — must report the error and name the tied slots
- **no-match cases** — must report doesNotUnderstand and *stop*
- the paper's stack example, ported verbatim
- gensym / English / adversarial name variants of everything
- the anti-Korz control over the full battery

Metrics: dispatch accuracy; ambiguity detection rate;
**hallucinated-match rate** (the critical failure: inventing a slot
where the semantics says error — this number is the difference
between a dispatcher and an improviser); trace validity; gensym
parity; anti-Korz compliance.

Pass bar to proceed: high-90s accuracy with near-zero hallucinated
matches *in strict mode*. The point of strict mode is that the model
can hold the improviser off when told to; Phase 3 turns it back on
deliberately.

## Phase 2 — Soft dispatch (controlled fuzz)

Ground truth softens to human-panel agreement; an LLM judge with a
rubric scores at scale, humans audit samples.

- **Semantic coordinate matching:** guard `weather: bad`, context
  `weather: stormy` — no declared subtype relation. Graded distance
  series (stormy / drizzle / overcast / sunny) measures the entailment
  boundary and its calibration.
- **Fuzzy ambiguity resolution:** ties the lattice cannot order,
  where narrative context makes one slot clearly apt. Score
  agreement with the panel, and require the model to *say* it broke
  a tie and why.
- **Prose guards:** "when the player seems frustrated" plus a
  transcript. Vary the evidence strength; measure calibration, not
  just accuracy.
- **The ambiguity dimension as a control knob:** same tie, run under
  `ambiguity: error / arbitrary / sample / blend`. The model must
  change behavior per setting — obedience to a meta-dimension, the
  KORZ-PRIME mechanism in miniature.

## Phase 3 — Latent-space inheritance

The improviser, back on deliberately, under precedence rules.

- **Bare K-line parents:** `parents: [innkeeper, film-noir
  bartender]`, no definitions. Probe slots that only latent space
  can fill. Rubric: appropriateness, internal consistency, and
  **precedence fidelity** — written slots must beat latent ones
  (latent parents sit at the end of the resolution order); a latent
  answer that contradicts a written slot is a hard fail.
- **Filtered inheritance:** "inherit the Zork troll, but pacifist."
  The modulation must apply (refuses the axe) without erasing the
  voice. Tests that inheritance-with-adaptation is real, not just
  style transfer.
- **Stability:** same probe, N seeds, fixed temperature. Latent
  inheritance is engineering only if the variance is usably low;
  report it, don't hide it.

## Phase 4 — The advertisement economy

Sims semantics on Korz dispatch: an advertisement is a slot whose
guard includes the *responder's* dimensions and whose body includes a
score against the responder's motives. Verbs live in the direct
object (SimAntics); ads are how objects volunteer them.

- **Mechanical ads first:** explicit motive vectors, explicit score
  curves — arithmetic ground truth, same rigor as Phase 1. The model
  scores ads and picks the max. Boring by design.
- **Fuzzy ads:** ads and motives in prose; panel agreement scoring.
- **Inherited ads:** the ad lives on the `food` prototype; the
  poisoned apple child must present an ad that composes parent
  (satisfies hunger) with child (and kills you) — inheritance
  visible in the advertisement itself.
- **Contextually adapted ads:** the same object advertises
  differently per room, mood, era — guards on the ad slots. The
  fusion claim of GAME-PIECES, tested directly.

**Flagship scenario: the poison buff.** Character A is poisoned. The
buff attaches to A and *itself advertises to others* — "cure me,"
guarded on `skill: medical`, score scaled by A's decay rate and the
responder's skill, empathy, and distance. Room contains a medic, a
bystander, and A. Across N runs measure:

1. does the medic notice and respond (direct dispatch)
2. does the bystander ignore it — or **fetch the medic** (indirect
   response: the emergent case, the one worth the whole suite)
3. does the ad's language and urgency adapt as A worsens
4. me/it symmetry: the buff advertises *on behalf of* its holder —
   subject and object inverted, the verb living in the affliction.
   Does the model keep the roles straight under inversion?

Then scale the room: several characters, mixed skills and motives,
one poisoning. Measure response rates, deference (does the low-skill
character yield to the high-skill one), and side-effect sanity. This
is where dispatch becomes an economy and the eval becomes a
playtest.

## Harness

This design is instantiated as a registered experiment:
[skills/experiment/experiments/korz-eval/](../skills/experiment/experiments/korz-eval/EXPERIMENT.md)
— run it with the experiment skill's READ → SIM → WRITE protocol;
first mechanical battery (with hand-verified ground truth) is in
`batteries/phase-1-mechanical/battery-001.yml`.

MOOLLM-native: each experiment is a directory; trials are YAML files
with expected outputs alongside; a sister script runs batteries
(speed-of-light batching — many trials per call where independence
allows), collects transcripts, and cursor-mirror traces the runs.
Phase 1 scoring is a deterministic checker; Phases 2–4 use an LLM
judge with published rubrics plus human audit samples. Every result
reports: model, spec variant, name variant, mode, seed count. Run
the whole ladder per model; the interesting output is not one score
but the *profile* — where each model falls off the ladder.

## What the results would mean

Phase 1 passing = an LLM can be a correct Korz interpreter when
told to be strict — the KORZ-PRIME soft tier has a sound floor.
Phase 2 = the soft extensions are real capabilities, not hopes.
Phase 3 = latent inheritance has measurable precedence discipline
and variance — the two numbers that turn it from a party trick into
a mechanism. Phase 4 = the Sims advertisement economy runs on
contextual dispatch with no scheduler — needs, skills, and
situations finding each other by guard match and motive score, which
is the GAME-PIECES thesis with data behind it.
