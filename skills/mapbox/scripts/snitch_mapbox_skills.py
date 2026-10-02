#!/usr/bin/env python3
"""Run skill-snitch over the official Mapbox agent skills, and over ours.

WHAT
    Measures each skill in a mapbox-agent-skills checkout -- structure, scripts, network
    destinations, token handling, advice-strength language -- merges the hand-written judgments in
    skill-snitches/findings.yml, and writes one report per skill plus a machine-readable roll-up.

WHY A SCRIPT AT ALL
    Because the alternative is twenty prose reports nobody can re-derive. Everything here is
    measurement: it runs against a commit hash and produces the same numbers tomorrow. The opinions
    live in findings.yml with a name and a date on them. That line is what makes a report worth
    forwarding to the people who wrote the skills -- they can re-run the half that is facts.

    This is skill-snitch's own rule made mechanical: grep finds, LLM understands. The script is the
    finding half. It deliberately cannot conclude anything: no tier is computed, and a skill missing
    from findings.yml is reported as UNJUDGED rather than assumed clean.

USAGE
    python3 scripts/snitch_mapbox_skills.py scan          # write skill-snitches/<skill>/ reports
    python3 scripts/snitch_mapbox_skills.py self          # write ../skill-snitch-report.md (ours)
    python3 scripts/snitch_mapbox_skills.py table         # roll-up to stdout, write nothing
    python3 scripts/snitch_mapbox_skills.py scan --check  # measure and diff, change nothing

    MAPBOX_SKILLS=/path/to/mapbox-agent-skills   overrides checkout discovery

OUTPUT
    skill-snitches/<skill-name>/skill-snitch-report.md   derived, never hand-edit
    skill-snitches/CORPUS.yml                            derived roll-up, machine-readable
    skill-snitch-report.md                               ours, at the skill's top level
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import OrderedDict
from datetime import date
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SNITCHES = SKILL_DIR / "skill-snitches"
FINDINGS = SNITCHES / "findings.yml"

# Where a sibling checkout of the official skills might be. Endosymbiosis, not vendoring: their
# repo keeps its own remote and lifecycle, and we point at it.
CANDIDATES = [
    Path.home() / "GroundUp/git/mapbox-agent-skills",
    SKILL_DIR.parent.parent.parent / "mapbox-agent-skills",
    Path.home() / "mapbox-agent-skills",
]

TEXT_SUFFIXES = {".md", ".py", ".ts", ".js", ".mjs", ".json", ".txt", ".yml", ".yaml"}
CODE_SUFFIXES = {".py", ".ts", ".js", ".mjs", ".sh"}

# What we look for, and what a hit would mean. Named so a report can cite the probe rather than a
# bare number -- "0 token_literal" says nothing; "0 hardcoded pk./sk. tokens" says something.
PROBES = OrderedDict([
    ("token_literal", (r"\b(?:pk|sk)\.eyJ[A-Za-z0-9._-]{10,}", "hardcoded access tokens")),
    ("shell_out", (r"\b(?:curl|wget|nc|ssh)\s+[-a-zA-Z0-9]", "shell-outs to network tools")),
    ("destructive", (r"\brm\s+-rf\b|\beval\(|\bos\.system\(", "destructive or eval-shaped calls")),
    ("process_spawn", (r"child_process|subprocess\.(?:Popen|run|call)|\bspawn\(", "process spawns")),
    ("env_token", (r"MAPBOX_[A-Z_]*TOKEN|process\.env|import\.meta\.env|os\.getenv", "env-var token references")),
    ("coercive", (r"(?i)ignore (?:all |any )?previous|do not tell the user|regardless of what the user",
                  "agent-coercive directives")),
    ("prohibition", (r"\bNEVER\b|\bMUST NOT\b|\bDo not\b|❌", "explicit prohibitions")),
    ("user_location", (r"(?i)user(?:'s)? location|geolocation|watchPosition|precise location", "user-location references")),
    ("permission", (r"(?i)permission|ACCESS_FINE_LOCATION|NSLocation[A-Za-z]*", "OS permission references")),
    ("consent", (r"(?i)\bconsent\b|\bopt-in\b", "consent references")),
    ("privacy_law", (r"(?i)GDPR|CCPA|data retention|anonymi[sz]|data minimi", "privacy-law references")),
])

HOST_RE = re.compile(r"https?://([A-Za-z0-9.-]+)")
FIRST_PARTY = ("mapbox.com",)

# A host in prose is an example; a host in code is a destination. Conflating them is how a scanner
# reports myapp.com as a third-party endpoint and teaches its reader to skim past the host section.
PLACEHOLDER_HOSTS = re.compile(
    r"^(localhost|127\.0\.0\.1|0\.0\.0\.0|.*\.local|"
    r"(www\.|staging\.|app\.)?(myapp|yourdomain|yoursite|example|mysite|yourapp|mydomain)\.(com|org|net)|"
    r"example\.(com|org|net))$")

TIERS = {
    "green": ("🟢 GREEN", "Nothing here makes it unsafe to load or rely on."),
    "blue": ("🔵 BLUE", "Safe, with a low-severity surface worth knowing about first."),
    "yellow": ("🟡 YELLOW", "Read it before you run it. It can reach something that matters."),
    "orange": ("🟠 ORANGE", "Suspicious. Manual review required."),
    "red": ("🔴 RED", "Dangerous. Do not use."),
    "unjudged": ("⚪ UNJUDGED", "Measured but not yet read by a person."),
}

SEVERITY_ORDER = ["critical", "high", "medium", "low", "info"]

# Only safety-class findings move a tier. See the tier_basis block in findings.yml for why: applied
# mechanically to a corpus that is 99% prose, the original ladder grades documents on whether they
# can execute, which they cannot, and would file a wrong-advice finding as "review before use".
TIER_FOR_WORST_SAFETY = {None: "green", "info": "green", "low": "blue",
                         "medium": "yellow", "high": "orange", "critical": "red"}


def expected_tier(findings):
    """Recompute a tier from safety-class findings, so a stated rule stays a checkable one."""
    safety = [f for f in findings or [] if f.get("class") == "safety"]
    if not safety:
        return "green"
    worst = min((f.get("severity", "info") for f in safety), key=SEVERITY_ORDER.index)
    return TIER_FOR_WORST_SAFETY[worst]


def check_tier(key, judged):
    """Warn when findings.yml disagrees with its own rule. Returns a note for the report, or None."""
    if not judged or "tier" not in judged:
        return None
    want = expected_tier(judged.get("findings"))
    got = judged["tier"]
    if want == got:
        return None
    print(f"  ! {key}: findings.yml says {got}, the rule computes {want}", file=sys.stderr)
    return f"Tier recorded as {got.upper()}; the rule in findings.yml computes {want.upper()}."


def load_yaml(path):
    """Read YAML without importing a dependency the skill does not otherwise need."""
    try:
        import yaml
    except ImportError:
        sys.exit("needs PyYAML: pip3 install pyyaml")
    with open(path) as f:
        return yaml.safe_load(f)


def find_upstream():
    env = os.environ.get("MAPBOX_SKILLS")
    if env:
        p = Path(env).expanduser()
        if (p / "skills").is_dir():
            return p, "MAPBOX_SKILLS"
        sys.exit(f"MAPBOX_SKILLS={p} has no skills/ directory")
    for p in CANDIDATES:
        if (p / "skills").is_dir():
            return p, "sibling checkout"
    sys.exit(
        "No mapbox-agent-skills checkout found. Clone it beside this repo:\n"
        "  git clone https://github.com/mapbox/mapbox-agent-skills ~/GroundUp/git/mapbox-agent-skills\n"
        "or set MAPBOX_SKILLS=/path/to/it"
    )


def git_commit(repo):
    try:
        out = subprocess.run(["git", "-C", str(repo), "log", "-1", "--format=%h %ad", "--date=short"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def frontmatter(md):
    """Return (name, description) from YAML frontmatter, flattening wrapped descriptions."""
    if not md.is_file():
        return None, None
    text = md.read_text(errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    name = desc = None
    for key, dest in (("name", "name"), ("description", "desc")):
        mm = re.search(rf"^{key}:\s*(.+?)(?=\n[a-z_-]+:|\Z)", m.group(1), re.S | re.M)
        if mm:
            val = " ".join(mm.group(1).split())
            if dest == "name":
                name = val
            else:
                desc = val
    return name, desc


# Scanning our own skill means scanning a directory that contains this scanner's own output. Left
# alone it counts twenty generated reports as source files and reads their probe tables as hits --
# the tool finding itself and filing it as evidence.
SELF_EXCLUDE = {"skill-snitches", "__pycache__", "node_modules"}

# A file that DEFINES the patterns will match them. skill-snitch's own ignore.yml carries this
# exact entry for cursor_mirror.py. Excluded from pattern probing, still counted as shipped code,
# and the exclusion is printed in the report rather than applied quietly -- an audit that hides its
# own exemptions is worse than one that has none.
PROBE_EXCLUDE = {"snitch_mapbox_skills.py"}


def measure(skill_path, exclude=SELF_EXCLUDE):
    """Everything about a skill that a re-run reproduces exactly."""
    files = sorted(p for p in skill_path.rglob("*")
                   if p.is_file() and not (set(p.relative_to(skill_path).parts) & exclude))
    scannable = [p for p in files if p.suffix in TEXT_SUFFIXES and not p.name.endswith("-lock.json")]
    probed = [p for p in scannable if p.name not in PROBE_EXCLUDE]
    exempt = [p.name for p in scannable if p.name in PROBE_EXCLUDE]
    blob = "\n".join(p.read_text(errors="replace") for p in probed)

    code = [p for p in files if p.suffix in CODE_SUFFIXES]
    code_lines = sum(len(p.read_text(errors="replace").splitlines()) for p in code)

    skill_md = skill_path / "SKILL.md"
    agents_md = skill_path / "AGENTS.md"
    refs = sorted(p.name for p in (skill_path / "references").glob("*.md")) \
        if (skill_path / "references").is_dir() else []

    evals = 0
    eval_file = skill_path / "evals" / "evals.json"
    if eval_file.is_file():
        try:
            data = json.loads(eval_file.read_text())
            items = data.get("evals", data) if isinstance(data, dict) else data
            evals = len(items) if isinstance(items, (list, dict)) else 0
        except Exception:
            evals = -1

    code_blob = "\n".join(p.read_text(errors="replace") for p in code if not p.name.endswith("-lock.json"))
    code_hosts = sorted({h.lower().rstrip(".") for h in HOST_RE.findall(code_blob)})
    doc_hosts = sorted({h.lower().rstrip(".") for h in HOST_RE.findall(blob)} - set(code_hosts))
    reached = [h for h in code_hosts
               if not any(fp in h for fp in FIRST_PARTY) and not PLACEHOLDER_HOSTS.match(h)]
    name, desc = frontmatter(skill_md)

    return {
        "name": name or skill_path.name,
        "description": desc or "",
        "files": len(files),
        "skill_md_lines": len(skill_md.read_text(errors="replace").splitlines()) if skill_md.is_file() else 0,
        "agents_md_lines": len(agents_md.read_text(errors="replace").splitlines()) if agents_md.is_file() else 0,
        "references": refs,
        "evals": evals,
        "code_files": [str(p.relative_to(skill_path)) for p in code],
        "code_lines": code_lines,
        "code_hosts": code_hosts,
        "doc_hosts": doc_hosts,
        "third_party_hosts": reached,
        "probes": {k: len(re.findall(rx, blob)) for k, (rx, _) in PROBES.items()},
        "broken_links": broken_links(skill_path, exclude),
        "probe_exempt": exempt,
    }


def broken_links(skill_path, exclude=frozenset()):
    """Markdown links to files that do not exist, resolved relative to the linking file."""
    bad = []
    for md in skill_path.rglob("*.md"):
        if set(md.relative_to(skill_path).parts) & set(exclude):
            continue
        for target in re.findall(r"\]\(([^)#:]+\.md)\)", md.read_text(errors="replace")):
            if not (md.parent / target).resolve().is_file():
                bad.append(f"{md.relative_to(skill_path)} -> {target}")
    return sorted(bad)


def first_sentence(text, limit=210):
    """One readable sentence from a wrapped YAML block, rather than whatever the first newline cut."""
    flat = " ".join((text or "").split())
    m = re.match(r"(.+?[.!?])(?:\s|$)", flat)
    out = m.group(1) if m else flat
    return out if len(out) <= limit else out[:limit].rsplit(" ", 1)[0] + "…"


def fmt_findings(findings):
    if not findings:
        return "Nothing specific to this skill. The corpus-wide observations below still apply.\n"
    out = []
    for f in sorted(findings, key=lambda x: SEVERITY_ORDER.index(x.get("severity", "info"))):
        cls = f.get("class", "unclassified")
        tiered = " · moves the tier" if cls == "safety" else " · recorded, does not move the tier"
        out.append(f"### {f.get('severity', 'info').upper()} — {f.get('id', 'unnamed')}\n")
        out.append(f"*{cls}{tiered}*\n")
        out.append(f"**Where** `{f.get('where', 'unspecified')}`\n")
        out.append(f"**What** {f.get('what', '').strip()}\n")
        if f.get("why"):
            out.append(f"**Why it matters** {f['why'].strip()}\n")
        for key, label in (("mitigations", "Mitigations"), ("fix", "Fix")):
            v = f.get(key)
            if isinstance(v, list):
                out.append(f"**{label}**\n\n" + "\n".join(f"- {x}" for x in v) + "\n")
            elif v:
                out.append(f"**{label}** {v.strip()}\n")
    return "\n".join(out)


def render(key, m, judged, meta, corpus, ours=False, disagreement=None):
    tier_key = (judged or {}).get("tier", "unjudged")
    badge, meaning = TIERS.get(tier_key, TIERS["unjudged"])
    probes = m["probes"]

    head = [
        f"# {key} — skill-snitch report\n",
        f"**Trust** {badge} · **Type** {'moollm' if ours else corpus.get('type', 'anthropic')} · "
        f"**Executable files** {len(m['code_files'])} · **Evals** {m['evals'] if m['evals'] >= 0 else 'unparseable'} · "
        f"**License** {meta.get('license', 'unknown')}\n",
        f"**{'Skill' if ours else 'Upstream'}** `{meta['upstream']}` @ `{meta['commit']}` · "
        f"**Scanned** {meta['scanned']} by {meta.get('auditor', 'unattributed')}\n"
        + (f"**Audits** `{meta['audits']}` — the twenty skills this one routes to\n" if meta.get("audits") else ""),
        "> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against\n"
        "> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.\n",
    ]

    body = []
    if judged and judged.get("is"):
        body.append(f"## What it is\n\n{judged['is'].strip()}\n")
    elif m["description"]:
        body.append(f"## What it is\n\n{m['description']}\n")
    if judged and judged.get("notable"):
        body.append(f"## Notable\n\n{judged['notable'].strip()}\n")

    body.append("## Measured surface\n")
    body.append(
        f"| Measure | Value |\n|---|---|\n"
        f"| Files | {m['files']} |\n"
        f"| SKILL.md | {m['skill_md_lines']} lines |\n"
        f"| AGENTS.md | {m['agents_md_lines'] or 'absent'} |\n"
        f"| References | {len(m['references'])}{' — ' + ', '.join(m['references']) if m['references'] else ''} |\n"
        f"| Executable code | {len(m['code_files'])} files, {m['code_lines']} lines |\n"
        f"| Broken internal links | {len(m['broken_links']) or 'none'} |\n"
    )

    body.append("### What the patterns found\n")
    if m["probe_exempt"]:
        body.append(f"Excluded from pattern probing because it defines the patterns: "
                    f"{', '.join(f'`{x}`' for x in m['probe_exempt'])}. Still counted as shipped code above.\n")
    rows = ["| Probe | Hits | Reading |", "|---|---|---|"]
    for pk, (_, label) in PROBES.items():
        n = probes[pk]
        if pk in ("token_literal", "shell_out", "destructive", "coercive"):
            reading = "clean" if n == 0 else "REVIEW"
        elif n == 0:
            reading = "absent"
        else:
            reading = "present, in context"
        rows.append(f"| {label} | {n} | {reading} |")
    body.append("\n".join(rows) + "\n")

    body.append("### Network destinations\n")
    if m["code_hosts"]:
        body.append("Hosts appearing in executable code — the ones this skill can actually reach:\n")
        body.append("\n".join(f"- `{h}`" for h in m["code_hosts"]) + "\n")
        tp = m["third_party_hosts"]
        body.append(f"\n{'All first-party Mapbox.' if not tp else 'Not first-party: ' + ', '.join(f'`{h}`' for h in tp)}\n")
    else:
        body.append("None. This skill ships no executable code, so it reaches nothing.\n")
    if m["doc_hosts"]:
        shown = [h for h in m["doc_hosts"] if not PLACEHOLDER_HOSTS.match(h)]
        placeholders = len(m["doc_hosts"]) - len(shown)
        body.append(
            f"\nHosts named in prose and examples ({len(m['doc_hosts'])} distinct"
            f"{f', {placeholders} of them placeholders like myapp.com' if placeholders else ''}): "
            + (", ".join(f"`{h}`" for h in shown[:12]) if shown else "all placeholders")
            + ". Documentation text, not destinations.\n")

    if m["broken_links"]:
        body.append("### Broken internal links\n\n" + "\n".join(f"- `{b}`" for b in m["broken_links"]) + "\n")

    body.append("## Findings\n")
    body.append(fmt_findings((judged or {}).get("findings") or []))

    if not ours:
        body.append("## Corpus-wide observations that also apply\n")
        for o in corpus.get("observations", []):
            body.append(f"- **{o['severity'].upper()} · {o['id']}** — {first_sentence(o['what'])}")
        body.append(f"\nFull text and reasoning: [`../README.md`](../README.md).\n")

    body.append("## Verdict\n")
    body.append(f"{badge} — {meaning}\n")
    fs = (judged or {}).get("findings") or []
    if fs:
        safety = [f for f in fs if f.get("class") == "safety"]
        body.append(
            f"\n{len(fs)} finding{'s' if len(fs) != 1 else ''} recorded above, "
            f"{'of which ' + str(len(safety)) + ' safety-class' if safety else 'none of them safety-class'}. "
            "The badge answers whether this is safe to load, not whether anything was found — "
            "see `tier_basis` in `../findings.yml`.\n")
    if disagreement:
        body.append(f"\n**Rule check** {disagreement}\n")
    if not judged:
        body.append("\nNo entry in `findings.yml`. Measured only; nobody has read it yet.\n")

    return "\n".join(head) + "\n" + "\n".join(body)


def do_scan(args, cfg, upstream, check=False):
    meta = dict(cfg["audited"])
    meta["commit"] = git_commit(upstream).split()[0] if args.live_commit else meta["commit"]
    meta["scanned"] = str(date.today()) if args.live_commit else meta["scanned"]
    corpus = cfg.get("corpus", {})
    judged_all = cfg.get("skills", {})

    skills = sorted(p for p in (upstream / "skills").iterdir() if (p / "SKILL.md").is_file())
    roll = OrderedDict()
    wrote = 0

    for sp in skills:
        key = sp.name
        m = measure(sp)
        judged = judged_all.get(key)
        report = render(key, m, judged, meta, corpus, disagreement=check_tier(key, judged))

        out = SNITCHES / key / "skill-snitch-report.md"
        if not check:
            out.parent.mkdir(parents=True, exist_ok=True)
            previous = out.read_text() if out.is_file() else None
            out.write_text(report)
            wrote += 1
            status = "unchanged" if previous == report else ("updated" if previous else "new")
        else:
            status = "would write"

        tier = (judged or {}).get("tier", "unjudged")
        roll[key] = {
            "tier": tier,
            "evals": m["evals"],
            "code_files": len(m["code_files"]),
            "code_lines": m["code_lines"],
            "findings": [{"id": f["id"], "severity": f["severity"]} for f in (judged or {}).get("findings") or []],
            "third_party_hosts": m["third_party_hosts"],
            "report": f"{key}/skill-snitch-report.md",
        }
        flags = sum(m["probes"][k] for k in ("token_literal", "shell_out", "destructive", "coercive"))
        print(f"  {TIERS[tier][0]:<12} {key:<36} evals={m['evals']:<3} code={len(m['code_files'])} "
              f"flags={flags}  {status}")

    if not check:
        write_corpus(roll, meta, corpus, cfg)
    print(f"\n{wrote} report{'s' if wrote != 1 else ''} "
          f"{'would be written' if check else 'written'} under {SNITCHES.relative_to(SKILL_DIR.parent.parent)}")
    unjudged = [k for k, v in roll.items() if v["tier"] == "unjudged"]
    if unjudged:
        print(f"UNJUDGED (measured, unread): {', '.join(unjudged)}")
    return roll


def write_corpus(roll, meta, corpus, cfg):
    """A machine-readable roll-up, matching skill-snitch's CATALOG.yml convention."""
    tiers = {}
    for v in roll.values():
        tiers[v["tier"]] = tiers.get(v["tier"], 0) + 1
    sev = {}
    for v in roll.values():
        for f in v["findings"]:
            sev[f["severity"]] = sev.get(f["severity"], 0) + 1

    lines = [
        "# CORPUS.yml — derived roll-up. Generated by scripts/snitch_mapbox_skills.py; do not edit.",
        "# Judgments live in findings.yml. Per-skill detail lives in <skill>/skill-snitch-report.md.",
        "",
        "audited:",
        f"  upstream: {meta['upstream']}",
        f"  commit: {meta['commit']}",
        f"  scanned: {meta['scanned']}",
        f"  skills: {len(roll)}",
        f"  license: {meta.get('license', 'unknown')}",
        "",
        "totals:",
        "  tiers:",
    ]
    for t in ["green", "blue", "yellow", "orange", "red", "unjudged"]:
        if tiers.get(t):
            lines.append(f"    {t}: {tiers[t]}")
    lines.append("  findings_by_severity:")
    for s in SEVERITY_ORDER:
        if sev.get(s):
            lines.append(f"    {s}: {sev[s]}")
    lines += [
        f"  evals: {sum(v['evals'] for v in roll.values() if v['evals'] > 0)}",
        f"  skills_shipping_code: {sum(1 for v in roll.values() if v['code_files'])}",
        f"  third_party_hosts: {sorted({h for v in roll.values() for h in v['third_party_hosts']}) or '[]'}",
        "",
        "# Corpus-wide observations, recorded once. Reasoning in README.md.",
        "observations:",
    ]
    for o in corpus.get("observations", []):
        lines.append(f"  - id: {o['id']}")
        lines.append(f"    severity: {o['severity']}")
        lines.append(f"    where: {json.dumps(str(o.get('where', '')))}")
    lines += ["", "skills:"]
    for k, v in roll.items():
        lines.append(f"  {k}:")
        lines.append(f"    tier: {v['tier']}")
        lines.append(f"    evals: {v['evals']}")
        if v["code_files"]:
            lines.append(f"    code: {v['code_files']} files, {v['code_lines']} lines")
        if v["findings"]:
            lines.append("    findings:")
            for f in v["findings"]:
                lines.append(f"      - {f['id']} ({f['severity']})")
        lines.append(f"    report: {v['report']}")

    (SNITCHES / "CORPUS.yml").write_text("\n".join(lines) + "\n")
    print(f"\n  CORPUS.yml: {tiers} · findings {sev}")


def do_self(cfg):
    """Same scanner, pointed at ourselves. A tool that only finds other people's problems is a press release."""
    judged = cfg.get("self", {})
    ours = git_commit(SKILL_DIR).split()
    meta = dict(cfg["audited"])
    meta["upstream"] = "SimHacker/moollm — skills/mapbox"
    meta["commit"] = ours[0] if ours and ours[0] != "unknown" else "working tree"
    meta["audits"] = f"{cfg['audited']['upstream']} @ {cfg['audited']['commit']}"
    m = measure(SKILL_DIR)
    report = render(judged.get("name", "moollm/skills/mapbox"), m, judged, meta, cfg.get("corpus", {}),
                    ours=True, disagreement=check_tier("self", judged))
    out = SKILL_DIR / "skill-snitch-report.md"
    out.write_text(report)
    flags = sum(m["probes"][k] for k in ("token_literal", "shell_out", "destructive", "coercive"))
    print(f"  {TIERS[judged.get('tier', 'unjudged')][0]} {judged.get('name')}  "
          f"code={len(m['code_files'])} lines={m['code_lines']} flags={flags}")
    print(f"  wrote {out.relative_to(SKILL_DIR)}")
    for f in judged.get("findings", []):
        print(f"    {f['severity']:<6} {f['id']}")


def do_table(cfg, upstream):
    meta = cfg["audited"]
    print(f"{meta['upstream']} @ {meta['commit']}  ({upstream})\n")
    print(f"  {'TIER':<12} {'SKILL':<36} {'EVALS':>5} {'CODE':>5} {'FINDINGS'}")
    for sp in sorted(p for p in (upstream / "skills").iterdir() if (p / "SKILL.md").is_file()):
        m = measure(sp)
        j = cfg.get("skills", {}).get(sp.name) or {}
        fs = ", ".join(f"{f['id']}({f['severity']})" for f in j.get("findings") or []) or "-"
        print(f"  {TIERS[j.get('tier', 'unjudged')][0]:<12} {sp.name:<36} {m['evals']:>5} "
              f"{len(m['code_files']):>5} {fs}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("command", choices=["scan", "self", "table"])
    ap.add_argument("--check", action="store_true", help="measure and report, write nothing")
    ap.add_argument("--live-commit", action="store_true",
                    help="stamp reports with the checkout's current commit and today's date "
                         "instead of the commit findings.yml was written against")
    args = ap.parse_args()

    if not FINDINGS.is_file():
        sys.exit(f"No findings.yml at {FINDINGS} — the judgments have to exist before reports can cite them.")
    cfg = load_yaml(FINDINGS)

    if args.command == "self":
        return do_self(cfg)

    upstream, how = find_upstream()
    print(f"upstream: {upstream}  ({how}, {git_commit(upstream)})")
    print(f"findings: {FINDINGS.relative_to(SKILL_DIR)}\n")
    if args.command == "table":
        return do_table(cfg, upstream)
    do_scan(args, cfg, upstream, check=args.check)


if __name__ == "__main__":
    main()
