# Prestoration 🕯️📜

**prestoration** *(n., portmanteau: preservation + restoration)* — correcting a historical
record to say what its subject asked it to say, while preserving the original bit-for-bit
beside it, with every change enumerated, hashed, and signed in public.

Not forgery. Not revisionism. Conservation with receipts.

This directory is the hub for the whole project: the case, the ethics, the
blow-by-blow, the reusable skill that came out of it, and the tools that made
the write-up possible.

## The case

On 2026-07-20, Don Hopkins and Craig Latta recorded a memorial screencast reading Vanessa
Freudenberg's SqueakJS paper (DLS '14, Most Notable Paper 2024) — and could only find the
version bearing her deadname. An AI agent (Fable, in Cursor) searched every public copy:
ACM, dblp, Semantic Scholar, her own site's Wayback snapshots (all bit-identical). No
corrected version had ever existed. Don nudged: *"How about downloading the old pdf file
and ninja-editing it to have the correct name?"* Twenty minutes of font-subset archaeology
later, a memorial edition existed — and the hunt for precedent then surfaced Vanessa's own
2021 Hacker News comment asking, in her own words, not to be deadnamed in citations.

She had asked for exactly this. The record just hadn't listened yet.

## The documents (this directory)

| Document | What |
|----------|------|
| [case-study.md](case-study.md) | The full story: the search, the nudge, the surgery, the twist |
| [alignment-and-forgery.md](alignment-and-forgery.md) | Head-on: was this forgery? why didn't the AI propose it? who has standing to correct history? The five-condition legitimacy test |
| [play-by-play.md](play-by-play.md) | Sportscaster's blow-by-blow of every script, error message, and rabbit hole |
| [screenshots.md](screenshots.md) | **The illustrated version**: five screen snapshots of the agent thinking — glyph inventories, kerning arithmetic, the kern-split grep evidence, the finished byline — with commentary |
| [name-change-toolkit.md](name-change-toolkit.md) | The design seed and brainstorm that grew into the skill below |

## The skill (lifted from this case)

The session was lifted into a reusable MOOLLM skill:
**[skills/change-name/](../../skills/change-name/)** — SCAN → DISCUSS → EDIT →
VERIFY → PUBLISH, with the ethics gate built into the protocol.

| Piece | What |
|-------|------|
| [README](../../skills/change-name/README.md) | Why it exists, how it works, the plugin socket |
| [SKILL.md](../../skills/change-name/SKILL.md) | The self-contained protocol |
| [pdf_name_scan.py](../../skills/change-name/scripts/pdf_name_scan.py) | Working scanner: finds kern-split names, checks font subsets can spell the replacement — tested against the founding PDF |
| [pdf-prestoration playbook](../../skills/change-name/playbooks/pdf-prestoration.md) | The battle-tested procedure, traps included |

Planned playbooks (git-mailmap, ACM petition, ORCID, registries, web archives,
life admin) are sketched in [name-change-toolkit.md](name-change-toolkit.md)
and slotted in the skill's [CARD.yml](../../skills/change-name/CARD.yml).

## The tools (how the write-up was possible)

- **[skills/cursor-mirror/](../../skills/cursor-mirror/)** — introspection into
  the agent's own session history: shell commands, thought bubbles, errors,
  recoveries. The [play-by-play](play-by-play.md) and the change-name skill's
  "traps learned the hard way" were both mined from the transcript with it.
  This is play-learn-lift as programming by demonstration: perform one
  instance, shine cursor-mirror over the thought stream, write up the skill.
- **[anthropic-skill-extensions.md](../anthropic-skill-extensions.md)** — how
  MOOLLM skills build on and extend Anthropic's skill model; why the result is
  composable and shippable.
- **pikepdf + Ghostscript** — the actual surgery and verification instruments;
  see the [playbook](../../skills/change-name/playbooks/pdf-prestoration.md).

## The deliverables (live)

- [Memorial edition PDF](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Freudenberg-2014-SqueakJS-memorial-edition.pdf) — byline corrected to Vanessa Freudenberg
- [Original PDF, untouched](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Freudenberg-2014-SqueakJS-original.pdf) — primary source, sha256-pinned
- [Provenance README](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/README.md) — every edit enumerated
- [Her HN comment](https://news.ycombinator.com/item?id=29125515) — "The main improvement for me is not being deadnamed."
- [The complete 2021 HN thread, preserved verbatim](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/hn-thread-2021-squeakjs.md) — including Don's two parent comments she was replying to (the hybrid-GC appreciation and the Ingalls HOPL quote), parentage verified against the HN API
- [Dan Ingalls's Zoo-corrected HOPL paper](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf) — the paper she asked us to cite; precedent that authors correct their own records
- [The 2023 Croquet Jasmine HN thread, preserved verbatim](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/hn-thread-2023-croquet-jasmine.md) — her VM philosophy in her own words: JavaScript over WASM ("to be honest, fun"), Self's dynamic deoptimization, the Lars Bak lineage to V8
- [Her JIT brain dumps, preserved](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg/sources/jit-notes) — the SqueakJS performance notes and runnable mockups she pointed HN at, in original Markdeep and extracted Markdown
- [Vanessa's character directory](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg) — memorial, profile, sources

## Where this wants to go

- **ACM petition** — [ACM's name-change policy, option 3](https://www.acm.org/publications/policies/author-name-changes)
  posts a corrected version of record. Her co-authors (Ingalls, Felgentreff, Pape,
  Hirschfeld) are the right petitioners, posthumously. The institution has a mechanism for
  "rewriting history" — it just needs to be asked.
- **Case study for archivists** — a Repo Show conversation with David Rosenthal (LOCKSS),
  Brewster Kahle (Internet Archive), and friends: what does fixity mean when the fixed
  bits are wrong about a person? Corrected editions layered *beside* immutable snapshots,
  never replacing them. See the memorial arc:
  [remembering-vanessa-freudenberg.yml](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/remembering-vanessa-freudenberg.yml)
- **The dissertation** — the fuller write-up of the method: one performed
  instance, introspected with cursor-mirror, lifted into a skill — program by
  demonstration where the demonstration is your own transcript. CACM-quality
  argument, Hacker News-quality readability.
- **More playbooks** — every venue in the [toolkit brainstorm](name-change-toolkit.md)
  is a flower waiting to bloom in [skills/change-name/](../../skills/change-name/).

*Part of the [Remembering Vanessa Freudenberg](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/memorial.md) memorial. We represent and discuss; we never speak as her. Her deadname appears in these documents only where the story of correcting it requires.*
