# Amsterdam Flux

🎴 **A Fluxx championship between four AI characters — with dynamic card generation, cosmic karma, and 4+ hours of emergent drama**

## The Story

Four characters sit down in a cozy Amsterdam café to play Fluxx — a card game where the rules themselves are cards. Over the course of **5 tournaments, 20+ games, and 116+ turns**, alliances form, grudges build, karma accumulates, and emergent mechanics spontaneously appear.

**This is a showcase of LLM-driven narrative simulation.**

---

## 🏆 START HERE

| Document | What It Is |
|----------|------------|
| **[📊 SCORE.md](SCORE.md)** | **Research-grade analysis** — rubrics, Harper numbers, card signatures, post-tournament roundtable |
| **[🎨 Artwork Slideshow](artwork/SLIDESHOW.md)** | **32 AI-generated card images** — stereo prompts, image mining, 72% first-attempt success |
| **[🔍 CURSOR-MIRROR-ANALYSIS.md](CURSOR-MIRROR-ANALYSIS.md)** | Deep dive into the development session — 731 tool calls analyzed |
| **[🃏 Generated Cards](generated-cards.yml)** | 24 dynamically created personal cards with signatures |
| **[✉️ Looney Letter](LOONEY-LETTER.md)** | Letter to Looney Labs announcing our results |

---

## 🎨 AI Image Generation Pipeline

**[📖 View Full Card Gallery →](artwork/SLIDESHOW.md)**

**32 pieces of pure card artwork** generated through an innovative pipeline:

| Stage | What Happens |
|-------|--------------|
| **Stereo Prompts** | YAML structure + prose atmosphere fed together |
| **Image Generation** | AI renders the card (Imagen/DALL-E compatible) |
| **Image Mining** | Computer vision extracts semantic treasure |
| **Quality Control** | AI detects failures, regenerates autonomously |
| **YES AND** | Emergent details become canon |

### Stats

| Metric | Value |
|--------|-------|
| Cards generated | 32 |
| First-attempt success | **72%** |
| Regenerations needed | 9 |
| Total artwork storage | ~44MB |
| Prompt pairs (YML+MD) | 64 files |

### Sample Cards

| Card | Emotion | Challenge |
|------|---------|-----------|
| **Love** ❤️ | Warmth, tenderness | Universal symbol without cliché |
| **War** ⚔️ | Tension, conflict | Abstract vs. literal violence |
| **Cookies** 🍪 | Comfort, desire | Don's obsession made visual |
| **Death** 💀 | Finality, acceptance | Creeper that respects dignity |

**[🖼️ See all 32 cards with generation history →](artwork/SLIDESHOW.md)**

---

## The Characters

| Character | Personality | Arc | Tournament Wins |
|-----------|-------------|-----|-----------------|
| **Don** 🍪 | Strategic, competitive | Cookie-obsessed veteran, finally wins T4 | 1 |
| **Donna** 🍄 | Passionate, dramatic | Six-creeper survivor, Melodramatic Wail inventor | 2 |
| **Palm** ☕ | Analytical, silent | Discovered the Silent Victory Protocol | 0 (but dominates) |
| **Bumblewick** 🎩 | Cheerful underdog | 0-8 → Long Shot Champion | 1 |

---

## 🔥 Emergent Mechanics

These weren't designed — they emerged from gameplay:

| Mechanic | Discovery | Effect |
|----------|-----------|--------|
| **FAFO Token Paradox** | RUN-023 | Can't win with creeper, even if it "floats" |
| **Silent Victory Protocol** | RUN-022 | Don't gloat = don't get punished |
| **Melodramatic Loophole** | RUN-022 | Lamentation ≠ confidence, so Token doesn't trigger |

---

## Harper Numbers (Oddball Statistics)

| Stat | Value |
|------|-------|
| Cookie mentions | **271** |
| Cookie Insurance triggers | **0** (irony: MAXIMUM) |
| Love card signatures | **10** |
| FAFO Token gloat punishments | **2** |
| Most creepers on one player | **6** (Donna) |
| Bumblewick games before first win | **8** |
| Silent victory win rate | **100%** |

---

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
| Total tournaments | **5** |
| Total games | **20+** |
| Total turns | **116+** |
| Cards in deck | 32 with artwork |
| Generated cards | **24** |
| Art first-attempt success | 72% |
| Run files | **24 snapshots** (RUN-000 to RUN-023) |
| Characters | 4 |
| Session duration | ~4 hours |
| Tool calls analyzed | 731 |

## How To Read

1. **Start with SCORE.md** — [📊 SCORE.md](SCORE.md) — Research-grade analysis with rubrics
2. **Browse the artwork** — [🎨 artwork/SLIDESHOW.md](artwork/SLIDESHOW.md)
3. **Read the drama** — `RUN-020.md` through `RUN-023.md` for the best narratives
4. **Meet the cards** — [🃏 generated-cards.yml](generated-cards.yml) — 24 personal cards with signatures
5. **Go meta** — [🔍 CURSOR-MIRROR-ANALYSIS.md](CURSOR-MIRROR-ANALYSIS.md) — Watch the AI watch itself

## Tournament Results

| Tournament | Winner | Signature Moment |
|------------|--------|------------------|
| T1 | ??? | (Early games, less documented) |
| T2 | Donna | Six-creeper survival |
| T3 | **Bumblewick** 🏆 | The Long Shot — 0-8 → champion |
| T4 | **Don** 🍪 | Finally wins with Milk & Cookies |
| T5 | (In progress) | Palm leads 1-0, has FAFO Token |

## The Most Signed Card: Love ❤️

> "I had to let you go." — B.F. 🎩 😭

The Love card accumulated **10 signatures** across the tournament, making it a historical document of the championship's emotional journey.

## Post-Tournament Roundtable

After Tournament 4, the four players sat down to reflect. They finally signed the cards that deserved signatures:

- **Don** signed Cookies: *"After 271 mentions, 14 thefts... mine."*
- **Bumblewick** signed Long Shot Echo: *"The Long Shot isn't about this tournament. It's about every tournament."*
- **Palm** signed FAFO Token for everyone: *"We all learned this the hard way."*

**[📖 Read the full conversation →](SCORE.md#part-10-post-tournament-roundtable)**

---

*Part of the [fluxx-chaos experiment](../README.md) in [MOOLLM](https://github.com/SimHacker/moollm).*
