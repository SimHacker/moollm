#!/usr/bin/env python3
"""content-rescue: download every asset in a manifest into <out>/, in order,
naming them by article position + caption slug, then emit INDEX.md (a captioned,
ordered gallery = an illustrated transcript) and map.tsv.

Re-runnable: skips assets already present. Works because the page may be
bot-walled but the asset CDN usually is not — so we hit the CDN per id.

Manifest format (pipe-separated, one per line):  <order_index>|<asset_id_or_url>|<caption>
  - asset_id like Medium's "1*AbC.png" / "0*XyZ" -> fetched via URL_TEMPLATE
  - OR a full http(s) URL (used as-is)

Usage:
  python3 fetch_images.py [manifest.psv] [out_dir] \\
      [--url-template 'https://miro.medium.com/v2/resize:fit:2000/{id}'] \\
      [--source-url 'https://...original article...']
"""
import os, re, sys, subprocess, argparse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
EXT_BY_MIME = {"image/png": "png", "image/jpeg": "jpeg", "image/gif": "gif", "image/webp": "webp"}
DEFAULT_TMPL = "https://miro.medium.com/v2/resize:fit:2000/{id}"  # Medium image CDN

def slugify(s, fallback):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").strip().lower()).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return (s[:60].rstrip("-")) or fallback

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", nargs="?", default="manifest.psv")
    ap.add_argument("out", nargs="?", default="images")
    ap.add_argument("--url-template", default=DEFAULT_TMPL,
                    help="{id} is substituted; ignored when a manifest row is a full URL.")
    ap.add_argument("--source-url", default="", help="original page URL, for INDEX.md provenance")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    rows = []
    with open(a.manifest, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            idx, iid, cap = (line.split("|", 2) + ["", ""])[:3]
            rows.append((idx.strip(), iid.strip(), cap))

    entries = []
    for seq, (idx, iid, cap) in enumerate(rows, start=1):
        base = "%03d-%s" % (seq, slugify(cap, slugify(iid.replace("*", "-"), "asset")))
        ext = ""
        m = re.search(r"\.(png|jpe?g|gif|webp)(?:$|\?)", iid, re.I)
        if m:
            ext = m.group(1).lower().replace("jpg", "jpeg")
        existing = [fn for fn in os.listdir(a.out) if fn.startswith(base + ".")]
        if existing:
            entries.append((seq, idx, iid, cap, existing[0])); continue
        url = iid if iid.startswith("http") else a.url_template.format(id=iid)
        tmp = os.path.join(a.out, base + ".tmp")
        r = subprocess.run(["curl", "-sSL", "-A", UA, url, "-o", tmp])
        if r.returncode != 0 or not os.path.exists(tmp) or os.path.getsize(tmp) < 100:
            print("FAIL", iid, file=sys.stderr)
            if os.path.exists(tmp): os.remove(tmp)
            continue
        if not ext:
            mime = subprocess.run(["file", "--mime-type", "-b", tmp],
                                  capture_output=True, text=True).stdout.strip()
            ext = EXT_BY_MIME.get(mime, "bin")
        fn = base + "." + ext
        os.replace(tmp, os.path.join(a.out, fn))
        entries.append((seq, idx, iid, cap, fn)); print("OK", fn)

    with open(os.path.join(a.out, "map.tsv"), "w", encoding="utf-8") as f:
        f.write("seq\tsource_index\tasset_id\tfile\tcaption\n")
        for seq, idx, iid, cap, fn in entries:
            f.write("%s\t%s\t%s\t%s\t%s\n" % (seq, idx, iid, fn, cap))

    with open(os.path.join(a.out, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("# Rescued gallery (article order)\n\n")
        if a.source_url:
            f.write("Source: <%s>\n\n" % a.source_url)
        f.write("Local copies of every asset, in order. (Some may be third-party — credit as captioned.)\n\n---\n\n")
        for seq, idx, iid, cap, fn in entries:
            f.write("**%d.** %s\n\n![%s](%s)\n\n" % (seq, cap or "(no caption)", (cap or "").replace("]", ")"), fn))
        f.write("---\n\n*%d assets.*\n" % len(entries))
    print("TOTAL", len(entries))

if __name__ == "__main__":
    main()
