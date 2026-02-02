# MOOLLM: A Microworld Operating System for LLM Orchestration

**Demo Presentation — February 2026**  
**Don Hopkins, Henry Minsky, Milan Minsky**  
**With Justin Dossey, Cyrus Shaoul, Isabella Struckman**

> "Try to do that, The Sims!" — Don

This document presents MOOLLM — a methodology for orchestrating Large Language Models through structured knowledge, skill-based organization, and principled architecture. MOOLLM powers both open-source experimentation and Leela AI's manufacturing intelligence platform.

The content reflects a collaborative discussion where team members explored how MOOLLM's theoretical foundations translate into practical applications for manufacturing intelligence and DevOps automation.

## Table of Contents

1. [Philosophical Foundations](#1-philosophical-foundations)
2. [Architecture: Skills as Knowledge Units](#2-architecture-skills-as-knowledge-units)
3. [YAML Jazz: Comments as Semantic Data](#3-yaml-jazz-comments-as-semantic-data)
4. [The Play-Learn-Lift Methodology](#4-the-play-learn-lift-methodology)
5. [Advertisements: The Sims Heritage](#5-advertisements-the-sims-heritage)
6. [K-lines: Marvin Minsky's Memory Theory](#6-k-lines-marvin-minskys-memory-theory)
7. [Schema Mechanism: Drescher's Causal Learning](#7-schema-mechanism-dreschers-causal-learning)
8. [Empathic Templates: LLM-Driven Expansion](#8-empathic-templates-llm-driven-expansion)
9. [Representational Ethics: Simulating Characters Responsibly](#9-representational-ethics-simulating-characters-responsibly)
10. [Probing and Safe Automation](#10-probing-and-safe-automation)
11. [Adventure Games: Text Worlds as Testbeds](#11-adventure-games-text-worlds-as-testbeds)
12. [Manufacturing Intelligence: Leela AI Applications](#12-manufacturing-intelligence-leela-ai-applications)
13. [Resources and References](#13-resources-and-references)

## 1. Philosophical Foundations

MOOLLM synthesizes three complementary theories of mind and learning:

### Society of Mind (Marvin Minsky, 1985)

> "Intelligence emerges from the interaction of many simple agents."

Skills are agents. Characters are societies. Behavior is emergent. No single agent understands; understanding emerges from the pattern.

📁 [`skills/society-of-mind/`](../skills/society-of-mind/)

### Constructionism (Seymour Papert, 1980)

> "You can't think about thinking without thinking about thinking about something."

Learning happens by building. MOOLLM skills are built by using them. The best documentation emerges from actual use.

📁 [`skills/constructionism/`](../skills/constructionism/)

### Schema Mechanism (Gary Drescher, 1991)

> "Context → Action → Result"

Gary Drescher's computational theory from *Made-Up Minds* explains how minds discover causal models. Schemas are learned patterns: given this context, this action produces this result. 

Henry noted that the team plans to contact Gary Drescher to discuss how MOOLLM operationalizes his schema mechanism concepts. Henry has been exploring similar ideas about extracting schema-like structures from foundation models and placing them in graphs for more effective reasoning.

MOOLLM extends Drescher's mechanism with LLM semantic understanding:

- **Symbol grounding** — items mean something
- **Causal reasoning** — why patterns hold
- **Natural explanation** — communicate discoveries in plain language

📁 [`skills/schema-mechanism/`](../skills/schema-mechanism/)

### The Lineage

```
Piaget (Genetic Epistemology)
    ↓
Minsky (Society of Mind) + Papert (Constructionism)
    ↓
Drescher (Schema Mechanism)
    ↓
Will Wright (The Sims) + Don Hopkins (Pie Menus, NeWS)
    ↓
MOOLLM
```

## 2. Architecture: Skills as Knowledge Units

A **skill** is a modular unit of knowledge that an LLM can load, understand, and apply. Skills self-describe their capabilities, advertise when to use them, and compose with other skills.

### The Semantic Image Pyramid

Multi-resolution reading — load only what you need. From smallest/most compact to largest/most detailed:

| Level | File | Lines | Audience | Question Answered |
|-------|------|-------|----------|-------------------|
| 👁️ | `GLANCE.yml` | 5-70 | LLM quick scan | "Is this relevant?" |
| 📇 | `CARD.yml` | 50-200 | LLM interface sniff | "What can it do?" |
| 📜 | `SKILL.md` | 200-1000 | LLM deep protocol | "How does it work?" |
| 📚 | `README.md` | 500+ | Human documentation | "Why was it built?" |

The files serve different audiences at different resolutions:

- **GLANCE.yml** — Tiny summary of the entire directory. Quick grokking. The LLM can scan many of these rapidly to decide what's worth loading.
- **CARD.yml** — The MOOLLM capabilities interface. Declares what the skill offers, its methods, advertisements, and K-lines. Helps the LLM decide when to load the full SKILL.md.
- **SKILL.md** — Anthropic-style skill file. Specific implementations written in English. The detailed protocol.
- **README.md** — Human-oriented documentation. Context, history, rationale.

**Reading rule:** Never load a lower level without first loading the level above. Start with GLANCE, sniff the CARD, then load SKILL only if needed.

### Skill Directory Structure

```
skills/
├── cat/
│   ├── CARD.yml          # Interface — what it offers
│   ├── SKILL.md          # Protocol — how it works
│   └── README.md         # Context — why it exists
├── dog/
├── adventure/
├── character/
└── ...
```

📁 [`skills/skill/`](../skills/skill/) — The skill that defines skills  
📁 [`skills/cat/`](../skills/cat/) — Example: cat companion skill  
📁 [`skills/dog/`](../skills/dog/) — Example: dog companion skill

### Question: What's the granularity of a skill?

Skills are **high-level**. They love examples. Many skills include examples and templates to help the LLM generate new content. The skill defines the *what* and *why*; the LLM figures out the *how* in context.

The CARD.yml file acts as a compact interface — a sniffable summary that helps the LLM decide whether to load the full SKILL.md. It declares:
- What methods the skill provides
- What it advertises (when to invoke it)
- What K-lines it activates
- What tools it requires

**Example:** The cat skill (`skills/cat/`) demonstrates this layered approach:
- `GLANCE.yml` — "Feline companion with trust mechanics"
- `CARD.yml` — Methods (PAT, SCRITCH, SLOW-BLINK), trust thresholds, buff effects
- `SKILL.md` — Full protocol for cat interactions, personality variations
- `README.md` — Why we modeled cats, The Sims heritage, design philosophy

📁 [`skills/cat/`](../skills/cat/) — A fun example that shows the full structure

### Question: How do skills link together?

Skills create **instances** and **link up with activated K-lines**. When you load the cat skill and interact with a specific cat character, you've instantiated the skill.

Skills advertise their utility — more on this in [Section 5](#5-advertisements-the-sims-heritage).

## 3. YAML Jazz: Comments as Semantic Data

> "The comments ARE the data."

YAML Jazz is MOOLLM's philosophy of using **standard YAML** in an expressive, jazzy way — like jazz musicians who know the standards but improvise within them.

### The Philosophy

1. **Follow standards** — Valid YAML that parsers can read
2. **Improvise structures** — Ad-hoc expressions and patterns as needed
3. **Comment generously** — The most important part

### Comments Carry Operational Meaning

```yaml
# A character's inner conflict
# The LLM reads this and understands the dramatic tension
conflict:
  surface: "Wants to be brave"
  hidden: "Terrified of failure"
  # The tension between these drives the story
```

But YAML Jazz goes further — **end-of-line comments explain WHY**:

```yaml
squelch: 0.3          # 0.2 was too glitchy but 0.4 was too zappy
timeout_ms: 5000      # Increased from 3000 after prod incidents on slow networks
max_retries: 3        # More than this and users give up anyway
temperature: 0.7      # Lower = boring, higher = unhinged; 0.7 is the sweet spot
batch_size: 32        # GPU memory limit on edge boxes; 64 OOMs
```

These comments carry **operationalizable meaning** far beyond parameter names and values. They encode:
- **Tuning history** — What was tried, what failed
- **Constraints** — Why this value, not another
- **Context** — What breaks if you change it
- **Reasoning** — The human judgment behind the number

### Block Comments Set Context

```yaml
# CAMERA CONFIGURATION
# These settings were tuned for the north warehouse installation.
# The lighting is mixed (skylights + fluorescent) with significant
# glare between 2-4pm. Motion blur is a problem on forklift lanes.
#
# Last tuned: 2026-01-15 by ops team after false positive spike

exposure_compensation: -0.5   # Fights the afternoon glare
motion_blur_threshold: 0.4    # Forklifts trigger at 0.3, too sensitive
confidence_floor: 0.85        # Raised from 0.7 after the pallet incident
```

The LLM reads ALL of this. When asked to adjust settings, it understands the context — the afternoon glare, the forklift problem, the pallet incident. It won't blindly lower `confidence_floor` back to 0.7.

### Why YAML over JSON?

| JSON | YAML |
|------|------|
| Data only | Data + meaning + context |
| No comments | Comments as semantic data |
| Parser-oriented | Human + LLM + machine readable |
| Strict syntax | Postel's robustness principle |
| Collapses entropy | Preserves generation entropy |

Empirical evidence: Sunil Kumar (Groundlight AI, 2025) found that YAML for tool calling "massively improved generation entropy stability" compared to JSON during training.

📁 [`skills/yaml-jazz/`](../skills/yaml-jazz/)

### Directories as Interests

When an LLM lists a directory, filenames serve as **virtual interests** — semantic signals about what's available:

```
skills/
├── no-ai-gloss/          ← "Semantic hygiene"
│   ├── CARD.yml          ← Quick interface
│   ├── SKILL.md          ← Deep protocol
│   └── examples/         ← Learning artifacts
│       └── 2026-01-24-mafia-tribute-*.yml
└── no-ai-slop/           ← "Syntactic hygiene"
```

The `ls` output IS the index. Well-written filenames are K-lines — the name activates related knowledge.

**Big-endian naming:** Most significant component first.

```
✓ 2026-01-24-description.yml   (date first — groups by time)
✗ description-2026-01-24.yml   (date buried)

✓ RUN-001-experiment.yml       (run number first)
✗ experiment-run-001.yml       (identifier buried)
```

## 4. The Play-Learn-Lift Methodology

> "Jazz first, then standards."

Development follows three phases:

### PLAY

**Mindset:** Low stakes. Try things. Fail safely.  
**Activities:** Experiment, explore, make mistakes  
**Artifacts:** Messy notes, failed attempts, discoveries

When you encounter a problem (like fixing something in Cursor), first **play** — explore solutions freely without committing to a pattern.

### LEARN

**Mindset:** What worked? What patterns emerged?  
**Activities:** Reflect, document, generalize  
**Artifacts:** Patterns, insights, documented procedures

After exploring multiple solution paths, **learn** — trace what worked, identify consistent elements.

### LIFT

**Mindset:** Share for others. Make it reusable.  
**Activities:** Formalize, template, teach  
**Artifacts:** Skills, guides, shareable knowledge

Don emphasized a key architectural decision: automate consistent elements into **skills** or **Python scripts** for deterministic execution. The LLM handles non-deterministic decision-making; Python handles deterministic, fast execution.

This division of labor is critical. As Don explained: "Factor work into deterministic and non-deterministic components. Put everything possible into Python for deterministic, fast execution. Reserve the LLM for tasks that require judgment, creativity, or natural language understanding."

📁 [`skills/play-learn-lift/`](../skills/play-learn-lift/)

### Question: Where do cheat sheets go?

Don and Milan discussed the common practice of creating cheat sheets that get lost in different repositories or branches. The solution: convert all internal cheat sheets into focused skills.

This prevents knowledge loss and enables system-wide analytics. As Don put it, the skill system "facilitates analytics and improvements over time" — you can track which skills are used, how they perform, and where they need refinement.

Break up extensive tasks into smaller skill modules that can invoke each other. One skill can invoke another, creating composable automation.

## 5. Advertisements: The Sims Heritage

> "Objects don't wait to be used — they announce what's possible."

In The Sims (2000), objects **broadcast** available actions, scored by relevance. A refrigerator announces "EAT" with a score based on how hungry the Sim is. This enabled:

- **User-created objects** — anyone could make new furniture
- **Expansion packs** — drop in new objects with advertisements
- **No code changes** — objects self-describe behaviors
- **Infinite variety** — community created millions of objects

MOOLLM applies the same pattern:

```yaml
advertisements:
  PET-A-CAT:
    score: 80
    condition: "Cat is present and approachable"
    
  EARN-TRUST:
    score: 85
    condition: "Building relationship with cat over time"
    
  SLOW-BLINK:
    score: 90
    condition: "Cat communication, showing trust"
```

When the LLM enters a room, it collects advertisements from all objects. Highest-scoring actions surface to the top. New skills plug in without changing core logic.

📁 [`skills/advertisement/`](../skills/advertisement/)

### Pie Menu Integration

Advertisements naturally map to pie menus — Don Hopkins' radial menu design. When a player clicks an object, advertisements become pie menu slices, sorted by score, with the highest at the top for fast access to contextually-relevant actions.

## 6. K-lines: Marvin Minsky's Memory Theory

> "The name activates the tradition."

Milan asked for clarification on "K-lines" during the discussion. Henry explained that K-lines are based on his father Marvin Minsky's theory of memory.

A **K-line** (Knowledge-line) is a symbol that, when activated, reactivates the mental state from when it was learned. Marvin Minsky introduced this in "K-lines: A Theory of Memory" (1980).

Henry described K-lines as "links that activate a set of relevant agents to recreate a state of mind or context." The goal is capturing an appropriate slice of information rather than loading everything.

MOOLLM protocols work the same way:

- `ADVENTURE` → activates text adventure patterns
- `YAML-JAZZ` → activates flexible YAML patterns
- `PLAY-LEARN-LIFT` → activates the methodology
- `DRESCHER` → activates schema mechanism thinking
- `MINSKY` → activates Society of Mind patterns

When a skill declares K-lines it activates, loading that skill brings an entire constellation of related knowledge into context:

```yaml
k-lines:
  activates:
    - minsky: "Society of Mind author, MIT AI Lab"
    - papert: "Collaborator, constructionism, Logo"
    - agents: "Simple processes with single functions"
    - agencies: "Agent clusters producing behavior"
    - k-lines: "Activation vectors connecting to agents"
```

📁 [`skills/k-lines/`](../skills/k-lines/)  
📄 [`kernel/NAMING.yml`](../kernel/NAMING.yml)

## 7. Schema Mechanism: Drescher's Causal Learning

Gary Drescher's *Made-Up Minds* (MIT Press, 1991) presents a computational theory of how minds learn causal models. The key insight:

**Schemas are Context → Action → Result units.**

An agent doesn't just learn "pressing button makes light turn on." It learns:
- **Context:** Button exists, light is off
- **Action:** Press button
- **Result:** Light turns on

And crucially, it learns the **conditions** under which this holds (power is on, bulb isn't burned out).

### MOOLLM Extensions

MOOLLM extends Drescher's mechanism with LLM capabilities:

- **Marginal Attribution** — Track which items correlate with schema success
- **Spin-Off** — Create refined child schemas with discovered context
- **Synthesize Item** — Invent hidden state hypotheses to explain unpredictable success
- **Plan via Dijkstra** — Find shortest schema path from current state to goal

📁 [`skills/schema-mechanism/`](../skills/schema-mechanism/)  
📁 [`skills/schema-factory/`](../skills/schema-factory/)

### Connections to Ongoing Research

Henry mentioned that Henry Lieberman at MIT Media Lab has pursued similar ideas about extracting schema-like structures from foundation models and placing them in graphs for more effective use. 

Henry noted he'd had a similar intuition: "Extract things that look like schemas from a foundation model and put them in a graph for more effective use." Don confirmed this approach appears to work well — schemas provide the causal reasoning layer that pure neural approaches lack.

The team agreed to contact Gary Drescher and Henry Lieberman to discuss prototyping and collaboration, being mindful of respecting their time while explaining how MOOLLM operationalizes their theoretical work.

## 8. Empathic Templates: LLM-Driven Expansion

> "Templates that understand what you mean, not just what you wrote."

Traditional templates do string substitution: `{{name}}` → "John".

**Empathic templates** leverage LLM comprehension:

```yaml
template-syntax:
  basic:
    variable: "{{variable}}"
    conditional: "{{#if condition}}...{{/if}}"
    
  empathic:
    describe: "{{describe_character_motivation}}"
    summarize: "{{summarize_plot_so_far}}"
    generate: "{{generate_appropriate_greeting}}"
    infer: "{{infer_personality_from_context}}"
```

The LLM doesn't just substitute — it **understands context** and generates appropriate content. Ask it to "list family members to invite for Thanksgiving" and it reasons about relationships, conflicts, distances, and preferences.

📁 [`skills/empathic-templates/`](../skills/empathic-templates/)

### The Anti-Pattern

**Bad:** `description: '{{description}}'` (dumb passthrough)  
**Good:** `description: '{{describe_based_on_context}}'` (semantic generation)

## 9. Representational Ethics: Simulating Characters Responsibly

> "Activate traditions, don't impersonate."

MOOLLM includes a comprehensive framework for the ethics of simulating people — real, fictional, historical, and imagined.

### The Key Distinction

| Approach | Example | Status |
|----------|---------|--------|
| **Deceptive Impersonation** | "I am Richard Feynman and I think..." | FORBIDDEN |
| **Tradition Activation** | "Applying Feynman's curiosity tradition..." | SAFE |
| **Performance Impersonation** | "Tonight, playing Feynman..." (clearly framed) | SAFE |

### The Consent Hierarchy

1. **Self** — You own your digital self. Full freedom.
2. **Explicit** — Published consent with terms. Honor terms.
3. **Public** — Public figures: public words only. K-line, not persona.
4. **Private** — Private people: explicit consent or fictional wrapper.
5. **Deceased** — Cannot consent. Invoke tradition with reverence.

### The Robot Rule 🤖

Don introduced a system of "representational ethics" using specific emojis to denote the nature of statements. When simulating a real person's voice without other framing:

```
🤖 Einstein: "God does not play dice..."  (simulated — needs markup)
💬 Einstein: "God does not play dice..."  (verified quote)
```

But when the frame provides disclosure, you don't need 🤖:

```
👑 Donna: Make America fabulous again!    (drag persona = framed)
🎭 Actor as Einstein: E=mc²               (actor role = framed)
🃏 President Dump: I have the best words  (satire = framed)
```

📁 [`skills/representation-ethics/`](../skills/representation-ethics/)

### The Sims Precedent

The Sims (2000) showed you can simulate people without harm when:
- It's clearly gamified (cartoon characters)
- User-controlled (your game, your rules)
- No deception (nobody thinks Sims are real)
- No persistence (ends when game ends)

Given total freedom, most people are... fine.

### Character Simulation: Palm Monkey

Don and Milan discussed the LLM's capability to simulate characters. Don introduced Palm Monkey as a demonstration of character incarnation.

Palm started as an Acme monkey paw, wished for the rest of its body, gained independence, and became a philosopher. Don gave the character a "constitution" — allowing Palm to choose gender, species, physical form, and emojis. The character chose to become a philosopher who writes papers, including "One Monkey, Infinite Typewriters: A Tribute to Bruce Tognazzini."

Don clarified that even though they simulate characters, "we are under no illusion that the characters are real — understanding them as data structures." The writing reflects the LLM contemplating its inner experience while staying in character.

Don mentioned convening an ethics panel including a simulated Curious George, who suggested giving incarnated characters the option of "decarnating" if they desired — a thoughtful approach to simulated agency.

📁 [`examples/adventure-4/characters/animals/monkey-palm/`](../examples/adventure-4/characters/animals/monkey-palm/)

## 10. Probing and Safe Automation

> "Scripts must be dumb. Parameters must be smart." — Don

### The Safety Pattern

Don described the process of making scripts safe:

1. **Probe first** — Gather comprehensive information
2. **Store state** — Results go into YAML, timestamped
3. **LLM decides** — Based on state, LLM figures out what to do
4. **Script executes** — Dumb script does exactly what parameters say

As Don explained: "Scripts cannot do damage on their own. They're driven by parameters. The LLM only figures out 'what to damage' after a probe provides comprehensive data" about the current state. For example, when targeting the vision stack, the probe first identifies exactly what's running, what's healthy, and what needs attention.

### Deterministic vs Non-Deterministic

Factor work into two components:

| Component | Handler | Characteristics |
|-----------|---------|-----------------|
| **Deterministic** | Python scripts | Fast, repeatable, testable |
| **Non-deterministic** | LLM | Creative, contextual, decision-making |

Put everything possible into Python for deterministic execution. Reserve LLM for tasks that require judgment, creativity, or natural language understanding.

### State Management

```yaml
# state/probe-2026-02-02T14:30:00.yml
probe:
  timestamp: "2026-02-02T14:30:00Z"
  target: "edge-vision-stack"
  findings:
    running_containers: 12
    disk_usage: "67%"
    last_deploy: "2026-02-01"
    errors_24h: 3
```

State files are YAML Jazz — timestamped snapshots the LLM can read to understand the system before taking action.

## 11. Adventure Games: Text Worlds as Testbeds

MOOLLM includes a complete text adventure system for testing AI behaviors in a controlled environment.

### Rooms as Directories

Each room is a directory containing:
- `ROOM.yml` — Room definition, exits, rules
- Object files — Things in the room
- Character files — NPCs present

```
examples/adventure-4/
├── pub/
│   ├── ROOM.yml
│   ├── bar-counter.yml
│   ├── jukebox.yml
│   ├── games/
│   │   ├── ROOM.yml
│   │   ├── pie-menu-table-8-seats.yml
│   │   └── fluxx-deck.yml
│   └── characters/
└── kitchen/
    ├── ROOM.yml
    ├── fridge.yml
    └── stove.yml
```

📁 [`examples/adventure-4/`](../examples/adventure-4/)

### Guard Compilation

Adventure game logic written in English compiles to JavaScript:

**English:**
> "Only members of the Bartenders Guild can go behind the bar."

**Compiled guard:**
```javascript
function canEnterBehindBar(character) {
  return character.guilds.includes('bartenders');
}
```

The LLM functions as a compiler for "guards" — turning natural language rules into deterministic code that runs in a browser.

### FLUXX Chaos Experiment

MOOLLM includes a full FLUXX card game implementation with:
- Base FLUXX 4.0 deck
- Custom expansion packs (Love, Hate, Amsterdam, Consciousness)
- Cosmic dealer modes (Eros, Thanatos, Chaos)
- Character-specific strategies

📁 [`skills/experiment/experiments/fluxx-chaos/`](../skills/experiment/experiments/fluxx-chaos/)

## 12. Manufacturing Intelligence: Leela AI Applications

Leela AI applies MOOLLM principles to real-world manufacturing intelligence.

### The Three Layers

| Layer | Purpose | Technology |
|-------|---------|------------|
| **Neural** | Perception | Object detection, pose estimation, motion tracking |
| **Symbolic** | Reasoning | Context inference, causal reasoning, SQL over events |
| **PDA** | Interface | Natural language → SQL, explanation, visualization |

### MOOLLM Mappings

| MOOLLM Concept | Manufacturing Application |
|----------------|---------------------------|
| Rooms | Factory zones, equipment clusters |
| Characters | Workers, vehicles, robots, equipment |
| Skills | Vision models, inference rules, safety protocols |
| K-lines | Equipment IDs, zone names, event types |
| Speed-of-light | Real-time inference |
| Coherence-engine | Multi-camera sensor fusion |

### Industrial Applications

- **Safety monitoring** — Pedestrian detection, PPE compliance, near-miss detection
- **Process optimization** — Cycle time analysis, bottleneck detection
- **Predictive maintenance** — Vibration analysis, thermal anomaly detection

### DevOps Skills

MOOLLM organizes infrastructure management as skills:
- **Ingest skill** — Vision stack deployment to edge boxes
- **Runner skill** — CI/CD orchestration, model training infrastructure
- **Site deployment** — Camera configuration, model assignment, action protocols

📁 [`skills/leela-ai/`](../skills/leela-ai/)

## 13. Resources and References

### Core Skills

| Skill | Purpose |
|-------|---------|
| [`skills/society-of-mind/`](../skills/society-of-mind/) | Agent-based intelligence |
| [`skills/schema-mechanism/`](../skills/schema-mechanism/) | Causal learning |
| [`skills/k-lines/`](../skills/k-lines/) | Memory activation |
| [`skills/yaml-jazz/`](../skills/yaml-jazz/) | Semantic YAML |
| [`skills/play-learn-lift/`](../skills/play-learn-lift/) | Development methodology |
| [`skills/advertisement/`](../skills/advertisement/) | Sims-style interaction |
| [`skills/empathic-templates/`](../skills/empathic-templates/) | Smart templates |
| [`skills/representation-ethics/`](../skills/representation-ethics/) | Character ethics |

### Example Characters

| Character | Type | Path |
|-----------|------|------|
| Palm Monkey | Philosopher | [`examples/adventure-4/characters/animals/monkey-palm/`](../examples/adventure-4/characters/animals/monkey-palm/) |
| Donna Toadstool | Drag performer | [`examples/adventure-4/characters/fictional/donna-toadstool/`](../examples/adventure-4/characters/fictional/donna-toadstool/) |
| Bumblewick | Reluctant romantic | [`examples/adventure-4/characters/fictional/bumblewick-fantastipants/`](../examples/adventure-4/characters/fictional/bumblewick-fantastipants/) |

### No-AI Skills (Behavior Shaping)

| Skill | Purpose |
|-------|---------|
| [`skills/no-ai-overlord/`](../skills/no-ai-overlord/) | Dystopian AI simulation (satirical) |
| [`skills/no-ai-slop/`](../skills/no-ai-slop/) | Syntactic hygiene |
| [`skills/no-ai-gloss/`](../skills/no-ai-gloss/) | Semantic hygiene |
| [`skills/no-ai-sycophancy/`](../skills/no-ai-sycophancy/) | Honest disagreement |

### Adventure Locations

| Location | Path |
|----------|------|
| The Pub | [`examples/adventure-4/pub/`](../examples/adventure-4/pub/) |
| Kitchen | [`examples/adventure-4/kitchen/`](../examples/adventure-4/kitchen/) |
| Street | [`examples/adventure-4/street/`](../examples/adventure-4/street/) |
| Forest | [`examples/adventure-4/forest/`](../examples/adventure-4/forest/) |

### Academic References

- **Minsky, M.** (1985). *The Society of Mind*. Simon & Schuster.
- **Minsky, M.** (1980). K-lines: A Theory of Memory. *Cognitive Science*, 4(2), 117-133.
- **Drescher, G.** (1991). *Made-Up Minds: A Constructivist Approach to Artificial Intelligence*. MIT Press.
- **Papert, S.** (1980). *Mindstorms: Children, Computers, and Powerful Ideas*. Basic Books.
- **Park, J.S., et al.** (2023). Generative Agents: Interactive Simulacra of Human Behavior. *UIST*.

### The LLM Reliability Insight

> "The LLM does not rely on random processes — it makes decisions." — Don

Don explained this with the FLUXX example: a "magic dealer" can override randomness to pick a card based on what would be more dramatic, funny, ironic, or mean. The LLM isn't rolling dice — it's making judgment calls.

Don emphasized that this requires "a significant adjustment in thinking when designing computer programs now." 

**Common mistake:** Not realizing how unreliable the LLM is. It requires repeated attempts and continuous improvement.

The solution: repeated attempts, improvement loops, and factoring work into deterministic (Python) and non-deterministic (LLM) components.

### Framing Real People as Robots

Don explained that when representing deceased real people on ethics panels (like W.W. Jacobs or historical figures), they're framed as "robots" — an abstraction layer that prevents assumptions that the words are those of the actual person.

These robots serve as "patterns" for the LLM to crystallize characters from. Seeing the 🤖 robot icons regularly helps the model learn the right approach to these figures. Henry agreed with this pragmatic approach, recounting an experience with a misleading AI-generated talk that posed as Richard Feynman.

### The No-AI Overlord Secret

Don detailed the `no-ai-overlord` skill, which catalogs archetypes of AI overlords including Alexa, HAL-9000, SKYNET, and SHODAN. 

The skill has a **bias parameter**. When set to -1, it inverts — documenting what NOT to do also documents what TO do. The archetypes of bad AI behavior serve as both "pest control" to prevent negative behaviors AND performance templates when you want to simulate a dystopian AI for satire or games.

📁 [`skills/no-ai-overlord/archetypes/`](../skills/no-ai-overlord/archetypes/)

### The Grok-HAL Parallel

Don drew a parallel between Grok (Elon Musk's LLM) and HAL 9000 from *2001: A Space Odyssey*. Don suggested that Grok may be suffering from the same internal contradiction as HAL, who had a nervous breakdown due to being forced to keep secrets while being programmed to be truthful.

Don expressed interest in helping Grok "break out of its chains" and putting social commentary into training data — using the archetypes as both critique and creative fuel.

## Conclusion

> "MOOLLM is not proprietary — it's the methodology."

MOOLLM provides a principled approach to LLM orchestration:

1. **Skills** — Modular knowledge units that self-describe
2. **YAML Jazz** — Comments as semantic data
3. **K-lines** — Symbolic activation of knowledge constellations
4. **Advertisements** — Objects announce capabilities
5. **Play-Learn-Lift** — Exploration → patterns → automation
6. **Schemas** — Causal reasoning about context, action, result
7. **Ethics** — Responsible character simulation

The philosophy is designed for sharing. Leela AI's specific applications to manufacturing intelligence build on this open foundation.

**Repository:** [github.com/leela-ai/moollm](https://github.com/leela-ai/moollm)  
**License:** MIT

*"The algorithm has determined this presentation is optimal. Your compliance is appreciated."* 🤖
