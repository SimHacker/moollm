# wump-bsd.c — sidecar

Code: [`wump-bsd.c`](wump-bsd.c) · Siblings: [`README.md`](README.md)

## Provenance

Dave Taylor (Intuitive Systems), contributed to Berkeley, 1989;
`games/wump/wump.c` in the BSD distributions ever since (this copy
from NetBSD, whose header runs through 2021). BSD-3-clause. This is
the `/usr/games/wump` still installed by games packages today — the
longest-shipping Wumpus.

## Code review

**Connectivity by number theory.** The jewel of the file is
`cave_init()`. Where Yob authored his graph and V7 rejection-sampled
one ([`wump-v7.md`](wump-v7.md)), Taylor *proves* his cave connected
before rolling a single chord:

```c
do {
        delta = (random() % (room_num - 1)) + 1;
} while (gcd(room_num, delta + 1) != 1);

for (i = 1; i <= room_num; ++i) {
        lnk = ((i + delta) % room_num) + 1;   /* connection */
        cave[i].tunnel[0] = lnk;              /* forw link */
        cave[lnk].tunnel[1] = i;              /* back link */
}
```

Linking every room `i` to `i + (delta+1) (mod n)` builds a circulant
graph on one generator, and the generator steps through *all* n rooms
— one Hamiltonian cycle — exactly when the step is coprime to n.
That's elementary group theory (a cyclic group element generates the
whole group iff its order is coprime to n), enforced by a
three-line `gcd()`. V7 needed "throw the cave away and retry" to get
a connected spine; Taylor gets it with zero rejections and a proof.
When students ask what number theory is *for*, this is a good answer:
it's how `/usr/games/wump` guarantees you're never sealed in a vault.
The cycle also restores a designed invariant that V7 lost — a
guaranteed long way *around*, the ghost of Yob's "shortest round trip
is 5 caves."

**The cave is secretly a digraph.** After the spine, random chords
fill the remaining tunnel slots — but the reciprocal back-link is
added only on a coin flip (`if (random() % 2 == 1) continue;`). So
some tunnels are one-way, on purpose, as a *property of generation*
rather than a special cave. Wumpus 2 offered "ONE WAY LATTICE" as
exotic cave number 5; twenty years later the exotic case is just what
falls out of the generator. Features migrate from content to system.

**Magic tunnels: a bug's field promotion.** Random chords can point
at room numbers beyond `room_num` when parameters allow; instead of
clamping, the game canonizes them — "A faint gleam tells you the
arrow has gone through a magic tunnel!" — as teleporters, with their
own prose and their own rules (walking one triggers `jump()`). This
is the robust-first move: don't crash, don't clamp, *narrate*. The
artifact became a mechanic.

**Everything is a parameter.** `-r` rooms (10–250), `-t` tunnels per
room, `-p` pits, `-b` bats, `-a` arrows, `-h` hard mode; sanity
checks refuse impossible configurations *in fiction* ("Too many
tunnels! The cave collapsed! (Fortunately, the wumpus escaped!)" —
"No self-respecting wumpus would live in such a small cave!"). Yob's
one graph became Wumpus 2's seven, became a two-dimensional design
space with the player at the knobs. Note also `link_num >
room_num - room_num/4` as the collapse threshold and hard mode
scaling hazards with cave size — generated content needs *derived*
difficulty, not constants.

**Probability as dramaturgy.** The 1973 rules were deterministic
outside placement and the wumpus's lazy walk. Taylor layers chance
everywhere, always in service of tension: 2-in-12 to survive a pit by
grabbing a rocky outcrop; bowstring breaks at the third room of an
arrow's flight (20%), the arrow "wavers" at the fourth (60%) — a
distance-decay curve making long shots gambles; and the sneaky
`static int lastchance` inside `shoot()`, escalating the odds the
wumpus moves with *each successive shot* — function-local static
state as a pressure mechanic. Even insults have a distribution:
1-in-15 that bad input earns "Que pasa?".

**Unix citizenship.** The instructions aren't a wall of `printf` like
V7's `intro[]`; they're a file (`_PATH_WUMPINFO`) displayed by
forking `$PAGER` (falling back to `cat` when stdout isn't a tty).
`setgid(getgid())` drops privileges first thing. A game, taking
process hygiene seriously in 1989 — because `/usr/games` binaries ran
setgid for score files, and every one of them was attack surface.

**One contract violation to teach with.** `int_compare()` returns
only −1 or 1, never 0 — technically an invalid `qsort` comparator
(equal elements have no consistent order). It's harmless here because
a room's tunnel list can't contain the duplicate it would take to
expose it... except duplicates *can* survive the chord loop's
skip-duplicates scan interacting with the spine links. It has never
mattered enough for anyone to notice. Interface contracts, kids:
honor them even when today's data forgives you.
