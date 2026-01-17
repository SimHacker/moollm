# 🎭 Many Voices, Not One: The Ensemble Update

> *"No single story is true — but the ensemble approximates actionable wisdom."*
> — Mike Gallaher

## The Numbers

```
27 commits
286 files changed
+31,951 lines / -17,707 lines
151 new files | 38 deleted (PROTOTYPE.yml → SKILL.md migration)
54 skills now Anthropic-compatible (37 new SKILL.md files)
```

## The Big Ideas

### 1. 🎪 Many Voices, Not One

Traditional chat gives you **the statistical center** — an averaged, hedged, genre-conventional answer that misses the outliers that actually matter.

MOOLLM now simulates an **ensemble of perspectives** within ONE LLM call:

```yaml
# One LLM epoch contains:
characters: 5       # Maya (paranoid), Frankie (idealist), Vic (evidence), Tammy (systems)
debate_rounds: 4    # Robert's Rules forces genuine exploration
evaluator: 1        # Independent scoring against rubric
perspectives: "all the outliers, not just the center"
llm_calls: 1        # Still just one call!
```

This is the **SPEED-OF-LIGHT** pattern applied to decision-making.

**New skills:**
- `adversarial-committee` — characters with opposing propensities
- `roberts-rules` — parliamentary procedure prevents short-circuiting
- `rubric` — measurable quality criteria
- `evaluator` — independent assessment without debate context

**Credit:** Mike Gallaher's "Stories All the Way Down" methodology. Full essay in `designs/mike-gallaher-ideas.md`.

### 2. 🔧 Anthropic-Compatible Skills

**All 54 skills** now follow the emerging Anthropic Skills standard:

```
skills/skill-name/
├── README.md           # Human-friendly GitHub landing
├── SKILL.md            # YAML frontmatter + protocol (token-efficient)
└── *.tmpl              # Templates at root level (not in template/ subdir)
```

**MOOLLM extensions beyond Anthropic:**
- Multiple prototype inheritance (Self-style)
- K-line activation (symbolic tradition invocation)
- LLM as template engine (POSTEL for templates)
- Three-tier state persistence

### 3. 📊 Three-Tier State Persistence

| Tier | Where | Lifespan | Example |
|------|-------|----------|---------|
| **Platform chat** | Cursor session | Ephemeral | Tool calls, thinking |
| **Narrative log** | `LOG.md`, `TRANSCRIPT.md` | Read-mostly | Data islands with `#object-id` |
| **State files** | `*.yml` | Read-write | Characters, rooms |

**Key patterns:**
- **Data islands**: Embed YAML in logs without creating files
- **Promotion**: Pop to `.yml` file when editing needed
- **Log inheritance**: `inherits: LOG.md#birth-state`

### 4. 🐱 Adventure-4: The Cat Cave Expansion

**Adventure-3** preserved pristine. **Adventure-4** is the evolved version:

```diff
+ pub/cat-cave/                 # TARDIS-like nested room
+   cat-terpie.yml              # The main cat
+   cat-stroopwafel.yml         # Her friend
+   kitten-myrcene.yml          # 8 terpene-named kittens
+   kitten-limonene.yml
+   kitten-linalool.yml
+   kitten-pinene.yml
+   kitten-caryophyllene.yml
+   kitten-humulene.yml
+   kitten-terpinolene.yml
+   kitten-ocimene.yml
+ pub/budtender-marieke.yml     # Dutch budtender NPC
+ pub/menu-strains.yml          # MOOLLM-themed cannabis strains
+ LOG.md                        # Summary table of changes
+ TRANSCRIPT.md                 # Pure narrative with hot links
+ characters/*/CHARACTER.yml    # Directory-based character identity
- MECHANICS.yml                 # Migrated to skills
```

### 5. 📝 The LLM IS the Template Engine

Templates aren't Mustache. They're **prompts with structure**:

```yaml
# Variables can be:
{{player.name}}                           # Property reference
{{./pub/ROOM.yml:description}}            # File reference  
{{count(inventory) > 5 ? 'heavy' : 'light'}}  # Expression
{{pick your favorite color}}              # Natural language
{{something cozy and warm}}               # YAML Jazz vibes
```

**POSTEL for templates:** The LLM is liberal in what it accepts.

### 6. 🔗 Skills Now Richly Cross-Referenced

Every skill's `related:` field updated. New skills integrated into the network:

- `soul-chat` → now links to `adversarial-committee`, `speed-of-light`
- `speed-of-light` → "Adversarial Committees" documented as killer app
- `coherence-engine` → links to deliberation skills
- `scoring` → links to `rubric`, `evaluator`
- `planning` → links to `roberts-rules`

### 7. 📜 New Design Document

`designs/mike-gallaher-ideas.md` captures:
- The "Stories All the Way Down" essay
- Committee methodology mapping to MOOLLM
- ADVERSARIAL-COMMITTEE / ROBERTS-RULES / RUBRIC / EVALUATOR patterns
- "Ensemble inference over the latent space of possible framings"

## File Changes Summary

### New Skills (SKILL.md)
```
adversarial-committee, buff, cat, character, coherence-engine,
constructionism, data-flow, economy, evaluator, hero-story,
mind-mirror, multi-presence, naming, needs, party, persona,
play-learn-lift, postel, probability, procedural-rhetoric,
protocol, representation-ethics, return-stack, reward,
roberts-rules, robust-first, room, rubric, scoring, scratchpad,
self-repair, session-log, simulation, speed-of-light, summarize,
time, visualizer, world-generation, yaml-jazz
```

### Deleted (migrated)
```
skills/*/PROTOTYPE.yml → skills/*/SKILL.md (YAML frontmatter)
skills/*/template/*.tmpl → skills/*/*.tmpl (root level)
```

### New Templates
```
skills/adventure/ADVENTURE.yml.tmpl
skills/adventure/TRANSCRIPT.md.tmpl
skills/rubric/RUBRIC.yml.tmpl
```

## Breaking Changes

**None for end users.** Skills are backwards-compatible.

**For skill developers:**
- `PROTOTYPE.yml` is gone — use YAML frontmatter in `SKILL.md`
- Templates live at skill root, not in `template/` subdirectory
- `README.md` is for humans; `SKILL.md` is token-efficient spec

## What's Next

- [ ] Sister script CLI for deterministic operations
- [ ] Web frontend for TRANSCRIPT.md rendering
- [ ] Git automation for simulation time travel
- [ ] Python `skillkit` for MCP integration

---

*"Start with jazz, end with standards."*

*"The map is not the territory. The story is not the reality. But the ensemble of stories, cross-examined, might just be useful."*
