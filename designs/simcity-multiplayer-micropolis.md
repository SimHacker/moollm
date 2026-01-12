# SimCity Multiplayer & Micropolis → MOOLLM

> *Collaborative Constructionist Education*
> *"SimCity is ideal for collaborative play, and constructionist education"* — Don Hopkins

## The Vision

SimCity isn't just a game — it's a platform for **constructionist education** as envisioned by Seymour Papert and Alan Kay. Don Hopkins developed multiple versions pushing this vision:

| Version | Year | Platform | Key Innovation |
|---------|------|----------|----------------|
| **SimCityNet** | 1993 | X11/Unix | Multiplayer collaboration, voting, chat |
| **OLPC Micropolis** | 2007-2008 | XO-1/Sugar | Educational, open source (GPLv3) |
| **Micropolis Web** | 2008+ | TurboGears/Flash | Server-based, browser client |
| **Micropolis WASM/Svelte** | Ongoing | Browser | Modern web stack |

---

## SimCityNet (1993): The First Multiplayer SimCity

Demonstrated at ACM InterCHI '93 in Amsterdam.

### Features

```
SimCityNet
├── Cooperative Multi-User Mode
│   ├── Multiple players, same city
│   ├── Shared money and resources
│   └── Consequences affect everyone
│
├── Communication Bridges
│   ├── Text chat (scrolling log)
│   ├── Networked audio (voice intercom)
│   └── Shared whiteboard overlay
│
├── Voting Dialogs
│   ├── Expensive items require votes
│   ├── Tax changes require consensus
│   └── Disasters require agreement
│
└── Multi-Platform
    ├── Sun SPARC workstations
    ├── SGI Indigo workstations
    └── NCD X Terminals
```

### The Social Layer

> "It's a cooperative game instead of a competitive game. We're all sharing the same money, trying to achieve the same goals. If somebody does something that pisses you off, you're going to be mad at them, and won't play with them. That will play out at a higher level than the game."

**MOOLLM Parallel:** The pub is a shared space. Characters share resources. Actions affect everyone. Social consequences emerge from gameplay.

### Voting Mechanics

```
Voting for Expensive Items:
1. Player proposes nuclear power plant
2. Dialog appears for all players
3. "Do you support the plan?" [Yes] [No]
4. Unanimous vote required
5. If vetoed, proposal fails

Voting for Tax Changes:
1. Player adjusts tax rate slider
2. "Continue with these figures?" appears
3. All players must agree
4. Budget only commits with consensus
```

**MOOLLM Parallel:** The [`party`](../skills/party/) skill implements voting. Group decisions require consensus. The stage performances need agreement.

---

## OLPC Micropolis: Constructionist Education

In 2007-2008, Don Hopkins adapted SimCity for the One Laptop Per Child project, eventually convincing Electronic Arts to release the source code under GPLv3.

### Core Philosophy

From Sugar user interface guidelines:

| Principle | SimCity Application | MOOLLM Application |
|-----------|--------------------|--------------------|
| **Activities, not Applications** | City building as activity | Sessions as activities |
| **Presence is Always Present** | Always-on collaboration | Characters always in rooms |
| **Tools of Expression** | Map annotation, storytelling | Session logs, essays |
| **Journaling** | Event history, checkpoints | Filesystem as save game |

### The Journaling Vision

```yaml
# The "Micropolis Journal" concept

newspaper_interface:
  sections:
    - generated_snapshots:
        source: simulator_events
        includes: [graphs, evaluation, statistics]
        
    - user_articles:
        source: player_written
        includes: [stories, opinions, reports]
        
    - event_stories:
        source: automatic_generation
        template: |
          Pollution levels dropped 15% this quarter,
          following the construction of new parks in
          the downtown district. Mayor {{player}}
          credits the "green initiative"...
          
  features:
    - live_links: "Click to jump into city at that moment"
    - branching_history: "What-if experiments"
    - embedded_maps: "Before/after overlays"
```

**MOOLLM Parallel:** 
- Session logs ARE the newspaper
- [`marathon-session.md`](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) is a living journal
- Palm's essays are player-written content
- Events generate narrative opportunities

---

## Alan Kay's Critique and Vision

Alan Kay provided crucial feedback that shaped MOOLLM's design philosophy:

### The Problem with Black Boxes

> "My main complaint about this game has always been the rigidity, and sometimes stupidity, of its assumptions (counter crime with more police stations) and the opaqueness of its mechanism (children can't find out what its actual assumptions are, see what they look like, or change them to try other systems dynamics)."

> "I have used SimCity as an example of an anti-ed environment despite all the awards it has won. It's kind of an air-guitar environment."

### The Solution: Open the Hood

> "Going to Python can help a few areas of this, but a better abstraction for the heart of SimCity would be a way to show its rules/heuristics in a readable and writable form."

**MOOLLM Response:**

```yaml
# MOOLLM's skills ARE the rules, readable and writable

# skills/needs/SKILL.md - the "assumptions" are visible
decay_patterns:
  hunger:
    rate: moderate
    satisfied_by: eating
    # You can SEE this, CHANGE this
    
# skills/action-queue/SKILL.md - the "mechanism" is documented
find_best_action:
  algorithm: |
    1. Scan all available interactions
    2. Score by motive advertisements
    3. Attenuate by distance
    4. Choose highest scoring
    # Visible. Editable. Understandable.
```

### Robot Odyssey: Alan Kay's Favorite Game

> "Robot Odyssey... I thought was a brilliant concept when the TLC people brought it to me at Atari in the early 80s. The big problem with Robot Odyssey was that the circuits-programming didn't scale to the game. They really needed to move to something like an object-oriented event-driven Logo with symbolic scripting."

**MOOLLM Response:** Skills ARE the symbolic scripting language. Characters ARE programmable robots. The LLM IS the interpreter that scales.

---

## The Web Version: Server + Browser

### Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Web Browser                      │
│  ┌─────────────────────────────────────────────┐    │
│  │       OpenLaszlo/Flash Client               │    │
│  │  - Tile display                             │    │
│  │  - Pie menus                                │    │
│  │  - Chat interface                           │    │
│  │  - Map overlays                             │    │
│  └─────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────┘
                         │ AMF (binary JSON for Flash)
                         │ HTTP
                         ▼
┌─────────────────────────────────────────────────────┐
│                 Python Web Server                   │
│  ┌─────────────────────────────────────────────┐    │
│  │          TurboGears Framework               │    │
│  │  - Session management                       │    │
│  │  - User accounts                            │    │
│  │  - City storage                             │    │
│  │  - Chat/messaging                           │    │
│  └─────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────┐    │
│  │          SWIG Python Bindings               │    │
│  └─────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────┐    │
│  │        C++ MicropolisEngine                 │    │
│  │  - Simulation core                          │    │
│  │  - Tile engine                              │    │
│  │  - Sprite engine                            │    │
│  └─────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

**MOOLLM Parallel:** This is exactly the architecture MOOLLM uses:
- Browser client (could be Svelte)
- Python/LLM server
- YAML/filesystem as the simulation state
- Skills as the engine

### Plugin Robots: PacBot

Don created plugin agents — programmable characters:

```python
# PacBot: A plugin agent that eats traffic
class PacBot(Agent):
    """
    PacBot follows roads looking for traffic.
    When it finds traffic, it eats it.
    This reduces pollution and raises PacBot's score.
    """
    
    def find_best_action(self):
        # Look at current tile
        traffic = self.sense_traffic()
        
        if traffic > 0:
            return self.eat_traffic()
        else:
            return self.follow_road()
```

**MOOLLM Parallel:** 
- Characters ARE programmable agents
- Cats prowl and mark territory
- Dogs scare grues
- The LLM interprets behavior descriptions

---

## Visual Programming Vision

The long-term goal was always to enable visual programming:

### Logo Turtles + SimCity

```yaml
# Collapse editing tools and agents

editing_agents:
  bulldozer:
    type: vehicle
    control: [keyboard, gamepad, mouse]
    behavior: "Drive around, crush things in wake"
    
  road_builder:
    type: vehicle
    control: [directional, gestural]
    behavior: "Move and lay road automatically"
    
  development_bot:
    type: programmable_robot
    behavior: |
      Lay out entire subdivisions:
      zones, roads, parks, wires
      Can be visually programmed
```

### Robot Odyssey Style

```yaml
# Open a monster, see its program

monster_behavior:
  interface:
    sensors:
      - current_tile
      - adjacent_tiles
      - nearest_building
    actuators:
      - move_direction
      - destroy_tile
      - roar
      
  visual_program:
    # Kids can rewire this
    - if: building_nearby
      then: move_toward_building
    - if: on_building
      then: destroy_tile
    - else: random_walk
```

**MOOLLM Parallel:** Skills ARE the visual program, but in prose:

```markdown
## skills/monster/SKILL.md

### MONSTER-BEHAVIOR

When the monster acts:
1. **Sense** — Look for nearby buildings
2. **Move** — Head toward the largest structure
3. **Destroy** — Crush anything underfoot
4. **Roar** — Occasionally terrify citizens

The monster can be reprogrammed by editing this skill.
```

---

## Educational Applications

### Teaching Democracy

```yaml
voting_curriculum:
  concepts:
    - proposal_writing: "Convince others to support your idea"
    - campaigning: "Build coalition before the vote"
    - compromise: "Find common ground"
    - consequences: "Live with group decisions"
    
  activities:
    - propose_stadium: "Write why the city needs it"
    - debate_taxes: "Argue for your position"
    - vote_on_disaster: "Collective responsibility"
```

### Teaching Language Skills

```yaml
creative_writing:
  newspaper_articles:
    - report_on_fire: "Describe the disaster"
    - interview_mayor: "Quote the player's decisions"
    - editorial: "Argue for policy change"
    
  journaling:
    - city_history: "Chronicle the timeline"
    - what_if: "Explore alternative decisions"
    - future_vision: "Plan and persuade"
```

**MOOLLM Parallel:** 
- Palm writes philosophical essays
- Session logs capture narrative
- Characters debate and vote
- Language IS the interface

---

## The Open Sourcing Story

Chaim Gingold tells the dramatic story in his PhD thesis *Play Design*:

> "Will Wright and I eventually talked them [EA] into actually making it open source in 2008."

Key arguments:
1. **Educational value** — Constructionist learning platform
2. **OLPC mission** — Reaching children worldwide
3. **Legacy preservation** — Classic game lives on
4. **Community benefit** — Enables modification and study

**MOOLLM Parallel:** MOOLLM is open source from day one. The philosophy is baked in, not retrofitted.

---

## Social Networking Vision

Mock-ups from 2009 showed SimCity embedded in social networks:

### Identity and Presence

```yaml
facebook_integration:
  identity:
    - real_names: "Connected to social graph"
    - friends: "Play with people you know"
    - history: "Your cities, your stories"
    
  features:
    - vote_from_wall: "Participate without opening game"
    - share_cities: "Publishing to friends"
    - slow_game: "Week-long collaborative sessions"
```

### The Wall as Voting Interface

> "Slow the game down a lot, so your Facebook wall will let your friends vote on things."

**MOOLLM Parallel:** 
- The pub guest book IS social persistence
- Characters can be summoned from the guest book
- Sessions can span days with async participation

---

## Technology Evolution

| Era | Server | Client | Notes |
|-----|--------|--------|-------|
| 1993 | X11 | X11 | Direct window system |
| 2007 | Python/GTK | X11/Cairo | OLPC Sugar |
| 2008 | TurboGears | OpenLaszlo/Flash | Web-based |
| Future | Python/LLM | WASM/Svelte | Modern web |

**MOOLLM Today:**
- Server: LLM (Claude, etc.)
- Client: Cursor IDE, browser, any text interface
- State: YAML files in filesystem
- Network: Git + collaboration tools

---

## Key Lessons for MOOLLM

### From SimCityNet

1. **Cooperation over competition** — Shared resources, shared consequences
2. **Voting for expensive actions** — Group decisions on major changes
3. **Multiple communication channels** — Text, overlay, presence

### From OLPC Micropolis

1. **Activities, not applications** — Sessions, not programs
2. **Journaling everything** — Filesystem IS the journal
3. **Tools of expression** — Writing as primary interface

### From Alan Kay

1. **Open the hood** — All rules visible and editable
2. **Symbolic scripting** — Skills as readable programs
3. **Scalable programming** — LLM handles complexity

### From Visual Programming Vision

1. **Agents as tools** — Characters carry capabilities
2. **Behavior as prose** — Skills describe action
3. **Plug-in architecture** — Extensible by design

---

## References

### Don Hopkins' Micropolis Materials

- [Micropolis GitHub Repository](https://github.com/SimHacker/micropolis)
- [PLAN.txt](https://github.com/SimHacker/micropolis/blob/master/micropolis-activity/PLAN.txt) — Development roadmap
- [OLPC-Notes.txt](https://github.com/SimHacker/micropolis/blob/master/MicropolisCore/OLPC-Notes.txt) — Sugar integration notes
- [TurboGears server](https://github.com/SimHacker/micropolis/blob/master/turbogears/) — Web server code
- [OpenLaszlo client](https://github.com/SimHacker/micropolis/blob/master/laszlo/) — Flash client code

### Videos

- [Multi Player SimCityNet for X11 on Linux](https://www.youtube.com/watch?v=_fVl4dGwUrA)
- [Micropolis Online Web Demo](https://www.youtube.com/watch?v=8snnqQSI0GE)
- [HAR 2009 Lightning Talk](https://donhopkins.medium.com/har-2009-lightning-talk-transcript-constructionist-educational-open-source-simcity-ec5f7d85ae50)

### Historical Documents

- [SimCityNet at InterCHI '93](http://www.art.net/~hopkins/Don/simcity/simcitynet.html)
- [Multi Player SimCity Announcement](http://www.art.net/~hopkins/Don/simcity/simcity-announcement.txt)
- [Educational SimCity for Linux Proposal (2002)](https://web.archive.org/web/20110611185928/http://www.donhopkins.com/drupal/node/24)
- [Open Sourcing SimCity](https://donhopkins.medium.com/open-sourcing-simcity-58470a27063e) — Chaim Gingold's account

### Related Projects

- [Snap!](https://snap.berkeley.edu/) — Visual programming by Jens Mönig
- [Sugar](https://sugarlabs.org/) — OLPC learning platform
- [Robot Odyssey](https://en.wikipedia.org/wiki/Robot_Odyssey) — Warren Robinett's classic

---

## Historical Correspondence

### Will Wright's Endorsement (December 2006)

The open-sourcing of SimCity began with this email from Will Wright:

> **From:** Will Wright  
> **To:** Rod Humble, Scott Evans, Don Hopkins  
> **Subject:** Fwd: Sim City in open source for $100 Laptop?  
> **Date:** Friday, December 01, 2006
>
> *"Rod, Scott, Don — I'd really like to see this happen, it seems like a very worthwhile project at no risk to us. Please let me know what I can do to move it forward if it hits a snag."*
> 
> —Will Wright

**MOOLLM Parallel:** Will's approach — enable experimentation at no risk — mirrors MOOLLM's permissive prototyping. Skill experiments cost nothing but imagination.

---

### Walter Bender Correspondence (December 2006)

Planning discussions with Walter Bender (OLPC co-founder):

> *"Since I've been working on this project a long time, I have a bunch of old ideas and notes about stuff I'd love to do with SimCity, a lot of which is much easier to do now that the technology has matured."*

Key planning points:
- **Journaling/Storytelling** as primary educational angle
- **The Sims Exchange** as model for player publishing
- **"Massively Single-Player"** games concept from Spore
- **Original SimCity simplicity** — "rang like a bell"

> *"I think the original version of SimCity rang like a bell, and has this wonderful approachable simplicity that was lost in the later more advanced versions. I've been careful not to do anything that breaks the original algorithms and game play."*

**MOOLLM Parallel:** The commitment to not breaking what works. Skills extend the framework without modifying its core philosophy.

---

### The Sims Exchange Inspiration

> *"Please check out what The Sims Exchange has done by enabling players to publish Family Albums (players take in-game screen snapshots, write stories in their Family Albums, and publish them on the web, along with save files that other players can download and play with)."*

This pattern directly influenced MOOLLM's session logs:

| The Sims Exchange | MOOLLM Sessions |
|-------------------|-----------------|
| Family Albums | Session logs |
| Screenshots | YAML snapshots |
| Stories | Narrative prose |
| Save files | Git history |
| Web publishing | GitHub/sharing |

---

### Key Collaborators & Contacts (Historical)

People Don reached out to for the OLPC project:

| Person | Affiliation | Relevance to MOOLLM |
|--------|-------------|---------------------|
| **Mike Perry** | Maxis | SimCity ActiveX control, practical API design |
| **Ted Selker** | MIT Media Lab | OLPC involvement, demonstrated multi-player to sponsors |
| **Upmanu Lall** | Columbia Earth Science | Educational simulation, experiment design |
| **Eric Scharff** | UCAR | Open source software PhD, simulation uses |
| **Doreen Nelson** | Maxis | Curriculum guides for teachers |
| **Alan Kay** | OLPC/MIT/UCLA | OOP inventor, constructionist education vision |

---

### Sugar Integration Design Notes

Detailed mapping of Sugar UI principles to SimCity:

```
Sugar Human Interface Guidelines → SimCity/MOOLLM

Activities, not Applications
├── SimCity: "Building and playing with a city"
└── MOOLLM: Sessions as activities, not programs

Presence is Always Present
├── SimCity: SimPolitics interpersonal layer
├── MOOLLM: Characters always in rooms
└── Exchange: "Send friends a link to your city"

Tools of Expression
├── SimCity: Creative expression, critique, iteration
└── MOOLLM: Session logs, essays, rich linking

Journaling
├── SimCity: Chronicle all activities
├── Events: Script writers handle and respond
└── MOOLLM: Filesystem IS the journal

Recoverability
├── SimCity: Checkpoint, rewind, replay edits
└── MOOLLM: Git history, working sets

Zoom Metaphor
├── Neighborhood → Friends → Home → Activity
└── MOOLLM: Repository → Examples → Adventure → Room
```

---

### The Frame Interface Design

Don's notes on applying Sugar's frame interface:

```
Frame Organization for SimCity:

TOP EDGE: Places
├── Cities on the mesh
├── Map locations
└── Named checkpoints

BOTTOM EDGE: Actions
├── Editing tools
├── Control panels
└── Notifications

LEFT EDGE: Objects
├── Buildings palette
├── Saved cities
└── Templates

RIGHT EDGE: People
├── Other players
├── Collaboration tools
└── Publishing interface
```

**MOOLLM Parallel:**
- Top: Directories (places)
- Bottom: Skills (actions)
- Left: Files (objects)
- Right: Characters (people)

---

### Network City Sharing: "What-If?" Trees

Revolutionary design for branching histories:

```yaml
# The What-If History Tree Concept

branching_history:
  description: |
    Multiple players build a tree of saved cities with 
    branching alternate histories. Like the parallel 
    universes in Niven's "All the Myriad Ways."

  operations:
    - checkpoint: Save current state
    - branch: Create alternate timeline
    - rewind: Go back up the tree
    - select: Choose different branch
    - playback: Replay edit-by-edit
    - takeover: Branch at any playback point

  collaboration_pattern: |
    When you play together in the same city, you have to 
    discuss and agree with other players about what to do.
    
    You can try an idea yourself by branching a private history,
    giving your idea a try, and reporting back to other players
    in the main shared timeline with links so they can see.

  gui: "Branching history tree outline viewer of saved files"
```

**MOOLLM Parallel:**
- Git branches as alternate timelines
- Session logs as playback
- "Speed of light" simulation explores many paths
- Each session can fork at any decision point

---

### Newspaper/Publishing Metaphor

Detailed design for the print/publish interface:

```yaml
newspaper_interface:
  print_dialog:
    metaphor: "Newspaper printing and publishing"
    
    outputs:
      - newspaper: In-game publication
      - paper: Physical print
      - disk: Save to file
      - clipboard: Copy
      - journal: Add to log
      - blog: Web publish
      
    content:
      - city_snapshot: Optional saved state link
      - text_entry: Blog-like commentary
      - map_views: Any overlay, chalk drawings
      - graphs: Evaluation, statistics
      - chat_log: Excerpts from discussions
      
  reporter_role: |
    A player could be a "reporter" interviewing other player 
    politicians via chat, before and after the vote on building 
    a stadium, asking them to make their case for or against,
    and publish in the "SimCity Journal."
    
  network_features:
    - browse_newspapers: Read others' publications
    - download_cities: Play cities from stories
    - story_links: "Flash: Monster invades SimCity, near reactor!"
```

**MOOLLM Parallel:**
- Session logs AS newspapers
- Characters as reporters
- Debates with voting (pie table)
- Palm's essays as player publications

---

### Geo-Blogging and OPML

Advanced overlay design using standard formats:

```yaml
geo_coded_opml:
  description: |
    Store city overlay information in OPML.
    Register map corners with real-world lat/long.
    Associate OPML nodes with map features.
    
  node_attachments:
    - names: "Name zones, buildings, neighborhoods"
    - notes: "Take notes about features"
    - pictures: "Attach images"
    - stories: "Write narratives"
    - links: "Connect to other nodes"
    
  signs_on_map:
    description: "Like SimCity 2000 signs"
    representation: OPML node
    contents: "Arbitrary OPML outlines with links"
    example: |
      Sign at crossroad → links to:
      - Road A node
      - Road B node
      - Regions each road leads to
      
  output: "Use OPML to write a city guide"
```

**MOOLLM Parallel:**
- `ROOM.yml` files as geo-coded nodes
- Exits as crossroad links
- Room descriptions as city guides
- YAML Jazz comments as annotations

---

### Scriptability Vision

From Don's notes on why scriptability matters:

> *"One of the most interesting and powerful aspects of this version of SimCity is that it has a built-in scripting language (TCL/Tk). Scriptable SimCity opens up a huge range of possibilities."*

Educational uses envisioned:

1. **Configure experiments** — Set up controlled conditions
2. **Run simulations** — Execute systematically
3. **Collect data** — Log all variables
4. **Export to spreadsheets** — Analyze with other tools
5. **Stimulate discussion** — Results provoke questions
6. **Understand systems** — Learn complex dynamics

**MOOLLM Parallel:**
- Skills as scriptable behaviors
- Session logs as experiment records
- YAML export for analysis
- LLM as the interpreter

---

### Performance & Real-Time Play

Don's UI innovations for high-speed simulation:

```yaml
high_speed_ui:
  # Running 1000 years/minute on 500MHz laptop!
  
  gestural_pie_menus:
    benefit: "Quick tool switching without moving to palette"
    style: "Real-time twitch game"
    
  blurred_display:
    what: "Year/month display blurs lower digits when fast"
    why: "Don't update screen every month"
    
  live_tax_dialog:
    behavior: "Doesn't pause game"
    interaction: "Drag taxes, watch buildings rise/fall in real time"
    
  transparent_overlays:
    feature: "Multiple map windows with different overlays"
    benefit: "Compare data while editing"
    
  live_notice_maps:
    content: "Problem notices include live map view"
    action: "Click to scroll main map there"
```

> *"When it's running so fast, it's extremely important to keep your fire department fully funded, because fires can spread through the whole city in the blink of an eye!"*

**MOOLLM Parallel:** Speed of light simulation — 33 turns in one call. Real-time response. Multiple views on same data.

---

### Don's First Reaction to SimCity (1989)

Posted to comp.theory.cell-automata at 5:37 AM after playing all night:

> *"I just got a chance to play SimCity! It's like a drawing program that lets you build cities... The simulation is actually running WHILE you're constructing it! It acts like cellular automata with very high level rules..."*
>
> *"Districts that you've zoned don't come online and start developing until they're hooked into the power grid, by being connected through power line cells or adjacent buildings. Buildings seem to 'feed' off of people brought in by roads and railroads..."*
>
> *"Once you build an airport, a helicopter flies around the city and reports on heavy traffic, encouraging you to redesign the roads in that area!"*
>
> *"You may wonder what traffic copters have to do with cellular automata. You just have to play it yourself to understand."*
>
> *"SimCity is absolutely the most amazing game I've seen on the Macintosh to date! The graphics and animation are beautiful. I'll leave it at that — mere text cannot do it justice."*
>
> — Don Hopkins, December 26, 1989, 5:37 AM

**MOOLLM Connection:** This early-morning wonder led to 35+ years of development, from SimCityNet to The Sims to MOOLLM. The same sense of "it's actually running WHILE you're constructing it" applies to MOOLLM's live sessions.

---

### The Micropolis Vision (2014)

What Don wanted to accomplish with the web-based Micropolis:

**Core Goal:**
> *"Faithfully reconstruct the original game experience in the web browser as free open software written in JavaScript, that runs on or offline, and has a few improvements. And to build a web site where the community can gather together, share their content, debate in their forums, document in their wikis, and build and explore each other's cities on the map of their Earth."*

**Stretch Goals:**
1. Open up the game, modularize and document it
2. Enable modders to create content: buildings, scenarios, disasters, vehicles, monsters
3. 3D visualization with Minecraft/Lego-style building tools
4. Scale into social, collaborative, democratic multi-player
5. Fully develop educational potential via Piaget, Papert, Kay, Nelson, Lall

**Technology Stack (2014):**
JavaScript, HTML5, Canvas, WebGL, WebRTC, Node.js, GitHub

**MOOLLM Today:** The same vision, but with LLMs as the interpreter instead of JavaScript. YAML instead of JSON. Prose instead of code. The "community gathering place" is now the pub; the "cities" are adventures; the "modding" is skill creation.

---

### On Appreciation and Support

This project represents significant personal investment — time, energy, money, and decades of accumulated knowledge. The work speaks for itself. It's not built for profit but for the joy of creation and the hope that it advances human-computer interaction.

If you find value in these ideas, the best support is:
- **Using them** — Fork the repo, run your own adventures
- **Extending them** — Write skills, create characters, build worlds
- **Sharing them** — Tell others who might benefit
- **Contributing** — Patreon donations, institutional support

> *"For the past 35 years, this simulated city has been my home, school and work."*
> — Don Hopkins

---

## The Sims Team & Legacy

For the colorful history of The Sims team, BBC documentary correspondence, ethical frameworks, and the books that shaped the game, see:

**→ [sims-team-history.md](./sims-team-history.md)**

Includes:
- The path from SimCity to The Sims (1989-2000)
- The naming saga (DH → AFA → TDS → "The Sims")
- Full team credits with nicknames
- The books that made The Sims (McCloud, Lem, PKD)
- BBC Documentary (2025)
- Ben Shneiderman's wisdom
- Early experiments and lessons in representation ethics

---

## See Also

- [sims-team-history.md](./sims-team-history.md) — The Sims team, BBC documentary, ethical lessons
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#simcity-the-sims-and-the-simulator-effect) — SimCity in context
- [sims-design-index.md](./sims-design-index.md) — All Sims influences
- [sims-pie-menus.md](./sims-pie-menus.md) — Pie menu interfaces
- [don-hopkins-projects.md](./don-hopkins-projects.md) — Full project lineage
- [skills/party/](../skills/party/) — Voting and group decisions
- [skills/speed-of-light/](../skills/speed-of-light/) — Fast simulation
- [skills/session-log/](../skills/session-log/) — Journaling activities

---

*"One of the most wonderful possibilities about this venture is that it will bring together very fluent designers from many worlds of computing in the service of the children. We should really try to pull this off!"* — Alan Kay

*"I'd really like to see this happen, it seems like a very worthwhile project at no risk to us."* — Will Wright
