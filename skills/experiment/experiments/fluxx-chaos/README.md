# Fluxx Chaos Experiment

🎴 **AI characters playing Fluxx while rules constantly change — with dynamic card generation, cosmic karma, and emergent game mechanics**

## What Is This?

An experiment where AI-generated characters play the card game Fluxx — a game where the rules themselves are cards that can be played, creating chaotic emergent gameplay.

**This became a 4-hour, 731-tool-call session that produced:**
- 5 tournaments, 20+ games, 116+ turns of simulated gameplay
- 24 dynamically generated personal cards forged from character stories
- 32 pieces of AI-generated artwork
- Emergent mechanics (FAFO Token Paradox, Silent Victory Protocol)
- Research-grade analysis with rubrics and scoring

The experiment tracks:
- **Game mechanics** — cards, rules, goals, hands, keepers
- **Character psychology** — personality-driven decisions, grudges, alliances
- **Dynamic card generation** — personal cards forged from dramatic moments
- **Karma systems** — FAFO Token that punishes gloating
- **Art generation** — each card gets pure artwork via stereo prompts
- **Narrative** — emergent stories with in-character dialogue
- **Card signatures** — players sign cards at emotional moments

---

## 🏆 Featured Run: Amsterdam Flux

Four characters. Five tournaments. Twenty games. One hundred sixteen turns. Thousands of ironic twists.

### 🔥 START HERE

| Document | What You'll Find |
|----------|------------------|
| **[📊 SCORE.md](runs/amsterdam-flux/SCORE.md)** | **Research-grade scoring** — rubrics, Harper numbers, card signatures, player roundtable |
| **[🔍 Cursor Mirror Analysis](runs/amsterdam-flux/CURSOR-MIRROR-ANALYSIS.md)** | Meta-analysis of 731 tool calls |
| **[🎨 Card Artwork Slideshow](runs/amsterdam-flux/artwork/SLIDESHOW.md)** | 32 cards with generation history |
| **[🃏 Generated Cards](runs/amsterdam-flux/generated-cards.yml)** | 24 personal cards with signatures |

### 📊 The Numbers

| Stat | Value |
|------|-------|
| Tournaments | **5** |
| Games simulated | **20+** |
| Total turns | **116+** |
| Standard cards with art | 32 |
| Generated personal cards | **24** |
| Card signatures | **13+** |
| Cookie mentions | **271** |
| FAFO Token transfers | **5** |
| Session duration | ~4 hours |
| Tool calls | **731** |

### 🎭 Emergent Mechanics

These weren't designed — they emerged from gameplay:

| Mechanic | What Happened |
|----------|---------------|
| **FAFO Token Paradox** | Can't win with creeper, even floating |
| **Silent Victory Protocol** | Don't gloat = survive |
| **Melodramatic Loophole** | Wailing ≠ confidence |

### 📁 Quick Links

| Resource | Description |
|----------|-------------|
| **[SCORE.md](runs/amsterdam-flux/SCORE.md)** | ⭐ Full analysis with rubrics |
| **[CURSOR-MIRROR-ANALYSIS.md](runs/amsterdam-flux/CURSOR-MIRROR-ANALYSIS.md)** | Session introspection |
| [Card Artwork Slideshow](runs/amsterdam-flux/artwork/SLIDESHOW.md) | Visual gallery |
| [Generated Cards](runs/amsterdam-flux/generated-cards.yml) | 24 personal cards |
| [Game Protocol](runs/amsterdam-flux/PROTOCOL.md) | How the simulation works |
| [Run Files](runs/amsterdam-flux/) | RUN-000.yml through RUN-023.yml |

## Directory Structure

```
fluxx-chaos/
├── README.md               # You are here
├── cards/                  # Card definitions by type
│   ├── keepers.yml
│   ├── goals.yml
│   └── ...
├── cardsets/               # Deck configurations
│   └── fluxx-4.0.yml
├── engine/                 # Rule processing
│   └── rules.yml
├── runs/                   # Simulation runs
│   ├── INDEX.yml
│   └── amsterdam-flux/     # ⭐ Featured run
│       ├── artwork/        # Card art + generation history
│       ├── RUN-*.yml       # Game state snapshots
│       ├── RUN-*.md        # Narrative descriptions
│       └── PROTOCOL.md     # How append-only works
└── state/                  # Shared state definitions
```

## The Experiment Loop

```
┌─────────────────────────────────────────────┐
│  Define cardset + characters + rules        │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Simulate game turns (append-only state)    │
│  → RUN-001.yml, RUN-002.yml, ...            │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Generate card artwork (stereo prompts)     │
│  → NN-name.yml + NN-name.md → NN-name.png   │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Image mining + quality control             │
│  → NN-name-mined.yml                        │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Iterate on failures (autonomous reroll)    │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Document learnings (SLIDESHOW.md)          │
└─────────────────────────────────────────────┘
```

## Key Innovation: Stereo Prompts

Each card gets two prompts fed together to the image generator:

1. **YAML skeleton** (`NN-name.yml`) — structured constraints
2. **Prose description** (`NN-name.md`) — evocative atmosphere

This "stereo" approach gives the model both precision and poetry.

## What We Learned

See the [full analysis in the slideshow](runs/amsterdam-flux/artwork/SLIDESHOW.md#analysis-failed-generations--prompt-engineering-lessons) for:

- Why "board game card art" triggers unwanted UI overlays
- How to translate emotions into visual specifications
- The difference between describing what you see vs. how good it is
- When to use abstract symbols vs. specific instances

---

*Part of the [MOOLLM](https://github.com/SimHacker/moollm) experiment skill.*
