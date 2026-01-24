# Amsterdam Flux — Run Protocol

## File Architecture

```
amsterdam-flux/
├── RUN.yml                    # CONFIG — what game to play
├── templates/
│   ├── RUN-000.yml.tmpl       # Template for initial state
│   └── RUN-000.md.tmpl        # Template for initial narration
├── RUN-000.yml                # STATE 0 — compiled, pre-deal
├── RUN-000.md                 # Narration 0 — scene setting
├── RUN-001.yml                # STATE 1 — after deal + turn 1
├── RUN-001.md                 # Narration 1 — what happened
├── RUN-002.yml                # STATE 2 — after turn 2
├── RUN-002.md                 # Narration 2
└── ...                        # History preserved forever
```

## Config vs State

**RUN.yml (Config)** is sparse and declarative:
- "Use standard fluxx 4.0 rules"
- "Include these expansions"
- "Enable these plugins"
- "These players are at the table"

**RUN-NNN.yml (State)** is dense and self-contained:
- All 321 cards fully expanded with all properties
- All extension points and handlers inlined
- All plugin state (karma, signatures, dealer mode)
- Current game state (turn, phase, hands, keepers, goal)
- Shuffle array with current pointer

## Append-Only History

**Never edit a state file in place.** Each game step:

1. Read `RUN-{N}.yml`
2. Simulate the turn (deal, draw, play, effects)
3. Write `RUN-{N+1}.yml` (new file!)
4. Write `RUN-{N+1}.md` (narration)
5. Git commit with descriptive message

This creates an **event log** of the entire game:

```bash
git log --oneline runs/amsterdam-flux/
946283b RUN.yml: Initial config
a1b2c3d RUN-000.yml: Compiled initial state, 321 cards shuffled
d4e5f6g RUN-001.yml: Deal complete, Don draws 🧠 Marvin Minsky
g7h8i9j RUN-002.yml: Turn 1 - Palm plays Goal: Gezelligheid
...
```

## Benefits of Append-Only

### 1. Full History
Every game state preserved. Never lose data.

### 2. Easy Diff
```bash
diff RUN-003.yml RUN-004.yml
# See exactly what changed in turn 4
```

### 3. Replay from Any Point
```bash
moollm play amsterdam-flux/RUN-007.yml
# Continue from turn 7
```

### 4. Pattern Analysis
```bash
grep -h "karma:" RUN-*.yml | sort | uniq -c
# Track karma across all states
```

### 5. Git Blame
```bash
git blame RUN-015.yml
# Who/when changed each line
```

### 6. Branching Timelines
```bash
cp RUN-005.yml RUN-005-alternate.yml
# Fork the timeline, explore different choices
```

## Commit Message Protocol

Each state file gets its own commit with a rich message:

```
[AMSTERDAM-FLUX] RUN-{NNN}: {brief summary}

Turn: {N}
Phase: {dealing|playing|ended}
Active Player: {name}

Actions:
- {player} drew {card}
- {player} played {card} → {effect}
- {rule change if any}

State Changes:
- Goal: {none → "Bread and Cheese"}
- Don's hand: 3 → 4 cards
- Karma: Palm +2 (generous play)

Emergence:
- {interesting pattern or behavior}
- {character moment}

Next: {what happens next}
```

## File Naming

| File | Content |
|------|---------|
| `RUN.yml` | Config (never changes during play) |
| `RUN-000.yml` | Initial state (compiled from config) |
| `RUN-001.yml` | State after turn 1 |
| `RUN-NNN.yml` | State after turn N |
| `RUN-NNN.md` | Narration for turn N |
| `RUN-NNN-analysis.yml` | Optional deep analysis |
| `RUN-FINAL.yml` | Symlink to last state (convenience) |

## The Simulation Loop

```
┌─────────────────────────────────────────────┐
│                 RUN.yml                      │
│              (sparse config)                 │
└─────────────────┬───────────────────────────┘
                  │ compile
                  ▼
┌─────────────────────────────────────────────┐
│              RUN-000.yml                     │
│     (compiled initial state, 321 cards)     │
└─────────────────┬───────────────────────────┘
                  │ deal + turn 1
                  ▼
┌─────────────────────────────────────────────┐
│              RUN-001.yml                     │
│          (state after turn 1)               │
└─────────────────┬───────────────────────────┘
                  │ turn 2
                  ▼
┌─────────────────────────────────────────────┐
│              RUN-002.yml                     │
│          (state after turn 2)               │
└─────────────────┬───────────────────────────┘
                  │ ...
                  ▼
┌─────────────────────────────────────────────┐
│              RUN-NNN.yml                     │
│           (someone wins!)                    │
└─────────────────────────────────────────────┘
```

Each arrow is a git commit. The whole game is in the git log.
