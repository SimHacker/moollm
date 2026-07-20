# change-name 🦋

> *Say my name right — everywhere it's written.*

A MOOLLM skill for changing a name — or an email address, phone number,
handle, affiliation, any identifying string — across the artifacts where it
lives, with archival discipline: originals preserved bit-for-bit, every change
enumerated and disclosed, institutional corrections pursued alongside
community-scale fixes.

**One concrete capability ships today: ninja-editing PDF files.** Look inside
the PDF and describe what you find, enter into a discussion of what should
change, then perform those changes — kerning-correct, font-aware,
hash-pinned. The skill is built as a socket: more document types and more
name-change chores plug in later as playbooks.

## Why this exists

People change names: transition, marriage, divorce, faith, stage names,
safety, transliteration across scripts. The record does not follow by itself.
Names persist in version-of-record PDFs, citation databases, git histories,
link annotations, metadata, and archives engineered never to change.

The founding case: Vanessa Freudenberg's SqueakJS paper (DLS '14, Most
Notable Paper 2024) existed publicly only under her deadname — even though
she had asked, [in her own words on Hacker News in
2021](https://news.ycombinator.com/item?id=29125515), not to be deadnamed in
citations: *"The main improvement for me is not being deadnamed."* An agent
session produced a memorial edition — byline, email, and repository link
corrected; original preserved beside it; every edit disclosed. The whole
story, ethics discussion, and blow-by-blow are in
[designs/prestoration/](../../designs/prestoration/).

This skill is that session, lifted. Using
[cursor-mirror](../cursor-mirror/), the agent inspected its own transcript —
every shell command, thought bubble, mistake, and recovery — and wrote up
what it had done as a reusable procedure. Play, learn, lift.

## How it works

The protocol is **SCAN → DISCUSS → EDIT → VERIFY → PUBLISH**, specified in
[SKILL.md](SKILL.md). The short version:

1. **SCAN** — [`scripts/pdf_name_scan.py`](scripts/pdf_name_scan.py) reports
   every place a target string lives in a PDF: metadata, content streams
   (including **kern-split text** like `(Freudenber)18(g)` that defeats
   grep), link annotations, and per-font whether the embedded glyph subset
   can even spell the replacement. Read-only; works stdlib-only, better with
   pikepdf.
2. **DISCUSS** — present findings in plain language, agree scope,
   replacements, typography, and labeling with the human. The ethics gate
   lives here.
3. **EDIT** — surgical byte-level content-stream edits with recomputed
   kerning and re-centering, fallback fonts where subsets fall short,
   annotation and metadata updates, provenance note embedded in the file.
4. **VERIFY** — render and look; extract text and count (old string must hit
   zero in agreed scope); hash both files.
5. **PUBLISH** — original + labeled edition + provenance README side by side,
   committed in public.

The full battle-tested procedure, including the traps we hit, is
[playbooks/pdf-prestoration.md](playbooks/pdf-prestoration.md).

## The ethics gate

A correction is legitimate only when **all five** conditions hold — any four
out of five is a forgery with good manners:

1. documented wish or clear standing;
2. original preserved, hash-pinned, adjacent;
3. total disclosure of every change;
4. honest labeling in the filename itself;
5. the canonical institutional fix pursued in parallel (e.g.
   [ACM's name-change policy](https://www.acm.org/publications/policies/author-name-changes)).

And **never out anyone** — a scan that finds every occurrence of an old name
is also a map of someone's exposure. The full argument (was this forgery? who
has standing to correct history? why didn't the AI propose it first?) is in
[alignment-and-forgery.md](../../designs/prestoration/alignment-and-forgery.md).

## The plugin socket

| Playbook | Status | What |
|----------|--------|------|
| [pdf-prestoration](playbooks/pdf-prestoration.md) | **implemented** | Byline/email/URL/metadata surgery in PDFs, with provenance |
| git-mailmap | planned | Attribution correction without history rewrite |
| acm-petition | planned | Corrected version of record via publisher policy |
| orcid | planned | The identity layer citations should have used all along |
| registries | planned | dblp, Semantic Scholar, Google Scholar, Wikidata |
| web-archives | planned | Corrected editions layered beside immutable snapshots |
| life-admin | planned | The non-document chores: accounts, directories, correspondence |

Each playbook is one file with the same shape: when to use, standing
required, procedure, verification. Add one, advertise it in
[CARD.yml](CARD.yml), and the skill grows a new flower.

## Files

| File | What |
|------|------|
| [GLANCE.yml](GLANCE.yml) | One-screen orientation |
| [CARD.yml](CARD.yml) | Machine-readable interface: methods, tools, playbooks, ethics |
| [SKILL.md](SKILL.md) | The self-contained protocol |
| [scripts/pdf_name_scan.py](scripts/pdf_name_scan.py) | The SCAN sister-script (tested on the founding case) |
| [playbooks/pdf-prestoration.md](playbooks/pdf-prestoration.md) | The implemented playbook |

## See also

- [designs/prestoration/](../../designs/prestoration/) — the founding case: story, ethics, play-by-play, design seed
- [Vanessa's philosophy](../../designs/vanessa-freudenberg-philosophy.md) — target JS not WASM, hybrid GC, Self→V8; links memorial edition and preserved threads
- [cursor-mirror](../cursor-mirror/) — the introspection skill used to lift this one from its own transcript
- [sister-script](../sister-script/) — the doc-first automation pattern the scanner follows
- [Vanessa's sources directory](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg/sources) — original, memorial edition, and provenance, live

## Part of MOOLLM

This skill lives in [MOOLLM](../../README.md); see the
[skill ecosystem](../README.md). It also works standalone: the protocol in
SKILL.md and the scanner in scripts/ need only python3, ghostscript, and
pikepdf.

**MIT License** — Copyright (c) 2026 Don Hopkins, Leela AI.
