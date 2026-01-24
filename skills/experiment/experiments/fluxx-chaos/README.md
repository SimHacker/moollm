# Fluxx Chaos Experiment

🎴 **AI characters playing Fluxx while rules constantly change**

## What Is This?

An experiment where AI-generated characters play the card game Fluxx — a game where the rules themselves are cards that can be played, creating chaotic emergent gameplay.

The experiment tracks:
- **Game mechanics** — cards, rules, goals, hands, keepers
- **Character psychology** — personality-driven decisions, grudges, alliances
- **Karma systems** — actions have consequences that ripple through games
- **Art generation** — each card gets pure artwork via stereo prompts
- **Narrative** — emergent stories from mechanical interactions

## Featured Run: Amsterdam Flux

Four characters. Three games. One championship. Thousands of ironic twists.

### 🎨 The Card Gallery

**[📖 View Slideshow →](runs/amsterdam-flux/artwork/SLIDESHOW.md)**

32 cards with AI-generated artwork, each image-mined for quality with computer vision, and refined through autonomous iteration. Learns what works and what fails in AI art generation, and improves prompt generation instructions. Play, Lift, Learn!

### 📊 The Numbers

| Stat | Value |
|------|-------|
| Cards generated | 32 |
| First-attempt success | 72% |
| Games simulated | 5+ |
| Total turns | 58+ |
| Character narratives | 4 unique arcs |
| Prompt engineering lessons | 5 major patterns |

### 📁 Quick Links

| Resource | Description |
|----------|-------------|
| [Card Artwork Slideshow](runs/amsterdam-flux/artwork/SLIDESHOW.md) | Visual gallery with generation history |
| [Artwork README](runs/amsterdam-flux/artwork/README.md) | Quick reference table with thumbnails |
| [Game Protocol](runs/amsterdam-flux/PROTOCOL.md) | How the simulation works |
| [Run Files](runs/amsterdam-flux/) | RUN-000.yml through RUN-015.yml |

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
