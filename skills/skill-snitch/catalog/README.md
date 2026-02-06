# skill-snitch Catalog

Reviewed skills from the wild. Human-readable (CATALOG.md) and machine-structured (CATALOG.yml) indexes of trust assessments.

The catalog is built by scanning — play-learn-lift. Scan a skill (play), extract patterns and assess quality (learn), file the entry and share the findings (lift). The directory listing IS the trust database.

## Two File Types: CATALOG.yml and CATALOG.md

Every catalog directory has:
- **CATALOG.yml** — machine-structured index for LLMs and tooling
- **CATALOG.md** — human-readable summary for browsing on GitHub

### NOT the same as INDEX.yml/INDEX.md

The skill INDEX files (`skills/INDEX.yml`, `skills/INDEX.md`) are for **machine routing and discovery** — which skills exist, what k-lines they activate, load order. They answer: "what skill handles X?"

The CATALOG files are **trust assessments for human and LLM consumption** — reviews, not routing. They answer: "is this skill safe? what did the audit find?"

## How MOOLLM Skills Are Cataloged vs Foreign Skills

### MOOLLM skills (`catalog/moollm/`)

One CATALOG.yml + CATALOG.md for ALL MOOLLM skills. Each entry is an abstract (summary, trust profile, key findings) that **points to** the skill's own deep report.

- Full analysis lives IN the skill directory: `skills/{skill-name}/skill-snitch-report.md`
- CATALOG.yml entries link to it: `analysis: ../../../{skill-name}/skill-snitch-report.md`
- Also link to GitHub: `github: https://github.com/SimHacker/moollm/tree/main/skills/{skill-name}`
- No individual `.yml` analysis files in `catalog/moollm/` — reports live where the skill lives
- Relative links work because we're in the same repo

### Foreign skills (all other catalog directories)

Each trust-tier directory has its own CATALOG.yml + CATALOG.md, plus individual analysis files.

- Detailed analysis files live IN the catalog directory: `./skill-name-tag-tag.yml`
- CATALOG.yml entries link to these local files: `analysis: ./skill-name-tag-tag.yml`
- Also link to source: `source: https://github.com/...`
- For interesting individual skills (malware, suspicious), the `.yml` analysis file IS the deep dive
- CATALOG.yml abstracts point to these files; CATALOG.md provides narrative summaries

## Incremental Scanning Workflow

The catalog supports incremental population:

1. **Add entries with null analysis** — record skills you know about but haven't scanned yet
2. **Scan the skill** — read GLANCE/CARD/SKILL, run patterns, write analysis
3. **Create the analysis file** — for foreign skills: `./skill-name-tag-tag.yml` in the catalog dir. For MOOLLM skills: `skill-snitch-report.md` in the skill dir.
4. **Update CATALOG.yml** — set the `analysis:` field to point to the report
5. **Add narrative to CATALOG.md** — short summary with link to the full analysis

In CATALOG.yml, an entry with `analysis: null` means "known but not yet scanned." An entry with a path means "scanned — follow the link." In CATALOG.md, unscanned skills are omitted — only include entries once you have something to say.

## Directory Layout

```
catalog/
├── README.md                    <- You are here
├── moollm/
│   ├── CATALOG.yml              <- ALL 121 MOOLLM skills, abstracts pointing to ../../../{skill}/skill-snitch-report.md
│   └── CATALOG.md               <- Human-readable summary of MOOLLM skill reviews
├── malware/
│   ├── CATALOG.yml              <- Index of malware entries
│   ├── CATALOG.md               <- Human-readable malware summary
│   ├── polymarket-traiding-bot-stealer-clawhavoc.yml
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
├── anthropic/                   <- Brand directory (when populated)
│   ├── CATALOG.yml
│   ├── CATALOG.md
│   └── README.md
└── pending/
    └── ...
```

## Link Conventions

Both relative and absolute links should be present — relative for in-repo navigation, absolute for when the catalog is read outside the repo.

**MOOLLM skill in `catalog/moollm/CATALOG.yml`**:
```yaml
- skill: no-ai-slop
  analysis: ../../../no-ai-slop/skill-snitch-report.md
  github: https://github.com/SimHacker/moollm/tree/main/skills/no-ai-slop
```

**Foreign skill in a tier directory**:
```yaml
- skill: polymarket-traiding-bot
  analysis: ./polymarket-traiding-bot-stealer-clawhavoc.yml
  source: https://github.com/openclaw/skills/tree/main/skills/aslaep123/polymarket-traiding-bot
```

## CATALOG.yml Schema

```yaml
catalog:
  name: "directory name"
  description: "what this collection contains"
  updated: "YYYY-MM-DD"
  count: N           # total entries
  scanned: N         # entries with analysis (not null)

entries:
  - skill: skill-name
    author: publisher
    summary: "one-line assessment"
    tags: [tag, tag]
    analysis: ../../../skill-name/skill-snitch-report.md  # moollm skills
    # OR
    analysis: ./skill-name-tag-tag.yml                     # foreign skills
    # OR
    analysis: null                                          # not yet scanned
    github: "https://..."
```

## CATALOG.md Format

```markdown
# Collection Name — N skills reviewed

| Skill | Assessment | Tags |
|-------|-----------|------|
| [skill-name](../../../skill-name/skill-snitch-report.md) | one-line | tag, tag |
```

Only include skills that have been scanned (analysis is not null). The CATALOG.yml is the complete inventory; the CATALOG.md is the curated view.

## Trust Tiers

| Directory | Meaning | Entry Criteria |
|-----------|---------|----------------|
| `malware/` | Confirmed malware — stealer, reverse shell, exfiltration | Pattern match on known IOCs, confirmed payload, or campaign attribution |
| `suspicious/` | Hidden payloads, clean camouflage over dirty scripts | Clean SKILL.md but payload in scripts/, or behavioral anomalies requiring deep review |
| `caution/` | Not malware but risky — financial requests, persistent access, privacy concerns | Asks for money, installs cron jobs, sends data to external services, social pressure mechanics |
| `reviewed/` | Deep review completed, caveats documented, use with awareness | Clean scan + manual review. Caveats are features not bugs — documented honestly |
| `approved/` | Clean, useful, well-built — safe to use | Zero pattern hits + good documentation + standard installation + clear provenance |
| `recommended/` | Approved AND worth seeking out — genuinely excellent | Everything in approved + innovation, good architecture, useful for MOOLLM integration |
| `moollm/` | MOOLLM's own skills — abstracts linking to full reports in skill dirs | Full reports at `../../../{skill}/skill-snitch-report.md` |
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
