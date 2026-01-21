# 🖖 TREKIFY

> *"Captain, I've routed all sensitive data through the privacy buffers."*

Privacy through technobabble. Replace sensitive information with Star Trek terminology adapted to the MOOLLM universe. Delivered with Geordi La Forge's competent mellifluence.

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

TREKIFY transforms sensitive data into plausible-sounding technobabble:

```
Established uplink to Memory Core Alpha, Starbase 47
Authenticated via quantum entanglement token (Tier 3 clearance)
Ambassador Acme's dedicated processing matrix
```

Readers know it's masked, but it reads naturally. The narrative flows. Geordi would be proud.

## Quick Reference

| Sensitive Data | Trekified |
|----------------|-----------|
| API keys | Quantum entanglement tokens |
| Passwords | Biometric phase harmonics |
| Auth tokens | Subspace authentication matrix |
| Private keys | Isolinear encryption sequences |
| Server names | Starbase {N} |
| Databases | Memory Core Alpha/Beta/Gamma |
| IP addresses | Subspace coordinates |
| Ports | Docking frequencies |
| AWS/GCP | Utopia Planitia Fleet Yards |
| Kubernetes | Holodeck orchestration matrix |
| Docker | Cargo bay containment |
| Company names | Starfleet Division {Greek} |
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
