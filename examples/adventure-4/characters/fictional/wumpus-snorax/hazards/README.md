# Hazards — the second plugin axis, and the one Yob lost

The 1973 listing advertises two axes of variation, four lines apart:

```
64 PRINT "     WUMP2:  SOME DIFFERENT CAVE ARRANGEMENTS"
66 PRINT "     WUMP3:  DIFFERENT HAZARDS"
```

**The caves came back.** Wumpus 2 shipped them, and all six live in
[`../topologies/`](../topologies/) with a manifest, corrected adjacency, and an
errata block recording the transcription typos.

**Wumpus 3 did not.** It was real — [`../sources/README.md`](../sources/README.md)
records the receipt from BCC1 page 248, where Yob sold paper tapes of "Wumpus,
Wumpus 2 and Wumpus 3" for $5.00 each from PO Box 354, Palo Alto — but no
published listing has surfaced in any of the usual archives. If a scan or a paper
tape turns up, it belongs in `../sources/`.

So the two directories are not symmetric, and the asymmetry is the important part:

| | `topologies/` | `hazards/` |
|---|---|---|
| Yob's version | shipped, in Wumpus 2 | shipped, in Wumpus 3, **listing lost** |
| Our files | transcribed, with errata | **written to a contract** |
| Checkable against | Yob's `DATA` statements | nothing |
| Therefore | restoration | invention, which must say so |

**Which is why every hazard declares `canon:`.** The pit and the super-bats are
`canon: wumpus-1` because they are in the original listing. Anything else added
here is invention against an interface, and marked accordingly, so that nobody
six months from now mistakes a good idea for a recovered one.

## The contract

A hazard is pluggable because the game reads one uniform block from it and
nothing else. Each file carries a `hazard:` block — id, a warning with a sense
and a priority, what happens on entering, and placement constraints — and the
full contract with its fields is specified in [`INDEX.yml`](INDEX.yml).

Everything *else* in the file is the piece being whatever kind of thing it is,
and the two shipped hazards deliberately differ:
[`SUPERBATS.yml`](SUPERBATS.yml) carries a `character:` block, because a colony
has a population, a temperament and an alpha;
[`BOTTOMLESS-PIT.yml`](BOTTOMLESS-PIT.yml) carries an `object:` block, because a
hole does not. **One contract, two kinds of being.** The engine cannot tell them
apart and does not need to.

The coupling this replaced is worth naming, because it is the ordinary way
plugin systems fail. `GAME.yml` used to hold the warning list as literal
strings in announce order, so adding a hazard meant editing the rules. Now each
hazard owns its own message and priority and the order is the sort — the same
move as the topology directory, where `mounted_topology` points at a manifest
instead of naming the dodecahedron.

## What the two canonical hazards actually contrast

Worth stating because it is a design lesson rather than trivia. **The pit just
kills you** — no mechanism, no appeal, `on_enter: death`. **The bats ruin your
map** — `on_enter: relocate`, survivable, and for a player who has been carefully
deducing a twenty-room graph from smells and drafts, considerably worse than
dying. One hazard ends the run; the other destroys the thing the run was made of.

And they interact, which is where a plugin axis earns its keep: bats may drop you
into a pit room, or the wumpus room, and the drop may chain into another bat
room. Those cross-references are declared in [`INDEX.yml`](INDEX.yml) so a new
hazard can see what it is joining, and linted so a reference to a hazard nobody
shipped fails the build.

## Adding one

Answer the contract, mark your provenance, pick an unused priority, and drop the
file in. The lints in [`INDEX.yml`](INDEX.yml) will tell you if the placement no
longer fits the mounted topology — two pits, two bat colonies, the wumpus and the
player already need six distinct rooms, which is why `GAME.yml` asks for seven
minimum.

## Related

- [`INDEX.yml`](INDEX.yml) — the manifest, the contract, and the lints
- [`../topologies/`](../topologies/) — the other axis, the one that survived
- [`../GAME.yml`](../GAME.yml) — `mounted_hazards`, and the turn structure that sorts by priority
- [`../sources/README.md`](../sources/README.md) — the Wumpus 3 paper-tape receipt
- [`../../../../../designs/GAME-PIECES.md`](../../../../../designs/GAME-PIECES.md) — hazards as piece prototypes, and why a pit works in a dungeon that never heard of a wumpus
