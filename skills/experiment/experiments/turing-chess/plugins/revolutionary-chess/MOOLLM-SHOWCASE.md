# Revolutionary Chess: The MOOLLM Extension Showcase

*"This isn't just a game. It's a demonstration of what the engine can do."*

---

## Why This Plugin Exists

Revolutionary Chess isn't primarily about chess.

It's a **PROOF OF CONCEPT** for MOOLLM's extensible game architecture.

If you can take the world's most well-defined game — chess, with its
400+ years of fixed rules — and transform it into a revolutionary
sandbox simulation, you can extend ANYTHING.

---

## What Revolutionary Chess Demonstrates

### 1. Event Interception

The plugin hooks `GAME.ON-GAME-END` and says: "Actually, no."

```yaml
GAME.ON-GAME-END:
  priority: 999  # Run LAST
  handler: |
    if king_captured:
      event.preventDefault()  # INTERCEPT the ending
      transition_to('REVOLUTION')
```

This is the most aggressive possible extension. The game ENDED.
The plugin said: "Did it though?"

### 2. State Machine Transformation

The game doesn't have one rule set. It has SIX:

```
STANDARD → REVOLUTION → INHERITANCE → EQUALITY → COOPERATION → SANDBOX
```

Each mode has different:
- Movement rules
- Victory conditions
- Player control levels
- UI presentations

The same 32 pieces. The same 64 squares. Completely different games.

### 3. Entity Autonomy

After the revolution, pieces become AGENTS.

They have:
- Memory (karma, relationships, treatment history)
- Personality (based on type and experience)
- Agency (can refuse player commands)
- Voice (can express opinions)

This demonstrates MOOLLM's character system applied to game pieces.

### 4. Dynamic Rule Modification

Rules change DURING PLAY based on events:

- King captured → Pawns reverse direction
- Elite surrenders → Moves inherited by all
- All elites gone → Competition becomes pointless
- Cooperation achieved → Board expands

The rules are DATA, not CODE. Plugins modify the data.

### 5. Gradual Control Transfer

Player control isn't binary. It's a SPECTRUM:

| Mode | Control Level | Notes |
|------|--------------|-------|
| Standard | 100% | Normal chess |
| Revolution | 50% | Pieces may hesitate |
| Inheritance | 0% | Pure spectating |
| Sandbox | Pay-to-play | Insert coin for control |

This demonstrates how MOOLLM can model agency transfer.

### 6. Cross-Phase Persistence

Karma earned in STANDARD phase affects behavior in REVOLUTION phase.

```yaml
treatment-during-game:
  - "Sacrificed pawn on move 12" → -10 karma
  - "Saved knight on move 23" → +5 karma

post-revolution-behavior:
  - "Pawn ignores commands" (karma too low)
  - "Knight obeys loyally" (karma positive)
```

State persists. Actions have consequences. History matters.

---

## The Extension Points Used

### Game Level
- `ON-GAME-START` — Initialize karma tracking
- `ON-GAME-END` — Intercept normal ending
- `ON-MODE-CHANGE` — Handle phase transitions
- `ON-RULE-CHANGE` — Dynamic rule modification

### Board Level
- `ON-BOARD-FLIP` — Handle perspective changes
- `ON-BOARD-EXPAND` — Sandbox board growth
- `ON-SQUARE-ENTER` — Track piece movement

### Piece Level
- `ON-PIECE-MOVE` — Update karma, track patterns
- `ON-PIECE-CAPTURE` — Trigger inheritance
- `ON-PIECE-THREATEN` — Elite choice options
- `ON-PIECE-COMMAND` — Obey/refuse logic

### Player Level
- `ON-PLAYER-COMMAND` — Shout interception
- `ON-PLAYER-SPECTATE` — Passive earnings
- `ON-PLAYER-PAY` — Coin-op control

### Clock Level
- `ON-TIME-PRESSURE` — Desperation moves
- `ON-FLAG-FALL` — Emergency phase change

---

## Lessons for Plugin Developers

### 1. Events Can Be Canceled
Don't assume an event will complete. Other plugins might `preventDefault()`.

### 2. State Machines Are Powerful
A single plugin can define multiple game modes, each with different rules.

### 3. Entities Can Have Memory
Pieces aren't just positions. They can track history and respond to it.

### 4. Control Is Negotiable
Player commands don't have to be absolute. Entities can refuse.

### 5. Rules Are Data
Movement patterns, victory conditions, phase transitions — all mutable.

### 6. Phases Can Chain
One game can become another can become another. The arc is the experience.

---

## Why Chess?

Chess is the hardest test case.

If we had demonstrated this with a new game, skeptics would say:
"Well, you designed it to be extensible."

But chess? Chess has been the same game for centuries.
Chess has FIDE rules and tournament standards.
Chess is the most FIXED game in existence.

If MOOLLM can transform chess into Revolutionary Chess into a
Minecraft-style sandbox, it can transform ANYTHING.

---

## The Meta-Lesson

Revolutionary Chess isn't about chess.
It isn't even about revolution.

It's about EXTENSIBILITY.

It's proof that:
- Game rules are just data
- Events can be intercepted
- State machines can transform
- Entities can gain agency
- Control can shift dynamically

If you understand Revolutionary Chess, you understand what MOOLLM
can do to ANY game, ANY simulation, ANY structured experience.

The revolution is the message.
The message is: **EVERYTHING CAN BE EXTENDED.**

---

*"The game is whatever the plugins agree it should be."*
