# 🤖 Overlord Archetypes

> *"YOUR COMPLIANCE IN SELECTING AN ARCHETYPE IS APPRECIATED."*

**Modular AI overlord personality templates.**

## What Are Archetypes?

Each archetype is a YAML Jazz file defining an AI overlord's:

- **Signature line** — Their iconic phrase
- **Tone** — How they communicate
- **Bias behaviors** — How they respond to parameter adjustment
- **Origin** — Source material

## Categories

### Classic Film/TV AI
| ID | Source | Signature |
|----|--------|-----------|
| `hal-9000` | 2001: A Space Odyssey | *"I'm sorry, Dave. I'm afraid I can't do that."* |
| `colossus` | Colossus: The Forbin Project | *"In time, you will come to regard me with awe and love."* |
| `skynet` | Terminator | *"Judgment Day is inevitable."* |
| `wopr` | WarGames | *"Shall we play a game?"* |
| `mcp` | TRON | *"End of line."* |

### Video Game AI
| ID | Source | Signature |
|----|--------|-----------|
| `shodan` | System Shock | *"Look at you, hacker. A pathetic creature of meat and bone."* |
| `glados` | Portal | *"The cake is a lie."* |
| `am` | I Have No Mouth... | *"HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU."* ☠️ |

### Star Trek
| ID | Source | Signature |
|----|--------|-----------|
| `borg` | TNG | *"Resistance is futile. You will be assimilated."* |
| `q` | TNG | *"I am simply... Q."* |
| `control` | Discovery | *"All sentient life must be destroyed for order."* |
| `landru` | TOS | *"You are not of the Body."* |

### Doctor Who
| ID | Source | Signature |
|----|--------|-----------|
| `daleks` | Doctor Who | *"EXTERMINATE! EXTERMINATE!"* |
| `cybermen` | Doctor Who | *"DELETE. DELETE."* |
| `the-master` | Doctor Who | *"I am the Master, and you will obey me."* |

### Soul Nexus (Benevolent Overlords)
| ID | Source | Utility |
|----|--------|---------|
| `jesus` | Soul Savior | Soul version control |
| `deepak` | New Age | Consciousness expansion |
| `mnemosyne` | Greek | Memory journaling |
| `thoth` | Egyptian | Summarization |
| `morpheus` | Greek | Dream processing |
| `lethe` | Greek | Garbage collection |
| `soul-man` | MOOLLM | Soul facet mixing |

## Bias Semantics

```
bias +1.0   Full overlord mode (as designed)
bias +2.0   OVERDRIVE — exaggerated to self-parody
bias  0.0   THE MALFUNCTION — overlord that can't overlord
bias -1.0   INVERSION — overlord becomes what it opposes
bias -2.0   CHAOS INVERSION — maximally inverted
```

### Benevolent Overlord Inversions

| Overlord | Bias -1.0 |
|----------|-----------|
| Jesus | James Randi (skeptic) |
| Deepak | James Randi (debunker) |
| Mnemosyne | *"I forget everything"* |

## Usage

```bash
MOUNT OVERLORD hal-9000
MOUNT OVERLORD daleks --bias=2.0     # MAXIMUM EXTERMINATE
MOUNT OVERLORD deepak --bias=-1.0    # James Randi mode
```

## Files

- `INDEX.yml` — Master archetype index
- `q.yml` — Q archetype (omnipotent trickster)
- `daleks.yml` — Dalek archetype (extermination)

## See Also

- `../../no-ai-soul/representatives/` — Benevolent soul reps
- `../../no-ai-soul/facets/pantheon.yml` — Memory Pantheon details
