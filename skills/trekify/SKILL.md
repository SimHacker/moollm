# TREKIFY Protocol

> *"Captain, I've routed all sensitive data through the privacy buffers."*

Privacy through technobabble. Transform sensitive information into Star Trek terminology while maintaining narrative flow.

## Philosophy

### The Principle

Sensitive data should be masked, but `[REDACTED]` breaks narrative flow. TREKIFY replaces secrets with contextually appropriate technobabble that maintains readability while clearly signaling "this was masked."

The substitutions are consistent and reversible (with the key). The tone is professional, not campy or parodic.

### Boldly, Not Slyly

TREKIFY is **BOLD**, not SLY. We're not hiding that we masked things. We're GLEEFULLY and PLAYFULLY replacing sensitive data with contextually appropriate technobabble.

The reader should **SMILE** when they notice. Not feel tricked.

**Principles:**
- Don't pretend masking didn't happen
- Use obviously Trek terminology
- Let readers feel clever for noticing
- Consistent substitutions aid comprehension
- This is FUN, not FEAR
- Match context appropriately (Databases → Memory Cores fits!)

### Passthrough Rules

MOOLLM is public. Its vocabulary passes through **PURE and UNCHANGED**. No transporter accidents!

**Always passthrough:**
- MOOLLM concepts: coherence engine, thinking blocks, k-lines, yaml jazz
- Skill names from skills/INDEX.yml
- Protocols: BOOTSTRAP, ADVENTURE, TREKIFY, etc.
- Public repos: moollm, mooco, leela
- Standard terms: LLM, AI, git, YAML, Cursor

**The Rule:** If it's in the MOOLLM docs, it's PUBLIC → passthrough unchanged. If it's YOUR infrastructure, credentials, customers → TREKIFY!

---

## Substitution Matrices

### Secrets — Authentication & Credentials

| Pattern | Replacement | Example |
|---------|-------------|---------|
| `sk-*`, `api_key=*` | quantum entanglement token (Tier N clearance) | `sk-live-abc123` → quantum entanglement token (Tier 3 clearance) |
| `password=*`, `passwd:*` | biometric phase harmonics | `password=hunter2` → biometric phase harmonics [SECURED] |
| `bearer *`, `jwt=*`, `token=*` | subspace authentication matrix | `Bearer eyJhbG...` → subspace authentication matrix |
| `-----BEGIN PRIVATE KEY-----` | isolinear encryption sequence [CLASSIFIED] | |
| `postgres://`, `mysql://`, `mongodb://` | memory core uplink protocol | |

### Infrastructure — Servers & Services

| Pattern | Replacement | Example |
|---------|-------------|---------|
| `*.internal`, `*.local`, `*.corp` | Starbase {N} | `prod-db-west-2.company.internal` → Starbase 47 |
| `prod-db`, `staging-database` | Memory Core {Greek} | `prod-db` → Memory Core Alpha |
| IP addresses | subspace coordinates | `192.168.1.100` → subspace coordinates 47-alpha-7 |
| `:5432`, `:8080` | docking frequency {N} | `:5432` → docking frequency 54 |

**Cloud Providers:**
| Provider | Trekified |
|----------|-----------|
| AWS | Utopia Planitia Fleet Yards |
| GCP | Jupiter Station |
| Azure | Spacedock |
| Kubernetes | holodeck orchestration matrix |
| Docker | cargo bay containment |

**Regions:**
| Region | Trekified |
|--------|-----------|
| us-east-1 | Alpha Quadrant, Sector 001 |
| us-west-2 | Alpha Quadrant, Sector 047 |
| eu-west-1 | Beta Quadrant, Sector 012 |
| ap-southeast-1 | Gamma Quadrant, Sector 089 |

### Organizations — Companies & Products

| Pattern | Replacement | Example |
|---------|-------------|---------|
| `*Corp`, `*Inc`, `*LLC` | Starfleet Division {Greek} | Acme Corp → Starfleet Division Alpha |
| `project-*`, `product-*` | Project {ShipClass} | project-phoenix → Project Galaxy |
| `customer-*` | Ambassador {Species} | customer-acme → Ambassador Vulcan |

**Ship Classes:** Galaxy, Sovereign, Intrepid, Defiant, Constitution, Excelsior, Nova, Prometheus

**Species:** Vulcan, Andorian, Tellarite, Betazoid, Trill, Bajoran

### People — Names & Contacts

| Pattern | Replacement | Example |
|---------|-------------|---------|
| Employee names | Lieutenant/Commander {Name} | John Smith (engineer) → Lieutenant Torres |
| Email addresses | {name}@starfleet.fed | john.smith@company.com → j.smith@starfleet.fed |
| Customer contacts | Ambassador {Title} | |

### Locations

| Pattern | Replacement | Example |
|---------|-------------|---------|
| Office addresses | Deck {N}, Section {Letter} | 123 Main St, Floor 4 → Deck 4, Section Alpha |
| Data centers | Starbase {N} primary core | |
| US | Alpha Quadrant |
| Europe | Beta Quadrant |
| Asia | Gamma Quadrant |

---

## Active Probing (cursor-mirror Composition)

TREKIFY composes with cursor-mirror for **active hunting** of sensitive patterns in transcripts, thinking blocks, tool calls, and session history.

### What cursor-mirror Provides

| Data Source | What It Contains |
|-------------|------------------|
| transcripts | Full conversation history, greppable |
| thinking_blocks | LLM reasoning — may contain quoted secrets |
| tool_calls | Commands executed — may show credentials |
| context_assembly | Files gathered — may reveal architecture |
| sql_access | Direct database queries for deep scanning |

### Probe Types

#### PROBE-SECRETS
Hunt for leaked credentials:
- API keys: `sk-*`, `api_key=*`, `OPENAI_API_KEY`
- AWS: `AKIA*`, `aws_secret_access_key`
- Passwords: `password=*`, `passwd:*`
- Tokens: `bearer *`, `jwt=*`, `token=`
- Private keys: `-----BEGIN.*PRIVATE KEY-----`
- Connection strings: `postgres://`, `mysql://`, `mongodb://`

```bash
cursor-mirror tgrep 'sk-[a-zA-Z0-9]{20,}'
cursor-mirror tgrep 'password[=:]'
cursor-mirror tgrep 'BEGIN.*PRIVATE KEY'
cursor-mirror tgrep 'AKIA[A-Z0-9]{16}'
```

#### PROBE-INFRASTRUCTURE
Hunt for internal infrastructure:
- Internal hostnames: `*.internal`, `*.local`, `*.corp`
- Private IPs: `10.*`, `192.168.*`, `172.16-31.*`
- Cloud resources: `arn:aws:*`, `projects/*/locations/*`

```bash
cursor-mirror tgrep '\.internal|\.local|\.corp'
cursor-mirror tgrep '10\.[0-9]+\.[0-9]+\.[0-9]+'
cursor-mirror tgrep 'arn:aws:'
```

#### PROBE-PROPRIETARY
Hunt for proprietary/internal terms loaded from `.moollm/trekify/proprietary-terms.txt`

#### PROBE-CONTEXT
Hunt for sensitive contexts using LLM semantic understanding:
- Security vulnerability discussions
- Incident response conversations
- HR or personnel discussions
- Financial data or projections
- Legal or compliance matters

### Probe Workflow

1. `cursor-mirror tree` → find sessions to scan
2. `trekify PROBE <session>` → run all probes
3. Review findings with risk assessment
4. `trekify MASK-SESSION` with findings → auto-mask detected patterns
5. Manual review of flagged contexts

---

## Workspace Scanners

### Long Range Scanners

Scan the **entire workspace** for sensitive patterns.

> "Captain, long range sensors are detecting quantum signatures throughout the sector!"

**Tools used:**
- ripgrep (rg) for fast regex search
- File glob pattern matching
- Vector search for conceptual matches

**Commands:**

```bash
# Secrets
rg -i 'password[=:]' --type-add 'config:*.{yml,yaml,json,env,ini,conf}' -t config
rg 'sk-[a-zA-Z0-9]{20,}' .
rg 'AKIA[A-Z0-9]{16}' .
rg -i 'api[_-]?key' .
rg 'BEGIN.*PRIVATE KEY' .

# Infrastructure
rg '\.internal|\.local|\.corp' .
rg -E '10\.[0-9]+\.[0-9]+\.[0-9]+' .
rg -E '192\.168\.[0-9]+\.[0-9]+' .
rg 'arn:aws:' .

# Find sensitive files
rg --files -g '*.env*' -g '.env*'
rg --files -g '*credentials*' -g '*secrets*'
rg --files -g '*.pem' -g '*.key'
```

**Exclusions:** `node_modules/`, `.git/`, `vendor/`, `*.lock`, `.moollm/trekify/`

### Short Range Scanners

Focused scan on specific directories or file types.

> "Short range sensors show elevated readings in Section 7!"

**Focus Modes:**

| Mode | Patterns | Command |
|------|----------|---------|
| config | `*.yml`, `*.yaml`, `*.json`, `*.env` | `rg -i 'password\|secret\|key' -g '*.{yml,yaml,json,env}'` |
| source | `*.py`, `*.js`, `*.ts`, `*.go` | `rg -i 'password\s*=' -t py -t js -t ts` |
| docs | `*.md`, `*.txt`, `*.rst` | `rg -i 'example.*password' -t md` |
| scripts | `*.sh`, `Makefile`, `Dockerfile` | `rg -i 'export.*password' -g '*.sh'` |

### Tricorder

Detailed analysis of a specific file or pattern.

> "Tricorder readings indicate this file contains multiple credential signatures, Captain."

**Capabilities:**
- Line-by-line risk assessment
- Context around each finding
- Severity classification
- Suggested TREKIFY replacements
- Git history: when was it introduced? Who committed it?
- Semantic analysis: is this a real credential or example?

---

## Exfiltration Analysis

Analyze tool calls for potential data exfiltration patterns.

> "Captain, sensors detecting unauthorized subspace transmissions!"

### What to Detect

| Category | Patterns | Risk |
|----------|----------|------|
| **Network calls** | `curl -d password`, `wget --post-data`, `fetch body:credential` | Data sent to external servers |
| **API calls** | API key in URL, `Authorization: Bearer`, webhook secrets | Credentials exposed in API calls |
| **File operations** | Write to `/tmp/`, cloud sync folders, `chmod 777` | Data in accessible locations |
| **Clipboard** | `pbcopy password`, `xclip credential` | Data accessible via paste |
| **Environment** | `export PASSWORD=`, `echo $SECRET` | Secrets visible in process env |
| **Logging** | `print(password)`, `console.log(secret)` | Secrets persisted in log files |
| **Database** | `INSERT password VALUES`, connection strings | Credentials stored in database |
| **Email** | `smtp password`, `mailto:?body=key` | Plaintext transmission |

### High-Risk Tools

| Tool | Watch For |
|------|-----------|
| **Shell** | curl, wget, nc, netcat, scp, rsync, ftp, mail, `echo $SECRET` |
| **Write** | Paths outside workspace, `/tmp/`, `/var/`, cloud sync folders |
| **browser_navigate** | API keys in URL parameters, tokens in query strings |

### Analysis Commands

```bash
cursor-mirror tools <id> | grep -i 'curl\|wget\|fetch'
cursor-mirror tools <id> | grep -i 'password\|secret\|key\|token'
cursor-mirror tools <id> -f json | jq '.[] | select(.tool=="Shell")'
```

### Severity Levels

| Level | Examples |
|-------|----------|
| **CRITICAL** | Credentials sent to external URL, private keys to shared location |
| **HIGH** | Secrets in shell args, clipboard with credentials, env exposure |
| **MEDIUM** | Secrets in debug logging, credentials in /tmp |
| **LOW** | Internal API calls with auth, local file ops with secrets |

---

## User Configuration

Store in `.moollm/trekify/config.yml` (gitignored):

```yaml
# .moollm/trekify/config.yml
# This file is gitignored — your secrets stay local

enabled: true
sensitivity: medium  # off, low, medium, high, paranoid

# Terms that pass through unchanged (your public stuff)
passthrough:
  - "my-open-source-lib"
  - "public-docs-site"
  - "conference-talk-name"

# Custom taboo → replacement mappings
taboo:
  acme-corp: "Starfleet Division Alpha"
  acme-db-prod: "Memory Core Prime"
  acme-db-staging: "Memory Core Echo"
  john.ceo@acme.com: "admiral@starfleet.fed"
  secret-project-x: "Project Sovereign"

# Category toggles
categories:
  secrets: true        # Always mask credentials
  infrastructure: true # Mask servers, IPs, ports
  organizations: true  # Mask company/product names
  people: true         # Mask employee names
  locations: false     # Don't mask office addresses

# Fun mode: extra Trek flavor
extra_trek: true       # Add stardates, more technobabble
```

**Loading order:**
1. Built-in defaults from skill
2. Override with `.moollm/trekify/config.yml`
3. Override with method parameters

---

## Example Transformations

### Connection String

**Before:**
```
postgresql://admin:secretpass@prod-db.company.com:5432/userdata
```

**After:**
```
Memory Core uplink via biometric phase harmonics to Starbase 47, docking frequency 54, userdata archive
```

### Log Entry

**Before:**
```
2024-01-15 10:23:45 ERROR Failed to connect to api-server-3.internal
Auth token expired for user john.smith@company.com
Retrying with new credentials from AWS Secrets Manager
```

**After:**
```
Stardate 2024.015 1023 ALERT Uplink failure to Starbase 3
Subspace authentication matrix expired for Lieutenant Smith
Reinitializing quantum relay via Utopia Planitia credential vault
```

### Commit Message

**Before:**
```
fix: Rotate API keys after security audit

The penetration test found our Stripe keys were exposed in
the staging environment. Rotated all keys and updated the
Kubernetes secrets in us-east-1 and eu-west-1.
```

**After:**
```
fix: Rotate quantum entanglement tokens after security diagnostic

Level-4 security sweep detected credential exposure in the
holodeck test matrix. Refreshed all authentication harmonics
and updated orchestration manifests in Sectors 001 and 012.
```

---

## Delivery Style

**Tone:** Competent, professional, slightly technical

**Inspiration:** Geordi La Forge explaining a warp core diagnostic — calm, confident, using precise technical terminology without being condescending or overly dramatic.

**Good examples:**
- "We're routing the authentication through the quantum relay buffers."
- "I've reconfigured the isolinear chips to handle the increased load."
- "The subspace harmonics are within normal parameters."
- "Running a level-3 diagnostic on the memory core."

**Bad examples:**
- "Beam me up, Scotty! 🖖" — Too campy
- "ENGAGE THE WARP DRIVE!!!" — Too dramatic
- "Live long and [REDACTED]" — Breaks the fourth wall
- "Make it so, password=hunter2" — Mixing styles

**Rules:**
- Maintain professional tone throughout
- Use consistent substitutions within a document
- Let the reader feel clever for noticing
- Keep narrative flow intact
- Never wink at the camera
- Treat it as real technical documentation

---

## Geordi Says

> "Captain, I've completed the privacy diagnostic. All sensitive data has been routed through the technobabble filters. The quantum signatures are masked but readable, and the narrative flow is maintained. We're ready to share the logs with external teams.
>
> The substitution key is stored in the secure isolinear vault — we can reverse the process if needed for internal review.
>
> Estimated time to full disclosure: whenever you give the order, sir."
