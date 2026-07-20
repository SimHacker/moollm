#!/usr/bin/env python3
"""pdf_name_scan.py — SCAN method of the change-name skill.

Look inside a PDF and report every place a target string lives, without
changing anything. Understands the ways names hide from grep:

  - deflate-compressed content streams (inflates them)
  - kern-split text: TeX stores "Freudenberg" as (Freudenber)18(g),
    so we match across TJ kern numbers
  - link annotations (/A//URI)
  - document metadata (docinfo + XMP)

Also reports, per embedded font, whether its glyphs can spell an intended
replacement string — the founding case's email font subset ended one code
point short of the letter 'v' and could not spell "vanessa".

Works with stdlib only (zlib scan). If pikepdf is installed, adds precise
per-page streams, annotations, docinfo/XMP, and font subset analysis.

Usage:
  python3 pdf_name_scan.py FILE.pdf --find "Old Name" [--find "old@email"]...
                           [--replacement "New Name"] [--context 60] [--json]

Exit code: 0 = ran clean (whether or not matches found); match count is in
the report. This tool never modifies the input file.
"""

import argparse
import hashlib
import json
import re
import sys
import zlib


def kern_tolerant_pattern(target: str) -> re.Pattern:
    """Match target even when split by TJ kern numbers and string breaks.

    In a content stream, "Freudenberg" may appear as (Freudenber)18(g) or
    (F)-1(reudenberg). Between any two characters of the target we allow
    an optional )NUMBER( interruption. Spaces in the target match either a
    literal space or a TJ word gap like )-250( .
    """
    gap = rb"(?:\)\s*-?\d+(?:\.\d+)?\s*\()?"
    word_gap = rb"(?:\)\s*-?\d+(?:\.\d+)?\s*\(| )"
    parts = []
    for ch in target:
        if ch == " ":
            parts.append(word_gap)
        else:
            parts.append(re.escape(ch.encode("latin-1")) + gap)
    return re.compile(b"".join(parts))


def inflate_streams(data: bytes):
    """Yield (offset, inflated_bytes) for every FlateDecode-able stream."""
    for m in re.finditer(rb"stream\r?\n", data):
        start = m.end()
        end = data.find(b"endstream", start)
        if end < 0:
            continue
        try:
            yield start, zlib.decompress(data[start:end])
        except zlib.error:
            continue


def scan_raw(path: str, targets, context: int):
    """Stdlib-only scan: raw bytes + inflated streams, kern-tolerant."""
    data = open(path, "rb").read()
    report = {
        "file": path,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "matches": [],
    }
    corpora = [("raw", data)]
    corpora += [("stream@%d" % off, blob) for off, blob in inflate_streams(data)]
    for target in targets:
        pat = kern_tolerant_pattern(target)
        plain = target.encode("latin-1", "replace")
        for where, blob in corpora:
            for m in set(
                list(pat.finditer(blob)) + list(re.finditer(re.escape(plain), blob))
            ):
                i = m.start()
                ctx = blob[max(0, i - context): m.end() + context]
                report["matches"].append({
                    "target": target,
                    "where": where,
                    "kern_split": b")" in m.group(0),
                    "context": ctx.decode("latin-1", "replace"),
                })
    return report


def scan_pikepdf(path: str, targets, replacement, context: int, report):
    """Precise pass: per-page streams, annotations, metadata, font coverage."""
    import pikepdf

    pdf = pikepdf.open(path)

    info = {}
    if pdf.docinfo:
        for k, v in pdf.docinfo.items():
            info[str(k)] = str(v)
    report["docinfo"] = info
    try:
        with pdf.open_metadata() as meta:
            report["xmp"] = {k: str(meta[k]) for k in ("dc:creator", "dc:title") if k in meta}
    except Exception:
        report["xmp"] = {}

    report["metadata_hits"] = [
        {"field": k, "value": v, "target": t}
        for t in targets
        for k, v in info.items()
        if t.lower() in v.lower()
    ]

    pages = []
    fonts_seen = {}
    for pageno, page in enumerate(pdf.pages, 1):
        entry = {"page": pageno, "text_hits": [], "annot_hits": [], "fonts": []}
        try:
            blob = page.Contents.read_bytes() if not isinstance(
                page.Contents, pikepdf.Array
            ) else b"".join(s.read_bytes() for s in page.Contents)
        except Exception:
            blob = b""
        for t in targets:
            for m in kern_tolerant_pattern(t).finditer(blob):
                i = m.start()
                entry["text_hits"].append({
                    "target": t,
                    "kern_split": b")" in m.group(0),
                    "context": blob[max(0, i - context): m.end() + context].decode("latin-1", "replace"),
                })
        annots = page.get("/Annots")
        if annots:
            for a in annots:
                action = a.get("/A")
                uri = str(action.URI) if action is not None and "/URI" in action else ""
                for t in targets:
                    if t.lower() in uri.lower():
                        entry["annot_hits"].append({"target": t, "uri": uri})
        res = page.get("/Resources")
        fdict = res.get("/Font") if res is not None else None
        if fdict is not None:
            for fname, font in fdict.items():
                base = str(font.get("/BaseFont", "?"))
                key = (pageno, str(fname))
                fd = font.get("/FontDescriptor")
                charset = str(fd.get("/CharSet", "")) if fd is not None else ""
                fc = font.get("/FirstChar")
                lc = font.get("/LastChar")
                finfo = {
                    "name": str(fname),
                    "base": base,
                    "first_char": int(fc) if fc is not None else None,
                    "last_char": int(lc) if lc is not None else None,
                }
                if replacement:
                    finfo["can_spell_replacement"] = can_spell(replacement, charset, fc, lc)
                entry["fonts"].append(finfo)
                fonts_seen[key] = base
        pages.append(entry)
    report["pages"] = [p for p in pages if p["text_hits"] or p["annot_hits"]]
    report["all_fonts"] = sorted(set(fonts_seen.values()))
    return report


def can_spell(text: str, charset: str, first_char, last_char):
    """Can this font subset render every glyph of text? Best-effort check."""
    glyph_names = {
        " ": "space", ".": "period", "@": "at", "-": "hyphen",
    }
    if charset:
        have = set(charset.strip("/").split("/"))
        missing = []
        for ch in text:
            g = glyph_names.get(ch, ch if ch.isalnum() else None)
            if g is not None and g not in have and ch != " ":
                missing.append(ch)
        return {"ok": not missing, "missing": sorted(set(missing)), "via": "CharSet"}
    if first_char is not None and last_char is not None:
        missing = sorted({c for c in text if not int(first_char) <= ord(c) <= int(last_char)})
        return {"ok": not missing, "missing": missing, "via": "FirstChar..LastChar"}
    return {"ok": None, "missing": [], "via": "unknown"}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pdf")
    ap.add_argument("--find", action="append", required=True,
                    help="string to locate (repeatable): old name, email, handle...")
    ap.add_argument("--replacement", help="intended new string, for font coverage check")
    ap.add_argument("--context", type=int, default=60)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    report = scan_raw(args.pdf, args.find, args.context)
    try:
        report = scan_pikepdf(args.pdf, args.find, args.replacement, args.context, report)
        report["engine"] = "pikepdf"
    except ImportError:
        report["engine"] = "stdlib (pip install pikepdf for pages/annots/fonts)"

    if args.json:
        json.dump(report, sys.stdout, indent=2)
        print()
        return

    print(f"# SCAN {report['file']}")
    print(f"sha256 {report['sha256']}  ({report['bytes']} bytes)  engine: {report['engine']}")
    for hit in report.get("metadata_hits", []):
        print(f"METADATA  {hit['field']} = {hit['value']!r}   <- {hit['target']!r}")
    for page in report.get("pages", []):
        for h in page["text_hits"]:
            tag = "kern-split" if h["kern_split"] else "plain"
            print(f"TEXT p{page['page']} [{tag}] ...{h['context']}...")
        for h in page["annot_hits"]:
            print(f"LINK p{page['page']} {h['uri']}   <- {h['target']!r}")
        for f in page["fonts"]:
            cov = f.get("can_spell_replacement")
            if cov and cov["ok"] is False:
                print(f"FONT p{page['page']} {f['base']} CANNOT spell replacement; "
                      f"missing {cov['missing']} (via {cov['via']})")
    if report["engine"].startswith("stdlib"):
        n = len(report["matches"])
        print(f"{n} raw/stream match(es) (kern-tolerant); install pikepdf for full detail")
        for m in report["matches"][:20]:
            print(f"  [{m['where']}] ...{m['context']}...")
    if not report.get("pages") and not report.get("metadata_hits") and not report["matches"]:
        print("no occurrences found")


if __name__ == "__main__":
    main()
