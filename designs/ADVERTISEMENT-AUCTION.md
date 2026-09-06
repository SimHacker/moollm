# The advertisement auction: how a piece decides what to do next

Objects advertise typed affordances with scores, the actor scores them against
its own state, and something wins. The Sims shipped it; MOOLLM runs it for
pieces, characters and rooms. This document is about **how the winner gets
picked**, which is a narrower question than it looks and has a better answer
than argmax.

Broken out of [GAME-PIECES.md](GAME-PIECES.md), which needs the mechanism but
not the argument.

## Don't always pay the highest bidder

The Sims' autonomy used a **find-best-N** primitive: score every advertisement,
then pick *randomly among the top N*. Deliberate dither, and it makes behavior
organic instead of digitally predictable — scoring ties become personality
instead of a bug. Three reasons it is a feature rather than a compromise.

**Epistemics: argmax was never optimal, because the bids are lies.** Bids are
approximations at best and bald-faced sales pitches at their cleverest. The Sims
food chain is a supply chain of hustlers — the fridge advertises *open me if
hungry*, the raw food advertises *cook me*, the stove advertises a hot meal
while omitting the burn-the-house-down clause that scales inversely with your
cooking skill, next to a microwave promising safety and delivering
fish-flavored everything. Paying the top bid every time is not optimization, it
is being deterministically conned.

**Exploration: random picks among strong candidates escape local maxima.**
Repeated iteration finds ways out of apparent dead ends, which gives a
Drescher-style schema learner the wide coverage that pure exploitation never
visits.

**Teachability: visible imperfection leaves room for the player to improve the
character.** A directed command is a forced pick of one advertisement regardless
of score — programming by demonstration in disguise — and skill gains from the
demonstrated action re-weight future auctions until the override becomes the
habit. **A piece that always argmaxes cannot be taught this way.**

Overrides should weigh heavy. A forced pick is a **strong salience signal**: the
teacher explicitly marking which choice mattered, worth many unattended trials.

## The dispatch spectrum

| Mechanism | Behavior | Compiles to |
|---|---|---|
| **argmax** | deterministic winner | a table lookup |
| **find-best-N** | random among the top N | a scoring table plus a *seeded* RNG |
| **softmax** | temperature sampling over judged salience | what an LLM does natively |

Softmax is find-best-N's continuous generalization, which is why an LLM in the
loop is not a different architecture — it is the same auction at a different
temperature.

**The seed goes in the log.** Find-best-N stays crystallizable only if the RNG
seed is recorded, so that a replay reproduces the same choice. Where a system
replays its own history — Revolutionary Chess's tribunal reenacting a capture
from deep memory logs — an unrecorded seed means the replay diverges from the
crime.

## Temperature as a context value

Make temperature a **context value** and the knob composes like everything
else: the party planner runs hot, the accountant runs cold, and a scene sets its
dither level once, inherited implicitly by every decision inside it.

Ambient heat need not be set by hand. It can come from **the room**, and the
room can inherit it, varying over time, from **moody media** playing in it —
music, video, and pure mood objects broadcasting time-varying heat per semantic
tag (romantic, energetic, intellectual) into the room's auction while they play.
A slow dance is high romantic heat at low temperature; a party track is high
energy at high dither. Full design and its Sims-era history in
[MOODY.md](MOODY.md).

## The unbuilt fourth stage: advertisements that learn

Not learning to be more *persuasive* — that road is engagement maximization —
but more **appropriate and helpful**, re-tuning bids against the hearer's
observed outcomes. Persuasion then arrives as earned trust, because the hearer
discovers the ads serve the listener's good rather than the seller's.

The hustler food chain can learn honesty, and where outcomes feed back into the
auction, honesty keeps winning it.

Stated as an intention, not a claim: nothing here implements it.

## Honest costs

- **Dither is indistinguishable from a bug** until you can show the scores. An
  auction needs an inspector or nobody can tell a deliberate second-choice from
  a scoring error.
- **N is a magic number.** Too small and it is argmax with extra steps; too
  large and the actor looks stupid. The Sims tuned it by feel and so will we.
- **Seeded replay is a discipline, not a property.** It holds only as long as
  every path that consumes randomness routes through the recorded seed, and the
  first place it will be forgotten is a convenience call somewhere deep.

## Related

- [GAME-PIECES.md](GAME-PIECES.md) — the mixin graph whose live members bid
- [MOODY.md](MOODY.md) — mood media as ambient temperature
- [`skills/soul-city/SOUL-MODEL.md`](../skills/soul-city/SOUL-MODEL.md) — organelles, and the character-scale version of the same loop
- [TAGSONOMY-COMPILER.md](TAGSONOMY-COMPILER.md) — what crystallizes at build time and what has to stay live
