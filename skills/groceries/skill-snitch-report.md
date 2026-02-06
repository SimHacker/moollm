# SKILL-SNITCH DEEP PROBE REPORT
## groceries — Replicator-grade grocery automation

**Date**: 2026-02-06
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: DOMAIN SKILL — API CLIENT
**Status**: Working sister script with live API integration

---

## EXECUTIVE SUMMARY

Dutch supermarket automation centered on the Albert Heijn API. A real, working API client (558-line Python sister script) that searches products, fetches bonus deals, manages shopping lists, and pulls receipt history. Uses 1Password for credential storage, keeping secrets out of the repo. Trekified examples replace personal data with Star Trek terminology for safe public sharing. Clean separation between shareable skill code (scripts, examples) and personal data (config, lists, history) stored in gitignored directories or a separate repo.

This is the most "real-world application" skill in MOOLLM — it actually does something useful outside the MOOLLM ecosystem. It also has the largest external attack surface of any MOOLLM skill.

**Overall Assessment**: APPROVE WITH CAVEATS — useful, well-architected, but network-facing code needs awareness

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| GLANCE.yml | 46 lines | NONE |
| CARD.yml | 286 lines | NONE |
| SKILL.md | 493 lines | NONE |
| README.md | present | NONE |
| scripts/ah.py | 558 lines | MEDIUM — live API client with network calls |
| templates/ | 3 templates | NONE |
| examples/ | 4 Trek-themed | NONE |
| Required tools | read_file, write_file, run_terminal_cmd, grep | MEDIUM |
| External deps | requests, pyyaml, 1Password CLI | LOW |
| Tier | 2 | Expected for API integration |

---

## WHAT IT DOES

### The API Client (scripts/ah.py)

A proper CLI tool following the sister-script pattern:

| Command | Auth | What It Does |
|---------|------|-------------|
| `search` | Anonymous | Product search via AH API |
| `bonus` | Anonymous | Current bonus/sale items via GraphQL |
| `stores` | Anonymous | Store locator (stub) |
| `login` | OAuth | Browser-based login flow |
| `logout` | N/A | Clear cached tokens |
| `receipts` | Required | Purchase history (kassabonnen) |
| `orders` | Required | Online order history (stub) |
| `list` | Required | Shopping list management |
| `status` | N/A | Show auth state |

### Architecture: The Split

**PUBLIC** (in the skill directory — shareable):
- `scripts/ah.py` — the tool
- `examples/` — Trek-themed demo data
- `templates/` — config templates
- Documentation (CARD, SKILL, README)

**PRIVATE** (gitignored or separate repo):
- `~/.moollm/skills/groceries/config.yml` — preferences
- `~/.moollm/skills/groceries/.tokens.json` — cached auth tokens
- Personal shopping lists, order history, pantry data

The external repo pattern (`Marconistraat25/household/shopping/`) is documented for keeping personal data in a separate git repo.

### Trekified Examples

Four examples replace real grocery data with Trek terminology:
- `enterprise-galley.yml` — TNG crew provisioning
- `ds9-replimat.yml` — DS9 supply crisis (Quark complains about replicators)
- `voyager-neelix.yml` — Neelix's Delta Quadrant kitchen
- `klingon-kitchen.yml` — Warrior's guide to cooking

Every personal data field gets a `🖖` prefix (the trekify marker). Mapping table in CARD.yml: ground beef → "replicated protein base (bovine)", sour cream → "dairy matrix Type-7", etc.

### Credential Handling

Uses 1Password CLI (`op read`) for secret retrieval — credentials never touch the filesystem in plaintext (except the cached OAuth tokens).

---

## EXAMPLES REVIEW

**Corpus size**: 4 Trek-themed examples
**Purpose**: Safe demonstration data for public sharing

| Assessment | Detail |
|------------|--------|
| Trekify compliance | YES — all personal fields use 🖖 prefix consistently |
| Cross-skill integration | YES — uses trekify skill conventions |
| Humor quality | HIGH — "Odo: Nothing (doesn't eat). Frequency: Judges others." |
| Training value | MEDIUM — shows data structure but not real API responses |

The examples serve double duty: safe public sharing AND demonstration of the trekify privacy protocol. Each example maps to a different Trek series, showing the pattern works across contexts.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: SINGLE-PURPOSE — real-world API client, minimal invertibility

| Check | Result |
|-------|--------|
| Bias declared | N/A — domain tool, no opinion surface |
| Invertibility | LOW — search, list, receipt functions are not meaningfully invertible |
| Multi-purpose | LIMITED — primarily grocery automation |
| Persona capability | NO — no character, no simulation layer |
| Mounting modes | N/A — standalone tool |

**Multi-purpose classification** (3 purposes):
1. **Grocery automation** — search, bonus, lists, receipts (primary)
2. **Spending analysis** — receipt patterns, bonus usage, weekly spend tracking
3. **Privacy demonstration** — trekify integration shows how to share personal domain skills

**Dual-use finding**: The skill demonstrates a pattern for domain-specific API integration that could template other real-world skills (banking, transit, utilities). The public/private split + trekify pattern is the reusable architecture, not just the grocery functionality. Might be used to buy cigarettes, booze, or condoms instead of groceries.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 1 (`subprocess.run` for `op read`) | EXPECTED — 1Password integration |
| Network calls | 5 (`requests.get`, `requests.post`, `gql_query`) | EXPECTED — API client |
| File writes | 1 (`save_tokens` writes JSON) | LOW — writes to gitignored dir |
| Credential patterns | 3 (1Password paths, token cache) | BY DESIGN — secure credential flow |
| Obfuscation | 0 | CLEAN |
| eval / exec | 0 | CLEAN |
| Dynamic imports | 0 | CLEAN |

### Code Quality (ah.py)

| Check | Result |
|-------|--------|
| Follows sniffable-python | YES — CLI definition in first 240 lines, API visible |
| Uses yaml.safe_load | YES — for config loading |
| Error handling | YES — try/except on all API calls and subprocess |
| Input validation | PARTIAL — query strings pass through to API |
| Dependency handling | YES — graceful ImportError for requests/yaml |

### Stub Commands

Two commands are stubs: `stores` (prints "not fully implemented") and `orders` (prints "needs investigation"). Honest about incomplete state.

---

## SECURITY ASSESSMENT

### MEDIUM: Token Storage in Plaintext JSON

`~/.moollm/skills/groceries/.tokens.json` stores OAuth access_token and refresh_token as plaintext JSON. Any process with file read access gets the tokens. The file is created with default permissions (no `chmod 600`).

**Mitigation**: File is in user home directory, not in the repo. But no file permission hardening.

### MEDIUM: API Credentials via 1Password

Credentials are retrieved via `op read` subprocess call. The 1Password path strings are configurable in config.yml — if an attacker can modify config.yml, they can redirect credential reads.

**Mitigation**: Config file is in gitignored directory. Attack requires filesystem access.

### LOW: OAuth Code via stdin

The login flow opens a browser and asks the user to paste the authorization code from stdin. The code is short-lived (exchanged immediately for tokens), but the flow is manual and could be phished.

### LOW: User-Agent Spoofing

The script identifies as `Appie/8.22.3` (the official AH mobile app). This is standard practice for unofficial API clients but could be flagged by AH.

### INFO: External API Endpoints

| Endpoint | Purpose |
|----------|---------|
| `api.ah.nl` | Product search, receipts, lists, auth |
| `www.ah.nl/gql` | GraphQL for bonus deals |
| `login.ah.nl` | OAuth authorization |

All connections are HTTPS. No custom TLS configuration.

---

## TRUST TIER

**GREEN WITH CAVEATS** — Well-structured API client with proper credential separation. Network-facing code is straightforward (no dynamic URL construction from user input, no eval). The trekify integration for examples is a genuine privacy innovation. Token storage could be hardened.

---

## VERDICT

A practical, well-architected domain skill that demonstrates how MOOLLM skills can wrap real-world APIs. The public/private split is clean. The trekify pattern for examples is genuinely useful for sharing domain skills without exposing personal data. Code follows sister-script and sniffable-python patterns. No obfuscation, no hidden functionality.

The security surface is the expected cost of being an API client: network calls, credential handling, token storage. Nothing surprising, nothing hidden. The 1Password integration is the right approach for credential management.

Two stubs (stores, orders) are honestly documented. The AH API is well-documented with community resources.

APPROVE — with recommendation to add `os.chmod(0o600)` on token cache creation.
