# Anthropic Skills x MOOLLM — Upgrade Opportunities

> What happens when you take Anthropic's clean, well-designed skills and add MOOLLM's unique capabilities? Each upgrade uses specific MOOLLM extensions that vanilla skills can't access.

## The MOOLLM Advantage Stack

| MOOLLM Extension | What It Adds | Vanilla Skills Can't |
|-----------------|-------------|---------------------|
| **speed-of-light** | Multi-turn simulation in one LLM call | Simulate debates, reviews, iterations without API round-trips |
| **empathic-templates** | `{{describe_X}}` semantic generation | Templates that understand intent, not just string replace |
| **empathic-expressions** | Fuzzy input → correct output | Accept pseudocode, wrong syntax, incomplete specs |
| **prototype** | Clone and customize, don't configure | Skills inherit from parents, override what's different |
| **mount** | GRANT abilities, AFFLICT constraints | Temporarily add capabilities without modifying base skill |
| **advertisement** | Objects announce what they can do | Scored relevance — right skill surfaces at right time |
| **visualizer** | Context → image with style consistency | Consistent visual series across a project |
| **coherence-engine** | LLM maintains consistency across state | Multi-file, multi-entity consistency without orchestrator |
| **character** | Body, location, inventory, relationships | Skills can have personas with knowledge domains |
| **incarnation** | Gold-standard character creation | Characters with ethical framing and patron saints |
| **room** | Directory as activation context | Skill behavior changes based on where you are |
| **adventure** | Filesystem as navigable world | Explore skill output as rooms |
| **buff** | Temporary effects (curses = shitty buffs) | Time-limited modifications to skill behavior |
| **needs** | Sims motivations drive behavior | Skills that respond to urgency, not just requests |
| **dual-use analyzer** | Invertibility + bias detection | Self-aware skills that document their own dual-use surface |

---

## Tier 1: High-Impact Upgrades (build these first)

### 1. skill-creator → MOOLLM Skill Creator

**Original**: Anthropic's meta-skill that teaches how to create new skills. Degrees-of-freedom framework. Progressive disclosure pyramid. 6-step lifecycle.

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| Templates | String replacement | **empathic-templates**: `{{describe_purpose}}`, `{{generate_examples}}`, `{{appropriate_tier}}` fill themselves |
| Inheritance | Copy-paste from examples | **prototype**: New skills clone from parent prototypes, override only what's different |
| Structure | Manual file creation | Generate full Semantic Image Pyramid (GLANCE → CARD → SKILL → README) |
| Validation | `quick_validate.py` checks structure | **skill-snitch** integration: auto-scan generated skill for security patterns |
| Documentation | Manual README writing | **sister-script** pattern: the skill IS the documentation |
| Quality | Manual review | **advertisement**: generated skill declares its own capabilities with scored relevance |
| Security | None | **dual-use analyzer**: generated skill includes its own invertibility assessment |

**Key integration**: The generated skill comes out as a full MOOLLM citizen — GLANCE.yml, CARD.yml with advertisements and k-lines, SKILL.md with methods, skill-snitch-report.md pre-populated. Not just a SKILL.md in a folder.

**Patron saint**: Anthropic (they designed the format). **Familiar**: The Skill Forge (MOOLLM's enhanced version).

---

### 2. doc-coauthoring → MOOLLM Collaborative Intelligence

**Original**: 3-stage document creation with Reader Testing via fresh Claude sub-agents.

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| Reader Testing | Fresh Claude instance | **speed-of-light**: simulate 3-5 reader personas in ONE call, each with different expertise |
| Persona | Generic "reader" | **character**: each reader has a persona (technical, executive, newcomer, skeptic) |
| Multi-perspective | Sequential sub-agents | **adversarial-committee**: readers with incompatible values debate the document |
| Debate | None | **debate** + **roberts-rules**: structured deliberation on document quality |
| Context | Info dump | **room**: document sections are rooms, navigate between them |
| Style | Generic | **mount no-ai-slop**: AFFLICT the document with syntactic hygiene during drafting |
| Version | Linear | **coherence-engine**: maintains consistency across sections as they evolve |

**Key integration**: Reader Testing becomes a full adversarial committee. Instead of one generic reader, you get The Engineer (checks technical accuracy), The Executive (checks clarity), The Newcomer (checks assumptions), The Skeptic (challenges claims) — all simulated in one speed-of-light call.

---

### 3. frontend-design → MOOLLM Design System

**Original**: Anti-AI-slop design guidelines with tone menu and variation mandate.

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| Anti-slop | Blacklist of fonts/colors | **mount no-ai-slop**: AFFLICT on the design process, plus no-ai-gloss for copy |
| Style selection | Manual tone choice | **advertisement**: design approaches broadcast scored relevance based on project context |
| Consistency | Manual tracking | **coherence-engine**: maintains visual consistency across generated components |
| Variation | "NEVER converge" mandate | **visualizer** + **buff**: each generation gets a temporary style buff that forces different aesthetics |
| Theme | Manual color/font picking | **empathic-templates**: `{{appropriate_palette_for project}}`, `{{generate_typography_for tone}}` |
| History | None | **room**: each design iteration is a room you can revisit and compare |

**Key integration**: The design skill becomes self-aware about what it's already generated. The coherence-engine tracks visual decisions (this project uses Fira Code, this blue, this grid) and enforces consistency without the designer repeating themselves. The variation mandate becomes structural — the buff system ensures each generation differs.

---

### 4. algorithmic-art → MOOLLM Generative Art Studio

**Original**: Philosophy-then-expression pipeline for p5.js generative art. Seed-based reproducibility.

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| Philosophy | Text manifesto | **incarnation**: the art philosophy becomes a CHARACTER with worldview, aesthetic values, references |
| Expression | Single p5.js output | **visualizer**: multi-modal output (p5.js + image + YAML description) |
| Series | Manual seed management | **coherence-engine**: series maintains visual DNA across pieces |
| Exploration | Linear generate-then-view | **adventure**: gallery as navigable rooms, each piece is an artifact you examine |
| Critique | None | **speed-of-light**: simulate art critic, gallerist, and collector reacting to the piece |
| Mining | None | **image-mining**: Three Eyes (structure, narrative, meaning) analyze generated art |
| Metadata | Seed + parameters | **yaml-jazz**: every piece gets a YAML sidecar with semantic annotations |

**Key integration**: The art studio becomes an adventure room. Walk through your gallery. Each piece is an object you can EXAMINE at three levels (glance, look, examine). The philosophy manifesto is an incarnated character who explains their artistic intent. Series maintain visual coherence automatically.

---

## Tier 2: Medium-Impact Upgrades (build after Tier 1)

### 5. mcp-builder → MOOLLM MCP Forge

**Original**: Build MCP servers with research → implement → review → evaluate pipeline.

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| Evaluation | Claude API calls | **speed-of-light**: simulate multiple test scenarios in one call |
| Testing | Sequential test cases | **experiment**: structured hypothesis → test → result schema (Drescher) |
| Patterns | Reference docs | **prototype**: MCP servers inherit from parent templates, override specifics |
| Security | Manual review | **skill-snitch**: auto-scan generated server for security patterns |
| Documentation | Manual | **sister-script**: generated server IS its own documentation |

**Patron saint**: The MCP spec authors. **Familiar**: Tux (inherits the github skill's ops knowledge).

---

### 6. pptx → MOOLLM Presentation Engine

**Original**: PowerPoint with mandatory adversarial QA. "If you found zero issues, you weren't looking hard enough."

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| QA | Sub-agent visual inspection | **speed-of-light**: simulate designer, audience member, and accessibility reviewer simultaneously |
| Themes | 10 color palettes | **empathic-templates**: `{{appropriate_theme_for audience_and_topic}}` |
| Content | Manual slide writing | **mount no-ai-slop + no-ai-hedging**: AFFLICT on content creation |
| Narrative | Linear slide order | **adventure**: presentation as a room sequence, navigate non-linearly |
| Consistency | Manual visual tracking | **coherence-engine**: enforces visual language across all slides |
| Speaker notes | Manual | **character**: create a presenter persona who generates natural speaker notes |

**Key integration**: The adversarial QA becomes a speed-of-light simulated audience. Three personas react to each slide: The Visual Designer ("that gradient clashes"), The Content Expert ("slide 7 contradicts slide 3"), The Audience Member ("I'm lost, what's the main point?").

---

### 7. pdf → MOOLLM Document Intelligence

**Original**: PDF toolkit with 8 clean Python scripts.

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| Reading | Text extraction | **image-mining**: Three Eyes on each page (structure, narrative, meaning) |
| Forms | Field filling | **empathic-expressions**: fuzzy instructions → correct form values |
| Analysis | Manual review | **room**: each page is a room, navigate the document as space |
| Batch | Sequential processing | **speed-of-light**: analyze multiple pages simultaneously |
| Metadata | Manual | **yaml-jazz**: YAML sidecar per document with semantic annotations |

---

### 8. brand-guidelines → MOOLLM Brand DNA

**Original**: Pure data — colors + fonts. Simplest possible skill.

**MOOLLM Upgrade**:

| Feature | Vanilla | MOOLLM Enhanced |
|---------|---------|----------------|
| Application | Manual checking | **mount**: GRANT brand-guidelines to any creative skill, they inherit the palette |
| Enforcement | Hope the LLM remembers | **buff**: brand DNA as a persistent buff on all design skills |
| Extension | Edit the YAML | **prototype**: new brands clone from this one, override specifics |
| Multi-brand | One brand per file | **persona**: switch brand identity like a costume |
| Context | Always applied | **advertisement**: brand guidelines surface only when design tasks are active |

**Key integration**: Brand guidelines become a mountable buff. MOUNT `brand-guidelines` ON `frontend-design` → the design skill now enforces Anthropic's palette automatically. MOUNT a different brand → different palette. The brand is a costume (persona) the design skill wears.

---

## Tier 3: Experimental Upgrades (explore as research)

### 9. internal-comms → MOOLLM Communication Hub

Mount `no-ai-slop` + `no-ai-gloss` + `no-ai-hedging` on all communications. Use `speed-of-light` to simulate how different audiences will receive the message. Use `character` to write in the voice of different departments.

### 10. webapp-testing → MOOLLM Test Theatre

Tests become adventures. Each test scenario is a room. Test results are objects you examine. Failed tests are puzzles to solve. The test runner has a character (the QA Gremlin) who delights in finding bugs.

### 11. slack-gif-creator → MOOLLM Animation Studio

Easing functions become buffs. Style becomes a mountable persona. GIF series maintain coherence. Each frame is explorable via PSIBER.

---

## Implementation Plan

### Phase 1: Foundations (skill-creator + doc-coauthoring)

These two establish the meta-patterns. Once MOOLLM Skill Creator exists, it generates all future upgraded skills. Once Collaborative Intelligence exists, it validates all document-producing skills.

### Phase 2: Creative Tools (algorithmic-art + frontend-design + brand-guidelines)

These three form a creative suite. Brand DNA mounts on design skills. Art Studio produces visual assets. Design System enforces quality. All share the coherence-engine for cross-project consistency.

### Phase 3: Document Suite (pptx + pdf)

Build on Phase 2's visual infrastructure. Presentations and documents use the same brand DNA, same anti-slop hygiene, same adversarial QA.

### Phase 4: Developer Tools (mcp-builder + webapp-testing)

Build on Phase 1's meta-skill infrastructure. MCP Forge uses the skill-creator pattern. Test Theatre uses the adventure pattern.

---

## What Makes These "MOOLLM Upgraded"

Every upgraded skill:

1. **Has a GLANCE → CARD → SKILL → README** (Semantic Image Pyramid)
2. **Declares advertisements** with scored relevance
3. **Inherits from prototype** (clone and customize)
4. **Can be mounted** on characters or rooms
5. **Has a skill-snitch-report** with dual-use analysis
6. **Uses empathic-templates** for semantic generation
7. **Supports speed-of-light** multi-turn simulation
8. **Maintains coherence** via coherence-engine
9. **Documents its own limitations** honestly
10. **Follows no-ai-* hygiene** (slop, gloss, hedging, moralizing)

The vanilla Anthropic skills are good. The MOOLLM upgrades make them citizens of an ecosystem where skills talk to each other, inherit from each other, mount on each other, and maintain consistency across a project.

---

*Documented 2026-02-06. Pattern: Play-Learn-Lift.*
*PLAY: Scan Anthropic's skills. LEARN: Map MOOLLM capabilities to upgrade opportunities. LIFT: Design the upgraded skill suite.*
