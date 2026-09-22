# Playbook: pdf-prestoration

*Surgical name/email/URL/metadata correction inside a PDF, with provenance.
Battle-tested on the founding case: [designs/prestoration/](../../../designs/prestoration/).*

## When to use

A PDF carries an old identity (byline, email, handle, URL) and the five ethics-gate
conditions hold ([SKILL.md](../SKILL.md#the-ethics-gate-read-first-always)). Typical:
author's own request, memorial correction with standing, your own documents.

## Requirements

`python3`, `pikepdf` (`pip install pikepdf`), Ghostscript (`gs`). Vision (or a careful
human eye) for render verification.

## Procedure

### SCAN

```bash
python3 ../scripts/pdf_name_scan.py FILE.pdf \
  --find "Old Name" --find "old@email" --find "oldhandle" \
  --replacement "new@email"
```

Read the report. For each hit note: page, exact TJ bytes, font, and whether the font
can spell the replacement. Hash is in the report header — that's your original's pin.

### DISCUSS

Agree scope, replacements, labeling, and record standing evidence. Do not proceed on
vibes; proceed on a documented wish.

### EDIT (pikepdf, on a copy)

**Text in an embedded font that CAN spell the replacement:**

1. Get glyph widths: `font.Widths`, indexed from `font.FirstChar` (units: milli-em).
2. Compute old and new run widths. TJ numbers *subtract* from displacement: a word gap
   is `-250`; a positive kern like `18` tightens. Include proper kern pairs for the new
   text (Times V–a ≈ `111`).
3. If the run is centered, shift its `Td` x by half the width delta; if a following
   sibling positions relatively, compensate its `Td` by the opposite amount.
4. Replace bytes in `page.Contents.read_bytes()` with `assert data.count(old) == 1`
   first; write back with `page.Contents.write(new_data)`. Bytes, not regex.

**Text in a font that CANNOT spell the replacement** (subsets end early — the founding
case's sans ended one glyph short of `v`):

5. Register a base-14 fallback matched by family (sans → `/Helvetica`, serif →
   `/Times-Roman`) in `page.Resources.Font`; set the run in it, sized to match
   optically (Helvetica ~0.94× of Computer Modern Sans at equal point size), and
   re-center using AFM widths.

**Link annotations:**

6. Update `annot.A.URI`; resize `annot.Rect` to the new visible text width
   (monospace: chars × width × size / 1000).

**Metadata:**

7. `pdf.docinfo['/Author']`, XMP `dc:creator`; add `/Note` docinfo stating what
   changed, when, why, by whom — the artifact must disclose itself.

**Visible correction notice (required — page 1):**

Metadata, filename, README, and a sibling original are necessary but not sufficient. A
renamed or printed copy loses all of them. Page 1 must carry a visible notice.

8. **Draft the notice** in DISCUSS — agree wording with the human. Required facts:
   honest label + date; not the version of record (DOI if any); what changed; standing /
   wish citation; original path + SHA-256; pointer to full change list; canonical fix in
   progress.

9. **Place it** — default: footer band **above** the publisher reference format / copyright
   block (3–4 lines at 7–7.5 pt). Alternative: top margin above the title (1–2 lines;
   full list in attachment). Avoid the author-to-abstract gap and the abstract body.

10. **Set it** — overlay with pikepdf (new content stream or Form XObject on page 1):
    7–7.5 pt sans or house footer face; small caps label line; 0.25 pt rule above; full
    text-block width. Condense for page 1; attach the enumerated edit list as a PDF
    attachment when needed.

11. **OpenTimestamps** (when publishing publicly): proof both original and edition hashes.

See [SKILL.md § Visible correction notice](../SKILL.md#visible-correction-notice-required)
for the full placement table, typography, and example copy. Working overlay script:
[`../scripts/pdf_add_correction_notice.py`](../scripts/pdf_add_correction_notice.py)
(founding case: `designs/prestoration/sources/Freudenberg-2014-SqueakJS-memorial-edition.pdf`).

### VERIFY

```bash
gs -q -dNOPAUSE -dBATCH -sDEVICE=png16m -r220 -dFirstPage=1 -dLastPage=1 -sOutputFile=p1.png EDITION.pdf
gs -q -dNOPAUSE -dBATCH -sDEVICE=txtwrite -sOutputFile=all.txt EDITION.pdf
gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage EDITION.pdf   # all pages render clean
```

- Look at the render: centering, family match, no keming; page-1 notice visible and
  legible at 100% zoom.
- Extract page 1 only — notice text must appear in plain extraction.
- `grep -c "Old Name" all.txt` must be 0 in agreed scope; new strings present.
- Re-run the scanner against the edition to confirm only planned deltas remain.
- `shasum -a 256` both files.

### PUBLISH

Original + edition + README in one directory. README lists every edit, both hashes,
the standing evidence (link the subject's own words if they exist), and the canonical
fix being pursued (e.g. ACM name-change policy option 3). Commit; the history is part
of the disclosure.

## Traps learned the hard way

- **Names hide from grep**: kern-split TJ arrays. Always scan inflated streams with the
  kern-tolerant matcher, never raw `grep`.
- **Raw-byte scans lie**: a match in raw bytes may be uncompressed debris; a *miss* in
  raw bytes proves nothing. Inflate first.
- **Subset fonts end early**: check `/CharSet` / `/LastChar` before promising in-font
  edits.
- **Redirects mask old handles**: `github.com/oldname/...` redirects fine and still
  displays the old name. Fix the visible text too.
- **`/tmp` is not an archive**: stage working files somewhere durable; re-verify hashes
  after any gap.
- **Metadata-only disclosure**: `/Note` in docinfo, README, and filename do not survive
  rename or print. Always add the visible page-1 notice.
- **Notice too small or buried**: 6 pt and side-margin rotation fail legibility and plain
  extraction. Footer band at 7–7.5 pt is the default.
