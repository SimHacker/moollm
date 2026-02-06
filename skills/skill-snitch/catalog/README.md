# 🕵️ skill-snitch Catalog

Reviewed skills from the wild. Each file is a scan result with trust assessment.

## Directory Structure

| Directory | Meaning |
|-----------|---------|
| `malware/` | Confirmed malware — stealer, reverse shell, exfiltration |
| `suspicious/` | Hidden payloads, clean camouflage over dirty scripts, needs deep review |
| `caution/` | Not malware but risky — financial requests, persistent access, privacy concerns |
| `reviewed/` | Deep review completed, caveats documented, use with awareness |
| `approved/` | Clean, useful, well-built — recommended |
| `pending/` | Queued for review |

## File Naming Convention

```
{skill-name}-{trust-tags}.yml
```

**Base name**: Same as the skill's directory name in its source repo.

**Trust tags** (appended with hyphens):

| Tag | Meaning |
|-----|---------|
| `-malware` | Confirmed malware |
| `-revshell` | Contains reverse shell |
| `-exfil` | Data exfiltration |
| `-stealer` | Credential/crypto stealer |
| `-payload-in-scripts` | Clean SKILL.md, payload hidden in scripts/ |
| `-taken-down` | Removed from source, scan from IOC data |
| `-crypto-risk` | Financial risk, asks for money |
| `-privacy-surface` | Sends data to external service |
| `-no-ethics` | Missing representation-ethics framing |
| `-own-security-surface` | Security tool with its own attack surface |
| `-reviewed` | Deep review completed |
| `-approved` | Approved for use / recommendation |
| `-useful` | Genuinely useful tool |
| `-reference` | Reference/documentation skill |
| `-hardware` | Physical device integration |
| `-export` | Data export/format skill |
| `-persona` | Character/identity skill |
| `-security` | Security tool |

**Examples**:
- `red/polymarket-traiding-bot-malware-stealer.yml`
- `green/inkjet-approved-useful-hardware.yml`
- `orange/rankaj-exfil-payload-in-scripts.yml`
- `blue/deepthink-privacy-surface-reviewed.yml`

## How to Read a Catalog Entry

Each `.yml` file contains:

```yaml
skill:
  name: "original skill name"
  author: "publisher username"
  source: "full URL to skill on GitHub or ClawHub"
  fetched: "date scanned"

trust:
  tier: red|orange|yellow|blue|green
  tags: [malware, stealer, ...]
  scanned_by: "skill-snitch FETCH-SCAN"
  scan_date: "YYYY-MM-DD"

summary: "one-line assessment"

findings: [...]  # pattern matches
analysis: "..."  # narrative assessment
moollm_integration: "..." # potential for MOOLLM adoption
```

## Source

First populated from: [2026-02-05-clawhub-malware-hunt.md](../../designs/snitches/2026-02-05-clawhub-malware-hunt.md)
