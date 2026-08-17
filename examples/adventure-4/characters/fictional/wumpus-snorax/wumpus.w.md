# HUNT THE WUMPUS — a literate program (first cut)

*Gregory Yob's 1973 BASIC, recast in the manner of Knuth's literate
Adventure ([`advent.w` at Knuth's Stanford
page](https://www-cs-faculty.stanford.edu/~knuth/programs.html#advent))
— a preview of the full treatment.*

Knuth took Woods's FORTRAN and produced `advent.w`: a program ordered
for human understanding, with `CTANGLE` recovering the machine order
and `CWEAVE` typesetting the book. Wumpus makes the same trick almost
embarrassingly easy, because **BASIC line numbers are a tangle that
ships with the program**: any ordering of the sections below, fed to
a 1973 interpreter, sorts itself back into executable order. The
weave is this document; the tangle is `SORT BY LINE NUMBER`. Section
names appear in ⟨angle brackets⟩ as Knuth writes them; the code is
the circulating transcription
([`sources/wumpus1-yob.bas`](sources/wumpus1-yob.bas)), with the 1976
book printing ([`sources/wumpus1-bcc1.bas`](sources/wumpus1-bcc1.bas))
noted where the editions disagree.

In the spirit of the master's introduction: *please play the game
first, at least ten times.* And please regard this as merely a
rearrangement of Yob — the phrases worth keeping are his.

---

## §1. Introduction.

The ur-graph-game for computers — Wumpus — was written by Gregory Yob
in 1973, in revolt against the 10×10 Cartesian grids of Hurkle,
Snark, and Mugwump. His war cry survives: "There has to be a hide and
seek computer game without that (exp. deleted) grid!! In fact, why
not a topological computer game." The player hunts a sleeping monster
through twenty caves joined by tunnels, armed with five arrows that
can fly around corners, warned only by smell, draft, and rustle.

The whole program is some 220 lines of BASIC. It contains, in embryo:
an adjacency-list world model, sensor-based partial information,
autonomous hazard agents, a probabilistic adversary, and a
save-and-replay facility. Two years later Crowther and Woods built
Adventure; the family resemblance is not a coincidence, it is a
lineage. (Knuth: "the ur-game." We are one generation further up the
cave.)

## §2. The program.

A BASIC program of this era is a sequence of numbered statements; we
present it as Knuth would, as a skeleton of named parts. The numbers
are real — this outline *is* the program's memory map.

    ⟨ Greet the hunter and offer instructions  10–50 ⟩
    ⟨ Dave Ahl advertises the sequels          52–67 ⟩
    ⟨ Build the cave                           68–160 ⟩
    ⟨ Define the dice                          170–190 ⟩
    ⟨ Take the census of monsters and hazards  200–340 ⟩
    ⟨ Play one game                            350–620 ⟩
    ⟨ Subroutine: instructions                 1000 ⟩
    ⟨ Subroutine: the senses                   2000 ⟩
    ⟨ Subroutine: move or shoot?               2500 ⟩
    ⟨ Subroutine: the crooked arrow            3000 ⟩
    ⟨ Subroutine: the wumpus stirs             3370 ⟩
    ⟨ Subroutine: walking                      4000 ⟩

Note the round numbers: 1000, 2000, 2500, 3000, 4000. The line-number
namespace is the module system, and Yob laid his subroutines out on
kilobyte boundaries of the address space, so to speak — a programmer
organizing storage he can see.

## §3. Build the cave.

The world is `S(20,3)`: twenty rooms, three tunnels each. Sixty
integers, and they are not arbitrary — they are the vertices and
edges of the dodecahedron.

```basic
68 REM-SET UP CAVE (DODECAHEDRAL NODE LIST)
70 DIM S(20, 3)
80 FOR J = 1 TO 20
90 FOR K = 1 TO 3
100 READ S(J, K)
110 NEXT K
120 NEXT J
130 DATA 2,5,8,1,3,10,2,4,12,3,5,14,1,4,6
140 DATA 5,7,15,6,8,17,1,7,9,8,10,18,2,9,11
150 DATA 10,12,19,3,11,13,12,14,20,4,13,15,6,14,16
160 DATA 15,17,20,7,16,18,9,17,19,11,18,20,13,16,19
```

Yob chose the dodecahedron "simply because it's my favorite Platonic
solid and once, ages ago, I made a kite shaped like one." He chose
better than he lets on. This graph is 3-regular, so every room prints
the same three-tunnel sentence and the interface never betrays
position. It is vertex-transitive, so no starting room is luckier
than another. Its girth is five — the shortest cycle without
reversals — which is Yob's own specification for the weapon: "the
shortest round trip without reversals is 5 caves — and thus the
Crooked Arrow." And it is the graph of Hamilton's 1857 Icosian game,
sold as a wooden puzzle a century before anyone could hunt anything
on it. The board is the oldest graph in recreational mathematics,
reprinted here as four DATA statements.

One invariant is worth stating because no code enforces it: the
adjacency is *reciprocal* (room 1 lists 2, room 2 lists 1). It holds
by authorial discipline alone. In Wumpus 2, a single printed typo
broke it — and silently turned an edge into a one-way door. See
[`sources/wumpus2-yob.md`](sources/wumpus2-yob.md).

## §4. Define the dice.

```basic
170 DEF FNA(X) = INT(20 * RND(1)) + 1
180 DEF FNB(X) = INT(3 * RND(1)) + 1
190 DEF FNC(X) = INT(4 * RND(1)) + 1
```

Three dice: a d20 for rooms, a d3 for tunnels, a d4 for the wumpus's
temperament. The arguments are decorative — BASIC's `DEF FN` required
one, so `X` stands there like a doorman. Everything stochastic in the
game flows through these three functions, which makes the program's
entire probabilistic surface auditable at a glance. (Modern game
programmers call this "own your RNG"; Yob just called it lines
170–190.)

## §5. Take the census.

Six dwellers: you, the wumpus, two pits, two bat colonies. Their
addresses live in `L(1..6)` — the world state is six integers,
indexed *by entity*.

```basic
210 REM-1-YOU,2-WUMPUS,3&4-PITS,5&6-BATS
220 DIM L(6)
230 DIM M(6)
240 FOR J = 1 TO 6
250 L(J) = FNA(0)
260 M(J) = L(J)
270 NEXT J
280 REM-CHECK FOR CROSSOVERS (IE L(1)=L(2),ETC)
290 FOR J = 1 TO 6
300 FOR K = J TO 6
310 IF J = K THEN 330
320 IF L(J) = L(K) THEN 240
330 NEXT K
340 NEXT J
```

Line 320 is rejection sampling at its most cheerful: if *any* two
dwellers collide, throw all six placements away and roll again. The
probability that six uniform draws from twenty rooms are all distinct
is 20·19·18·17·16·15 / 20⁶ ≈ 0.436, so the census fails more often
than it passes and runs about 2.3 times on average. It does not
matter, and knowing that it does not matter is the lesson. `M(1..6)`
is the carbon copy — the original save game, restored at line 560
when the hunter asks for the "SAME SET-UP" after falling down a pit
on move one. Mercy, implemented as an array copy.

## §6. The senses.

```basic
2020 FOR J = 2 TO 6
2030 FOR K = 1 TO 3
2040 IF S(L(1), K) <> L(J) THEN 2110
2050 ON J - 1 GOTO 2060, 2080, 2080, 2100, 2100
2060 PRINT "I SMELL A WUMPUS!"
2080 PRINT "I FEEL A DRAFT!"
2100 PRINT "BATS NEARBY!"
```

For each dweller (skipping yourself), scan your three tunnels; on a
hit, dispatch the message by entity type. Line 2050 is a jump table —
the 1976 printing spells it in the lovelier HP dialect, `GOTO J-1 OF
2060,2080,2080,2100,2100` — and the repeated targets encode the
entity taxonomy: one wumpus, two pits, two bat rooms.

This subroutine is the game. The player never sees the graph; the
player sees a room number, three tunnel numbers, and at most three
sentences of smell, draft, and rustle. Formally: an adjacency oracle
plus 1-neighborhood hazard predicates, from which the hunter must
reconstruct enough of a hidden labeled graph to route a fatal walk.
Yob designed for exactly this play: he fixed the cave numbering "in
the hopes a practised player might notice this and make himself a
permanent map of the caverns." The scraps of scrawled paper he found
on the floor at Stanford's Synergy conference — his first sight of
strangers playing it — were the proof. Graph reconstruction is the
fun part. It still is; ask any roguelike.

## §7. Move or shoot?

```basic
2510 PRINT "SHOOT OR MOVE (S-M)";
2520 INPUT I$
2530 IF I$ <> "S" THEN 2560
2540 O = 1
2550 RETURN
```

The verb set is two. (Adventure would need a vocabulary hash; Wumpus
needs an IF.) The result returns in the global `O`, and the main loop
dispatches `ON O GOTO 440, 480`. Throughout the program, subroutines
report through global registers — `O` the choice, `F` the fate: −1
you lose, 0 play on, +1 you win — checked after every GOSUB like an
exit code. Shell scripting would rediscover this convention a decade
later.

## §8. The crooked arrow.

```basic
3040 PRINT "NO. OF ROOMS(1-5)";
3095 IF K <= 2 THEN 3115
3100 IF P(K) <> P(K - 2) THEN 3115
3105 PRINT "ARROWS AREN'T THAT CROOKED - TRY ANOTHER ROOM"
```

You dictate the arrow's flight plan, up to five rooms. Line 3100 is
the arrow's one aerodynamic law: `P(K) ≠ P(K−2)`, no immediate
reversal — in graph language, the flight is a *non-backtracking
walk*, and on a girth-5 graph the shortest such walk that returns
home has length five. The weapon's name is a theorem.

```basic
3150 FOR K1 = 1 TO 3
3160 IF S(L, K1) = P(K) THEN 3295
3170 NEXT K1
3180 REM-NO TUNNEL FOR ARROW
3190 L = S(L, FNB(1))
```

And the failure mode is graceful: name a room with no tunnel to it,
and the arrow takes a random tunnel instead — aim degrades to a
random walk, without a special error state, and possibly into your
own room ("OUCH! ARROW GOT YOU!"). One craft wart for the connoisseur:
`DIM P(5)` sits at line 3030, *inside* this subroutine, so a strict
interpreter faults the second shot with a re-dimension error.
Allocation wants to live in setup; even in 1973 the second call was
the test that mattered.

## §9. The wumpus stirs.

```basic
3380 K = FNC(0)
3390 IF K = 4 THEN 3410
3400 L(2) = S(L(2), K)
3410 IF L(2) <> L THEN 3440
3420 PRINT "TSK TSK TSK- WUMPUS GOT YOU!"
```

The d4: on 1–3 the wumpus steps through that tunnel, on 4 he stays.
A lazy random walk, P = .75 to move — the fraction is quoted in the
instructions themselves, which is to say Yob published his monster's
transition matrix and the game is scary anyway. The original design
had a findable, shootable, *stationary* wumpus, and Yob's playtest
verdict was "a bit dull. To fix this, the Wumpus was given a little
life." Those four lines are the little life.

## §10. Walking.

```basic
4270 IF L <> L(5) AND L <> L(6) THEN 4310
4280 PRINT "ZAP--SUPER BAT SNATCH! ELSEWHEREVILLE FOR YOU!"
4290 L = FNA(1)
4300 GOTO 4130
```

The move routine checks legality (three tunnels, or — line 4090 — 
your own room, the do-nothing move nobody advertises), then falls
through the hazard gauntlet: wumpus, pits, bats. The bat lines repay
staring at: the snatch re-enters the gauntlet at 4130, so the bat can
drop you on a pit, the wumpus, or *another bat* — the sample run's
"ZAP ... FELL IN PIT" double kill is a legitimate code path, not a
misprint. Yob called the superbats "a rapid transit system gone a
little batty"; a mathematician would say one bat achieves total
mixing, erasing every bit of the map you've built. Both are correct
and his is funnier.

## §11. Endings.

```basic
520 PRINT "HA HA HA - YOU LOSE!"
550 PRINT "HEE HEE HEE - THE WUMPUS'LL GETCHA NEXT TIME!!"
```

The taunts are asymmetric by design — you are mocked in defeat *and*
in victory, which sets the game's whole voice in two PRINT
statements. Then `L(J) = M(J)` restores the census and "SAME SET-UP
(Y-N)" offers the replay. Win, lose, the wumpus abides.

## §12. Remarks toward the full treatment.

What this first cut omits, and the finished web would carry:

1. **The full listing woven in place** — every line present exactly
   once across the sections, so that sorting the code blocks by line
   number reproduces [`sources/wumpus1-yob.bas`](sources/wumpus1-yob.bas)
   byte for byte. (The check is a five-line script; a literate
   program should verify its own tangle.)
2. **An edition apparatus** — BCC1's HP dialect (`#`, `GOTO..OF`,
   `RND(0)`, the `REM: BY GREGORY YOB` credit) footnoted at each
   divergence, per [`sources/wumpus1-bcc1.md`](sources/wumpus1-bcc1.md).
3. **An index** in the Knuth manner — every variable with its cast
   entry: `S` the world, `L` the census, `M` the memory, `F` the
   fate, `O` the choice, `A` the quiver, `J9` the flight plan.
4. **The sequels as appendices** — Wumpus 2's seven caves
   ([`sources/wumpus2-yob.md`](sources/wumpus2-yob.md)) and the two
   Unix rewrites ([`sources/wump-v7.md`](sources/wump-v7.md),
   [`sources/wump-bsd.md`](sources/wump-bsd.md)), where the cave
   stops being authored and starts being generated — first by
   rejection, then by number theory.
5. **Exercises.** (E.g.: prove the crooked arrow cannot return home
   in fewer than five rooms; make the bats carry the wumpus, as Yob
   assigns on page 248; compute the expected number of census
   restarts; find the do-nothing move.)

Knuth closed his Adventure introduction with a warning that fits this
program even better, since Wumpus without gotos is not Wumpus: "if
you don't like goto statements, don't read this. (And don't read any
other programs that simulate multistate systems.)"

---

*Sources, scans, and provenance for everything quoted:
[`sources/README.md`](sources/README.md) and the essay digest
[`sources/yob-1975-essay-digest.md`](sources/yob-1975-essay-digest.md).
Yob's essay quotes are from BCC1 pages 247–248
([scans](sources/scans/)).*
