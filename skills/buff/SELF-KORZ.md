# Self, Korz, Korz′ — three readings of a buff

> *"A buff is a mixin with an expiration date or condition on its delegation
> edge."* — [GAME-PIECES.md](../../designs/GAME-PIECES.md)

That sentence is a **Self** reading. It is correct and it is not the most
general one available. Two more readings sit above it, each removing a
restriction the previous one did not know it had.

## 1. The Self reading — where the design already is

A buff is a prototype in the host's `inherits:` list, with a condition on the
edge. Attaching is adding a delegation parent; detaching is removing it. The
host's behavior is the **union of the cards of every live, enabled mixin**,
scored together in one auction, derived at lookup and never stored.

What Self buys: no classes, so no buff needs a declared type; runtime edge
mutation, so buffs arrive and leave without recompiling anything; delegation
rather than copying, so the buff stays one object no matter how many hosts
carry it.

What it still costs — the restriction Self cannot see: **a buff must be
attached to a host object.** The object boundary is intact, so every buff needs
an owner. That single assumption produces every awkward corner in this skill:

- `skills/buff/` says **CHARACTERS ONLY**, and routes room effects through
  invented "room spirit" characters, because a room is not the kind of thing a
  buff was allowed to own.
- A modifier that belongs to a *material* — everything made of silver burns
  werewolves — has nowhere to live, so it gets copied onto every instance.
- Weather, faction standing, time of day, and the ruleset itself all want to
  modify behavior and none of them are characters.

The room-spirit character is a workaround for a limitation of the model, not a
design. Korz removes the limitation.

## 2. The Korz reading — the host is just another dimension

Korz (Ungar, Ossher, Kimelman) deletes the object boundary. What remains is a
**sea of slots**, each carrying coordinates on named dimensions, with **guards**
deciding applicability and **symmetric dispatch** — no privileged receiver, no
"self" that owns the method.

Re-read a buff in that vocabulary and it stops being a thing attached to
something:

**A buff is a set of slots whose coordinates include the host as one dimension
among several.**

Everything awkward becomes ordinary:

| Buff concept | Korz reading |
|---|---|
| `while: carrying(holy-symbol)` | a guard on the binding |
| attached to a character | a coordinate on the `who` dimension |
| an **aura** (proximity-scoped) | a coordinate on the `where` dimension — no room spirit needed |
| a DF **syndrome** on a material | a coordinate on the `material` dimension, so anything made of it dispatches the same way, with zero per-instance application |
| a **weather** or **mood** effect | a coordinate on an ambient dimension the room sets and everything inside inherits |
| a buff on the **ruleset** (Fluxx, Revolutionary Chess) | a coordinate on a rules dimension — the rules are not special |

The sharpest case is one GAME-PIECES already describes without naming it: a
POISONED debuff advertises "seek antidote" **to its host** and "administer
antidote" **to bystanders**. In Self that needs two objects and a message
between them. In Korz it is one slot answering differently depending on who is
asking — **symmetric dispatch**, which is exactly what
[Unreal's GAS](buffopedia/systems/unreal-gas/SYSTEM.yml) ships as
`source_tags` and `target_tags` on every single modifier: a guard on both ends,
in a commercial engine, running Fortnite.

So Korz's payoff for this skill is not elegance. It is the deletion of four
special cases and one fake object type.

## 3. The axis Korz does not have — lifetime

Here the buff literature has something to give back.

A Korz context binding lives for the **dynamic extent of a send** — stack
discipline, implicitly carried down the call chain, gone when the call returns.
A buff is the opposite: **a context binding that outlives the call that created
it.** Heap-allocated context, garbage-collected by timer.

That is the whole content of `expires_at`, `expires_when`, and `while`: they
are **lifetime policies on a coordinate binding**, a vocabulary Korz has no
need for and games cannot live without. Laid out as a ladder:

| Lifetime | Binding dies when | Seen in |
|---|---|---|
| instant | immediately, after applying once | GAS Instant; `cleanse`, `antidote` |
| dynamic extent | the send returns | **Korz** |
| N ticks | the timer runs out | most buffs; Sims moodlets |
| until event | something happens | `expires_when: sunrise` |
| **while a phase is active** | **the owning phase ends — or the whole scene aborts** | **SimProv's Hope Chest**; see below |
| while predicate | the guard goes false, re-checked at lookup | `while: carrying(holy-symbol)` |
| until rebound | someone binds that dimension again | **Fluxx** New Rule cards; WoW exclusive categories |
| permanent | never | tech-tree unlocks; NetHack intrinsics |

⚠ The claim that Korz bindings are strictly dynamic-extent is a reading of the
design, not a quotation. It is [question 9 for David
Ungar](../../../WillWrightShowForFood/characters/david-ungar/korz/ask-david.md)
— *what is the lifetime of a coordinate binding, and does Korz want an `until`?*

### Phase extent — dynamic extent, with a scene instead of a stack

The new row is the interesting one, because it is **dynamic extent scaled up**:
the binding lives for the extent of a *phase of a staged event* rather than of a
call, and something in the world owns that phase and is responsible for unwinding
it.

SimProv's wedding is the worked example, and it is not hypothetical — the state
machine is written down in
[`catalogs/simprov/ORCHESTRATOR.yml`](../../../WillWrightShowForFood/catalogs/simprov/ORCHESTRATOR.yml).
The **Hope Chest** owns eight states (`single → flirting → in_love → engaged →
planning → rehearsal → ceremony → reception`), and each transition declares what
it `unlocks:`, `spawns:`, and `requires:`. Buddha's need-suppression and the
Crowd Sitter's seating are scoped to phases of that machine, not to turn counts.

Three things follow, and each is something the timer-based rows cannot express:

- **The scope has an owner.** `while: phase == ceremony` is meaningless without
  something that knows the phase. The orchestrator object is that something —
  placeable, inspectable, and holding the state where a player can find it.
- **Abort is the hard case, and the owner is the only thing that can handle it.**
  A wedding that collapses halfway must remove Buddha's suppression, release the
  seated crowd, and dismiss spawned NPCs. That is `try/finally` as an object:
  **the orchestrator is the unwind handler**, and phase-scoped buffs are what it
  unwinds. Nothing keyed to a turn count can clean up after a cancelled scene.
- **Unwind ownership migrates.** The orchestrator owns cleanup only for the phases
  it owns. When a staged event emits a durable artifact, that artifact takes over
  its own later lifecycle — and the orchestrator becomes deletable. A marriage
  certificate handles its own divorce and its own widowhood long after the Hope
  Chest is gone. So cleanup follows the **lifecycle stage**, not whoever created
  the state.
- **The phase gates the ads, not just the stats.** Transitions carry `unlocks:`,
  so a phase change rewrites what is *available* — the tech-tree row of this same
  table, driven by a scene rather than by accumulated progress.

Full write-up, including the pie-menu targeting and the applicators the chest
conducts: [`buffopedia/systems/simprov/`](buffopedia/systems/simprov/SYSTEM.yml).

Note also that the **tech tree** is this table's last row with a different
guard: a permanent binding gated on progress instead of time. See
[TECH-TREE.md](../../designs/TECH-TREE.md). One mechanism, two ends of the
lifetime axis.

## 4. The Korz′ reading — guards the LLM judges

Korz′ is Korz where an LLM may improvise coordinates and evaluate guards that
have no boolean implementation. This skill already has the feature and did not
know what to call it:

```yaml
# skills/buff/ semantic buffs — these are Korz′ coordinates
effect: "cats seem to like you today"
effect: "radiating calm energy"
```

There is no numeric axis for "cats seem to like you today." It is a coordinate
in a dimension invented at authoring time and evaluated by judgment. A guard
like *while the room feels tense* is likewise real and unimplementable, and an
LLM handles it natively.

That gives a **two-tier dispatcher**:

- **strict tier** — numeric modifiers, tag matches, timers, checkable guards.
  Deterministic, crystallizable, replayable from a seed.
- **soft tier** — prose guards and semantic effects, judged. Non-deterministic
  by design, logged with provenance so a replay can be audited.

And a crystallization loop, which is [play-learn-lift](../play-learn-lift/) one
level down: soft guards that fire consistently get compiled into strict ones.
The Zendo move — induce the rule from labelled examples — is the same as
Oliver Steele's instance-first development: write the buffs, then discover the
guard schema.

**Crystallization is literal compilation, and it has a machine.** The English
guard becomes a `guard_js` / `guard_py` snippet that the deterministic adventure
engine runs directly, emitted by the same linter pipeline that already compiles
exit guards and dynamic descriptions. That makes the two tiers here the two tiers
of a JIT: the judge is the interpreter, the snippet is compiled code, and a
snippet that meets a case it mishandles **deopts back to the prose**, which stays
authoritative. Full design, including which fields compile and what the tick
budget looks like afterwards: [BUFF-IN-TIME-COMPILER.md](BUFF-IN-TIME-COMPILER.md).

This is also where the buffopedia's portability story comes from. The
behavioral tier of a foreign buff does not port mechanically, but it ports as
**prose intent**, and the destination re-implements it in its own idiom. See
[buffopedia/interchange.yml](buffopedia/interchange.yml).

### The other guard axis — *when* it is checked

Strict and soft is a question about *how* a guard is evaluated. There is a second
axis, which the buff model currently collapses: **when**.

| Checked at | Failure means | Example |
|---|---|---|
| **placement / authoring** | the thing cannot exist there — refused before any state is created | an eloporter that requires one end indoors and one outdoors |
| **application** | the buff does not land | GAS source and target tag requirements |
| **lookup / tick** | the buff stops contributing, and may resume | `while: carrying(holy-symbol)` |

Nearly every system surveyed has the last two and only build tools have the first.
It is the cheapest and kindest of the three: failure happens **before anything
exists to clean up**, and it can be reported in the editor rather than discovered
in play. A precondition that can be checked at placement should be, and the Sims'
build mode — where an object simply refuses to go somewhere illegal — is the model.

Worked example, and where it comes from:
[`life-events-playset.md`](../../../WillWrightShowForFood/designs/orchestrator-playsets/life-events-playset.md).

## 5. One question all three readings must answer: conflict

Two bindings want the same dimension. Every system picks one of three answers,
and MOOLLM should support all three and declare which applies per dimension:

- **Order** — layer them in a defined sequence. Magic's CR 613, the CSS
  cascade, GAS's fixed operator equation. Ambiguity is resolved by legislation.
- **Rebind** — one binding per dimension, the new one displaces the old. Fluxx
  makes conflict physically unrepresentable; WoW's exclusive categories keep
  both icons and apply only the strongest.
- **Score and sample** — do not resolve it, let both bid, then pick among the
  top N. The Sims shipped this, and it is the layer-3 rung of the GAME-PIECES
  ladder.

Korz errors on an ambiguous tie, which is the correct choice for a language and
an impossible one for a game — Magic has judges and cannot stop play. See
[mtg-layers](buffopedia/systems/mtg/SYSTEM.yml) for what legislating a total
order actually costs.

## What this implies for the skill

Concrete gaps, each traceable to the Self-level restriction above:

1. **Guards on both ends.** Add source/target requirements to modifiers, not
   just tags on the buff. (GAS, feature-flag targeting.)
2. **Scope instead of room spirits.** `scope: target | prototype | region`
   replaces the CHARACTERS-ONLY rule and the invented spirit characters.
3. **A fixed operator sequence** instead of hand-picked `priority: 100/200`
   integers, so authors never choose a number. (GAS, CSS, MTG all converged.)
4. **A stacking policy per buff** — add / refresh / max / replace / ignore, and
   aggregate-by-source vs by-target. Reapplication has five sane meanings.
5. **Lifetime as declared vocabulary**, using the ladder in §3.
6. **Provenance on category assignment**, because exclusivity is contested data
   (see the WoW entry's patch archaeology).

## See also

- [GAME-PIECES.md](../../designs/GAME-PIECES.md) — the Self-level canonical model
- [MOODY.md](../../designs/MOODY.md) — heat drives parameters, buffs gate the wires
- [TECH-TREE.md](../../designs/TECH-TREE.md) — the permanent, progress-gated end of the lifetime axis
- [buffopedia/](buffopedia/) — eighteen dialects, four axes, one fidelity ladder
- [EFFECTIVE-VALUES.md](EFFECTIVE-VALUES.md) — base is truth, effective is reality
- [designs/SELF-ISH-INFLUENCES.md](../../designs/SELF-ISH-INFLUENCES.md) — the Self lineage in MOOLLM
- [designs/KORZ-LLM-EVALS.md](../../designs/KORZ-LLM-EVALS.md) — Korz′ evaluation work
- WWSFF: [korz/examples/](../../../WillWrightShowForFood/characters/david-ungar/korz/examples/)
  — sims-advertisements, mtg-layers, fluxx-nomic, df-procedural-magic
