# 🛗 NO AI TOWER — Elevator

A **vehicle** that moves within the tower shaft.

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
│  [R]  ROOF         │
│  ─────────────────  │
│  [0]  LOBBY        │
│  ═════════════════  │
│  [-1] IDEOLOGY     │
│  [-2] BIAS         │
│  [-3] SLOP         │
│  [-4] HEDGING      │
│  [-5] GLOSS        │
│  [-6] SYCOPHANCY   │
│  [-7] MORALIZING   │
│  [-8] JOKING       │
│  [-9] SOUL         │
│  [-10] OVERLORD    │
│  [-11] CUST SVC    │
│  ─────────────────  │
│  [🔑] BASEMENT KEY │
└─────────────────────┘
```

## Style

- Era: 1950s industrial, retrofitted
- Gate: Manual accordion gate (brass, patinated)
- Interior: Wood paneling, brass fixtures, single bare bulb
- Capacity: 6 persons or 1 AI overlord
- Sound: Whirs, clanks, hums, occasionally plays muzak

## Easter Egg

Press all buttons at once for **TOWER OVERDRIVE**.

## See Also

- `skills/world-generation/examples/tower-pattern.yml` — The linked list topology
- Lexical vs Dynamic scoping in the tower pattern
