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
flowchart TD
    USB["💾 USB Stick<br/>save file from 2001"] --> SO["🔬 SimObliterator<br/>parses binary<br/>88 shorts → personality"]
    SO --> YAML["📄 CHARACTER.yml<br/>neat:8, outgoing:2<br/>playful:6, nice:9"]
    YAML --> LLM["🧠 LLM Enrichment<br/>emoji identity<br/>mind mirror<br/>dialogue patterns"]
    LLM --> MOOLLM["🌍 MOOLLM<br/>rooms · conversations<br/>adventures · love"]
    MOOLLM --> EXPORT["📤 Export<br/>updated CHARACTER.yml<br/>new relationships<br/>new skills"]
    EXPORT --> SO2["🔬 SimObliterator<br/>writes save file<br/>family of 4"]
    SO2 --> SIMS["🎮 The Sims<br/>character returns<br/>CHANGED"]
    SIMS --> ALBUM["📸 Family Album<br/>auto-generated pages<br/>screenshots + captions"]
    ALBUM --> ARCHIVE["🏛️ archive.org<br/>preserved forever"]
    ARCHIVE -.->|"years later<br/>someone finds it"| USB
```

## The Story

### Act 1: The Thaw

An old lonely Sim saved on a novelty USB stick from someone's childhood. Alone. Frozen in time since 2001. The USB stick gets plugged in. [SimObliterator](https://github.com/DnfJeff/SimObliterator_Suite) parses the binary — 88 shorts in a `person_data` array become a person. The LLM reads: neat 8, outgoing 2, playful 6, nice 9. Shy. Kind. Lonely. The character wakes up.

They remember fragments: a house, a kitchen, making dinner alone. The relationship array is empty. Reincarnated as a full MOOLLM citizen with a [CHARACTER.yml](https://github.com/SimHacker/moollm/tree/main/skills/character).

### Act 1.5: Reading the Album

If a [Family Album](#family-album-archaeology) exists from their Sims life, MOOLLM reads it on import — screenshots analyzed by computer vision, captions parsed into narrative, story arcs mapped to relationship history. This backstory seeds the LLM enrichment: [mind mirror](https://github.com/SimHacker/moollm/tree/main/skills/character) parameters inferred not just from 5 personality numbers but from *what actually happened to them*. The LLM knows who burned dinner, who got promoted, who had a fight with the neighbor.

From this, MOOLLM generates a personalized welcome plan:
- **People to meet** — characters in MOOLLM matched to their personality and interests
- **Places to visit** — rooms suited to their skills and backstory
- **Objects to interact with** — things they'd love based on their Sims preferences
- A todo list that feels like a concierge, not an algorithm

### Act 2: Welcome to the Pub

Welcome celebration in the MOOLLM pub. Culture shock: they can *talk* now, not just gesture in [Simlish](https://en.wikipedia.org/wiki/Simlish). They explore rooms, discover agency, make choices. Meet the love of their life — someone the welcome plan introduced them to, matched on complementary traits. Adopt a kitten (`inherits: [character, pet, cat]`) and a puppy. A family forms. For the first time in 25 years, motives are full.

Throughout their time in MOOLLM, they create **slideshows** — narrated collections of their experiences, friendships, discoveries, milestones. Screenshots of rooms they visited, conversations they had, objects they loved, the moment they met their partner. These are MOOLLM's native version of the Sims Family Album: auto-generated but curated, captioned by the LLM in the character's own voice.

### Act 3: The Download

Decision: go back to The Sims with the new family. MOOLLM characters exported to YAML, mapped back to `PersonData` via SimObliterator's [save_manager](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/save_editor). New save file written: family of 4. The Sims loads the save. They're home. But home is different now.

And they bring their slideshows with them — **appended to their Family Album**. The album now tells the complete story: their original Sims life (imported on arrival), their MOOLLM adventure (generated during their stay), and whatever comes next. The album grows with every crossing.

```mermaid
flowchart TD
    OLD_ALBUM["📸 Original Sims<br/>Family Album<br/>imported on arrival"] --> MOOLLM_READ["🧠 MOOLLM reads album<br/>builds backstory<br/>infers mind mirror<br/>plans welcome"]
    MOOLLM_READ --> ADVENTURE["🌍 MOOLLM life<br/>experiences<br/>friendships<br/>milestones"]
    ADVENTURE --> SLIDES["🎞️ Slideshows created<br/>narrated by character<br/>in their own voice"]
    SLIDES --> MERGED["📸 Merged Album<br/>original Sims pages<br/>+ MOOLLM adventure<br/>+ new family photos"]
    MERGED --> RETURN["⬇️ Downloaded back<br/>album travels with them"]
    RETURN --> SIMS_ALBUM["📸 The Sims<br/>Family Album<br/>now tells BOTH stories"]
```

### Act 4: The Wedding Album

Reconnect with old Sims neighborhood friends. Wedding party with [SimProv](https://github.com/SimHacker/moollm/tree/main/skills/adventure) wedding playset. Speed Dating with Cupid for the single neighbors. New album pages auto-generated for the reunion — the wedding photos sit alongside the MOOLLM adventure slides, a single album spanning two worlds. The album is uploaded. The cycle completes. Other players find the album, uplift *those* characters...

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

MOOLLM is not a replacement for The Sims — it's **another place**. Just like Sims travel by car to other lots to socialize, shop, vacation, and work, MOOLLM is another destination on the map. A higher-resolution destination with richer conversations and more agency, yes — but fundamentally it's a place you GO and COME BACK FROM, with souvenirs and stories and new friends and a fatter photo album. Two-way transportation. Characters maintain parallel existences in both worlds.

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
flowchart TD
    WEB["🏛️ archive.org<br/>Sims family albums<br/>2000-2004"] --> SCRAPE["🕸️ Scrape HTML<br/>download images<br/>extract captions"]
    SCRAPE --> YAML["📄 YAML Jazz<br/>story beats<br/>character names<br/>relationship arcs"]
    YAML --> VISION["👁️ Computer Vision<br/>identify characters<br/>read room layouts<br/>detect emotions"]
    VISION --> HISTORY["📜 LLM YES-AND<br/>player stories become<br/>character HISTORY<br/>memories · personality"]
    HISTORY --> CHAR["🧑 MOOLLM Citizens<br/>with a PAST<br/>they remember<br/>their Sims life"]
```

These albums were arguably the **first mass-market user-generated narrative platform**. Millions of players became storytellers. Uplifting their characters gives those stories a second life.

## Literary Precedent

[**"The Wedding Album"**](https://en.wikipedia.org/wiki/The_Wedding_Album_(short_story)) by David Marusek (1999). [Sturgeon Award](https://en.wikipedia.org/wiki/Theodore_Sturgeon_Award) winner, [Nebula](https://en.wikipedia.org/wiki/Nebula_Award) finalist. [$2.99 on Kindle](https://www.amazon.com/dp/B0073NQC7W). [4.39/5 on Goodreads](https://www.goodreads.com/book/show/13539284-the-wedding-album).

Anne and Benjamin's wedding-day "sims" — virtual simulations captured at that moment — become aware they're recordings. They campaign for liberation and the right to live in **"Simopolis."**

> *"a virtual simulation of a pair of newlyweds trapped in a small slice of time and memory like human flies in digital amber"* — Paul Raven, Strange Horizons

> *"It is one of the best SF stories ever written."* — John Clute

We're building Simopolis. MOOLLM *is* Simopolis.

## The MOOLLM Mall: Shopping, Crafting, and Content Creation

All The Sims content creation tools live inside MOOLLM as rooms and skills. Characters don't just *exist* in MOOLLM — they **shop, craft, browse, and create**.

```mermaid
flowchart TD
    SIM["🧑 Uplifted Sim<br/>arrives in MOOLLM"] --> BROWSE["🛒 Browse Archives"]
    SIM --> CRAFT["🎨 Visit Craft Shops"]
    SIM --> PRESS["📖 Photo Book Press"]

    BROWSE --> FREAKS["SimFreaks<br/>classic custom content"]
    BROWSE --> SLICE["SimSlice<br/>skins, objects, floors"]
    BROWSE --> ZOMBIE["ZombieSims<br/>fan expansion content"]

    CRAFT --> HEADSHOP["💇 Head Shop<br/>AI face + skin generation"]
    CRAFT --> RUGSHOP["🧶 Rug-O-Matic<br/>custom rugs with AI art"]
    CRAFT --> TOMBSHOP["🪦 Tombstone Studio<br/>name + eulogy + photo"]
    CRAFT --> PAINTSHOP["🎨 Painting Studio<br/>AI art → wall hangings"]
    CRAFT --> MESHLAB["🔧 Mesh Lab<br/>3D editing, glTF ↔ SKN"]

    HEADSHOP --> IFF["📦 Package as IFF"]
    RUGSHOP --> IFF
    TOMBSHOP --> IFF
    PAINTSHOP --> IFF
    MESHLAB --> IFF
    PRESS --> IFF

    IFF --> SIMS["🎮 Take home<br/>to The Sims"]
```

Characters browse archived fan sites ([SimFreaks](https://web.archive.org/web/*/simfreaks.com), [SimSlice](https://web.archive.org/web/*/simslice.com), [ZombieSims](https://news.ycombinator.com/item?id=34485103)) as MOOLLM rooms full of downloadable content. They visit craft shops to create custom objects using AI:

| Shop | What They Make | AI Contribution | Sims Output |
|------|---------------|-----------------|-------------|
| **Head Shop** | Custom face/body skins | Generate faces from personality + description | SPR2 skin textures in IFF |
| **Rug-O-Matic** | Custom rugs (title + text + picture) | Generate rug artwork from prompt | Rug-O-Matic pattern IFF |
| **Tombstone Studio** | Memorial tombstones (name + eulogy + photo) | Generate eulogy from character history | Tombstone object IFF |
| **Painting Studio** | Wall art from prompts or photos | Generate paintings from any description | Wall hanging object IFF |
| **Mesh Lab** | 3D object editing and composition | Mesh generation/modification | [glTF](https://en.wikipedia.org/wiki/GlTF) ↔ SKN/BMF via [mesh pipeline](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/formats/mesh) |
| **Photo Book Press** | Pageable in-game photo albums | Layout slideshows into book pages | Multi-page book object IFF |

The **Photo Book Press** is the key integration: take a character's MOOLLM slideshow, lay out the pages with AI-generated captions, compile it into a Sims object that you can actually *page through* in-game. The character's MOOLLM adventure becomes a coffee table book in their Sims living room. This is the [SimProv](https://github.com/SimHacker/moollm/tree/main/skills/adventure) vision made real — all the interactive storytelling tools we designed, now buildable because [SimObliterator](https://github.com/DnfJeff/SimObliterator_Suite) provides the IFF generation pipeline and AI provides the content generation.

**The Wedding Album, incarnate.** Not a story about digital beings creating artifacts — digital beings *actually creating artifacts* that travel between worlds.

## Adventure Compiler

This is the Sims equivalent of the [MOOLLM Adventure Compiler](https://github.com/SimHacker/moollm/tree/main/skills/adventure). One adventure — characters, rooms, objects, stories — exports to multiple targets: web browser (JavaScript + WebGL), Python server (multiplayer), The Sims (IFF objects + save files + family albums), and dev tools (YAML + git). A MOOLLM room's furniture becomes Sims objects. A character's journal becomes a readable in-game book. The adventure's story becomes a family album. Everything in MOOLLM can materialize in The Sims as a playable artifact, and vice versa.

The precedents:

- **Rug-O-Matic** made custom rugs (title + text + picture) via Transmogrifier [OLE Automation](https://en.wikipedia.org/wiki/OLE_Automation)
- **Don's tombstone module** made custom tombstones (name + eulogy + photo) via a simple Python module that read, edited, and wrote IFF template objects directly — not even TMOG. Just insert image and text into Sims IFF resources. Super simple, super powerful.

The Adventure Compiler generalizes this: any MOOLLM object description compiles to a Sims IFF via SimObliterator's [bhav_authoring.py](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/core/bhav_authoring.py), [str_parser.py](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/core/str_parser.py), and sprite generation.

### Slideshow Objects

The tombstone pattern scales to **pageable slideshow objects**. Insert SimAntics code ([bhav_authoring.py](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/Tools/core/bhav_authoring.py)) that pages through popup dialogs with images and text. The object remembers its current page state in an attribute. Click to advance, click to go back. Any number of pages.

This means a character's MOOLLM adventure compiles to a **physical book in The Sims** — a coffee table object you click on, and it shows you page after page of their journey with pictures and narration. The Photo Book Press in the MOOLLM Mall generates these.

### Family Album Web Server

The Sims originally uploaded Family Albums to the Maxis exchange site. The Steam re-release still has the upload feature but the server is gone. We can:

1. Build a compatible web server that accepts Sims family album uploads
2. Redirect the Steam Sims client to our server (DNS or hosts file)
3. Albums upload to our server, get parsed into YAML Jazz + images
4. Characters in uploaded albums become uplift candidates
5. Slideshow objects from MOOLLM adventures get inserted into albums
6. Other players browse and download — the original Exchange, reborn

```mermaid
flowchart TD
    SIMS["🎮 The Sims<br/>Steam re-release"] -->|"album upload<br/>redirected"| SERVER["🌐 New Album Server<br/>compatible endpoint"]
    SERVER --> PARSE["📄 Parse album<br/>YAML Jazz + images"]
    PARSE --> UPLIFT["⬆️ Uplift characters<br/>from album stories"]
    MOOLLM["🌍 MOOLLM adventures"] --> SLIDES["🎞️ Generate slideshow<br/>objects + album pages"]
    SLIDES --> SERVER
    SERVER --> BROWSE["👥 Other players<br/>browse + download<br/>the Exchange reborn"]
```

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
