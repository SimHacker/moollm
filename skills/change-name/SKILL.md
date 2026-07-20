---
name: change-name
description: >
  Change a name, email address, phone number, handle, or any identifying
  string across the artifacts where it lives — starting with surgical,
  provenance-disciplined PDF editing: scan the file, describe what's found,
  discuss the changes, perform and verify them. Originals preserved,
  every change disclosed, institutional corrections pursued in parallel.
license: MIT
tier: 2
allowed-tools:
  - run_terminal_cmd
  - read_file
  - write_file
related: [postel, robust-first, sister-script, artifactory, skill-snitch]
tags: [moollm, identity, name-change, pdf, provenance, archives, prestoration]
credits: >
  Founding case: Vanessa Freudenberg's SqueakJS paper (designs/prestoration/).
  Her words, HN 2021: "The main improvement for me is not being deadnamed."
  Precedent: Dan Ingalls's Zoo-corrected HOPL paper. Nudge: Don Hopkins.
---

# CHANGE-NAME 🦋

> *Say my name right — everywhere it's written.*

People change names — transition, marriage, divorce, faith, stage names, safety,
transliteration across scripts. The record does not follow by itself. Names live in
version-of-record PDFs, citation databases, git histories, link annotations, metadata,
and archives engineered never to change. This skill changes them — carefully, honestly,
and with receipts.

**One concrete task ships today:** ninja-editing PDF files. **The context is a socket:**
each venue (git, ACM, ORCID, registries, archives, life admin) plugs in as a playbook in
`playbooks/`. This SKILL.md is self-contained for the PDF task; playbooks extend it.

## The Ethics Gate (read first, always)

A correction is legitimate when **all five** hold. Any four out of five is a forgery
with good manners:

1. **Documented wish or clear standing** — the subject asked (best: find it in their own
   words), or those closest to them act on documented evidence of their identity.
   Standing order: self > subject's recorded request > family/co-authors > community.
2. **Original preserved** — bit-for-bit, sha256-pinned, adjacent to the edition.
3. **Total disclosure** — every change enumerated, in the artifact (embedded note) and
   beside it (README).
4. **Honest labeling** — the filename says what the file is (`-memorial-edition`,
   `-corrected`, never a silent replacement).
5. **Canonical fix pursued** — the edited derivative is a bridge to the institutional
   correction (publisher petition, registry update), never a substitute for it.

**Never out anyone.** A scan that finds every occurrence of an old name is also a map of
someone's exposure. Treat SCAN reports as sensitive; publish only what the subject or
their standing-holders approve.

## Protocol: SCAN → DISCUSS → EDIT → VERIFY → PUBLISH

### 1. SCAN — look at the PDF and describe what you find

Run the sister script (degrades gracefully without pikepdf):

```bash
python3 scripts/pdf_name_scan.py TARGET.pdf --find "Old Name" [--replacement "New Name"]
```

It reports, without changing anything:

- **Document metadata** — `/Author`, `/Title`, docinfo, XMP
- **Content-stream text** — including **kern-split occurrences**: TeX-produced PDFs
  store names like `(Freudenber)18(g)`, invisible to naive grep. The scanner inflates
  streams and matches across TJ kern numbers.
- **Link annotations** — URIs containing the old name (profile links, repo links)
- **Font subsets** — per font: BaseFont, CharSet/FirstChar/LastChar, and **whether the
  embedded glyphs can spell the replacement**. (Founding case: the email font subset
  ended at glyph 117 — one code point short of the letter `v`. It could not spell
  "vanessa". Know this *before* you promise an in-font edit.)

Describe findings to the human in plain language: where the name appears, what fonts
carry it, what can be edited in-font and what needs a fallback face.

### 2. DISCUSS — agree the plan

Present the evidence, then agree, explicitly:

- **Which occurrences** change (byline yes; historical citations in *other* people's
  references may be out of scope), and which stay.
- **Replacement strings** — name, email, URLs (beware redirect masking: an old-handle
  URL that redirects still *displays* the old handle; update visible text).
- **Typography** — in-font where the subset allows (recompute kerning), matched fallback
  face where it doesn't (base-14 Helvetica for sans, Times for serif).
- **Labeling** — the edition's filename and the embedded provenance note text.
- **The gate** — confirm all five conditions; record the wish/standing evidence in the
  ledger.

### 3. EDIT — perform the surgery

With pikepdf, on a **copy** (never the original):

- **Byline/text**: locate the exact TJ array in the page content stream; build the
  replacement with correct kerning (glyph widths from the font's `/Widths`; word gaps
  as `-250`-style TJ numbers; known kern pairs, e.g. V–a ≈ +111 in Times); re-center by
  shifting the text matrix half the width delta; `assert count == 1` for every pattern
  before replacing — bytes, not regex, wherever possible.
- **Annotations**: update `/A//URI` and resize `/Rect` hotspots to the new text width.
- **Metadata**: `/Author`, XMP `dc:creator`; embed a `/Note` docinfo field stating what
  changed, when, why, and by whom.

### 4. VERIFY — prove it

- **Render** the edited pages (Ghostscript → PNG) and *look at them* — centering, font
  match, no keming. Zoom against an unedited neighbor for comparison.
- **Extract** full text (`gs -sDEVICE=txtwrite`) — the old string's count in agreed
  scope must be **zero**; the new string must appear where planned.
- **Regression** — all pages render clean (`-sDEVICE=nullpage`).
- **Hash** original and edition; record both.

### 5. PUBLISH — file it honestly

Original + edition + README side by side. README enumerates every edit, pins both
hashes, cites the wish/standing evidence, and links the canonical-fix path (e.g.
[ACM name-change policy](https://www.acm.org/publications/policies/author-name-changes),
option 3 — corrected version of record). Commit with a message that tells the story.

## Beyond PDFs — the playbook socket

`playbooks/pdf-prestoration.md` is implemented (the founding case, step by step).
Planned playbooks each get one file, same shape (when to use, standing required,
procedure, verification): `git-mailmap` (attribution correction without history
rewrite), `acm-petition`, `orcid`, `registries` (dblp/Scholar/Wikidata),
`web-archives` (layer corrections beside immutable snapshots — fixity is evidence,
not the enemy), `life-admin` (the chores beyond documents). Add a playbook, advertise
it in CARD.yml, and this skill grows a new flower.

## Part of MOOLLM

This skill lives in [MOOLLM](../../README.md) — see [skills/README.md](../README.md)
for the ecosystem. Founding case study: [designs/prestoration/](../../designs/prestoration/).
Works standalone: the protocol above and the script in `scripts/` need only python3,
ghostscript, and pikepdf.
