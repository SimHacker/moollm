# Sources — the canonical Wumpus implementations

Curated primary sources only: Yob's originals and the Unix `/usr/games`
lineage. No weekend ports, no perl scripts. The bar for inclusion is
**historic canon**: the implementations that defined the game or carried it
into a new ecosystem.

Every code file is pure source with a language suffix; its story,
provenance, and code review live in a same-named `.md` sidecar. Open
them side by side. The literate treatment of Wumpus 1 is one level up:
[`../wumpus.w.md`](../wumpus.w.md).

| Code | Sidecar | What |
|------|---------|------|
| [`wumpus1-yob.bas`](wumpus1-yob.bas) | [`wumpus1-yob.md`](wumpus1-yob.md) | **Hunt the Wumpus** (Wumpus 1), Gregory Yob, BASIC, 1973 — circulating transcription (genericized dialect, WUMP4 ad) |
| [`wumpus1-bcc1.bas`](wumpus1-bcc1.bas) | [`wumpus1-bcc1.md`](wumpus1-bcc1.md) | Wumpus 1, BCC1 book printing — HP 2000 BASIC dialect (`#`, `GOTO ... OF`, `RND(0)`), `REM: BY GREGORY YOB` credit, two-sequel ad |
| [`wumpus2-yob.bas`](wumpus2-yob.bas) | [`wumpus2-yob.md`](wumpus2-yob.md) | **Wumpus 2**, Gregory Yob, BASIC, 1975 — topology becomes a parameter; seven caves |
| [`wump-v7.c`](wump-v7.c) | [`wump-v7.md`](wump-v7.md) | **wump**, C, V7 Unix, 1979 — "stolen from PCC Vol 2 No 1"; the cave becomes generated |
| [`wump-bsd.c`](wump-bsd.c) | [`wump-bsd.md`](wump-bsd.md) | **wump**, C, Dave Taylor's BSD rewrite, 1989 — connectivity by number theory; still shipping |

Essay and scans:

| File | What | Provenance |
|------|------|-----------|
| [`yob-1975-essay-full-text.md`](yob-1975-essay-full-text.md) | **The complete article text** (pp. 247–250): both essays, tapes sidebar, full sample run, marginalia and illustrations described, OCR emendations logged | Atariarchives text layer, proofread against [`scans/`](scans/) and the program listing |
| [`yob-1975-essay-digest.md`](yob-1975-essay-digest.md) | **Digest and study guide**: genesis, topology, the annotated playthrough, edition comparison | [BCC1 pages 247–250](https://www.atariarchives.org/bcc1/showpage.php?page=247) + archive text layer |
| [`scans/`](scans/) | **Page scans** of the full BCC1 spread (247–250): essay, sample run, hand-drawn maps, listing | Mirrored from [atariarchives.org](https://www.atariarchives.org/bcc1/showpage.php?page=247) (hosted there with the copyright holders' permission) for study and criticism |

Provenance details per implementation are in the sidecars:
Wumpus 1 — PCC newsletter (Nov 1973), Creative Computing (1975),
[BCC1 scans](https://www.atariarchives.org/bcc1/showpage.php?page=247);
Wumpus 2 — [BCC2 scans](https://www.atariarchives.org/bcc2/showpage.php?page=244),
transcription via [roug.org](https://www.roug.org/retrocomputing/languages/basic/morebasicgames/);
V7 — [unix-history-repo](https://github.com/dspinellis/unix-history-repo) /
[TUHS](https://www.tuhs.org/cgi-bin/utree.pl?file=V7%2Fusr%2Fsrc%2Fgames%2Fwump.c), Caldera license;
BSD — [NetBSD src](https://github.com/NetBSD/src/blob/trunk/games/wump/wump.c), BSD-3-clause.

Not included, and why:

- **Wumpus 3** — announced in the Wumpus 1 listing ("WUMP3: DIFFERENT
  HAZARDS") and confirmed real by BCC1 page 248: Yob sold "paper tapes of
  Wumpus, Wumpus 2 and Wumpus 3" for $5.00 each from PO Box 354, Palo
  Alto. But no published listing has surfaced in the usual archives.
  If a scan (or a paper tape) turns up, it belongs here.
- **TI-99/4A Hunt the Wumpus (1981)** — commercial cartridge, source not
  published. Lore only.
- **Ports and remakes** — the game has hundreds; they document enthusiasm,
  not design. The four above are where the design decisions happened.

## Verification

The five alternate cave topologies in [`../topologies/`](../topologies/)
were extracted before this harvest and have now been **cross-checked
programmatically against the DATA statements in `wumpus2-yob.bas`**: three
match exactly (string of beads, dendrite, one-way lattice), and the two
differences are precisely the documented errata — Möbius strip room 15
(printed `12,16,17`, corrected `13,16,17`) and hex torus room 10 (printed
`5,6,14`, corrected `5,1,14`), both non-reciprocal tunnels in the published
listing. This transcription also preserves the famous Wumpus 2 dodecahedron
typo (room 15: `6,4,16` for `6,14,16`), which is how you know it's faithful
to the printed page.

## Lineage in one paragraph

Yob wrote Wumpus at the People's Computer Center in 1973 to escape the
10×10-grid hide-and-seek games (Hurkle, Snark, Mugwump) — "topology turned
out to be the answer." PCC printed it; Creative Computing reprinted it;
Wumpus 2 made the topology a *parameter* (six caves including
enter-your-own); V7 Unix carried a C version into every university machine
room ("stolen from PCC Vol 2 No 1" is the whole citation culture of 1979 in
six words); and Dave Taylor's 1989 BSD rewrite is the one still shipping in
games packages today. The MOOLLM character on top of these:
[Snorax](../README.md), whose [rules](../GAME.yml) are distilled from the
1973 BASIC and whose [caves](../topologies/) are extracted from the 1975
sequel.
