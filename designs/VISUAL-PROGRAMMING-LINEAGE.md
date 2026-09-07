# Visual Programming Lineage: From Smalltalk to MOOLLM

A trail of ideas connecting constructionist education, visual programming,
character simulation, and modern LLM orchestration.

## The Thread

### 1960s: Pioneers

**Sketchpad** (Ivan Sutherland, MIT, 1963)
- First graphical user interface
- Direct manipulation of geometric objects
- Constraint-based graphics

**NLS/oNLine System** (Douglas Engelbart, SRI, 1968)
- The Mother of All Demos
- Collaborative editing, hypertext, windows
- Human augmentation through computing

**PIXIE** (Neil Wiseman, Heinz Lemke, John Hiles, Cambridge, 1969)
- "A New Approach to Graphical Man-Machine Communication"
- Light pen interaction with structured graphics
- CAD Conference Southampton, IEEE Publication 51
- [PIXIE Paper](https://www.donhopkins.com/home/documents/pixie.pdf)
- [Flight of the PIXIE (video remix)](https://www.youtube.com/watch?v=jDrqR9XssJI)

### 1970s-80s: Foundations

**Smalltalk** (Alan Kay, Xerox PARC)
- Objects all the way down
- Live editing environment
- Kids as target audience

**Logo** (Seymour Papert, MIT)
- Microworlds for learning
- Turtles as thinking tools
- "Learning by making"

**HyperCard** (Bill Atkinson, Apple)
- Stacks and cards metaphor
- Direct manipulation editing
- Scripting for everyone (HyperTalk)

### 1980s-90s: NeWS Era

**NeWS** (James Gosling, Sun)
- PostScript as code, graphics, AND data
- Networked extensible window system
- Architecturally similar to what became AJAX

**HyperLook** (Arthur van Hoff, Turing Institute)
- HyperCard for NeWS
- PostScript scripting
- Property sheets as editable stacks
- [HyperLook Article](https://medium.com/@donhopkins/hyperlook-nee-hypernews-nee-g...)

**PSIBER Space Deck** (Don Hopkins)
- Visual PostScript debugging
- "Consensual hallucination" of data structures
- [PSIBER Space](https://donhopkins.medium.com/the-shape-of-psiber-space-oct...)

### 1990s: Interval Research Era

At Interval Research Corporation (Paul Allen's "PARC for the 90s"),
several threads converged:

**Hookup → Body Electric → Bounce** (David Levitt)

One continuous dataflow language across three decades and three industries —
MIDI, then virtual reality, then components — carried by the same designer. **The
most direct answer in this file to the claim that visual programming never
shipped anything real:** Body Electric drove commercial VR systems, live, on
stage.

- Hookup: Atari Cambridge/MIT Media Lab era, MIDI visual programming
- Body Electric: VPL Research, inherited MMP (Macromedia Director player)
- VR integration: Flock of Birds, Polhemus, DataGlove, Convolvotron
- Swivel3D articulated trees for bodies, hands, gesture recognition
- Broadcast positions via UDP to TWO SGI workstations (one per eye!)
- Jaron Lanier performed with VR musical instruments live
- Bounce: David's post-VPL version at Levity, Don Hopkins did UI
- COM/ActiveX integration: new wire types for JSON-like nested data
- Solved six-input-limit with polymorphic dictionary objects
- Don ported Bounce to PowerPC Mac and built a cross-platform plug-in
  architecture on COM, porting the ActiveX Template Library to the Mac to do it

**The lesson is the one worth carrying forward, because it is a negative
result stated by the people who built the thing:** *pure* dataflow becomes
unwieldy once complex state is involved, and the fix was to let opaque
objects — COM components — sit inside the graph and hold state, with richer wire
types to carry nested data between them.

That is the same shape as the resolution in
[AXES-NOT-CAMPS.md](./AXES-NOT-CAMPS.md): not one mechanism winning, but a
visual layer for the connections and a symbolic layer for the state, each doing
what it is good at. A patch graph is a beautiful way to express *flow* and a bad
way to express *memory*.

Note also the pairing with Lanier's augmentation/automation axis — the same
Jaron Lanier, performing music with a dataflow language, is the person whose
review supplies that axis. The instrument was augmentation, literally.

**MediaFlow** (Marc Davis)
- Visual programming for video processing
- Semantic annotation (before AI vision)
- "Professional video by hobbyists with camcorders"
- [MediaFlow Design Discussion](https://donhopkins.com/home/interval/mediaflow-design.html)

**Embedded Constraint Graphics** (Tom Ngo)
- Create interactive graphics from target examples
- Interpolate between states on simplicial complexes
- Patent US5933150

**Component Technology Survey** (Don Hopkins)
- [Pluggers Survey](https://donhopkins.com/home/interval/pluggers) — snapshot of 1996
- [IFC vs Bongo](https://donhopkins.com/home/interval/ifc-vs-bongo.html) — Java frameworks compared

Key insight from Richard Gabriel's *Patterns of Software*:
> "Data and control abstractions are generally best when they are codesigned,
> and this is rarely done any more."

### 1996-2000: The Sims Era

**SimAntics** (Maxis/EA) — the visual programming language the characters run on.
The name is a pun on *semantics*, and it is the most widely deployed visual
programming language in this whole lineage: it shipped inside a game that sold
in the tens of millions, and players edited it.

- Character simulation visual programming language
- Simple local rules → complex global behavior
- Players as authors, not just consumers

**It did not start with The Sims — it came from SimCopter, and that matters for
this document.** SimAntics is a link in a chain rather than a one-off:

> "Edith lets you view and edit SimAntics code, which is the visual programming
> language for scripting the behavior of The Sims. […] The SymAntics [sic]
> language was used to program the people in SimCopter, and Edith evolved out of
> that."
> — Don Hopkins, SimWatch list, 2000-08-26

`verified: recovered primary source; text and provenance in
[sims/MEDIUM-RESCUE.md](./sims/MEDIUM-RESCUE.md). The email uses the early
"SymAntics" variant; the established spelling is SimAntics.`

So the sequence is **SimCopter people → SimAntics → The Sims**, with the editor
evolving alongside the language rather than being bolted on after.

**Edith** — the editor, and the reason this belongs in a *lineage* rather than a
catalogue. Named for Edith Bunker, the first mother Sim, and doubling as "EDIT
House." It was compiled *into* The Sims rather than shipped alongside it, and
the payoff is the property every environment-side language in this document is
chasing:

> "Edith has grown a lot and is much wiser, now that she's integrated into The
> Sims instead of running as a separate program, so she is actually able to
> **debug and edit code and data while it's running live in the game**."

That is the Smalltalk image property, reached by a commercial game studio for
production reasons. It also cost what liveness always costs: Edith was never
publicly released, and the blocker was *documentation*. See
[AXES-NOT-CAMPS.md](./AXES-NOT-CAMPS.md) on the notation-side/environment-side
trade this exemplifies.

**Why that much effort for a language with four users.** Early on, SimAntics had
Jamie Doornbos writing it, Don porting it to Windows and making it easier to
use, Patrick J Barrett III using it heavily and making it "much more colorful,"
and Will Wright as the only other user. The investment is not justified by user
count — **it is justified by whose iteration cost you are lowering.** Wright is
rare enough that making his loop faster changes what gets designed, so tooling
spent on one designer's throughput can return more than tooling spread across
thousands. This is the strongest case in this whole file for visual programming
as a *leverage* technology rather than a mass-adoption one, and it is the
opposite of how the field usually argues for it.

Will Wright's progression:
- SimAnt: Too simple
- SimEarth: Too complex  
- SimCity 2000: Just right
- The Sims: EVEN SWEETER — simple for kids, complex for artists

Don's contributions:
- SimAntics documentation and cleanup
- Mac to Windows UI rewrite
- Pie menu interaction system
- Extensive testing and exploration

**User-Created Content Tools** (Don Hopkins, Maxis/EA)
- SimShow: Pre-release tool for character skins — fans hit ground running
- Transmogrifier (TMog): OLE component for custom objects without 3D Studio
  — <https://thesimstransmogrifier.com/>
- rug-o-matic: Template + drag-drop = storytelling "rugs" (title+description+image)
- Fan communities (Yahoo Groups, personal blogs) = social currency economy
- Heather "SimFreaks" + Steve "SimSlice" met in fandom, got married!

### 2000s-2010s: Constructionist Platforms

**Scratch** (Mitchel Resnick, MIT Media Lab)
- Block-based visual programming
- Seymour Papert's constructionism realized
- Millions of young programmers

**Snap!** (Brian Harvey, Jens Mönig)
- First-class procedures and data
- Build Your Own Blocks
- Connects to Berkeley CS curriculum

### 2020s: MOOLLM

MOOLLM synthesizes these threads:

**From Self's Prototype OOP:**
- "OOP RISC microcode" — so simple you can build other OOP systems in it:
  - Instance/class (Smalltalk)
  - Morphic composition
  - CLOS generic dispatch
  - HyperCard delegation
  - **COM IUnknown / OLE IDispatch**
- Multiple interfaces per directory (ROOM+CHARACTER, SKILL+CHARACTER, etc.)
- Battle-tested patterns, extremely well represented in training data
- Solves real problems: discovery, versioning, extension points, aggregation instead of inheritance
- Dovetails with the other interlocking object systems
- Just another way of looking at directories full of files
- The ground truth multiverse lives in GitHub

**From COM/OLE (Microsoft) → MOOM/MOOLE:**
- IUnknown: "QueryInterface" = check if directory has ROOM.yml, CHARACTER.yml, etc.
- Multiple interfaces sharing state: one directory, many .yml schemas
- **CARD.yml is like IDispatch** — advertisements + interface definitions for 
  high-level polymorphic dispatch, automatically binding parameters from context,
  natural language triggers, skill composition, K-line activation
- IDispatch: late-bound method invocation = LLM interpretation of affordances
- Aggregation instead of inheritance: tear-off interfaces, other cool tricks
- See: [DIRECTORY-AS-IUNKNOWN.md](DIRECTORY-AS-IUNKNOWN.md)

**From Minsky's Society of Mind:**
- Debating experts, not single-voice averaging
- K-lines as tradition activation
- NO-AI-* suite prevents pathologies

**From constructionism:**
- Microworlds for exploration
- Learning by building
- Students as researchers

**From The Sims:**
- Character simulation with emergent behavior
- Speed-of-light: 8 characters × 99 turns in ONE call
- Memory + reflection + planning (realized with LLMs)

**From GitHub as MMORPG:**
- Social collaboration features as game mechanics
- Characters as bots in discussions, reviews, flame wars
- Branches as parallel universes

**Layered Multi-Paradigm Integrated Object Systems:**

All seamlessly interoperating together — ALL WELL DEFINED IN TRAINING DATA:

| System | Contribution |
|--------|--------------|
| Self | Prototype OOP as RISC microcode |
| Morphic | Composition, direct manipulation |
| Dan Ingalls' Lively Kernel | Web-native Morphic |
| Smalltalk | Message passing, everything is an object |
| Python, JavaScript, TypeScript | Modern dynamic languages |
| NeWS/PostScript | Code as data as graphics |
| HyperCard/HyperTalk | Almost natural language scripting |
| C++ | Multiple inheritance → multiple vtables |
| Objective-C | Message forwarding, categories |
| COM/OLE → MOOM/MOOLE | IUnknown, IDispatch, aggregation |
| ScriptX/CLOS | Generic functions, multiple dispatch |
| LispM Flavors | Mixins, method combination |
| Simula | Original OOP, simulation focus |
| Actors | Message passing concurrency |

**Reactive Programming & Constraint Systems:**

| System | Type | Contribution |
|--------|------|--------------|
| **Svelte 5 Runes** | Push | Compiler-driven fine-grained reactivity. Fucking awesome! |
| OpenLaszlo | Push | Declarative constraints compiled to Flash, worked with Henry Minsky |
| Garnet (Brad Myers, CMU) | Pull | Built on KR (Knowledge Representation) Lisp frames library. **Structural inheritance** — see [GARNET-AMULET-PROTOTYPE-SYSTEM.md](GARNET-AMULET-PROTOTYPE-SYSTEM.md) |
| React | (barely) | Virtual DOM diffing, NOT as reactive as its name claims |

**Push vs Pull Constraints:**

- **OpenLaszlo (Push/Eager):** When source changes, propagate immediately.
  Better for responsive UIs in Flash/ActionScript runtime.
  Don worked there with Henry Minsky and other MIT Lisp hackers.
  
- **Garnet (Pull/Lazy):** Compute only when value is requested.
  Better for high-latency environments (X11 round trips).
  Don worked on this with Brad Myers at CMU.
  Built on KR (Knowledge Representation) — Lisp GOFAI frames library.
  
- **Svelte 5 Runes:** Best of both worlds via compiler magic!
  `$state` = reactive source, `$derived` = computed value,
  `$effect` = side effects. Business logic AND UI can be reactive!

We're using **SvelteKit** for our web stack. Delightful to use, great community.
Not as well represented in training data as React (SO popular), but
Svelte has a pretty big dedicated community — not such an underdog.

**Instance Substitution Principle** (Oliver Steele at Laszlo Systems):
An instance can be replaced by its inline definition, and vice versa.
This enables **Instance-First Development**: build specific, then generalize.
Svelte components embody this — refactoring inline to component is trivial.

See: `MicropolisCore/laszlo/micropolis/README.md` — long essay comparing
OpenLaszlo/Garnet constraints to Svelte 5 runes.

## The Connection to Generative Agents

The Stanford Generative Agents paper (Park et al., 2023) finally builds
what we designed in 1997 but couldn't implement without LLMs:

| The Sims (1997) | Generative Agents (2023) |
|-----------------|--------------------------|
| Motive tracking | Reflection mechanism |
| Social relationships | Memory streams |
| Activity scheduling | Planning architecture |
| Emergent behavior | Valentine's Day party |

MOOLLM extends this with:
- Multiple debating perspectives (not averaged)
- GitHub as persistent world state
- Composable Anthropic skills
- Real-world AIOps applications

## Resources

- [Stanford Generative Agents Welcome](STANFORD-GENERATIVE-AGENTS-WELCOME.md)
- [MOOLLM Skills Index](../skills/INDEX.yml)
- [The X-Windows Disaster](https://donhopkins.medium.com/the-x-windows-disaster-128d398...)
- [Designing User Interfaces to Simulation Games](https://donhopkins.medium.com/designing-user-interfaces-to-simulation-games-bd7a9d81e62d)

---

*This document traces the intellectual lineage from Papert and Kay through
The Sims to modern LLM-based agents. The thread is continuous: microworlds,
direct manipulation, character simulation, constructionist learning.*
