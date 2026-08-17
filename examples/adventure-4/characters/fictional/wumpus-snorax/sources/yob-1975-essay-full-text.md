# Hunt the Wumpus — the full article text (BCC1 pp. 247–250)

Gregory Yob, "Hunt the Wumpus," in *The Best of Creative Computing,
Volume 1*, ed. David H. Ahl, Creative Computing Press, 1976,
pp. 247–250 (reprinting the 1975 *Creative Computing* appearance).
Transcribed for study and criticism from the
[atariarchives.org text layer](https://www.atariarchives.org/bcc1/showpage.php?page=247),
proofread and corrected against the page scans mirrored in
[`scans/`](scans/) and, for machine output, against the program
listing itself ([`wumpus1-bcc1.bas`](wumpus1-bcc1.bas)) — the PRINT
statements are the best witness to what the terminal printed. OCR
errors are emended (log at the end); the printed page's own oddities
are preserved. Companion digest and code review:
[`yob-1975-essay-digest.md`](yob-1975-essay-digest.md).

---

## Page 247 — [scan](scans/bcc1-page-247.png)

*Another new game from Creative Computing....*

*[Header illustration: a cave cross-section. A superbat hangs from
the ceiling; a bird wearing a number 5 vest perches near caves
numbered 19 and 20; a sleeping Wumpus (a "W" on its belly, "ZZZZ"
overhead) snores in a cave mouth; a sign reads PIT with an arrow. The
hand-lettered title: HUNT THE WUMPUS By GREGORY YOB.]*

### The Genesis of Wumpus

Two years ago I happened by People's Computer Company (PCC) and saw
some of their computer games — such as Hurkle, Snark, and Mugwump. My
reaction was: "EECH!!" Each of these games was based on a 10 x 10
grid in Cartesian co-ordinates and three of them was too much for me.
I started to think along the lines of: "There has to be a hide and
seek computer game without that (exp. deleted) grid!!" In fact, why
not a topological computer game — Imagine a set of points connected
in some way and the player moves about the set via the
interconnections.

That afternoon in meditation the phrase "Hunt the Wumpus" arrived,
and Wumpus was born. He's still a bit vague in physical detail as
most dedicated Wumpus hunters know, but appearances are part of the
game. (If you like, send me a picture of your version of a Wumpus.
Perhaps friendly Dave, our editor, will publish the best one in
*Creative Computing*.) The grid I chose was the vertices of a
dodecahedron — simply because it's my favorite Platonic solid and
once, ages ago, I made a kite shaped like one. The edges became the
connecting tunnels between the caves which were the set of points for
the game.

My basic idea at this time was for the player to approach the Wumpus,
back off, and come up to him by going around the dodecahedron. To my
knowledge, this has never happened... most players adopt other
strategies rather than this cold-blooded approach.

Anyway... how to get the Wumpus! How about an arrow which could turn
corners as it goes from room to room. Let the hunter tell the arrow
where to go and let it fly. The shortest round trip without reversals
is 5 caves — and thus the Crooked Arrow.

Hmmm... How does one sense the Wumpus? It's dark in yonder cave, and
light would wake him up. If one got one cave away, the Wumpus's
distinct smell would serve as a warning. So far, so good... but
Wumpus is still too easy, so let's find some appropriate hazards for
the caves.

Bottomless pits were easy. Any imaginary cave would have a few of
those around the place. Superbats were harder to come by. It took me
a day or two to get that idea. The Superbats are a sort of rapid
transit system gone a little batty (sorry about that one). They take
you a random distance to a random cave and leave you there. If that's
a pit or a Wumpus, well, you are in Fate's hands.

Around this time, I saw that Map-making would be a regular activity
of Wumpus-hunters. I numbered the caves and made the scheme fixed in
the hopes a practised player might notice this and make himself a
permanent map of the caverns. (Another unrealised hope — as an
exercise, make yourself such a map on a Squashed Dodecahedron).

*[Diagram: a pentagon nested inside two larger pentagons, vertices
dotted and joined — captioned "A Squashed Dodecahedron."]*

To start the game fairly, Wumpus, Hazards, and Hunter are located on
different points at the start of the game. Each game starts with
random choices of location, but the hunter may restart with the same
set-up if he chooses. This allows re-plays if the hunter, say, fell
into a pit on the first move.

Wumpus was nearly done in my mind... (hint to a games-writer: Have a
clear notion of your game before you

## Page 248 — [scan](scans/bcc1-page-248.png)

start coding it. This saves MUCH confusion.) yet I felt it was a bit
dull. Once you found the Wumpus all you had to do was shoot it. To
fix this, the Wumpus was given a little life. If you shot an arrow or
moved into his cave, he woke up and chose to move to a neighboring
room or to the same room (one of 4 choices). If you and the Wumpus
were in the same room after he moved, he ATE YOU UP!!

Around here I noticed that the pits and the bats didn't affect the
Wumpus. To explain this, I added some color by making him heavy and
with the legendary sucker feet. After all, evolution works in strange
ways!! If you are a Wumpus fiend, make a version of Wumpus in which
he avoids pits and superbats can carry him only one room (with the
possibility of being dumped into your cave). This can be done by
making the wumpus moving procedure a subroutine.

I wrote Wumpus and dropped it off at PCC. Then I went home and
dreamed up Wumpus II which will be covered in the next issue of
*Creative Computing*.

### The Birth of Wumpus

Around a month later, I went to the Synergy conference at Stanford,
where many of the far-out folk were gathered to share their visions
of improving the world. PCC had a few terminals running in a
conference room and I dropped by. To my vast surprise, all of the
terminals were running Wumpus and scraps of paper on the floor with
scrawled numbers and lines testified that much dedicated
Wumpus-hunting was in progress. I had spawned a hit computer game!!!

Later, PCC published Wumpus in its newsletter (If you haven't seen
it, write them for a subscription: P.O. Box 310, Menlo Park, Cal.
94025), and Wumpus appeared in all sorts of unlikely places. I have
reports of Wumpus written in RPG, a listing of one in FORTRAN, a
rumor of a system command of 'to Wumpus' on a large corporation's R&D
computer system and have even seen an illustrated version for the
Hazeltine CRT terminal!!

### WUMPUS TAPES, ETC.

I can be found at:

> Gregory Yob
> PO Box 354
> Palo Alto, Calif. 94301

Paper tapes of Wumpus, Wumpus 2 and Wumpus 3 are available and cost
$5.00 each.

May your arrows remain straight. — Gregory Yob

### SAMPLE RUN

```
INSTRUCTIONS (Y-N)?Y
WELCOME TO 'HUNT THE WUMPUS'
  THE WUMPUS LIVES IN A CAVE OF 20 ROOMS. EACH ROOM
HAS 3 TUNNELS LEADING TO OTHER ROOMS. (LOOK AT A
DODECAHEDRON TO SEE HOW THIS WORKS-IF YOU DON'T KNOW
WHAT A DODECAHEDRON IS, ASK SOMEONE)

     HAZARDS:
 BOTTOMLESS PITS - TWO ROOMS HAVE BOTTOMLESS PITS IN THEM
     IF YOU GO THERE, YOU FALL INTO THE PIT (& LOSE!)
 SUPER BATS - TWO OTHER ROOMS HAVE SUPER BATS. IF YOU
     GO THERE, A BAT GRABS YOU AND TAKES YOU TO SOME OTHER
     ROOM AT RANDOM. (WHICH MIGHT BE TROUBLESOME)

     WUMPUS:
 THE WUMPUS IS NOT BOTHERED BY THE HAZARDS (HE HAS SUCKER
 FEET AND IS TOO BIG FOR A BAT TO LIFT).  USUALLY
 HE IS ASLEEP. TWO THINGS WAKE HIM UP: YOUR ENTERING
 HIS ROOM OR YOUR SHOOTING AN ARROW.
     IF THE WUMPUS WAKES, HE MOVES (P=.75) ONE ROOM
 OR STAYS STILL (P=.25). AFTER THAT, IF HE IS WHERE YOU
 ARE, HE EATS YOU UP (& YOU LOSE!)

     YOU:
 EACH TURN YOU MAY MOVE OR SHOOT A CROOKED ARROW
   MOVING: YOU CAN GO ONE ROOM (THRU ONE TUNNEL)
   ARROWS: YOU HAVE 5 ARROWS. YOU LOSE WHEN YOU RUN OUT.
   EACH ARROW CAN GO FROM 1 TO 5 ROOMS. YOU AIM BY TELLING
   THE COMPUTER THE ROOM#S YOU WANT THE ARROW TO GO TO.
   IF THE ARROW CAN'T GO THAT WAY(IE NO TUNNEL) IT MOVES
   AT RAMDOM TO THE NEXT ROOM.
     IF THE ARROW HITS THE WUMPUS, YOU WIN.
     IF THE ARROW HITS YOU, YOU LOSE.

    WARNINGS:
     WHEN YOU ARE ONE ROOM AWAY FROM WUMPUS OR HAZARD,
    THE COMPUTER SAYS:
 WUMPUS-  'I SMELL A WUMPUS'
 BAT   -  'BATS NEARBY'
 PIT   -  'I FEEL A DRAFT'

HUNT THE WUMPUS

BATS NEARBY!
YOU ARE IN ROOM  2
TUNNELS LEAD TO  1     3     10

SHOOT OR MOVE (S-M)?M
WHERE TO?1
ZAP--SUPER BAT SNATCH! ELSEWHEREVILLE FOR YOU!
YYYIIIIEEEE . . . FELL IN PIT
HA HA HA - YOU LOSE!
SAME SET-UP (Y-N)?Y
HUNT THE WUMPUS

BATS NEARBY!
YOU ARE IN ROOM  2
TUNNELS LEAD TO  1     3     10

SHOOT OR MOVE (S-M)?M
WHERE TO?3

YOU ARE IN ROOM  3
TUNNELS LEAD TO  2     4     12
```

*[Margin, first game: a hand-drawn map — room 2 circled, arrows to 1,
3, and 10, a cloud marked BATS around room 1. Hand-written: "SUPERBATS
PUT ME IN A PIT SOMEWHERES."]*

## Page 249 — [scan](scans/bcc1-page-249.png)

```
SHOOT OR MOVE (S-M)?M
WHERE TO?4

YOU ARE IN ROOM  4
TUNNELS LEAD TO  3     5     14

SHOOT OR MOVE (S-M)?M
WHERE TO?5

BATS NEARBY!
YOU ARE IN ROOM  5
TUNNELS LEAD TO  1     4     6

SHOOT OR MOVE (S-M)?M
WHERE TO?6

I FEEL A DRAFT
YOU ARE IN ROOM  6
TUNNELS LEAD TO  5     7     15

SHOOT OR MOVE (S-M)?M
WHERE TO?7
YYYIIIIEEEE . . . FELL IN PIT
HA HA HA - YOU LOSE!
SAME SET-UP (Y-N)?Y
HUNT THE WUMPUS

BATS NEARBY!
YOU ARE IN ROOM  2
TUNNELS LEAD TO  1     3     10

SHOOT OR MOVE (S-M)?M
WHERE TO?10

BATS NEARBY!
YOU ARE IN ROOM  10
TUNNELS LEAD TO  2     9     11

SHOOT OR MOVE (S-M)?M
WHERE TO?11
ZAP--SUPER BAT SNATCH! ELSEWHEREVILLE FOR YOU!

YOU ARE IN ROOM  14
TUNNELS LEAD TO  4     13    15

SHOOT OR MOVE (S-M)?M
WHERE TO?15

I SMELL A WUMPUS!
YOU ARE IN ROOM  15
TUNNELS LEAD TO  6     14    16

SHOOT OR MOVE (S-M)?S
NO. OF ROOMS(1-5)?1
ROOM #?16
AHA! YOU GOT THE WUMPUS!
HEE HEE HEE - THE WUMPUS'LL GETCHA NEXT TIME!!
```

*[Margin, second game: the map grows move by move — 2→3→4→5 with
branches to 10, 12, 14 noted; "JUST KEEP ON TRUCKIN!" beside the
chain; after the draft at 6 and death at 7, the pit is marked
"PIT!!" and the note reads "BLEW IT AGAIN!!"]*

*[Margin, third game: 2→10 with 9 and 11 hanging off; a "snatch"
cloud marked BATS at 11; the bats' drop at 14 sketched with 13 and
15; finally 15's neighbors 6, 14, 16 with the Wumpus drawn snoring in
16. Hand-written beside the kill: "CAN YOU FIT THIS MAP INTO THE
OTHER ONE ABOVE? FIGURE OUT HOW I KNEW THE WUMPUS WAS IN 16."]*

## Page 250 — [scan](scans/bcc1-page-250.png)

**PROGRAM LISTING** — transcribed in full, verbatim, as the runnable
source file [`wumpus1-bcc1.bas`](wumpus1-bcc1.bas) (227 lines, HP
2000 BASIC). Kept as code rather than duplicated here; the dialect
notes are in [`wumpus1-bcc1.md`](wumpus1-bcc1.md).

---

## Emendations log

OCR errors corrected against the scans and the program listing;
readings that belong to the printed page are kept even when odd.

| Where | Text layer (OCR) | Emended to | Witness |
|-------|------------------|------------|---------|
| p248 warnings | "WUMPUS OP HAZARD" | "WUMPUS OR HAZARD" | listing line 1350; scan |
| p248 run | "YYYIIIIEFEE" | "YYYIIIIEEEE" | listing line 4230 |
| p248 run | "SAME SET UP (Y-N)?Y" | "SAME SET-UP (Y-N)?Y" | listing line 0590 |
| p248 run, end | "TUNNELS LEAD TO 2 4 10" | "2 4 12" | adjacency DATA (room 3: 2,4,12); scan |
| p248 instructions | "20 ROOMS: EACH ROOM", "IF YOU GO THERE: YOU FALL", "(P=0.75)", "(P=0.25)", "AFTER THAT" punctuation variants | normalized to the listing's PRINT strings | listing lines 1020–1390 |
| p249 | "WHERE T0?4", "T0?5", "T0?6", "T0?7", "LEAD T0" | TO (letter O) | throughout |
| p249 | "WHERE TO?ll", "TO?l5", "ROOMS(l-5)?l" | 11, 15, (1-5)?1 | digit/letter |
| p249 kill turn | "SHOOT OR MOVE (S-M)?M" | "(S-M)?S" | scan (the turn is a shot); listing flow |
| p249 | "HEE HEE HFE" | "HEE HEE HEE" | listing line 0550 |

Preserved as printed (not emended):

- "AT RAMDOM" in the arrow instructions — the two text layers
  *disagree*: the p248 sample-run OCR reads "RANDOM", the p250
  listing OCR reads "RAMDOM" (line 1300). The same program printed
  both, so the printed pages must agree with each other and one OCR
  pass is wrong. We print the listing's reading in both places
  (program identity outranks either OCR pass) and keep the flag; the
  scans are the arbiter.
- "three of them was too much for me" (p247) — Yob's grammar, kept.
- "practised", "unrealised" (p247) — British spellings as printed.
- "fiend,make" spacing (p248) — normalized to "fiend, make"; pure
  typesetting kerning, not a reading.

## Attribution

Text by Gregory Yob (1945–2005); this transcription follows the
atariarchives.org text layer, corrected as logged above. Scans hosted
at [atariarchives.org](https://www.atariarchives.org/bcc1/showpage.php?page=247)
with the copyright holders' permission and mirrored in
[`scans/`](scans/) for study; transcribed here for educational and
critical purposes. Digest, page guide, and edition comparison:
[`yob-1975-essay-digest.md`](yob-1975-essay-digest.md).
