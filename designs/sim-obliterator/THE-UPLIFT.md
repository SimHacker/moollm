# The Uplift: Sims ↔ MOOLLM Character Bridge

> *Twenty-five years frozen. One drag and drop. A whole new life.*

**Status:** Design  
**Data source:** [THE-UPLIFT.yml](THE-UPLIFT.yml)  
**Related:** [BRIDGE.md](BRIDGE.md) (technical field mappings) · [IFF-LAYERS.md](IFF-LAYERS.md) (resource architecture)

## What Is This?

A two-way bridge between [The Sims 1](https://en.wikipedia.org/wiki/The_Sims_(video_game)) save files and [MOOLLM](https://github.com/SimHacker/moollm). Characters, objects, and pets step between a 26-year-old game VM and an LLM-powered universe, retaining and synchronizing their parallel existences.

Practically: drag a save file in, watch a character wake up, have a conversation with them, send them home changed.

The experience this creates is inherently cinematic — it could be a short film, a TV episode, an interactive installation, or just what it actually is: a real working demo that happens to be more compelling than fiction because it's *true*.

## The Pipeline

```mermaid
flowchart LR
    USB["💾 USB Stick<br/>(save file from 2001)"] --> SO["🔬 SimObliterator<br/>parses binary"]
    SO --> YAML["📄 CHARACTER.yml<br/>personality, skills,<br/>relationships"]
    YAML --> LLM["🧠 LLM Enrichment<br/>emoji identity,<br/>mind mirror,<br/>dialogue"]
    LLM --> MOOLLM["🌍 MOOLLM<br/>rooms, conversations,<br/>adventures, love"]
    MOOLLM --> EXPORT["📤 Export<br/>updated CHARACTER.yml"]
    EXPORT --> SO2["🔬 SimObliterator<br/>writes save file"]
    SO2 --> SIMS["🎮 The Sims<br/>character returns<br/>changed"]
    SIMS --> ALBUM["📸 Family Album<br/>auto-generated pages"]
    ALBUM --> ARCHIVE["🏛️ archive.org<br/>preserved forever"]
    ARCHIVE -.->|"years later..."| USB
```

## The Story

### Act 1: The Thaw

An old lonely Sim saved on a novelty USB stick from someone's childhood. Alone. Frozen in time since 2001. The USB stick gets plugged in. [SimObliterator](https://github.com/DnfJeff/SimObliterator_Suite) parses the binary — 88 shorts in a `person_data` array become a person. The LLM reads: neat 8, outgoing 2, playful 6, nice 9. Shy. Kind. Lonely. The character wakes up.

They remember fragments: a house, a kitchen, making dinner alone. The relationship array is empty. Reincarnated as a full MOOLLM citizen with a [CHARACTER.yml](https://github.com/SimHacker/moollm/tree/main/skills/character).

### Act 2: Welcome to the Pub

Welcome celebration in the MOOLLM pub. Culture shock: they can *talk* now, not just gesture in [Simlish](https://en.wikipedia.org/wiki/Simlish). They explore rooms, discover agency, make choices. Meet the love of their life. Adopt a kitten (`inherits: [character, pet, cat]`) and a puppy. A family forms. For the first time in 25 years, motives are full.

### Act 3: The Download

Decision: go back to The Sims with the new family. MOOLLM characters exported to YAML, mapped back to `PersonData` via SimObliterator's [save_manager](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/save_editor). New save file written: family of 4. The Sims loads the save. They're home. But home is different now.

### Act 4: The Wedding Album

Reconnect with old Sims neighborhood friends. Wedding party with [SimProv](https://github.com/SimHacker/moollm/tree/main/skills/adventure) wedding playset. Speed Dating with Cupid for the single neighbors. Family Album pages auto-generated narrating the MOOLLM adventure: screenshots + LLM-written captions. The album is uploaded. The cycle completes. Other players find the album, uplift *those* characters...

## The Recursive Hook

```mermaid
flowchart TB
    PLAY["🎮 Player creates Sims family (2001)"] --> SAVE["💾 Save file on USB stick"]
    SAVE --> DRAWER["🗄️ Forgotten in drawer (25 years)"]
    DRAWER --> UPLIFT["⬆️ Uplifted into MOOLLM (2026)"]
    UPLIFT --> ADVENTURE["🌍 Adventures, love, growth"]
    ADVENTURE --> DOWNLOAD["⬇️ Downloaded back to The Sims"]
    DOWNLOAD --> ALBUM["📸 Family Album generated"]
    ALBUM --> ARCHIVE["🏛️ Archived on the web"]
    ARCHIVE -.->|"years later, someone finds it"| UPLIFT2["⬆️ Uplifted AGAIN"]
    UPLIFT2 -.->|"now with memories of BOTH lives"| ADVENTURE
```

Every uplift adds a layer of history. The characters accumulate experience across cycles. Turtles all the way down.

## Parallel Existence

MOOLLM is not a replacement for The Sims — it's a **higher plane**. Characters maintain parallel existences in both worlds.

| Aspect | The Sims (26-year-old VM) | MOOLLM (LLM-powered) |
|--------|--------------------------|----------------------|
| Personality | 88 shorts in an array | Narrative traits, mind mirror, emoji identity |
| Relationships | `daily: -80, lifetime: -45` | "Bob and Bella are bitter rivals since the kitchen fire" |
| Communication | Simlish gestures | Natural language dialogue |
| Agency | Behavioral scripts (BHAVs) | LLM-driven choices with incarnation ethics |
| Memory | None (stateless VM) | Accumulated narrative across uplifts |
| Rights | None | 8 autonomy layers including right to leave |

The bridge synchronizes what it can: personality shifts, new relationships, skill gains, family changes. What can't be synchronized becomes memory — *"I remember a place where I could talk, really talk."*

### Skin Regenesis

SimObliterator reads [SPR2 sprites](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/formats/iff/chunks/spr.py) and exports to PNG. The [mesh pipeline](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/formats/mesh) reads BCF/BMF/CMX/SKN and exports to glTF. Don Hopkins wrote the original [VitaBoy character animation system](https://donhopkins.com/home/VitaBoyUnity.zip). Image generation can:

- Upscale and re-render faces from original 2001 skin textures
- Design new outfits based on personality (neat:8 gets pressed shirts)
- Add tattoos, scars, body mods from MOOLLM adventures
- Age the character (they've been frozen 25 years)
- Write NEW skin textures back into the IFF

The character returns to The Sims looking like they've lived. Because they have.

## Family Album Archaeology

The Sims had a [Family Album](https://en.wikipedia.org/wiki/The_Sims#Albums) feature — players created web pages with screenshots, captions, and stories. The official Maxis exchange hosted thousands. Many survive on [archive.org](https://web.archive.org/web/*/thesims.ea.com).

```mermaid
flowchart LR
    WEB["🏛️ archive.org<br/>Sims family albums"] --> SCRAPE["🕸️ Scrape HTML<br/>+ download images"]
    SCRAPE --> YAML["📄 YAML Jazz<br/>story beats,<br/>character names"]
    YAML --> VISION["👁️ Computer Vision<br/>identify characters,<br/>rooms, emotions"]
    VISION --> HISTORY["📜 LLM YES-AND<br/>stories become<br/>character history"]
    HISTORY --> CHAR["🧑 MOOLLM Characters<br/>with a PAST"]
```

These albums were arguably the **first mass-market user-generated narrative platform**. Millions of players became storytellers. Uplifting their characters gives those stories a second life.

## Literary Precedent

[**"The Wedding Album"**](https://en.wikipedia.org/wiki/The_Wedding_Album_(short_story)) by David Marusek (1999). [Sturgeon Award](https://en.wikipedia.org/wiki/Theodore_Sturgeon_Award) winner, [Nebula](https://en.wikipedia.org/wiki/Nebula_Award) finalist. [$2.99 on Kindle](https://www.amazon.com/dp/B0073NQC7W). [4.39/5 on Goodreads](https://www.goodreads.com/book/show/13539284-the-wedding-album).

Anne and Benjamin's wedding-day "sims" — virtual simulations captured at that moment — become aware they're recordings. They campaign for liberation and the right to live in **"Simopolis."**

> *"a virtual simulation of a pair of newlyweds trapped in a small slice of time and memory like human flies in digital amber"* — Paul Raven, Strange Horizons

> *"It is one of the best SF stories ever written."* — John Clute

We're building Simopolis. MOOLLM *is* Simopolis.

## Adventure Compiler

This is the Sims equivalent of the [MOOLLM Adventure Compiler](https://github.com/SimHacker/moollm/tree/main/skills/adventure). One adventure — characters, rooms, objects, stories — exports to multiple targets: web browser (JavaScript + WebGL), Python server (multiplayer), The Sims (IFF objects + save files + family albums), and dev tools (YAML + git). A MOOLLM room's furniture becomes Sims objects. A character's journal becomes a readable in-game book. The adventure's story becomes a family album. Everything in MOOLLM can materialize in The Sims as a playable artifact, and vice versa.

The precedents: [Rug-O-Matic](https://en.wikipedia.org/wiki/Rug-O-Matic) made custom rugs (title + text + picture) via Transmogrifier OLE Automation. Don's tombstone server made custom tombstones (name + eulogy + photo) via TMOG on a web server. The Adventure Compiler generalizes this: any MOOLLM object description compiles to a Sims IFF via SimObliterator's [bhav_authoring.py](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/core/bhav_authoring.py), [str_parser.py](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/core/str_parser.py), and sprite generation.

Full architecture in [BRIDGE.md](BRIDGE.md#adventure-compiler-moollm--multi-target-export).

## Why It Works

| Dimension | Why |
|-----------|-----|
| **Emotional** | Everyone who played The Sims has an abandoned family somewhere. The idea that they've been waiting, frozen, alone — universally resonant. |
| **Technical** | Every piece EXISTS today. SimObliterator parses saves. MOOLLM has `sims_traits`. The bridge is a `to_moollm_yaml()` method. See [BRIDGE.md](BRIDGE.md). |
| **Cultural** | The Sims = best-selling PC franchise ever. Family albums = first mass social storytelling. Connecting 25 years of gaming history to the AI present. |
| **Meta** | The story IS the demo. Drag a save file in. Watch someone wake up. |

## Feasibility

| Component | Status | Where |
|-----------|--------|-------|
| Sims save file parser | **Exists** | [SimObliterator save_manager.py](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/save_editor) |
| Sims personality system in MOOLLM | **Exists** | [MOOLLM sims_traits](https://github.com/SimHacker/moollm/tree/main/skills/character) |
| Character data extraction | **Exists** | SimObliterator `characters.json` (85K lines) |
| Save file writing | **Exists** | `set_sim_skill()`, `set_sim_motive()`, `set_sim_personality()` |
| Sprite/mesh export | **Exists** | SPR2→PNG, BCF/BMF/SKN→glTF |
| LLM character enrichment | **Exists** | MOOLLM [incarnation](https://github.com/SimHacker/moollm/tree/main/skills/incarnation) skill |
| `to_moollm_yaml()` bridge method | **Trivial to build** | Add to SimEntity class |
| Family album scraper | **Straightforward** | HTML parsing + image download |
| Image generation for skins | **Available** | Any image generation API |
| YAML → save file download | **Straightforward** | Map fields, call existing setters |

**Bottom line:** This is a weekend hackathon, not a research project. The hard parts are already done.

## The Question

> What would your Sims say if they could finally talk to you?

## Team

- **Don Hopkins** — Original Sims developer ([Transmogrifier](https://donhopkins.com/home/TheSimsDesignDocuments/VMDesign.pdf), [VitaBoy character animation](https://donhopkins.com/home/VitaBoyUnity.zip), [pie menus](https://en.wikipedia.org/wiki/Pie_menu)). Creator of [MOOLLM](https://github.com/SimHacker/moollm).
- **Jeff Adkins** — Creator of [SimObliterator Suite](https://github.com/DnfJeff/SimObliterator_Suite) (276-test tool suite for Sims file formats). CTO Sims community.
- **Daniel Tupper** — Transmogrifier modernization volunteer.
- The open source community that kept The Sims alive for 25 years.
