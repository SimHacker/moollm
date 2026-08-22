# Goldilocks Complexity

**Class:** lens · **Attribution:** Will Wright (the postmortem ladder)

> **SimEarth too hard, SimAnt too simple, SimCity 2000 just right.**

Wright's own postmortem ladder: SimEarth failed *opaquely* — the planet died and
you couldn't tell why, so the possibility space felt like a slot machine; SimAnt
was too simple — every colony converged, so mastery ran out; SimCity 2000 sat in
the band where failure is visible, varied, and attributable. The test isn't
"how complex is the system?" but **how legible is failure at this complexity?**
Complexity you can't attribute is noise; complexity you can attribute is depth.
The band moves with the interface: better feedback widens what players can
handle (the [mental-model-compiler](mental-model-compiler.md) toolchain again —
UI, sim, and mental model must stay tractable *together*).

Working test: when the player fails, can they (1) notice, (2) name a cause,
(3) form a next experiment? Three yeses: inside the band. The lens applies
verbatim to APIs, config systems, and LLM prompts — a system whose failures
can't be attributed is too complex *for its current instrumentation*, whatever
its actual size.

**Go deeper:**
[Wikipedia: SimEarth](https://en.wikipedia.org/wiki/SimEarth) ·
[Wikipedia: SimAnt](https://en.wikipedia.org/wiki/SimAnt) ·
Wright's GDC talks passim — the ladder recurs for a decade

**Sources:**
[wwsff don-hopkins/teaching-complicated-systems-without-a-manual.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/teaching-complicated-systems-without-a-manual.md) ·
[wwsff characters/will-wright/](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/will-wright)

**See:** [mental-model-compiler](mental-model-compiler.md) ·
[../methods/failure-as-entertainment.md](../methods/failure-as-entertainment.md) —
why legible failure is also the content ·
[level-band](level-band.md) — the same band-picking, for knowledge ·
[../masters/will-wright.md](../masters/will-wright.md),
[../masters/scott-kim.md](../masters/scott-kim.md)
