# Sniff Depths

**Class:** lens · **Attribution:** moollm sniffable-python
**Dispatch:** whole skill at moollm [skills/sniffable-python/](../../sniffable-python/) — load it; this entry is the design-sense pointer.

> **Depth is a legibility property.**

Structure artifacts so a reader — human, LLM, or tool — can sniff them at three
depths without opening everything: **glance** (the docstring, the section
headers, the `__all__`), **structure** (signatures, class layout, the shape of
the thing), and **full** (the implementation). Sniffable Python is the code
version: module docstrings that summarize honestly, functions ordered by
importance, names that advertise — so `grep` and a 30-line read answer "is this
the file I need?" before a 500-line read answers "how does it work?"

Legibility isn't clarity at one zoom level — it's *having the zoom levels at
all*. A perfectly clear function in an unsniffable module is a well-labeled
jar in an unlabeled warehouse. The lens applies to any artifact with insides:
code, YAML, papers (abstract → sections → prose), directory trees, even
meetings (agenda → headlines → discussion).

**Go deeper:**
moollm [skills/sniffable-python/](../../sniffable-python/) (CARD.yml for the
structure rules)

**Sources:** moollm `skills/sniffable-python/`

**See:** [semantic-mipmap](semantic-mipmap.md) — the same pyramid, for published
artifacts · [directories-as-advertisements](directories-as-advertisements.md) —
sniffability at the tree level ·
[../methods/sister-script.md](../methods/sister-script.md) ·
[../masters/dan-ingalls.md](../masters/dan-ingalls.md) — fits-in-one-head
requires sniffable depths
