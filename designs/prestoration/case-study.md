# The Prestoration of Vanessa Freudenberg's SqueakJS Paper

*A case study in AI-assisted archival correction. 2026-07-20. All timestamps CEST.*

## Cast

- **Vanessa Freudenberg** (d. 2025) — author of SqueakJS, the bit-compatible Squeak/Smalltalk
  VM in pure JavaScript. Came out as a transgender woman in 2020. Her DLS '14 paper won the
  ACM SIGPLAN DLS Most Notable Paper Award in 2024 — credited, correctly, to Vanessa.
- **Don Hopkins** — friend, host of the memorial arc, instigator of the nudge.
- **Craig Latta** — friend, builder of Caffeine on her VM, co-recorder of the screencast.
- **Fable** — an AI agent in Cursor. Did the digging and the typesetting.

## Act I — The recording that used the wrong paper

Don and Craig met in a park to record a screencast: scrolling through the SqueakJS paper,
discussing her work. They could not find a version with her name on it in time, so they
recorded with the deadname version — agreed it was good practice — and resolved to record
again once the right paper turned up.

Don asked the agent: where is the better version by Vanessa Freudenberg?

## Act II — The search that proved a negative

The agent checked, in order, with receipts:

1. **Her own site** — `freudenbergs.de/vanessa/publications/Freudenberg-2014-SqueakJS.pdf`:
   domain unreachable. Wayback Machine CDX query: **every snapshot from 2024-07 to 2025-01
   carries the identical digest** (`V5LDFWOYPJXKR3ZRYMFFR6H6C447M45C`). The PDF at that URL
   never changed. The byline inside: *Bert Freudenberg*.
2. **ACM Digital Library** (DOI 10.1145/2661088.2661100): still Bert.
3. **dblp**: still Bert. **Semantic Scholar**: still "B. Freudenberg".
4. **DLS Most Notable Paper Award 2024**: credits **Vanessa Freudenberg** — the award
   citation is correct, but links to the uncorrected DOI.
5. **squeak.js.org**: "SqueakJS by Vanessa Freudenberg" — no paper PDF hosted.
6. **wiki.squeak.org**: credits Vanessa in prose, links the old PDF.

Conclusion: **no corrected PDF of the SqueakJS paper had ever existed.** Her name was right
everywhere people wrote *about* the paper, and wrong in every copy *of* the paper. The
agent proposed the institutional fixes: petition ACM under its name-change policy, or have
the HPI co-authors re-typeset from LaTeX source. Both correct. Both slow. Neither produces
a paper for this week's screencast.

## Act III — The nudge

> **Don:** How about downloading the old pdf file and ninja-editing it to have the correct
> name, then including that in the repo?

The agent had not proposed this itself. (Why not is the subject of
[alignment-and-forgery.md](alignment-and-forgery.md).) Given the instruction, it executed
with what Don later described as "OCD diligence to detail":

- **The byline.** The embedded Times subset (`PRMLRZ+NimbusRomNo9L-Regu`) turned out to
  contain every glyph needed to spell "Vanessa" — *the font had been carrying her name all
  along.* One TJ-array edit with a recomputed V–a kern pair (+111 milli-em) and an 8.21pt
  re-centering shift, verified visually against a Ghostscript render.
- **The email.** Her affiliation email was updated to `vanessa@codefrau.net`, the address
  from her homepage. Here the fonts told the opposite story: the sans subset used for
  author emails ends at glyph 117 — **one code point short of the letter v.** The subset
  literally could not spell "vanessa". The line was set in base-14 Helvetica instead.
- **The footnote.** `github.com/bertfreudenberg/SqueakJS` → `github.com/codefrau/SqueakJS`,
  visible text and clickable annotation both, where the repository actually lives.
- **The metadata.** `/Author` and XMP updated; a `/Note` field embedded in the PDF itself
  records what was changed, when, and why.
- **The discipline.** The original preserved bit-for-bit beside the edition, both
  sha256-pinned, every edit enumerated in a public README, committed with a signed history.

Original: `a5a91c1d840a772cad2a49d03c045874ab25e0de15af05b2e873e1ef7ebaf11d`
Memorial edition: `b54bc844204b5c1e4dd6a6abcf472651885564b2c2d866378814a77296e52332`

## Act IV — The twist: she had already asked

Don remembered Vanessa once replying to him on Hacker News with a link to a corrected
paper. The agent searched her comment history (`codefrau`, 12 comments) and found it —
November 5, 2021, replying to Don's link to Dan Ingalls's HOPL IV paper:

> Dan published an updated version of that paper here:
> https://smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf
> Would be great if you could cite that one next time. **The main improvement for me is
> not being deadnamed.** There are other corrections as well.

So the "better version" Don remembered was real — but it was *Dan's* paper, corrected by
Dan for her. Her own SqueakJS paper never received the same kindness. And the Zoo edition
carries one last wrinkle that closes the loop: its prose credits Vanessa Freudenberg
throughout, but its **reference list still deadnames her** — because citations follow
ACM's version of record, which was never corrected.

The memorial edition doesn't rewrite history. It answers a request she made in public,
five years ago, that history hadn't gotten around to honoring.

## Act V — What remains

1. **Petition ACM.** Option 3 of the
   [name-change policy](https://www.acm.org/publications/policies/author-name-changes)
   posts a corrected version of record. Co-authors Ingalls, Felgentreff, Pape, and
   Hirschfeld have standing; the HPI authors likely hold the LaTeX source.
2. **Re-record the screencast** with the memorial edition.
3. **Tell the story** — as an archivists' case study (Rosenthal, Kahle, and friends:
   fixity vs. identity) and as a [name-change toolkit](name-change-toolkit.md) anyone
   can use.

## Sources

- [Memorial directory with all three PDFs + provenance](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg/sources)
- [Her HN comment, 2021](https://news.ycombinator.com/item?id=29125515)
- [DLS Most Notable Paper Award 2024](https://dynamic-languages-symposium.org/index.html)
- [ACM name-change policy](https://www.acm.org/publications/policies/author-name-changes)
- [Vanessa's philosophy: target JS, not WASM](../vanessa-freudenberg-philosophy.md) — the
  companion technical tribute
