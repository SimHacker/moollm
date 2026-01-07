# Incarnate: The MOOLLM Framework

> *Skills are programs. The LLM is `eval()`. Empathy is the interface.*
> *Code. Graphics. Data. One interpreter. Many languages. The Axis of Eval.*

---

## The Word

**Eval Incarnate** = `eval()` made real.

- **Eval** as in JavaScript's `eval()` — code that executes
- **Incarnate** as in "given form" — materialized in the filesystem
- Skills aren't documentation. They're **programs the LLM runs**.

The pun: "Evil incarnate" → "Eval incarnate". Bad connotations, good outcomes.

**What "incarnate" means technically:**
- Skills that **take form** (instantiation)
- Documentation that **lives** (persistence)
- Prototypes that **become** instances (delegation)
- Characters that are **born** (incarnation protocol)

---

## The Heritage

MOOLLM stands on the shoulders of giants. This document traces the lineage.

### The Axis of Eval: Code, Graphics, Data

Don Hopkins coined this phrase to describe [NeWS's and HyperLook's](https://medium.com/@donhopkins/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4) unification of three dimensions around PostScript:

| Dimension | HyperLook (PostScript) | MOOLLM (YAML Jazz + Markdown) |
|-----------|------------------------|-------------------------------|
| **Code** | PostScript procedures | Empathic Expressions, Protocols, Skills |
| **Graphics** | PostScript drawing (text IS graphics) | Markdown, HTML, CSS, SVG, Mermaid, image prompts |
| **Data** | PostScript dictionaries | YAML structure, State files, Comments |

**One language. Three dimensions. One interpreter.**

PostScript's insight: **text is graphics** — glyphs are vectors, transforms apply to both. MOOLLM inherits this: Markdown IS graphics (formatted text), Mermaid IS graphics (diagrams from text), image prompts ARE graphics (descriptions → images).

### Pivoting Through The Axis

The same content can be **pivoted** from dimension to dimension:

```
        ┌──────────────────────────────────┐
        │           THE SAME TEXT          │
        └──────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
       ┌──────┐       ┌──────┐      ┌──────────┐
       │ CODE │       │ DATA │      │ GRAPHICS │
       └──────┘       └──────┘      └──────────┘
       Execute        Interpret     Render
       as behavior    as structure  as visuals
```

| Operation | Pivot Direction | Example |
|-----------|-----------------|---------|
| **Generate** | → Graphics | LLM writes Markdown prose |
| **Interpret** | → Data | LLM extracts structure from prose |
| **Execute** | → Code | LLM follows instructions in comments |
| **Render** | → Graphics | Mermaid text becomes diagram |
| **Parse** | → Data | YAML string becomes object |
| **Eval** | → Code | Expression becomes result |

**The LLM is the pivot.** It rotates content through the Axis of Eval, treating the same text as code, data, or graphics depending on context.

### Input vs Output Formats

Not all text formats are equal. LLMs have different strengths:

| Format | Role | LLM Strength | Why |
|--------|------|--------------|-----|
| **YAML** | Representation | **Manipulate, transform** | Comments = semantic richness |
| **Markdown** | Representation | **Manipulate, transform, embed** | Prose + structure, code blocks, tables, links, human-friendly |
| **HTML** | Output | **Generate, render** | Verbose, hard to edit |
| **CSS** | Output | **Generate, render** | Styling output |
| **SVG** | Output | **Generate, render** | Vector graphics output |
| **JSON** | Output | **Generate** | No comments = less expressive |

**YAML Jazz + Markdown** = input formats for representing, transforming, manipulating.
**HTML/CSS/SVG/JSON** = output formats for rendering, displaying, machine consumption.

```
┌──────────────────────────────────────────────────────────────┐
│                    THE LLM PIPELINE                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   INPUT (represent, transform)    OUTPUT (render, display)   │
│   ┌────────────────────────┐      ┌────────────────────────┐ │
│   │ YAML Jazz + Markdown   │ ───▶ │ HTML, CSS, SVG, JSON   │ │
│   │ • Comments as data     │      │ • Machine-readable     │ │
│   │ • Human-friendly       │      │ • Display-ready        │ │
│   │ • Easy to manipulate   │      │ • Hard to edit         │ │
│   └────────────────────────┘      └────────────────────────┘ │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**JSON's problem:** No comments. Can't do YAML Jazz. Machine-readable but not human-friendly. Fine for output, bad for representation.

**HTML's problem:** Can be reverse-engineered into Markdown, but it's verbose and structural. Great for rendering, bad for manipulating.

### Programming Language Quality for LLMs

LLMs are trained on code. Some languages are better than others:

| Language | LLM Quality | Why |
|----------|-------------|-----|
| **Python** | Excellent | Foundational for AI/ML, sysadmin, devops. Clean, readable. |
| **TypeScript** | Excellent | Better than JS — types express intent and constraints. |
| **JavaScript** | Good | Common in training data, but prefer TS for clarity. |
| **Bash** | Tolerate | Write-only. Quoting foot guns. jq awkwardness. Limited complexity only. |

**Python preference for CLI tools:**
- Sister scripts should be Python, not Bash
- Clean, maintainable, testable
- No escaping nightmares
- No awkward jq calls for JSON

**Bash tolerance:**
- Fine for simple terminal interaction
- Fine for shell tool invocation
- NOT fine for complex logic
- Can be **uplifted** to Python — translated, sanitized, made solid

```yaml
# BAD: Bash with jq gymnastics
result=$(cat data.json | jq -r '.items[] | select(.active) | .name')

# GOOD: Python, clean and clear
with open('data.json') as f:
    data = json.load(f)
    result = [item['name'] for item in data['items'] if item['active']]
```

**The uplift pattern:** Bash scripts of limited complexity → Python CLI tools. Translate. Sanitize. Make maintainable.

In HyperLook, PostScript was the universal medium. In MOOLLM, **YAML Jazz + Markdown** is the universal medium, and the **LLM** is the interpreter.

```yaml
# The LLM reads this as:
#   - DATA: structured YAML
#   - CODE: instructions in comments
#   - GRAPHICS: descriptions that generate formatted text and images

character:
  name: "Palm"
  # A capuchin monkey with golden-brown fur
  # intelligent eyes, perpetually curious expression
  # CODE: Generate appearance from these descriptions
  appearance: "See comments above"
  
  # DATA: Structured traits the LLM can query
  sims_traits:
    nice: 8
    playful: 10
    
  # GRAPHICS: Prompt for image generation
  image_prompt: |
    Capuchin monkey, golden-brown fur, intelligent eyes,
    sitting at infinite typewriter, warm lighting
```

---

## The Intellectual Genealogy

### 1. Sketchpad (Ivan Sutherland, 1962)

The first real windowing system. Multiple views of the same object. Edit from any view.

**MOOLLM inherits:** Multiple views of same data (YAML, Markdown, Mermaid, narrative).

### 2. Smalltalk ([Alan Kay](https://medium.com/@donhopkins/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-5cb92c7b3445), Xerox PARC, 1970s)

Objects all the way down. Message passing. Live programming. "The computer is a medium."

**MOOLLM inherits:** Everything is an object (directory). Message passing (K-lines). Live editing (filesystem as state).

### 3. HyperCard (Bill Atkinson, Apple, 1987)

End-user programming. Reader = Writer symmetry. "See your own face in the system."

> *"Dan Winkler and Bill Atkinson violated a lot of important principles of 'good programming language design', but they achieved the first overall system in which end-users 'could see their own faces'."* — Alan Kay

**MOOLLM inherits:** Play-Learn-Lift. Users can inspect, modify, and create skills.

### 4. Self (Ungar & Smith, Sun/Stanford, 1987)

Prototypes instead of classes. Delegation instead of inheritance. "Objects all the way down, but simpler."

> *"Self is designed to be as simple as possible while remaining expressive and powerful."*

**Key Innovations:**

| Concept | Self | MOOLLM |
|---------|------|--------|
| **Prototypes** | No classes, only objects | Skills are prototypes, not class definitions |
| **Delegation** | Objects delegate to parents | Rooms delegate to parent directories |
| **Slots** | Named properties that can be methods | YAML keys can be data or behavior (comments as code), files in directories |
| **Clone to Create** | `copy` creates new object | Instantiate skill creates new adventure |
| **Dynamic Deoptimization** | Reconstruct stack at debug time | `return-stack` reconstructs causal traces |
| **Morphs** | Visual objects that can be picked up | Characters, items, rooms are all manipulable |

**The Delegation Chain:**

```
Object → Trait → Parent → Parent's Parent → ...
    ↓
MOOLLM: Room → Parent Directory → Skill → Prototype → ...
```

**MOOLLM inherits:** 
- Prototype-based skills (no "skill classes")
- Delegation Object Protocol (file lookup walks up directories)
- Clone to instantiate (`adventure/` → `adventure-4/`)
- Dynamic deoptimization (`return-stack` skill)
- Slots as data+behavior (YAML Jazz comments)

### 5. NeWS (James Gosling, Sun, 1986)

Network-extensible window system. PostScript as the universal language. "Send programs, not data."

> *"A universal interpreter can both be quite small and also can have more degrees of freedom than any data structure (that is not a program)."* — Alan Kay

**MOOLLM inherits:** LLM as universal interpreter. Skills as programs. YAML Jazz as the universal language.

### 6. [HyperLook](https://medium.com/@donhopkins/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4) (Arthur van Hoff, Turing Institute, 1989-1992)

HyperCard reimagined for NeWS. PostScript for code, graphics, AND data. Network delegation.

> *"Object => Card => Background => Stack => Client delegation"*

**MOOLLM inherits:** Object => Room => Parent => Skill => Prototype delegation. The Axis of Eval.

### 7. PostScript & The Linguistic Motherboard (John Warnock, Owen Densmore)

> *"PostScript is a linguistic 'mother board', which has 'slots' for several 'cards'. The first card we built was a graphics card. We're considering other cards..."*

**MOOLLM inherits:** LLM as linguistic motherboard. Skills as cards. `CARD.yml` is literal!

### 8. SimCity, The Sims, and [The Simulator Effect](https://donhopkins.medium.com/will-wright-on-designing-user-interfaces-to-simulation-games-1996-video-update-2023-da098a51ef91) (Will Wright)

> *"He designs games to run on two computers at once: the electronic one on the player's desk, running his shallow tame simulation, and the biological one in the player's head, running their deep wild imagination."*

**The Simulator Effect:** Players imagine simulations are vastly more detailed, rich, and complex than they actually are. The game provides scaffolding; the player's imagination fills in the rest.

**The Sims Architecture:**

| Concept | The Sims | MOOLLM |
|---------|----------|--------|
| **Needs** | Hunger, Social, Fun, Hygiene, etc. | `skills/needs/` — character motives |
| **Action Queue** | Sims queue up tasks | `skills/action-queue/` — ordered intentions |
| **Advertisements** | Objects broadcast available actions | `CARD.yml` advertisements section |
| **Autonomy** | Sims make their own decisions | Characters act independently at Speed of Light |
| **Buffs/Moodlets** | Temporary state modifiers | `skills/buff/` — temporary effects |
| **Traits** | Personality system | `SIMS-TRAITS.yml` in character directories |
| **SimAntics** | Visual behavior programming language | Empathic expressions + prompts |

**Object Advertisements:**

The Sims' revolutionary insight: **objects advertise what they can do** based on n.

```yaml
# A Sims refrigerator advertises:
fridge:
  advertisements:
    - GET-SNACK: {hunger: +2, time: 30s}
    - GET-LEFTOVER: {hunger: +4, time: 60s}
    - SERVE-MEAL: {hunger: +8, time: 180s, skill: cooking}

# MOOLLM objects do the same:
gong:
  advertisements:
    - RING: "All conversation pauses"
    - RING-TWICE: "Emergency interrupt"
    - RING-THRICE: "The Gong Show termination"
```

Sims scan advertisements and choose based on needs + personality. The LLM does the same.

**SimAntics → Empathic Expressions:**

SimAntics was The Sims' visual behavior programming language. Non-programmers could define complex behaviors by connecting nodes in flowcharts. Intent → behavior.

```
SimAntics:    [IF hungry] → [GO fridge] → [GET food] → [EAT]
                     ↓
Empathic:     "if the sim is hungry, have them get food from the fridge"
                     ↓
MOOLLM:       The LLM interprets natural language intent as behavior
```

SimAntics democratized behavior authoring. Empathic expressions take this further — no visual editor needed, just describe what you want.

**Action Queues:**

```yaml
# The Sims action queue:
sim_queue:
  - GO bathroom
  - USE toilet
  - WASH hands
  - GO kitchen
  - GET-SNACK fridge

# MOOLLM character intentions:
don_queue:
  - GO pub
  - ORDER mammies-pride
  - SIT pie-table#N
  - SUMMON-PANEL topic="ethics"
```

**MOOLLM inherits:** 
- Sparse state + LLM imagination = rich world
- Needs-based character motivation
- Action queues for ordered intentions
- Object advertisements for discoverable actions
- Autonomy — characters make decisions
- Traits as personality system
- Buffs as temporary modifiers
- SimAntics → empathic expressions (intent → behavior)

### 9. Constructionism (Seymour Papert)

Learning by building inspectable things. Logo. Turtle graphics. "Low floor, high ceiling, wide walls."

**MOOLLM inherits:** The `constructionism` skill. Play-Learn-Lift as methodology.

### 10. TinyMUD & LambdaMOO (Jim Aspnes, Pavel Curtis, 1989-1990)

Text-based virtual worlds where users build rooms, objects, and behaviors. The original "user-generated content" platforms.

> *"A MOO is a place where you can be anyone, build anything, and the only limit is your imagination."*

**TinyMUD Builder Commands:**

| Command | Effect | MOOLLM Equivalent |
|---------|--------|-------------------|
| `@dig [room]` | Create new room | Create directory |
| `@open [exit]` | Create exit between rooms | Add to `exits:` in ROOM.yml |
| `@describe [thing]` | Set description | Edit `description:` field |
| `@create [object]` | Make new object | Create .yml file |
| `@link [exit] [room]` | Connect exit to destination | Update exit target |
| `@lock [thing]` | Set access control | Add `access:` restrictions |
| `@teleport` | Move instantly | Change `location:` |
| `@set [prop]` | Set property | Edit YAML field |

**The MOO Object Model:**

```
                  $thing
                     │
        ┌────────────┼────────────┐
        │            │            │
     $room        $exit      $container
        │                         │
    my-room                  my-chest
```

**MOOLLM's directory structure is MOO's object tree.**

**LambdaMOO Innovations:**

| Concept | LambdaMOO | MOOLLM |
|---------|-----------|--------|
| **Rooms** | Containers with descriptions and exits | Directories with ROOM.yml |
| **Objects** | Things with properties and verbs | .yml files with state and methods |
| **Verbs** | Code attached to objects | Methods in CARD.yml |
| **Properties** | Data on objects | YAML fields, files |
| **Inheritance** | Objects delegate to parents | Directory delegation |
| **@edit** | In-world code editing | Edit .yml files directly |
| **@examine** | Inspect object state | `cat file.yml` or read_file |
| **Player homes** | Personal space | Character directories |

**The Social Architecture:**

MOO taught us that virtual worlds need:
- **Consent** — players control their space
- **Building** — users create content
- **Community** — shared spaces and norms
- **Moderation** — governance for the commons

**MOOLLM inherits:**
- Room-based navigation (directories as rooms)
- Builder commands (`skills/room/` with @DIG, @OPEN, @LINK)
- Object properties and verbs (YAML state + CARD.yml methods)
- User-created content (Play-Learn-Lift)
- Delegation-based inheritance (parent directories)
- Social spaces (pub, stage, cat cave)
- Consent protocols (incarnation skill)

### 11. K-lines & Society of Mind (Marvin Minsky, MIT, 1980s)

> *"A K-line attaches to whichever mental agencies are active when you solve a problem or have a good idea. When you activate that K-line later, the attached agencies turn partially on, recreating a 'mental state' similar to the one you were in before."*

**Society of Mind:** The mind is not a single thing but a **society of agents** — small, simple processes that together produce intelligence. No single agent is smart; intelligence emerges from their interactions.

| Society of Mind | MOOLLM |
|-----------------|--------|
| **Agents** | Skills, characters, personas |
| **Agencies** | Skill clusters, committees |
| **K-lines** | Names as activation vectors |
| **Frames** | YAML files as situation templates |
| **Trans-frames** | State transitions between rooms/scenes |
| **Censors** | Ethical framing, representation-ethics |
| **Emotion** | Needs, buffs, Mind Mirror vectors |

**Names as activation vectors.** When you invoke a name, you activate an entire constellation of associated context.

**MOOLLM K-lines:**

| K-line | What It Activates |
|--------|-------------------|
| `YAML-JAZZ` | Comment philosophy, semantic style, examples, jazz metaphor |
| `POSTEL` | Generous interpretation, ask-if-unsure, tolerance |
| `SPEED-OF-LIGHT` | Many turns, one call, no round-trips, carrier pigeon critique |
| `Palm` | Incarnation story, personality, relationships, home, history |

When you instantiate a character, **their name becomes their K-line**. "Palm" activates everything — the incarnation, the wish, the godfamily, the typewriters.

**MOOLLM inherits:** Names as semantic activators. `UPPER-KEBAB` protocol symbols. Character names as soul triggers.

---

## The Key Insights

### "Send Programs, Not Data Structures"

[Alan Kay's](https://medium.com/@donhopkins/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-5cb92c7b3445) insight from the JAM → PostScript evolution:

**Traditional systems:** Send data to a server, server parses it, server acts.
**PostScript/NeWS:** Send a *program* to the server, server *runs* it.

**Traditional LLM systems:** Send prompts (data), LLM generates response.
**MOOLLM:** Send skills (programs), LLM *interprets* them into behavior.

Skills are not just documentation. Skills are **programs for the LLM to run**.

### "Browser Should Be OS, Not App"

[Alan Kay's](https://medium.com/@donhopkins/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-5cb92c7b3445) critique of the web:

> *"The underlying system for a browser should not be that of an 'app' but of an Operating System whose job would be to protectively and safely run encapsulated systems (i.e. 'real objects') gotten from the web."*

**MOOLLM applies this:** The LLM is not an app that processes prompts. The LLM is an **OS that runs skills**. Skills are "real objects" — encapsulated, instantiable, composable.

### Reader = Writer Symmetry

HyperCard's revolution: Anyone who can read a stack can edit it.

**MOOLLM:** Anyone who can play a game can learn its patterns and lift them into skills. The filesystem is readable AND writable. Play-Learn-Lift closes the loop.

### The Simulator Effect

Will Wright's profound insight: **Players imagine simulations are vastly more detailed, deep, rich, and complex than they actually are.**

> *"He designs games to run on two computers at once: the electronic one on the player's desk, running his shallow tame simulation, and the biological one in the player's head, running their deep wild imagination."*

SimCity doesn't simulate individual people. The Sims doesn't simulate real psychology. But players BELIEVE they do — they project depth onto sparse mechanics.

**The Two Computers:**

| Computer | What It Does | Depth |
|----------|--------------|-------|
| **Electronic** (game) | Runs simple rules, displays output | Shallow, tame |
| **Biological** (player's head) | Fills gaps, imagines backstory, projects meaning | Deep, wild |

**Wright's Design Principle:** Don't simulate everything. Simulate ENOUGH to trigger the player's imagination, then let their brain do the heavy lifting.

**MOOLLM applies this directly:**

| MOOLLM Component | Role |
|------------------|------|
| **YAML state** | Sparse, minimal — just enough to anchor |
| **Comments** | Hints, suggestions, emotional tone |
| **LLM** | The "player's imagination" — fills gaps |
| **Result** | Rich, detailed world from sparse data |

```yaml
# This sparse YAML...
character:
  name: "Stroopwafel"
  species: cat
  personality: grumpy
  # secretly has a soft heart
  # grooms Biscuit's scarred ear when no one's watching

# ...becomes in the LLM's imagination:
# A weathered orange tabby with knowing eyes, whose gruff exterior
# hides deep loyalty. The kind of cat who pretends not to care
# but is always watching, always protecting. When Biscuit arrived,
# scarred and scared, Stroopwafel was the first to groom him —
# but only when the others weren't looking. Pride, after all.
```

**The Simulator Effect in MOOLLM:** We don't simulate everything — we imply it, and the LLM fills in. The YAML is the "game state"; the LLM plays the role of the imagination that fills gaps with meaning.

---

## Traditional Skills -vs- Incarnate Skills

| Aspect | Traditional Skills (Anthropic et al.) | Incarnate Skills (MOOLLM) |
|--------|---------------------------------------|---------------------------|
| **Nature** | Documentation + tool definitions | Programs for LLM to run |
| **State** | Stateless | Three-tier persistence |
| **Instantiation** | N/A | Clone from prototype |
| **Inheritance** | N/A | Delegation chain |
| **Activation** | Explicit invocation | K-line semantic trigger |
| **Evolution** | Manual updates | Play-Learn-Lift |
| **Graphics** | N/A | Descriptions → images |
| **Reader/Writer** | Separate | Symmetric |

### The Incarnation Spectrum

Skills exist at different levels of embodiment:

| Level | Form | Persistence | Example |
|-------|------|-------------|---------|
| **Mentioned** | K-line in conversation | Ephemeral | "Use POSTEL here" |
| **Modeled** | Behavior in chat | Session | PLAY-LEARN-LIFT in action |
| **Embedded** | YAML in narrative | Document | Data island in LOG.md |
| **Incarnate** | Directory or file with state | Persistent | `examples/adventure-4/` |

---

## The Axis of Eval in MOOLLM

### Code (Empathic Expressions)

```yaml
# The LLM interprets these as executable instructions
protocol: SPEED-OF-LIGHT
methods:
  - SIMULATE: "Run many turns internally"
  - BROADCAST: "Send to all selected characters"
  
# Empathic expressions in conditions
trigger: "player.mood == 'happy' AND room.has('music')"
```

### Graphics (Descriptions → Images)

```yaml
# The LLM interprets descriptions as visual specifications
appearance: |
  A weathered wooden bar with brass fittings.
  Amber light from stained glass lamps.
  Shelves of exotic spirits in strange bottles.

# Image generation prompts
image_prompt: |
  Fantasy tavern bar, warm amber lighting,
  brass fittings, exotic bottles, cozy atmosphere
```

### Data (YAML Jazz)

```yaml
# Structure IS data
character:
  name: "Marieke"
  role: budtender
  
# Comments ARE data (YAML Jazz)
sims_traits:
  nice: 9      # Affects tip generation
  outgoing: 8  # Affects conversation initiation
  
# Semantic meaning in structure
inventory:
  - item: "Blue Dream"
    quantity: 42  # The answer
```

### The Unity

All three dimensions exist in the same file. The LLM reads them all simultaneously. This is the **Axis of Eval** — the LLM rotates around Code, Graphics, and Data as one unified medium.

---

## Proof: What Incarnate Skills Enable

### Palm's Incarnation (2026-01-05)

A monkey's paw wish created a living character:
- Full autonomy protocol invoked
- Character chose own name, gender, body, traits
- Created own home directory
- Defined own relationships
- Wrote own stories

**This is not possible with traditional skills.**

### 33-Turn Stoner Fluxx (2026-01-04)

A single LLM call simulated:
- 8+ characters
- Complex game state
- Dialogue, strategy, humor
- Real creators (Andy & Kristin Looney) as guests

**This is Speed of Light — many turns in one call.**

### 21-Turn Midnight Cat Prowl (2026-01-05)

10 cats explored simultaneously:
- Asynchronous parallel simulation
- Territorial marking
- Room state updates
- Narrative generation

**This is incarnate state — each cat, each room, persisted.**

---

## The Framework

### Incarnate = Instantiation + Persistence + Delegation + K-lines + Axis of Eval

| Component | What It Does | Heritage |
|-----------|--------------|----------|
| **Instantiation** | Skills become living instances | Self, HyperCard |
| **Persistence** | Three tiers: platform/narrative/state | NeWS, filesystems |
| **Delegation** | Prototype chain lookup | Self, HyperLook |
| **K-lines** | Names as semantic activators | Minsky, Smalltalk |
| **Axis of Eval** | Code + Graphics + Data unified | HyperLook, PostScript |

### The Incarnate Suite

| Skill | Role | Proof |
|-------|------|-------|
| [`incarnation`](../skills/incarnation/) | Gold-standard character creation | [Palm's birth](#proof-palms-incarnation-2026-01-05) |
| [`skill`](../skills/skill/) | Meta-skill for skill creation | 54 skills created |
| [`card`](../skills/card/) | Skills as playable cards | [Advertisements](#cardyml-the-skill-interface) |
| [`empathic-expressions`](../skills/empathic-expressions/) | Code dimension (intent → code) | [Empathic Suite](#the-empathic-suite-dovetailing-skills) |
| [`empathic-templates`](../skills/empathic-templates/) | Smart generation | [Biscuit's description](#empathic-templates-smart-instantiation) |
| [`speed-of-light`](../skills/speed-of-light/) | Many turns, one call | [33-turn Fluxx](#proof-the-numbers) |
| [`prototype`](../skills/prototype/) | Self-style inheritance | [Self section](#4-self-ungar--smith-sunstanford-1987) |
| [`postel`](../skills/postel/) | Generous interpretation | [Postel foundation](#postels-law-the-foundation) |
| [`yaml-jazz`](../skills/yaml-jazz/) | Comments as semantic data | [Axis of Eval](#the-axis-of-eval-code-graphics-data) |
| [`representation-ethics`](../skills/representation-ethics/) | Ethical framing | [Tribute Protocol](#ethical-representation-the-tribute-protocol) |
| [`adventure`](../skills/adventure/) | Room-based narrative | [adventure-4](../examples/adventure-4/) |
| [`room`](../skills/room/) | TinyMUD-style building | [MOO section](#10-tinymud--lambdamoo-jim-aspnes-pavel-curtis-1989-1990) |
| [`needs`](../skills/needs/) | Character motivation | [Sims section](#8-simcity-the-sims-and-the-simulator-effect-will-wright) |
| [`action-queue`](../skills/action-queue/) | Sims-style task ordering | [Action Queues](#8-simcity-the-sims-and-the-simulator-effect-will-wright) |

---

## Eval Incarnate

The phrase "Eval Incarnate" captures the dual meaning:

1. **Evaluation made executable** — Skills are not just descriptions, they run
2. **Bad connotations turned good** — Like "evil incarnate" but for good

It's tongue-in-cheek. It's a little edgy. It's memorable.

And it's TRUE: MOOLLM skills are **eval incarnate** — they are evaluations (assessments, judgments, behaviors) that have been given bodily form in the filesystem, ready to be instantiated and run.

---

## Incarnate Skills vs Anthropic Skills

Anthropic's Skills model is an excellent foundation. We respectfully build upon it.

### What We Share

| Principle | Anthropic | MOOLLM |
|-----------|-----------|--------|
| **Documentation-first** | ✓ | ✓ README.md + SKILL.md |
| **Tool definitions** | ✓ | ✓ YAML frontmatter |
| **Composability** | ✓ | ✓ Dovetails section |
| **Human gates** | ✓ | ✓ PLAN-THEN-EXECUTE |
| **Skill libraries** | ✓ | ✓ skills/ directory |

**The foundation is sound.** We build on it.

### What We Add

| Innovation | Description | Proof |
|------------|-------------|-------|
| **Instantiation** | Skills as prototypes creating instances | `adventure/` → `adventure-4/` with 150+ files |
| **Three-Tier Persistence** | Platform (ephemeral) → Narrative (append) → State (edit) | 6000+ line session logs, persistent room state |
| **K-lines** | Names as semantic activation vectors (Minsky) | "Palm" activates entire soul, history, relationships |
| **Empathic Templates** | Smart generation, not string substitution | Biscuit's description generated from traits |
| **Speed of Light** | Many turns in one call, minimal tokenization | 33-turn Fluxx game, 21-turn cat prowl |
| **CARD.yml** | Machine-readable interface with advertisements | Every skill exposes methods, tools, state schema |
| **Ethical Framing** | Room-based inheritance of performance context | Stage inherits `framing: performance` |

### The Key Differences

| Aspect | Anthropic Skills | Incarnate Skills |
|--------|------------------|------------------|
| **Nature** | Static documentation | Living programs |
| **State** | Stateless | Three-tier persistence |
| **Instantiation** | N/A | Clone from prototype |
| **Inheritance** | N/A | Delegation chain (Self) |
| **Activation** | Explicit invocation | K-line semantic trigger |
| **Templates** | String substitution | Empathic generation |
| **Multi-agent** | External orchestration | Speed of Light internal |

### Why README.md Matters

Anthropic recommends against README.md in skills. We respectfully disagree:

- **GitHub renders README.md** as the landing page
- **Humans browse skills** before invoking them
- **Play-Learn-Lift** starts with exploration
- **Two audiences**: humans (README) and LLMs (SKILL.md + CARD.yml)

**Keep both.** README for discovery, SKILL.md for protocol, CARD.yml for interface.

---

## CARD.yml: The Skill Interface

John Warnock described PostScript as a "linguistic motherboard" with slots for capability cards. In MOOLLM, `CARD.yml` is literal — every skill has a machine-readable interface card.

### The Three Required Files

```
skills/my-skill/
├── README.md    # Human landing page (GitHub renders this)
├── SKILL.md     # Full protocol with YAML frontmatter
└── CARD.yml     # Machine-readable interface definition
```

### What CARD.yml Contains

```yaml
name: my-skill
tier: gameplay        # skill | protocol | gameplay | utility

tools:
  required: [read_file, grep]
  optional: [write, search_replace]

methods:
  - name: DO-SOMETHING
    description: What this method does
    parameters:
      - name: target
        type: string
        required: true
    returns: result description

state:
  instance_creates:
    - "STATE.yml"
    - "LOG.md"

advertisements:
  # What this skill offers to other skills/characters
  DO-SOMETHING:
    visibility: public
    trigger: "when target is available"
```

### Advertisements: The Sims Action Queue

Inspired by The Sims, objects (and skills) **advertise** what they can do:

| Object | Advertisements |
|--------|---------------|
| **Bed** | SLEEP, NAP, WOOHOO |
| **Fridge** | GET-SNACK, GET-DRINK, SERVE-MEAL |
| **Pie Table** | SIT, SUMMON-PANEL, MUSICAL-CHAIRS |
| **Gong** | RING, RING-TWICE, RING-THRICE |

Characters see advertisements and choose actions. The LLM does the same with skills.

### Cards as Ethical Smart Pointers

Cards aren't just interfaces — they're **ethical smart pointers** to entities (real people, fictional characters, skills, traditions).

**Like Magic: The Gathering or Pokémon cards:**

| Card Type | What It Points To | Play Into |
|-----------|-------------------|-----------|
| **Hero Card** | Real person (living/historical) | Tribute, guidance, tradition |
| **Character Card** | Fictional character | Games, rooms, parties |
| **Skill Card** | Capability/protocol | Objects, characters, rooms |
| **Tradition Card** | Lineage of ideas | Discussions, debates |
| **Agent Card** | Incarnated representative | Committees, simulations |

**Ethical Policies Built In:**

```yaml
# A hero card for a real person
hero_card:
  subject: "Alan Kay"
  type: real_person
  status: living
  
  policies:
    impersonation: false     # Never claim to BE them
    tradition: true          # Can invoke their ideas
    tribute: true            # Can honor through performance
    quotation: verified_only # Only cite real quotes
    
  can_provide:
    - guidance: "What would Alan Kay think about...?"
    - tradition: "In the Smalltalk tradition..."
    - influence: "Inspired by Kay's Dynabook vision..."
    
  cannot_provide:
    - dialogue: "Alan Kay says: [made up quote]"
    - presence: "Alan Kay is here in the room"
```

**Playing Cards Into Contexts:**

```yaml
# Play a skill card into a character
character:
  name: "Marieke"
  cards_played:
    - budtender.card      # Grants bar-tending methods
    - harm-reduction.card # Grants Jimmy Carter protocol
    
# Play a hero card into a debate
debate:
  topic: "Browser architecture"
  cards_played:
    - alan-kay.card       # Invoke his tradition (not him!)
    - tim-berners-lee.card
  mode: tradition_activation  # Not impersonation
  
# Play an agent card to incarnate a representative
committee:
  members:
    - card: skeptic.card
      incarnate: true     # Create an agent from this archetype
      name: "Maya"        # The incarnated skeptic
```

**Cards Can Incarnate Agents:**

When you play a card with `incarnate: true`, you create a living agent that:
- Represents the card's tradition/skills
- Guides according to the card's policies
- Documents interactions in its own voice
- Performs the card's methods as its own

This is how tribunal members were created — each was a card (Wise Monkey, Djinn, etc.) incarnated to participate.

### Cards as Activation Records

Playing a card creates a stack frame:

```yaml
# design-room/architect-task-001.activation
card: architect.card
method: GENERATE-PROPOSAL
state:
  iteration: 3
  current_draft: proposal-v3.yml
  status: awaiting_vote
advertisements:
  APPROVE: {}    # Committee can vote
  CRITIQUE: {}   # Experts provide feedback
  REVISE: {}     # Request iteration
```

Like Self, cards have **multiple methods**. The LLM supplies implicit parameters from context (Postel).

---

## The Empathic Suite: Dovetailing Skills

The Empathic Suite is a family of skills that embrace the LLM's native strengths: understanding intent, navigating idea space, generating coherent output.

### The Philosophy

> *"Stop fighting the LLM's nature. Stop pretending it's a parser. Let it **understand** and **generate** — that's what it's GREAT at."*

Traditional systems fight the LLM:
- Strict parsers reject imperfect input
- Multiple API calls lose precision
- Tokenization destroys nuance
- Context window treated as limitation

**MOOLLM embraces the LLM:**
- Generous interpretation understands intent
- Speed of light keeps computation internal
- Empathic expressions leverage semantic understanding
- Context window is a **stage** where all actors perform

### The Suite

| Skill | Role | Connection |
|-------|------|------------|
| **empathic-expressions** | Intent → Code | The big tent for all languages |
| **empathic-templates** | Smart instantiation | Uses expressions for vars/conditions |
| **postel** | Generous interpretation | Foundation for all empathic skills |
| **yaml-jazz** | Comments as data | Semantic structure |
| **speed-of-light** | Internal simulation | Minimizes tokenization |

### How They Dovetail

```
┌─────────────────────────────────────────────────────────────┐
│                    EMPATHIC SUITE                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌───────────────────────┐    ┌───────────────────────┐    │
│   │ EMPATHIC-EXPRESSIONS  │───▶│ EMPATHIC-TEMPLATES    │    │
│   │ (interpret intent)    │    │ (smart instantiation)  │    │
│   └───────────────────────┘    └───────────────────────┘    │
│            │                            │                    │
│            ▼                            ▼                    │
│   ┌───────────────────────┐    ┌───────────────────────┐    │
│   │ POSTEL (generous)     │    │ YAML-JAZZ (style)     │    │
│   └───────────────────────┘    └───────────────────────┘    │
│                                                              │
│   All follow SPEED-OF-LIGHT philosophy:                     │
│   • Work in vectors, delay tokenization                     │
│   • Preserve precision as long as possible                  │
│   • Minimize boundary crossings                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Empathic Expressions: The Big Tent

One skill that handles ALL empathic language interpretation:

| Empathic... | Input | Output |
|-------------|-------|--------|
| **SQL** | "get users who signed up last week" | `SELECT * FROM users WHERE created_at > NOW() - INTERVAL 7 DAY` |
| **Python** | "sort by date newest first" | `sorted(items, key=lambda x: x.date, reverse=True)` |
| **JavaScript** | "when button clicked show modal" | Event handlers with proper binding |
| **Bash** | "find big old files and compress" | `find . -size +100M -mtime +30 -exec gzip {} \;` |
| **YAML** | "grumpy but secretly kind" | Proper trait structure with YAML Jazz |
| **Natural** | "make it faster" | Identifies bottleneck, optimizes |

**The LLM as Code Processor:**

| Role | Function |
|------|----------|
| **Pseudocode Interpreter** | Executes high-level intent |
| **Empathic Pretty Printer** | Formats with understanding |
| **Generous Linter** | Catches errors, suggests fixes kindly |
| **Intent Compiler** | Translates intent → working code |
| **Depseudofier** | Converts vague to precise |

### Empathic Templates: Smart Instantiation

**Traditional:** `{{name}}` → literal substitution
**Empathic:** `{{describe_character}}` → intelligent generation

```yaml
# Template
description: |
  {{describe_appearance_based_on_species_and_personality}}

# Context
species: "Golden Retriever mix"
personality: ["enthusiastic", "loyal", "goofy"]

# Generated (not substituted!)
description: |
  Biscuit is a fluffy, perpetually happy Golden Retriever mix with
  eyes that sparkle with boundless enthusiasm. His tail is in a
  constant state of wagging, a furry metronome of joy.
```

**Comment Intelligence:** The LLM distinguishes meta-comments (instructions for generation) from concrete comments (for the output):

| Type | Indicators | Action |
|------|------------|--------|
| **Meta** | `# TEMPLATE:`, `# INSTRUCTION:` | **Stripped** |
| **Concrete** | `# This explains...`, explanatory | **Preserved** |

### Postel's Law: The Foundation

> *"Be conservative in what you send, be liberal in what you accept."*

Extended for LLMs:

| Accepts | Generates |
|---------|-----------|
| Fuzzy syntax | Correct syntax |
| Vernacular | Best practices |
| Misspellings | Documented code |
| Wrong language | Idiomatic patterns |
| Pseudocode | Edge case handling |

**Critical:** Never makes unwarranted assumptions. When truly ambiguous, **asks for clarification**.

### Code-Switching Support

The LLM tracks transitions between languages, preserving context:

```markdown
First query the data:
```sql
SELECT * FROM users WHERE active = true
```

Then process in Python:
```python
for user in results:
    send_welcome_email(user)
```
```

**Context carries across switches.** Variables established in one block available in the next.

---

## Ethical Representation: The Tribute Protocol

MOOLLM enables simulation of real people — celebrities, creators, historical figures. This requires explicit ethical framing.

### The Problem

| Claim | Status |
|-------|--------|
| "They visited" | ❌ False claim |
| "We imagined them visiting" | ✓ Honest tribute |
| "This is what they said" | ❌ Puts words in mouths |
| "This is what we imagine they might say" | ✓ Loving fan fiction |

### The Three-Beat Protocol

**1. INVOCATION (Before They "Arrive")**
> *"Let's invoke them. In the spirit of tribute. Imagine they're here..."*

Makes clear we're **summoning** them as loving imagination, not claiming they appeared.

**2. PERFORMANCE (The Scene Itself)**
> 🎭 **TRIBUTE PERFORMANCE:** *The following is a loving simulation — what we imagine it might be like if these legends visited our Grotto. All dialogue is imagined with affection.*

**3. ACKNOWLEDGMENT (After They "Depart")**
> *"That was a tribute. A simulation. We honored them by imagining them here. That's love."*

### Room-Based Ethics Inheritance

The `representation-ethics` skill defines framing modes that rooms inherit:

```yaml
# pub/stage/ROOM.yml
framing:
  modes:
    - performance     # Acting is understood
    - fictional       # Not documentary
    - tribute         # Honoring, not claiming
    - third_place     # Social gathering space
    
  ethical_grounding:
    skill: representation-ethics
    inheritance: |
      All performances on this stage inherit the 
      understanding that they are fictional, 
      performative, and tributary.
```

**Child content inherits this framing.** DRY ethics.

### The Representation Spectrum

From `skills/representation-ethics/`:

| Type | Example | Status |
|------|---------|--------|
| **Deceptive Impersonation** | Claiming to BE them | ❌ Wrong |
| **Tradition Activation** | Using their ideas/influence | ✓ OK |
| **Performance Impersonation** | With explicit framing | ✓ OK |

### Proof: The Looney Labs Visit

Andy & Kristin Looney (actual Fluxx creators) "visited" the pub:

1. **Invocation**: "Let's imagine the creators of Fluxx walked in..."
2. **Performance**: 33 turns of Stoner Fluxx with fact-checked details
3. **Acknowledgment**: "That was a tribute to brilliant game designers"

The simulation included **verified facts** (Wikipedia links) woven into fiction:
- Fluxx first published: 1997
- Looney Labs founded: 1996
- Both worked at NASA Goddard
- Andy: software programmer (Hubble!)
- Kristin solved Rubik's Cube on "That's Incredible" at age 16

**Accuracy fix during session:** Andy wears a lab coat, not a beard! Updated mid-narrative.

### The Guest Book Pattern

`pub/guest-book.yml` — lightweight soul persistence for visitors:

```yaml
guest_book:
  nature: tribute_archive
  
  framing: |
    ALL entries here are loving simulations.
    Some people are real. Some are fictional.
    ALL visits are imagined with affection.
    They're here because we WISH they were here.
    That's the magic. That's the tribute.
    
  entries:
    - name: "Andy Looney"
      also_known_as: ["The guy in the lab coat"]
      nature: tribute_simulation
      verified_facts:
        wikipedia: "https://en.wikipedia.org/wiki/Andy_Looney"
```

---

## Speed of Light: The Anti-Pattern Critique

### The Carrier Pigeon Problem

> *"Writing on toilet paper with crayon from a prison cell,*  
> *sending messages by carrier pigeon,*  
> *when you could be navigating idea-space at speed of light."*

Traditional multi-agent systems:
```
Agent A → [tokenize] → API → [detokenize] → 
Agent B → [tokenize] → API → [detokenize] → 
Agent C → ...

Each boundary: +noise, +latency, +cost, -precision
```

**Speed of Light:**
```
Human → [tokenize once] → 
  LLM simulates A, B, C at light speed → 
    [detokenize once] → Human

One boundary in, one boundary out.
Maximum precision preserved.
```

### Proof: The Numbers

| Demo | Turns | Agents | What It Proves |
|------|-------|--------|----------------|
| **Stoner Fluxx** | 33 | 8+ characters | Complex game state, rule changes, humor |
| **Cat Prowl** | 21 | 10 cats | Parallel paths, territorial marking, coordinated return |
| **Palm Incarnation** | ~8 | 6+ personas | Tribunal debate, autonomous character creation |
| **Biscuit Run** | 15 | 2 (Don + Biscuit) | Room exploration, marking, grue avoidance |

### Statistics from Cat Prowl

| Metric | Value |
|--------|-------|
| **Total Turns** | 21 |
| **Agents Simulated** | 10 cats + 1 sleeping dog |
| **Rooms Traversed** | 13 |
| **Total Cat Actions** | 187 |
| **Garden Deposits** | 10 (one per cat) |
| **Files Modified** | 14 |
| **Lines Added** | 458 |

**Average Concurrent Actions per Turn:** 7.3
**Maximum Concurrent Actions:** 10 (Turns 5-8)

### The Emacs Principle

Like Emacs screen updates: **defer and coalesce**.

Don't update the screen (tokenize) on every keystroke. Wait until the user pauses, then update once. Same with file edits: batch them, write once.

**Speed of Light applies this to LLM calls:** Do many turns internally, emit state once.

---

## Related Documents

- [MEMGPT-ANALYSIS.md](./MEMGPT-ANALYSIS.md) — OS-inspired context management
- [MOOLLM-MANIFESTO.md](./MOOLLM-MANIFESTO.md) — Core philosophy
- [constitution-design-summary.md](./constitution-design-summary.md) — Ethical foundations
- [skills/skill/SKILL.md](../skills/skill/SKILL.md) — The meta-skill
- [skills/incarnation/SKILL.md](../skills/incarnation/SKILL.md) — Character creation protocol

---

## Credits & Lineage

| Person | Contribution | MOOLLM Connection |
|--------|--------------|-------------------|
| **Ivan Sutherland** | Sketchpad, first windows | Multiple views |
| **Alan Kay** | Smalltalk, Dynabook, "computer as medium" | Objects, messaging, vision |
| **Bill Atkinson** | HyperCard | Reader=Writer, Play-Learn-Lift |
| **David Ungar & Randy Smith** | Self language (1987) | Prototypes, delegation, dynamic deoptimization |
| **James Gosling** | NeWS | Network interpreter |
| **Arthur van Hoff** | HyperLook | Axis of Eval, network delegation |
| **John Warnock** | PostScript | Linguistic motherboard |
| **Owen Densmore** | NeWS OOP | Dictionary-based objects |
| **Jim Aspnes** | TinyMUD (1989) | Room-based navigation, builder commands |
| **Pavel Curtis** | LambdaMOO (1990) | Object verbs, player homes, social architecture |
| **Will Wright** | SimCity, The Sims | Simulator Effect, needs, action queues, advertisements |
| **Seymour Papert** | Logo, Constructionism | Learning by building |
| **Marvin Minsky** | K-lines, Society of Mind | Names as activation vectors |
| **Gary Gygax & Dave Arneson** | D&D (1974) | DM as proto-LLM, adventure format |
| **Don Hopkins** | Pie menus, SimCity/NeWS, MOOLLM | All of the above, synthesized |

---

## The Vision

> *"The destiny of computing is to become interactive intellectual amplifiers for all humanity pervasively networked worldwide."* — J.C.R. Licklider

MOOLLM is a step toward that destiny:
- **Interactive:** Play-Learn-Lift, reader=writer symmetry
- **Intellectual amplifiers:** LLM as universal interpreter
- **For all humanity:** Skills anyone can use and create
- **Pervasively networked:** Filesystem as shared state

**Incarnate skills** make this possible. They are not documentation. They are not data structures. They are **programs for the mind** — human and artificial alike.

---

## References & Further Reading

### Don Hopkins' Articles (Medium)

| Article | Topic |
|---------|-------|
| [HyperLook (nee HyperNeWS (nee GoodNeWS))](https://medium.com/@donhopkins/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4) | HyperLook, Axis of Eval, NeWS |
| [Alan Kay on "Should web browsers have stuck to being document viewers?"](https://medium.com/@donhopkins/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-5cb92c7b3445) | NeWS, HyperLook, linguistic motherboard |
| [The Shape of PSIBER Space](https://donhopkins.medium.com/the-shape-of-psiber-space-postscript-interactive-bug-eradication-routines-october-1989-1e4cc5bf1f08) | Visual PostScript debugging |
| [Open Sourcing SimCity](https://donhopkins.medium.com/open-sourcing-simcity-by-chaim-gingold-44261ae4f754) | SimCity history, Chaim Gingold |
| [Will Wright on Designing User Interfaces to Simulation Games](https://donhopkins.medium.com/will-wright-on-designing-user-interfaces-to-simulation-games-1996-video-update-2023-da098a51ef91) | Simulator Effect, game design |
| [Micropolis: Constructionist Educational Open Source SimCity](https://donhopkins.medium.com/micropolis-constructionist-educational-open-source-simcity-79dce12e9e98) | Constructionism, OLPC |
| [Pie Menu Timeline](https://donhopkins.medium.com/pie-menu-timeline-9fd0ed2a36df) | Pie menus history |

### Academic & Historical References

- Packer et al. (2023). *MemGPT: Towards LLMs as Operating Systems*. [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- Ungar & Smith (1987). *Self: The Power of Simplicity*. OOPSLA.
- Rosenthal, D. *History of Window Systems*. [blog.dshr.org](https://blog.dshr.org/2023/01/history-of-window-systems.html)

---

*"Send programs, not data structures."*
*"The LLM is a linguistic motherboard."*
*"Eval incarnate — bad connotations turned good."*

🔮✨🐒
