# Prestoration sources — the founding case files

The primary sources of the founding prestoration case: Vanessa Freudenberg's
SqueakJS paper, before and after, plus the HN comment where she asked for the
correction in her own words. Canonical archival home is the
WillWrightShowForFood repo (characters/vanessa-freudenberg/sources/); these
copies live here so the [prestoration design](../README.md) and the
[change-name skill](../../../skills/change-name/) are self-contained.

## Freudenberg-2014-SqueakJS-original.pdf — before

**"SqueakJS: A Modern and Practical Smalltalk That Runs in Any Browser"**,
DLS '14 (SPLASH, Portland, October 2014). ACM SIGPLAN DLS Most Notable Paper
Award 2024. The author's version exactly as she published it at
`https://freudenbergs.de/vanessa/publications/Freudenberg-2014-SqueakJS.pdf`,
bearing her deadname — preserved unmodified.

- Retrieved via the [Wayback Machine snapshot of 2025-01-19](https://web.archive.org/web/20250119071632/https://freudenbergs.de/vanessa/publications/Freudenberg-2014-SqueakJS.pdf)
  (her site is down)
- sha256: `a5a91c1d840a772cad2a49d03c045874ab25e0de15af05b2e873e1ef7ebaf11d`
- All Wayback snapshots of that URL (2024-07 through 2025-01) share this one
  digest: the PDF was never re-typeset with her name during her lifetime

## Freudenberg-2014-SqueakJS-memorial-edition.pdf — current edition

**Start here.** The corrected memorial edition with a **visible page-1 notice**,
embedded change-list attachment, and updated PDF metadata. Same technical content
as the original; byline and links corrected per Vanessa's stated wish.

- Visible notice on page 1 (top margin; see
  [change-name skill](../../../skills/change-name/SKILL.md#visible-correction-notice-required))
- Attachment: `prestored-change-list.txt` (full enumerated edits)
- sha256: `9c13dabb101df2ca0b5fd97c14f9853e625fde380b71dfdb3aca8072c13bcdda`

Content edits (2026-07-20, from v1 base):

- Page 1 byline: "Bert Freudenberg" → "Vanessa Freudenberg" (re-centered)
- Page 1 email: → `vanessa@codefrau.net`
- Page 4 footnote 2 + link: `github.com/bertfreudenberg/SqueakJS` →
  [`github.com/codefrau/SqueakJS`](https://github.com/codefrau/SqueakJS/)
- PDF Author metadata updated

Notice edition (2026-09): page-1 overlay + attachment + `/Note` metadata update.
Produced by
[`pdf_add_correction_notice.py`](../../../skills/change-name/scripts/pdf_add_correction_notice.py).

How the byline edits were made:
[play-by-play](../play-by-play.md), and the lifted
[pdf-prestoration playbook](../../../skills/change-name/playbooks/pdf-prestoration.md).
Ethics: [alignment-and-forgery.md](../alignment-and-forgery.md).

## Freudenberg-2014-SqueakJS-memorial-edition-v1.pdf — prior edit (archived)

July 2026 edit: byline, email, and footnote corrected; disclosure in filename, README,
and PDF `/Note` only — **no visible page-1 notice**. Kept as the intermediate state
before the September 2026 notice pass. Do not cite by default; use
`Freudenberg-2014-SqueakJS-memorial-edition.pdf` above.

- sha256: `b54bc844204b5c1e4dd6a6abcf472651885564b2c2d866378814a77296e52332`

## hn-thread-2021-squeakjs.md — her request, in her own words

The complete November 2021 Hacker News thread, preserved verbatim with
parentage verified against the HN API. Don linked Dan Ingalls's original
HOPL IV Smalltalk paper; Vanessa replied herself
([codefrau, HN 29125515](https://news.ycombinator.com/item?id=29125515)):

> Dan published an updated version of that paper here:
> https://smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf
> Would be great if you could cite that one next time. **The main improvement
> for me is not being deadnamed.** There are other corrections as well.

That comment is the standing authorization the memorial edition carries out:
she asked, publicly, that the record use her name. Dan's corrected Smalltalk
Zoo edition of the HOPL paper — the paper that already got this treatment —
is not duplicated here; it lives at
[smalltalkzoo.thechm.org](https://smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf).

## The canonical fix still worth pursuing

The [ACM name-change policy](https://www.acm.org/publications/policies/author-name-changes)
(option 3, "Updated Identity") lets ACM post a corrected version of record
([doi:10.1145/2661088.2661100](https://doi.org/10.1145/2661088.2661100) still
says "Bert"). Posthumously, the co-authors — Dan Ingalls, Tim Felgentreff,
Tobias Pape, Robert Hirschfeld — are the right petitioners, and the HPI
co-authors likely still hold the LaTeX source for a proper re-typeset.
