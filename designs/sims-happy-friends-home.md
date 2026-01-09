# Happy-Friends-Home: The Sims Origin Story

> *"Somebody has to get this sorry excuse for a family into shape. That's where you come in."*
> — Project X Initial Proposal, October 2, 1996

---

## Summary

"Happy-Friends-Home" was the working title for what became The Sims — the best-selling PC game of all time. This document comprehensively summarizes the October 1996 Project X proposal by Jamie Doornbos (JDM) and Will Wright (WW), revealing the original vision and how MOOLLM inherits and extends its core principles.

---

## Document Details

- **Title:** Happy-Friends-Home
- **Project:** Project X Initial Proposal
- **Authors:** JDM (Jamie Doornbos), WW (Will Wright)
- **Handwritten Notes:** DH (Don Hopkins)
- **Revision:** 3
- **Date:** October 2, 1996
- **Printed:** January 20, 1997
- **Classification:** Maxis Confidential (historical)

---

## Table of Contents

1. [What Do You See?](#1-what-do-you-see)
2. [What Do You Do?](#2-what-do-you-do)
3. [What Is the Point?](#3-what-is-the-point)
4. [Why Is It Good?](#4-why-is-it-good)
5. [Leverage Our Success](#5-leverage-our-success)
6. [What Will It Take?](#6-what-will-it-take)
7. [Don Hopkins' Marginalia](#don-hopkins-handwritten-marginalia)
8. [MOOLLM Design Inheritance](#moollm-design-inheritance)

---

## 1. What Do You See?

> *"You start the game by selecting a home and family from several stock choices or custom options. The entire game takes place in the house and yard of the home."*

### The Visual Design

- **Roofless cut-away view** — see inside the house
- **Tile/grid-based** house and furnishings
- **Viewpoint and objects rotate in 90-degree increments**
- Characters are **"surprisingly lifelike"** — they wander about, play with gadgets, sit on furniture, and eat donuts
- **"They appear a little lazy"** — the default state

### The Living World

> *"People come to the door of the house. If somebody answers it, there might be a brief 'conversation,' or maybe they'll come on in and sit down. Time passes, people come by; not a lot gets done."*

The autonomous behavior creates a living world even without player intervention:

- Visitors arrive and knock
- Brief conversations at the door
- Visitors come in and sit down
- Time passes naturally
- **"When they run out of donuts, somebody might go over to the phone and order a pizza, which is delivered immediately."**

### MOOLLM Parallel: The Lazy Default

The "lazy" default behavior is **brilliant design** that MOOLLM inherits:

| Sims Concept | MOOLLM Implementation |
|--------------|----------------------|
| Lazy characters waiting for direction | Characters exist in rooms, waiting for player prompts |
| Roofless cut-away view | Room descriptions provide narrative "view" into spaces |
| Tile-grid world | Directory/file hierarchy as world structure |
| Objects in grid | YAML files as objects with properties |
| Characters wander and interact | NPCs have autonomous behaviors defined in their files |
| Visitors come to door | Characters can enter rooms, triggering interactions |
| Order pizza when hungry | [`needs`](../skills/needs/) skill triggers actions when needs are low |

The [`room`](../skills/room/) skill defines spaces. The [`character`](../skills/character/) skill defines inhabitants. They exist and can be observed even without active gameplay.

---

## 2. What Do You Do?

> *"Somebody has to get this sorry excuse for a family into shape. That's where you come in."*

### Direct Control

> *"You can directly control each family member in turn (but not the visitors)."*

The player **inhabits** characters:

- **Click-and-go:** Move characters by clicking destinations
- **Object interaction:** Click on a gadget like the TV, character walks over and turns it on
- **Fire-and-forget:** "Then he'll probably watch for a while, at least until he gets hungry or bored"
- **You're not helping much yet** — initially, you just observe

### Multi-Character Orchestration

> *"You can get all of your family members doing something productive at the same time."*

**Parallel coordination:**
- Send some into the bathroom
- Another cooks breakfast
- Another fetches the paper
- **Catalog shopping** — buy through computer or catalog
- **Start conversations** with visitors — ask them to do things, or "just talk about sports"
- **Introduce friends** to each other

### Long-Term Activities

> *"Over the long term, you keep up with the maintenance chores, go on outings (school, work, job interviews, shopping, visiting), start projects, practice the guitar, play cards, and throw parties."*

**Time management features:**
- **Daily routines and weekly chores** — "relieve yourself of the repetitiveness"
- **Fast-forward time** — "zip through the sleeping hours, or when the house is vacant"
- **Content with routine** — fast-forward when everyone's on schedule or behaving naturally

### MOOLLM Parallel: Command and Control

| Sims Interaction | MOOLLM Implementation |
|------------------|----------------------|
| Direct control of family members | Player issues commands to characters |
| Click-and-go navigation | Room navigation commands |
| Fire-and-forget activities | [`action-queue`](../skills/action-queue/) skill handles ongoing actions |
| Multi-character coordination | Issue commands to multiple NPCs |
| Catalog shopping | Object acquisition, economy interactions |
| Daily routines | Character schedules in YAML files |
| Fast-forward time | [`time`](../skills/time/) skill with acceleration |
| Conversation starters | Dialogue templates, [`empathic-expressions`](../skills/empathic-expressions/) |

The **speed of light pattern** in MOOLLM is the ultimate "fast-forward" — simulating entire scenes in a single LLM call.

---

## 3. What Is the Point?

> *"Beyond the behaviors described above, the entire household is running under a complex simulation. How you manage your family determines how successful you're going to be and whether you're going to be able to afford a grand home and throw killer parties."*

### The Three Pillars of Value

| Pillar | Description | Cost | Trade-off |
|--------|-------------|------|-----------|
| **Home** | House and material belongings | Money to buy, effort to maintain | *"He who dies with the most toys wins."* — but bigger house = more chores |
| **Friends** | Relationships with family and outsiders | Time investment | *"Maybe they'll do you a favor when you need one. And nobody likes to party alone."* |
| **Happiness** | Free time, low stress, education, enrichment, creativity, hobbies | Intangible but scored | The real measure of success |

### The Balance Requirement

> *"The simulation will be tuned so that you must make balanced progress on all three pillars to really get ahead. Any lagging factor will tend to hold back the others."*

**Trade-offs and synergies:**
- Most activities trade one value for another
- Strong pillars can **"hoist up"** weak ones
- *"One of your good friends gives you a great tip about a job opportunity"*

### Short-Term vs. Long-Term

| Short-Term | Long-Term |
|------------|-----------|
| Toys that depreciate fast | Remodeling that appreciates |
| Superficial friends you bribe with gifts | Long-term relationships |
| Eating chocolate | Being thin and fit |

### MOOLLM Parallel: Multi-Dimensional Needs

| Sims Pillar | MOOLLM Skill | Function |
|-------------|--------------|----------|
| Home | [`economy`](../skills/economy/) | Track resources, possessions, home value |
| Friends | [`party`](../skills/party/), social tracking | Relationship graphs, favors, social debt |
| Happiness | [`needs`](../skills/needs/) | Comfort, fun, hygiene, social, energy |
| Balance | [`scoring`](../skills/scoring/) | Holistic evaluation, weighted priorities |
| Trade-offs | [`reward`](../skills/reward/) | Action consequences, opportunity costs |

The **Three Pillars** concept directly influenced MOOLLM's multi-dimensional needs system. Characters in MOOLLM aren't optimizing a single score — they're balancing competing goods.

---

## 4. Why Is It Good?

### "Why Do I Care?"

> *"You identify with your family, their happiness is in your hands, and you live vicariously through them."*

**Player choices:**
- **Mimic your real-world family** — or build your dream house with any housemates
- **See if you can attain the "better things in life"**

**MOOLLM Parallel:** Character creation with meaningful personality traits. The [`persona`](../skills/persona/) skill lets players define who their characters are. The [`character`](../skills/character/) skill provides the template.

### Direct Control

> *"You can 'inhabit the body' of any family member; your influence over outsiders and the objects in your house is through them."*

**Fire-and-forget interactions:**
- Click on object → character walks over and starts activity
- Start activities for multiple family members simultaneously
- **"Watch them all do your bidding at once"**

**MOOLLM Parallel:** Switching between character perspectives. Issuing commands through NPCs. The player's will flows through the characters they control.

### Open-Ended

> *"Ultimately, you decide what your goals are, and when they are accomplished."*

**Scoring without winning:**
- Measurable "scores" like net worth and "happiness quotient"
- **But you decide what kind of life your family has**
- **Almost completely open-ended** architecture
- Extreme flexibility in furnishing
- *"You'll find that some designs work better than others"* — emergent discovery
- *"Some friends are more helpful than others"*

**MOOLLM Parallel:** No prescribed win conditions. The [`adventure`](../skills/adventure/) skill provides structure, but players define their own objectives. Emergent gameplay from skill interactions.

### Accessible

> *"Right out of the box, you can pick a canned house and family, and sit back and watch them wander around, doing what they please."*

**Accessibility layers:**

| Level | Activity | Engagement |
|-------|----------|------------|
| **1. Passive** | Watch characters wander | Observe |
| **2. Toy mode** | Buy stuff, plop it down | *"See if the little buggers go interact with it. You might want to start with donuts."* |
| **3. Architectural** | Remodel without controlling characters | Build/design |
| **4. Direct control** | Control characters, easy to learn | Command |
| **5. Make-believe** | *"Make-believe what the characters are saying"* | Imagine |

**MOOLLM Parallel:** Multiple engagement levels. The [`visualizer`](../skills/visualizer/) skill lets you observe. Commands let you interact. Creative building through file editing.

### Long-Term Play

> *"There are a vast number of starting conditions; choices of homes, of family members, and of combinations of these."*

**Different success scenarios:**
- Rich, stressed yuppies
- Scholarly fine artists
- **"Living with your band in a wanton party house"**
- Each requires different approach to making money, friends, and living well

**MOOLLM Parallel:** Different room configurations, character mixes, and skill loadouts create unique experiences. The [`world-generation`](../skills/world-generation/) skill creates varied starting conditions.

### Broad Appeal

> *"One obvious goal is to 'make my people happy.' This is considered to be a strong appeal factor for girls and women."*

**Appeal spectrum:**

| Audience | Appeal | Style |
|----------|--------|-------|
| Soft/casual | *"Erector Set" or "Doll House"* | Fun without engaging the Sim |
| Young players | Spectrum of play as skills advance | Progressive complexity |
| Hard-core | Strategic fast-forward requires good routines | Optimization |
| Eye candy seekers | *"Lots of eye candy, especially in the party scenes"* | Visual spectacle |
| Social | *"Everybody likes an aquarium"* | Shared experience |

**The Insane Asylum Scenario:**

> *"Try one [aquarium] full of lunatics. Simulate the movie 'Queen of Hearts' in which an insane asylum's lunatics break out and inhabit an abandoned hotel."*

**MOOLLM Parallel:** MOOLLM welcomes all play styles. Narrative exploration, mechanical optimization, creative building, social play.

---

## 5. Leverage Our Success

> *"Project X was designed from day zero to leverage its success in the market, and it has stayed true to the SimWorld concept."*

### Extensibility

> *"Already, plug-in furnishings and gadgets are supported, containing their own graphics and interactive behaviors, and their effects on the Sim."*

**Extension strategy:**
- **Freebies** to extend the game — "website bait"
- **Incremental enhancements** extend product lifespan
- **Sequels and variations** by reusing the engine — *"A SimTribe idea has been suggested"*
- **Character appeal** extends beyond the game — *"If we're good, we can make the market appeal of some of these characters extend well beyond the game"*

### Online Features (Prescient in 1996!)

> *"The home computer prop can connect to our Web site. In fact, when you 'shop' via the computer, you can be selecting add-ins from the original installation or our Web site seamlessly."*

**Online vision:**
- Post households and parties to web pages
- *"Freeware applet so anybody can see the hot party action you post to your Web page"*
- Multi-player potential — *"natural for human-to-human interaction over the Net"*
- *"Great parties can draw great sponsors"*

### Third-Party Development

> *"The add-ons have great potential; they can provide very diverse extensions of the content, and the actions, in your house. You can get some from our Web site."*

**Ecosystem vision:**
- Web TV integration
- Video capture and transmission
- URL-based model sharing
- Cryptographic signatures for plug-in reputation

### MOOLLM Parallel: Extensible Architecture

| Sims Extension | MOOLLM Implementation |
|----------------|----------------------|
| Plug-in objects with behavior | Skills as self-contained plug-ins |
| Freebies/"website bait" | Community skills on GitHub |
| Engine reuse for variants | Skill composition and inheritance |
| Character appeal beyond game | [`card`](../skills/card/) skill for character trading |
| Web seamless shopping | Filesystem + community sharing |
| Third-party development | Open YAML format, documented protocols |
| Applet for viewing | Shared session logs, exportable rooms |

---

## 6. What Will It Take?

The proposal enumerated major technical components:

### Development Status (1996)

| Component | Status | Notes |
|-----------|--------|-------|
| Cross-Platform UI and graphics framework | "Well under development" | — |
| Dialog box definition language | "Java. Com. Bongo?" | Uncertain technology |
| Tile-based graphics for house, furniture, terrain | "Well under development" | — |
| Behavior simulation language, interpreter, editors, "tree tracer" | "Well developed" | SimAntics foundation |
| Behavior "trees" and personalities | "Substantial content development work" | The creative core |
| Architectural tools (floors, walls, doors, windows, furniture) | "Substantial enhancements to come" | — |
| Object editor (bitmaps, interaction behaviors, properties) | "Well developed (on Mac). Several sample objects exist." | Edith foundation |
| 3D animated characters, motion sequences | "Core technology; also for SimCircus, SimCity 3000" | Shared investment |
| Mid-level 3D graphics libraries | "Work with Direct3D on Win95, 'Z-mixing' into a scene background" | Platform-specific |
| 3D renderer for Mac and other non-Win95 platforms | "Core technology" | Cross-platform |
| 3D exporters from 3D Studio Max | "Core technology" | Asset pipeline |
| Relationship Sim and conversations | "Substantial content development work" | — |
| Household Sim, lifestyle, outside activities | — | Major effort |
| Party simulation | — | Major effort |
| Save-game file format, with add-ins | — | Extensibility |
| Simulation timebase | "Supports animation, simulation, fast-forward, 'fast carpenters' effect, networking" | — |
| Audio support and "musical skillz" | — | — |
| UI design and implementation | "Well developed. UI tuned over a long time. Cross platform." | Mature |

### Publishing Toolkit Vision

> *"Publish toolkit-kits slotted into the game as plug-in 3-D objects to allow users to write it primitives so others can make specialized authoring tools."*

**MOOLLM Parallel:** The YAML/Markdown authoring format is MOOLLM's "publishing toolkit" — users create skills, rooms, and characters with standard text editors.

---

## Don Hopkins' Handwritten Marginalia

The original document contains handwritten annotations (by Don Hopkins) that reveal the scope of his thinking:

### On Creative Content

| Note | Context |
|------|---------|
| *"Creative writing"* | Expanding interactions |
| *"Scripts Stories"* | Narrative tools |
| *"dancing to music videos lyrics to Song"* | Music integration |
| *"injected in creative musicals Sit injected"* | Performance systems |

### On Scale and Integration

| Note | Context |
|------|---------|
| *"SimCity Scale 3000's of buildings"* | Exterior views, SimCity integration |
| *"lego-lite sets of building"* | Simplified construction |
| *"simple authoring"* | User-created content |
| *"town See Guyfftoru Buicks"* | Town exploration |

### On Dark/Experimental Content

| Note | Context |
|------|---------|
| *"Three Stigmata of Palmer Eldritch"* | PKD influence — adults playing with dollhouses |
| *"Petri Dish"* | Experimental systems |
| *"Don't prohibit the development of sex, violence, gambling plug-ins"* | Moderation philosophy |
| *"Ratings system for plug-ins? Voluntary, not centralized"* | Community governance |
| *"Sim Deadconcert"* | Dark scenario |
| *"Sim Run it free"* | Alternative scenarios |

### On Pets and Expansion

| Note | Context |
|------|---------|
| *"Pets. Dog, Cat, gerbils, ant farm, fish Reptiles"* | Prescient — became expansion packs |

### On Technology Integration

| Note | Context |
|------|---------|
| *"Simulated home computers"* | In-game computing |
| *"Play video game consoles"* | Meta-gaming |
| *"Parlor play-in"* | Social gaming space |
| *"SimJunk Mail. Banner ads like on web pages. click to follow to sponsor."* | In-game advertising |
| *"TV, Stereo, Phone. Record/CD collection. play music on PC"* | Media integration |
| *"Manage CD collection"* | Personal media |
| *"URL games effect sim subtly"* | Web integration |
| *"elephant, bird, house"* | Pets, expansion |
| *"get cellular costomer"* | Communication tech |
| *"Captures 3-D object/motion in view of camera, transmit URL of models and positioning information"* | 3D capture vision |
| *"read player and der geometry"* | Player sensing |
| *"security in public mind"* | Privacy awareness |
| *"Cryptographic signatures in securities so you can look up reputation of the plug-ins online"* | Trust systems |

### On Robustness

> *"How can we design it to be robust in the face of incompletely built environments? They shouldn't die if you haven't installed bathrooms."*

**MOOLLM Parallel:** The [`robust-first`](../skills/robust-first/) skill and Postel's Law in [`postel`](../skills/postel/) — be liberal in what you accept.

---

## MOOLLM Design Inheritance

### Core Concepts

| Happy-Friends-Home Concept | MOOLLM Implementation | Skill/Protocol |
|---------------------------|----------------------|----------------|
| Three Pillars (Home/Friends/Happiness) | Multi-dimensional needs system | [`needs`](../skills/needs/) |
| Fire-and-forget interactions | Command queue, async actions | [`action-queue`](../skills/action-queue/) |
| Fast-forward time | Time acceleration, speed-of-light | [`time`](../skills/time/), [`speed-of-light`](../skills/speed-of-light/) |
| Plug-in objects with behavior | Skills as modular plug-ins | [`skill`](../skills/skill/) |
| Open-ended goals | Player-defined objectives | [`adventure`](../skills/adventure/) |
| Multiple engagement levels | Observe/command/build modes | Various |
| Direct control switching | Character perspective switching | [`persona`](../skills/persona/) |
| Web integration | Filesystem + community sharing | GitHub, sessions |
| Extensible engine | Skill composition and inheritance | YAML Jazz |
| Voluntary ratings | Ethical framing inheritance | [`representation-ethics`](../skills/representation-ethics/) |
| Behavior trees | [`empathic-expressions`](../skills/empathic-expressions/) | Behavior templates |
| Relationship Sim | Social graph tracking | [`party`](../skills/party/) |
| Party simulation | Event systems | [`party`](../skills/party/) |
| Robustness to incomplete environments | Postel's Law, graceful degradation | [`postel`](../skills/postel/), [`robust-first`](../skills/robust-first/) |

### The Living World Inheritance

The Sims' "lazy default" where characters exist and act autonomously is MOOLLM's foundation:

1. **Characters exist in files** — they have state even when not in play
2. **Rooms contain characters** — spatial organization as filesystem
3. **Autonomous behaviors** — NPCs act according to their nature
4. **Player intervention optional** — observe or direct

### The Extensibility Inheritance

The 1996 vision of user-created objects, web distribution, and third-party tools is MOOLLM's architecture:

1. **YAML files are objects** — create new ones with any text editor
2. **Skills are plug-ins** — drop in new capabilities
3. **GitHub is the web** — share rooms, characters, skills
4. **Open format** — no proprietary tools required

---

## See Also

- [sims-maxis-requirements.md](./sims-maxis-requirements.md) — Seven Points of Sim
- [sims-design-index.md](./sims-design-index.md) — Master index of Sims documents
- [sims-team-history.md](./sims-team-history.md) — Team history including PKD influence
- [sims-personality-motives.md](./sims-personality-motives.md) — Personality and motives system
- [sims-find-best-action.md](./sims-find-best-action.md) — Action selection algorithm
- [sims-simantics-vm.md](./sims-simantics-vm.md) — Distributed behavior system
- [sims-will-wright-microworlds-1996.md](./sims-will-wright-microworlds-1996.md) — Will Wright's 1996 Stanford lecture
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — Incarnate framework

---

*"Then EA bought Maxis, and saved us from our living hell by firing the focus groups, who were the ones actually tormenting us. And they forced us to stop focusing, playing with prototypes, reading comic books, spinning foosball and thinking up names, and then fucking well finish the damn game."*
— Don Hopkins
