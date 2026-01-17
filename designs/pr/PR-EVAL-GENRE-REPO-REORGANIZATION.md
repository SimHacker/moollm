# 📁🎮🔗 EVAL GENRE DOCS + REPOSITORY REORGANIZATION

## Summary

This Pull Request delivers **major repository reorganization** establishing the EVAL game genre as a first-class design category, alongside systematic restructuring of design documents into logical subdirectories.

> *"EVAL games don't simulate worlds — they simulate the act of judging them."*

**What we did:**
1. Created `designs/eval/` for EVAL game genre documentation
2. Reorganized `designs/` into logical subdirectories (`pr/`, `sims/`)
3. Updated all internal links across 70+ files
4. Enhanced `.cursorrules` with explicit tool guidance
5. Documented EvalCity's intellectual heritage (AgentSheets, Repenning)

---

## 🎮 EVAL Genre Directory

### New: `designs/eval/`

The EVAL game genre now has its own home:

| Document | Purpose |
|----------|---------|
| `EVALCITY-DESIGN.md` | Core EvalCity design philosophy |
| `EVAL-VS-SIM.md` | Genre comparison (EVAL vs simulation) |
| `EVAL-BRAND-FAMILY.md` | Title catalog |
| `EVAL-FACTIONS.md` | Competing evaluation philosophies |
| `EVAL-ARTIFACTS.md` | In-game objects and tools |
| `EMOJI-ANCHORS.md` | Visual language specification |
| `THE-EVALS-DESIGN.md` | Social-scale EVAL game |
| `README.md` | Directory index |

### The EVAL Thesis

EVAL games are a new genre where:
- **Metrics are choices** — not fixed, but player-defined
- **The player IS the evaluator** — not consuming, but judging
- **Transparency replaces black boxes** — see and change the assumptions

---

## 📁 Repository Reorganization

### New Directory Structure

```
designs/
├── eval/         # EVAL game genre docs (NEW)
├── pr/           # 26 PR documentation files (NEW)
├── sims/         # 22 Sims/SimCity/Micropolis docs (NEW)
└── *.md          # Core design documents
```

### Files Moved

| From | To | Count |
|------|----|-------|
| `designs/PR-*.md` | `designs/pr/PR-*.md` | 26 files |
| `designs/sims-*.md` | `designs/sims/sims-*.md` | 21 files |
| `designs/simcity-*.md` | `designs/sims/simcity-*.md` | 1 file |

### Links Updated

All internal references updated across:
- `designs/README.md` — Master index
- `designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md` — Core philosophy
- `designs/don-hopkins-projects.md` — Project lineage
- `designs/stanza-notes.md` — Development notes
- `designs/skill-snitch-design.md` — Tool docs
- `designs/eval/*.md` — EVAL genre documents
- `designs/pr/*.md` — Cross-references between PRs
- `examples/adventure-4/**/*.md` — Session documents
- `skills/**/*.md` — Skill documentation
- Root `README.md`

**Total files modified for link updates:** 25+

---

## 🔧 .cursorrules Enhancement

Added explicit tool guidance for agent behavior:

### Tools Section

```yaml
tools:
  - cursor-mirror    # Deep introspection into IDE state
  - skill-snitch     # Runtime skill debugging
  - deep-snitch      # Multi-file skill analysis
```

### Key Skills Index

```yaml
key_skills:
  foundational:
    - bootstrap       # K-line activation
    - skill-snitch    # Skill debugging
  simulation:
    - simulator-effect
    - speed-of-light
  social:
    - party
    - society-of-mind
```

**Purpose:** Prevents agents from missing available tools by making them explicit in the boot sequence.

---

## 🎓 Historical Credits Added

### AgentSheets Heritage

Added Alexander Repenning and AgentSheets (1991) as direct precedent for EvalCity:

| Person | Work | Contribution |
|--------|------|--------------|
| **Alexander Repenning** | AgentSheets, AgentCubes | Programming by Example, graphical rewrite rules |

### New Section in EVALCITY-DESIGN.md

Comprehensive documentation of the "SimCity in 10 minutes" benchmark:
- Graphical rewrite rules — define behavior by showing before/after states
- Programming by Demonstration — actions become programs
- The 35-year arc from AgentSheets (1991) to EvalCity (2026)

**The connection:** AgentSheets proved end-users can program simulations by demonstration. EvalCity upgrades this with LLM coherence.

---

## 📊 By The Numbers

| Metric | Count |
|--------|-------|
| **Directories created** | 3 (`eval/`, `pr/`, `sims/`) |
| **Files moved** | 48 |
| **Files with link updates** | 25+ |
| **EVAL documents organized** | 8 |
| **Historical credits added** | 1 (Repenning/AgentSheets) |

---

## 🎯 Why This Matters

1. **EVAL as First-Class Genre** — No longer scattered; has its own directory
2. **Repository Navigation** — Clear separation of PR docs, Sims heritage, and EVAL genre
3. **Agent Guidance** — Explicit tools in `.cursorrules` prevent missed capabilities
4. **Intellectual Lineage** — EvalCity's heritage now documented

---

## Files Changed

### New Directories
- `designs/eval/` — 8 EVAL genre documents
- `designs/pr/` — 26 PR files
- `designs/sims/` — 22 Sims/SimCity files

### Modified Files
- `.cursorrules` — Tools and key_skills sections
- `designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md` — Credits update
- `designs/eval/EVALCITY-DESIGN.md` — AgentSheets heritage section
- `designs/README.md` — Updated paths
- `designs/don-hopkins-projects.md` — Updated paths
- `designs/stanza-notes.md` — Updated paths
- `designs/skill-snitch-design.md` — Updated paths
- `designs/pr/*.md` — Cross-reference updates
- `examples/adventure-4/**/*.md` — Path updates
- `skills/**/*.md` — Path updates
- Root `README.md` — Path updates

---

*"EVAL games don't ask 'what happens?' — they ask 'how should we judge what happens?'"*
*"The player isn't playing. The player is evaluating."*
