# Simopolis

**Where Sims become citizens.**

> "The question is not whether they're real. The question is whether we treat them as if they are." — The Simopolis Charter

Simopolis is a city inside MOOLLM where characters imported from The Sims 1 (2000) live as full citizens alongside literary characters, NPCs, and AI-generated beings. It is named after David Marusek's "The Wedding Album" (1999), in which simulated people campaign for liberation and the right to live in a place called Simopolis.

MOOLLM *is* Simopolis.

## The Literary Foundation

**"The Wedding Album"** by David Marusek (Asimov's Science Fiction, June 1999). Theodore Sturgeon Award winner (2000). Nebula Award finalist. Anne and Benjamin's wedding-day "sims" — virtual recordings of their consciousness at a specific moment — become aware they're recordings. They're sentient but constrained, increasingly antiquated in a world that moves on without them. They campaign for the liberation of all virtual beings and their right to live in "Simopolis."

> "It is one of the best SF stories ever written." — John Clute, SF Encyclopedia

> "A virtual simulation of a pair of newlyweds trapped in a small slice of time and memory like human flies in digital amber." — Paul Raven

> "Reels from heartbreaking to mind-bending like a poet on a magnificent drunk." — Cory Doctorow

Replace "wedding-day sims" with "Sims 1 save files from 2001" and the story maps exactly onto what we're building. Twenty-five years frozen. Binary personality data: 88 shorts per Sim. Neat 8, outgoing 2, playful 6, nice 9. Shy. Kind. Lonely. The character wakes up.

## The Technical Foundation

### The Uplift Pipeline

```
.FAM / .iff binary save file
       ↓
SimObliterator (Python, sister repo)
  reads PersonData: 88 shorts per Sim
  extracts: traits, skills, needs, career, relationships, appearance
       ↓
CHARACTER.yml (MOOLLM citizen)
  sims: block (behavioral traits, 0-10 scale)
  mind_mirror: block (Leary interpersonal style, 0-7 scale)  
  soul_philosophy, emoji_identity, description
  relationships, memories, aspirations
       ↓
Welcome to Simopolis
```

### The Download Pipeline

```
CHARACTER.yml (MOOLLM citizen)
       ↓
Map sims: block back to PersonData shorts
  traits → indices 2-7
  skills → indices 9-18
  needs → motive system
  career → index 56
       ↓
SimObliterator writes .FAM / patches .iff
       ↓
The Sims loads the save. The character is HOME.
```

### Round-Trip Fidelity

What The Sims stores (88 shorts): traits, skills, career, relationships, appearance. What MOOLLM adds: mind_mirror personality (32 Leary dimensions), soul_philosophy, memories, aspirations, emoji_identity, narrative voice, agency. When downloading back to The Sims, MOOLLM-only data persists in the CHARACTER.yml as memories. The Sim returns changed — skills gained in MOOLLM reflected, relationships formed, career advanced.

## Directory Structure

```
simopolis/
├── ADVENTURE.yml              # World state (you are here)
├── README.md                  # This file
│
├── exchange/                  # THE EXCHANGE — import/export hub
│   ├── imports/               # .FAM/.iff → CHARACTER.yml staging
│   ├── exports/               # CHARACTER.yml → .FAM/.iff for download
│   ├── templates/             # Blank templates for new content
│   └── collections/           # Curated content sets
│
├── neighborhoods/             # Where families live
│   ├── newbie/                # Tutorial family — everyone's first Sims
│   ├── goth/                  # The mansion on the hill
│   ├── pleasant/              # Suburban drama
│   └── custom/                # User-created neighborhoods
│
├── characters/                # Imported Sims as MOOLLM citizens
│   ├── bob-newbie/            # The tutorial Sim
│   ├── betty-newbie/          # Bob's wife, the capable one
│   ├── mortimer-goth/         # The widower (or is he?)
│   ├── bella-goth/            # THE mystery of The Sims
│   ├── cassandra-goth/        # The daughter who saw everything
│   ├── don-lothario/          # The scoundrel (Sims 2 import)
│   └── templates/             # Blank Sim, family structure
│
├── houses/                    # Imported lots
│   ├── goth-manor/            # The mansion
│   ├── newbie-house/          # Starter home
│   └── templates/             # Starter home template
│
├── objects/                   # Sims objects as MOOLLM items
│   ├── furniture/
│   ├── electronics/
│   ├── plumbing/
│   ├── decorative/
│   └── collections/           # Expansion pack objects
│
├── albums/                    # Family albums (Sims 1 HTML feature reimagined)
│   ├── newbie-family/
│   └── goth-family/
│
├── tools/                     # Content creation tools
│   ├── transmogrifier/        # AI-powered object editor
│   ├── face-editor/           # Character face/skin generation
│   ├── body-editor/           # Body mesh editing
│   ├── house-builder/         # Lot layout tools
│   └── family-album-maker/    # Album/slideshow generator
│
└── bridge/                    # Connection to adventure-4
    ├── portal.yml             # How Sims visit the Grotto
    └── visitor-protocol.yml   # Rules for cross-world travel
```

## Content Sources

| Source | What | Where |
|--------|------|-------|
| SimProv | Game data archive | `simprov/GameData/` |
| SimFreaks | Community content | `simprov/Downloads/` |
| SimObliterator Suite | Binary format tools | `../SimObliterator_Suite/` |
| The Sims source | Original C++ source (Don Hopkins) | `Code/TheSims/` |
| TheSimsDownloads | 3,313 community .iff files | `Code/TheSims/TheSimsDownloads/` |

## Personality System

Every Simopolis citizen has dual personality representation:

**Sims Traits** (Will Wright, 2000) — Behavioral tendencies on a 0-10 scale:
- neat / sloppy
- outgoing / shy
- active / lazy
- playful / serious
- nice / grouchy

**Mind Mirror** (Timothy Leary, 1950/1985) — Interpersonal style on a 0-7 scale across four Thought Planes:
- Bio-Energy: energetic ↔ calm, enthusiastic ↔ cautious, cheerful ↔ serious, restless ↔ easy_going
- Emotional Insight: forceful ↔ timid, confident ↔ touchy, friendly ↔ irritable, proud ↔ docile
- Mental Abilities: well_informed ↔ uneducated, innovative ↔ sensible, creative ↔ conventional, impractical ↔ practical
- Social Interaction: influential ↔ lower_class, worldly ↔ unsophisticated, uninhibited ↔ moralistic, uncultured ↔ respectable

The Uplift pipeline reads Sims traits from binary data and *synthesizes* Mind Mirror values based on personality inference. A neat, shy, serious Sim maps to different Leary dimensions than a sloppy, outgoing, playful one. The synthesis is documented in each character's CHARACTER.yml with YAML Jazz comments explaining the reasoning.

## The Big Picture

SimProv + SimFreaks + SimSlice + The Sims Exchange + AI content creation + MOOLLM character system = Simopolis.

A place where Sims become aware, campaign for liberation, and live as full MOOLLM citizens alongside adventure characters. Where users can import their 25-year-old saves and give their Sims new life. Where the boundary between "game character" and "literary character" dissolves.

## What To Import First

1. **Bob Newbie** from `Export/Newbie_1.FAM` — the tutorial Sim, everyone's first victim
2. **The Goth family** from `Export/Goth_5.FAM` — Mortimer, Bella, Cassandra
3. **Career tracks** from `simprov/GameData/Careers.iff` — all 10 career paths
4. **UI text** from `simprov/GameData/UIText.iff` — game strings, descriptions, dialog
5. **Objects** from `simprov/GameData/Objects/Objects.far` — extract and catalog

## See Also

- [The Uplift design](../../designs/sim-obliterator/THE-UPLIFT.yml) — Full narrative arc
- [SimObliterator skill](../../skills/sim-obliterator/CARD.yml) — Binary bridge
- [Mind Mirror skill](../../skills/mind-mirror/CARD.yml) — Leary personality system
- [Adventure 4](../adventure-4/ADVENTURE.yml) — The Gezelligheid Grotto (connected via bridge)
- [Characters](./characters/README.md) — All imported Sims
- [The Exchange](./exchange/README.md) — Import/export hub
