---
name: advertisement
description: Objects announce what they can do — The Sims style
allowed-tools:
  - read_file
  - write_file
  - list_dir
tier: 1
protocol: ADVERTISEMENT
related: [card, object, society-of-mind, room, action-queue, coherence-engine, needs, task]
tags: [moollm, game, interaction, sims, behavior, autonomy]
---

# Advertisement

> *"Objects don't wait to be used — they announce what they can do."*

## What Is It?

**Advertisement** is The Sims-style object interaction: every object in a room broadcasts its available actions, scored by relevance to the current context.

Instead of the user memorizing commands, objects **advertise** what's possible:

```
You approach the workbench.

Available actions (sorted by relevance):
  ⭐ CRAFT tool (you have materials)
  • EXAMINE blueprints
  • ORGANIZE parts
  • MORE options...
```

## The Sims Connection

In **The Sims**, objects have "advertisements" — each interaction scores based on:
- The Sim's current needs (hunger, fun, social)
- Object properties (a fridge scores high for hunger)
- Context (can't use stove if broken)

This extensible object architecture was **key to The Sims' massive success**:
- **User-created objects** — anyone could make new furniture, appliances, characters
- **Expansion packs** — just drop in new objects with their advertisements
- **No code changes** — objects self-describe their behaviors
- **Infinite variety** — the community created millions of objects

The same YAML file that defines what an object *is* also defines what it *can do*. Plug-in architecture for free.

MOOLLM applies this to **any object**:

```yaml
# workbench.yml
advertisements:
  CRAFT:
    score: 80
    score_if: "the actor has materials and the crafting skill"
    satisfies: [productivity, creativity]
  EXAMINE:
    satisfies: [curiosity]
```

`EXAMINE` says nothing about its score or when it applies, so it bids the default 50, always.

## One Concept

Everything that says "choose me, here, for this" is an advertisement. The populations differ in which keys they use, not in what they are:

| Population | Where | Typical keys |
|---|---|---|
| World offers | objects, rooms, characters | score, guard, effect, cost, say, give |
| Word and concept triggers | props, characters | trigger, say, guard |
| Skill relevance | every skill CARD | score, score_if (prose, judged by the model) |
| Provides and wants | service skills (leela-ai, manufacturing-intelligence) | parameters, satisfies, effect |
| AMBIENT | skills that stay in context | score, score_if, scope, resolution |

A canned response is the degenerate case, not the model. A trigger advertisement can carry a guard, a score_if and parameters like any other, which is what keeps it from being a canned reply.

## Protocol

The canonical schema is [ADVERTISEMENT.yml](ADVERTISEMENT.yml), in the format of [SCHEMA.md](../../designs/object-system/SCHEMA.md#schema-files). Its top-level slots (`score: 50`, `reach: room`, `invoked_by: [player, npc]`) are what every advertisement inherits; its `schema:` key describes every key with shape, default and meaning, plus worked examples.

### Defaults: state only what is unusual

Every key has a default, and an omitted key means its default. No `score_if:` means always. No `guard:` means always available. No `reach:` means the advertiser's room. No `method:` means the method with the advertisement's name, if there is one. A linter treats a value equal to its default as removable.

Two conventions hold for every key unless the key says otherwise:

- a bare string where a list is expected is a list of one;
- a list means any of its members, `{ all: [...] }` every member, `{ not: [...] }` none.

### Shape

`advertisements:` is a map keyed by name. UPPERCASE names are commands a player types; lowercase names are callable from code. Each entry is a map of the keys below.

```yaml
advertisements:
  RING-GONG:
    description: "Ring the brass gong to announce good news"
    when_flags: [good_news, victory, milestone]
    say: "BWONGGG. {actor} has news."
    satisfies: { social: 20 }
```

### Base keys

| Key | Shape | Default | Meaning |
|---|---|---|---|
| `description` | prose | none; the name is the label | what it offers; the LLM performs it from this when there is no effect or method |
| `score` | 0..100 | 50 | the bid when `score_if` holds or is absent |
| `score_if` | prose, compiles | always | the situation in which it wants to be chosen |
| `guard` | prose, compiles | always available | what must be true for it to be offered at all |
| `guard_fail` | string | the engine's generic refusal | what the actor hears when the guard refuses |
| `parameters` | map name → prose | none | what it needs from the actor or context |
| `effect` | prose, compiles | none | what happens, beyond the graduated effect keys |
| `method` | method name | the method with its name | what performs it, called with its parameters |
| `satisfies` | list or map | none | motives on the actor; a bare list means 10 each |
| `invoked_by` | list of player, npc, self, any | `[player, npc]` | who may choose it |
| `reach` | self … user | `room` | how close an actor must be to see it |

`guard` and `score_if` are different questions. The guard asks *can you?* and hides the advertisement when false. `score_if` asks *would you want to?*: when it holds the bid is `score`; when it doesn't the bid is 0 and the advertisement stays available, so a player can still pick it from the menu and autonomy won't. A compiled `score_if_js` may return a number instead of a bool; the number replaces the score, which is how a bid scales with a need.

In a skill CARD the "room" is the context the card is loaded in, the player is the user, and the npc is the model choosing a skill. Most skill advertisements name no method: the effect is "load this skill and act".

### Compile, then graduate

Every prose key aims to be compilable. The adventure compiler has an LLM write `<key>_js` and `<key>_py` siblings (`guard` → `guard_js`, `score_if` → `score_if_js`, `effect` → `effect_js`) that the engine runs; empty siblings fall back to the prose.

When enough compiled expressions repeat one shape, the shape graduates into a standard key with simple parameters, which the engine runs with no generated code:

```
prose            guard: "the player has a feather token"
prose + _js      guard_js: "(world) => world.has('feather_token')"
graduated key    requires_items: [feather_token]
```

Rungs coexist: an advertisement may have `requires_tags:` and a prose `guard:` for what the tags don't capture, and only the prose needs a `_js`.

**Graduated conditions**

| Key | Default | Meaning |
|---|---|---|
| `requires_tags` | anyone | the actor carries any of these tags |
| `requires_items` | none | the actor holds all of these; not consumed unless `{ all: [...], consume: true }` |
| `when_state` | none | state pairs on the advertiser, all match |
| `when_flags` | none | world flags, any set |
| `requires_lighting` | any light | `{ min, max }`, 0..10 inclusive, in the actor's room |
| `cost` | free | coins from the actor to the advertiser's owner when chosen; also a guard |
| `trigger` | none | words or phrases, any, whole-word, case-insensitive; `{ phrases, concepts }` for concepts the LLM judges |

**Graduated effects**

| Key | Meaning |
|---|---|
| `say` | spoken by the advertiser to its room; `{name}` fills from parameters and context |
| `set` | state pairs written on the advertiser |
| `move_to` | moves the actor; a path relative to the advertiser's room |
| `give` / `take` | one of each item, advertiser → actor / actor → advertiser |
| `pay` | coins from the advertiser to the actor |
| `buff` | buffs applied to the actor |
| `spawn` | objects created in the advertiser's room |

All effect keys default to none. Their names are the vocabulary of a deterministic DSL: `requires_tags`, `when_state`, `reach` and `cost` are its adjectives and prepositions; `say`, `set`, `move_to`, `give`, `take`, `spawn` its verbs; items, tags, flags and rooms its nouns. Plugged-in objects extend it: a coin dispenser that implements `cost:` makes `cost:` runnable in any room that holds one.

### Older spellings

Readers accept these; writers emit the canonical key.

| Old | Canonical |
|---|---|
| list entries with `action:` or `name:` | map keyed by that name |
| `condition:` | `guard:` in world objects, `score_if:` in CARDs |
| `preconditions:` | `guard:` |
| `score-if:` | `score_if:` |
| `score_hint:` | `score:` |
| `requires:` tag list | `requires_tags:` (prose `requires:` is a `guard:`) |
| `response:`, `result:` on trigger entries | `say:` |
| `delegate: { method, params }` | `method:` + `parameters:` |
| `motives_satisfied:` | `satisfies:` |
| trigger scores 0..1 | × 100 |

### Extensions

Object-specific keys are YAML Jazz until they graduate; never reuse a standard key with another meaning. AMBIENT advertisements add `scope:` and `resolution:` (see [CARD.yml](CARD.yml)). WillWrightShowForFood's `schemas/advertisement-dispatch.yml` extends this schema with dispatch modes (forward, inject, hub, magazine, spawn), locked advertisements that teach by refusing, and reciprocal services; its `score_when` is `score_if`.

## Autonomous Selection

For **autonomous agents**, advertisements enable self-direction:

```
Agent evaluates all objects in room:
  workbench: CRAFT (85), EXAMINE (50)
  bookshelf: READ (70), ORGANIZE (30)
  door: EXIT (40)

Agent selects among the top N: CRAFT at workbench (score 85)
```

No hardcoded behavior. Objects define possibilities. Agent selects based on goals. The Sims picked randomly among the top N rather than always taking the highest bid; why that is a feature, and how temperature generalizes it, is in [ADVERTISEMENT-AUCTION.md](../../designs/ADVERTISEMENT-AUCTION.md).

Top actions surface in the [PIE-MENU](../room/): center = highest score = default action.

```
    [CRAFT]
       ⭐
[ORGANIZE] • [EXAMINE]
       •
    [MORE]
```

## Example: Smart Room

```yaml
# research-lab/ROOM.yml
objects:
  microscope:
    advertisements:
      ANALYZE-SAMPLE:
        score: 90
        requires_items: [sample]
      CALIBRATE:
        score: 60
        score_if: "accuracy is below 0.9"
  notebook:
    advertisements:
      WRITE-NOTES:
        score: 75
        score_if: "there are unrecorded observations"
      REVIEW:
        score: 40
  coffee-maker:
    advertisements:
      BREW:
        score: 65
        score_if: "the actor is tired"
        cost: 1
        give: [coffee]
        satisfies: { energy: 30 }
      CLEAN:
        score: 30
        score_if: "used more than five times since the last clean"
        set: { uses: 0 }
```

Agent enters with a sample, a bit tired, sees:

```
Top actions:
  1. ANALYZE-SAMPLE at microscope (90) — you have a sample
  2. WRITE-NOTES at notebook (75) — observations pending
  3. BREW at coffee-maker (65) — you're a bit tired
```

## SimAntics Heritage

This is **SimAntics** — The Sims' behavioral engine:

| SimAntics | MOOLLM |
|-----------|--------|
| Object advertisement | `advertisements:` map in YAML |
| Motive scores | `score`, `score_if`, `satisfies` against needs |
| Autonomous selection | Agent picks among the top-scored actions |
| Pie menu | [PIE-MENU](../room/) for user interaction |

Don Hopkins worked on SimAntics. This is that tradition, for LLM agents.

## HyperCard-Style Event Bubbling

When you click an advertised action, it triggers a **symbolic event** that bubbles up:

```
Click CRAFT on workbench

Event path:
  1. workbench (object)     → handles CRAFT? no, pass up
  2. workshop/ (room)       → handles CRAFT? no, pass up
  3. building/ (parent)     → handles CRAFT? no, pass up
  4. world/ (root)          → handles CRAFT? no, check inheritance
  5. workbench-prototype    → handles CRAFT? YES → execute
```

Just like HyperCard: events bubble from button → card → background → stack.

### Containment Tree (Spatial)

Events bubble **up** the room hierarchy:

```
object in room in parent-room in world
   ↑         ↑              ↑        ↑
              event bubbles up
```

### Inheritance Graph (Prototype)

If no handler in containment tree, check the **prototype chain**:

```
workbench
   ↓ inherits from
furniture-prototype
   ↓ inherits from
object-prototype     → has default CRAFT handler!
```

### Combined Path

```yaml
# Event resolution order:
1. The object itself
2. Parent room
3. Grandparent room
4. ... up to world root
5. Object's prototype
6. Prototype's prototype
7. ... up to root prototype
```

First handler that responds wins. Unhandled events can:
- Log a warning
- Trigger POSTEL (charitable interpretation)
- Invoke a default handler

### Example: Custom Behavior

```yaml
# workshop/ROOM.yml
handles:
  CRAFT: |
    # Room-level craft handler
    Check if character has required skill.
    Check if materials available in room.
    If conditions met, delegate to object.
    Otherwise, suggest where to get materials.
```

The room intercepts CRAFT before it reaches the object, adding room-specific logic.

## Dovetails With

- [Room](../room/) — Where objects live and advertise
- [Object](../object/) — `OBJECT.yml` gives every object an empty `advertisements:` map
- [PIE-MENU](../room/) — How advertisements surface to users
- [SNAP-CURSOR](../room/) — Context-aware object interaction
- [Coherence Engine](../coherence-engine/) — Evaluates and selects actions
- [Trading Card](../card/) — Cards can advertise too
- [Needs](../needs/) — What `satisfies` feeds
- [Buff](../buff/) — What `buff` applies
- [Rubric](../rubric/) — **Scoring criteria** for advertisement evaluation
- [Scoring](../scoring/) — How scores are calculated and valued

## Protocol Symbols

```
ADVERTISEMENT        — Objects announce available actions
AUTONOMOUS-SELECTION — Agent picks based on scores
SIMANTICS            — The Sims behavioral model
PIE-MENU             — Radial display of options
FLY-UNDER-RADAR      — Normalize through defaults
PROCEDURAL-RHETORIC  — Rules carry ideology
```

See: [PROTOCOLS.yml](../../PROTOCOLS.yml)

## The Deep Insight

From [SIMANTICS](../../PROTOCOLS.yml):

> *"The Sims' AI isn't centralized — it's distributed throughout objects."*
> *"A refrigerator knows it offers food. A bed knows it offers sleep."*
> *"The Sim chooses from what's advertised nearby."*

This IS MOOLLM's architecture. Objects self-describe. The coherence engine orchestrates. Intelligence is **distributed** throughout the world.

The advertisements ARE the AI.

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/advertisement/](https://github.com/SimHacker/moollm/tree/main/skills/advertisement)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
- **Related skills:** [object](../object/), [room](../room/), [card](../card/), [needs](../needs/), [action-queue](../action-queue/), [coherence-engine](../coherence-engine/)
