---
name: constructionism
description: Educational philosophy — learn by building inspectable things
allowed-tools: []
tier: 0
protocol: CONSTRUCTIONISM
tags: [philosophy, education, papert, microworld]
origin: "Seymour Papert — Logo, Mindstorms"
related: [play-learn-lift, room, yaml-jazz, sister-script, adventure]
---

# Constructionism

> *"If you can build it, you can understand it. If you can inspect it, you can trust it."*

Seymour Papert's educational philosophy: you learn best by **building things** you can **inspect and modify**. Not passive consumption. Not abstract explanation. **Construction.**

## The Tradition

**Logo Microworlds** — Children don't learn geometry from textbooks. They teach a turtle to draw shapes:

```logo
TO SQUARE :SIZE
  REPEAT 4 [FORWARD :SIZE RIGHT 90]
END
```

The child:
1. **Builds** the procedure
2. **Runs** it and sees results
3. **Debugs** when it's wrong
4. **Understands** geometry through construction

## MOOLLM as Microworld

| Logo | MOOLLM |
|------|--------|
| Turtle | Agent/Character |
| Canvas | Room floor |
| Procedures | Skills |
| Variables | YAML state |
| Drawing | File creation |

**Everything is inspectable.** Open `ROOM.yml` — see the state. Read `session-log.md` — see the history. Modify `character.yml` — change the world.

## Core Principles

### Low Floor
Easy to start — no setup, just explore:
```
> LOOK
You are in the workshop.
> EXAMINE hammer
A simple claw hammer.
```

### High Ceiling
Unlimited complexity — build custom skills, complex pipelines, new protocols.

### Wide Walls
Many paths to many goals — adventure games, workflow automation, knowledge organization.

## Learning by Doing

### The Debug Cycle

1. **Try** something — it doesn't work
2. **Inspect** state — see what happened
3. **Hypothesize** — "maybe the path is wrong"
4. **Modify** and retry — test the hypothesis
5. **Understand** — now you know how it works

### Cheating is Learning

From Don's Logo Adventure:

> Type `PRINT :ITEMS` to see where everything is.
> Type `MAKE "RNUM 5` to teleport to the treasure room.
> **If you cheat, you win by learning Logo.**

"Cheating" in MOOLLM:
```
> Open character.yml directly
> Add "magic_sword" to inventory
> You've learned YAML and file structure!
```

The system rewards curiosity with knowledge.

## Micropolis: The Dream

Don's Micropolis for OLPC applied the same philosophy to SimCity:
- Open source simulation
- Scriptable in Python
- Kids can modify the rules
- The city IS the curriculum

MOOLLM applies this to LLM agents:
- Open file state
- Scriptable in any language
- Users can modify the rules
- **The filesystem IS the microworld**

### Embed Micropolis in MOOLLM

```
cities/downtown/
├── ROOM.yml           # Room metadata
├── city.save          # Micropolis save file
├── state.yml          # Extracted game state
├── newspaper/         # Generated stories
├── advisors/          # Expert cards
└── session-log.md
```

LLM reads state, plays the game, summons advisors.

## PLAY-LEARN-LIFT

Constructionism in action:

1. **PLAY** — Explore manually, make messes
2. **LEARN** — Notice patterns, understand
3. **LIFT** — Extract principles, create skills

You don't design skills in the abstract. You **build them** from experience.

## The Insight

> *"If you can build it, you can understand it."*
> *"If you can inspect it, you can trust it."*
> *"The filesystem IS the microworld."*
