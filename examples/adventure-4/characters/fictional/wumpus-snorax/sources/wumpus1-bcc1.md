# wumpus1-bcc1.bas — sidecar

Code: [`wumpus1-bcc1.bas`](wumpus1-bcc1.bas) · Scan:
[`scans/bcc1-page-250.png`](scans/bcc1-page-250.png) · Essay digest:
[`yob-1975-essay-digest.md`](yob-1975-essay-digest.md)

## Provenance

The listing as printed in *The Best of Creative Computing, Vol. 1*
(1976), page 250, taken from the atariarchives.org text layer with
only unambiguous digit/letter OCR fixes. Same program as
[`wumpus1-yob.bas`](wumpus1-yob.bas), earlier edition: it carries the
credit line `0015 REM: BY GREGORY YOB` (absent from the circulating
transcription) and Dave Ahl's advertisement names only *two* sequels
(WUMP2, WUMP3), dating this printing before WUMP4 existed. The full
edition-difference table is in the essay digest.

## Why keep a second copy of the same program

Because the dialect is the fossil record. This printing preserves the
HP 2000 time-sharing BASIC Wumpus was born in:

- **`#` for not-equals** — `IF I$#"Y" THEN 240`. HP BASIC accepted
  both `#` and `<>`; the printed page says `#`, and every `<>` in the
  circulating transcription is a later hand smoothing the dialect
  away.
- **`GOTO J-1 OF 2060,2080,2080,2100,2100`** — HP's computed GOTO,
  the ancestor idiom that ANSI BASIC spells `ON J-1 GOTO ...`. It is
  a jump table: expression in, address out. The same shape returns as
  `switch` in C and as the dispatch tables in every interpreter since;
  seeing it in 1973 with the branches written as a tuple of line
  numbers makes the "dispatch = indexed data" idea unusually naked.
- **`RND(0)`** vs the transcription's `RND(1)` — RNG seeding
  conventions differed per vendor; porting BASIC meant porting the
  dice.

None of this changes gameplay. That is the point: comparing the two
editions separates the **program** (identical graph, identical rules)
from the **notation** (vendor dialect, later normalization). It is
the cheapest possible lesson in the difference between semantics and
surface syntax — the same lesson ports teach, in miniature, with a
one-page diff.

One open question is flagged rather than fixed: line 1300 prints "AT
RAMDOM" in the archive text layer. Whether that is Yob's/the
typesetter's or the OCR's is undecided; the scan is the arbiter, and
we keep the reading with a flag instead of silently correcting
history. (Editorial rule: emend transcription errors, preserve
printing errors.)
