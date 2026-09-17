# The Sims 0, and the game that should have been between

*A coinage, a fifteen-year gap, and the games that stood in it.*

**The Sims 0** is [Little Computer People](https://en.wikipedia.org/wiki/Little_Computer_People)
(Activision, 1985). Three characters do what a paragraph of lineage explanation does: it says
*ancestor*, it says *same series in spirit*, and it says *before the numbering started*, all without
a footnote. Will Wright cited LCP directly. The house had room for one man and one dog, every floppy
was serialized at the duplicator so each disk held a *different* man, and his accumulated state lived
in a 256-byte block his own disk drive rewrote as he aged.

Then nothing, for fifteen years, until The Sims in February 2000.

So the question is the interesting one: **what would have been, if there had been a game in between?**

## The Sims 0.5 — the one that was designed and dropped

It existed as a prototype and a pitch. Producer Sam Nelson, on the LCP sequel:

> a Little Computer People apartment complex. In that kind of a scenario, it would be more
> interesting to watch the interaction between the people, study the relationships that form, and so
> on. And you would be able to do things in several houses at once.

It never shipped, because *"Activision wasn't in the practice of sequelling what we had done already.
So we just played around with it in the office for a little while and then dropped it on the floor"*
([Lemon64 interview](https://www.lemon64.com/doc/little-computer-people/353)).

That is the missing game, precisely specified by the person who dropped it. One house becomes several.
One person becomes a population. Watching becomes watching *relationships*. Every single step from
LCP to The Sims is in that paragraph, in 1986, and the only thing missing is a publisher who wanted it.

**It is also exactly what a soul bridge is.** People who each live on their own disk, arranged into a
neighbourhood from outside the game, forty years late. The sequel does not need Activision now; it
needs a disk reader and somewhere to move in.

## Who actually stood in the gap

Four games occupied the empty slot, and each one shipped a different piece of what The Sims would
later put in one box.

**Alter Ego** (Activision, 1986) — same publisher, the very next year. Cradle-to-grave decisions with
separate male and female scripts, a values questionnaire at the start, and life stages as chapters.
It shipped the *biography*: a life as an accumulating sequence of choices rather than a state to
maintain.

**Jones in the Fast Lane** (Sierra, 1991) — the loop. Money, happiness, education, career, as four
player-set goals; a week of actions with weekend events; locations that are both services and
workplaces. Turn-based and boardgame-shaped, but it is the needs-and-errands economy that The Sims
would run in real time.

**Tamagotchi** (Bandai, 1996) — Rich Gold's side of the LCP argument, winning, in hardware. Gold
wanted a fishbowl you watch and tend, David Crane rewrote half the program to let you interact. The
keychain is the fishbowl, sold by the tens of millions, and it demonstrates that the passive design
was never wrong — it was a different product.

**Creatures** (CyberLife / Mindscape, 1996) — the strongest claim to the slot, and the one nobody
counts because it had fur instead of furniture.

## Creatures shipped the soul bridge in 1996

Norns had genomes and neural-net brains, and — this is the part that matters here — **you could
export one to a file and give it to another player.**

| Creatures, 1996 | What it is in this project's vocabulary |
|---|---|
| `File > Export` writes a creature to a `.exp` file and **removes it from your world** | `drain` — a move, not a copy, with conservation enforced by the game itself |
| Import restores it identically, and *"usually the game then tries to delete the file, simulating a move rather than copy"* | The same discipline, in the other direction, at the destination |
| Read-only the file or keep a backup and the move becomes a copy | The hole every conservation scheme has, found by players inside a year |
| Import blocked when population is over eight, greyed out in the menu, **recently deceased still counting** | A destination-side capacity constraint — the reason a bridge asks *can you take her* before it asks *will you* |
| **Import shock**: breeders kept backups *"just in case"* | The named failure mode of transmigration, in the wild, thirty years ago |
| Creatures 1 could not export a *pregnant* norn until the 1.0.2 patch | Dependent state at the border: what travels with whom, decided by patch rather than by design |
| Adoption agencies, CyberLife's own and dozens of fan-run ones | Soul City's marketplace, running on `.exp` files and web forms |
| Docking Station's warp, sending norns between live online worlds | The federation, minus the protocol |

Sources: [Export](https://creatures.wiki/Export) and [Import](https://www.creatures.wiki/Import) on
the Creatures Wiki; CyberLife's own
[adoption page](http://www.creaturesvillage.com/creatures1/com_centre/cc_adoption.htm), 2000.

And the detail that belongs in the [glossary](../../skills/soul-city/GLOSSARY.md) rather than in a
spec: Jenn Frank's *Playing God: On Death, Motherhood and Creatures* was written after she found a
childhood stash of exported norns on old floppy disks. Souls on a shelf, waiting. That is the whole
project in one anecdote, and it happened by accident because a game let people keep their creatures
as files.

**What Creatures did not have** is a second game to send them to. Every `.exp` file went from one
copy of Creatures to another copy of Creatures. The bridge existed; the federation did not. That is
the gap this work is in.

## The numbering

| | | |
|---|---|---|
| **The Sims 0** | Little Computer People, 1985 | One person, one dog, one house, one disk |
| **The Sims 0.5** | Nelson's apartment complex, 1986 | Designed, prototyped, dropped on the floor |
| *the stand-ins* | Alter Ego 1986 · Jones 1991 · Tamagotchi 1996 · Creatures 1996 | Biography · the needs loop · the fishbowl · the export file |
| **The Sims 1** | 2000 | All of it in one box, and no way out of the box |

## Filling the slot late, with the actual soul of retro gaming

[Tiny Life](sims-tiny-life.md) is the honest occupant of the 0.5 slot — not because it is small, but
because of *what kind* of small. One developer. A town rather than a world. Households you can export.
Modding as a first-class feature rather than a tolerated one. Files you own, on your disk, in a format
someone will still be able to read.

That is the actual soul of retro gaming, and it is a set of practices, not an aesthetic. Pixel art is
the least of it. The soul is: one author's decisions all the way through, scope you can hold in your
head, data the player keeps, and no server standing between a person and the thing they made. LCP had
every one of those properties in 1985 because nobody had invented the alternatives yet. Tiny Life has
them in 2026 on purpose, which is harder.

So the plan reads as one sentence: **boot The Sims 0 off a real floppy, and move him into 0.5.** The
apartment complex Activision dropped, built from outside, with the original tenant.

## See also

- [`sims-tiny-life.md`](sims-tiny-life.md) — the destination
- [`sims-will-wright-microworlds-1996.md`](sims-will-wright-microworlds-1996.md) — Wright on moving
  data between games, four years before The Sims shipped
- [`skills/soul-city/SOUL-BRIDGES.md`](../../skills/soul-city/SOUL-BRIDGES.md) — `measure`, `drain`,
  `squirt`, and the gates Creatures was groping toward
- [`skills/soul-city/GLOSSARY.md`](../../skills/soul-city/GLOSSARY.md) — transmigration, refugee, soul
- MicropolisCore
  [`federation-peer-games.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md)
  — LCP as the headwater, Creatures as a bridge target
- MicropolisCore
  [`apple-ii-floppy-bridge.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/apple-ii-floppy-bridge.md)
  — how the 1985 disk gets read
