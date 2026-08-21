# The Maze of Twisty Little Passages, All Different

The second **Korzork** import, chosen as the structural opposite of
[`../all-alike-maze/`](../all-alike-maze/): eleven rooms (`diff0`–`diff10`,
original locations q107, q112, q131–q139) plus the `pony` dead end (q140),
transcribed faithfully from Knuth's literate `advent.w` — including the fact
Knuth documents in prose: the maze is **an 11×11 Latin square**. Each room
leads to each of the others under the ten motions, with exactly two
exceptions: `diff0` goes down to the entrance (`wlong`), and `diff10` goes
south to the dead end where the vending machine sells fresh batteries for
coins.

## The contrast (why import both)

| | All alike | All different |
|---|---|---|
| Rooms | 14 + brink + 11 dead ends | 11 + 1 dead end |
| Descriptions | **one**, inherited by all | **eleven**, all distinct |
| Exits per room | 2–6, sparse | **all ten**, total |
| Structure | hand-drawn tangle | 11×11 Latin square |
| doesNotUnderstand | most motions fall through | impossible by construction inside |
| How players cope | drop objects (materialize a distinguishing slot) | read carefully (the description IS the coordinate) |

In Korz terms: the all-alike maze is a **sparse shadow tree** — one inherited
description slot, exits materialized only where they exist. The all-different
maze is the **anti-shadow** — every room materializes everything, a total
dispatch table where no send can fail. And its "different" descriptions are
permutations of a single word bag ({maze, little, twisty/twisting, passages}),
so identity lives entirely in word order: a permutation group wearing prose.
One corpus, both extremes of the materialization spectrum, written by Don
Woods in 1977.

Two guards worth noticing:

- The entrance instruction carries Woods's **condition 100 — "Dwarves not
  permitted"** — a guard on the character dimension, Adventure's cousin to
  Zork's `TROLL-FLAG` conditional exits.
- When the pirate robs you, one line cross-links the two mazes:
  `move(CHEST, chest_loc); move(MESSAGE, message_loc);` — the chest lands at
  `dead2` in the *all-alike* maze (behind the NW dirty trick), and a message
  in flowery script lands here at `pony`: *"This is not the maze where the
  pirate leaves his treasure chest."* The game taunts you across mazes.

## Jazzork

Both imports practice **Jazzork**: lifting the historic comments out of the
code and into the YAML jazz data. Knuth's `@q..@>` location numbers, his
"dirty trick!" aside, his Latin-square explanation, his "if you ever get into
a 'little twisting maze of passages,' you're really lost" — all preserved as
comments beside the data they annotate, where the three audiences can read
them: humans for the history, LLMs for the meaning, machines for nothing at
all, which is fine, because the faithful courier forwards the channel that
isn't for it.

## Provenance

- Knuth's `advent.w`: [cs.stanford.edu/~knuth/programs/advent.w.gz](https://cs.stanford.edu/~knuth/programs/advent.w.gz),
  © 1998 Donald R. Woods and Donald E. Knuth.
- Part of the Korz′ instance-first program:
  [korz-prime.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime.md)
  ("Zorkizing Adventure" and "Instance first: Korzork") and its
  [cauldron](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime-cauldron.md).
