# Revolutionary Chess — Rules

Normative spec. Where this disagrees with the earlier prototype documents, this
wins. Design rationale is in [README.md](README.md); the argument for what the
variant is *for* is in [BRINGING-IT-HOME.md](BRINGING-IT-HOME.md).

Terms:

- **Commoner** — a pawn, or an aristocrat that has joined the commons.
- **Aristocrat** — king, queen, rook, bishop, knight, not yet joined. Defined
  negatively: a piece that inherits no commons.
- **Commons** — the append-only ledger of move-sets available to commoners. One
  per side, plus a world commons above both.
- **Move-set** — a named bundle of legal moves, held by delegation, written in
  side-relative coordinates.
- **Deposit** — to add a move-set to a commons. The only write operation the
  game has.

## Base game

### Setup

Standard chess. Standard position, standard pieces, standard clock. Each side's
commons is seeded with the pawn move-set and nothing else.

Any legal chess position may be used as a starting position, including the final
position of a recorded historical game. This is a supported opening, not a
curiosity. Kasparov versus Deep Blue, game 6, 1997 — Kasparov as Black,
resigning after nineteen moves — is the canonical one: the machine's victory
becomes the initial condition for whatever the survivors decide to do next.

### Standard mode

Ordinary chess, played for real. Check exists. Checkmate exists. Nothing about
the revolution is visible or reachable.

### Trigger

The game-end event of standard mode is intercepted rather than honored. The
result is recorded — someone won that game of chess — and becomes the initial
condition of the revolution.

The fallen side revolts. The winning side is not yet involved.

### Revolution mode

Deposit the homeward move-set into the revolting side's commons. This is
additive: pawns keep every forward move and gain the homeward ones. Single step
homeward, double step from the far rank, diagonal capture homeward, promotion on
reaching their own home rank.

Capture rules change:

- Commoners may capture aristocrats of their own colour.
- Aristocrats may capture commoners of their own colour, in self-defence.
- Nobody may capture anything of the other colour. The other colour is
  **terrain**: it moves, it occupies squares, it blocks lines and lanes, and it
  cannot attack or be attacked.
- Check does not exist. The king is a piece that can be taken.
- En passant is inoperative, since it is defined between opposing pawns and
  pawns now only fight their own aristocrats.

This is a civil war, not an invasion. The revolution is not against the enemy;
it is against your own elites.

Terrain is not neutral in effect, only in intent. A piece of the other colour
standing in the wrong place will shield an aristocrat from the pawns that want
it, or seal the escape square it needed, and it will do so without meaning
anything by it.

### Inheritance

When an aristocrat leaves the board or joins the commons, by any route:

1. Its move-set is deposited into its side's commons.
2. Every commoner of that side gains those moves, by lookup, immediately.
3. No aristocrat gains anything.

There is no waiting for a piece type to go extinct, and no waiting for the
second rook. Equality does not queue.

A captured aristocrat is enfranchised rather than executed: it joins the
commons as a full equal. (House rules can make capture lethal or put it on
trial; see the variant axes.)

### The aristocrats' three options

Available when threatened, or voluntarily on your own turn. Pawns do not get
these options. Pawns don't negotiate — they take.

**Surrender.** The piece survives, its move-set is deposited, and it joins the
commons as an equal, holding everything deposited so far and everything
deposited afterward.

**Bribe.** The piece survives with its move-set private and inherits nothing,
ever. It becomes isolated. The price is paid in position, service, or
protection commitments, and the commons votes on whether to accept it.

**Resist.** Normal capture rules. If taken, the move-set is deposited anyway. If
it survives, it stays an aristocrat.

### Status by deed

An aristocrat that captures a commoner while the old order still stands is
marked. The mark is a fact in the log, not a label anyone assigns by fiat, and
other pieces may act on it: a marked aristocrat has no protection from either
side.

Pieces keep append-only memories; squares keep their own ledgers of arrivals,
departures, and deaths. Loyalty, karma, and eligibility are computed by reading
those logs at the moment a decision needs them, never from a cached score.

### Modes after the revolution

**Inheritance mode** begins when the revolting side has no aristocrats left
outside the commons. Both sides are now in play: the winning side's commoners
gain homeward moves and begin their own revolution against their own
aristocrats. Two ledgers, two timelines. The board can hold one flat society
and one still-royalist kingdom at the same time, and the flat side will
proselytize across the ranks.

**Equality mode** begins when no aristocrats remain on either side. Every piece
has every move. Capture is still legal and gains nothing: you take your mirror
image and receive what you already had.

**The International** merges the two side commons into the world commons.
Nothing is repointed — the delegation edge was there from the first move. The
move-sets are moved upstairs and the duplicates collapse, because side-relative
coordinates meant the two sides' pawn files always held the same contents.

**Cooperation mode** begins when the players stop trying to capture. Adjacent
pieces may combine actions; three or more may build.

**Sandbox mode** has no victory condition and no end. The board expands past
8x8 because the edges were always arbitrary. Crafting, logistics, and building
replace capture.

### End conditions

| Mode | Ends when | Becomes |
|------|-----------|---------|
| Standard | checkmate, resignation, or draw | Revolution |
| Revolution | revolting side's aristocrats all gone or joined | Inheritance |
| Inheritance | no aristocrats remain anywhere | Equality |
| Equality | capture stops paying | Cooperation |
| Cooperation | by agreement | Sandbox |
| Sandbox | never | — |

There is also a democratic ending available from phase 7 onward: the surviving
pieces vote, one piece one vote, pawns included and especially, and the winner
is crowned. The game becomes politics. This is a legal way to stop.

## Phases inside the revolution

One rule changes at a time, in the manner of Fluxx. The phases advance on their
own triggers; a table of exact triggers is engine business and deliberately not
fixed here.

| # | Phase | Rule change |
|---|-------|-------------|
| 1 | The Reversal | homeward moves deposited; pawns walk both roads |
| 2 | The Grudge Bearers | homeward capture |
| 3 | The Flanking | sideways movement |
| 4 | The Coronation | promotion at your own home rank |
| 5 | The Apotheosis | double promotion |
| 6 | No More Privilege | the surviving king is capturable |
| 7 | The New Order | any piece may be crowned by vote |

## Variant axes

House rules are opt-in mixins on two axes. The dealer announces them before the
first move. None are on by default; the base rules above apply unless a mixin
replaces them.

### Surrender policy

| Rule | Effect |
|------|--------|
| NO-QUARTER | nobody may surrender |
| VICTORS-EXIT | only the winning side's aristocrats may surrender |
| VANQUISHED-MERCY | only the defeated side's aristocrats may surrender |
| GOLDEN-BRIDGE | the window closes for a type once one of that type has been executed |
| AMNESTY-VOTE | each surrender is admitted by majority vote of the current commons |
| EXILE | surrender means leaving the board, and the move-set leaves with you |

EXILE is the only one that breaks monotonicity from the commons' point of view,
and it does so without a removal: it declines to deposit.

### Capture policy

| Rule | Effect |
|------|--------|
| TRIBUNAL | captured aristocrats stand trial; the board votes life or death; either way the move-set is deposited |
| THE-HAGUE | stacks on TRIBUNAL: judge, jury by lot from both colours, advocates, evidence replayed from the logs, and a restorative verdict alongside life and death |
| SHOGI-DROPS | captured pieces go to the captor's bench and may be dropped back as theirs; allegiance is orientation, not paint |

TRIBUNAL and THE-HAGUE require the append-only piece and square memories.
Without them, ballots fall back to karma weighting.

### Accounting

| Rule | Effect |
|------|--------|
| EXTINCTION-TRIGGERED | deposit only when both pieces of a type are gone, instead of on each capture |
| CROSS-COLOUR-COUNTING | a white rook and a black rook together count as the extinction of rooks, and the deposit lands in both commons |

CROSS-COLOUR-COUNTING is the conservative old accounting and the strongest
metaphor: a technique released by anyone frees everyone, and both armies get a
reason to cooperate before either revolution has finished. It is slower and it
is a variant.

## What the base rules deliberately do not decide

- What promotion grants at the home rank once the commons already grants
  everything. The coronation is defined; its payload is not. Candidates: a vote
  weight, eligibility to be crowned in phase 7, or nothing at all but the title.
- Whether the revolution triggers on checkmate declared or on a king actually
  taken. Most real games end in resignation, so this is not an edge case.
- Whether the surviving king may be taken by any commoner or only by a pawn.
  Restricting regicide to pawns — the pieces that did the dying — is a strong
  reading and a real cost in playability.
- How phases advance. Move count, event count, and player agreement are all
  defensible; the choice belongs to the table.
