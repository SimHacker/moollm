# Anthropic Official Skills — 16 Skills Reviewed

> The trusted baseline. 30 scripts analyzed line-by-line. Zero malware. Each interesting skill has a deep-dive with code review, security analysis, and MOOLLM integration notes.

**Publisher**: [anthropics/skills](https://github.com/anthropics/skills) (~64k stars)
**Scanned**: 2026-02-06 by skill-snitch Deep Probe v2.0

## Verdicts

| Tier | Count | Skills |
|------|-------|--------|
| GREEN | 10 | algorithmic-art, canvas-design, frontend-design, theme-factory, slack-gif-creator, pdf, brand-guidelines, internal-comms, doc-coauthoring, skill-creator |
| YELLOW | 6 | docx, pptx, xlsx (shared soffice.py), mcp-builder, web-artifacts-builder, webapp-testing |

## Deep Dives (with MOOLLM integration notes)

| Skill | Verdict | Analysis | Action |
|-------|---------|----------|--------|
| [algorithmic-art](./algorithmic-art-generative-creative.md) | GREEN | Philosophy-then-expression, seed reproducibility, p5.js | **IMPORT** as new MOOLLM skill |
| [slack-gif-creator](./slack-gif-creator-animation.md) | GREEN | Gold standard Python modules, easing library, GIF optimization | **IMPORT** as MOOLLM `animation` skill |
| [pdf](./pdf-document-processing.md) | GREEN | 8 scripts, CWD issues, needs sister-script upgrade | **IMPORT** as new MOOLLM skill |
| [mcp-builder](./mcp-builder-development.md) | YELLOW | Clean factory pattern, evaluation harness with Claude as test subject | **IMPORT** as new MOOLLM skill |
| [skill-creator](./skill-creator-meta-reference.md) | GREEN | Degrees-of-freedom, three-resource-type convention | **RAVAGE** for `skill` skill — steal ideas, don't import |
| [frontend-design](./frontend-design-anti-slop.md) | GREEN | Anti-slop blacklist, tone menu | **INTEGRATE** examples into `no-ai-slop` + future `web-publisher` |
| [doc-coauthoring](./doc-coauthoring-collaborative.md) | GREEN | Zero-Context Reader Test, speed-of-light committee | **INTEGRATE** pattern into `adversarial-committee` |
| [soffice.py](./soffice-shared-systems-engineering.md) | YELLOW | Runtime C compilation, LD_PRELOAD syscall interception | **REFERENCE** only — too heavy to import |

## Skills Without Deep Dives

| Skill | Trust | One-liner |
|-------|-------|-----------|
| canvas-design | GREEN | Museum-quality static art. Mandatory self-critique. Bundled fonts. |
| brand-guidelines | GREEN | Pure data (colors + fonts). Simplest possible skill. Better as a persona costume. |
| internal-comms | GREEN | Dispatcher pattern: 1.5KB routes to guideline files. |
| theme-factory | GREEN | 10 themes + PDF showcase. Better as a mountable buff. |
| docx | YELLOW | Word docs via XML manipulation. Depends on soffice.py. |
| pptx | YELLOW | PowerPoint with adversarial QA. Depends on soffice.py. |
| xlsx | YELLOW | Excel with financial standards. Writes macro to user config. |
| web-artifacts-builder | YELLOW | React+Vite+Tailwind. MOOLLM would do SvelteKit instead. |
| webapp-testing | YELLOW | Playwright with server lifecycle. shell=True. |

## Design Patterns Harvested

1. **Mandatory adversarial QA** (pptx): "If you found zero issues, you weren't looking hard enough."
2. **Zero-Context Reader Test** (doc-coauthoring): [deep dive](./doc-coauthoring-collaborative.md)
3. **Dispatcher pattern** (internal-comms): Tiny SKILL.md routes to specific files.
4. **Anti-AI-slop constraints** (frontend-design): [deep dive](./frontend-design-anti-slop.md)
5. **Degrees of freedom** (skill-creator): [deep dive](./skill-creator-meta-reference.md)
6. **Philosophy-then-expression** (algorithmic-art): [deep dive](./algorithmic-art-generative-creative.md)
7. **Gold standard Python modules** (slack-gif-creator): [deep dive](./slack-gif-creator-animation.md)
8. **Runtime Environment Adaptation** (soffice.py): [deep dive](./soffice-shared-systems-engineering.md)

## Import Plan

Full plan: [designs/anthropic-import-plan.md](../../../../designs/anthropic-import-plan.md)

**Import as new MOOLLM skills** (non-overlapping):
- algorithmic-art, animation (from slack-gif-creator), pdf, mcp-builder

**Integrate ideas into existing skills** (overlapping):
- skill-creator → `skill` skill (degrees-of-freedom, three-resource-types)
- frontend-design → `no-ai-slop` (visual slop examples) + future `web-publisher`
- doc-coauthoring → `adversarial-committee` (Zero-Context Reader Test)

**Not importing**: brand-guidelines (persona costume), internal-comms (too specific), theme-factory (mountable buff), docx/pptx/xlsx (soffice.py too heavy), web-artifacts-builder (SvelteKit > React), webapp-testing (extend experiment instead)
