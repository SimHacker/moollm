# Will Wright: Interfacing to Microworlds (1996)

> *"Our real end product is the mental model in the player's head."*
> — Will Wright, Stanford University, April 26, 1996

---

## Summary

This document comprehensively summarizes Will Wright's landmark lecture to Terry Winograd's user interface class at Stanford University on April 26, 1996. Wright demonstrates SimEarth, SimAnt, and SimCity 2000, then previews an extremely early prototype of "Dollhouse" (which became The Sims) — **four years before the game shipped**.

The lecture reveals Wright's core design philosophy and demonstrates ideas that directly inform MOOLLM's architecture. Don Hopkins attended this lecture, took extensive notes, and later worked with Will Wright at Maxis on The Sims from 1997-2000.

**Video:** [YouTube - Will Wright - Maxis - Interfacing to Microworlds](https://www.youtube.com/watch?v=...)  
**Notes:** [Don Hopkins' Medium article](https://donhopkins.medium.com/designing-user-interfaces-to-simulation-games-bd7a9d81e62d)  
**Stanford Archive:** [searchworks.stanford.edu](https://searchworks.stanford.edu/view/yj113jt5999)

---

## Table of Contents

1. [The Anatomy of a Simulation Game](#the-anatomy-of-a-simulation-game)
2. [On the User Model](#on-the-user-model)
3. [On the Simulation Model](#on-the-simulation-model)
4. [On the Gameplay](#on-the-gameplay)
5. [On the User Interface](#on-the-user-interface)
6. [Post Morta](#post-morta)
7. [The Dollhouse Preview](#the-dollhouse-preview)
8. [The Julie Doll Lesson](#the-julie-doll-lesson)
9. [The Backseat Driver](#the-backseat-driver)
10. [The Storytelling Insight](#the-storytelling-insight)
11. [Failure Modes: Kids vs. Adults](#failure-modes-kids-vs-adults)
12. [The Calvin Syndrome](#the-calvin-syndrome)
13. [Key Design Principles](#key-design-principles)
14. [MOOLLM Parallels](#moollm-parallels)
15. [Historical Context](#historical-context)

---

## The Anatomy of a Simulation Game

Wright identifies several tightly coupled parts of a simulation game that must be designed closely together:

| Part | Role | Challenge |
|------|------|-----------|
| **Simulation Model** | Modeling the real world | Must be tractable on hardware |
| **Game Play** | Problem solving, constraints, challenges | Must be engaging |
| **User Interface** | Visualizing and controlling the simulation | Must be intuitive |
| **User's Model** | The mental model in the player's head | The actual end product |

> *"In order for a game to be realizable, all of those different parts must be tractable. There are games that might have a great user interface, be fun to play, easy to understand, but involve processes that are currently impossible to simulate on a computer."*

### The Unrealized Sim Thunder Storm

> *"There are also games that are possible to simulate, fun to play, easy to understand, but that don't afford a useable interface: Will has designed a great game called 'Sim Thunder Storm', but he hasn't been able to think of a user interface that would make any sense."*

**The Problem:** Some systems are hard to control because there's no natural interaction metaphor.

**MOOLLM Parallel:** Natural language interfaces solve this problem fundamentally. When you can describe what you want in prose, many previously "impossible" interfaces become trivial:

| Traditional Interface | MOOLLM Interface |
|----------------------|------------------|
| Buttons, sliders, menus | Prose commands |
| "What does this control?" | "What do you want?" |
| Metaphor discovery required | Intent expression natural |
| Interface limits interaction | Imagination limits interaction |

---

## On the User Model

### The Mental Model Compiler

This is Wright's most profound insight:

> *"The digital models running on a computer are only compilers for the mental models users construct in their heads."*

> *"The actual end product of SimCity is not the shallow model of the city running in the computer. More importantly, it's the deeper model of the real world, and the intuitive understanding of complex dynamic systems, that people learn from playing it, in the context of everything else about a city that they already know."*

**The Key Insight:** SimCity, SimEarth, and SimAnt are educational because they **implant useful models in their users' minds**. The computer simulation is an intermediary — an "incremental step" — between reality and understanding.

**MOOLLM Parallel:**

| Sims Mental Model | MOOLLM Mental Model |
|-------------------|---------------------|
| How cities work | How conversations work |
| How ecosystems balance | How characters interact |
| How ants organize | How skills compose |
| How life unfolds | How stories emerge |

Skills are compilers for mental models. The LLM processes skill definitions, but the real output is the player's understanding of:
- How to structure conversations
- How to develop characters
- How to build worlds
- How emergent behavior arises

**MOOLLM Skill:** All skills are mental model compilers

---

## On the Simulation Model

### Reverse Over-Engineering

> *"Many geeks have spent their time trying to reverse engineer the simulator by performing experiments to determine how it works, just for fun. This would be a great exercise for a programming class."*

Don's experience:

> *"When I first started playing SimCity, I constructed elaborate fantasies about how it was implemented, which turned out to be quite inaccurate. But the exercise of coming up with elaborate fantasies about how to simulate a city was very educational, because it's a hard problem!"*

**Key Insight:** The act of trying to reverse-engineer the simulation IS the learning. Players who guess at implementation learn more than players who read documentation.

### Implication Is More Efficient Than Simulation

This is one of Wright's most practical insights:

> *"The actual simulation is much less idealistically general purpose that I would have thought, epitomizing the Nike 'just do it' slogan... It sacrifices expandability and modularity for speed and size, just the right trade-off for the wonderful game that it is."*

> *"Because of its nature as a game, and the constraint that it must run on low end home computers, it tries to fool people into thinking it's doing more than it really is, by taking advantage of the knowledge and expectations people already have about how a city is supposed to work. **Implication is more efficient than simulation.**"*

### Players Attribute Causality That Doesn't Exist

> *"People naturally attribute cause and effect relationships to events in SimCity that Will as the programmer knows are not actually related. Perhaps it is more educational for SimCity players to integrate what they already know to fill in the gaps, than letting them in on the secret of how simple and discrete it really is."*

**MOOLLM Parallel:** LLMs work exactly this way:

| SimCity Implication | MOOLLM Implication |
|---------------------|-------------------|
| Player fills in city dynamics | Player fills in character psychology |
| Simple rules + player knowledge | Skill templates + LLM imagination |
| Attributed causality | Emergent narrative |
| More educational than "real" simulation | More meaningful than scripted dialogue |

The **speed of light pattern** leverages this: let the LLM's imagination do the heavy lifting. Don't simulate every detail — imply it.

### The SimRefinery Story

> *"Then there was the oil company who wanted 'Sim Refinery', so you could use it to lay out oil tanker ports and petroleum storage and piping systems, because they thought that it would give their employees useful experience in toxic waste disaster management, in the same way SimCity gives kids useful experience in being the mayor of a city."*

SimRefinery was later recovered and analyzed by Phil Salvador at [The Obscuritory](https://obscuritory.com). The game was real — it actually taught oil refinery management through play.

**MOOLLM Parallel:** Skills can teach any domain. The [`skill`](../skills/skill/) framework is domain-agnostic.

### The Sim MIS Disaster

> *"And there was the X-Terminal vendor who wanted to adapt the simulator in SimCity into a game called 'Sim MIS', that they would distribute for free to Managers of Information Systems... The idea was that the poor overworked MIS would have fun playing this game in which they could build networks with PCs, X-Terminals, and servers... that had disasters like 'viruses' infecting the network of PC's, and 'upgrades' forcing you to reinstall Windows on every PC, and business charts that would graphically highlight the high maintenance cost of PCs versus X-Terminals."*

> *"Their idea was to use a fun game to subtly influence people into buying their product, by making them lose if they didn't. Unlike the oil company, they certainly realized the potential to exploit the indirect ways in which a game like SimCity can influence the user's mind, but **they had no grip on the concept of subtlety or game design**."*

**The Lesson:** Propaganda games don't work because they're not fun. Players see through rigged systems. Educational games must be **genuinely good games** first.

**MOOLLM Parallel:** MOOLLM skills must be genuinely useful, not propaganda for any framework or ideology.

---

## On the Gameplay

### Games Are Separate from Simulations

> *"Usually the game is separate from the simulation. Games can be based on conflicts and goals, that are external to the simulation itself. The simulation goes on doing its thing, and the user can play different games with their own sets of goals."*

> *"The simulation does not consider fires spreading between buildings to be an error condition or a source of conflict — that's just the way the simulator's supposed to behave. But the user might, unless the game they're playing is pyromaniacal."*

**Key Insight:** The simulation is neutral. Games are interpretive layers on top of simulations.

**MOOLLM Parallel:**

| Layer | Content | Example |
|-------|---------|---------|
| **Simulation** | Rooms, characters, objects | YAML files, skill definitions |
| **Game** | Goals, challenges, win conditions | Adventure scenarios, quests |
| **Interpretation** | Player's story, meaning | Session logs, narratives |

Players can use the same simulation for different games:
- **Story game:** Create narrative arcs
- **Optimization game:** Maximize character stats
- **Social game:** Build relationships
- **Building game:** Design rooms and worlds

### SimCity as Multiple Toys in One

You can use SimCity as:
- A **sandbox** or landscaping toy (terraforming without starting the city)
- A **painting tool** (drawing designs with land, water, roads, buildings)
- A **scenario game** (disasters with specific goals)
- A **city builder** (open-ended development)
- A **personalization tool** (naming roads, buildings, districts)

**MOOLLM Parallel:** MOOLLM supports multiple play modes:

| SimCity Toy | MOOLLM Mode |
|-------------|-------------|
| Sandbox/landscaping | World building, room creation |
| Painting | Character design, atmosphere setting |
| Scenario | Adventure quests, challenges |
| City builder | Emergent world development |
| Personalization | Character naming, story crafting |

### SimCity as Story Medium

> *"There was some interesting discussion about using SimCity as a medium for story telling: encouraging people to imagine far beyond the bounds of what the computer is able to simulate."*

> *"You can build cities to empathize with, and tell stories about them, about their people, culture, buildings, and history."*

**Proposed classroom exercise:**

> *"A class of students could label different parts of a city, and each person could tell a story about a different part, that interacted with the stories going on in neighboring parts of the city. Then they could make a web site with the downloadable city, and an image map of the whole city, linking to all the stories on web pages, with screen snapshots of their neighborhoods, and lots of hypertext links between each story."*

**MOOLLM Parallel:** This is exactly what MOOLLM does with rooms, characters, and session logs:

| SimCity Storytelling | MOOLLM Storytelling |
|---------------------|---------------------|
| City as story setting | Rooms as story settings |
| Neighborhood stories | Room-specific narratives |
| Hypertext links between stories | Links between sessions, characters, rooms |
| Web site with downloadable city | GitHub repo with shareable world |
| Image map of whole city | Directory structure as world map |

The simulation is the paper; the player writes stories on it.

---

## On the User Interface

Wright demonstrated the close-up and overall views in SimEarth, and showed how SimCity 2000 integrated these with zooming in one window. He discussed information density and screen size.

**Key Observations:**
- Multiple views of the same data serve different purposes
- Zoom levels correspond to different types of thinking
- Information density must match screen real estate

**MOOLLM Parallel:** Room descriptions serve as "zoom levels":
- **Overview:** List rooms in a directory
- **Detail:** Read a room's ROOM.yml
- **Deep dive:** Read individual object files
- **Narrative:** Session logs provide story-level view

---

## Post Morta

Wright compared his games against SimCity Classic as the standard:

| Game | Assessment | Problem |
|------|------------|---------|
| **SimEarth** | Too complex | Users couldn't grasp or affect the simulation satisfyingly |
| **SimAnt** | Too simple | Popular with younger kids, but not enough depth |
| **SimCity 2000** | Just right | Balance of complexity and accessibility |

### SimEarth Problems

> *"With SimEarth, anything you do is quickly wiped out by continental drift, erosion, and evolution; you can walk away from it for a while, come back later, and it will have evolved life or shriveled up and died without you, looking pretty much the same as if you had slaved over it for hours."*

> *"It was too complex a simulation for people to grasp or effect in a satisfying way."*

**The Lesson:** Player agency requires visible, lasting impact. If your actions disappear, you're not really playing.

**Time scale communication:** The view controls along the bottom were ordered in a temporal progression, in the order you'd need to use them, from continental drift to technology display.

### SimAnt Problems

> *"SimAnt had just the opposite problem — it was too simple, but that made it popular with younger kids."*

> *"Like SimEarth, it didn't support creative personal imprinting as well as SimCity, since one ant farm looks pretty much like any other, and ants are quite disposable and devoid of personality…"*

**Educational point:** Teaching about emergent behavior of multi-cellular organisms.

> *"I think SimAnt would make a fascinating large scale multi player game."*

### The Sweet Spot

**MOOLLM Parallel:** The Goldilocks principle:

| Too Simple | Just Right | Too Complex |
|------------|------------|-------------|
| No emergence | Emergent behavior | Unpredictable chaos |
| Boring | Engaging | Frustrating |
| No learning | Discovery | Confusion |
| SimAnt | SimCity/The Sims | SimEarth |

MOOLLM targets the sweet spot through **skill composition** — simple skills combine to create complex behaviors without overwhelming complexity.

---

## The Dollhouse Preview

This is the most remarkable part of the lecture — **four years before The Sims shipped**.

### The $5 Billion Question

> **Student:** *"What projects are you working on now, and if you'd rather not talk about that, what projects or models had you considered before that were kind of interesting that you didn't do?"*
>
> **Will Wright:** *"Oh, God..."*

What followed was a preview of the project that would become the best-selling PC game of all time.

### The Hobby Model vs. Movie Model

> *"Most of the game industry right now is built on kind of the movie model. So you spend a lot of money developing one big title, you come out with it, you advertise it, either it goes or it dies, and then you do the next one separate. Except for sequels."*

> *"Now what we've tried to do, and we're kind of working on slowly over time, is to build our games more as a hobby model. Where people buy and collect things, but they relate to the last things they collected."*

> *"It's like a train set. You build this train set, and some people get into the building the hills, and the cliffs, and the mountains, and the trees, really detailed. They could care less about the train. Other people get into the village, or the track switching, and the scheduling. Everybody can kind of come into that, take their particular slant on it, their interest, and focus in that area in great detail."*

**MOOLLM Parallel:** MOOLLM follows the hobby model:

| Movie Model | Hobby Model | MOOLLM |
|-------------|-------------|--------|
| One-shot consumption | Ongoing collection | Session accumulation |
| Producer-controlled | Player-customized | User-created skills |
| Closed experience | Open extension | Community contributions |
| Buy next game | Extend this game | Fork and extend |
| One play style | Multiple focuses | Various skill loadouts |

Skills, rooms, and characters can be collected, shared, and combined. Players focus on what interests them — some on character development, others on world-building, others on game mechanics.

### Loading SimCity into Dollhouse

> *"This is a game I call Dollhouse. And if this looks familiar, it's because I've just loaded a SimCity file into here. So what we're seeing is a SimCity file, but now at this point I can actually zoom down to the street level."*

**The vision:** Walk around inside the cities you built in SimCity. Data portability between games.

**MOOLLM Parallel:** Rooms can be shared between adventures. Characters can move between worlds. Skills apply across contexts.

### The Distributed AI Architecture

This is the revolutionary idea — **behavior lives in objects, not characters**:

> *"Now what's interesting here is that that person, in the person's data structure, there's no knowledge of any objects in this environment whatsoever. The object itself contains the descriptions of how a person interacts with it, and why, what the animation sequence would be, and the scheduling."*

Objects **advertise** their affordances:

> *"A person's in a room, they have certain motivations, needs, they might be hungry, sleepy, lonely, angry. They scan the room for people and objects, and the objects are all kind of advertising: 'If you're angry, pick up me and throw me!', 'If you're hungry, eat me!'. And there's a communication there. It's all data driven."*

Even animations are distributed:

> *"So they don't have to know how to ride a bike, or sit on the toilet. The object tells them how to, when they come up and say, 'okay, you're gonna make me less hungry, I'm gonna interact with you, what do I do?'. The object tells it what to do."*

### The Extensibility Vision

> *"The cool thing about this is that we can drop new objects in later. Maybe it's network based, or maybe it's something else. We can even have tools where the users build these objects. Maybe one person is totally into designing furniture, or designing exercise equipment, I don't know what, exercise videos. But if we had a tool to where the user could build these things, they could then post them on the net, and other people could download them, and then the environment gets more rich."*

This vision was realized with tools like:
- **SimShow** — object viewer
- **IFFPencil2** — resource editor
- **FreeTheSims** — modding tools
- **Transmogrifier** — object creation
- **RugOMatic** — picture storytelling rugs

And fan sites like:
- **SimFreaks** — professional custom content
- **Simslice** — unique objects
- **SimBabes** — wedding playsets and more

### Doom-Compatible Data Structures

> *"This is actually a very similar data structure to Doom. I could be in here in a 3D point of view, shooting the person on the toilet if I wanted to. Maybe it's a different game player in a different game, but still running off the same server."*

> *"So in a way you can think of this as a graphic MUD or something like that."*

**MOOLLM Parallel:** This is exactly the MOOLLM architecture:

| The Sims (1996 Vision) | MOOLLM (2025) |
|------------------------|---------------|
| Objects advertise affordances | Skills advertise via CARD.yml |
| Characters don't know objects in advance | Characters discover skill capabilities |
| Data-driven interactions | YAML-driven interactions |
| Drop new objects in later | Drop new skills in later |
| User-created objects | User-created skills |
| Network distribution | GitHub distribution |
| "Graphic MUD" | Text-based MUD with LLM |

---

## The Julie Doll Lesson

Wright tells a cautionary tale about a $250 talking doll with voice recognition:

> *"They put this in focus groups with girls. And they played with it for a while, and then after about a half an hour they take the batteries out, and keep playing with it."*

Why?

> *"What was happening is that the girls were propping up this elaborate fantasy in their play, and the dolls were supposed to be a structure for that fantasy, they weren't supposed to BE the fantasy. The doll was telling them what the fantasy was, and it was conflicting with what the girls were saying, and so it was interfering actively with their fantasy and their play."*

**The Lesson:** Don't make AI too specific. Leave room for imagination.

> *"We don't have to be doing a valid simulation of human personality. What we have to do is we have to put up something that's ambiguous enough to where somebody can read in what they want."*

**MOOLLM Parallel:**

| Over-specific AI | Ambiguous AI |
|------------------|--------------|
| Scripted dialogue | Prose templates |
| Fixed personalities | Personality traits as guides |
| AI tells you the fantasy | AI supports your fantasy |
| Batteries come out | Engagement continues |

This is why MOOLLM characters speak in prose, not scripted dialogue. The abstraction leaves room for player imagination. The LLM provides structure; the player provides meaning.

**MOOLLM Skill:** [`empathic-templates`](../skills/empathic-templates/) — structure without over-specification

---

## The Backseat Driver

Wright observes that kids rarely play computer games alone:

> *"One of the interesting things I've noticed with my daughter is that she almost never plays computer games or video games by herself. But if a friend's over they'll both play them. And usually it's one at the controls, and the other one is the backseat driver. And it's the dialogue between the two that really makes the game interesting."*

Games as **social facilitators**:

> *"So really for them, the game is facilitating a social interaction. And the game itself is not interesting enough for them to really spend much time with it. But in terms of it facilitating a social interaction, that's when it really is valuable."*

**Social currency:**

> *"And they maybe have Super Mario Brothers, and I'm motivated to get better at it and find the hidden level, so I can tell Tommy. And it's kind of like social currency that I'm passing around, this knowledge I have about the system."*

**MOOLLM Parallel:**

| Backseat Driver Pattern | MOOLLM Pattern |
|------------------------|----------------|
| Player + observer | User + LLM collaborating |
| Dialogue makes it interesting | Conversation IS the game |
| Social facilitation | Session logs as shared narrative |
| "Tell Tommy about the secret level" | Share sessions, discoveries, adventures |

Session logs like [`don-session-1.md`](../examples/adventure-4/sessions/don-session-1.md) capture this dialogue. The "backseat driver" is often the user themselves, talking to the LLM about what the characters should do.

---

## The Storytelling Insight

Don Hopkins made a crucial observation, which Wright enthusiastically confirmed:

> **Don Hopkins:** *"They're using it as a medium to tell stories about."*
>
> **Will Wright:** *"Yeah!"*
>
> **Don Hopkins:** *"Where they're using it as a piece of paper, to write."*
>
> **Will Wright:** *"Yeah, that's exactly right. There's a parallel simulation going on here in the game. Everybody's taking a linear path through this, and they're basically, most people will attempt to understand things like this with a story. They'll think about 'I did this, then that happened, because of that', and so the story becomes kind of their logical connection, their logical reverse engineering, of the simulation that they're playing inside of."*

**MOOLLM Parallel:** This is the core MOOLLM insight:

| Insight | The Sims | MOOLLM |
|---------|----------|--------|
| The medium | Simulation | Rooms, skills, characters |
| The output | Stories | Session logs |
| Player's role | Storyteller | Author/player |
| Simulation's role | Paper | Paper |
| Meaning | Player-created | Player-created |

The simulation is paper; the player writes stories on it. Session logs ARE the stories.

---

## Failure Modes: Kids vs. Adults

Wright identifies a crucial difference in how children and adults approach games:

### Adults

- **Afraid of failure**
- Timid, think twice before clicking
- Don't try random things
- When they fail, they want to know why
- If they don't understand failure, they **quit**

### Kids

- **Love failure**
- Build towers of blocks just to knock them down
- Failure doesn't bother them because they're always failing
- What they don't like is **boring** failure
- Learn fast because they're not afraid to fail

> *"What's important for the kid is that the failure mode is fun and interesting. Adults are uncomfortable with failure in general. Which is what makes kids so cool. They're just really fun to watch. And that's, I think, one of the reasons they learn so fast. They're not afraid to fail, and the failure is really the basis of their learning."*

**MOOLLM Parallel:**

| Design Principle | Implementation |
|------------------|----------------|
| Make failure fun | Interesting consequences, not just "game over" |
| Make failure understandable | Transparent YAML, traceable causality |
| Make failure recoverable | Git saves, session branches |
| Make failure informative | Failure teaches about the system |

The filesystem-as-world makes MOOLLM failure-friendly. You can always see what went wrong by reading the files.

---

## The Calvin Syndrome

Wright discovered that the first thing people do with SimCity is find the bulldozer and start destroying things:

> *"The first thing they would do is they would find the bulldozer, because it was the first tool, and they'd try it. Generally it blows something up... And so, they would sit there, it was kind of like poking an ant colony with a stick to see what happens. They had to perturb the system to get a sense of is it fragile or not, or is this a painting, or is it really a simulation?"*

This is universal — kids and adults both test validity by destruction.

> *"So we decided to name that the Calvin Syndrome. These people wanted to go in and wreak havoc on these things."*

**The Solution:** The disaster menu. Let players destroy on purpose, get it out of their system, then they appreciate building more.

> *"It's really funny the disaster thing, because I think people have to see how fragile a system is before they really appreciate building it."*

**MOOLLM Parallel:**

| Calvin Syndrome | MOOLLM Support |
|-----------------|----------------|
| "Is this real?" | Editable YAML files — poke the system |
| Test by destruction | Git branches — experiment safely |
| Disaster menu | The Grue, hazards, what-if scenarios |
| "Is this a painting?" | No — it's a simulation, and you can change it |

---

## Key Design Principles

### 1. Mental Model Compiler
The computer simulation is just a compiler for the mental model in the player's head. The real output is understanding, not graphics.

### 2. Implication Over Simulation
Take advantage of what players already know. The simulation doesn't need to be complete — players fill in the gaps with their own knowledge.

### 3. Toys, Not Games
Leave goals open-ended. Let players decide what winning means. Multiple valid play styles.

### 4. Entertaining Failure
Failure should be fun and understandable. If players can't figure out why they failed, they'll quit. Make failure visible and recoverable.

### 5. The Calvin Syndrome
Let players destroy things. They need to test validity before they trust the simulation. Destruction builds appreciation.

### 6. Distributed Intelligence
Put behavior in objects, not agents. Objects advertise what they can do; agents discover affordances. This enables infinite extensibility.

### 7. Structural Ambiguity
Don't make AI too specific. Leave room for player imagination to fill in the gaps. Support fantasy, don't dictate it.

### 8. Social Currency
Games facilitate social interaction. The dialogue around the game matters as much as the game itself. Discovery is shareable.

### 9. Stories as Reverse Engineering
Players understand simulations through stories. The narrative is their model of causality. Stories are how humans process complexity.

### 10. The Hobby Model
Build games where things relate to what players already collected. Data portability between games. Ongoing investment, not one-shot consumption.

---

## MOOLLM Parallels

### Comprehensive Mapping

| Wright Concept (1996) | MOOLLM Implementation (2025) | Skill/Protocol |
|----------------------|------------------------------|----------------|
| Mental model compiler | Skills compile to player understanding | All skills |
| Implication over simulation | LLM imagination fills gaps | [`speed-of-light`](../skills/speed-of-light/) |
| Toys, not games | Rooms are sandboxes, players set goals | [`adventure`](../skills/adventure/) |
| Entertaining failure | Transparent YAML, traceable causality | Filesystem transparency |
| Calvin Syndrome | Editable files, "poke" the simulation | Git + YAML |
| Distributed intelligence | Skills advertise via CARD.yml | [`card`](../skills/card/) |
| Objects contain behavior | Skills contain methods and protocols | [`skill`](../skills/skill/) |
| Structural ambiguity | Prose descriptions, not scripted dialogue | [`empathic-templates`](../skills/empathic-templates/) |
| Social currency | Session logs capture dialogue | Session system |
| Stories as reverse engineering | Sessions ARE the stories | Session logs |
| Data portability | Shared YAML files, skill inheritance | YAML Jazz |
| Hobby model | Collect and extend skills over time | Community skills |
| Network distribution | GitHub, community skills | Open source |
| User-created objects | User-created skills and rooms | Open format |
| "Graphic MUD" | Text-based MUD with LLM | MOOLLM itself |

### The Trurl Connection

Wright's dream of building "Trurl's invention" — a box with a kingdom inside, controlled through an interface — is MOOLLM's mission statement. From Stanislaw Lem's "The Cyberiad":

> *"We're nowhere near building Trurl's invention, but I think to me that's kind of why I do a lot of this."*

The difference between 1996 and 2025:

| Trurl's Invention | MOOLLM |
|-------------------|--------|
| "Really fancy knobs" | Natural language |
| Physical box | Filesystem as world |
| Kingdom to rule | Characters to befriend |
| Decrees and control | Conversation and collaboration |
| Electronics and mechanics | LLM and YAML |

**We're getting closer.**

---

## Historical Context

### Don Hopkins' Involvement

> *"I was fascinated by Dollhouse, and subsequently went to work with Will Wright at Maxis (then EA) for three years. We finally released it as The Sims in 2000, after several name changes: TDS (Tactical Domestic Simulator), Project-X (everybody has one of those), Jefferson (after the president, not the sitcom), happy fun house (or some other forgettable Japanese whimsy)."*

> *"A couple of years before seeing this demo [1994], Will dropped by my office at Kaleida Labs, plugged his hard drive into my Mac, and gave me a demo of an early version of Dollhouse that I couldn't believe was remotely possible on the regular old computer I used every day."*

### The Sims Steering Committee Demo (June 4, 1998)

> *"After we finally decided to name it 'The Sims', but a year and a half before we finally released it on March 2000, we produced a private internal EA demo version for 'The Sims Steering Committee' on June 4, 1998. It was well received by the executives and decision makers at EA (i.e. their kids), so we were given the go-ahead to finish and ship The Sims."*

The "steering committee" demo convinced EA to ship the game that became the best-selling PC game of all time.

### Chaim Gingold's Research

Chaim Gingold's PhD dissertation "Play Design" (UC Santa Cruz, 2018) includes:
- SimCity Reverse Diagrams — analyzing how SimCity works
- In-depth analysis of SimCity as a cultural artifact
- The story of open sourcing SimCity
- Interviews with Will Wright and other game designers
- Research on Doreen Nelson's Design Based Learning
- Foundations of OLPC Micropolis educational version

See [simcity-multiplayer-micropolis.md](./simcity-multiplayer-micropolis.md) for the Micropolis story.

---

## See Also

- [sims-design-index.md](./sims-design-index.md) — Master index of Sims documents
- [sims-happy-friends-home.md](./sims-happy-friends-home.md) — Project X proposal (October 1996)
- [sims-maxis-requirements.md](./sims-maxis-requirements.md) — Seven Points of Sim (December 1996)
- [sims-find-best-action.md](./sims-find-best-action.md) — The advertising algorithm
- [sims-simantics-vm.md](./sims-simantics-vm.md) — Distributed behavior system
- [sims-team-history.md](./sims-team-history.md) — Lem, Cyberiad, Trurl
- [simcity-multiplayer-micropolis.md](./simcity-multiplayer-micropolis.md) — Micropolis and open source SimCity
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — Trurl's vision realized

---

## References

- **Video:** [Will Wright - Maxis - Interfacing to Microworlds (YouTube)](https://www.youtube.com/watch?v=...)
- **Don's Medium Article:** [Will Wright on Designing User Interfaces to Simulation Games (1996)](https://donhopkins.medium.com/designing-user-interfaces-to-simulation-games-bd7a9d81e62d)
- **Stanford Archive:** [searchworks.stanford.edu](https://searchworks.stanford.edu/view/yj113jt5999)
- **Chaim Gingold's PhD:** [Play Design (ProQuest)](https://search.proquest.com)
- **SimRefinery Recovery:** [The Obscuritory](https://obscuritory.com)
- **GDC 2001:** [Those Darned Sims: What Makes Them Tick?](https://www.gdcvault.com)

---

*"We're nowhere near building Trurl's invention, but I think to me that's kind of why I do a lot of this."*
— Will Wright, 1996

*We're getting closer.*
— MOOLLM, 2025
