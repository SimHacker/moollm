#!/usr/bin/env python3
"""Route Mapbox questions to the official Mapbox Agent Skills, and check local reality.

This skill owns no Mapbox knowledge it can borrow. Mapbox publishes twenty skills
(mapbox/mapbox-agent-skills, MIT); this script finds that checkout wherever it lives,
indexes it, and says which skills to load for a given question. What it *does* own is
the part Mapbox cannot know: where this operator's tokens live, and the restriction
behaviour measured against the live API rather than read off a docs page.

Sister-script order: imports, globals, CLI definition, implementation.
Read the top for the interface; the bottom is detail.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Where the official checkout might be, best candidate first. A miss is not an error:
# every command degrades to pointing at the URL (robust-first).
UPSTREAM_REPO = "https://github.com/mapbox/mapbox-agent-skills"
UPSTREAM_ENV = "MAPBOX_AGENT_SKILLS"
UPSTREAM_CANDIDATES = [
    "~/GroundUp/git/mapbox-agent-skills",
    "~/git/mapbox-agent-skills",
    "~/src/mapbox-agent-skills",
    "./mapbox-agent-skills",
    "../mapbox-agent-skills",
    "../../mapbox-agent-skills",
    "~/.agents/skills",
    "~/.claude/skills",
]

# Question shape to official skill. Deliberately coarse: the point is to load two or
# three skills instead of all twenty, not to be clever.
ROUTES = {
    "token": ["mapbox-token-security"],
    "secret": ["mapbox-token-security"],
    "scope": ["mapbox-token-security"],
    "403": ["mapbox-token-security"],
    "restrict": ["mapbox-token-security"],
    "rotate": ["mapbox-token-security"],
    "style": ["mapbox-style-patterns", "mapbox-style-quality"],
    "color": ["mapbox-cartography", "mapbox-style-quality"],
    "design": ["mapbox-cartography"],
    "label": ["mapbox-cartography"],
    "legible": ["mapbox-cartography"],
    "slow": ["mapbox-web-performance-patterns"],
    "performance": ["mapbox-web-performance-patterns"],
    "fps": ["mapbox-web-performance-patterns"],
    "svelte": ["mapbox-web-integration-patterns"],
    "react": ["mapbox-web-integration-patterns"],
    "vue": ["mapbox-web-integration-patterns"],
    "framework": ["mapbox-web-integration-patterns"],
    "ios": ["mapbox-ios-patterns"],
    "swift": ["mapbox-ios-patterns"],
    "android": ["mapbox-android-patterns"],
    "kotlin": ["mapbox-android-patterns"],
    "flutter": ["mapbox-flutter-patterns"],
    "geocode": ["mapbox-search-patterns", "mapbox-search-integration"],
    "address": ["mapbox-search-patterns"],
    "search": ["mapbox-search-patterns", "mapbox-search-integration"],
    "poi": ["mapbox-search-patterns"],
    "autocomplete": ["mapbox-search-integration"],
    "route": ["mapbox-navigation-patterns"],
    "direction": ["mapbox-navigation-patterns"],
    "navigation": ["mapbox-navigation-patterns"],
    "isochrone": ["mapbox-geospatial-operations"],
    "distance": ["mapbox-geospatial-operations"],
    "buffer": ["mapbox-geospatial-operations"],
    "turf": ["mapbox-geospatial-operations"],
    "within": ["mapbox-geospatial-operations"],
    "geofence": ["mapbox-geospatial-operations"],
    "cluster": ["mapbox-data-visualization-patterns"],
    "heatmap": ["mapbox-data-visualization-patterns"],
    "choropleth": ["mapbox-data-visualization-patterns"],
    "locator": ["mapbox-store-locator-patterns"],
    "store": ["mapbox-store-locator-patterns"],
    "google": ["mapbox-google-maps-migration"],
    "maplibre": ["mapbox-maplibre-migration"],
    "leaflet": ["mapbox-maplibre-migration"],
    "mcp": ["mapbox-mcp-runtime-patterns", "mapbox-mcp-devkit-patterns"],
    "agent": ["mapbox-mcp-runtime-patterns", "mapbox-location-grounding"],
    "ground": ["mapbox-location-grounding"],
    "cite": ["mapbox-location-grounding"],
    "hallucinat": ["mapbox-location-grounding"],
}

# Subjects the official twenty simply do not cover. Saying so is more useful than routing
# to a near-miss skill, and it points at the surface that does handle them: the CLI.
UNCOVERED = {
    "tileset": "mapbox tilesets ... (or the separate `tilesets` binary) — MTS recipes, uploads, jobs",
    "tile": "mapbox tilesets ... — no official skill covers tiling",
    "mts": "mapbox tilesets ... — recipe and source management",
    "tippecanoe": "tippecanoe, built separately — GeoJSON to vector tiles, offline",
    "font": "mapbox fonts ... — glyph upload and listing",
    "sprite": "mapbox sprites ... — sprite sheet management",
    "account": "mapbox accounts ... — account and usage queries",
    "billing": "mapbox accounts ... — usage; billing itself is the dashboard, not an API",
    "invoice": "the Mapbox dashboard; not exposed as a skill or CLI command",
    "atlas": "Atlas is a self-hosted product, out of scope for the agent skills",
    "movement": "Movement and Boundaries are licensed data products, not covered by the skills",
}

# Measured against api.mapbox.com on 2026-09-20, not read off a docs page. Every one of
# these is invisible in all 6128 lines of the official skills, which never say "referer"
# or "403" — so this table is the reason this skill exists.
MEASURED = [
    ("A restricted token is dead from a terminal",
     "No Referer means 403. curl, CI, server-side fetch and MCP servers all send none, "
     "so a URL-restricted token cannot be used for any of them. Keep an unrestricted "
     "token for those and never put it in a browser bundle."),
    ("Enforcement is per-endpoint",
     "Tile and data requests (/v4/..., /styles/v1/.../tiles) enforce the restriction. "
     "Style metadata (/styles/v1/<user>/<id>) answered 200 from every origin tried, "
     "so a passing metadata call proves nothing about the restriction."),
    ("Restriction edits take minutes to reach the edge",
     "A saved URL list does not apply at once, and the intermediate state is per-variant: "
     "for several minutes http://localhost:5173 answered 200 while http://localhost:5173/ "
     "answered 403, which reads exactly like a matching bug and is not one. "
     "Re-probe a few minutes after saving before concluding anything."),
    ("An exact port pins you to one dev server",
     "With http://localhost:5173 listed, referer http://localhost:5173/ passes but "
     "http://localhost:4173/ and http://localhost:3000/ are refused, so vite preview and "
     "any second port break. Use the wildcard http://localhost:* as Mapbox's own "
     "token-security skill advises. An apex entry does cover www: with "
     "https://ebike-safari.com listed, www.ebike-safari.com passes too."),
    ("Scopes are editable, the token string is not reissued",
     "Changing public scopes or URL restrictions leaves the pk. string unchanged, so "
     "nothing needs redeploying. Secret scopes are the exception: they produce an sk. "
     "token shown once that must never reach a browser."),
]

# This operator's key locations. The only machine-specific block in the skill.
TOKENS = {
    "prod": {
        "ref": "op://Employee/Mapbox/ebike-safari-token",
        "note": "URL-restricted to ebike-safari.com. Browser-safe. Useless from a shell.",
    },
    "dev": {
        "ref": "op://Employee/Mapbox/token",
        "note": "Unrestricted default. Use for CLI, MCP servers and scripts. Never ship it.",
    },
}
OP_ACCOUNT = "groundupsoftware.1password.com"

# A referer that must pass and one that must fail, for the doctor's sanity check.
PROBE_URL = "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.vector.pbf"


def build_parser():
    p = argparse.ArgumentParser(
        prog="mapbox_router.py",
        description="Route Mapbox questions to official skills; check tokens and tooling.",
        epilog="Upstream: " + UPSTREAM_REPO + " (MIT). This script never vendors it.",
    )
    sub = p.add_subparsers(dest="command", required=True)

    sub.add_parser("where", help="Show where the official checkout was found, or how to get it.")

    lst = sub.add_parser("list", help="List the official skills with their descriptions.")
    lst.add_argument("--json", action="store_true", help="Emit JSON instead of text.")

    rt = sub.add_parser("route", help="Name the skills to load for a question.")
    rt.add_argument("question", nargs="+", help="The question, in plain words.")
    rt.add_argument("--paths", action="store_true", help="Print resolved file paths to read.")

    sub.add_parser("measured", help="Print the measured restriction behaviour.")

    doc = sub.add_parser("doctor", help="Check tooling, then probe token restrictions live.")
    doc.add_argument("--probe", metavar="DOMAIN", default="ebike-safari.com",
                     help="Domain that should pass the restriction check.")
    doc.add_argument("--offline", action="store_true", help="Skip network probes.")
    return p


def resolve_upstream():
    """Return (skills_dir, how) or (None, reason). Never raises."""
    env = os.environ.get(UPSTREAM_ENV)
    candidates = ([env] if env else []) + UPSTREAM_CANDIDATES
    for raw in candidates:
        try:
            base = Path(os.path.expanduser(raw)).resolve()
        except OSError:
            continue
        if not base.is_dir():
            continue
        for sub in (base / "skills", base):
            if sub.is_dir() and any(sub.glob("mapbox-*/SKILL.md")):
                how = f"{UPSTREAM_ENV}={raw}" if raw == env else f"found at {raw}"
                return sub, how
    return None, "no local checkout found"


def read_frontmatter(skill_md):
    """Pull name and description out of the SKILL.md frontmatter. Tolerant by design."""
    name = skill_md.parent.name
    desc = ""
    try:
        text = skill_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return name, desc
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return name, desc
    body = m.group(1)
    d = re.search(r"^description:\s*(.+?)(?=\n[a-zA-Z_-]+:|\Z)", body, re.S | re.M)
    if d:
        desc = " ".join(d.group(1).split())
    n = re.search(r"^name:\s*(\S+)", body, re.M)
    if n:
        name = n.group(1)
    return name, desc


def load_catalog():
    skills_dir, how = resolve_upstream()
    if not skills_dir:
        return [], how
    out = []
    for md in sorted(skills_dir.glob("mapbox-*/SKILL.md")):
        name, desc = read_frontmatter(md)
        out.append({"name": name, "description": desc, "path": str(md)})
    return out, how


def http_status(url, referer=None, timeout=10):
    req = urllib.request.Request(url)
    if referer:
        req.add_header("Referer", referer)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None


def op_read(ref):
    if not shutil.which("op"):
        return None
    try:
        r = subprocess.run(["op", "read", ref, "--account", OP_ACCOUNT],
                           capture_output=True, text=True, timeout=30)
        return r.stdout.strip() or None
    except Exception:
        return None


def cmd_where(_args):
    skills_dir, how = resolve_upstream()
    if skills_dir:
        n = len(list(skills_dir.glob("mapbox-*/SKILL.md")))
        print(f"  official skills: {skills_dir}")
        print(f"  how:             {how}")
        print(f"  count:           {n}")
        print(f"  refresh:         git -C {skills_dir.parent} pull")
    else:
        print(f"  official skills: NOT FOUND ({how})")
        print("  this skill still works, it just cannot quote them. To mount:")
        print(f"    git clone {UPSTREAM_REPO}")
        print(f"  or point at an existing copy: export {UPSTREAM_ENV}=/path/to/repo")
    return 0


def cmd_list(args):
    cat, how = load_catalog()
    if args.json:
        print(json.dumps({"how": how, "skills": cat}, indent=2))
        return 0
    if not cat:
        print(f"  no catalog ({how}) — see: {UPSTREAM_REPO}")
        return 0
    print(f"  {len(cat)} official skills ({how})\n")
    for s in cat:
        print(f"  {s['name']}")
        if s["description"]:
            print(f"      {s['description'][:100]}")
    return 0


def cmd_route(args):
    q = " ".join(args.question).lower()
    hits, why = [], {}
    for key, skills in ROUTES.items():
        if key in q:
            for s in skills:
                if s not in hits:
                    hits.append(s)
                why.setdefault(s, []).append(key)
    cat, how = load_catalog()
    known = {s["name"]: s for s in cat}

    gaps = {k: v for k, v in UNCOVERED.items() if k in q}
    if gaps:
        print(f"  question: {q}\n")
        print("  no official skill covers this. Use the CLI surface instead:\n")
        for key, where in gaps.items():
            print(f"    {key:<12} {where}")
        if not hits:
            return 0
        print()

    if not hits:
        print("  no keyword matched. Load the index and choose by hand:")
        print("    mapbox_router.py list")
        return 0

    print(f"  question: {q}\n  load these, in order:\n")
    for s in hits:
        print(f"  {s}   (matched: {', '.join(why[s])})")
        if s in known:
            if args.paths:
                print(f"      {known[s]['path']}")
            if known[s]["description"]:
                print(f"      {known[s]['description'][:96]}")
        elif cat:
            print("      not in the local checkout — name may have changed upstream")
        else:
            print(f"      no local checkout; read it at {UPSTREAM_REPO}")
    if any(k in q for k in ("token", "403", "restrict", "secret", "scope")):
        print("\n  also read this skill's measured findings, which upstream lacks:")
        print("    mapbox_router.py measured")
    return 0


def cmd_measured(_args):
    print("  Measured against api.mapbox.com, 2026-09-20.")
    print("  Upstream never says 'referer' or '403' in 6128 lines of SKILL.md.\n")
    for title, body in MEASURED:
        print(f"  {title}")
        for line in body.split(". "):
            line = line.strip().rstrip(".")
            if line:
                print(f"      {line}.")
        print()
    return 0


def cmd_doctor(args):
    print("  tooling")
    for tool, why in (("mapbox", "official agent-first CLI"),
                      ("tilesets", "tileset upload CLI"),
                      ("op", "1Password, for token refs"),
                      ("npx", "runs the three MCP servers")):
        path = shutil.which(tool)
        print(f"    {tool:<10} {path or '-- missing (' + why + ')'}")
    if not shutil.which("mapbox"):
        print("    install the CLI: curl -fsSL https://cli.mapbox.com/install.sh | sh")

    skills_dir, how = resolve_upstream()
    print(f"\n  official skills\n    {skills_dir or 'NOT FOUND'}  ({how})")

    print("\n  tokens")
    if not shutil.which("op"):
        print("    op not installed — cannot resolve references")
        return 0
    for role, meta in TOKENS.items():
        tok = op_read(meta["ref"])
        if not tok:
            print(f"    {role:<5} {meta['ref']}  UNRESOLVED")
            continue
        print(f"    {role:<5} {meta['ref']}  ok ({tok[:3]}..., {len(tok)} chars)")
        print(f"          {meta['note']}")
        if args.offline:
            continue
        url = f"{PROBE_URL}?access_token={tok}"
        pass_ref = f"https://{args.probe}/"
        checks = [
            (f"referer {pass_ref}", http_status(url, pass_ref)),
            ("referer http://localhost:5173/ (dev)", http_status(url, "http://localhost:5173/")),
            ("referer http://localhost:4173/ (preview)", http_status(url, "http://localhost:4173/")),
            ("referer https://evil.example.com/", http_status(url, "https://evil.example.com/")),
            ("no referer (cli, ci, server)", http_status(url)),
        ]
        for label, code in checks:
            verdict = "ok" if code == 200 else ("blocked" if code == 403 else "?")
            print(f"          {label:<40} {code} {verdict}")
        restricted = checks[-1][1] == 403
        print(f"          -> {'restricted: browser only' if restricted else 'unrestricted: never ship in a bundle'}")
        if restricted and checks[3][1] == 200:
            print("          -> WARNING restricted token answers an unrelated origin; check the URL list")
        if restricted and checks[1][1] == 200 and checks[2][1] == 403:
            print("          -> pinned to one port: vite preview (4173) is refused. Prefer http://localhost:*")
    return 0


HANDLERS = {
    "where": cmd_where,
    "list": cmd_list,
    "route": cmd_route,
    "measured": cmd_measured,
    "doctor": cmd_doctor,
}


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        return HANDLERS[args.command](args)
    except KeyboardInterrupt:
        return 130
    except Exception as e:
        # Degrade, never crash: a broken probe should still leave the operator oriented.
        print(f"  {type(e).__name__}: {e}", file=sys.stderr)
        print(f"  the official skills are still at {UPSTREAM_REPO}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
