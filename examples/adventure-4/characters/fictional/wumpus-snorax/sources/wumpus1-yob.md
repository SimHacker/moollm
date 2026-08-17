# wumpus1-yob.bas — sidecar

Code: [`wumpus1-yob.bas`](wumpus1-yob.bas) · Literate treatment:
[`../wumpus.w.md`](../wumpus.w.md) · Siblings: [`README.md`](README.md)

## Provenance

Gregory Yob, 1973, written at/for People's Computer Company; first
printed in the PCC newsletter (November 1973), reprinted in *Creative
Computing* (1975) and *The Best of Creative Computing, Vol. 1* (1976,
pp. 247–250). This file is the **circulating modern transcription**:
genericized dialect (`<>` comparisons, `ON ... GOTO`, `RND(1)`,
`INPUT A$` pauses), Dave Ahl's three-sequel advertisement (WUMP4
included), and a couple of transcription typos it faithfully drags
along ("SUPER RATS", line 1100). The book printing in the original HP
2000 dialect is [`wumpus1-bcc1.bas`](wumpus1-bcc1.bas) with its own
sidecar [`wumpus1-bcc1.md`](wumpus1-bcc1.md); the edition differences
are tabulated in [`yob-1975-essay-digest.md`](yob-1975-essay-digest.md).

## Code review

**The board is the oldest graph in recreational mathematics.** Lines
130–160 encode `S(20,3)`, the adjacency list of the dodecahedral
graph: 20 vertices, 30 edges, 3-regular (cubic), vertex-transitive,
girth 5, diameter 5, Hamiltonian. William Rowan Hamilton sold this
exact object as a puzzle in 1857 — the Icosian game, "travel the
dodecahedron visiting every city once." Yob picked it because he'd
made a kite shaped like one; he landed on the graph whose study named
the Hamiltonian cycle. Every property is load-bearing: 3-regular
means every room reads the same ("TUNNELS LEAD TO x y z"), so the
interface never leaks position; vertex-transitive means no room is
special, so hazard placement is fair by symmetry; girth 5 is Yob's
own sentence, "the shortest round trip without reversals is 5 caves —
and thus the Crooked Arrow."

**Undirected graph, directed storage, invariant by discipline.** Each
edge appears twice in the DATA (room 1 lists 2; room 2 lists 1).
Nothing in the code checks reciprocity — it is an invariant
maintained by the author's care, not the program. Wumpus 2's printed
errata (see [`wumpus2-yob.md`](wumpus2-yob.md)) show exactly what
happens when the discipline slips: a typo silently turns an edge into
a one-way arc, and the cave becomes a digraph nobody designed.

**Index by entity, not by place.** `L(1)`=you, `L(2)`=wumpus,
`L(3–4)`=pits, `L(5–6)`=bats: the world state is an entity→location
map, six integers total. The V7 Unix rewrite
([`wump-v7.md`](wump-v7.md)) transposes the same relation into
location→contents bitmasks. Both are correct; which queries are cheap
is what differs. "Is a pit adjacent to me?" costs a scan here and a
flag test there. Choosing the transpose of your relation is a real
design decision, visible across fifty years of this one game.

**Rejection sampling with the birthday problem.** Lines 240–340 place
all six entities uniformly, then restart *all six draws* if any two
collide. Probability all six of twenty rooms are distinct:
(20·19·18·17·16·15)/20⁶ ≈ 0.436 — so the loop restarts more often
than it succeeds, about 2.3 attempts expected. Correct, simple,
wasteful, and completely fine at this scale: a good first lesson in
knowing when not to optimize. (The restart-everything granularity
also makes the distribution exactly uniform over distinct placements,
which per-item retry would too, but less obviously.)

**The senses are neighborhood predicates.** The 2000 block scans the
three neighbors of your room against `L(2..6)` and dispatches the
message on entity type with `ON J-1 GOTO`. "I SMELL A WUMPUS!" is a
closed-neighborhood query. The whole game is therefore **graph
reconstruction from local sensing**: the player holds an adjacency
oracle (the tunnel listing) and three 1-neighborhood hazard oracles,
and wins by inferring enough of the hidden labeling to aim a length-≤5
walk. Yob knew: he fixed the numbering scheme on purpose, "in the
hopes a practised player might notice this and make himself a
permanent map."

**The crooked arrow is a non-backtracking walk.** The path entry loop
(3070–3115) rejects `P(K) = P(K-2)` — you may not immediately
reverse. That single check plus girth 5 is why a self-hit takes the
full five rooms. When the named room isn't adjacent, line 3190 sends
the arrow through a uniformly random tunnel instead: aim degrades to
a random walk, gracefully, without a special failure state.

**The Wumpus performs a lazy random walk.** Lines 3370–3440: with
probability 3/4 he steps to a uniform neighbor, with 1/4 he stays
(`FNC` rolls 1–4; 4 means stand still). Lazy walks are the standard
trick for making random processes on graphs converge nicely; here the
laziness is dramaturgy — one turn in four, the monster is exactly
where you feared.

**Bats compose.** Line 4290 teleports you uniformly and jumps back to
4130, re-entering the hazard checks — so bat→bat→pit chains are real,
and the sample run's "ZAP--SUPER BAT SNATCH! ... FELL IN PIT" is the
code path, not a fluke. The teleport erases all positional knowledge:
in mixing terms, one bat is total.

**Craft notes, 1973 calling conventions.** Subroutines live at
round-number addresses (1000 instructions, 2000 senses, 2500 choice,
3000 arrow, 4000 move) — the line-number namespace as module system.
Results return in global registers: `O` is the menu choice, `F` is
the status word (−1 lose, 0 continue, +1 win) checked after every
GOSUB — an exit-code convention a decade before shell scripting made
it universal. Two warts worth teaching: `DIM P(5)` sits *inside* the
arrow routine (line 3030), so strict BASICs error on the second shot
(re-dimension) — allocation belongs in setup; and line 4090 accepts
your current room as a legal "move," a do-nothing turn that still
wakes nothing. `M(6)` shadowing `L(6)` is the save-game: "SAME
SET-UP" restores the initial placement, Yob's explicit mercy for
first-move pit deaths.
