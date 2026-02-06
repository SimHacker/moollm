# frontend-design — Deep Probe + MOOLLM Integration Notes

> NOT importing as separate skill. Integrate anti-slop examples into `no-ai-slop`, design system concepts into future `web-publisher` skill.

**Trust**: GREEN | **Scripts**: 0 | **License**: Apache 2.0

## What It Does

Design guidelines with explicit anti-AI-slop constraints. Tone menu (brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined). Per-generation variation mandate. Design Thinking step before coding.

## Key Anti-Slop Patterns Worth Extracting

### Visual Slop Blacklist (for no-ai-slop)

**NEVER use these**:
- Inter, Roboto, Arial, system fonts (AI defaults)
- Purple gradients on white (the AI aesthetic)
- Centered everything with uniform rounded corners
- Cards-in-a-grid as the default layout
- Stock illustration style with flat pastel colors

**ALWAYS prefer**:
- Distinctive typography (pick ONE unusual font)
- Bold color choices (not safe neutrals)
- Asymmetric layouts when appropriate
- One memorable visual element per page
- Match implementation complexity to aesthetic vision

### Tone Menu (for future web-publisher)

| Tone | Visual Language |
|------|----------------|
| Brutally minimal | Lots of whitespace, stark contrasts, one typeface |
| Maximalist chaos | Overlapping elements, bold colors, mixed media |
| Retro-futuristic | Pixel art meets neon, CRT aesthetics |
| Organic/natural | Flowing shapes, earth tones, hand-drawn elements |
| Luxury/refined | Thin serifs, gold accents, generous margins |

## Where This Goes

### Into `no-ai-slop` (visual slop extension)

Add a `visual-slop.yml` examples file documenting the visual anti-patterns above. This extends no-ai-slop from text hygiene to visual hygiene. The sin: VISUAL-MEDIOCRITY — using AI-default aesthetics when the context calls for something distinctive.

### Into future `web-publisher` skill

The tone menu becomes a **persona costume** system. Each tone is a character that provides CSS conventions:

- **Ben Shneiderman** (patron saint): information density, direct manipulation, visual information seeking
- **Jakob Nielsen** (patron saint): usability heuristics, error prevention, recognition over recall
- **Bret Victor** (patron saint): explorable explanations, reactive documents, seeing the state
- **Don Hopkins** (patron saint): pie menus, spatial interfaces, playful interaction
- **Klaus Nomi** (patron saint): theatrical presentation, bold aesthetic choices, refusing mediocrity

Each patron saint contributes a CSS "stylesheet" (set of design principles that generate CSS). They can be mixed, matched, merged, modulated via the **mount** system and **bias** spectrum.

### NOT a standalone skill

Anthropic's `frontend-design` is 4.4KB of guidelines. That's not a skill — it's a buff. Mount it on whatever creative skill needs visual discipline.
