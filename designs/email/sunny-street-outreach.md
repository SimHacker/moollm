# *For Sungman Cho — Sunny Street and the same problem from two directions*

***Status:** Outreach / reading list (public)*  
***Written for:** Sungman Cho, building **Sunny Street** — an open-world town for kids roughly 9–11*  
***Also for:** Anyone curious why MicropolisCore and MOOLLM keep circling the same themes*

***Repos:** [MicropolisCore](https://github.com/SimHacker/MicropolisCore) · [moollm](https://github.com/SimHacker/moollm)

***Canonical:** [designs/email/sunny-street-outreach.md](https://github.com/SimHacker/moollm/blob/main/designs/email/sunny-street-outreach.md)*

---

## *What I like about Sunny Street — and why it matters beyond one project*

*What caught my eye in your note:*

- A **[readable simulation](https://github.com/SimHacker/moollm/blob/main/designs/legible-social-dynamics.md)** for kids — rules you can name, not mechanics hidden behind “the model decided.” See also [procedural rhetoric](https://github.com/SimHacker/moollm/blob/main/designs/indexes/PROCEDURAL-RHETORIC-INDEX.md) (the town argues through its rules) and [what to show vs imply](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/designing-inward-miyamoto-principles.md) (Simulator Effect: shallow sim on screen, deep sim in the kid’s head).
- **[Direct manipulation](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simcity-tool-palette-design.md)** you can stand behind — [pie menus](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-pie-menus.md), object [advertisements](https://github.com/SimHacker/moollm/blob/main/skills/advertisement/SKILL.md), in-place affordances instead of hunting linear menus.
- Steering away from the black-box trap **[Alan Kay](https://github.com/SimHacker/moollm/blob/main/designs/sims/simcity-multiplayer-micropolis.md#alan-kays-critique-and-vision)** named when criticizing SimCity: opaque assumptions, kids can’t open the hood. (“Air-guitar environment.” We want the opposite.)

*That sits in the Sims lineage I know—neighbors, routines, social texture.*

***Legible rules** and **[narrow AI for memory and recognition](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-imagine-loop.md)** (not a second simulator) are exactly the problems I have been working on since SimCity and The Sims: [microworlds](https://github.com/SimHacker/moollm/blob/main/designs/MOOLLM-MANIFESTO.md), pie menus, advertised actions, and now [MOOLLM](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md), where a character’s mind is a **[folder you can open](https://github.com/SimHacker/moollm/tree/main/skills/character)**, not a secret prompt. The [Imagine Loop](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-imagine-loop.md) is the architectural split: the **game** ticks; the **LLM** examines YAML, imagines, edits, and injects—without pretending to be the physics.*

*That combination is still rare in 2026. Most “AI towns” optimize for viral clips—opaque agents, emergent drama, no inspectable state. I like that you are pointed the other way.*

*Why it matters beyond Sunny Street: your project, MicropolisCore’s **[Simopolis](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simopolis.md)** vision, and MOOLLM are three answers to the same design question—how do you pair a real simulation runtime with an LLM layer that narrates and remembers without replacing the game?*

---

## *Micropolis Federation — characters that travel between worlds (and save files)*

*The umbrella doc is **[Characters as hydrogen](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md)** — read this if you read one Federation doc. Summary:*

*Will Wright, Stanford 1996: **“persistent data that can move from one game to another.”** The **Micropolis Federation** (not a franchise—a Star-Trek-style cooperative of sovereign open-source projects) treats **characters as the unit of value**: one canonical soul-file (`CHARACTER.yml` in git), many **incarnations** at once—a row in a Sims `.iff`, an aggregate in a Micropolis city zone, a MOOLLM citizen directory, a narrative-only **Micropolis Dream** space. They are not copies; they are one identity kept in sync by the **[Bifrost](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md#the-bifrost-the-bridge-as-a-structured-ontological-transition)** protocol (structured import/export between substrates, with provenance and merge semantics like git over identity).*

*Today the shipped path is **The Sims**: parse `Neighborhood.iff` → edit soul-files → write valid `.iff` back ([Simopolis](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simopolis.md), [sims-io](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io)). The substrate is **license-agnostic**—it works on **save files the player owns**, not on embedding proprietary engines. Same posture as 25 years of Sims fan tools.*

*Between players, **[Family Album as storymaker](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/family-album-as-storymaker.md)** moves “snippets of DNA” (character + scene bundles) through a branching graph with Bifrost merge and attribution.*

*Between **other games**, **[Federation peer games](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md)** catalogs who fits next—Stardew, RimWorld, CK3, Dwarf Fortress, Bethesda saves, VTT character sheets—with an **[onboarding playbook](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md#how-the-bifrost-handles-a-new-peer-game-onboarding-playbook)** for any new peer whose save format we can read and write lawfully. **Sunny Street** is exactly that shape of peer once its town/save format is documented: import townsfolk into Dream, export Federation characters into a Sunny Street save, round-trip memories and relationships without either engine owning the other.*

*Supporting plumbing: [Sims content registry](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/sims-content-registry.md) (dependencies), [Tornado/archives](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-tornado-and-the-archives.md) (historical character import), [simopolis uplift roadmap](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simopolis-uplift-roadmap.md) (what ships when).*

---

## *Where our work overlaps yours*

### *1. Legible simulation (rules you can read, not magic you cannot)*

*The Sims always encoded social possibility in **mechanics** (relationships, motives, objects that advertise what you can do). Stanford’s Generative Agents paper (2023) re-discovered that recipe with LLMs and opaque memory streams. MOOLLM’s bet is older and more literal: **if it matters, it is in a file**. Directories are rooms; characters are paths; memories and traits are YAML you can diff. That is the same ethic as teaching a child “the town has rules” instead of “the model felt like it.”*

*For Sunny Street, two labels from our lineage split the problem cleanly.*

***Procedural rhetoric** (Bogost): the town argues through its rules. The Sims didn’t lecture about tolerance—it made discrimination impossible in the relationship model. Sunny Street’s design choice is which social possibilities you **encode on purpose**, not which moral you paste in a tooltip.*

***Simulator Effect** (Wright): the shallow simulation runs on the machine; the deep one runs in the kid’s head. Implication is richer than simulation. Name a rule when a child needs to learn the protocol; leave it as felt consequence when a wave, a remembered gift, or a snub already carries the lesson—and don’t talk them out of the magic by over-explaining.*

*[Legible social dynamics](https://github.com/SimHacker/moollm/blob/main/designs/legible-social-dynamics.md) is our worksheet for the first half (rules that were always operating, now spelled in YAML). The second half is why you don’t render every inner monologue.*

***Start here***

- *[Procedural rhetoric index](https://github.com/SimHacker/moollm/blob/main/designs/indexes/PROCEDURAL-RHETORIC-INDEX.md) — rules as arguments; many voices, not averaged mush*  
- *[Simulator Effect (EVAL framework)](https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) — Wright, two computers, implication vs simulation*  
- *Skill: [simulator-effect](https://github.com/SimHacker/moollm/blob/main/skills/simulator-effect/SKILL.md)*  
- *[MOOLLM manifesto](https://github.com/SimHacker/moollm/blob/main/designs/MOOLLM-MANIFESTO.md) — filesystem as world; inspectable state*  
- *[MOOLLM microworld OS](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md) — character = directory, room = directory*  
- *[MOOLLM–Micropolis integration](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-micropolis-integration.md) — tutors, command bus, shared ground*

### *2. Narrow AI for memory and recognition (not a second simulator)*

*The instinct to use AI for **memory and recognition**, not to re-run The Sims in a browser, matches what we call the **Imagine Loop**: the LLM **examines** parsed world state, **imagines** outcomes at the timescale you choose, **edits** high-level YAML, and **injects** back into a real runtime. The deterministic engine still ticks; the AI does not pretend to be the physics. For a kid-facing town, the parallel is sharp: the **game** handles moment-to-moment affordances; the **AI layer** handles “they remember your birthday” and “this NPC connects you to that quest” — but only if those memories live somewhere a curious player (or parent) could eventually inspect.*

*MOOLLM’s **memory palace**, **mind-mirror**, and **character** skills are the toolkit version of that split. The Sims design index maps personality and motive systems, advertisements, and autonomy to file-based equivalents.*

***Start here***

- *[Character simulation index](https://github.com/SimHacker/moollm/blob/main/designs/indexes/CHARACTER-SIMULATION-INDEX.md) — Sims (1997) → Generative Agents → file-based memory*  
- *[Imagine Loop](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-imagine-loop.md) — LLM-as-narrator, not LLM-as-simulator*  
- *Skills: [character](https://github.com/SimHacker/moollm/blob/main/skills/character/SKILL.md) · [memory-palace](https://github.com/SimHacker/moollm/blob/main/skills/memory-palace/SKILL.md) · [mind-mirror](https://github.com/SimHacker/moollm/blob/main/skills/mind-mirror/SKILL.md) · [incarnation](https://github.com/SimHacker/moollm/blob/main/skills/incarnation/SKILL.md) · [representation-ethics*](https://github.com/SimHacker/moollm/blob/main/skills/representation-ethics/SKILL.md)  
- *[Sims design index](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-design-index.md) · [Find-best-action / autonomy*](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-find-best-action.md)

### *3. Direct manipulation and what to show on screen*

*Readable simulation is also a **UI** problem. Pie menus, SimCity’s tool palette, and The Sims’ object **advertisements** all say: here is what you can do right now, in place, without hunting a linear menu. **PieCraft** extends that to players who design their own pie menu gesture trees and memory maps at runtime — UI literacy as gameplay. For a town aimed at 9–11, the Miyamoto/Wright complement still applies: design inward from the child’s delighted face and **gesturing hands**; use the **Simulator Effect** — implication richer than simulation — so you do not render every inner thought when a glance and a consequence will do.*

***Start here***

- *[Piecraft (MicropolisCore)](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/piecraft/README.md) · [PIE-MENU-MODEL*](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/piecraft/PIE-MENU-MODEL.md)  
- *[SimCity tool palette](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simcity-tool-palette-design.md) · [Virtual pointer and pie cursors*](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/virtual-pointer-and-pie-cursors.md)  
- *[Sims pie menus (moollm)](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-pie-menus.md)*  
- *[Designing inward (Miyamoto + Simulator Effect)](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/designing-inward-miyamoto-principles.md)*  
- *[Simulator Effect (EVAL framework)](https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) — same Wright thread, moollm repo*  
- *Skill: [advertisement](https://github.com/SimHacker/moollm/blob/main/skills/advertisement/SKILL.md) — objects broadcast available actions*  
- *[Interaction design articles index](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/interaction-design-articles-index.md) — HCI corpus with primary sources*

### *4. Town scale, cozy lineage, and building on Sims without cloning*

*Sunny Street’s open world rhymes with **two-resolution** play: city map and street-level life (Will Wright’s 1996 dollhouse demo is the historical receipt). **Simopolis** is our umbrella doc for Micropolis + Sims under one federation; **characters-as-hydrogen** explains why people are the binding atom across scales. **OG cozy games** and **Tomodachi comparison** docs are useful when you are deciding what Nintendo-style towns hide versus what you want Sunny Street to make legible.*

***Start here***

- *[Simopolis](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simopolis.md)*  
- *[Characters as hydrogen](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md)*  
- *[Will Wright microworlds 1996](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-will-wright-microworlds-1996.md)*  
- *[OG cozy games](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/og-cozy-games.md) · [Tomodachi life and Simopolis*](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/tomodachi-life-and-simopolis.md)  
- *[Constructionist index](https://github.com/SimHacker/moollm/blob/main/designs/indexes/CONSTRUCTIONIST-INDEX.md) — Papert → Wright → microworlds in schools*

### *5. Micropolis + MOOLLM as “town + tutors” (if you want a second substrate)*

*If Sunny Street ever wants a **city-scale** sibling or classroom mode: Micropolis (open SimCity) plus MOOLLM tutors is documented as Observe → Explain → Preview → Propose → Approve → Execute — humans and agents on common ground, not agents ghosting the UI.*

- *[MOOLLM–Micropolis integration](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-micropolis-integration.md)*  
- *[Filesystem object model](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/filesystem-object-model.md)*  
- *[Collaborative microworld lineage](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/collaborative-microworld-lineage.md)*  
- *Skill: [micropolis](https://github.com/SimHacker/moollm/blob/main/skills/micropolis/SKILL.md)*

### *6. Proof the microworld pattern is real (not slideware)*

- *[examples/adventure-4](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/README.md) — 150+ file room-based world, characters, emergent play*  
- *Skills: [adventure](https://github.com/SimHacker/moollm/blob/main/skills/adventure/SKILL.md) · [room](https://github.com/SimHacker/moollm/blob/main/skills/room/SKILL.md) · [simulator-effect*](https://github.com/SimHacker/moollm/blob/main/skills/simulator-effect/SKILL.md)

### *7. Git under the filesystem — GitHub as the social layer*

*A filesystem is the right **single source of truth** for a microworld: characters, rooms, memories, and rules you can open in an editor. Files and directories are the ground truth **right now**. **Git** adds a whole dimension on top: history (who changed what, when, and why), branches (parallel timelines, what-if towns), merges (reconciling two stories), blame and audit trails, tags and releases, reversibility without mystery undo stacks. For Sunny Street, that matters the moment you care about NPC memory over time, modding, classroom forks, or “show me the rule before the patch.”*

***GitHub** is the collaborative MMORPG layer on top of git: issues as quests, discussions as town halls, pull requests as negotiated merges, orgs and teams as factions, Actions as NPCs that respond to events, Pages as the public square. We are not pretending GitHub is a game engine—we are using infrastructure that already solved multiplayer persistence, permissions, and social workflow so the town simulation can stay in **files you trust**.*

*There is a **constructionist agenda** in choosing this stack on purpose: pre-program people to get git—and even GitHub—because the town, the classroom, and the modding community require them. Not “take a version-control elective,” but “your neighborhood fork branched, merge your story back, read the blame on who changed the bakery rule.” Papert’s learn-by-building, applied to the tools adults already use to ship software. That is a useful skill in 2026 whether or not Sunny Street ships; baking it into a kid-facing microworld is feature, not detour.*

***Start here***

- *[GitHub as MMORPG (moollm)](https://github.com/SimHacker/moollm/blob/main/designs/GITHUB-AS-MMORPG.md) — branches as universes, issues as objects, social dynamics as rhetoric*  
- *[GitHub as MMORPG multiverse (MicropolisCore)](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/github-as-mmorpg-multiverse.md) — MicropolisHub mapping: orgs, teams, issues, Pages*  
- *[Command timeline and git branches](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/command-timeline-git-branches.md) — the branch is the universe; commands are leaves*  
- *[MOOLLM–Micropolis integration](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-micropolis-integration.md) — Observe → Propose → Approve → Execute → **commit***  
- *[Constructionist index](https://github.com/SimHacker/moollm/blob/main/designs/indexes/CONSTRUCTIONIST-INDEX.md) — Papert → Wright → school-owned repos; GitHub as educational platform*  
- *Skill: [constructionism](https://github.com/SimHacker/moollm/blob/main/skills/constructionism/SKILL.md) · [play-learn-lift*](https://github.com/SimHacker/moollm/blob/main/skills/play-learn-lift/SKILL.md)  
- *[Collaborative microworld lineage](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/collaborative-microworld-lineage.md) — SimCityNet, OLPC, constructionist multiplayer*

---

## *Hubs (when you want to wander)*


| *Hub*                    | *URL*                                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| *MOOLLM design indexes*  | *[designs/indexes/INDEX.md](https://github.com/SimHacker/moollm/blob/main/designs/indexes/INDEX.md)*                       |
| *MOOLLM skills (129)*    | *[skills/INDEX.md](https://github.com/SimHacker/moollm/blob/main/skills/INDEX.md)*                                         |
| *MicropolisCore designs* | *[documentation/designs/README.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/README.md)* |


---

## *Outside the repos (still on-point)*

- *[Designing user interfaces to simulation games](https://donhopkins.medium.com/designing-user-interfaces-to-simulation-games-bd7a9d81e62d) — Don Hopkins*  
- *[Will Wright, Stanford 1996](https://www.youtube.com/watch?v=nsxoZXaYJSk)*  
- *[Generative Agents (Park et al., 2023)](https://arxiv.org/abs/2304.03442) — compare to file-based memory in the character-simulation index*

---

