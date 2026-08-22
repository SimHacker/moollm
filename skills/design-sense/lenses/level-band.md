# Level Band

**Class:** lens · **Attribution:** Marvin Minsky ("K-Lines: A Theory of Memory", 1980)

> **Reattach at the middle of the pyramid.**

Minsky's level-band principle: when a K-line reactivates a prior mental state, it
should attach agents in a *middle band* of the abstraction pyramid — strongly in
the middle, weakly at the fringes. Attach too low and stale concrete details
fight the new situation (you remember the old phone number, not how to remember
phone numbers); attach too high and you hallucinate the problem as already
solved (you remember *that* it worked, not what made it work).

The design applications are constant:

- **Resuming work** — a session summary should restore mid-level structure
  (goals, open questions, key decisions), not raw transcripts (too low) or "it
  went well" (too high).
- **Onboarding docs** — teach the middle band: the concepts that generate the
  details, not the details or the mission statement.
- **Context restoration for LLMs** — the whole art of the context window is
  choosing the band; moollm's hot/working-set files are level-band engineering.
- **Tutorials** — teach at the band the player can act on now
  ([goldilocks-complexity](goldilocks-complexity.md) is this lens applied to
  whole systems).

**Go deeper:**
Minsky, "K-Lines: A Theory of Memory" (*Cognitive Science* 4, 1980), §the
level-band principle · *The Society of Mind*, ch. 8

**Sources:** moollm [designs/P-PYRAMID.md](../../../designs/P-PYRAMID.md) ·
moollm [skills/k-lines/](../../k-lines/)

**See:** [k-line-activation](k-line-activation.md) · [semantic-mipmap](semantic-mipmap.md) —
the mipmap stores all bands; level-band picks one ·
[../masters/marvin-minsky.md](../masters/marvin-minsky.md) ·
[../masters/stewart-brand.md](../masters/stewart-brand.md) — pace layers are
level bands with clocks
