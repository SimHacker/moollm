# Anthropic Skills → MOOLLM: Import Plan

> What to import, what to integrate into existing skills, what to leave alone.

## Ground Rules

1. **Don't duplicate what exists.** MOOLLM's `skill` skill already handles skill creation, instantiation, debugging, lifting. Don't create a second meta-skill.
2. **Import non-overlapping skills as new MOOLLM-native skills.** Give them the full Semantic Image Pyramid, advertisements, k-lines.
3. **Integrate IDEAS from overlapping skills into existing MOOLLM skills.** But discuss changes to core skills before touching them.
4. **MOOLLM-native means MOOLLM-native.** Imported skills depend on MOOLLM protocols freely. They're not ports — they're reimaginations.
5. **MOOLLM is platform-independent.** MOOLLM runs on Cursor today but must work on any LLM orchestrator. mooco is a design for a custom orchestrator that would enable advanced features (explicit context control, multiplayer, MCP coordination) but is not yet implemented. Skills can take advantage of mooco features when available but must have fallbacks. Think of `.moollm/hot.yml`, `cold.yml`, `working-set.yml` as advisory memory-mapped I/O — the orchestrator reads them if it can, the LLM reads them as context if not. Virtual device drivers, not hard dependencies.
6. **This is a design document, not a shipping plan.** These are ideas for things that would be powerful if built. No promises about timeline or implementation.

## Overlap Analysis

### OVERLAPS — integrate ideas, don't import as new skills

| Anthropic Skill | MOOLLM Equivalent | What To Steal |
|----------------|-------------------|---------------|
| skill-creator | `skill` (foundation) | Degrees-of-freedom framework, three-resource-type convention (scripts/references/assets) |
| brand-guidelines | `no-ai-ideology` / `persona` | Accent color cycling pattern, font fallback strategy |
| frontend-design | `no-ai-slop` + `visualizer` | Anti-slop blacklist for visual design, tone menu concept |
| doc-coauthoring | `adversarial-committee` + `speed-of-light` | Reader Testing via fresh sub-agents, shorthand response format |

**These should NOT become new skills.** Instead, adopt specific ideas into existing skills via targeted updates.

### DOES NOT OVERLAP — import as new MOOLLM-native skills

| Anthropic Skill | Why It's New | MOOLLM Integration Points |
|----------------|-------------|---------------------------|
| algorithmic-art | No generative art skill exists | visualizer, incarnation, adventure, image-mining, yaml-jazz |
| slack-gif-creator | No animation skill exists | visualizer, easing as mountable buff, adventure performances |
| pdf | No document processing skill exists | sister-script, sniffable-python, schema-factory |
| mcp-builder | No MCP server construction skill exists. Cursor runs MCP servers natively, cursor-mirror sees all active ones. mooco is designed to orchestrate MCP servers but is not yet implemented. | skill, prototype, experiment, github, cursor-mirror |

### MAYBE — worth discussing

| Anthropic Skill | Question |
|----------------|----------|
| pptx | Useful but massive (soffice.py C shim). Import or just reference? |
| docx | Same question. The soffice.py dependency is heavy. |
| xlsx | Same. The macro-writing-to-user-config is concerning. |
| theme-factory | Could be a persona costume for visualizer instead of a separate skill |
| webapp-testing | Could extend experiment skill instead of being standalone |

## Tier 1: Import These Now

### 1. `algorithmic-art` → MOOLLM `algorithmic-art`

**Why**: No generative art skill exists. The philosophy-then-expression pipeline is elegant. Seed-based reproducibility is a new capability.

**MOOLLM-native enhancements**:
- The art philosophy becomes an **incarnation** — a character with aesthetic values, not just a text block
- Gallery is an **adventure room** — walk through generated pieces as explorable objects
- Each piece gets **image-mining** (Three Eyes: structure, narrative, meaning)
- Series use **coherence-engine** to maintain visual DNA
- **yaml-jazz** sidecars per piece with semantic annotations
- **speed-of-light** simulates art critic, gallerist, and collector reacting to each piece
- The p5.js template is an **empathic-template**: `{{describe_artistic_philosophy}}`, `{{generate_algorithm_for philosophy}}`
- **advertisement**: ALGORITHMIC-ART activates when creative/generative contexts arise
- **skill-snitch-report.md** with dual-use analysis (generative art can be spam/deepfake generation at negative bias)

**Characters as stylesheets**: This philosophy-then-expression pattern applies far beyond p5.js generative art. It works for image generation prompts AND web page/site HTML+CSS+SVG generation. The lloooomm prototype (predecessor to MOOLLM) explored this deeply and fruitfully — characters as CSS stylesheets that can be mixed, matched, merged, combined, modulated. A patron saint like Bret Victor produces different CSS than one like Klaus Nomi. Mount both and you get explorable explanations with theatrical flair. This is the foundation for a future `web-publisher` skill.

**Does NOT touch**: any existing skill. Pure addition.

### 2. `slack-gif-creator` → MOOLLM `animation`

**Why**: No animation skill exists. The easing library, GIF optimization, and Slack-specific validators are genuinely useful. Rename to `animation` because it's more than Slack.

**MOOLLM-native enhancements**:
- Easing functions become **mountable buffs** — MOUNT `bounce-ease` ON character movement
- Style becomes a **persona costume** — animation style changes like a persona
- GIF series use **coherence-engine** for visual consistency
- **adventure** integration: animated room transitions, character action GIFs
- The validator pattern maps to **rubric** — measurable criteria for animation quality
- **advertisement**: ANIMATE activates when visual motion/transition is needed
- `gif_builder.py` already follows **sniffable-python** — zero changes needed, it's the gold standard

**Does NOT touch**: any existing skill. Pure addition.

### 3. `pdf` → MOOLLM `pdf`

**Why**: No document processing skill exists. 8 clean Python scripts. Real utility for any project that handles PDF forms, text extraction, or conversion.

**MOOLLM-native enhancements**:
- All scripts upgraded to **sister-script** pattern: argparse, `--json` output, CWD-independent
- `check_fillable_fields.py` gets `if __name__` guard (currently runs on import)
- `fill_fillable_fields.py` relative import fixed to CWD-independent
- **empathic-expressions**: fuzzy instructions → correct form values ("fill in the name field" → identifies correct field_id)
- **room**: each page is a room, navigate the document as space
- **image-mining**: Three Eyes on each page for structural analysis
- **advertisement**: PDF-OPS activates when PDF files are in context

**Does NOT touch**: any existing skill. Pure addition.

### 4. `mcp-builder` → MOOLLM `mcp-builder`

**Why**: No MCP skill exists. The factory pattern (stdio/SSE/HTTP connections) and evaluation harness are clean architecture. MCP is central to the Cursor/Claude ecosystem.

**MOOLLM-native enhancements**:
- MCP servers inherit from **prototype** — clone a template, override specifics
- Evaluation uses **experiment** (Drescher schema: hypothesis → test → result)
- Server quality assessed by **rubric** with measurable criteria
- **github** skill handles deployment (delegation pattern)
- **speed-of-light**: simulate multiple test scenarios in one call
- **skill-snitch**: auto-scan generated server for security patterns
- `connections.py` already follows best practices — pure library, type hints, ABC pattern

**Does NOT touch**: any existing skill. Pure addition.

## Tier 2: Integrate Ideas Into Existing Skills

### Ideas for `skill` skill (CAREFUL — core skill)

**Candidates to adopt** (small, additive, non-breaking):

1. **Degrees-of-freedom annotation**: Add to CARD.yml schema. Each method gets a `freedom:` field (high/medium/low). High = text instructions, medium = pseudocode, low = specific script. This is metadata, not behavioral change.

2. **Three-resource-type convention**: Document in SKILL.md that `scripts/` = executable, `references/` = context-loaded docs, `assets/` = output files never loaded. Some MOOLLM skills already follow this pattern (groceries, adventure). Formalizing it is documentation, not code change.

**NOT adopting** (too risky for a core skill):

- Anthropic's `init_skill.py` scaffolding — MOOLLM's `CREATE` method already handles this with empathic-templates
- Anthropic's frontmatter-only validation — MOOLLM's skill-snitch does deeper analysis
- Anthropic's `.skill` packaging format — premature for MOOLLM, different distribution model

### Ideas for `no-ai-slop` (additive)

- Anthropic's `frontend-design` anti-slop blacklist for visual design: ban Inter, Roboto, purple gradients, centered layouts. Add as a visual-slop extension.
- The tone menu concept (brutally minimal, maximalist chaos, retro-futuristic) could inform adventure room aesthetics.

### Ideas for `adversarial-committee` (additive)

- Anthropic's Reader Testing: fresh sub-agent with zero context tests document clarity. This is a specific adversarial-committee configuration worth documenting as a named pattern: "The Zero-Context Reader Test."

## What NOT To Import

| Skill | Why Not |
|-------|---------|
| brand-guidelines | Too simple for a standalone skill. Better as a persona costume. |
| internal-comms | Too Anthropic-specific. The dispatcher pattern is already documented. |
| theme-factory | Better as a mountable buff for visualizer than a separate skill. |
| web-artifacts-builder | Too framework-specific (React + Vite + shadcn). Heavy npm surface. |
| webapp-testing | Extend `experiment` instead. The `with_server.py` pattern is useful but not a full skill. |
| docx/pptx/xlsx | The soffice.py C compilation dependency is heavy. Reference as external tools, don't import. |

## Implementation Order

1. **algorithmic-art** — pure addition, most creative, best showcase of MOOLLM enhancements
2. **animation** (from slack-gif-creator) — pure addition, easing-as-buff is a novel integration
3. **pdf** — pure addition, most practical, needs sister-script upgrades
4. **mcp-builder** — pure addition, most relevant to the Cursor/Claude ecosystem
5. **Integrate ideas** into skill, no-ai-slop, adversarial-committee — last, after discussion

## Open Questions

1. Should imported skills keep Anthropic's Apache 2.0 license alongside MOOLLM's? Attribution in the lineage section.
2. Should we notify Anthropic that we're building MOOLLM-native versions of their skills? Good citizenship.
3. The `algorithmic-art` skill uses p5.js CDN — is that acceptable for a MOOLLM skill or should we bundle?
4. The `pdf` scripts have relative imports between each other — refactor to package or keep flat?

---

*Planned 2026-02-06. Pattern: Plan-Then-Execute.*
*Do not start implementation without reviewing this plan.*
