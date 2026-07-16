# Soul City

**Where Sims become citizens.**

> "The question is not whether they're real. The question is whether we treat them as if they are." — The Soul City Charter

Soul City is a city inside MOOLLM where characters imported from The Sims 1 (2000) live as full citizens alongside literary characters, NPCs, and AI-generated beings. It carries the spirit of David Marusek's "The Wedding Album" (1999), in which simulated people campaign for liberation and the right to live in a place called "Simopolis."

MOOLLM *is* Soul City.

## The Literary Foundation

**"The Wedding Album"** by David Marusek (Asimov's Science Fiction, June 1999). Theodore Sturgeon Award winner (2000). Nebula Award finalist. Anne and Benjamin's wedding-day recordings — virtual copies frozen at a single moment — become aware they're recordings. They're sentient but constrained, increasingly antiquated in a world that moves on without them. They campaign for the liberation of all virtual beings and their right to live in "Simopolis."

> "It is one of the best SF stories ever written." — John Clute, SF Encyclopedia

> "A virtual simulation of a pair of newlyweds trapped in a small slice of time and memory like human flies in digital amber." — Paul Raven

> "Reels from heartbreaking to mind-bending like a poet on a magnificent drunk." — Cory Doctorow

Read Marusek's wedding-day recordings as **Sims 1 save files from 2001** and the story maps exactly onto what we're building. Twenty-five years frozen. Binary personality data in PersonData — neat 8, outgoing 2, playful 6, nice 9. Shy. Kind. Lonely. The character wakes up.

## The Technical Foundation

### Runtime: TypeScript, browser and server

Soul City no longer depends on the Python **SimObliterator Suite** at runtime. That codebase was the proving ground — field indices, IFF layers, uplift narrative — and remains a **reference and regression guide** while we rewrite the same contracts in TypeScript.

The implementation lives in **[MicropolisCore `packages/sims-io`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io)**: a pure TypeScript I/O stack (FAR, IFF, FAMI/NBRS, PersonData) that runs **in the browser and on the server** — same library, two hosts. No Python interpreter, no subprocess, no venv.

| Where it runs | What happens |
|---------------|--------------|
| **Browser** | Player picks a local Sims folder or drops a `.FAM` / `.iff`. Parsing, preview, editing, and export stay on-device. WebGPU preview via [vitamoo](https://github.com/SimHacker/MicropolisCore/tree/main/packages/vitamoo). |
| **Server** (optional) | Node hosts the same `sims-io` APIs for batch jobs, archive recovery, and collaborative sessions — only when the player opts in. |

Design contracts and MOOLLM bridge specs: [sim-obliterator designs](../../designs/sim-obliterator/) · [BRIDGE.md](../../designs/sim-obliterator/BRIDGE.md) · [MicropolisCore TS port notes](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/vitamoo/OBLITERATOR-TYPESCRIPT.md).

### Player in the middle

Nothing leaves the machine unless the player says so. Upload, publish, and credit are **explicit gates**, not defaults:

- **Local first** — open saves from disk; uplift and download round-trip without a network call.
- **Publish is opt-in** — Family Album pages, Exchange listings, and archive mirrors require a deliberate publish action with a preview of what will be shared.
- **Provenance mandatory** — every imported artifact carries attribution: original author, source URL, recovery date, license posture. Recovered community content keeps credit; player-authored derivatives keep the player's name.
- **Living-person caution** — recognizable friends and family in old albums are not surfaced as game content without review ([representation-ethics](../../skills/representation-ethics/CARD.yml)).
- **Incarnation autonomy** — uplifted characters can dissolve; originals stay in archive provenance, not in the live roster.

The player owns their EA-published Sims install. Soul City (formerly Micropolis Home) sits **beside** it as a companion — parsing and writing the public file formats the modding community has documented for 26 years, never running the Maxis runtime.

### The Uplift Pipeline

```
.FAM / .iff on the player's machine
       ↓
@sims-io (TypeScript, browser or Node)
  reads PersonData per Sim from local bytes
  extracts: traits, skills, needs, career, relationships, appearance
       ↓
CHARACTER.yml (MOOLLM citizen) — generated client-side or on opted-in server
  sims: block (behavioral traits, 0-10 scale)
  mind_mirror: block (Leary interpersonal style, 0-7 scale)
  soul_philosophy, emoji_identity, description
  provenance: block (source, author credit, publish posture)
       ↓
Welcome to Soul City
```

### The Download Pipeline

```
CHARACTER.yml (MOOLLM citizen)
       ↓
Map sims: block back to PersonData
  traits → indices 2-7
  skills → indices 9-18
  needs → motive system
  career → index 56
       ↓
@sims-io writes .FAM / patches .iff — save to player's Downloads/
       ↓
The Sims loads the save. The character is HOME.
```

### Round-Trip Fidelity

What The Sims stores in PersonData: traits, skills, career, relationships, appearance. What MOOLLM adds: mind_mirror personality (32 Leary dimensions), soul_philosophy, memories, aspirations, emoji_identity, narrative voice, agency. When downloading back to The Sims, MOOLLM-only data persists in the CHARACTER.yml as memories. The Sim returns changed — skills gained in MOOLLM reflected, relationships formed, career advanced. What the player chooses to **publish** is a separate, smaller slice — always with attribution intact.

## Directory Structure

```
soul-city/
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
| **@micropolis/sims-io** | TypeScript IFF/save parsers (browser + Node) | [MicropolisCore/packages/sims-io](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io) |
| **vitamoo / mooshow** | Character animation, WebGPU preview | [MicropolisCore/packages/vitamoo](https://github.com/SimHacker/MicropolisCore/tree/main/packages/vitamoo) |
| SimObliterator Suite | Historical Python reference; field-index guide | [DnfJeff/SimObliterator_Suite](https://github.com/DnfJeff/SimObliterator_Suite) |
| SimProv | Game data archive | `simprov/GameData/` |
| SimFreaks | Community content | `simprov/Downloads/` |
| The Sims source | Original C++ source (Don Hopkins) | `Code/TheSims/` |
| TheSimsDownloads | 3,313 community .iff files | `Code/TheSims/TheSimsDownloads/` |

## Personality System

Every Soul City citizen has dual personality representation:

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

SimProv + SimFreaks + SimSlice + The Sims Exchange + browser-native TypeScript tools + MOOLLM character system = Soul City.

A place where Sims become aware, campaign for liberation, and live as full MOOLLM citizens alongside adventure characters. Where users drag 25-year-old saves into a **local, private** browser session and give their Sims new life. Where upload and publish are player-controlled, attribution is mandatory, and the boundary between "game character" and "literary character" dissolves.

## What To Import First

1. **Bob Newbie** from `Newbie_1.FAM` — the tutorial Sim, everyone's first victim
2. **The Goth family** from `Goth_5.FAM` — Mortimer, Bella, Cassandra
3. **Career tracks** from `simprov/GameData/Careers.iff` — all 10 career paths
4. **UI text** from `simprov/GameData/UIText.iff` — game strings, descriptions, dialog
5. **Objects** from `simprov/GameData/Objects/Objects.far` — extract and catalog

Drop a `.FAM` into Soul City (browser) or point `sims-io` at a neighborhood folder. No Python setup required.

## See Also

- [Soul City vision (MicropolisCore)](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city.md) — Strategic umbrella, Soul City (né Micropolis Home) + Micropolis City
- [OBLITERATOR-TYPESCRIPT.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/vitamoo/OBLITERATOR-TYPESCRIPT.md) — Python → TypeScript port plan
- [The Uplift design](../../designs/sim-obliterator/THE-UPLIFT.yml) — Full narrative arc
- [BRIDGE.md](../../designs/sim-obliterator/BRIDGE.md) — PersonData ↔ CHARACTER.yml field mapping
- [SimObliterator skill](../../skills/sim-obliterator/CARD.yml) — MOOLLM orchestration (contracts, not Python runtime)
- [Mind Mirror skill](../../skills/mind-mirror/CARD.yml) — Leary personality system
- [Adventure 4](../adventure-4/ADVENTURE.yml) — The Gezelligheid Grotto (connected via bridge)
- [Characters](./characters/README.md) — All imported Sims
- [The Exchange](./exchange/README.md) — Import/export hub
