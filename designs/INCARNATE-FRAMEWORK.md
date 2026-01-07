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

Don Hopkins coined this phrase to describe [NeWS's and HyperLook's](https://donhopkins.medium.com/simcity-cellular-automata-and-happy-tool-for-hyperlook-d678b40347e9) unification of three dimensions around PostScript:

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

### 2. Smalltalk ([Alan Kay](https://donhopkins.medium.com/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-52e059ce0a68), Xerox PARC, 1970s)

Objects all the way down. Message passing. Live programming. "The computer is a medium."

**MOOLLM inherits:** Everything is an object (directory). Message passing (K-lines). Live editing (filesystem as state).

### 3. HyperCard (Bill Atkinson, Apple, 1987)

End-user programming. Reader = Writer symmetry. "See your own face in the system."

> *"Dan Winkler and Bill Atkinson violated a lot of important principles of 'good programming language design', but they achieved the first overall system in which end-users 'could see their own faces'."* — Alan Kay

**MOOLLM inherits:** Play-Learn-Lift. Users can inspect, modify, and create skills.

### 4. Self (Ungar & Smith, 1987)

Prototypes instead of classes. Delegation instead of inheritance. "Objects all the way down, but simpler."

**MOOLLM inherits:** Prototype-based skills. Delegation Object Protocol. Clone to instantiate.

### 5. NeWS (James Gosling, Sun, 1986)

Network-extensible window system. PostScript as the universal language. "Send programs, not data."

> *"A universal interpreter can both be quite small and also can have more degrees of freedom than any data structure (that is not a program)."* — Alan Kay

**MOOLLM inherits:** LLM as universal interpreter. Skills as programs. YAML Jazz as the universal language.

### 6. [HyperLook](https://donhopkins.medium.com/simcity-cellular-automata-and-happy-tool-for-hyperlook-d678b40347e9) (Arthur van Hoff, Turing Institute, 1989-1992)

HyperCard reimagined for NeWS. PostScript for code, graphics, AND data. Network delegation.

> *"Object => Card => Background => Stack => Client delegation"*

**MOOLLM inherits:** Object => Room => Parent => Skill => Prototype delegation. The Axis of Eval.

### 7. PostScript & The Linguistic Motherboard (John Warnock)

> *"PostScript is a linguistic 'mother board', which has 'slots' for several 'cards'. The first card we built was a graphics card. We're considering other cards..."*

**MOOLLM inherits:** LLM as linguistic motherboard. Skills as cards. `CARD.yml` is literal!

### 8. SimCity, The Sims, and [The Simulator Effect](https://donhopkins.medium.com/will-wright-on-designing-user-interfaces-to-simulation-games-1996-video-update-2023-da098a51ef91) (Will Wright)

> *"He designs games to run on two computers at once: the electronic one on the player's desk, running his shallow tame simulation, and the biological one in the player's head, running their deep wild imagination."*

**MOOLLM inherits:** Sparse state + LLM imagination = rich world. The LLM fills gaps.

### 9. Constructionism (Seymour Papert)

Learning by building inspectable things. Logo. Turtle graphics. "Low floor, high ceiling, wide walls."

**MOOLLM inherits:** The `constructionism` skill. Play-Learn-Lift as methodology.

---

## The Key Insights

### "Send Programs, Not Data Structures"

[Alan Kay's](https://donhopkins.medium.com/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-52e059ce0a68) insight from the JAM → PostScript evolution:

**Traditional systems:** Send data to a server, server parses it, server acts.
**PostScript/NeWS:** Send a *program* to the server, server *runs* it.

**Traditional LLM systems:** Send prompts (data), LLM generates response.
**MOOLLM:** Send skills (programs), LLM *interprets* them into behavior.

Skills are not documentation. Skills are **programs for the LLM to run**.

### "Browser Should Be OS, Not App"

[Alan Kay's](https://donhopkins.medium.com/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-52e059ce0a68) critique of the web:

> *"The underlying system for a browser should not be that of an 'app' but of an Operating System whose job would be to protectively and safely run encapsulated systems (i.e. 'real objects') gotten from the web."*

**MOOLLM applies this:** The LLM is not an app that processes prompts. The LLM is an **OS that runs skills**. Skills are "real objects" — encapsulated, instantiable, composable.

### Reader = Writer Symmetry

HyperCard's revolution: Anyone who can read a stack can edit it.

**MOOLLM:** Anyone who can play a game can learn its patterns and lift them into skills. The filesystem is readable AND writable. Play-Learn-Lift closes the loop.

### The Simulator Effect

Will Wright's insight: Players imagine more than the simulation contains.

**MOOLLM:** The LLM imagines more than the YAML contains. Sparse state + rich comments + LLM imagination = detailed world. We don't simulate everything — we imply it, and the LLM fills in.

---

## Incarnate Skills vs Traditional Skills

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

| Skill | Role |
|-------|------|
| `incarnation` | Gold-standard character creation |
| `skill` | Meta-skill for skill creation |
| `card` | Skills as playable cards |
| `empathic-expressions` | Code dimension (intent → code) |
| `empathic-templates` | Graphics + Data dimensions (smart generation) |
| `speed-of-light` | Many turns, one call |
| `prototype` | Self-style inheritance philosophy |

---

## Eval Incarnate

The phrase "Eval Incarnate" captures the dual meaning:

1. **Evaluation made executable** — Skills are not just descriptions, they run
2. **Bad connotations turned good** — Like "evil incarnate" but productive

It's tongue-in-cheek. It's a little edgy. It's memorable.

And it's TRUE: MOOLLM skills are **eval incarnate** — they are evaluations (assessments, judgments, behaviors) that have been given bodily form in the filesystem, ready to be instantiated and run.

---

## Related Documents

- [MEMGPT-ANALYSIS.md](./MEMGPT-ANALYSIS.md) — OS-inspired context management
- [MOOLLM-MANIFESTO.md](./MOOLLM-MANIFESTO.md) — Core philosophy
- [constitution-design.md](./constitution-design.md) — Ethical foundations
- [skills/skill/SKILL.md](../skills/skill/SKILL.md) — The meta-skill
- [skills/incarnation/SKILL.md](../skills/incarnation/SKILL.md) — Character creation protocol

---

## Credits & Lineage

| Person | Contribution | MOOLLM Connection |
|--------|--------------|-------------------|
| **Ivan Sutherland** | Sketchpad, first windows | Multiple views |
| **Alan Kay** | Smalltalk, Dynabook, "computer as medium" | Objects, messaging, vision |
| **Bill Atkinson** | HyperCard | Reader=Writer, Play-Learn-Lift |
| **David Ungar & Randy Smith** | Self | Prototypes, delegation |
| **James Gosling** | NeWS | Network interpreter |
| **Arthur van Hoff** | HyperLook | Axis of Eval, network delegation |
| **John Warnock** | PostScript | Linguistic motherboard |
| **Owen Densmore** | NeWS OOP | Dictionary-based objects |
| **Will Wright** | SimCity, Sims | Simulator Effect, action queues |
| **Seymour Papert** | Logo, Constructionism | Learning by building |
| **Marvin Minsky** | K-lines, Society of Mind | Name-based activation |
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
| [SimCity, Cellular Automata, and Happy Tool for HyperLook](https://donhopkins.medium.com/simcity-cellular-automata-and-happy-tool-for-hyperlook-d678b40347e9) | HyperLook, Axis of Eval, NeWS |
| [Alan Kay on "Should web browsers have stuck to being document viewers?"](https://donhopkins.medium.com/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-52e059ce0a68) | NeWS, HyperLook, linguistic motherboard |
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
