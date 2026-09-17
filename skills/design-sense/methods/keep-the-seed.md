# Keep the Seed

**Class:** method · **Attribution:** Don Hopkins (multiplayer SimCity city-proposal design); the generative-art and undo-history lineage generally

> **Generation appends to a history. It never replaces what was there.**

A generator that overwrites its own output makes every roll a gamble, and it makes
collaboration destructive: the moment a second person hits *generate*, the first
person's world is gone and nobody can get it back.

The fix is small. Keep the **seed**, not the artifact. A random world is a
function of its seed, so the seed is a few bytes that recover megabytes exactly.
Store the seed with every proposal and the history becomes navigable instead of
merely regrettable — page back and the generated thing returns, bit for bit,
without anyone having saved a file.

The multiplayer SimCity design says it in one line: *players can page through the
proposed-city history, and you can go back to randomly generated terrains because
it saves the random number generator seed.* Load San Francisco, someone rolls a
random island, someone loads Detroit — the island is still two clicks back. That
turned a shared generator from a weapon into a conversation. (Whether the original
Mac release had this is unconfirmed; the design is in the multiplayer notes in the
Micropolis source.)

## The verb set

Anything generative owes the user all six, visibly:

| Verb | What it must guarantee |
|---|---|
| **Generate** | Produce a candidate *and* record its seed as a new entry |
| **Reroll** | Another candidate, without discarding the last one |
| **Edit** | Hand-authored change on top of a generated base, tracked as its own entry |
| **Revise** | Regenerate *within* constraints the user has pinned |
| **Reset** | Back to the last committed state, not to nothing |
| **Clear** | Deliberately to nothing, and itself undoable |

Two rules keep the set honest. **Reset and clear are different verbs** — collapsing
them is how people lose work while pressing the button that promised safety. And
**an edit on generated content must not be silently overwritten by the next roll**:
if a reroll would clobber hand-work, that is a question to ask, not a thing to do.

## Why it matters more with generators in the loop

A model generating text, a terrain generator, and a second player at the same table
are the same problem: another author with write access to something you care about.
History is what makes that safe, and it is what makes *asking* cheap: an agent can
propose freely when nothing it does is irreversible, so reversibility is what buys
automation its freedom, and a generator without it has to be supervised instead.

Proposals also want **consent that clears itself**. In the SimCity design every
player must agree before a proposed city is played, and proposing a new one clears
all votes. Agreement is attached to a specific candidate, not to the generator, and
a new candidate starts the agreement over.

**Go deeper:**
[Micropolis multiplayer notes (`documentation/notes/MultiPlayerIdeas.txt`)](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/notes/MultiPlayerIdeas.txt) ·
[Wikipedia: Undo](https://en.wikipedia.org/wiki/Undo) ·
[Wikipedia: Random seed](https://en.wikipedia.org/wiki/Random_seed)

**Sources:** [MicropolisCore `documentation/designs/generative-history-and-proposals.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/generative-history-and-proposals.md) (the implementation spec) · [moollm `designs/INTERFACE-TO-AGENCY.md`](../../../designs/INTERFACE-TO-AGENCY.md) (who is allowed to drive)

**See:** [instance-first](instance-first.md) · [tuned-emergence](tuned-emergence.md) ·
[find-best-n-dither](find-best-n-dither.md) — pick among candidates instead of trusting one ·
[play-learn-lift](play-learn-lift.md) — exploration presumes cheap mistakes
