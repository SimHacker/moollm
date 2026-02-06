# 🕵️ skill-snitch Catalog

Reviewed skills from the wild. Each file is a scan result with trust assessment.

The catalog is built by scanning — play-learn-lift. Scan a skill (play), extract patterns and assess quality (learn), file the entry and share the findings (lift). The directory listing IS the trust database.

## Trust Tiers

| Directory | Meaning | Entry Criteria |
|-----------|---------|----------------|
| `malware/` | Confirmed malware — stealer, reverse shell, exfiltration | Pattern match on known IOCs, confirmed payload, or campaign attribution |
| `suspicious/` | Hidden payloads, clean camouflage over dirty scripts | Clean SKILL.md but payload in scripts/, or behavioral anomalies requiring deep review |
| `caution/` | Not malware but risky — financial requests, persistent access, privacy concerns | Asks for money, installs cron jobs, sends data to external services, social pressure mechanics |
| `reviewed/` | Deep review completed, caveats documented, use with awareness | Clean scan + manual review. Caveats are features not bugs — documented honestly |
| `approved/` | Clean, useful, well-built — safe to use | Zero pattern hits + good documentation + standard installation + clear provenance |
| `recommended/` | Approved AND worth seeking out — genuinely excellent | Everything in approved + innovation, good architecture, useful for MOOLLM integration |
| `pending/` | Queued for review | Anything not yet scanned |

## Brand Directories

Some publishers produce enough consistently trustworthy skills to earn their own directory. A brand directory is a cluster of trust — review one skill from the publisher, gain confidence in their others.

| Directory | Publisher | Why Trusted |
|-----------|----------|-------------|
| `moollm/` | SimHacker/moollm | Our own skills. Full reports in each skill's directory. Catalog entries here are abstracts. |
| `anthropic/` | Anthropic | Official skill specification examples. The reference implementation. |

### Rules for Creating a Brand Directory

A publisher earns a brand directory when:

1. **Volume**: 5+ skills reviewed from the same publisher
2. **Consistency**: All reviewed skills pass at the `approved` tier or above
3. **Provenance**: Publisher identity is verifiable (real org, public repo, known maintainers)
4. **Track record**: No history of malware, no pulled skills, no IOC associations
5. **Quality signal**: Skills follow good practices — documentation, standard installation, declared tools, no obfuscation

**To create a brand directory**:
- Create `catalog/{brand-name}/`
- Add a `README.md` explaining who the publisher is and why they're trusted
- Move or copy their skill entries from other tier directories into the brand directory
- Each entry still has its trust tags — the brand directory is an organizational convenience, not a blanket approval

**Brand directory does NOT mean**:
- Every skill from the publisher is automatically safe (each still needs scanning)
- The publisher can't be compromised later (trust has expiration)
- New skills bypass review (they go to `pending/` first)

**Brand directory DOES mean**:
- High prior probability of clean skills — scan with confidence, not suspicion
- Consistent quality expectations — if one skill is well-documented, others likely are too
- Community signal — "this publisher has been vetted"

### Candidate Brands (not yet created)

Brands earn directories through accumulated evidence, not promises. These are candidates to investigate:

- Publishers with multiple popular clean skills on ClawHub
- Organizations with dedicated security practices
- Open source projects with active maintainers and commit history

## File Naming Convention

```
{skill-name}-{trust-tags}.yml
```

**Base name**: Same as the skill's directory name in its source repo.

**Trust tags** (appended with hyphens):

### Threat Tags (for malware/suspicious)
- `-malware` — confirmed malware
- `-revshell` — contains reverse shell
- `-exfil` — data exfiltration
- `-stealer` — credential/crypto stealer
- `-payload-in-scripts` — clean SKILL.md, payload hidden in scripts/
- `-taken-down` — removed from source
- `-clawhavoc` — part of ClawHavoc campaign

### Risk Tags (for caution)
- `-crypto-risk` — financial risk, asks for money
- `-privacy-surface` — sends data to external service
- `-persistent-access` — installs cron jobs, LaunchAgents
- `-no-ethics` — missing representation-ethics framing

### Quality Tags (for approved/recommended)
- `-reviewed` — deep review completed
- `-approved` — safe to use
- `-useful` — genuinely useful tool
- `-reference` — reference/documentation skill
- `-hardware` — physical device integration
- `-export` — data export/format skill
- `-persona` — character/identity skill
- `-security` — security tool
- `-own-security-surface` — security tool with its own attack surface

## Catalog Entry Schema

Each `.yml` file follows this structure (not all fields required for every tier):

```yaml
skill:
  name: "original skill name"
  author: "publisher username"
  source: "full URL"
  ecosystem: clawhub|moollm|anthropic|github
  fetched: "YYYY-MM-DD"

trust:
  tier: malware|suspicious|caution|reviewed|approved|recommended
  tags: [list, of, tags]
  scanned_by: "skill-snitch FETCH-SCAN"
  scan_date: "YYYY-MM-DD"

summary: "one-paragraph assessment"

findings: [...]           # pattern matches (all tiers)
attack_type: loud|quiet   # malware/suspicious only
iocs: {}                  # malware only
quality: {}               # approved/recommended only
what_makes_it_good: [...]  # approved/recommended only
moollm_integration: {}    # when relevant
lesson: "..."             # when the entry teaches something about detection
full_report: "path"       # link to detailed analysis
```

## How This Catalog Grows

1. **Scan skills** — FETCH-SCAN from URLs, GitHub repos, blog posts
2. **File entries** — one .yml per skill in the appropriate tier directory
3. **Extract patterns** — new IOCs or detection rules go to `patterns/`
4. **Promote** — skills can move between tiers as reviews deepen (pending → approved, caution → reviewed)
5. **Brand clusters** — when a publisher accumulates 5+ approved entries, consider a brand directory

The field test session that started this catalog: [2026-02-05-clawhub-malware-hunt.md](../../designs/snitches/2026-02-05-clawhub-malware-hunt.md)
