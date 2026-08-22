# Worse Is Better

**Class:** method · **Attribution:** Richard Gabriel, "Lisp: Good News, Bad News, How to Win Big" (1989)
**Dispatch:** kin skill at moollm `skills/format-design/` — this entry is the design-sense pointer.

> **Can you remove more?**

Two schools. The **MIT approach**: correctness, consistency, and completeness are
non-negotiable; simplicity of interface matters more than simplicity of
implementation; the design must handle every case right. The **New Jersey
approach** (Unix, C): simplicity of *implementation* is the highest value — it's
acceptable for the interface, correctness, and completeness to suffer a little if
the implementation stays simple. Gabriel's uncomfortable finding: New Jersey wins.
The simple-to-implement system ships early, ports everywhere, spreads like a
virus, and then — with the whole world now invested — gets improved to 90% of
right. The elegant system is still being perfected when the war ends. The canonical
exhibit is the PC-loser-ing problem: ITS did the hard, correct thing in the kernel;
Unix said "the syscall might return EINTR, try again" and pushed the complexity
onto every caller — wrong, ugly, and victorious.

He argued with himself about it for a decade (sometimes under the pseudonym
"Nickieben Bourbaki"), which is part of why it's a lens you hold, not a law you
obey.

The working checklist (format-design's distillation): memorable name, real
problem, builds on existing behavior, learnable by example — and always: **can you
remove more?**

**Go deeper:**
["Worse Is Better" (dreamsongs.com)](https://dreamsongs.com/WorseIsBetter.html) —
Gabriel's own hub, with the original essay and the decade of self-rebuttals ·
["The Rise of Worse Is Better"](https://dreamsongs.com/RiseOfWorseIsBetter.html) ·
[Wikipedia: Worse is better](https://en.wikipedia.org/wiki/Worse_is_better)

**Sources:** moollm `skills/format-design/`

**See:** [../masters/richard-gabriel.md](../masters/richard-gabriel.md) ·
[power-of-simplicity](power-of-simplicity.md) — Ungar's simplicity is about the
*language kernel*, Gabriel's about *what survives contact with the world*; they
rhyme but argue · [low-floor-no-ceiling](low-floor-no-ceiling.md) — the tension:
simple that wins vs. simple that caps.
