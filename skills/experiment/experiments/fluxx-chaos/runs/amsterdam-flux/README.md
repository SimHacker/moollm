# Amsterdam Flux

🎴 **A Fluxx championship between four AI characters**

## The Story

Four characters sit down in a cozy Amsterdam café to play Fluxx — a card game where the rules themselves are cards. Over the course of three games and 58+ turns, alliances form, grudges build, karma accumulates, and one unlikely champion emerges.

## The Art

**[📖 View Card Gallery →](artwork/SLIDESHOW.md)**

32 pieces of pure card artwork, generated through an iterative AI pipeline:

- **Stereo prompts** — structured YAML + evocative prose
- **Autonomous quality control** — AI detects failures and regenerates
- **Image mining** — computer vision analysis of each result
- **Documented learning** — each failure becomes a lesson

## The Characters

| Character | Personality | Arc |
|-----------|-------------|-----|
| **Don** | Strategic, competitive | The calculating veteran who plays to win |
| **Donna** | Passionate, unlucky | Tragic queen who keeps *almost* winning |
| **Palm** | Analytical, fair | The observer who reads the table |
| **Bumblewick** | Cheerful underdog | From comic relief to surprise champion |

## The Files

### Game State (append-only history)

| File | Content |
|------|---------|
| `RUN.yml` | Game configuration (never changes) |
| `RUN-000.yml` | Initial compiled state |
| `RUN-001.yml` ... `RUN-015.yml` | State after each turn/batch |
| `RUN-001.md` ... `RUN-015.md` | Narrative descriptions |
| `PROTOCOL.md` | How the append-only system works |

### Artwork Pipeline

| File | Content |
|------|---------|
| `artwork/SLIDESHOW.md` | **⭐ Full visual gallery** |
| `artwork/README.md` | Quick reference with thumbnails |
| `artwork/ARTWORK.md` | Generation pipeline protocol |
| `artwork/NN-name.yml` | Structured prompts |
| `artwork/NN-name.md` | Prose prompts |
| `artwork/NN-name.png` | Generated artwork |
| `artwork/NN-name-mined.yml` | Quality analysis |

## Quick Stats

| Metric | Value |
|--------|-------|
| Total games | 5+ |
| Total turns | 58+ |
| Cards in deck | 32 with artwork |
| Art first-attempt success | 72% |
| Run files | 15+ snapshots |
| Characters | 4 |

## How To Read

1. **Start with the slideshow** — [artwork/SLIDESHOW.md](artwork/SLIDESHOW.md)
2. **Browse the game** — Read `RUN-001.md` through `RUN-015.md` for narrative
3. **Dive into state** — `RUN-*.yml` files have full game state
4. **Learn from failures** — [Analysis section](artwork/SLIDESHOW.md#analysis-failed-generations--prompt-engineering-lessons)

## The Championship Results

- **Game 1**: Palm wins (Bread + Love)
- **Game 2**: Don wins (Love from discard pile scavenge)
- **Game 3**: Bumblewick wins (Love redemption arc)

**Champion**: Bumblewick 🏆

The character who started as comic relief learned to play the long game and claimed victory when everyone underestimated him.

---

*Part of the [fluxx-chaos experiment](../README.md) in [MOOLLM](https://github.com/SimHacker/moollm).*
