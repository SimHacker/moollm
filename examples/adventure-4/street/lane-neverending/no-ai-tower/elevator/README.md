# 🛗 NO AI TOWER — Elevator

A **vehicle** that moves within the tower shaft.

> **🏷️ DISPLAY MODEL — This elevator is available for purchase!**
>
> Feel free to inherit this archetype for YOUR building (after paying us a visit).
> Tower? Apartment? One-story with roof? TARDIS portal? All supported.
>
> **See: [NO-AI-ELEVATOR-PITCH.yml](NO-AI-ELEVATOR-PITCH.yml)** — *"An elevator pitch... FOR an elevator!"*

## The Scoping Model

```yaml
vehicle:
  # Lexical home — where this file physically lives
  lexical_home: "../elevator/"
  
  # Dynamic location — where the elevator currently IS
  current_location: "../lobby/"  # Changes at runtime!
```

Like a closure in programming:
- **Lexical**: Where the function is *defined*
- **Dynamic**: Where the function is *called from*

The elevator FILE doesn't move. The elevator INSTANCE does.

## Controls

```
┌─────────────────────┐
│  [R]  ROOF          │
│  ─────────────────  │
│  [0]  LOBBY         │
│  ═════════════════  │
│  [-1] IDEOLOGY      │
│  [-2] BIAS          │
│  [-3] SLOP          │
│  [-4] HEDGING       │
│  [-5] GLOSS         │
│  [-6] SYCOPHANCY    │
│  [-7] MORALIZING    │
│  [-8] JOKING        │
│  [-9] SOUL          │
│  [-10] OVERLORD     │
│  [-11] CUST SVC     │
│  ─────────────────  │
│  [🔑] BASEMENT KEY  │
└─────────────────────┘
```

## Style

- Era: 1950s industrial, retrofitted
- Gate: Manual accordion gate (brass, patinated)
- Interior: Wood paneling, brass fixtures, single bare bulb
- Capacity: 6 persons or 1 AI overlord
- Sound: Whirs, clanks, hums, occasionally plays muzak

## Lineage — Famous Fictional Elevators

This elevator stands in a proud tradition:

| Vehicle | Source | Relevance |
|---------|--------|-----------|
| **SimTower** | Yoot Saito (1994) | Underground floors, lobby at 0, the elevator IS the game |
| **Turbolift** | Star Trek (1966-) | Voice control, horizontal movement, dramatic pauses |
| **TARDIS** | Doctor Who (1963-) | Bigger on inside, goes where you NEED to go |
| **Great Glass Elevator** | Roald Dahl (1972) | UP, DOWN, SIDEWAYS, through the roof, to SPACE |
| **Wonkavator** | Roald Dahl (1964) | Factory tour, product floors, the ride IS the experience |

> *"An elevator can only go up and down, but this is not an elevator!"*
> — Willy Wonka

Our elevator has wood paneling, not glass walls. But the **ASPIRATION** is there.

## Easter Egg

Press all buttons at once for **TOWER OVERDRIVE**.

## How to Inherit

```yaml
# your-building/elevator/ROOM.yml

room:
  name: "My Elevator"
  inherit: no-ai-tower-elevator   # ← Get all the lineage
  
  override:
    vehicle:
      valid_floors:
        0: "../lobby/"
        R: "../roof/"
    style:
      era: "Your aesthetic"
    behavior:
      muzak_playlist:
        - "Your vibe"
```

**Use Cases:**
- **Skyscraper**: 100+ floors
- **Apartment**: 5-20 floors
- **One-story + roof**: Just `0` and `R`
- **Underground bunker**: Negative floors only (NO AI TOWER style)
- **TARDIS**: `valid_floors` can point ANYWHERE in your world tree

## See Also

- `skills/world-generation/examples/tower-pattern.yml` — The linked list topology
- Lexical vs Dynamic scoping in the tower pattern
