# *For Sungman Cho — Sunny Street and an exciting shared universe*

***Status:** Outreach / reading list (public)*  
***Written for:** Sungman Cho and **Sunny Street** (from his public LinkedIn description — we have not played the beta)*  
***Also for:** Anyone curious why MicropolisCore and MOOLLM keep circling similar themes*

***Repos:** [MicropolisCore](https://github.com/SimHacker/MicropolisCore) · [moollm](https://github.com/SimHacker/moollm)

***Canonical:** [designs/email/sunny-street-outreach.md](https://github.com/SimHacker/moollm/blob/main/designs/email/sunny-street-outreach.md)*

---

## *What you said publicly — and what resonates on our side*

*From your LinkedIn post (paraphrased, not a spec for your game):*

- Kids are growing up with AI **before** their own thinking skills fully form — so the product question is pedagogical, not just technical.
- Most tools **give instant answers**; you want kids to learn to **think, create, and solve problems with AI** instead.
- **Sunny Street** is a game: explore a **living town** with **AI characters**, hit **unexpected problems**, work through **curiosity, planning, creativity, and collaboration** (wildfire recovery, crops failing, coordinating villagers).
- Goal: *“help kids build strong thinking muscles in the AI era.”*
- First **closed beta** (May 18, 50 families) — early, real, and appropriately narrow in scope.

*We have not seen the build. Nothing below assumes your save format, your age band, your UI stack, or that you want interoperability on day one. This letter is: “here is the lineage we work in; here are directions that might be fertile **if** they match what you are actually making.”*

### *Why that post caught my attention*

- **“With AI,” not “from AI.”** That is the same wedge we care about: AI as partner in a **challenge the town presents**, not a chatbot that short-circuits the kid’s plan. Our [Imagine Loop](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-imagine-loop.md) is one pattern we use in Micropolis / MOOLLM — game ticks, narrator examines state and proposes edits, human (or kid) stays in the loop.
- **Town + coordinated villagers + systemic surprises** rhymes with Sims / SimCity / microworld history — neighbors, routines, consequences — without claiming Sunny Street is a Sims clone or should be.
- **Scenarios that need planning** (wildfire, crops, coordination) are where [procedural rhetoric](https://github.com/SimHacker/moollm/blob/main/designs/indexes/PROCEDURAL-RHETORIC-INDEX.md) matters: the world argues through what fails and what recovers, not through a lecture about resilience.

*What I do **not** know from the post: whether character state is **inspectable** (by players, modders, researchers — anyone curious), how much simulation runs on-device vs in the model, or what “coordination” looks like in your architecture. Those are good conversation topics, not things we should project onto you.*

### *Fertile directions (optional — only if useful to you)*


| Your stated theme                    | Something we have been exploring (not a prescription)                                                                                                                                                                                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Thinking muscles, not answer vending | Tutors that **Observe → Explain → Preview → Propose → Approve → Execute** ([MOOLLM–Micropolis integration](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-micropolis-integration.md)) — agency stays with the player |
| Unexpected town problems             | Legible cause/effect and [Simulator Effect](https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) — shallow sim on screen, deeper inference in the kid’s head                                     |
| AI villagers + collaboration         | Sims social texture + [legible social dynamics](https://github.com/SimHacker/moollm/blob/main/designs/legible-social-dynamics.md) — if you ever want rules anyone can read, not only vibes                                                              |
| Living town                          | [Micropolis](https://github.com/SimHacker/MicropolisCore) city scale + street-level life sim — **only** if you want a second substrate later; no pressure                                                                                                |


*MicropolisCore’s **[Soul City](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simopolis.md)** and **[MOOLLM](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md)** are our corner of the same **shared universe**: how to pair a real simulation runtime with an LLM layer that helps narrate and remember **without replacing the game**. Sunny Street may build that differently for your players — comparing notes is the collaboration, not merging codebases by default.*

---

## *Possible collaboration (low pressure)*

*Reasonable near-term overlaps — only if you want them:*

- **Compare pedagogy:** instant-answer AI vs planning-first play; what you measure in beta (curiosity, collaboration) vs what we document for tutors and curious players.
- **Compare architecture sketches:** where the “thinking muscle” lives — in the kid’s plan, in town rules, in villager coordination, in an LLM layer — without either project pretending to own the other’s stack.
- **Share reading lists** (below): Sims/MOOLLM lineage on towns, memory, and UI — take or leave.
- **Longer horizon (optional):** if Sunny Street ever exposes **documented, player-owned save data** for characters, we maintain an open **[Bifrost](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md#the-bifrost-the-bridge-as-a-structured-ontological-transition)** target in **[Federation peer games → Sunny Street](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md#sunny-street)** — companion tooling, not a partnership or embed. Until then, it is design fiction on our side, not an ask for your beta.

*Good luck with the May 18 closed beta. Fifty families is the right scale to learn what actually builds thinking muscles.*

---

## *Micropolis Federation — only if character portability ever matters*

*Our catalogue (Sunny Street listed as a [featured peer](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md#sunny-street)) describes **hypothetical** bidirectional import/export — not what your game ships today. Umbrella framing: **[Characters as hydrogen](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md)**.*

*Will Wright, Stanford 1996: **“persistent data that can move from one game to another.”** ([characters as hydrogen](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md)) — compatible **in principle** with a town where kids invest in AI villagers, **if** you someday want cross-world characters and documented saves.*

*What we ship today:* **The Sims 1** via [Soul City](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simopolis.md) and [sims-io](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io). Full peer roster and **[onboarding playbook](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md#how-the-bifrost-handles-a-new-peer-game-onboarding-playbook)** in **[Federation peer games](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md)**.*

### *If interoperability ever became interesting (speculative)*

- **Sims household → Sunny Street town** (hypothetical): only if both saves are bridgeable and **you** want that fantasy — kid-scale relationships, not EA assets inside your runtime.
- **Sunny Street villager → Sims / Dream** (hypothetical): only if you export structured identity data the player owns.
- **Hub, not pairwise lock-in:** soul-file ↔ Stardew, RimWorld, etc. — only if portability is **your** product goal.

*[Family Album as storymaker](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/family-album-as-storymaker.md) is player-to-player stories; Bifrost is game-to-game. Optional layers on a game that stands alone.*

---

## *Where our work overlaps yours*

### *1. Legible simulation (rules you can read, not magic you cannot)*

*The Sims always encoded social possibility in **mechanics** (relationships, motives, objects that advertise what you can do). Stanford’s Generative Agents paper (2023) re-discovered that recipe with LLMs and opaque memory streams. MOOLLM’s bet is older and more literal: **if it matters, it is in a file**. Directories are rooms; characters are paths; memories and traits are YAML you can diff. That is the same ethic as teaching a child “the town has rules” instead of “the model felt like it.”*

*Two labels from our lineage that **might** rhyme with wildfire/crop/coordination scenarios — if you are encoding systemic problems, not only dialogue:*

***Procedural rhetoric** (Bogost): the town argues through its rules. The Sims didn’t lecture about tolerance—it made discrimination impossible in the relationship model. A design question for any town sim: which social possibilities you **encode on purpose**, not which moral you paste in a tooltip.*

***Simulator Effect** (Wright): the shallow simulation runs on the machine; the deep one runs in the kid’s head. Implication is richer than simulation. Name a rule when a child needs to learn the protocol; leave it as felt consequence when a wave, a remembered gift, or a snub already carries the lesson—and don’t talk them out of the magic by over-explaining.*

*[Legible social dynamics](https://github.com/SimHacker/moollm/blob/main/designs/legible-social-dynamics.md) is our worksheet for the first half (rules that were always operating, now spelled in YAML). The second half is why you don’t render every inner monologue.*

***Start here***

- *[Procedural rhetoric index](https://github.com/SimHacker/moollm/blob/main/designs/indexes/PROCEDURAL-RHETORIC-INDEX.md) — rules as arguments; many voices, not averaged mush*  
- *[Simulator Effect (EVAL framework)](https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) — Wright, two computers, implication vs simulation*  
- *Skill: [simulator-effect](https://github.com/SimHacker/moollm/blob/main/skills/simulator-effect/SKILL.md)*  
- *[MOOLLM manifesto](https://github.com/SimHacker/moollm/blob/main/designs/MOOLLM-MANIFESTO.md) — filesystem as world; inspectable state*  
- *[MOOLLM microworld OS](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md) — character = directory, room = directory*  
- *[MOOLLM–Micropolis integration](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-micropolis-integration.md) — tutors, command bus, shared ground*

### *2. AI that scaffolds planning (our lineage — not a prescription for your stack)*

*If Sunny Street’s AI helps kids **plan and coordinate** rather than **answer for them**, that rhymes with our **Imagine Loop** split (we do not know your implementation): the LLM **examines** parsed world state, **imagines** outcomes, **edits** high-level state, and **injects** back into a real runtime — the deterministic engine still ticks; the AI does not pretend to be the physics. One open design question for any town sim with AI in the loop: can **anyone curious** see **what** the system remembered or changed — player, teacher, researcher, you? We use files and git; you may solve it another way.*

*MOOLLM’s **memory palace**, **mind-mirror**, and **character** skills are the toolkit version of that split. The Sims design index maps personality and motive systems, advertisements, and autonomy to file-based equivalents.*

***Start here***

- *[Character simulation index](https://github.com/SimHacker/moollm/blob/main/designs/indexes/CHARACTER-SIMULATION-INDEX.md) — Sims (1997) → Generative Agents → file-based memory*  
- *[Imagine Loop](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-imagine-loop.md) — LLM-as-narrator, not LLM-as-simulator*  
- *Skills: [character](https://github.com/SimHacker/moollm/blob/main/skills/character/SKILL.md) · [memory-palace](https://github.com/SimHacker/moollm/blob/main/skills/memory-palace/SKILL.md) · [mind-mirror](https://github.com/SimHacker/moollm/blob/main/skills/mind-mirror/SKILL.md) · [incarnation](https://github.com/SimHacker/moollm/blob/main/skills/incarnation/SKILL.md) · [representation-ethics*](https://github.com/SimHacker/moollm/blob/main/skills/representation-ethics/SKILL.md)  
- *[Sims design index](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-design-index.md) · [Find-best-action / autonomy*](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-find-best-action.md)

### *3. Direct manipulation and what to show on screen*

*Readable simulation is also a **UI** design challenge — relevant **if** you want kids to do planning and coordination in the world, not only read AI text. Pie menus, SimCity’s tool palette, and The Sims’ object **advertisements** are our lineage’s version of in-place affordances; **PieCraft** extends that for designers who build gesture trees at runtime. Miyamoto/Wright **Simulator Effect**: implication richer than simulation — often better than rendering every inner thought when a glance and a consequence will do.*

***Start here***

- *[Piecraft (MicropolisCore)](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/piecraft/README.md) · [PIE-MENU-MODEL*](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/piecraft/PIE-MENU-MODEL.md)  
- *[SimCity tool palette](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simcity-tool-palette-design.md) · [Virtual pointer and pie cursors*](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/virtual-pointer-and-pie-cursors.md)  
- *[Sims pie menus (moollm)](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-pie-menus.md)*  
- *[Designing inward (Miyamoto + Simulator Effect)](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/designing-inward-miyamoto-principles.md)*  
- *[Simulator Effect (EVAL framework)](https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) — same Wright thread, moollm repo*  
- *Skill: [advertisement](https://github.com/SimHacker/moollm/blob/main/skills/advertisement/SKILL.md) — objects broadcast available actions*  
- *[Interaction design articles index](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/interaction-design-articles-index.md) — HCI corpus with primary sources*

### *4. Town scale, cozy lineage, and building on Sims without cloning*

*A **living town** at street level may someday rhyme with **two-resolution** play (city map + neighborhood) — Will Wright’s 1996 dollhouse demo is the historical receipt. **Soul City** is our umbrella for Micropolis + Sims; **characters-as-hydrogen** explains why people are the binding atom across scales. **OG cozy games** and **Tomodachi** comparisons are optional reading when calibrating what to show kids vs imply.*

***Start here***

- *[Soul City](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simopolis.md)*  
- *[Characters as hydrogen](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md)*  
- *[Will Wright microworlds 1996](https://github.com/SimHacker/moollm/blob/main/designs/sims/sims-will-wright-microworlds-1996.md)*  
- *[OG cozy games](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/og-cozy-games.md) · [Tomodachi life and Soul City*](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/tomodachi-life-and-simopolis.md)  
- *[Federation peer games → Sunny Street](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md#sunny-street) — Sims/Stardew/RimWorld/… ↔ your town via soul-files*  
- *[Constructionist index](https://github.com/SimHacker/moollm/blob/main/designs/indexes/CONSTRUCTIONIST-INDEX.md) — Papert → Wright → microworlds in schools*

### *5. Micropolis + MOOLLM as “town + tutors” (if you want a second substrate)*

***If** you ever want a **city-scale** sibling or classroom mode (not implied by the LinkedIn post): Micropolis (open SimCity) plus MOOLLM tutors is documented as Observe → Explain → Preview → Propose → Approve → Execute — humans and agents on common ground, not agents ghosting the UI.*

- *[MOOLLM–Micropolis integration](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-micropolis-integration.md)*  
- *[Filesystem object model](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/filesystem-object-model.md)*  
- *[Collaborative microworld lineage](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/collaborative-microworld-lineage.md)*  
- *Skill: [micropolis](https://github.com/SimHacker/moollm/blob/main/skills/micropolis/SKILL.md)*

### *6. Proof the microworld pattern is real (not slideware)*

- *[examples/adventure-4](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/README.md) — 150+ file room-based world, characters, emergent play*  
- *Skills: [adventure](https://github.com/SimHacker/moollm/blob/main/skills/adventure/SKILL.md) · [room](https://github.com/SimHacker/moollm/blob/main/skills/room/SKILL.md) · [simulator-effect*](https://github.com/SimHacker/moollm/blob/main/skills/simulator-effect/SKILL.md)

### *7. Git under the filesystem — GitHub as the social layer*

*Our MOOLLM stack uses a filesystem as **single source of truth** for microworlds — characters, rooms, memories, rules you can open in an editor; **git** for history, branches, merges. **If** Sunny Street ever cares about NPC memory over time, modding, classroom forks, or “show me the rule before the patch,” that stack is one proven pattern — not the only pattern, and not something your beta needs to adopt.*

***GitHub** is the collaborative MMORPG layer on top of git: issues as quests, discussions as town halls, pull requests as negotiated merges, orgs and teams as factions, Actions as NPCs that respond to events, Pages as the public square. We are not pretending GitHub is a game engine—we are using infrastructure that already solved multiplayer persistence, permissions, and social workflow so the town simulation can stay in **files you trust**.*

*There is a **constructionist agenda** in our choosing git/GitHub on purpose — Papert’s learn-by-building applied to tools adults use to ship software. Whether that fits a kid-facing commercial game is your call; we mention it as fertile overlap with “thinking muscles,” not as a requirement.*

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

