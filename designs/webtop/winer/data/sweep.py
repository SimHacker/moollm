#!/usr/bin/env python3
"""Sweep HN Algolia for DonHopkins comments about Dave Winer / UserLand / outliners."""
import json, re, time, urllib.parse, urllib.request, html, sys

AUTHOR = "DonHopkins"
TERMS = [
    "Dave Winer", "Winer", "UserLand", "Scripting News", "Frontier",
    "Radio UserLand", "Aretha", "outliner", "outlining", "OPML",
    "XML-RPC", "Living Videotext", "ThinkTank", "MORE 3.1",
    "DaveNet", "instant outlining", "scripting.com", "Manila",
]
# Local confirmation regex per term (case-insensitive, word-ish boundaries).
CONFIRM = {t: re.compile(r"\b" + re.escape(t).replace(r"\ ", r"[\s\-]+") + r"\b", re.I) for t in TERMS}
CONFIRM["Frontier"] = re.compile(r"\bfrontier\b", re.I)
CONFIRM["Aretha"] = re.compile(r"\baretha\b", re.I)

def fetch(term, page=0):
    q = urllib.parse.quote(term)
    url = (f"https://hn.algolia.com/api/v1/search_by_date?"
           f"tags=comment,author_{AUTHOR}&query={q}"
           f"&typoTolerance=false&hitsPerPage=1000&page={page}")
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

def strip(t):
    t = re.sub(r"<[^>]+>", " ", t or "")
    return re.sub(r"\s+", " ", html.unescape(t)).strip()

hits = {}
for term in TERMS:
    page, total = 0, None
    while True:
        d = fetch(term, page)
        if total is None:
            total = d.get("nbHits", 0)
            print(f"{term:20s} raw={total}", file=sys.stderr)
        for h in d.get("hits", []):
            txt = strip(h.get("comment_text"))
            if not CONFIRM[term].search(txt):
                continue
            oid = h["objectID"]
            rec = hits.setdefault(oid, {
                "id": oid,
                "date": (h.get("created_at") or "")[:10],
                "story": h.get("story_title") or "",
                "story_id": h.get("story_id"),
                "parent_id": h.get("parent_id"),
                "text": txt,
                "terms": set(),
            })
            rec["terms"].add(term)
        page += 1
        if page >= d.get("nbPages", 1) or page > 10:
            break
        time.sleep(0.2)
    time.sleep(0.2)

out = sorted(hits.values(), key=lambda r: r["date"])
for r in out:
    r["terms"] = sorted(r["terms"])
json.dump(out, open("hits.json", "w"), indent=1)
print(f"\nCONFIRMED UNIQUE COMMENTS: {len(out)}", file=sys.stderr)
