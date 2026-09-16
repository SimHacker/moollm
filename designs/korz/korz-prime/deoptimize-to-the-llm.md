# Deoptimize to the LLM: inference as tier 0 of a tiered JIT

The Self VM solved the hardest problem in dynamic language implementation
with a tiered architecture: run everything in a slow, maximally flexible
interpreter; let hot, stable code crystallize into optimized machine
code via type feedback and hidden classes ("maps"); and when a compiled
method's assumptions break, **dynamically deoptimize** — fall back to the
interpreter, mid-execution, and carry on. (Don's pet name, stated to
David Ungar directly: *pessimization*.) That lineage became HotSpot and
V8; it's running in your browser tab right now.

MOOLLM runs the same architecture with the interpreter replaced by an
inference engine.

## The tiers

**Tier 0 — the LLM as maximal interpreter.** A microworld is a sea of
guarded slots in YAML: characters, rooms, buffs, house rules,
advertisements, written instance-first with fuzzy ad-hoc schemas. The LLM
evaluates guards by inference, fills unbound dimensions from latent
space, and has a *generative miss handler*: an unmatched send doesn't
fault, it improvises in character — and the ruling gets lifted into a new
slot so next time it's deterministic. (Play-Learn-Lift is type feedback
for meaning.)

**Tier 1 — the crystallized subset.** Gelling is schema inference over
usage: which dimensions actually occur, which guards are decidable
predicates over enumerable coordinates, which scores have settled into
arithmetic. That subset compiles — the
[adventure compiler](https://github.com/SimHacker/moollm)
emits deterministic JS from natural-language scripts, and gelled mixin
combinations compile to dispatch tables and ECS archetypes
([Game Pieces](https://github.com/SimHacker/moollm/blob/main/designs/GAME-PIECES.md)
works the chess/ECS case). Prototypes for authoring, classes for the
machine to discover: maps, one level up.

**Coherence** comes from subset semantics plus monotone extension. The
VM's semantics are a subset, never a translation: anything the VM runs
means the same thing to the LLM, and everything the LLM adds — new
dimensions, fuzzy guards, improvised slots — is a monotone addition the
VM treats as absent-therefore-default, Postel-style. The engines never
disagree about the crystal, only about the cloud around it.

**Deoptimization closes the loop.** When runtime invalidates a compiled
assumption — a revolution rewrites the rules, a player does something no
table anticipated — fall back to tier 0: re-engage the LLM, let coherence
handle the surprise in character, lift the ruling, recompile. Dynamic
pessimization with inference as the fallback tier.

## The dispatch spectrum

Where the tiers meet, dispatch policy is a knob, not a religion:

| Policy | Who ships it | Crystallizable? |
|---|---|---|
| **argmax** — most specific slot wins | Korz (Ungar/Ossher/Kimelman), classical dispatch | Trivially: table lookup |
| **find-best-N** — score all, pick randomly among top N | The Sims' autonomy — deliberate dither, organic not digital; ties become personality | Yes: scoring table + seeded RNG (log the seed; replays must not diverge) |
| **softmax** — temperature over judged salience | The LLM natively; temperature sampling is find-best-N's continuous generalization | Only where scoring gels into arithmetic |

The dither in the middle row is load-bearing, not sloppy: scores are
approximations at best and intentional lies at their cleverest (Sims
objects hustle each other down the food chain), so argmax over lies is
just being deterministically conned; random picks among strong
candidates escape local maxima; and visible imperfection is what leaves
the player room to teach by overriding — an agent that always takes its
own best guess cannot learn from demonstration, because its teacher has
nothing to add. The full argument lives in the
[Korz deep dive](../sources/korz-paper-deep-dive-moollm-mapping.md).

The crystallization frontier runs exactly along the line between
*specificity you can sort* and *salience you must judge*. And the knob
composes contextually: make temperature a context value and
`{temperature: 0}` recovers classical deterministic dispatch, the party
planner runs hot while the accountant runs cold, and a scene sets its
dither once, inherited implicitly by every decision inside it. Ambient
heat can even come from the room itself, inherited time-varying from
**moody media** playing in it — media artifacts carrying semantic heat
tracks that broadcast while they play
([MOODY.md](https://github.com/SimHacker/moollm/blob/main/designs/MOODY.md)).

## Lineage

Self's tiered VM and dynamic deoptimization (Ungar, Chambers, Hölzle) ·
Korz's contextual dispatch and subjective objects
([deep dive](../sources/korz-paper-deep-dive-moollm-mapping.md)) ·
The Sims' advertisement scoring and find-best-N (Wright et al.; Don built
the object system tooling) · OpenLaszlo/Declare instance-first
development (Temkin, Steele) · the adventure compiler and Play-Learn-Lift
(MOOLLM). Companion essay:
[Teaching complicated systems without a manual](../../teaching-complicated-systems-without-a-manual.md).
