# The Maze of Twisty Little Passages, All Alike

The first **Korzork** import: a faithful transcription of the all-alike maze
from Crowther & Woods's ADVENT (1977) into jazz YAML, taken from Knuth's
literate `advent.w` (CWEB edition, with Don Woods, 1998) — locations q42–q56,
q80–q87, and q114 in the original numbering, which Knuth preserved in `@q..@>`
margin comments and this transcription preserves in YAML comments.

[`MAZE.yml`](MAZE.yml) is the whole thing: 14 all-alike rooms, the brink of
the pit, and 11 dead ends — including the `NW` exit from `like13` that Knuth's
own comment calls "a dirty trick!", which leads to `dead2`, which is
`chest_loc`: where the pirate hides his treasure chest.

## Why this subset first

The Korzork plan
([korz-prime-cauldron.md §7](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime-cauldron.md))
calls for instance-first extraction of modular, reusable parts. The maze is
the ideal first specimen because it is **pure travel table** — no daemons, no
fuses, no combat, no state. Twenty-six rooms, zero code. It passes the
modularity acceptance test trivially: it runs in a soup that contains none of
the rest of its game (the two boundary exits, `wmist` and `bird`, are declared
external).

By the numbers, Knuth's Adventure is the easier corpus overall: `advent.w` is
4,439 lines *including* all the literate prose and TeX, in one file, versus
20,703 lines of Zork MDL across 19 files, with roughly 500 decision points
against Zork's ~2,200 `COND` clauses.

## What it teaches (the Korz reading)

- **One description, fourteen rooms.** `all_alike` is a single string in the
  original; every like-room points at it. The description is an inherited
  slot; each room materializes only its exits. The maze is a sparse shadow
  tree that shipped in 1977.
- **Identity is behavioral.** The rooms are indistinguishable by observation
  and distinguishable only by how they respond to motion — Knuth: "you can
  psych out the whole maze." Dispatch, not appearance, is identity.
- **Players invent the shadow tree.** The classic technique — drop an object
  in each room to tell them apart — is the player materializing a
  distinguishing slot in an otherwise-inherited room. Disambiguation by
  writing to the world.
- **Self-loops are honest slots.** `like8` south, `like10` north, `like11`
  west and south all lead to themselves — guards that match and return you
  to your own context.

## Provenance

- Knuth's `advent.w`: [cs.stanford.edu/~knuth/programs/advent.w.gz](https://cs.stanford.edu/~knuth/programs/advent.w.gz),
  © 1998 Donald R. Woods and Donald E. Knuth. Transcribed here as data
  (the travel table facts), with Knuth's location numbering and his
  dirty-trick comment credited in place.
- The Zork MDL counterpart corpus: [MITDDC/zork](https://github.com/MITDDC/zork).
- Part of the Korz′ instance-first program:
  [korz-prime.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime.md)
  ("Zorkizing Adventure" and "Instance first: Korzork").

## Siblings

[`../all-different-maze/`](../all-different-maze/) is this maze's structural
opposite from the same cave: eleven rooms, eleven distinct descriptions, all
ten motions defined everywhere — an 11×11 Latin square, the anti-shadow to
this maze's sparse inheritance. The pirate cross-links them: his chest hides
here (at `dead2`), his taunting message lands there (at `pony`).

[`../adventure-4/maze/`](../adventure-4/maze/) is the native MOOLLM maze —
directory-per-room, wumpus warnings, cats. This one is the imported ancestor:
flat, faithful, and forty-nine years old. The adventure compiler should
eventually accept both.
