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

## The primitives, and the buttons

Most of the verbs people ask for are not primitives. There are four operations
underneath, and everything else is the interface weaving them together:

| Primitive | What it does |
|---|---|
| **Produce** | Run the generator with a given set of inputs; append the result as a new entry |
| **Edit** | Apply a hand-authored change to an entry; append the result as a new entry |
| **Select** | Make any entry in the history the current one |
| **Delete** | Remove entries. The *only* destructive operation, and itself undoable |

The familiar buttons are combinations. *Generate* is produce with new inputs.
*Reroll* is produce with the **same** inputs. *Revise* is produce with the inputs
the user has pinned. *Reset* is select — an earlier entry, not a special state.
*Clear* is select-the-empty-entry, or produce-nothing. None of them destroys
anything, which is what lets the interface be direct-manipulation and reversible
at the same time: the user drags, picks and rerolls freely, and the only button
that removes work says *delete* on it.

Storage is cheap enough that this is not a trade. Keep every roll.

## When the generator is not deterministic

A seeded terrain generator returns the same world for the same seed, so rolling
again means changing the seed. A model does not: **the same prompt and parameters
produce a different result every time.** That makes *produce with identical inputs*
a genuinely useful operation rather than a no-op, and it is what "reroll" actually
means in a generative-model workflow.

So an entry records **all** its inputs — seed if there is one, prompt, parameters,
model and version, and the sampling temperature — because the honest question is
not "what seed was that" but "what would it take to get this again, or something
near it."

Which gives the useful knob: **heat**. Low heat rerolls hover near the last result
(a gentle variation on something almost right); high heat leaves the neighbourhood.
One control that spans "again, but a little different" to "surprise me," instead of
two differently-named buttons.

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
