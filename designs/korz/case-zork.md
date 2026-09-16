# Case study: Zorkizing Adventure

*Part of the [Korz cauldron](README.md). KORZ is an anagram of ZORK —
and the pun turns out to be load-bearing: the adventure game shipped
symmetric context dispatch in 1979, and rebuilding it as Korz slots is
the most concrete test of the whole [design](korz-prime/README.md).*

## Knuth got here first (half way)

Knuth literate-ized Adventure: his CWEB edition of Crowther & Woods's
ADVENT (*Selected Papers on Fun and Games*) is the canonical literate
program — the cave as a book. Korz Jazz ([design.md](korz-prime/README.md))
suggests the sequel: **zorkize it** — rewrite the cave as a sea of
slots with load-bearing comments, one artifact that both tiers can run
and both kinds of reader can enjoy.

## Zork decomposes into Korz with almost no force

ZIL — Infocom's implementation language — dispatches every turn
through parser globals: **PRSA** (the verb), **PRSO** (direct object),
**PRSI** (indirect object) — plus two more implicit context globals
the parser keeps bound: **WINNER**, the character (say "ROBOT, PUSH
BUTTON" in Zork II and the parser rebinds WINNER to the robot — same
verb, same object, different dispatch), and **HERE**, the location
(the current room, whose action routine speaks first via `M-BEG`).
Then a fixed most-specific-first cascade: roughly the room, the
indirect object's handler, the direct object's, the verb's default.

That is symmetric dispatch over an implicit context with no privileged
receiver — **five hardwired dimensions — verb, direct object, indirect
object, character, location — and a frozen specificity order, shipped
in the Z-machine in 1979**. The Sims froze two dimensions (`me` and
`stackObject` — see [korz-notes](korz-notes.md)); Zork froze five,
sixteen years earlier. Korz generalizes to N: those five, plus light
and the clock (daemons and fuses become slots guarded on a time
dimension), all become ordinary addable dimensions, the cascade
becomes the specificity lattice, and "you can't get there from here"
degrades from error to improvisation in the soft tier.

**Character and location are the load-bearing pair.** They're the two
dimensions MOOLLM already reifies as first-class directories —
`characters/` and rooms, the adventure-game pair — which is why the
[hosting story](korz-prime/hosting-moollm.md) works: the filesystem tree *is*
those two dimensions spatialized (containment is a guard; a character
directory is a standing `rcvr` binding). Zork bound them as globals;
MOOLLM binds them as addresses; Korz names them as ordinary dimensions
and lets you add the rest. Korz may be the ultimate adventure modeling
and scripting language — the thesis MOOLLM's
[GAME-PIECES](https://github.com/SimHacker/moollm/blob/main/designs/GAME-PIECES.md)
design states for game objects generally, stated here as a language
claim.

## The toolchain circle

Crystallization already has a shipped precedent: MOOLLM's
[adventure compiler](https://github.com/SimHacker/moollm/blob/main/skills/adventure/ADVENTURE-COMPILER.md)
compiles adventure YAML — rooms, objects, guards — into deterministic
JavaScript and Python that runs standalone or tethered to an LLM for
creative decisions. The next step is a **Zork compiler** that emits
deterministic, executable **Korz** instead of (or as well as) JS and
Python — the strict tier's slot space as a compilation target, not
just a hand-authored one.

And the arrow points both ways: the adventure compiler can use the
Korz deterministic engine as its runtime instead of emitting a bespoke
engine per game. The adventure model is already slot-shaped — rooms,
objects, verbs, guards — and Zork's five frozen dimensions map
straight onto Korz guards, so compilation becomes *translation into
the soup* rather than code generation. What the engine can't supply —
I/O, persistence, dice, timers, media — arrives as plug-in objects:
host objects registered into the soup under their own dimension,
callable from method slots, the same trick every scripting language
uses at its C boundary. One runtime, many games.

The full circle: Adventure → literate CWEB (Knuth's weave) → jazz YAML
(zorkized) → the Zork compiler → deterministic Korz slots — played
strict when the guards are decidable, improvised soft when the player
walks off the map.

## Instance first: Korzork

Don't design the adventure dimension set from theory —
reverse-engineer it from the two best corpora in existence. Knuth's
`advent.w` is Adventure with the crystallization commentary *already
written*: every data structure explained in prose beside its code,
literate programming as pre-paid jazz. And the original MIT Zork MDL
source (the late-'70s "muddle" code, preserved from the Dynamic
Modeling Group tape at [MITDDC/zork](https://github.com/MITDDC/zork),
with Infocom's ZIL descendants at
[historicalsource](https://github.com/historicalsource)) is where the
five-dimension dispatch actually lives in the wild.

Mine both for interesting, modular, *reusable* parts — the dwarf
daemon, the lamp fuse, the pirate, the thief, the parser's WINNER
rebinding, the troll himself — and translate each into Korz slots one
artifact at a time: **Korzork**. The name is the method — Korz
semantics wearing Zork's flesh — and each translated part is a test
case with forty-five years of players as its oracle.

The transcription discipline is **Jazzork**: lift the historic
comments out of the code and into the YAML jazz data — Knuth's
`@q..@>` location numbers, his "dirty trick!" aside, Woods's
Latin-square construction — preserved as comments beside the facts
they annotate, where all three audiences can reach them.

---

*Sibling case study: [case-cellular-automata.md](case-cellular-automata.md)
— what Korz looks like when every guard is decidable and every
dimension is frozen.*
