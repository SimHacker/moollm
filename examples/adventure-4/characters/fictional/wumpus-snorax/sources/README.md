# Sources — the canonical Wumpus implementations

Curated primary sources only: Yob's originals and the Unix `/usr/games`
lineage. No weekend ports, no perl scripts. The bar for inclusion is
**historic canon**: the implementations that defined the game or carried it
into a new ecosystem.

| File | What | Provenance |
|------|------|-----------|
| [`../wumpus-basic-source.md`](../wumpus-basic-source.md) | **Hunt the Wumpus** (Wumpus 1), Gregory Yob, BASIC, 1973 | People's Computer Company newsletter (Nov 1973); Creative Computing (Sep/Oct 1975); [The Best of Creative Computing Vol 1 scans](https://www.atariarchives.org/bcc1/showpage.php?page=247), with Yob's design essay |
| [`wumpus2-yob.bas`](wumpus2-yob.bas) | **Wumpus 2**, Gregory Yob, BASIC, 1975 — the alternate-cave sequel | Creative Computing (Jan/Feb 1976); [The Best of Creative Computing Vol 2 scans](https://www.atariarchives.org/bcc2/showpage.php?page=244); this transcription via [roug.org's More BASIC Computer Games archive](https://www.roug.org/retrocomputing/languages/basic/morebasicgames/) |
| [`wump-v7.c`](wump-v7.c) | **wump**, C, V7 Unix `/usr/src/games/wump.c`, 1979 — header: "stolen from PCC Vol 2 No 1" | [unix-history-repo](https://github.com/dspinellis/unix-history-repo) (Research-V7); also at [TUHS](https://www.tuhs.org/cgi-bin/utree.pl?file=V7%2Fusr%2Fsrc%2Fgames%2Fwump.c); Caldera license |
| [`wump-bsd.c`](wump-bsd.c) | **wump**, C, BSD games rewrite by Dave Taylor (Intuitive Systems), 1989 — the modern `/usr/games/wump` | Berkeley 1989/1993, BSD-3-clause (header retained); this copy from [NetBSD src](https://github.com/NetBSD/src/blob/trunk/games/wump/wump.c) |

Not included, and why:

- **Wumpus 3** — announced in the Wumpus 1 listing ("WUMP3: DIFFERENT
  HAZARDS") but no published listing has surfaced in the usual archives.
  If a scan turns up, it belongs here.
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
