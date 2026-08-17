# wumpus2-yob.bas — sidecar

Code: [`wumpus2-yob.bas`](wumpus2-yob.bas) · Extracted caves:
[`../topologies/`](../topologies/) · Siblings: [`README.md`](README.md)

## Provenance

Gregory Yob's own sequel, 1975; printed in *Creative Computing* and
*The Best of Creative Computing, Vol. 2* (page 244 onward). This
transcription came via roug.org's More BASIC Computer Games archive
and faithfully preserves the printed typos ("I SHELL A WUMPUS!", "YOU
LOOSE!", "ELSEWHERESVILLE") — see the verification notes in
[`README.md`](README.md) for the three cave errata cross-checked
against the extracted [`../topologies/`](../topologies/).

## Code review

**Topology becomes a parameter.** Wumpus 1 hard-wired the
dodecahedron; Wumpus 2 keeps the entire engine (senses, arrow, moves
are line-for-line the same design) and swaps only the DATA. The cave
selector at 2530 dispatches `ON N+1 GOSUB` into seven loaders. This
is the whole idea of data-driven design in one move: the game is a
function of a graph, so ship the function once and enumerate graphs.
Every level editor since is this line item grown up — and cave 6,
"ENTER YOUR OWN CAVE," which reads twenty adjacency rows from the
player, may be the first user-authored level in a published game.

**The DATA pointer is a tape head.** BASIC gives all DATA statements
one global sequential pointer; `RESTORE` rewinds it to the top.
Wumpus 2's caves live in six 60-number blocks, so the loader for cave
k must *seek*: it rewinds (`2585 RESTORE`), then burns through 60·k
values with dummy `READ B0` loops (the `FOR B1/B2` nests at 2735,
2815, 2895, ...) before the real `READ S(J,K)` at 3240. That is
`lseek` implemented in a language with no random access — a perfect
small example of simulating an addressable store on a sequential one,
and of why the *shape* of your storage API leaks into every consumer.

**Six caves are a taxonomy of graph properties.** Yob's instructions
even say so ("CAVES 1-3 ARE REGULAR IN A SENSE THAT..."):

| Cave | Object | What it teaches |
|------|--------|-----------------|
| 0 Dodecahedron | 3-regular, planar, girth 5 | the symmetric baseline |
| 1 Möbius strip | cubic graph from a 2×10 band with a half-twist | the twist lives in the *embedding*; as a bare graph the non-orientability is invisible — topology vs graph structure |
| 2 String of beads | five diamonds joined in a ring | cut vertices and 2-edge bottlenecks; low connectivity is why Yob warns "difficult to play" — hazard warnings pile up at chokepoints |
| 3 Hex network on torus | hex lattice, opposite sides identified | a genus-1 embedding; locally flat, globally wrapped |
| 4 Dendrite w/ degeneracies | a tree plus self-loops and parallel edges | a *multigraph*; no cycles means no round trips — the crooked arrow's five-room trick is dead here, and self-loops make "move" a possible no-op |
| 5 One-way lattice | directed edges only | a digraph by design; "to return, you must go around (about 5 moves)" is a directed-girth statement |

Caves 4 and 5 quietly break assumptions the engine never checks:
reciprocity (gone in 5) and simple-graph-ness (gone in 4). The engine
survives because it only ever reads "the three numbers in your row" —
robustness by ignorance, a design that works until someone's typo
turns cave 0 into cave 5 by accident (which is exactly what the
printed dodecahedron typo at room 15, `6,4,16`, did).

**Error-handling theater.** Line 3180 validates user-entered caves
with `IF S(J,K) > 0 AND S(J,K) < 21 AND ABS(S(J,K))=ABS(S(J,K)) THEN
3210` — the third clause compares a value to itself and is always
true. The intent was surely `INT(S(J,K))=ABS(S(J,K))` (an
integrality check, as used correctly at 1670 and 2240). Lesson one:
validators are code and need testing like code. Lesson two: the bug
is invisible in play, because non-integer rooms mostly behave as
their truncations — failures that don't fail are the ones that ship.

**Ergonomics, 1975.** The input loops grew `ERROR` re-prompts and
integrality checks that Wumpus 1 lacked, and arrows now cost their
path length (`1810 A=A-J9`) instead of one per shot — a real economy
rebalance, making long speculative shots expensive. Sequels tune the
meta, even in 1975.
