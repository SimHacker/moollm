# Buffopedia

**Many games invented the same thing. Here is what each of them calls it, how
each of them stores it, and what survives the trip between them.**

Sibling of [schemapedia](../../schema/schemas/registry.yml). Same idea, different
subject, and one honest difference in kind.

## Why this is not schemapedia

A schema is *load-bearing infrastructure for moving data*. You translate between
JSON Schema and Zod on a Tuesday because a wire needs both ends to agree. That
happens constantly, and interop is the whole point.

A buff is not like that. Nobody wakes up needing to port World of Warcraft's
aura stacking into Dwarf Fortress. Buff systems are **internal dialects** —
each one shaped by its game's economy, tuned against its own numbers, and
meaningless outside them. There is no daily interop pressure and no standard
anybody wants.

But two things make a buffopedia earn its place anyway:

1. **Buffs are character data, and characters travel.**
   [Soul City's Exchange](../../../examples/soul-city/exchange/README.md) already
   uplifts Sims out of `.iff`/`.FAM` binaries into MOOLLM characters and writes
   them back, and the
   [Visitor Protocol](../../../examples/soul-city/bridge/visitor-protocol.yml)
   already says what persists when a character crosses worlds: identity, needs,
   relationships, `mind_mirror`. It says **nothing about buffs** — and a Sim who
   walks into Adventure 4 mid-hangover should still have the hangover. Buffs are
   part of a character's current state, so if characters are portable, buffs need
   a stated fidelity policy. [interchange.yml](interchange.yml) is that policy.

2. **Convergent design is the lesson.** Eighteen systems independently derived
   the same mechanism and disagreed productively about four questions: what the
   guard is, how conflicts resolve, when the binding dies, and who owns the
   ordering. Reading them side by side is how you find out which of MOOLLM's
   choices are principled and which are just the first thing that worked.

So: a comparative dialect atlas with a working import/export path, not a
standards effort.

## The mechanism, stated once

From [GAME-PIECES.md](../../../designs/GAME-PIECES.md): a buff is **a mixin with
an expiration date or condition on its delegation edge**, carrying its own CARD,
whose advertisements merge into the host's pool while it is live and enabled.
Every system in here is a variation on four axes:

| Axis | The question | Range across systems |
|---|---|---|
| **Guard** | when does this apply? | timer · event · predicate · tag match on source *and* target · proximity · material · prerequisite |
| **Conflict** | two bindings, one slot? | ordered layers · fixed operator sequence · exclusive category with max-wins · rebind · additive stack · score-and-sample |
| **Lifetime** | how long does the binding live? | instant · N ticks · until event · while predicate · until rebound · permanent |
| **Ownership** | who decides the order? | engine-fixed · designer-declared channels · content data · legislated rulebook · emergent from scoring |

[TECH-TREE.md](../../../designs/TECH-TREE.md) is the same mechanism with a
progress guard and no expiry, which is why unlocks, spells, abilities, modifiers
and buffs are one node type and not five subsystems.

## Reading order

1. [registry.yml](registry.yml) — the index: families, systems, status, confidence
2. [interchange.yml](interchange.yml) — the fidelity ladder and the wire format
3. `systems/<id>/SYSTEM.yml` — one dialect at a time
4. [plugin-convention.yml](plugin-convention.yml) — how to add one

## The fidelity ladder, in one paragraph

Porting a buff is not one operation, it is four, and they fail at different
rates. **Narrative** (name, source, description, polarity, tags) ports perfectly
and is the only tier every target can consume. **Temporal** (duration, expiry
condition) ports if you can map clocks. **Numeric** (stat modifiers) ports only
where stat namespaces align, and needs a declared mapping plus a magnitude
rescale — a `+5 damage` from a game where damage runs 1–20 is not a `+5` in a
game where it runs 1–2000. **Behavioral** (guards, hooks, scripts, dispatch
effects) does not port at all, mechanically.

The new thing is that behavioral tier's failure mode changed. Historically it
was dropped. In an LLM-orchestrated world it degrades to **prose intent** — the
buff's own description of what it is trying to do — and the destination
re-implements it in its own idiom. That is the whole reason this pedia is worth
building now and would not have been in 2005. See
[interchange.yml](interchange.yml) for the tier table and the degradation rules.

## Naming

*Buffopedia*, with the classical `-o-` connective, matching encyclopedia.
"Buffpedia" stutters, "bufferpedia" implies I/O buffers, "buffipedia" implies a
Latin stem that does not exist. The word "buff" here is the gamer term (a
temporary beneficial modifier), from bodybuilding slang by way of MMOs, and
"debuff" is its antonym — MOOLLM treats them as one thing, per the house line:
*all effects are buffs, some are just shitty.*

## See also

- [../SKILL.md](../SKILL.md) — the runtime skill: APPLY, TICK, CLEANSE, tags, categories
- [../EFFECTIVE-VALUES.md](../EFFECTIVE-VALUES.md) — base value is truth, effective value is reality
- [../buffs/INDEX.yml](../buffs/INDEX.yml) — the buff *library* (instances: hangover, munchies, terpene blessings)
- [designs/GAME-PIECES.md](../../../designs/GAME-PIECES.md) — the canonical model
- [designs/MOODY.md](../../../designs/MOODY.md) — buffs gate the constraint wires
- [designs/TECH-TREE.md](../../../designs/TECH-TREE.md) — unlock as the same mechanism
- [skills/schema/](../../schema/) — the sibling pedia, and the deeper mapping machinery
