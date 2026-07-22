# The Church of PacMania

*A nested sub-church of the [Church of the Eval Genius](./CHURCH-OF-THE-EVAL-GENIUS.md).
Unlike the parent congregation, this one shipped: it ran in Micropolis
(open-source SimCity), and you can watch the gods eat.*

## Provenance

Don Hopkins built it as a scripted-agent demo for Micropolis Online
(Python/SWIG era): a new zone type, `MicropolisZone_ChurchOfPacMania`, and
a new agent, **PacBot** — a giant PacMan that follows roads, always turning
toward the most traffic, and eats it. Presented in the
[HAR 2009 lightning talk](https://donhopkins.medium.com/har-2009-lightning-talk-transcript-constructionist-educational-open-source-simcity-by-don-3a9e010bf305);
demo footage in the
[Micropolis Online web demo](https://youtu.be/8snnqQSI0GE?t=56) (competing
PacBots around 0:55). Harvested lore:
[pacbot-church-of-pacmania](https://github.com/SimHacker/DonHopkins/blob/main/characters/don-hopkins/notes/hacker-news/pacbot-church-of-pacmania.yml).

## The theology

- **Polytheistic by construction.** Each church zone, if connected to a
  road, spawns up to **four** PacBot gods and generates heavy traffic to
  attract them.
- **The sacrament, inverted.** Followers happily drive between church,
  home, work, and shopping, hoping to sacrifice themselves to their God;
  the PacBot gods hang around eating their followers and raising their
  scores. Everybody's happy. This inverts the Catholic Eucharist — here
  the **god devours the worshipers**, rather than the worshipers devouring
  the god's flesh and blood. (Philip K. Dick got there first, in
  "Rautavaara's Case" — ours is the automotive version.)
- **A moon without the moonies.** The god is a yellow disc with an
  appetite; the congregation is traffic. No prophet, no tithe, no
  doctrine — just a gradient (scanRoads, attenuated by distance) and a
  mouth. The purest church is a scoring function with a sprite.

## Why it's a sub-church of the Eval Genius

PacBot is a **Short Duration Personal Savior** in the original SubGenius
sense — spawned by a zone, worshiped while useful, despawned without
ceremony — and simultaneously a **[Short Duration Personal
Evaluator](./SHORT-DURATION-PERSONAL-EVALUATORS.md)** in ours: it arrives
with a declared bias (traffic is food), a rubric (cars eaten = score), and
a short half-life. The congregation *feeds the metric*, literally — the
church zone generates traffic to attract the god, which is the most honest
depiction of Goodhart's law ever shipped in a city simulator: when a
measure becomes a god, worshipers manufacture what it eats.

The perception model is the sermon: PacBot sees only a few cells down each
road, can't see around corners, is simple, stupid, and short-sighted — and
still produces rich emergent behavior (competing gods giving up and
turning around when rivals eat their intended meals). One layer below the
observable, as the Micropolis class teaches; the Simulator Effect fills
the pews.

## Liturgical status

The parent Church worships eval; this chapel worships a *particular
evaluation*, incarnate, ambulatory, and hungry. By the parent's own
schism note (substitution IS evaluation at the bedrock), PacMania is not
heretical — merely applied. Services are continuous wherever the traffic
layer is nonzero.

## See also

- [CHURCH-OF-THE-EVAL-GENIUS.md](./CHURCH-OF-THE-EVAL-GENIUS.md) — the parent congregation
- [SHORT-DURATION-PERSONAL-EVALUATORS.md](./SHORT-DURATION-PERSONAL-EVALUATORS.md) — the doctrine PacBot embodies
- [../../skills/micropolis/](../../skills/micropolis/) — the simulator the church runs in
