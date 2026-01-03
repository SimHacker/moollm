# Constructionism

> *"If you can build it, you can understand it. If you can inspect it, you can trust it."*

---

## What Is It?

**Constructionism** is Seymour Papert's educational philosophy: you learn best by **building things** you can **inspect and modify**.

Not passive consumption. Not abstract explanation. **Construction.**

---

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

---

## MOOLLM as Microworld

The filesystem IS a microworld:

| Logo | MOOLLM |
|------|--------|
| Turtle | Agent/Character |
| Canvas | Room floor |
| Procedures | Skills |
| Variables | YAML state |
| Drawing | File creation |

**Everything is inspectable.** Open `ROOM.yml` — see the state. Read `session-log.md` — see the history. Modify `character.yml` — change the world.

---

## Core Principles

### 1. Low Floor

Easy to start:
```
> LOOK
You are in the workshop.
Objects: hammer, nails, wood
> EXAMINE hammer
A simple claw hammer.
```

No setup. No configuration. Just explore.

### 2. High Ceiling

Unlimited complexity:
```yaml
# Build a custom skill
skills/my-analysis/
  README.md
  PROTOTYPE.yml
  template/
    ANALYSIS.yml.tmpl
```

Same system scales from simple exploration to sophisticated automation.

### 3. Wide Walls

Many paths to many goals:
- Build adventure games
- Automate workflows
- Create characters
- Design data pipelines
- Organize knowledge

The tools don't constrain the application.

---

## Learning by Doing

### The Debug Cycle

1. **Try something** — it doesn't work
2. **Inspect state** — see what happened
3. **Form hypothesis** — "maybe the path is wrong"
4. **Modify and retry** — test the hypothesis
5. **Understand** — now you know how it works

This is how programmers learn. This is how MOOLLM teaches.

### Cheating is Learning

From Don's [Logo Adventure](https://medium.com/@donhopkins/logo-adventure-for-c64-terrapin-logo-81c679e715f6):

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

---

## Micropolis: The Dream

Don's [Micropolis](https://medium.com/@donhopkins/micropolis-constructionist-educational-open-source-simcity-58566f20f063) for OLPC:

Alan Kay criticized SimCity: "You can't see inside of it."

Micropolis fixes that:
- Open source simulation
- Scriptable in Python
- Kids can modify the rules
- The city IS the curriculum

MOOLLM applies the same philosophy to LLM agents:
- Open file state
- Scriptable in any language
- Users can modify the rules
- The filesystem IS the microworld

### Embed Micropolis in MOOLLM

The dream realized — a city simulation as a MOOLLM room:

```
cities/downtown/
├── ROOM.yml           # Room metadata, links to simulator
├── city.save          # Micropolis save file
├── state.yml          # Extracted game state: population, budget, zones
├── views/             # Rendered map images, charts, overlays
├── newspaper/         # Generated stories about city events
├── advisors/          # Characters: traffic-expert.card, economist.card
└── session-log.md     # Who did what, human and LLM alike
```

**How it works:**

1. **Sister script** runs Micropolis headless: advance N ticks, inject edits, render views
2. **state.yml** is extracted game state — population, budget, zones, disasters
3. **LLM reads state.yml**, examines views, and *plays the game*
4. **Multiple users** can play together, mediated by LLM
5. **Advisor characters** analyze the city: traffic expert, economist, environmentalist
6. **Virtual newspaper** writes stories about citizens, traffic jams, monster attacks

```
> SUMMON traffic-expert
Traffic Expert materializes, clipboard in hand.
"The highway through downtown is gridlocked. 
 Consider adding a rail line or reducing industrial zoning."

> BUILD rail-line FROM downtown TO industrial-district
Adding rail line...
[sister script injects edit]
[simulator advances 100 ticks]
[state.yml updated]

Traffic Expert: "Congestion reduced 23%. Good call!"
```

**This is constructionism:**
- The city is inspectable (state.yml, views/)
- Kids can modify the rules (edit zone costs, disaster frequency)
- Characters teach through dialogue (advisors explain trade-offs)
- The simulation IS the curriculum

---

## Building Skills

**PLAY-LEARN-LIFT** is constructionism in action:

1. **PLAY** — Explore manually, try things, make messes
2. **LEARN** — Notice patterns, understand what works
3. **LIFT** — Extract principles, create reusable skills

You don't design skills in the abstract. You **build them** from experience.

See: [play-learn-lift/](../play-learn-lift/)

---

## Example: Learning Rooms

A new user:

```
Day 1: "How do I navigate?"
> LOOK
> GO north
> EXAMINE object
[Learns basic commands by doing]

Day 2: "What's in these YAML files?"
> cat ROOM.yml
[Sees the data structure, starts to understand]

Day 3: "Can I add my own object?"
> echo "magic_lamp: {}" >> objects.yml
[Modifies the world, sees the result]

Day 4: "I want to automate this..."
[Writes a skill, becomes a builder]
```

**The system teaches itself** through inspectability.

---

## Dovetails With

- [Play-Learn-Lift](../play-learn-lift/) — The methodology of constructionist learning
- [Room](../room/) — The microworld to explore
- [YAML Jazz](../yaml-jazz/) — Inspectable, modifiable state
- [Sister Script](../sister-script/) — Building automation from exploration
- [Adventure](../adventure/) — Learning through narrative

---

## Protocol Symbol

```
CONSTRUCTIONISM
```

Invoke when: Designing for learning, building inspectable systems, teaching through construction.

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#CONSTRUCTIONISM)
