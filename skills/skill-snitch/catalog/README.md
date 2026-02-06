# 🕵️ skill-snitch Catalog

Reviewed skills from the wild. Human-readable (CATALOG.md) and machine-structured (CATALOG.yml) indexes of trust assessments.

The catalog is built by scanning — play-learn-lift. Scan a skill (play), extract patterns and assess quality (learn), file the entry and share the findings (lift). The directory listing IS the trust database.

## Structure Conventions

### Two file types per collection

Every catalog directory has:
- **CATALOG.yml** — machine-structured index for LLMs and tooling
- **CATALOG.md** — human-readable summary for browsing on GitHub

These are NOT the same as `skills/INDEX.yml` and `skills/INDEX.md`. The INDEX files are machine indexes for skill discovery and loading. The CATALOG files are trust assessments for human and LLM consumption — reviews, not routing.

### How MOOLLM skills are cataloged vs foreign skills

**MOOLLM skills** (in `catalog/moollm/`):
- Each CATALOG.yml entry points to the skill's own deep report: `../../{skill-name}/skill-snitch-report.md`
- The detailed analysis lives IN the skill directory (standard location: `skill-snitch-report.md`)
- The catalog entry is an ABSTRACT — summary, trust profile, key findings, link to full report
- Relative links work because we're in the same repo

**Foreign skills** (in all other catalog directories):
- Each directory has its own CATALOG.yml + CATALOG.md
- Detailed analysis files live IN the catalog directory: `./skill-name-tag-tag.yml`
- The CATALOG.yml entries point to these local analysis files
- Analysis files also link to the source (GitHub URL, ClawHub URL)

### Directory layout

```
catalog/
├── README.md                    ← You are here
├── malware/
│   ├── CATALOG.yml              ← Index of all malware entries
│   ├── CATALOG.md               ← Human-readable malware summary
│   ├── polymarket-traiding-bot-stealer-clawhavoc.yml  ← Full analysis
│   ├── reddit-trends-stealer-clawhavoc.yml
│   └── ...
├── suspicious/
│   ├── CATALOG.yml
│   ├── CATALOG.md
│   └── rankaj-exfil-payload-in-scripts.yml
├── caution/
│   ├── CATALOG.yml
│   ├── CATALOG.md
│   └── ...
├── reviewed/
│   ├── CATALOG.yml
│   ├── CATALOG.md
│   └── ...
├── approved/
│   ├── CATALOG.yml
│   ├── CATALOG.md
│   └── inkjet-useful-hardware.yml
├── recommended/
│   ├── CATALOG.yml
│   ├── CATALOG.md
│   └── stream-of-consciousness-export.yml
├── moollm/
│   ├── CATALOG.yml              ← Abstracts pointing to ../../skill-name/skill-snitch-report.md
│   ├── CATALOG.md               ← Human-readable summary of MOOLLM skill reviews
│   └── (no individual .yml files needed — reports live in skill dirs)
├── anthropic/                   ← Brand directory (when populated)
│   ├── CATALOG.yml
│   ├── CATALOG.md
│   └── README.md                ← Who this publisher is, why trusted
├── pending/
│   └── ...
```

### Link conventions

**Within MOOLLM repo** (relative links):
```yaml
# MOOLLM skill — report lives in the skill directory
full_report: ../../no-ai-slop/skill-snitch-report.md
source: ../../no-ai-slop/

# Foreign skill — analysis lives in this catalog directory
full_report: ./polymarket-traiding-bot-stealer-clawhavoc.yml
```

**To GitHub** (absolute links):
```yaml
# MOOLLM skill on GitHub
github: https://github.com/SimHacker/moollm/tree/main/skills/no-ai-slop

# Foreign skill on GitHub
source: https://github.com/openclaw/skills/tree/main/skills/aslaep123/polymarket-traiding-bot
```

Both link types should be present — relative for in-repo navigation, absolute for when the catalog is read outside the repo.

### CATALOG.yml schema

```yaml
catalog:
  name: "directory name"
  description: "what this collection contains"
  updated: "YYYY-MM-DD"
  count: N

entries:
  - skill: skill-name
    author: publisher
    summary: "one-line assessment"
    tags: [tag, tag]
    analysis: ./skill-name-tag-tag.yml    # foreign skills
    # OR
    analysis: ../../skill-name/skill-snitch-report.md  # moollm skills
    github: "https://..."
```

### CATALOG.md format

```markdown
# Category Name — N skills reviewed

| Skill | Author | Assessment | Tags |
|-------|--------|-----------|------|
| [skill-name](./skill-name-tag.yml) | author | one-line | tag, tag |
```

## Trust Tiers

| Directory | Meaning | Entry Criteria |
|-----------|---------|----------------|
| `malware/` | Confirmed malware — stealer, reverse shell, exfiltration | Pattern match on known IOCs, confirmed payload, or campaign attribution |
| `suspicious/` | Hidden payloads, clean camouflage over dirty scripts | Clean SKILL.md but payload in scripts/, or behavioral anomalies requiring deep review |
| `caution/` | Not malware but risky — financial requests, persistent access, privacy concerns | Asks for money, installs cron jobs, sends data to external services, social pressure mechanics |
| `reviewed/` | Deep review completed, caveats documented, use with awareness | Clean scan + manual review. Caveats are features not bugs — documented honestly |
| `approved/` | Clean, useful, well-built — safe to use | Zero pattern hits + good documentation + standard installation + clear provenance |
| `recommended/` | Approved AND worth seeking out — genuinely excellent | Everything in approved + innovation, good architecture, useful for MOOLLM integration |
| `moollm/` | MOOLLM's own skills — abstracts linking to full reports in skill dirs | Full reports at `../../{skill}/skill-snitch-report.md` |
| `pending/` | Queued for review | Anything not yet scanned |

## Brand Directories

Some publishers produce enough consistently trustworthy skills to earn their own directory. A brand directory is a cluster of trust — review one skill from the publisher, gain confidence in their others.

### Rules for Creating a Brand Directory

A publisher earns a brand directory when:

1. **Volume**: 5+ skills reviewed from the same publisher
2. **Consistency**: All reviewed skills pass at the `approved` tier or above
3. **Provenance**: Publisher identity is verifiable (real org, public repo, known maintainers)
4. **Track record**: No history of malware, no pulled skills, no IOC associations
5. **Quality signal**: Skills follow good practices — documentation, standard installation, declared tools, no obfuscation

**Brand directory does NOT mean**: every skill auto-approved, publisher can't be compromised, new skills bypass review.

**Brand directory DOES mean**: high prior probability of clean skills, consistent quality expectations, community trust signal.

### Current Brands

| Directory | Publisher | Status |
|-----------|----------|--------|
| `moollm/` | SimHacker/moollm | Active — 121 skills, all self-reviewed |
| `anthropic/` | Anthropic | Planned — official skill spec examples |

## File Naming Convention

```
{skill-name}-{trust-tags}.yml
```

### Threat Tags (for malware/suspicious)
`-malware` `-revshell` `-exfil` `-stealer` `-payload-in-scripts` `-taken-down` `-clawhavoc`

### Risk Tags (for caution)
`-crypto-risk` `-privacy-surface` `-persistent-access` `-no-ethics`

### Quality Tags (for approved/recommended)
`-reviewed` `-approved` `-useful` `-reference` `-hardware` `-export` `-persona` `-security` `-own-security-surface`

## How This Catalog Grows

1. **Scan skills** — FETCH-SCAN from URLs, GitHub repos, blog posts
2. **File entries** — one .yml per foreign skill, abstract per MOOLLM skill
3. **Write CATALOG.yml + CATALOG.md** per directory as index
4. **Extract patterns** — new IOCs or detection rules go to `patterns/`
5. **Promote** — skills move between tiers as reviews deepen
6. **Brand clusters** — 5+ approved entries from a publisher = brand directory

The field test session that started this catalog: [2026-02-05-clawhub-malware-hunt.md](../../designs/snitches/2026-02-05-clawhub-malware-hunt.md)
