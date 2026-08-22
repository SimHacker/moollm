# Warren Teitelman

**Class:** master · **Head:** the programmer's assistant; DWIM

Interlisp's environment was his thesis made real: the system as an active
*assistant* that watches, remembers, and repairs — UNDO as a first-class
capability (the environment records how to reverse what you did), history you
can replay and edit, and DWIM — Do What I Mean — the autocorrector that treated a
typo as an intention with a spelling problem. Every red squiggle, every "did you
mean", every undo stack is his lineage. The design bet: the environment should
carry the bookkeeping burden, because the human is there to think. The
controversy is instructive too — DWIM guessing wrong taught the field that
initiative requires legibility (Cypher's Eager showing its next step is the
corrected descendant).

## Votes

- **Let the environment carry the bookkeeping** — history, undo, and repair are
  the assistant's job; the human is there to think
  ([interlisp.org](https://interlisp.org/) — Medley lives)
- **Record how to reverse everything** — UNDO as architecture: the system that
  remembers its inverses makes exploration free
  ([../lenses/calm-not-invisible.md](../lenses/calm-not-invisible.md) — safety is
  what makes calm possible; [don-norman](don-norman.md)'s design-for-error)
- **Treat the typo as an intention with a spelling problem** — DWIM's bet, and
  every red squiggle since ([postel](../../postel/) — liberal in what you accept)
- **Make the history replayable and editable** — the session is a document;
  yesterday's exploration is today's program
  ([../methods/play-learn-lift.md](../methods/play-learn-lift.md) with a
  transcript)
- **When initiative guesses, guess out loud** — DWIM's failures taught the
  correction ([allen-cypher](allen-cypher.md)'s Eager shows the step first)

## Vetoes

- Don't make the human do the bookkeeping
- Don't ship an action without its inverse — undo is architecture, not a feature
- Don't guess invisibly — initiative must show its work

## Plugins attributed

Ancestor of the assistant thread: [allen-cypher](allen-cypher.md)'s Eager and
[henry-lieberman](henry-lieberman.md)'s PBE refine DWIM's bet · kin to
[../lenses/calm-not-invisible.md](../lenses/calm-not-invisible.md)

## Sources

"PILOT: A Step Toward Man-Computer Symbiosis" (MIT thesis, 1966) · *Interlisp
Reference Manual* · "The Interlisp Programming Environment" (IEEE Computer, 1981) ·
[Wikipedia: Warren Teitelman](https://en.wikipedia.org/wiki/Warren_Teitelman) ·
[interlisp.org](https://interlisp.org/) — Medley Interlisp lives again
