# algorithmic-art — Deep Probe + MOOLLM Integration Notes

> IMPORT as new MOOLLM-native skill. No generative art skill exists.

**Trust**: GREEN | **Scripts**: 0 (templates only) | **License**: Apache 2.0

## What It Does

Two-phase creative pipeline: write a "philosophy manifesto" for an art movement, then express it as a self-contained p5.js HTML artifact. Seed-based reproducibility (Art Blocks pattern). Template-first approach with Anthropic-branded viewer.

## Security Review

Zero executable code. The p5.js template loads from CDN (`cdnjs.cloudflare.com/ajax/libs/p5.js`). The generated HTML is self-contained. No credentials, no file system access, no network calls beyond the CDN load.

## Key Design Patterns

1. **Philosophy-then-expression**: ideation separate from implementation. The manifesto defines constraints and vocabulary; the code implements them.
2. **Seed-based reproducibility**: same seed = identical output. Art Blocks pattern.
3. **Self-contained artifacts**: generated HTML works offline (except CDN).
4. **Conceptual seed deduction**: a subtle reference embedded in the algorithm as creative DNA.
5. **Mandatory variation**: each generation must differ from previous.

## MOOLLM-Native Version

**New skill**: `skills/algorithmic-art/`

| Feature | Anthropic | MOOLLM-native |
|---------|-----------|---------------|
| Philosophy | Text block | **incarnation**: the art philosophy is a character with worldview and aesthetic values |
| Expression | p5.js HTML | **visualizer** integration: multi-modal (p5.js + image + YAML sidecar) |
| Series | Manual seed management | **coherence-engine**: series maintains visual DNA across pieces |
| Exploration | View in browser | **adventure**: gallery as rooms, each piece is an object (glance/look/examine) |
| Critique | None | **speed-of-light**: art critic + gallerist + collector react in one call |
| Analysis | None | **image-mining**: Three Eyes (structure, narrative, meaning) |
| Metadata | Seed + parameters | **yaml-jazz**: semantic annotations per piece |
| Discovery | Manual invocation | **advertisement**: ALGORITHMIC-ART activates on creative contexts |
| Templates | String templates | **empathic-templates**: `{{describe_artistic_philosophy}}` |
| Dual-use | Undocumented | **skill-snitch**: generative art can be spam/deepfake at negative bias |

**Patron saint candidates**: Sol LeWitt (instructions as art), Vera Molnar (algorithmic pioneer), Casey Reas (Processing/p5.js creator).
