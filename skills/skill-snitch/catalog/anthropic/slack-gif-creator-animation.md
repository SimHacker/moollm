# slack-gif-creator — Deep Probe + MOOLLM Integration Notes

> IMPORT as new MOOLLM-native `animation` skill. No animation skill exists.

**Trust**: GREEN | **Scripts**: 4 Python modules (gif_builder, validators, easing, frame_composer) | **License**: Apache 2.0

## What It Does

Creates animated GIFs optimized for Slack. GIF builder with frame management, color optimization (global palette), deduplication. Validators for Slack constraints (128x128 emoji, 480x480 message). 16 easing functions with interpolation. Frame composer with shapes, text, gradients.

## Code Review — The Gold Standard

These four modules are the best-written code in the entire Anthropic repo:

| Module | Lines | Docstrings | Type Hints | CWD-dep | I/O Side Effects |
|--------|-------|-----------|-----------|---------|------------------|
| gif_builder.py | 220 | Every method | Extensive | No | GIF file output |
| validators.py | 110 | Every function | Extensive | No | stdout (verbose mode) |
| easing.py | 210 | Every function | All params + returns | No | None (pure math) |
| frame_composer.py | 175 | Every function | All params + returns | No | None (returns PIL Images) |

**Why it's the gold standard**: Pure libraries. No `__main__`. No CWD dependencies. No global state. Type hints on everything. Docstrings with Args/Returns. Zero subprocess, eval, exec. The easing module is pure math — zero imports beyond `math`.

**sniffable-python score**: 10/10. API visible in first 5 lines of every file.

## MOOLLM-Native Version

**New skill**: `skills/animation/` (broader than Slack GIFs)

| Feature | Anthropic | MOOLLM-native |
|---------|-----------|---------------|
| Scope | Slack GIFs | General animation (GIF, sprite sheets, CSS transitions) |
| Easing | Library of functions | **mountable buffs**: MOUNT `bounce-ease` ON character movement |
| Style | Hardcoded per GIF | **persona costume**: animation style swappable like a persona |
| Series | Manual consistency | **coherence-engine**: visual consistency across animation set |
| Quality | validators.py (dimensions, size) | **rubric**: measurable criteria for animation quality |
| Integration | Standalone | **adventure**: animated room transitions, character action GIFs |
| Integration | Standalone | **visualizer**: animation as a rendering mode |
| Discovery | Manual invocation | **advertisement**: ANIMATE activates when motion/transition needed |

**What to keep as-is**: The four Python modules. They're perfect. Don't rewrite them. Wrap them in MOOLLM CARD.yml + advertisements + k-lines.

**What to add**: GLANCE.yml, CARD.yml with advertisements, SKILL.md with MOOLLM methods (ANIMATE, EASE, VALIDATE, COMPOSE-FRAMES), skill-snitch-report.md.
