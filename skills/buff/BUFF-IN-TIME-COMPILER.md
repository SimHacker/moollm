# The buff-in-time compiler

> *A JIT, for buffs. English is the source language; `_js` and `_py` snippets are
> the object code; the deterministic adventure engine is the machine.*

A buff is written in English, because that is the notation a person — or a
character, or a player — can actually author in:

```yaml
buff:
  name: "Sugar Crash"
  host: character/timmy
  guard: "only while he is still indoors"
  tick: "lose a bit more energy each turn, faster the longer it goes on"
  expires: "when he falls asleep, or after about ten turns"
```

Nothing in that is runnable. Evaluating it means asking a language model, every
turn, for every buff, on every host — which is slow, costs money, and gives a
different answer each time. So the compiler turns each expression into a code
snippet, in both runtimes, stored next to the English that produced it:

```yaml
buff:
  name: "Sugar Crash"
  host: character/timmy
  guard: "only while he is still indoors"
  guard_js: "return !subject.room.hasTag('outdoors')"
  guard_py: "lambda world, subject, verb, object: not subject.room.has_tag('outdoors')"
  tick: "lose a bit more energy each turn, faster the longer it goes on"
  tick_js: "modify_effective(subject, 'energy', -(1 + Math.floor(world.buffAge(this) / 3)))"
  expires: "when he falls asleep, or after about ten turns"
  expires_js: "return subject.asleep || world.buffAge(this) >= 10"
```

Now the engine runs it: deterministically, at native speed, the same way twice,
with no model in the loop.

## This is mostly already built

The buff-in-time compiler is a **naming and a specification of a pipeline that
already exists** for other fields. The existing parts, verified 1 Sep 2026:

| Piece | Where |
|---|---|
| The dual-runtime rule: every expression compiles to both `_js` and `_py` | [`events/COMPILE_EXPRESSION.yml.tmpl`](../adventure/events/COMPILE_EXPRESSION.yml.tmpl) |
| Compile requests as typed linter events, emitted per unimplemented expression | [`adventure.py`](../adventure/adventure.py) |
| The closure signature `(world, subject, verb, object)`, parallel-safe | [`engine.js` `compileJs`](../adventure/engine.js) |
| Resolution order — compiled closure first, static value as fallback | `engine.js` `resolveText`, `field` → `field_js` → `field_js_fn` |
| Warm cache of the eval'd function on the object itself | the `_js_fn` slot, populated on first use |
| English kept beside its compiled form, so the diff is reviewable | the `guard` / `guard_js` pair on exits |
| `active_buffs` on characters; `buff` recognized as a document type | `adventure.py` |
| The compile brief that tells the model the buff vocabulary, citing `EFFECTIVE-VALUES.md` as its documentation | `adventure.py` runtime context |

What is missing is the **runtime half**. The compile brief promises the model a
vocabulary of `i_have_buff`, `i_add_buff`, `i_remove_buff`, `get_effective`,
`modify_effective` and `multiply_effective` — and neither `engine.js` nor
`adventure_runtime.py` contains the string `buff` or `effective` at all. A
snippet compiled faithfully against the current brief throws at play time.

That is the first thing to fix, and it is a small, well-specified job: implement
the advertised vocabulary in both runtimes, then add the buff record itself with
the fields below. The contract is already written; only the implementation is
absent.

## Which fields compile

Every expression-shaped field on a buff gets the same treatment. All of them use
the existing `(world, subject, verb, object)` signature, where `subject` is the
**host** — so the same snippet works whether the host is a character, a room, an
object, or a relationship:

| Field | English says | Compiles to | Returns |
|---|---|---|---|
| `guard` | when this applies at all | `guard_js` / `guard_py` | boolean |
| `applier_guard` | who is allowed to apply it | `applier_guard_js` | boolean |
| `effect` | the modification | `effect_js` | void, via `modify_effective` |
| `tick` | what happens each turn | `tick_js` | void |
| `expires` | when it ends | `expires_js` | boolean |
| `radiates.while` | the spatial or relational guard on who it reaches | `while_js` | boolean |
| `stacks_with` | how it combines with its own kind | `stacks_with_js` | a policy value |

A purely numeric buff needs no compilation at all — `effect: { energy: +2 }` is
already data, and the compiler should leave it alone. The compiler earns its
keep only where the English is doing work no data structure can hold.

## The JIT correspondence

This is Self's speculative optimization applied to *semantics* rather than to
types, which is why the analogy pays for itself instead of just being a pun.

| JIT | Buff-in-time |
|---|---|
| Source language | English on the buff |
| Bytecode interpreter — correct, slow, always available | the language model judging the prose |
| Compiled code — fast, specialized, assumption-dependent | the `_js` / `_py` snippet |
| Warmup: interpret until it is worth compiling | run judged the first few times, compile once the behavior is stable |
| Type guard on entry to compiled code | the snippet's own assumptions about what exists in the world |
| Deoptimization when a guard fails | fall back to the prose and the judge, and log why |
| Inline cache | the `_js_fn` slot on the object |
| Polymorphic inline cache — one entry per receiver shape | one snippet per host kind, when a buff behaves differently on a room than on a person |
| Recompilation after the assumption changes | regenerate `_js` when the runtime API or naming conventions change — the English is the durable half |
| Profile-guided optimization | compile the *observed* behavior, not the stated intent, when they differ |

Two of those rows are the interesting ones.

**Deopt is what keeps the English authoritative.** A compiled guard is a bet that
the prose meant exactly what the snippet says. When the world produces a case the
snippet mishandles — a novel host kind, a situation the compiler did not
anticipate, a contradiction between snippet and prose — the answer is not to
patch around it at runtime but to *fall back to the prose, note the discrepancy,
and recompile*. The prose is the specification; the snippet is a cache of one
reading of it. This is the same relationship [`EFFECTIVE-VALUES.md`](EFFECTIVE-VALUES.md)
describes between base and effective values, one level up: the compiled form is
derived, invalidatable, and never authoritative.

**Polymorphic dispatch on host kind is the honest way to handle open hosts.**
Now that a buff can live on a character, a room, a material or a relationship
([SKILL.md § Hosts](SKILL.md)), "waterlogged" means something different on each.
One snippet with a chain of host-kind tests is the monomorphic-inline-cache
mistake; one snippet per host kind, selected on application, is a PIC.

## What compiling buys, beyond speed

**A tick budget that is affordable.** LambdaMOO metered every task and killed
runaway ones ([`buffopedia/systems/lambdamoo/`](buffopedia/systems/lambdamoo/SYSTEM.yml)),
and that mattering scales with cost. A prose guard judged by a model every turn,
for every buff, on every host, is the most expensive imaginable per-tick
operation. Compiled, a tick costs a function call, and the budget problem shrinks
to the ordinary one. **Compilation is the answer to the tick-budget question**,
not a separate optimization.

**Determinism, so play is replayable.** The strict tier in
[`SELF-KORZ.md`](SELF-KORZ.md) exists precisely so a session can be replayed from
a seed. A judged guard cannot be; a compiled one can. Compilation is the
mechanism that moves a buff from the soft tier to the strict tier — the
crystallization loop, with an actual crystal at the end.

**Legibility, which is the surprising one.** Black & White's failure was that its
learned model of the player was readable and never shown, so players formed
superstitions ([`buffopedia/systems/black-and-white/`](buffopedia/systems/black-and-white/SYSTEM.yml)).
A compiled buff is *more* legible than a prose one, not less: the snippet states
exactly what will happen, whereas the prose leaves it to a judge whose reasoning
nobody sees. `guard_js: "return !subject.room.hasTag('outdoors')"` can be shown
to a player, argued with, and pointed at when they ask why. The compiled form is
the explanation.

**An escape from Spore's lossy projection.** Spore's disappointment was an
unbounded authoring surface projecting onto about ten ability tracks, so
authoring became decoration ([`buffopedia/systems/spore/`](buffopedia/systems/spore/SYSTEM.yml)).
The projection target here is *arbitrary code in two runtimes*. A
player-authored buff can therefore be noticed by the simulation in proportion to
what it actually says, which is the condition Spore failed to meet. This is the
strongest argument for the compiler being load-bearing rather than an
optimization: **it is what makes player-authored buffs worth authoring.**

## Open questions

1. **When to compile.** On first use, on lint, or on a stability threshold? The
   linter already emits compile requests at build time, which argues for eager
   compilation — but a buff invented mid-scene by a character has no build step.
2. **Who decides a deopt is permanent.** A snippet that keeps falling back is
   wrong, and something has to notice the pattern and ask for a recompile rather
   than deopting forever.
3. **Whether `stacks_with` is compilable at all.** Combination policy may be too
   structural for a snippet; the fixed operator sequence in
   [`EFFECTIVE-VALUES.md`](EFFECTIVE-VALUES.md) might have to own it.
4. **Cross-runtime divergence.** Two snippets from one English source can drift,
   and nothing currently checks that `_js` and `_py` agree. Differential testing
   on a seeded replay would.
5. **Compiling against a learned guard.** If the applier-side predicate is
   *learned* rather than authored — the Black & White case — there is no prose to
   compile from. Possibly the compiled artifact is a distilled decision tree
   rather than a hand-written snippet, which is model distillation wearing a
   compiler's hat.

## See also

- [SKILL.md](SKILL.md) — the buff, and its open host model
- [EFFECTIVE-VALUES.md](EFFECTIVE-VALUES.md) — base vs. effective, the caching spectrum this extends
- [SELF-KORZ.md](SELF-KORZ.md) — the strict/soft two-tier dispatcher and the crystallization loop
- [`../adventure/ADVENTURE-COMPILER.md`](../adventure/ADVENTURE-COMPILER.md) — the compiler this rides on
- [`../../designs/object-system/DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md`](../../designs/object-system/DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md) — English as the durable half, and compilation as literate programming
