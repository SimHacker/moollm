# wump-v7.c — sidecar

Code: [`wump-v7.c`](wump-v7.c) · Siblings: [`README.md`](README.md)

## Provenance

`/usr/src/games/wump.c` from Seventh Edition Unix, Bell Labs, 1979.
The entire citation is the header comment: "stolen from PCC Vol 2 No
1" — six words carrying author, venue, and the whole easy-come
culture of 1970s code circulation. (PCC Vol 2 No 1 is where Yob's
listing ran in the newsletter.) Copy via the unix-history-repo /
TUHS; Caldera license.

## Code review

**The dodecahedron dies here.** This is the port where the cave stops
being authored and starts being *generated*. The `init:` block builds
a random cave in two phases:

1. **A random spine.** The first loop threads all 20 rooms into a
   random chain: pick a random unvisited room `j`, link the current
   chain-end `k` forward (`room[k].tunn[0] = j`) and `j` backward
   (`p->tunn[1] = k`), advance. When it finishes, tunnels 0 and 1
   trace a random Hamiltonian path through every room. **Connectivity
   is guaranteed by construction** — whatever else the random filler
   does, you can always walk the spine.
2. **Random chords, rejection at whole-graph granularity.** The
   second loop fills every remaining slot via `tunnel(i)` (find a
   random room with a free slot, link both directions), then checks
   each room for self-loops and duplicate tunnels — and on any
   violation does `goto init`: **throw the entire cave away and start
   over.** Compare Yob's hazard-placement restart (six draws) and
   BSD's zero-rejection number theory ([`wump-bsd.md`](wump-bsd.md));
   three answers to "how do I sample a constrained random structure,"
   escalating in sophistication.

The design consequence is real: Yob's cave was vertex-transitive and
girth-5 *on purpose*, so the crooked arrow's five-room minimum was a
theorem about the board. A random cave has no such theorem — short
cycles exist, so this version quietly loses the property Yob's
"Crooked Arrow" was named for. Procedural generation traded away a
designed invariant for variety, in 1979, and the tradeoff has been
with us ever since.

**The relation transposes.** Yob stored entity→location (`L(6)`);
this stores location→contents: `struct room { int tunn[NTUNN]; int
flag; }` with octal masks `BAT 01, PIT 02, WUMP 04`. Hazard sensing
becomes a flag test on neighbors (`near()`), placement becomes
set-a-bit, and the "crossover" check becomes `(flag & (PIT|BAT)) ==
0` — the collision logic Yob wrote as a double loop is now implicit
in the data structure. When the shape of the store matches the shape
of the queries, whole subroutines evaporate.

**Rebalanced for random caves.** Three pits and three bats (`NPIT 3,
NBAT 3` — Yob had two of each), and the wumpus is smelled at distance
*two* (the `near()` scan runs over the neighbors' neighbors). With no
symmetric board to reason about, the game compensates by giving the
player a longer sensor and the cave more teeth.

**A museum of pre-standard C.** Worth reading for the dialect alone:
`=|` and `=&` (the original assignment-operator spellings, before
they flipped to `|=`/`&=` because `i =- 1` was ambiguous);
initializers without `=` (`char *intro[] { ... }`); the lone `#` on
line 1 (the historical way to force the C preprocessor to run);
implicit `int` everywhere; `qsort(&p->tunn[0], NTUNN, 2, icomp)` —
the element width is a literal `2` because ints are two bytes on a
PDP-11; `exit()` with no status. Every one of these is a fossil with
a story, and all of them still compile somewhere.

**Control flow is still BASIC.** Labels `init / setup / loop / again
/ mwump / done` and raw `goto` reproduce the line-number structure of
the original almost 1:1 — this is a state machine, and the labels are
its states. Knuth's own defense (from his literate Adventure: "if you
don't like goto statements, don't read this — and don't read any
other programs that simulate multistate systems") applies verbatim.
The interesting judgment call for a modern reader: which gotos are
the state machine, and which are just 1979?

**One economy change hiding in `case 's'`.** The arrow's room list is
terminated by 0 rather than counted in advance, and an invalid room
is replaced by rejection-sampling *until the random room happens to
be adjacent* (`ranarw`) — same outcome as Yob's random tunnel, less
direct. And the wumpus moves after **every** shot (`goto mwump`), not
just misses that survive: shooting is always noisy. The 3/4-move
lazy walk (`rnum(NTUNN+1)`, move unless the extra face comes up) is
preserved exactly from 1973.
