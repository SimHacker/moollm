# Lean Into Latent

**Class:** lens · **Attribution:** moollm no-ai-humansplaining
**Dispatch:** whole skill at moollm [skills/no-ai-humansplaining/](../../no-ai-humansplaining/) — load it; this entry is the design-sense pointer.

> **If it's in latent space, point. If not, spell it once, findably.**

The test before writing anything for an LLM (and increasingly, for people): is
the pointee already in the training data? If yes, the name is the activation —
"Fitts' law" costs two tokens and buys fifty years of research; pasting the
Wikipedia article costs two thousand and buys the same thing minus trust. If no,
spell it out exactly once, in a findable file, and point thereafter. The
economics are brutal and simple: latent knowledge is prepaid; respelled
knowledge is billed per call, forever; and novel jargon that isn't written down
anywhere is a cache miss that never fills.

This is the inbound twin of anti-slop: slop pollutes what the model says,
humansplaining pollutes what it's told. Both waste the same budget. The
constitutional directive — *lean into the training data* — is also a design
principle for docs, APIs, and naming: choose names that activate existing
knowledge ([k-line-activation](k-line-activation.md)) over names that require a
glossary nobody will load.

**Go deeper:**
moollm [skills/no-ai-humansplaining/](../../no-ai-humansplaining/) (the sin
catalog: MANUAL-PASTING, RESPELLING, GUID-NAMING…) ·
moollm [designs/object-system/LATENT-SPACE-INHERITANCE.md](../../../designs/object-system/LATENT-SPACE-INHERITANCE.md)

**Sources:** moollm `skills/no-ai-humansplaining/`

**See:** [k-line-activation](k-line-activation.md) — the mechanism this lens
exploits · [../methods/latent-space-inheritance.md](../methods/latent-space-inheritance.md) —
inheritance implemented by pointing ·
[../methods/point-dont-copy.md](../methods/point-dont-copy.md) — the same rule
for files instead of models
