# Revolutionary Chess

The game that begins when the king falls.

Invented by Don Hopkins. This directory is the design: what the variant is, why
it is built the way it is, and what it is good for besides chess.

Companions: [RULES.md](RULES.md) — the normative spec ·
[BRINGING-IT-HOME.md](BRINGING-IT-HOME.md) — the frontier-and-return argument, and
why children should be taught the frontier ·
[GAME-PIECES.md](../GAME-PIECES.md) — the mixin graph pieces are built from ·
[skills/constructionism](../../skills/constructionism/) ·
[snap/moollm-integration.md](../snap/moollm-integration.md)

Running implementation, as a plugin:
[skills/experiment/experiments/turing-chess/plugins/revolutionary-chess](../../skills/experiment/experiments/turing-chess/plugins/revolutionary-chess/)

## The claim

Checkmate is not an ending. It is a change of subject.

Standard chess stops at the moment its central fact becomes interesting: an
army has just discovered that the thing it was organized around is gone, and
thirty-one pieces are still standing on the board. Revolutionary Chess keeps
playing. The rules change, one at a time, and each change is a redistribution
of capability rather than a redistribution of territory.

The single invariant everything else serves:

**When an aristocrat leaves the board or joins the commons, its move-set is
inherited by commoners only.**

Not by other aristocrats. The queen does not gain the knight's jump when the
knight falls. Only the pieces at the bottom rise. A palace coup redistributes
power among the few; this rule makes that impossible to express in the game.

## What is actually new here

Chess has hundreds of variants. Almost all of them change the starting
position, the board, or the move table, and then play a normal game to a normal
end. Four things here are unusual, and the variant collapses without any of them.

**The game continues past its own end condition.** The end condition is
intercepted, not deleted. Standard chess is played in full, with real stakes,
and then its result becomes the initial condition of the next mode. Every
historical game ever recorded is a legal opening, and the canonical one is
Kasparov versus Deep Blue, game 6, 1997: the machine wins, the human leaves the
table, and the pieces are still standing there. The computer won — now what do
we do? See [BRINGING-IT-HOME.md](BRINGING-IT-HOME.md).

**Capture is enfranchisement, not execution.** A taken aristocrat is not
removed and forgotten; it is added to the commons, and so are its moves. This
is what makes the arc converge instead of grinding down to bare kings.

**Move-sets are data, not identity.** A piece is not a queen. A piece is
something that currently delegates to a queen move-set. Powers are held by
reference, so they can be deposited, inherited, shared, and pooled. This is the
[GAME-PIECES.md](../GAME-PIECES.md) mixin graph doing the work: type, rules,
presentation, allegiance, and metadata are separate axes, so "gains queen moves"
is one edge, not a new class.

**The politics are monotonic.** Every event is an addition. Setup deposits the
pawn move-set; revolution deposits the homeward moves; every capture,
surrender, and verdict deposits another. Nothing is ever removed from a
commons. Equality is not a state that gets switched on — it is the limit the
ledger converges to. There is no operation in the game that takes a move away
from the people.

## The commons

The mechanism is prototype delegation, so the mechanism *is* the politics.

There is one commons file per side and one world commons above them. A pawn has
exactly one rules parent: its side's commons. There is no PAWN class — the pawn
move-set is the founding deposit in each side's ledger. Ask "do pawns have queen
moves yet?" and the answer comes from a delegation lookup, never from a cached
flag.

Move-sets are written in side-relative coordinates: *forward* means toward the
enemy's home rank, *homeward* toward your own. One file serves both colors, the
way a rotationally symmetric cellular automaton rule serves every orientation
of its neighborhood. No white-pawn-moves and black-pawn-moves duplication
anywhere.

Aristocracy needs no file of its own. It is defined negatively: an aristocrat is
a piece that inherits no commons. Aristocrats don't share, so there is nothing
to factor out, so there is no class to clean up when the last one joins or
falls. A class file holds what its members have in common, and the elites hold
nothing in common except their refusal to hold things in common.

The degenerate case is a feature. A piece with no move-sets at all does not
crash; its menu is derived from the move-sets present, so an empty commons
yields an empty menu. It just sits there, like furniture. The floor of
degradation is an ottoman, not a stack trace.

## The pawn's widening

The reversal is the first rule change, and it is additive. The pawn does not
turn around — it gains the homeward moves and keeps the forward ones. It now
walks both roads: single step homeward, double step from the far rank, diagonal
capture homeward, and promotion on reaching its own home rank.

That last clause is the one to notice. In standard chess, promotion is a reward
for crossing the whole board away from home. Here the pawn can also be promoted
for coming home. The march that mattered was the return trip.

## What the aristocrats can do

Three options, available when threatened or voluntarily on your own turn:

| Option | Survives | Move-set | Inherits later deposits |
|--------|----------|----------|-------------------------|
| Surrender | yes | donated to the commons | yes — joins as a full equal |
| Bribe | yes | kept private | no |
| Resist | maybe | seized if captured | no |

Surrender is not a demotion. It is enfranchisement: you arrive as an equal with
everything the ledger has accumulated so far, and everything it accumulates
after.

Bribery is the trap, and the trap is arithmetic rather than moral. The bribed
knight keeps its L-jump and inherits nothing else. Meanwhile the commoners
accumulate rook slides, bishop diagonals, and queen lines. The knight ends up
the least mobile thing on the board, still jumping in L-shapes with nothing left
to jump over. Hold onto your privilege and you fall behind; give it up and you
join something that keeps growing.

**Status is earned by deed, not declared.** An aristocrat that captures a
commoner in defense of the old order is marked as such, and the mark is what
other pieces act on. Declarations only count when the log backs them up. The
pieces keep append-only memories and the squares keep their own ledgers, so
loyalty and karma are computed by reading the logs at decision time. A number
can be argued with; a log is testimony.

## Diminishing privilege

The strategy that falls out of the invariant is the interesting part, and it is
not symmetric across piece types.

The queen's move-set is the game-changing deposit, so queens draw maximum
protection and are the highest-value target. Rooks and bishops matter next. The
knight is in a curious position: its jump is unique but not essential, and once
the commons holds rook and bishop moves, leaping is nearly worthless — there is
rarely anything left to leap over. So the knight becomes the natural first
release: the cheapest privilege to give up, the low-stakes token you use to
find out whether cooperation is possible at all.

Privilege is only worth what its scarcity is worth. Every elimination order
tells a different story of liberation.

## Nobody explains any of this to you

Everything above is a payoff table, not a lesson. That is the design, and it is
the point.

Nobody tells you that hoarding decays. You bribe your way out with the knight
because it looked clever, and thirty moves later you are moving the only piece
on the board that cannot get anywhere, watching former pawns glide past it, and
you work out why on your own. Nobody tells you that defection cascades. You hold
out one move too long, once, and after that you can feel the moment coming. And
nobody tells you that only the bottom rises — you discover it as a hard
constraint the first time you want to hand your rook's slide to your queen and
find that the game gives you no way to say it.

The moral consequences are built in the player's head out of their own moves.
They are not delivered. This is Papert: you understand a system because you built
a working model of it and used it and broke it, not because you were given the
finished account. And it is Bogost: the rules *are* the argument. A game
persuades procedurally, through what it makes expensive and what it makes
possible, and the argument that arrives that way arrives as something you know
rather than something you were told.

See [skills/constructionism](../../skills/constructionism/) and
[skills/procedural-rhetoric](../../skills/procedural-rhetoric/).

The joke doubles as the acceptance test. A game about retiring kings, queens and
bishops has no business delivering its point in a lecture from a bishop. If the
argument needs a pope to explain it, the argument is not in the game, and the
design has failed on its own terms.

Which is the honest limit of this document. It is for people implementing the
thing. Players get the rules and a board.

## The arc

Two levels, which the earlier documents sometimes conflate. **Modes** are the
macro state machine; each transition is triggered by an end condition. **Phases**
are the individual rule changes inside the revolution, one at a time, in the
manner of Fluxx.

Modes:

```
STANDARD -> REVOLUTION -> INHERITANCE -> EQUALITY -> COOPERATION -> SANDBOX
```

Phases inside the revolution:

1. The Reversal — homeward moves deposited
2. The Grudge Bearers — capture homeward
3. The Flanking — sideways movement
4. The Coronation — promotion at the home rank
5. The Apotheosis — double promotion
6. No More Privilege — the surviving king is capturable
7. The New Order — any piece can be crowned, by vote

Each mode ends the way chess ends: by running out of the thing it was about.
Competition ends not because it is forbidden but because it stops paying. When
every piece has every move, capturing your mirror image gains you nothing that
was not already shared, and the only move with a return on it is cooperation.
Then the board expands, because the edges were always arbitrary, and the game
becomes crafting and logistics and building. There is no victory condition at
the end. That is the destination, not a failure to design one.

Every competitive system contains the seeds of its own transcendence. The rules
that create the hierarchy also create the conditions for the revolution; the
revolution creates the conditions for equality; equality creates the conditions
for cooperation; cooperation creates the conditions for infinite play.

## Layers, kept separate

Three concerns that are easy to collapse and should not be:

**The piece and rule model.** Prototypes, mixins, delegation, move-sets as
organelles. General to all games with pieces. Lives in
[GAME-PIECES.md](../GAME-PIECES.md).

**The variant.** Revolutionary Chess itself: this directory. A rule state
machine over the piece model. It needs no players, no characters, and no
narration to be well defined, and it can be implemented in any engine that can
intercept a game-end event and edit a delegation table.

**Simulating the players.** Whether the pieces have inner lives, personalities,
grudges and memories they narrate; whether they resent you for move 23 — that is
a social simulation layered *on top of* a game, and the game underneath it need
not be this one. Separate design, documented elsewhere, out of scope here.

The cut between the second and third layer is **authority versus psychology**.
Who is entitled to decide a piece's move is a rule, and rules are this
directory's business. Why a piece wants what it wants is a character, and
characters are somebody else's. A piece can refuse an order for purely
structural reasons — because at this point in the arc nobody is entitled to give
it one — with no inner life whatsoever.

The two compose in one direction and are independent in the other. A social
simulation makes Revolutionary Chess vivid; Revolutionary Chess gives a social
simulation far more to talk about, and a much longer game to talk during. But
neither requires the other, which is the test of whether the layering is real.

## Where the agency goes

The two humans at the board are inside the world model, so "do the pieces still
do what they say?" is a rule question and belongs here.

**At the reversal, nothing about control changes.** Same two players, same
alternation, one piece moved per turn, same hands on the same wood. Only the
legal moves and the goal have changed. This is deliberate: breaking the interface
at the same instant you break the rules makes the moment unreadable. The player
needs exactly one familiar thing to hold onto while everything else moves, and
turn-taking is the cheapest thing to leave alone. Whatever goals emerge — hunt
your own queen, protect the pawn you owe, get everyone home — emerge inside the
old contract.

**Then the interaction model follows the political model.** This is the same
claim as delegation-is-the-politics, pointed at the interface. A monarchy is
played with one hand moving every piece from above; that is what it *is*. A flat
society cannot be played that way without the game arguing against itself. If
the ledger has distributed every capability to every piece and there is still a
single omniscient commander at the console, the design has smuggled the king back
in through the input device.

So agency migrates, in two motions that should not be confused. The **gradient**
is derived, like everything else: how much a piece has to decide is the size of
its own decision space, which is whatever the commons currently gives it. A pawn
holding one forward step needs no free will to express it; a commoner holding
queen lines, rook slides, diagonals and the knight's jump has a real choice every
turn, and being steered from above starts to be the anomaly. Nothing new is
stored, because that number is capability read twice.

The **event** is separate: the moment a piece stops being anyone's to move. That
should be earned by a journey rather than announced by a mode, and the two
candidates are at opposite ends of the same file — a piece that goes out and
returns to its own first rank, and a pawn on the eighth rank that declines the
queenship. Full workshop in [AGENCY.md](AGENCY.md).

The alternative is the explicit grant — free will as a switch the player throws,
The Sims' actual shipped answer. It is more legible and less elegant, and it is a
perfectly good variant.

**The destination is the Sims interaction model.** Select a current character.
Click anything — another piece, the same piece, a square, the board itself, or
any object that has since appeared in the world — and get a pie menu of what that
thing advertises. The board carries global verbs, a square carries local ones, a
piece carries social ones. Menus are *derived from what is present*, never
authored per case, which is the same lookup that answers "do pawns have queen
moves yet?" and the same reason a piece with an empty commons degrades to an
ottoman with an empty menu instead of an exception.

Two more properties of that lookup matter enough to have their own document. It
takes **the asker** as an argument, so the same piece shows one menu to its owner
and a different one to the opponent, with no branching in the piece — Korz
subjective dispatch, where the viewer is a context dimension and the piece is not
special-cased. And it runs **backwards**: click a square and it answers with every
piece that can act on it, either as a move now or as a destination to head for,
which turns any square into a live readout of how far the commons has spread. See
[AGENCY.md](AGENCY.md).

Pie menus pay off twice here, because a radial menu on a board can be oriented
*to the board*: north is forward, the diagonals are the diagonals. Which means a
piece's menu is a picture of its own capability, and the political arc is legible
as geometry. A pawn opens with one slice lit. Later the same pawn opens eight, and
the player sees the inheritance rather than being told about it.

See [skills/advertisement](../../skills/advertisement/),
[skills/action-queue](../../skills/action-queue/),
[sims-find-best-action.md](../sims/sims-find-best-action.md) for the algorithm
underneath, [sims-pie-menus.md](../sims/sims-pie-menus.md) for the menus Don put
in The Sims, and the plugin's
[PIE-MENUS.yml](../../skills/experiment/experiments/turing-chess/plugins/revolutionary-chess/PIE-MENUS.yml)
for the board-aligned version and the four post-revolution player verbs.

**And the world grows the same way the ledger does.** Plant a seed on a square,
water it, and it grows and bears fruit; the grown thing arrives carrying its own
advertisements, so the verb space widens exactly as the move space widened.
Stardew Valley's loop and the commons' loop are one operation seen twice: a
deposit into a place where lookups go. This is why sandbox mode is not a
different game bolted onto the end. It is the same mechanism after the pieces
have run out of aristocrats to liberate and started liberating squares.

What is left for the human is not command. It is attention: who to be with, what
to plant, where to look, and the one decision no piece can make — whether the
game is worth continuing.

The plugin ships a sharper reading, which is that after the revolution influence
is *priced*. Watching is free, a suggestion is cheap and can be ignored, a strong
suggestion lands about four times in five depending on how you have treated the
piece, and an outright override costs ten times a suggestion, lasts one move, and
damages trust. Commanding does not become impossible; it becomes expensive, and
the bill is itemised. That is a good way to make the loss of command something the
player feels rather than reads, and it is the same lesson the knight's owner
learns from the bribe — privilege retained is privilege that stops compounding.

## Design principles, collected

- Bottom-up only. The invariant is structural, not policed.
- Every event is an addition. Politics as a monotonic ledger.
- Derived, never cached. Capability answers come from delegation lookup;
  karma comes from reading logs.
- One edit, one file. World events edit commons contents; they never rewrite a
  piece's parents. Topology is constitution, contents are law.
- Side-relative coordinates. One rule file per move-set, both colors.
- Degrade to furniture, not to an exception.
- Interaction follows politics. A flat board is not played from above.
- Rules are data. The game is whatever the plugins agree it is.

## Provenance

Revolutionary Chess is Don Hopkins' invention, first prototyped in LLOOOOMM
alongside a performance piece in which a chess set decided its own moves by
democratic process. The current running version is a plugin, cited above, whose
`COMMONS.yml` carries the commons and delegation design and whose `MANIFESTO.md`
carries the phase list and the philosophy at length. This directory is the
consolidated design: it supersedes the earlier prototype's rules where they
disagree, and it keeps the ideas the prototype got right.

## Open questions

- Should aristocrats' own piece-type files become seeded micro-commons of one or
  two members, making the entire rule system one uniform mechanism? A question
  for the David Ungar conversation.
- Cross-color accounting: the earlier prototype counted a white rook and a black
  rook together as the extinction of rooks, which released the move-set to
  everyone on both sides and gave the two armies a reason to cooperate before
  either revolution finished. The current base rule deposits on individual
  capture instead, and does not wait for extinction. Both are interesting; the
  cross-color version is the better metaphor and the worse ruleset, and it is
  currently a variant rather than the base.
- Does turn-taking survive autonomy? Alternation is the one thing the reversal
  deliberately leaves alone, but once pieces decide for themselves there is no
  structural reason for them to wait their turn, and The Sims' answer is
  continuous time with an action queue per character. Keeping turns preserves
  chess's readability and the ability to replay a game as notation; dropping them
  is more honest about a board of independent agents and much harder to follow.
  Currently unresolved, and it may be the fork between "a chess variant" and
  "a simulation that starts as chess".
- Does the revolution trigger on checkmate declared, or only on a king actually
  taken? The manifesto says the king falls; the engine hook watches game-end.
  These differ whenever a game ends in resignation, which is most of them.

> "When you see a checkmate, don't see an ending. See the first move of what
> comes next."
