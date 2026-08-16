# Topologies — the Wumpus 2 caves, extracted

The 1973 listing ([wumpus-basic-source.md](../wumpus-basic-source.md)) *announces*
alternate caves but does not implement them — lines 52–67 are Dave Ahl's
advertisement for the sibling programs (WUMP2: cave arrangements, WUMP3: hazards,
WUMP4: hide-n-seek). The caves themselves live in Gregory Yob's **Wumpus 2**
(*Creative Computing*; source: [wumpus2.bas](https://www.roug.org/retrocomputing/languages/basic/morebasicgames/wumpus2.bas)),
which offers seven choices:

| # | Cave | File | Character |
|---|------|------|-----------|
| 0 | Dodecahedron | [`../DODECAHEDRON.yml`](../DODECAHEDRON.yml) | regular, two-way — Snorax's native territory |
| 1 | Möbius strip | [`MOBIUS-STRIP.yml`](MOBIUS-STRIP.yml) | regular, two-way, one half-twist |
| 2 | String of beads | [`STRING-OF-BEADS.yml`](STRING-OF-BEADS.yml) | regular, two-way, chokepoints ("difficult to play") |
| 3 | Hex network on torus | [`HEX-NETWORK-TORUS.yml`](HEX-NETWORK-TORUS.yml) | regular, two-way, wraps both directions |
| 4 | Dendrite with degeneracies | [`DENDRITE.yml`](DENDRITE.yml) | irregular: tree, self-loops, double tunnels |
| 5 | One-way lattice | [`ONE-WAY-LATTICE.yml`](ONE-WAY-LATTICE.yml) | irregular: every tunnel one-way |
| 6 | Enter your own cave | any `ROOM.yml` network | the original port contract, 1975 |

Cave #6 is the punchline: Wumpus 2 already shipped "bring your own topology."
MOOLLM's version is the port contract in [GAME.yml](../GAME.yml) — any room
network with adjacency, ≥7 rooms, one safe start.

## Topologies are embedded worlds; locations are URLs

Each topology file is an **embedded room network** — virtual rooms you can
navigate without any directory scaffolding. A character or instance points into
one with a location reference, the way a browser encodes state in a URL:

```yaml
lair: topologies/MOBIUS-STRIP.yml#room-7     # file + fragment = where
history:                                      # browser-style back stack
  - DODECAHEDRON.yml#cave-13
  - DODECAHEDRON.yml#cave-12
```

Most game state stays in the **instance file** (memory, arrows, grudges — see
[`../instances/`](../instances/)); locations are just pointers into whichever
topology the session mounted. Swap the file, same game runs on a Möbius strip.

## Errata

The circulating wumpus2.bas listing has three transcription typos, caught by
symmetry-checking (caves 0–3 are documented as two-way: every tunnel must
appear in both rooms' lists). These files ship **corrected** adjacency and
record the printed variant in an `errata:` block:

- **Dodecahedron, room 15**: printed `6,4,16`; the 1973 original reads `6,14,16`
- **Möbius strip, room 15**: printed `12,16,17`; symmetry requires `13,16,17`
- **Hex network, room 10**: printed `5,6,14`; symmetry requires `5,1,14`

The dendrite and one-way lattice are *supposed* to be asymmetric — that's the
"irregular" in the instructions — so they are transcribed verbatim.
