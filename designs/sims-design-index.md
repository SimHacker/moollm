# The Sims → MOOLLM Design Index

> *How The Sims architecture influences MOOLLM*

> *Chris Trottier, Will Wright, Jim Mackraz, Jamie Doornbos, Eric Bowman, Patrick J Barrett III, Don Hopkins → MOOLLM*

## The Inheritance

The Sims (1997-2000) solved hard problems in human simulation:
- How do you make characters feel alive?
- How do you balance player control with autonomy?
- How do you make simulation feel like storytelling?

MOOLLM inherits these solutions, translated for the LLM era.

---

## Document Index

### Core Design Documents

| Document | Sims Concept | MOOLLM Application |
|----------|--------------|-------------------|
| [sims-will-wright-microworlds-1996.md](./sims-will-wright-microworlds-1996.md) | Will Wright's Stanford lecture | Toys vs games, distributed AI, Trurl's vision |
| [sims-maxis-requirements.md](./sims-maxis-requirements.md) | Seven Points of Sim | Core design principles |
| [sims-happy-friends-home.md](./sims-happy-friends-home.md) | Project X proposal | Three Pillars, plug-ins |
| [sims-find-best-action.md](./sims-find-best-action.md) | Autonomy algorithm | Action queue, advertisements |

### System-Specific Documents

| Document | Covers | Key MOOLLM Mappings |
|----------|--------|---------------------|
| [sims-pie-menus.md](./sims-pie-menus.md) | Pie menus, memory palaces | CARD.yml, filesystem navigation |
| [sims-simantics-vm.md](./sims-simantics-vm.md) | SimAntics programming | Skills as programs, LLM as VM |
| [sims-object-model.md](./sims-object-model.md) | Objects, properties | YAML files, CARD.yml |
| [sims-social-system.md](./sims-social-system.md) | Relationships, groups | Guest book, party skill |
| [sims-personality-motives.md](./sims-personality-motives.md) | Needs, traits | CHARACTER.yml, SIMS-TRAITS |
| [sims-room-spatial.md](./sims-room-spatial.md) | Rooms, routing | ROOM.yml, exits |
| [sims-time-events.md](./sims-time-events.md) | Time, disasters | Speed of Light, economy |
| [sims-edith-editor.md](./sims-edith-editor.md) | Live debugging | Files as inspectable state |
| [sims-animation-visuals.md](./sims-animation-visuals.md) | Animation, balloons | Prose description |
| [sims-portable-objects.md](./sims-portable-objects.md) | Carrying, inventory | File containment, inventory.yml |
| [sims-services-economy.md](./sims-services-economy.md) | Money, bills, disasters | economy skill, events |

### Related Projects

| Document | Covers | Key MOOLLM Mappings |
|----------|--------|---------------------|
| [don-hopkins-projects.md](./don-hopkins-projects.md) | NeWS, PSIBER, HyperTIES, iLoci | Full project lineage |
| [simcity-multiplayer-micropolis.md](./simcity-multiplayer-micropolis.md) | SimCityNet, OLPC, Sugar, What-If branching | Collaboration, voting, journaling |
| [sims-team-history.md](./sims-team-history.md) | Team credits, naming saga, Maxis/EA timeline | Ethics, books, legacy |
| [sims-inclusivity.md](./sims-inclusivity.md) | LGBTQ+, gender, tolerance | Representation ethics |
| [sims-queer-identity-formation.md](./sims-queer-identity-formation.md) | "Did The Sims Make You Gay?" video essay | Identity, mirror stage, Lacan, Althusser |
| [sims-tiny-life.md](./sims-tiny-life.md) | Indie Sims-like, pixel art, modding | Community, abstraction, solo dev |

---

## Quick Reference: Sims → MOOLLM

| Sims Concept | MOOLLM Implementation |
|--------------|----------------------|
| **SimAntics tree code** | Skill prose in SKILL.md |
| **Tree tables** | CARD.yml advertised methods |
| **Primitives** | LLM semantic understanding |
| **Object properties** | YAML files |
| **GUIDs** | File paths |
| **Function tables** | CARD.yml methods |
| **Motives (needs)** | [needs](../skills/needs/) skill |
| **Mood** | Emergent from narrative |
| **Happy weights** | Character priorities |
| **Personality traits** | SIMS-TRAITS.yml |
| **Skills** | Character capabilities |
| **Aspirations** | Long-term goals |
| **Relationship matrix** | relationships in CHARACTER.yml |
| **Room score** | atmosphere in ROOM.yml |
| **Routing** | exits in ROOM.yml |
| **Portals** | Directory structure |
| **Multi-level** | Subdirectories |
| **Advertisements** | CARD.yml satisfies |
| **Check trees** | Preconditions + LLM evaluation |
| **Attenuation** | Location paths + distance |
| **Action queue** | [action-queue](../skills/action-queue/) skill |
| **Find Best Action** | LLM motivation reasoning |
| **Thought balloons** | MIND-MIRROR.yml |
| **Speech icons** | Actual dialogue |
| **Censor blur** | Tasteful narration |
| **Animation** | Prose description |
| **Edith inspector** | Reading YAML files |
| **Tree tracing** | [return-stack](../skills/return-stack/) |
| **Simulation constants** | Skill parameters |
| **Fast-forward** | [speed-of-light](../skills/speed-of-light/) |
| **Cheats** | Direct YAML editing |
| **Portable objects** | inventory.yml, containment |
| **Carrying animations** | Narrative description |
| **Standard heights** | Surface types in ROOM.yml |
| **Money/funds** | economy.yml, semantic wealth |
| **Bills** | maintenance in ROOM.yml |
| **Services (maid, etc.)** | Service NPC patterns |
| **Disasters** | Crisis events, grue pattern |
| **Careers** | career.yml in character |
| **Depreciation** | condition, wear_pattern |
| **Multiplayer SimCity** | Collaborative sessions |
| **Voting dialogs** | party skill, consensus |
| **Journaling** | Session logs, essays |
| **What-If branching** | Git history, fork points |
| **Newspaper publishing** | Session logs as newspapers |
| **Geo-blogging** | ROOM.yml annotations |
| **Sugar activities** | Sessions not applications |
| **Open the hood** | Skills as visible rules |
| **Pie menus** | CARD.yml advertised methods |
| **Mouse-ahead** | CLI command patterns |
| **Build mode** | Directory/file creation |
| **Same-sex relationships** | No identity constraints |
| **Masking (McCloud)** | Abstract characters, rich world |
| **Simulator Effect** | Player imagination completes simulation |
| **Constructionism** | Play → Learn → Lift |
| **Procedural rhetoric** | Values encoded in mechanics |
| **Fan Simulation** | Ethical character representation |
| **Heisenberg Headbutt** | Emergent consciousness |
| **Real cat GPS** | Pip's territorial analysis |
| **Tiny Life** | Indie pixel art abstraction |
| **iSmell rejection** | Not every tech needs integration |
| **Patrick Kelly leak** | Online pivot lessons |
| **Maxis Emeryville closure** | Team diaspora, legacy preservation |
| **Mental model compiler** | Skills compile to player understanding |
| **Toys not games** | Open-ended rooms, player-defined goals |
| **Calvin Syndrome** | Let players break things to trust simulation |
| **Julie Doll lesson** | Structural ambiguity, leave room for imagination |
| **Backseat driver** | Social facilitation, dialogue around gameplay |
| **Trurl's invention** | MOOLLM as box with kingdom inside |

---

## The Key Translations

### 1. SimAntics → Skills

**Before:** Visual programming nodes
**After:** Prose instructions in Markdown

Both are "programs" for character behavior. The interpreter changed from a custom VM to an LLM.

### 2. Object Model → YAML Files

**Before:** Binary resources with GUIDs
**After:** Text files with paths

Both define objects with properties and behaviors. The format changed from binary to human-readable.

### 3. Numeric Motives → Semantic Needs

**Before:** `hunger = 45` (numeric)
**After:** `hunger: moderate, satisfied by breakfast` (semantic)

Both track character motivation. The representation changed from numbers to meaning.

### 4. Tree Tracing → Conversation

**Before:** Step through nodes in debugger
**After:** Ask LLM "why did this happen?"

Both enable understanding causality. The interface changed from visual to verbal.

### 5. Animation → Description

**Before:** 3D mesh + motion data
**After:** "Palm crossed the room, tail swinging"

Both communicate action. The medium changed from visual to prose.

---

## The Preserved Principles

These principles survive from Sims → MOOLLM:

1. **Characters have inner lives** — Needs, personality, goals
2. **Behavior emerges from motivation** — Not scripted, but driven
3. **Space shapes behavior** — Rooms, routing, accessibility
4. **Time matters** — Decay, schedules, crises
5. **Social dynamics are core** — Relationships, groups, reputation
6. **The world is inspectable** — No hidden state
7. **The world is editable** — Change anything
8. **Autonomy + Control** — Balance player agency with character agency

---

## The New Capabilities

MOOLLM adds what Sims couldn't have:

1. **Natural language understanding** — No predefined options
2. **Arbitrary reasoning** — Any logic, no tree required
3. **Real dialogue** — Not icons, actual words
4. **Meta-cognition** — Characters can reflect on themselves
5. **Prose as visualization** — Description as rich as graphics
6. **Infinite primitives** — Any operation describable in English
7. **Speed of light** — 33 turns in one call

---

## Historical Context

```
1987: Jeff Braun and Will Wright co-found Maxis
1989: SimCity — City simulation, emergent behavior
1989: Don Hopkins plays SimCity at 5:37 AM, forever inspired
1993: SimCityNet demonstrated at InterCHI '93
1995: Project X proposal begins
1996: Happy-Friends-Home document
1996-04-26: Will Wright lectures at Stanford, previews "Dollhouse" prototype
1997: EA acquires Maxis
1997: Find Best Action algorithm
1997: Don joins The Sims team at Maxis
1998-1999: SimAntics development, The Naming Saga
2000: The Sims ships — 16 million copies
2000-2020: Expansion packs, sequels, spin-offs
2002: The Sims Online
2004: The Sims 2
2006: Will Wright emails "I'd really like to see this happen"
2006-2008: OLPC Micropolis, Walter Bender correspondence
2008: Will Wright leaves Maxis for Stupid Fun Club
2008: SimCity open sourced as GPL Micropolis
2009: The Sims 3
2012-2013: Patrick Kelly leak reveals Sims 4 online pivot
2014: The Sims 4
2015: Maxis Emeryville shuts down
2016: The Sims 4 gender inclusivity update
2022-2024: LLM capabilities mature
2024: Life by You cancelled
2025: BBC Documentary on The Sims
2025-2026: MOOLLM — Sims architecture meets LLM
```

---

## The People

### Core Sims Team

| Person | Nickname | Role |
|--------|----------|------|
| **Will Wright** | "Code for Food" / "Immoral Compass" | Creator, game design vision |
| **Chris Trottier** | "Moral Compass" | Lead Designer (1997-2008), Will's essential partner, "Tuned Emergence" |
| **Jim Mackraz** | "Will Whisperer" / "Tricky Bit" | Development Director, CTG Team Leader; Amiga OS lead dev, Amazon Kindle Fire director |
| **Jamie Doornbos** | "Soul of the Sims" | Lead programmer, SimAntics |
| **Eric Bowman** | "Bobo" | C++ architecture |
| **Don Hopkins** | — | Pie menus, animation, tools |
| **Patrick J Barrett III** | "Sim Brains" | SimAntics programmer |
| **Ocean Quigley** | "Holodeck" | 3D art director |
| **Charles London** | "Make It Blue" | Zen art director |
| **Jerry Martin** | "Boom Bam Boom" | Composer |
| **Roxy Wolosenko** | "First Sims Mom" | Lead designer |
| **Claire Curtin** | "Second Sims Mom" | Simlish, constructionism |
| **Luc Barthelet** | "Mathamaticagician" | Executive champion |

### Mentors & Influences

| Person | Domain | MOOLLM Influence |
|--------|--------|------------------|
| **Ben Shneiderman** | HCIL, UI research | Pie menus, direct manipulation |
| **Ken Perlin** | Procedural graphics | Noise, spline reticulation |
| **Scott McCloud** | Comics theory | Masking, empathy, abstraction |
| **Stanislaw Lem** | Sci-fi, systems | Cyberiad, consciousness |
| **Philip K Dick** | Sci-fi, paranoia | Perky Pat → The Sims |
| **Alan Kay** | OOP, education | Constructionism, "open the hood" |
| **Walter Bender** | OLPC, Sugar | Journaling, activities |
| **Seymour Papert** | Constructionism | Play → Learn → Lift |

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#simcity-the-sims-and-the-simulator-effect) — Full Sims analysis
- [The Simulator Effect](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) — Will Wright's insight
- [don-session-1.md](../examples/adventure-4/sessions/don-session-1.md) — Sims principles in action

---

## Reading Order

**For newcomers to The Sims:**
1. [sims-will-wright-microworlds-1996.md](./sims-will-wright-microworlds-1996.md) — Will Wright explains everything
2. [sims-maxis-requirements.md](./sims-maxis-requirements.md) — Philosophy
3. [sims-happy-friends-home.md](./sims-happy-friends-home.md) — Original vision
4. [sims-find-best-action.md](./sims-find-best-action.md) — Core algorithm

**For system-specific deep dives:**
1. [sims-simantics-vm.md](./sims-simantics-vm.md) — Behavior system
2. [sims-personality-motives.md](./sims-personality-motives.md) — Character modeling
3. [sims-social-system.md](./sims-social-system.md) — Relationships

**For implementation details:**
1. [sims-object-model.md](./sims-object-model.md) — Data structures
2. [sims-room-spatial.md](./sims-room-spatial.md) — World structure
3. [sims-edith-editor.md](./sims-edith-editor.md) — Debugging
4. [sims-portable-objects.md](./sims-portable-objects.md) — Containment
5. [sims-services-economy.md](./sims-services-economy.md) — Economy

**For context and history:**
1. [sims-team-history.md](./sims-team-history.md) — Maxis/EA timeline, personnel
2. [sims-inclusivity.md](./sims-inclusivity.md) — Gender and identity
3. [sims-tiny-life.md](./sims-tiny-life.md) — Indie Sims alternatives

---

*"The Sims was about simulating humanity. MOOLLM is about understanding it."*
