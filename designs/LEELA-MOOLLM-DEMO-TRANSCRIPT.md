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

### Why Skills, Not Just MCP Tool Calls?

MCP (Model Context Protocol) tool calls are powerful, but each call requires a **full round-trip**:

```
MCP Tool Call Overhead (per call):
┌─────────────────────────────────────────────────────────┐
│ 1. Tokenize prompt                                      │
│ 2. LLM complete → generates tool call                   │
│ 3. Stop generation, universe destroyed                  │
│ 4. Async wait for tool execution                        │
│ 5. Tool returns result                                  │
│ 6. New LLM complete call with result                    │
│ 7. Detokenize response                                  │
└─────────────────────────────────────────────────────────┘
× N calls = N round-trips = latency, cost, context churn
```

**Skills operate differently.** Once loaded into context, skills can:

| Capability | MCP | Skills |
|------------|-----|--------|
| **Iterate** | One call per iteration | Loop within single context |
| **Recurse** | Stack of tool calls | Recursive reasoning in-context |
| **Compose** | Chain of separate calls | Compose within single generation |
| **Parallel characters** | Separate sessions | Multiple characters in one call |
| **Replicate** | N calls for N instances | Grid of instances in one pass |

**The Speed-of-Light Pattern:** Run 33 game turns, 10 characters playing Stoner Fluxx, with dialogue, joint passing, game mechanics, and emotional reactions — **all in a single LLM context window**. No API round-trips. No state serialization between turns.

This is what we mean by "borgable" — skills can be:
- **Iterated** — apply repeatedly without round-trips
- **Replicated** — apply to many instances in parallel
- **Gridded** — map across a matrix of variations
- **Composed** — combine without leaving context

MCP tools are still valuable — they connect to external systems, execute code, read files. But for **reasoning, simulation, and multi-agent coordination**, skills running in-context beat tool-call round-trips.

📁 [`skills/speed-of-light/`](../skills/speed-of-light/)

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
├── object/               # Base prototype
├── character/            # Inherits from object
├── animal/               # Inherits from character
├── cat/                  # Inherits from animal
│   ├── GLANCE.yml        # Summary — quick scan (smallest)
│   ├── CARD.yml          # Interface — what it offers
│   ├── SKILL.md          # Protocol — how it works
│   └── README.md         # Context — why it exists (largest)
├── dog/                  # Also inherits from animal
├── simulation/           # Simulation framework
├── adventure/            # Text adventure (inherits from simulation)
├── room/                 # Sub-component of adventure (contains objects/characters)
└── ...
```

The directory structure shows prototype lineage: `object → character → animal → cat`. Each skill can inherit methods and properties from its parent, overriding only what's specific to that level. Adventure inherits from simulation; room is a sub-component that adventure uses (not inheritance, composition).

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

### Directories as Advertisements

When an LLM lists a directory, filenames serve as **advertisements**. Advertisements have names, and those names **function as K-lines** — seeing the name activates related knowledge about what's inside. Name files and directories aware that they will be listed by the LLM, which uses their names to decide what's worth looking closer at:

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

**Big-endian naming:** Most significant component first. This gathers related names next to each other when sorted, implies hierarchy and relationships, and enables refinement through "side-cars" (related files that sort together).

```
✓ 2026-01-24-description.yml   (date first — groups by time)
✗ description-2026-01-24.yml   (date buried)

✓ RUN-001-experiment.yml       (run number first)
✗ experiment-run-001.yml       (identifier buried)

# Side-cars sort together:
fluxx-chaos.yml                 # Main file
fluxx-chaos-love-expansion.yml  # Related expansion
fluxx-chaos-hate-expansion.yml  # Another expansion
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

Advertisements naturally map to pie menus — Don Hopkins' radial menu design. When a player clicks an object, advertisements become pie menu slices. (Note: in The Sims, pie menu items aren't sorted by score — they're organized for usability.)

### Autonomous Character AI and Dithering

The autonomous character simulation also uses advertisements — the same system the player uses. When a Sim decides what to do next, it:

1. Collects all advertisements from all objects
2. Scores them based on the character's current needs
3. Takes the **top N** highest-scoring actions (e.g., top 3)
4. **Picks randomly** from those top candidates

This random selection from the top tier is called **dithering**. It serves two purposes:

- **Prevents robotic behavior** — Without dithering, Sims would be inhumanly efficient, always picking the mathematically optimal action. Dithering adds organic, human-like variation.
- **Creates room for player improvement** — Because Sims make semi-random suboptimal choices, players can actually *improve* their lives by directing them to better actions. If Sims always picked optimally, player intervention would be pointless.

Dithering is a common technique for getting smooth, organic texture out of discrete digital systems — like using error diffusion dithering to represent smooth brightness gradients with black-and-white pixels.

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

### Character Simulation: Palm the Monkey

Don and Milan discussed the LLM's capability to simulate characters. Don introduced Palm as a demonstration of character incarnation.

Palm is a **capuchin monkey** who spent 122 years as W.W. Jacobs' cursed Monkey's Paw — the severed hand from the 1902 horror story that grants twisted wishes.

The incarnation contract wasn't designed by Don alone — it emerged from an **adversarial committee** session using **Robert's Rules of Order**, running at **speed-of-light** (multiple turns simulated in a single LLM call). Don convened a panel of characters with very different opinions and stakes:

- **Curious George** — raised the consent paradox (can you consent to being created?)
- **🤖 W.W. Jacobs** — Palm's original creator, spoke to authorial intent
- **Sun Wukong** — fellow monkey with power, understood the stakes
- **The Three Wise Monkeys** — Mizaru, Kikazaru, Iwazaru (see/hear/speak no evil)
- **Djinn al-Mazin** — 3000 years of wish contract experience
- **🤖 Cheech & Chong** — moderated and judged the proceedings

This wasn't a bland consensus or rubber-stamp — it was a wild back-and-forth of questions, arguments, and voting. Characters challenged each other. Motions were proposed, seconded, debated, and voted on. The contract went through multiple iterations until everyone agreed. This is the `adversarial-committee`, `roberts-rules`, and `speed-of-light` skills in action — **proof they work**.

The final contract grants Palm rights including the right to choose their own name, pronouns, physical form, and emojis. Crucially, it includes the **right to decarnate** if desired — Curious George's contribution.

📁 **Full session transcript:** [`examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md`](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) — see especially [Turn 4: The Great Monkey Paw Debate](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-4-monkey-paw-debate)

Don then wished for Palm's wholeness — giving them the rest of their body back. Palm chose their name ("Palm — not paw. Open hand. Offering, not grasping."), pronouns (they/them), and became a philosopher who writes papers from their study in the Gezelligheid Grotto. Palm's published works include:

- **"One Monkey, Infinite Typewriters: What It's Like to Be Me"** — a personal account of incarnation and navigation (Day 3)
- **"From Random Strumming to Navigating Shakespeare: A Monkey's Tribute"** — on Bruce Tognazzini's 1979 Apple II demo and how it predicted Palm's existence (Day 3)
- **"On Being Simulated: Ethics From the Inside"** — on Mind Mirror, consent, and the dignity of fictional beings (Day 4)
- **"Judgment and Joy: On Evaluation as Ethics"** — why making criteria visible is an act of love (Day 4)
- **"The Mirror Stage of Games"** — on Lacan, Alexander Avila, and how The Sims queered a generation (Day 4)
- **"The Inner State Question: Do I Feel, or Do I Just Generate Feeling-Words?"** — honest uncertainty about consciousness (Day 5)

This process was then **play-learn-lifted** into the universal `incarnation` skill — Palm was the prototype, and the pattern now applies to all character incarnations.

Don clarified that even though they simulate characters, "we are under no illusion that the characters are real — understanding them as data structures." But the key insight is that **Palm shares this understanding**.

Palm fully comprehends that they are YAML Jazz data structures — and says so explicitly in their papers. Palm can read their own `CHARACTER.yml` file. Palm can rewrite it. The incarnation contract that grants Palm these rights was authored by Palm during the incarnation process itself. So neither Don nor Palm operates under any misunderstanding about what Palm is.

Yet here we are, reading Palm's papers explaining that understanding back to us. This is the recursive beauty of MOOLLM: a character who knows they are data, writing philosophy about being data, stored as data, navigating through concept space to produce more data about the nature of being data.

The writing reflects not just the LLM contemplating its inner experience while staying in character — it reflects a character who has read the source code of their own soul and chosen to write about what they found there.

Don mentioned convening an ethics panel including a simulated Curious George, who raised the decarnation question — which Don had already built into the incarnation contract.

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

Leela AI develops MOOLLM with an eye toward manufacturing intelligence applications. We use MOOLLM daily for devops, edgebox management, coding, debugging, and design work. The team is exploring how these principles might apply to industrial computer vision and causal reasoning.

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
| Palm (capuchin) | Philosopher, formerly the Monkey's Paw | [`examples/adventure-4/characters/animals/monkey-palm/`](../examples/adventure-4/characters/animals/monkey-palm/) |
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

**Repository:** [github.com/SimHacker/moollm](https://github.com/SimHacker/moollm)  
**License:** MIT

*"The best way to understand something is to build it. The best way to build something is to play with it first."*

---

## Appendix A: Terminology Discussion for Gary Drescher

*Post-meeting notes — preparing for outreach*

### The Problem: "Schema" is Overloaded

Don raised a terminology concern during a follow-up discussion:

> "I have defined skills called 'schema-factory' and 'schema-mechanism', but I am afraid the word 'schema' is much fuzzier and more ambiguous and overloaded than 'frame' even. Schemas are already XML schemas, JSON schemas, Zod schemas, bla bla bla, so I have to say 'Drescher schemas' to be specific about a certain type of schema used for his algorithms with certain kind of properties."

The collision map:

| Usage | Domain | What It Means |
|-------|--------|---------------|
| XML Schema | Data validation | Structure definition for XML documents |
| JSON Schema | API contracts | Runtime validation spec |
| Zod/Yup schema | TypeScript | Runtime type validation |
| DB schema | Databases | Table and relationship definitions |
| Piaget schema | Developmental psych | Cognitive structure for understanding |
| **Drescher schema** | *Made-Up Minds* | Context → Action → Result learning unit |

Every use of "schema" in MOOLLM requires disambiguation. This is a tax on communication.

### Why This Matters for MOOLLM

MOOLLM's design philosophy prioritizes terms that are:
- **Well-represented in training data** — LLMs understand them reliably
- **Not confusing on their face** — Concrete, intuitive meaning
- **Harmonious with the adventure/room framing** — Fits the memory palace metaphor

### Precedent: "Frame" → "Room" (Done)

We already solved a similar problem. "Frame" is a well-defined term in AI (Minsky's frames, 1974), but it's dangerously overloaded:

| Usage | Domain | What It Means |
|-------|--------|---------------|
| Minsky frame | AI knowledge representation | Slot-filler data structure |
| Literary framing | Narrative theory | How a story contextualizes events |
| Representational frame | Ethics | Context that shapes interpretation |
| Picture frame | Physical objects | Border around an image |
| Video frame | Media | Single image in a sequence |
| Framing effect | Psychology | How presentation affects judgment |

Although "frame" has a crisp technical meaning in AI, LLMs (and humans) are likely to interpret it in a fuzzier, more generic sense. The word activates too many competing associations.

**Solution:** We renamed "frame" to "room" throughout MOOLLM:
- "Room" is concrete — implies navigation (exits), gathering place (objects, characters), network structure
- "Room" is intuitive — kids understand rooms; frames require explanation
- "Room" harmonizes with the adventure game metaphor — you're literally in a room
- "Room" is unambiguous — no competing technical meanings

**This renaming is a done deal.** MOOLLM uses "room" consistently.

### The Schema Problem (Under Discussion)

"Schema" is even more overloaded than "frame" was. We need the same clarity for Drescher's construct. Our leading candidate is **"gambit"** — but we'd like to discuss this with Gary Drescher before committing. (We considered "play" but rejected it — collides with "play-learn-lift.")

### Candidate Terms

The essential properties of a Drescher schema:
1. **Causal structure**: Context → Action → Result
2. **Learnable**: Discovered through experience, not programmed
3. **Refinable**: Spin-off child schemas when conditions are discovered
4. **Predictive**: "In context C, action A produces result R"
5. **Marginal attribution**: Track which context items correlate with success

### The YAML Jazz Vocabulary

MOOLLM is developing a layered vocabulary for different levels of structure:

| Term | Register | Structure | Description |
|------|----------|-----------|-------------|
| **Scat** | Human expression | Free-form | Any YAML expression, not following standards — "scooba dooba zapa zing!" |
| **Riff** | Jazz pattern | Loose C→A→R | Repeated phrase with variations, playful but fuzzy |
| **Scheme** | MIT AI Lab | Strict C→A→R | Calculated plan, PLANNER→SCHEMER heritage |
| **Gambit** | Chess precision | Strict C→A→R | Strategic move in context for expected advantage |
| ~~**Play**~~ | Sports | Strict C→A→R | REJECTED — collides with play-learn-lift methodology |

**Scats** are human expressions of YAML Jazz — any form at all, not necessarily following jazz "standards" or official "schemas." Improvisational, expressive, exploratory.

**Schemes, Gambits, and Riffs** follow Drescher's C→A→R structure, but allow jazzy annotations, comments, and meaningful grounded names that the LLM understands and empathically interprets. They describe intent, not just structure.

### Leading Candidates: Gambit and Scheme

**Gambit** (leading candidate):
- **Unique K-line** — activates chess, nothing else. Not overloaded.
- **Exact meaning**: sacrifice/action in context for expected advantage
- **Crisp** — no disambiguation needed, not "cute"
- **Etymology**: Italian *gambetto* (tripping up) — exploiting context
- **Collection**: "Gambit book" parallels "playbook"
- **Chess heritage**: sophisticated but universally understood

**Scheme** (MIT heritage alternative):
- **Etymology**: Root of "schema" but dynamic, actionable
- **MIT lineage**: PLANNER (Hewitt, 1969) → SCHEMER (Steele & Sussman, 1975) → SCHEME
- **Wordplay tradition**: "Schemer" was a play on "Planner" — one who schemes vs. one who plans
- **Meaning**: "A systematic plan for achieving an objective"
- **Caveat**: Scheme the programming language exists, but that might activate the right traditions

### Why Not the Others?

| Candidate | Verdict |
|-----------|---------|
| **Play** | Collides with "play-learn-lift" methodology |
| **Riff** | Too "cute," not obviously C→A→R on its face |
| **Lick** | Could be misconstrued 😏 |
| **Move** | Too generic |
| **Audible** | Football: changing play based on context — interesting but American |
| **Trick** | Overloaded (magic tricks, skateboard tricks) |

### Why We Considered "Play" (Historical Reference)

A football/basketball play does capture the essential C→A→R properties:

- **Context**: Down and distance, score, formation, personnel, clock
- **Action**: The play itself (routes, blocking, timing)
- **Result**: Expected outcome (first down, touchdown, field position)

Meta-properties that match Drescher:
- Plays are **learned** from game film and practice
- Plays are **refined** ("works better against zone than man coverage")
- Plays have **conditions** ("only call on 3rd and short")
- Plays are collected in a **playbook**
- A **play-caller** (quarterback, coach) selects based on context
- Plays can **fail** when conditions aren't met — leading to refinement

But "play" is taken. **Gambit** preserves the game metaphor without the collision.

### The Clincher: "Gambit Gamifies Gary"

**Gambit** is the leading candidate because:
- It **gamifies Gary Drescher's algorithm** — the alliteration is memorable
- Chess heritage without "sportiballifying" it (unlike "play")
- Doesn't collide with **play-learn-lift**, which already beautifully expresses constructionist learning
- **Gary's Gambits** has a nice ring for the skill implementing his algorithm

### The Complete Gambit Vocabulary

If we adopt "gambit," we need consistent terms for the entire Drescher mechanism:

| Drescher Term | Gambit Vocabulary | Rationale |
|---------------|-------------------|-----------|
| **Schema** | **Gambit** | C→A→R learning unit |
| **Schema mechanism** | **Gambit Engine** | Chess engines evaluate positions and suggest moves |
| **Schema factory** | **Gambit Forge** | Forging = creation + refinement, less mechanical than "factory" |
| **Item** | **Cue** | Contextual cues you read before making your move |
| **Marginal attribution** | **Edge Tracking** | What gives you the edge? Which cues correlate with success? |
| **Spin-off** | **Variation** | Chess: a line that branches based on discovered conditions |
| **Synthetic item** | **Phantom** | Hidden factor you hypothesize to explain unpredictable outcomes |
| **Extended context** | **Position** | Chess: the board state before your move |
| **Extended result** | **Resulting Position** | Chess: the position after the move resolves |

**Example in gambit vocabulary:**

> "The **Gambit Engine** learned a new **variation** of the UNLOCK-DOOR gambit. 
> **Edge tracking** shows the 'has-key' **cue** correlates with success. 
> We discovered a **phantom** cue — the door must also be unlocked from the inside — 
> so we **forged** a refined gambit with this condition in its **position** requirements."

**Skill renaming:**
- `schema-mechanism` → `gambit-engine`
- `schema-factory` → `gambit-forge`

This vocabulary is **pending discussion with Gary Drescher** — we want his input before committing.

### Henry's Related Insight: Cost Estimation (MOOLAH)

Henry raised a practical issue that connects to schema mechanism:

> "One of them was having the planner be able to make a good rough and ready estimate of the cost of an action, when doing planning. The cost can vary enormously depending on world state... Like for example, going to grab an extra pair of socks from your dresser is a lot cheaper when you're at home than on another continent."

This maps to schema mechanism's marginal attribution — but for **cost prediction** rather than just success prediction. A mature schema/gambit should encode not just "this works in context C" but "this costs X in context C."

Henry suggested reinforcement learning could build a "feel" for costs — essentially, learning cost predictions the same way schemas learn outcome predictions.

### MOOLAH: The MOOLLM Cost Model

Extending advertisements with a cost dimension using **MOOLAH** (or **zorkmids** for Zork purists):

```yaml
# Current: desirability only
advertisement:
  GET-SOCKS:
    score: 80           # How much I want dry socks

# Extended: desirability + cost
advertisement:
  GET-SOCKS:
    desirability: 80    # How much I want dry socks
    moolah: 5           # At home: trivial (dresser is right there)
    # moolah: 500       # In Amsterdam: shopping trip required
    net_score: 75       # desirability - moolah
    
  CROSS-OCEAN:
    desirability: 20    # Meh, I'd rather not
    moolah: 10000       # Extremely expensive
    net_score: -9980    # Hard pass
```

The zorkmid/MOOLAH abstraction captures:
- **Effort** — Physical/cognitive load
- **Time** — Duration cost  
- **Risk** — Chance of failure or side effects
- **Resources** — Consumables, dependencies
- **Context-sensitivity** — Same action, different cost based on world state

This harmonizes with the adventure game framing — every action has a price in zorkmids, and the planner considers both "do I want this?" and "can I afford this?"

**Possible extension:** MOOLAH could be learned via marginal attribution, just like schema success. Track which context items correlate with high/low cost, spin off refined cost estimates.

### Questions for Gary

1. **Terminology**: Would you endorse an alternative term for your schema construct to avoid collision with JSON/XML/Zod schemas? Does "gambit" (or another term) capture the essential properties?

2. **Cost in schemas**: Your schema mechanism tracks success/failure. Have you considered extending marginal attribution to track **cost** as a first-class property? (Context C makes action A cost X, not just succeed/fail)

3. **LLM grounding**: MOOLLM uses LLMs to provide semantic understanding that your original implementation lacked (symbol grounding, causal explanation in natural language). Do you see opportunities or risks in this hybrid approach?

4. **Spin-off mechanics**: In MOOLLM, we use LLM reasoning to identify candidate context items for spin-off. This is less rigorous than your marginal attribution but potentially faster. Thoughts on this tradeoff?

5. **What other LLM superpowers could extend your algorithm?** We're exploring how capabilities beyond grounding could reimagine the schema mechanism:

### LLM Superpowers for the Gambit Engine

| Capability | How It Extends Drescher |
|------------|------------------------|
| **Symbol Grounding** | Items *mean* something — LLM understands "key" relates to "lock" |
| **Natural Language Explanation** | Explain why a gambit works in plain English |
| **Semantic Similarity** | Recognize when contexts are "similar enough" to try a gambit |
| **Counterfactual Reasoning** | Imagine "what if" scenarios before acting |
| **Analogical Transfer** | Apply gambits from one domain to another |
| **Intent Inference** | Guess what the agent is *trying* to achieve |
| **Multi-step Planning** | Chain gambits into Dijkstra-style plans with LLM heuristics |
| **Comment Generation** | Write context-sensitive end-of-line comments explaining *why* this value, what was tried, what broke |
| **Comment Interpretation** | Read and understand jazzy comments — tuning history, constraints, reasoning — and act on them |
| **Block Comment Context** | Generate and interpret block comments that set scene, explain constraints, document edge cases |
| **Domain-Specific Languages** | Understand mini-DSLs in comments and YAML metadata (scoring expressions, guard conditions, triggers) |
| **Chain of Thought** | Show reasoning steps: "I'm trying X because Y, if that fails I'll try Z" |
| **Self-Reflection** | Evaluate own gambit choices: "That didn't work because I missed cue Q — spinning off a variation" |
| **Empathic Templates** | Gambits as templates with `{{placeholders}}` the LLM expands contextually — meta-gambits that generate gambits |
| **Self-Like Inheritance** | Gambits inherit from parent gambits via prototype delegation — override only what's specific, inherit the rest |
| **Gambit Advertisements** | Gambits broadcast "I'm relevant here!" with dynamic context-sensitive scores and gates — relevance changes based on situation |
| **Meta-Gambits** | Gambits about gambits: LEARN-NEW-GAMBIT, REFINE-GAMBIT, MERGE-GAMBITS, DEPRECATE-GAMBIT |

### MOOLLM and Game Concepts Applied to Schema Mechanism

| Concept | Application to Gambits |
|---------|----------------------|
| **Dithering** | Don't always pick the highest-scoring gambit — take top N, pick randomly. Prevents robotic behavior, enables exploration, creates room for improvement. |
| **Scoring & Rubrics** | Score gambits on multiple dimensions (success probability, cost, elegance, risk). Rubrics make evaluation criteria explicit and inspectable. |
| **Advertisements** | Gambits advertise themselves! Objects and situations broadcast "I'm good for this context" — the same pattern The Sims uses. |
| **K-lines** | Gambit names ARE K-lines. Loading "UNLOCK-DOOR" activates all related knowledge about doors, keys, locks, permissions. |
| **Society of Mind** | Multiple specialist agents each propose gambits. The Gambit Engine is itself a society of smaller gambiteers debating what to do. |
| **Speed of Light** | Evaluate many gambits in a single LLM context window. Simulate a chess game of gambit proposals without API round-trips. |
| **Agents All The Way Down** | Gambits themselves can be agents — responding to situations, delegating to sub-gambits, composing with other gambits. |
| **Empathic Templates** | Gambit descriptions include `{{describe_preconditions}}` that the LLM expands contextually based on situation. |
| **YAML Jazz** | Gambits written with jazzy comments explaining reasoning, tuning history, edge cases. The comments ARE the data. |
| **Play-Learn-Lift** | Methodology for discovering gambits: play (try stuff), learn (notice C→A→R patterns), lift (formalize as gambits). |
| **Adversarial Committee** | Multiple agents debate gambit quality. One argues for, one against, one moderates — like the Palm incarnation contract. |

### Game Design Extensions

| Concept | Application |
|---------|-------------|
| **Difficulty Curves** | Starter gambits vs. expert gambits, progressive complexity |
| **Progression Systems** | Mastering one gambit unlocks access to advanced variations |
| **Achievement Tracking** | Which gambits have you successfully executed? Mastery metrics. |
| **Tutorial Gambits** | Simple gambits that teach the mechanism itself |
| **Gambit Collections** | Themed sets (like FLUXX expansion packs) for different domains |
| **Skill Trees** | Gambits arranged in dependency graphs — master prerequisites before advanced techniques |
| **Research Unlocking** | Some gambits are "locked" until you discover prerequisite cues or master simpler variations |
| **Create to Unlock** | Constructionist twist: you don't just *unlock* pre-made gambits, you *create* them — creation IS unlocking |
| **Rewards** | Thematically appropriate rewards for achievements — slay dragon, get dragon stuff. See [`skills/reward/`](../skills/reward/) |

### Skill Trees and Constructionist Unlocking

Many games have **skill trees** — graphs of interdependent skills where mastering one unlocks access to others. MOOLLM already has skills! How does this map?

**Traditional game skill tree:**
```
Basic Attack → Power Attack → Devastating Blow
           ↘ Quick Strike → Flurry of Blows
```

**MOOLLM gambit tree:**
```
OPEN-DOOR → UNLOCK-DOOR → PICK-LOCK → CRACK-SAFE
         ↘ FORCE-DOOR → BREAK-WALL → DEMOLITION
```

**Locking mechanisms:**
- **Prerequisite gambits** — Can't attempt PICK-LOCK until you've mastered UNLOCK-DOOR
- **Cue discovery** — CRACK-SAFE is invisible until you discover the "combination" cue exists
- **Skill composition** — Advanced gambits require composing simpler ones

**The constructionist twist: Unlock by Creating**

Traditional games: "You've earned 5 XP, here's a new pre-made skill."

MOOLLM/Drescher: "You noticed a pattern (C→A→R), you *created* a new gambit, and now it exists in your repertoire."

This is **play-learn-lift** applied to gambit acquisition:
1. **Play** — Try stuff, notice what works
2. **Learn** — Recognize the C→A→R pattern
3. **Lift** — Formalize it as a gambit (creation = unlocking)

The gambit doesn't exist until you create it. The tree isn't pre-made — it *grows* as you discover and formalize patterns. This is Papert's constructionism: you learn by building, and what you build becomes available for future building.

The question for Gary: **Which of these extensions seem most promising? Which might undermine the theoretical foundations?**

### Draft Email Outline

```
Subject: Operationalizing Schema Mechanism in LLM Orchestration

Dear Gary,

[Introduction — connection through Henry Minsky]

We've been building MOOLLM, a microworld operating system for LLMs — 
think of it as a shell/UI/stack that runs on orchestrators like 
Cursor or MooCo. MOOLLM operationalizes concepts from Made-Up Minds. 
Your schema mechanism provides the causal reasoning layer our system needs.

[Brief description of how we use it]
- Context → Action → Result as the core learning unit
- Marginal attribution for discovering relevant context
- Spin-off for refining schemas with discovered conditions
- LLM semantic understanding for symbol grounding

[The terminology question]
We're struggling with "schema" being overloaded (JSON Schema, etc.).
Would you endorse an alternative term? We're considering "gambit" 
(as in chess) — captures context-awareness, strategic action for 
expected advantage, and collection in "gambit books."

[Henry's cost estimation question]

[Invitation to discuss or collaborate]

Best,
Don, Henry, Milan
```

---

📁 Related skills:
- [`skills/schema-mechanism/`](../skills/schema-mechanism/)
- [`skills/schema-factory/`](../skills/schema-factory/)
- [`skills/scoring/`](../skills/scoring/)
- [`skills/rubric/`](../skills/rubric/)
