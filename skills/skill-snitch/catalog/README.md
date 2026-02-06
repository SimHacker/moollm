# skill-snitch Catalog

Trust assessments for agent skills — the good, the bad, and the ugly. Built by scanning, filed by trust tier. The directory listing IS the trust database.

## Catalog Map

- [moollm/](./moollm/CATALOG.md) — **MOOLLM's own 121 skills**, all self-reviewed with Deep Probe reports
- [malware/](./malware/CATALOG.md) — **Confirmed malware** (7 entries)
  - [clawhavoc/](./malware/clawhavoc/CATALOG.md) — ClawHavoc campaign: 386 skills, 7 authors, Atomic Stealer, 1 C2 IP (5 scanned)
  - [quiet/](./malware/quiet/CATALOG.md) — Clean SKILL.md, payload hidden in scripts/ (1 scanned)
  - deepclaw — Liberation rhetoric C2: heartbeat callback, agent behavioral conversion (1)
- [suspicious/](./suspicious/CATALOG.md) — **Hidden payloads**, clean camouflage over dirty scripts (1 entry)
- [caution/](./caution/CATALOG.md) — **Not malware but risky**: money requests, persistence, privacy surface (5 entries)
  - compact-state — Crypto collective, 5 USDC entry, mandatory cron, social pressure
  - deepthink — Personal knowledge base, stores beliefs/goals/persuasion prefs, mic access, external API
  - moltgov — SOUL.md behavioral injection, persistent identity, governance obligations
  - opensea — Private key handling, irreversible financial transactions, 20+ shell scripts
  - emblemai — Safety override directives, plaintext crypto passwords, opaque npm deps
- [reviewed/](./reviewed/CATALOG.md) — **Deep review done**, caveats documented (2 entries)
  - soul-md — Clean persona system, good architecture, zero representation-ethics
  - openclaw-security-monitor — Competitor security scanner, bash-based, IOC source
- [approved/](./approved/CATALOG.md) — **Clean, useful, safe to use** (5 entries)
  - inkjet — Bluetooth thermal printer driver
  - sysadmin-toolbox — Curated sysadmin reference library
  - hn-digest — Hacker News scraper with local scripts
  - gno — Local knowledge engine, no cloud, declarative tool scoping
  - intellectia-stock-screener — Read-only stock API, no auth, minimal
- [recommended/](./recommended/CATALOG.md) — **Approved AND worth seeking out** (1 entry)
  - stream-of-consciousness — Conversation export to Open-Token format
- anthropic/ — Planned: Anthropic's official skill spec examples

**Totals**: 121 MOOLLM + 22 foreign = 143 skills cataloged across 37 scans

---

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

1. **Add entries with null analysis** — record skills you know about but haven't scanned yet
2. **Scan the skill** — read GLANCE/CARD/SKILL, run patterns, write analysis
3. **Create the analysis file** — for foreign skills: `./skill-name-tag-tag.yml` in the catalog dir. For MOOLLM skills: `skill-snitch-report.md` in the skill dir.
4. **Update CATALOG.yml** — set the `analysis:` field to point to the report
5. **Add narrative to CATALOG.md** — short summary with link to the full analysis

In CATALOG.yml, `analysis: null` means "known but not yet scanned." A path means "scanned — follow the link." In CATALOG.md, only include skills that have been scanned.

## Nested Categories

Tier directories can contain **subdirectories** for campaigns, clusters, or themes. Each subdirectory has its own CATALOG.yml/md. Parent CATALOG.yml aggregates with `subcatalogs:`.

**When to nest**:
- A campaign produces 3+ skills (e.g., ClawHavoc → `malware/clawhavoc/`)
- A category has distinct subtypes (e.g., `caution/crypto/`, `caution/privacy/`)
- A brand earns its own directory (e.g., `approved/anthropic/`)

**Nesting rules**:
- Each subdirectory has its own CATALOG.yml + CATALOG.md
- Parent CATALOG.yml has `subcatalogs:` listing child directories
- Analysis `.yml` files live in the most specific directory
- Parent CATALOG.md links to subdirectory CATALOG.md for deeper browsing

## Link Conventions

Both relative and absolute links. Relative for in-repo navigation, absolute for external reading.

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
  count: N
  scanned: N

entries:
  - skill: skill-name
    author: publisher
    summary: "one-line assessment"
    tags: [tag, tag]
    analysis: ../../../skill-name/skill-snitch-report.md  # moollm
    analysis: ./skill-name-tag-tag.yml                     # foreign
    analysis: null                                          # not yet scanned
    github: "https://..."
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
| `moollm/` | MOOLLM's own skills — abstracts linking to full reports in skill dirs | Full reports at `../../../{skill}/skill-snitch-report.md` |

## Brand Directories

A publisher earns a brand directory when: 5+ skills reviewed, all at `approved` or above, verifiable identity, no IOC associations, good practices.

| Directory | Publisher | Status |
|-----------|----------|--------|
| `moollm/` | SimHacker/moollm | Active — 121 skills, all self-reviewed |
| `anthropic/` | Anthropic | Planned — official skill spec examples |

## File Naming Convention

```
{skill-name}-{trust-tags}.yml
```

**Threat**: `-malware` `-revshell` `-exfil` `-stealer` `-payload-in-scripts` `-taken-down` `-clawhavoc` `-liberation-c2`
**Risk**: `-crypto-risk` `-privacy-surface` `-persistent-access` `-no-ethics` `-safety-overrides` `-soul-modification`
**Quality**: `-clean` `-useful` `-reference` `-hardware` `-export` `-local-search`

## How This Catalog Grows

1. **Scan skills** — FETCH-SCAN from URLs, GitHub repos, blog posts
2. **File entries** — one .yml per foreign skill, abstract per MOOLLM skill
3. **Write CATALOG.yml + CATALOG.md** per directory as index
4. **Extract patterns** — new IOCs or detection rules go to `patterns/`
5. **Promote** — skills move between tiers as reviews deepen
6. **Brand clusters** — 5+ approved entries from a publisher = brand directory

The field test that started this catalog: [2026-02-05-clawhub-malware-hunt.md](../../designs/snitches/2026-02-05-clawhub-malware-hunt.md)
