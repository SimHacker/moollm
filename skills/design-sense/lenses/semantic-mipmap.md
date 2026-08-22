# Semantic Mipmap

**Class:** lens · **Attribution:** moollm (after Lance Williams' mipmaps, SIGGRAPH 1983); kin to Ungar's stage magic

> **Publish every artifact at every resolution.**

In graphics, a mipmap stores the same texture at every power-of-two resolution so
the renderer never pays for detail the viewing distance can't show. The semantic
version: ship every artifact at multiple meaning-resolutions — glance (is this
relevant?), interface (what can it do?), protocol (how does it work?), deep why
(why was it built?) — and never load a finer level until the coarser one has
earned it. moollm's GLANCE → CARD → SKILL → README pyramid is the running
implementation; this registry's one-line statements above the fold are the same
lens applied to itself.

What it buys:

- **Attention economics** — readers (and LLMs) pay per token; the mipmap lets
  them pay exactly the resolution the decision needs.
- **Honest progressive disclosure** — nothing is hidden, everything is staged;
  progressive disclosure by *budget*, not by locking features away.
- **Trilinear reading** — like the renderer blending mip levels, a reader holds
  the GLANCE summary while sampling one SKILL section; design levels to compose.

**Go deeper:**
[Wikipedia: Mipmap](https://en.wikipedia.org/wiki/Mipmap) — Williams'
"Pyramidal Parametrics" is the founding paper ·
moollm [designs/MOOPMAP.md](../../../designs/MOOPMAP.md) ·
moollm [designs/GLOSSARY.md](../../../designs/GLOSSARY.md) (Semantic Mipmap entry)

**See:** [stage-magic](stage-magic.md) — the same reveal, dramatized ·
[sniff-depths](sniff-depths.md) — the mipmap as code structure ·
[level-band](level-band.md) — Minsky's rule for *which* resolution to reattach ·
[../masters/edward-tufte.md](../masters/edward-tufte.md) — resolution as respect
