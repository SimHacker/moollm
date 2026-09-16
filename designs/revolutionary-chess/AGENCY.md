# Menus, goals, and who is entitled to act

Work in progress. [README.md](README.md) says agency migrates from the players to
the pieces and that the interaction model should follow the political model. This
is the mechanism, and it is one mechanism: **a menu is the result of a lookup, and
the lookup takes the asker as an argument.**

## The menu is a dispatch, not a property of the piece

Two players sit at a board that has not yet given its pieces any say. There are
two loci of agency and one set of rules. Click your own knight and you get what
that knight can do — first person, or first piece. Click your opponent's knight
and you get what *your* pieces are permitted to do to it, which may be nothing.
Same knight, two menus, and neither of them is the knight's property. The knight
does not contain a list of moves any more than the map contains the territory.

This is [Korz](../korz/README.md) — Ungar, Ossher and Kimelman's subjective
dispatch, named after Korzybski for exactly the reason the map sentence applies —
used for what it is for. Verbs are slots with guards over context dimensions; a
click computes the most specific match for the current context; the target has no
branches in it. The dimensions the chess world needs:

| Dimension | Coordinates | Where it comes from |
|-----------|-------------|---------------------|
| `viewer` | `white`, `black`, `self`, `spectator`, `engine` | who clicked |
| `relation` | `self`, `ally`, `opponent`, `neutral`, `commons-sibling` | derived from viewer + target |
| `mode` | `standard`, `revolution`, `inheritance`, `equality`, `cooperation`, `sandbox` | the arc |
| `agency` | `owned`, `self-directed` | the piece's own history |
| `ledger` | move number | the commons as of now |

`relation` is derived from two other dimensions and never stored, for the same
reason karma is read out of logs instead of kept in a field. `ledger` is the
dating index: the same click on the same square at move 12 and at move 40 are two
different questions, and a cached answer to the first is a wrong answer to the
second.

```yaml
# a pawn's forward step: only its owner may order it, and only while owned
step_forward:
  guard: { relation: self, agency: owned }
  effect: advance one square

# what the other side sees when clicking that same pawn
capture_it:
  guard: { relation: opponent, mode: standard }
  effect: offer captures by any of my pieces that can reach it

# after the revolution the owner's imperative degrades to a request
step_forward_request:
  guard: { relation: self, agency: self-directed }
  cost: influence
  effect: suggest; the pawn decides
```

Nothing above is chess-specific plumbing. It is one guarded-slot table doing the
work that would otherwise be spread across a UI layer, a rules layer and a
permissions layer, all three of which would have to agree.

### Understand is always on the menu

Every object supports **understand**, at all times, and not because the dispatch
failed. The tempting wrong version is Smalltalk's `doesNotUnderstand`: a hook that
fires only after lookup has already missed, which makes explanation the thing you
get when nothing else works. That has it backwards. Explanation is most wanted in
the middle of a full menu, where every item is legal and you cannot tell which one
the rules will reward.

The right precedent is COM's `IUnknown`. Every object implements it without
exception, `QueryInterface` is the one call guaranteed to be there, and "no, I do
not support that" is an answer it returns rather than a dispatch that fell
through. MOOLLM already reads directories this way — see
[DIRECTORY-AS-IUNKNOWN.md](../DIRECTORY-AS-IUNKNOWN.md). Pieces, squares, the
board and the clock carry `understand` for the same reason: it is the floor of the
type system, not a rescue path. The menu is therefore never empty, structurally,
and nobody had to remember to handle the empty case.

**Reflection in a subjective system is itself subjective.** `understand` is
dispatched like any other verb, with `viewer` in the context, so what an object
tells you depends on who is asking:

| Click | What understand answers |
|-------|-------------------------|
| your own piece | its state, what it holds from the commons, what it may do this turn, what it owes and to whom |
| an opponent's piece | the public rules that apply to it, what your pieces may do to it, and why the rest of your menu is empty |
| a self-directed piece | what it wants, if it cares to say — and declining is an answer it is now entitled to give |
| a square | who can reach it, this turn or eventually |
| the board | mode, ledger contents, who is free |
| the clock | whose time is running, and why |

An opponent's piece explaining only what you are entitled to know is not a
limitation bolted on afterwards. It is one guard on one slot, and it means the fog
of the game and the help system are the same mechanism.

This is where [the refusal to lecture](README.md#nobody-explains-any-of-this-to-you)
stays honest rather than turning into obscurantism. Nothing is explained
unprompted; everything is explained on request, about the one thing the player was
curious enough to click. Help is diegetic and pull-only, which is the
constructionist form of documentation — it answers the question you actually have
at the moment you have it.

### Rings: cross-cutting verbs go inside

A radial menu on a chessboard has its outer ring spoken for. North is forward, the
diagonals are the diagonals, and that alignment is what makes a pie menu worth
using here at all. A cross-cutting verb parked out there would have to steal a
direction from board geometry.

So use concentric rings, and let **distance from the centre select the kind of
question while angle selects the item**. The outer ring belongs to the world:
moves, headings, destinations, anything with a direction. An inner ring holds the
verbs that apply to every object regardless of what it is — `understand`, and
whatever else turns out to cut across everything.

Direction still wants to mean something, and the repo's existing convention
already fits: up is how a thing presents, down is what holds it up (the signed
vertical axis in [pie-stack-views](../pie-stack-views/THE-TOWER.md)). So `about`
reads naturally at the top — what this is, in the world's own terms — and
`understand` at the bottom, being the rules, guards and dispatch that produced the
menu you are looking at. Not a commitment to shipping both, just the direction each
one wants if it exists.

The payoff is that the inner ring never changes. As the commons grows, the outer
ring fills up — one slice lit for a fresh pawn, eight for a late one — while the
meta gesture stays exactly where it was in move one. Muscle memory survives the
revolution, for the same reason turn-taking is left alone at the reversal: the
player needs a fixed handhold while the rest transforms.

### The piece as viewer

When a piece becomes self-directed it becomes an asker, and it gets its menu from
the same dispatch with `viewer: self`. The player's view of that piece loses the
imperatives and keeps the requests. One coordinate changes. There is no second
interface for autonomous pieces, no separate AI command path, and no branch
anywhere that reads "if the revolution has happened".

## Clicking a square

Chess selects a piece and then a destination. Squares that advertise invert it:
select the destination and the square answers with everyone who can act on it.
Two kinds of item come back —

- **Moves**: pieces that can reach it this turn, as one move, now.
- **Goals**: pieces that could get there eventually, offered as a standing
  intention rather than a step.

The inversion is the Sims' object model applied to real estate — the verb lives
in the direct object, and a square is an object like any other. See
[sims-object-model.md](../sims/sims-object-model.md) and
[sims-simantics-vm.md](../sims/sims-simantics-vm.md).

What makes it more than a convenience is that **the square is a readout of the
commons**. Early in a game, click an empty square in the middle and three pieces
answer. Forty moves later the same square is reachable by most of the board.
Click a square on your own first rank and ask who can get home: the pawns can,
because pawns turned around; the surviving aristocrats mostly cannot, or not
quickly. The bottom-up invariant stops being a sentence in a rules document and
becomes a spatial fact you can point at. Nobody explains it. You clicked a square
and counted.

The board itself takes global verbs, and it is the natural home for anything that
is nobody's move in particular: what mode are we in, what does the ledger contain,
who is self-directed, show me every piece that can reach here, call a vote.

## Goals that outlive a turn

A goal is a standing intention with a route attached, which is Civilization's
`goto` and the Sims' action queue meeting in the same object. See
[skills/action-queue](../../skills/action-queue/).

The reason it belongs in *this* game rather than being interface sugar: **the
route is computed against a rule set that is changing underneath it.** A pawn
ordered home takes nine turns. Four turns in, a bishop falls, the commons gains
diagonals, and the remaining route is three. The player sees the revolution as
travel time getting shorter — the most legible feedback in the whole design, and
it costs nothing to build, because the path is recomputed from the current ledger
every turn and the ledger only grows. Routes can also worsen: the plugin's
revolution mode puts barricades on the board, and a blockade is a blockade.

Open policy, and a real fork rather than a detail:

- **Interruption.** Does a piece under a standing goal stop when threatened,
  when a better option appears, or never? The Sims answer is priority-based
  interrupt; the chess answer is that you are the one steering and it should do
  what you said. Both are defensible and they play completely differently.
- **Re-planning.** Silent (the piece just gets there sooner) or announced (the
  piece reports that the fall of the bishop shortened its way home)? Silent is
  cleaner, announced is how the player learns the connection between a capture
  and a capability without anyone telling them.

Once pieces are self-directed, goal-setting is where the player keeps a hand in
the game. Dictating a step is expensive and lasts one move; proposing a
destination is cheap and may be adopted as the piece's own project. The player
stops micromanaging and starts campaigning, which is the same demotion described
in [README.md](README.md#where-the-agency-goes), arriving as a change in what is
worth clicking.

## The clock is an object too

Chess has a third participant that no piece can capture and that the rules of
movement never mention. It can be clicked, and after the revolution the question
of whose time it is has no obvious answer. Candidates, all optional:

- **Command runs the clock; watching is free.** Your clock ticks while you are
  issuing orders and pauses while pieces act on their own. Control costs time
  rather than a separate currency — the most chess-native price there is, and it
  means a player who insists on running everything loses on time to a player who
  delegates.
- **Time as a commons.** Increments deposit into a shared pool that any commoner
  may draw from. The ledger already knows how to hold a common resource; this is
  the same append-only mechanism pointed at the one asset both players thought
  was private.
- **The strike.** A quorum of self-directed commoners can stop the clock. Nobody's
  time advances and the game cannot be forced forward. A strike in chess is a
  stopped clock, which is both the correct metaphor and two lines of code.
- **Donation.** A piece gives time to another piece. Fischer increments as a gift
  economy.

Clocks are where this design is most likely to break chess's readability, so
every one of these is off by default. See
[sims-time-events.md](../sims/sims-time-events.md).

## How a piece gets autonomy

The workshop. Each mechanism below is stated with what it argues and what it
costs, because a trigger for self-direction is a claim about where freedom comes
from, and the cheap ones make cheap claims.

**Base: coming home.** A piece that leaves its home rank, goes out into the game,
and returns to its own first rank is self-directed from then on. This is the exact
inversion of promotion, on the same file, at the other end. Walk to the enemy's
back rank and you are made a queen — maximum power, still a tool, promoted into
the class you were fighting. Walk back to your own and you are nobody's piece.
Two opposite rewards at two opposite edges, and the emancipation square is the
address the piece was issued from.

It cannot be reached before the revolution, because pawns cannot go backward
until the reversal, so the mechanism is causally downstream of the politics
instead of running in parallel with them. It generalises to every piece type
without a special case. The round trip must be real — departure and return, not
mere presence — or a rook that never moved would start the game free.

Its cost is a gravitational pull toward the back rank, which drains the middle of
the board late in a game. That may be the correct shape (everybody goes home) or a
defect (nobody contests anything), and it is the first thing to playtest.

**Base: declining the promotion.** A pawn reaching the eighth rank may refuse the
queenship. Accept, and you are the most powerful piece on the board and still take
orders. Decline, and you keep the move-set you inherited and answer to no one.
This adds no mechanism at all — the promotion prompt already exists — and it puts
the game's whole argument into one click at the moment the player most wants the
queen.

**House rule: the refusal.** A piece ordered to certain loss for no compensation
may decline, and its first refusal is the moment it becomes self-directed. Keyed
on the treatment ledger the design already keeps, so a player who has been
spending pawns loses the obedience of pawns first. The player's own record picks
who stops listening. Nothing new to store; read the log.

**House rule: manumission by contact.** A self-directed piece adjacent to an owned
one can free it. Autonomy spreads by proximity, which is organising, and it gives
freed pieces a project other than fighting. Needs a cap or it saturates the board
in a few turns: once per piece per turn, or commoners only, or it costs the
freeing piece its move.

**House rule: quorum.** When a majority of commoners are self-directed, the
remainder become so at once. Solidarity as a threshold rather than an achievement.
Pairs with the cross-colour accounting variant: count both armies together and the
two revolutions finish in the same moment, which is a much better metaphor and a
much harder game to follow.

**House rule: resist and survive.** An aristocrat that chose RESIST and lived is
self-directed and still elite. This is the sharpest thing in the list because it
denies that autonomy is a reward for virtue: it is a description of who is acting
for themselves. The stubborn loyalist stops taking orders too, and the player
learns that losing command of a piece is not the same as the piece changing sides.

**On the shelf: witnessing.** Any piece adjacent to the king when it fell. Listed
because it is the obvious mechanism, and because it is instant, collective and
free, which is to say it argues that freedom is something that happens to you.
Probably too fast. Kept where it can be rejected on purpose.

Autonomy is monotonic, like everything else here: once self-directed, always. But
it can be *spent* — a free piece may choose to follow orders, and that is what
turns a command into a request that gets granted. Consent is not the absence of
obedience.

## Where this stops being chess

Routing does not require hexes; the board stays sixty-four squares, and Civ's
influence here is the standing order, not the map. But once squares carry objects
that grow, the board is a map, pieces are units, and at the far end of the arc the
game is Civilization-shaped. That was always where sandbox mode pointed, and the
honest way to say it is that Revolutionary Chess is a chess variant for as long as
turn-taking survives. When it doesn't, it is a simulation that starts as chess.
That fork is [an open question in README.md](README.md#open-questions), and this
document does not settle it.

## See also

- [README.md](README.md) — the design; [RULES.md](RULES.md) — the normative spec
- [korz/](../korz/) — Ungar's subjective dispatch and the Korz′ design
- [DIRECTORY-AS-IUNKNOWN.md](../DIRECTORY-AS-IUNKNOWN.md) — QueryInterface as a
  filesystem pattern, which is where `understand` comes from
- [pie-stack-views/](../pie-stack-views/) — the pie menu design cluster
- [skills/advertisement](../../skills/advertisement/) — objects volunteering verbs
- [sims-pie-menus.md](../sims/sims-pie-menus.md),
  [sims-find-best-action.md](../sims/sims-find-best-action.md)
- [GAME-PIECES.md](../GAME-PIECES.md) — pieces as compositions of mixins
- The plugin's
  [PIE-MENUS.yml](../../skills/experiment/experiments/turing-chess/plugins/revolutionary-chess/PIE-MENUS.yml)
  — board-aligned radial menus and the priced post-revolution player verbs
