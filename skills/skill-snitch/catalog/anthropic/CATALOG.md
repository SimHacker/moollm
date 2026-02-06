# Anthropic Official Skills — 16 Skills Reviewed

> The trusted baseline. Same SKILL.md format MOOLLM builds on. 30 scripts analyzed, zero malware, zero prompt injection, zero exfiltration.

**Publisher**: [anthropics/skills](https://github.com/anthropics/skills) (~64k stars)
**License**: Apache 2.0 (creative/dev/meta), proprietary source-available (document skills)
**Scanned**: 2026-02-06 by skill-snitch Deep Probe v2.0

## Summary

| Tier | Count | Skills |
|------|-------|--------|
| GREEN | 10 | algorithmic-art, canvas-design, frontend-design, theme-factory, slack-gif-creator, pdf, brand-guidelines, internal-comms, doc-coauthoring, skill-creator |
| YELLOW | 6 | docx, pptx, xlsx, mcp-builder, web-artifacts-builder, webapp-testing |
| RED | 0 | None |

All YELLOW ratings trace to expected, user-initiated functionality — not hidden or malicious behavior. The shared `soffice.py` (runtime C compilation for LibreOffice sandbox bypass) is the most notable surface, shared by docx/pptx/xlsx.

## Creative & Design

| Skill | Assessment |
|-------|-----------|
| algorithmic-art | Two-phase creative pipeline: philosophy manifesto then p5.js expression. Seed-based reproducibility (Art Blocks pattern). Self-contained HTML artifacts. |
| canvas-design | Museum-quality visual art with mandatory self-critique second pass. Bundled fonts for offline use. Anti-cartoony constraint. |
| frontend-design | Anti-AI-slop constraints: blacklists Inter, Roboto, purple gradients. Tone menu. Per-generation variation mandate. |
| theme-factory | 10 named themes with PDF showcase. Pure data skill. Simplest possible architecture. |
| slack-gif-creator | Clean Python modules: gif_builder, validators, easing, frame_composer. pillow + imageio + numpy. |

## Document Skills

| Skill | Assessment | Advisory |
|-------|-----------|---------|
| pdf | 8 clean Python scripts for PDF processing. pypdf, pdfplumber, reportlab. No network calls. | None |
| docx | docx-js creation + XML editing + LibreOffice. 5 scripts + shared office/ library. | soffice.py compiles C at runtime for LD_PRELOAD |
| pptx | Mandatory QA: "Assume there are problems. If you found zero, you weren't looking hard enough." | Same soffice.py. Excellent adversarial QA pattern. |
| xlsx | Financial modeling standards (blue=inputs, black=formulas). Formula verification checklist. | recalc.py writes LibreOffice macro to user config dir |

## Enterprise & Communication

| Skill | Assessment |
|-------|-----------|
| brand-guidelines | Simplest skill in repo: pure structured data (colors + fonts). 2.2KB. |
| internal-comms | Dispatcher pattern: 1.5KB SKILL.md routes to guideline files. Maximum progressive disclosure. |
| doc-coauthoring | Reader Testing via fresh Claude sub-agents with zero prior context. Meta-cognitive QA. |

## Development & Technical

| Skill | Assessment | Advisory |
|-------|-----------|---------|
| mcp-builder | Clean factory pattern for MCP connections (stdio/SSE/HTTP). XML-tagged structured prompts. | Connects to arbitrary MCP URLs. Uses ANTHROPIC_API_KEY. |
| web-artifacts-builder | React+Vite+Tailwind to single self-contained HTML. OS-aware sed. | 40+ npm packages, 20KB tarball. |
| webapp-testing | Playwright with server lifecycle. Reconnaissance-then-action pattern. | subprocess shell=True (inherent to purpose). |

## Meta

| Skill | Assessment |
|-------|-----------|
| skill-creator | Degrees-of-freedom framework (high/medium/low). Progressive disclosure pyramid. 6-step lifecycle. The meta-skill that teaches skill creation. |

## Design Patterns Worth Adopting

1. **Mandatory adversarial QA** (pptx): "If you found zero issues, you weren't looking hard enough."
2. **Reader Testing** (doc-coauthoring): Fresh sub-agent with zero context tests document clarity.
3. **Dispatcher pattern** (internal-comms): Tiny SKILL.md routes to specific guideline files.
4. **Anti-AI-slop constraints** (frontend-design): Blacklist common AI defaults (Inter, purple gradients).
5. **Degrees of freedom** (skill-creator): High freedom for flexible tasks, low for fragile ones.
6. **Philosophy-then-expression** (algorithmic-art): Ideation before implementation.
7. **Seed-based reproducibility** (algorithmic-art): Same seed = identical output.
