# P-Pyramid Attention

**Class:** lens · **Attribution:** Marvin Minsky (AI Memo 516; *Society of Mind* lineage)

> **Attention is an anchored weight mask.**

Minsky's P-pyramid models attention as a weight mask anchored over a graph of
agents: activation flows down from an anchor, attenuating with distance, and
*cross-exclusion groups* act like radio buttons — force one member on and its
siblings inhibit. That's not just a mind model, it's a UI architecture already in
production everywhere you look: tab stacks are cross-exclusion groups, z-order is
short-term memory, focus is the anchor, and modal dialogs are a (usually rude)
total mask. The lens: design attention structures with the same care as data
structures, *because that's what they are* — and most attention bugs (lost focus,
buried windows, notification pile-up) are data-structure bugs wearing UX clothes.

The Micropolis application: pie-menu tab windows as a literal P-pyramid — the
active overlay set is an anchored mask over the map, tabs cross-exclude, and the
level of the anchor decides how much simulation detail attaches.

**Go deeper:**
Minsky, AI Memo 516 ("K-lines: A Theory of Memory" working material) ·
[*The Society of Mind*](https://en.wikipedia.org/wiki/Society_of_Mind)

**Sources:**
[MicropolisCore documentation/designs/p-pyramid-attention-overlay.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/p-pyramid-attention-overlay.md) ·
moollm [designs/P-PYRAMID.md](../../../designs/P-PYRAMID.md)

**See:** [level-band](level-band.md) — the vertical rule on the same pyramid ·
[k-line-activation](k-line-activation.md) — the masks, named ·
[foveation](foveation.md) — the hardware this software runs on ·
[../masters/marvin-minsky.md](../masters/marvin-minsky.md)
