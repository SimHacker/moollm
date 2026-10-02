# Gwern, "PDF Forgeries Are Surprisingly Rare" (2022–2025)

Essay: https://gwern.net/blog/2022/pdf-forgery
HN (2026-09-22): https://news.ycombinator.com/item?id=49774269
Harvest: what the essay is doing, not a rewrite of it.

## What he noticed

People fake photos, videos, chat logs, and Word files all the time.
They also write new PDFs full of junk science. They almost never take
an existing published paper, edit the PDF, and let that edited file
circulate as if it were the original.

You can download a paper from someone's personal site and, most of the
time, it is the paper you think it is. The usual failure is version:
a preprint, not a forgery. When a PDF is doing propaganda, it is
usually a new "white paper," not a doctored Nature article.

## Why he thinks that is

A PDF is a compiled print layout, closer to a binary than to a
document you write in. Normal work edits the source (LaTeX, Word) and
exports a new PDF. There is no everyday Photoshop for that compiled
file. Kids edit photos. Almost nobody edits PDFs except designers and
a few specialists. Forgers follow the easy path.

Scribes used to tamper with manuscripts constantly. The constraint
here is the tool culture, not human virtue.

## We already did the hard edit — and wrote the ethics into a skill

On 2026-07-20 Don asked an agent to download Vanessa Freudenberg's
DLS '14 SqueakJS paper and correct the byline. Every public copy
still carried her deadname. ACM, dblp, her own Wayback snapshots:
one digest. No corrected file had ever existed. Twenty minutes of
font-subset work later there was a memorial edition. The email font
in the original could not even spell "vanessa" — the subset ended
one glyph short of `v`. They brought Helvetica.

That is the edit Gwern says almost nobody does: take a real
published PDF and change it. The craft was the same as a forgery
(kerning, TJ arrays, link rects). It was not a forgery because of
process, not because the format is sacred.

Five conditions, all required
([change-name](../../../../skills/change-name/) skill;
[alignment-and-forgery.md](../../../prestoration/alignment-and-forgery.md)):

1. Documented wish or standing — Vanessa's own 2021 HN comment:
   "The main improvement for me is not being deadnamed." Don knew
   her; Dan Ingalls had already quietly corrected a HOPL PDF for
   her while she was alive.
2. Original kept bit-for-bit, hashed, in the same directory.
3. Every change listed in a README and in a `/Note` inside the PDF.
4. The filename says memorial-edition. Nobody is asked to believe
   the 2014 conference shipped this file.
5. The ACM name-change petition is pursued in parallel. The edit
   is a bridge, not a replacement of the record.

Drop any one and the same pikepdf session is a fake. The agent
would not propose the edit on its own: "don't forge documents"
beat "don't use deadnames" until Don had standing and nudged.
That collision is the point of the skill. SCAN, then DISCUSS,
then EDIT. Never out anyone with a scan report.

Playbook: [pdf-prestoration.md](../../../../skills/change-name/playbooks/pdf-prestoration.md).
Case: [designs/prestoration/](../../../prestoration/).

Gwern is still right that silent public-paper impersonation is
rare. He is describing the hole the skill exists to keep from
being filled the wrong way. The HN line "just ask Claude to edit
the PDF" is not a 2026 prediction. It is a job we already did,
and the skill is what makes that job not a crime.

## What the HN thread adds (and does not)

Gwern is talking about *editing an existing public paper* and letting
it spread. He is not saying nobody fakes a PDF.

Private forgeries are common: bank statements, mortgages, KYC,
student IDs, surveys, engineering stamps (sjtgraham, yieldcrv,
cucumber3732842, reddalo). Those are new or privately targeted files,
not a Nature paper on Google Scholar.

Editing tools really are bad (tristanj, mjg59). Small text changes
work; paragraphs and layout fall apart because a sentence is often
many separate text objects. mjg59's landlord/RightSignature case is
already linked in the essay: proving a tamper costs much more than
doing it.

PDFs also do not go viral the way images do (laserbeam). A paper
asks to be read; a fake photo is understood in a glance
(rickdeckard). Those are extra reasons the public-paper attack is
rare. They do not replace the write-only-workflow reason.

Libgen/Sci-Hub will take a file without ISBN or DOI (creatonez asked;
Gwern said yes). The redistribution path he described is real.

"Ask Claude to edit the PDF" (tristanj, 2026) is not hypothetical
here. See the Vanessa case above. The friction dropped for people
who have the skill. The remaining constraint is the five-condition
gate, not Acrobat.

## Two names, applied here

**Reverse over-engineering (Don):** this essay pulls a design out of
an absence. The design is "a PDF of a paper is trustworthy enough to
host on a personal site." The mechanism he offers is compile-only
habit, not signatures. Mark as a hypothesis: HN's private-fraud
examples do not kill it; they bound it to *public academic
impersonation*.

**Simulation effect (Will):** readers treat "it is a PDF" as "a
journal stood behind this." The file implies more institution than it
contains. That is why a personal-site PDF works, and why a forged one
would work if someone did it well.

## What we take for the webtop / git stack

Git is the source document. The built site is the PDF. Do not treat a
screenshot or a one-shot export as the thing you can trust or edit.

Gwern's bet: keep the public paper hard to silently alter, so hosting
it is safe. Our bet on files you can open (cities, rooms, YAML) is
the opposite on purpose — good people must be able to change the
object — so provenance has to live next to the file, not in the
difficulty of the format.

Agents can already edit PDFs. The compiled file is no longer a
moat. What remains is the prestoration rule: keep the original,
disclose every change, pursue the publisher, and do not pretend
the conference shipped the new file. Checksums and a sibling
original are how you tell conservation from a silent fake.
