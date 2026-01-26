# skill-snitch: Skill Audit & Runtime Surveillance

> "What's this skill REALLY doing?" — Static analysis + runtime observation.

**Status: IMPLEMENTED** (January 2026)

---

## What We Built

### cursor-mirror Security Commands (73 total commands)

| Command | Purpose | Output |
|---------|---------|--------|
| `deep-snitch` | Comprehensive security audit | K-REFs to findings |
| `secrets` | Scan for credentials/API keys | K-REFs |
| `full-audit` | ALL vectors: prompts, tools, shell, MCP | K-REFs |
| `exfil-audit` | Secret exfiltration detection | K-REFs |
| `url-audit` | URLs in tool calls with secrets | K-REFs |
| `pattern-scan` | UUIDs, hashes, custom patterns | K-REFs |
| `audit` | Composable: surfaces × patterns | K-REFs |
| `scrub` | Redact sensitive content | Modified files |
| `mask-in-place` | Mask secrets preserving length | Modified files |
| `tgrep` | Transcript-aware grep | Structured matches |

### skill-snitch Skill (28 files)

```
skills/skill-snitch/
├── CARD.yml              # Interface, methods, trust tiers
├── SKILL.md              # Protocol, prompts, workflow
├── README.md             # Documentation
├── SCAN-METHODOLOGY.md   # Deep methodology docs
├── registry.yml          # Skill registry
├── analyzers/            # 6 analysis dimensions
│   ├── behavioral.yml    # Runtime behavior checks
│   ├── consistency.yml   # Cross-file consistency
│   ├── provenance.yml    # Origin/lineage tracking
│   ├── runtime.yml       # Execution observation
│   ├── skill-type.yml    # Classification
│   └── smells.yml        # Code smell detection
├── patterns/             # 5 pattern categories
│   ├── dangerous-ops.yml # Shell, eval, subprocess
│   ├── exfiltration.yml  # Data leakage vectors
│   ├── obfuscation.yml   # Encoded/hidden code
│   ├── secrets.yml       # API keys, passwords
│   └── template-injection.yml
├── surfaces/             # 4 scan surfaces
│   ├── config-files.yml  # .cursorrules, settings
│   ├── skill-files.yml   # CARD.yml, SKILL.md, *.py
│   ├── sqlite.yml        # Database introspection
│   └── transcripts.yml   # Chat history
└── templates/            # 8 scaffolding templates
    └── *.tmpl
```

---

## The Ouroboros Effect

When security scanning a transcript that contains security pattern definitions:

```
Finding: "API key pattern sk-[a-zA-Z0-9]+ detected"
Location: cursor_mirror.py:4521
Reality: FALSE POSITIVE — it's the regex definition, not a leak
```

**~80% of findings are false positives** in self-referential scans. The scanner finds its own patterns. We named this the **Ouroboros Effect** and added the snake to the mythical characters roster.

Mitigation: Check actual line content, not just pattern match.

---

## Architecture: Orchestrator-Agnostic

`skill-snitch` works across ALL orchestrators by calling the appropriate `<orchestrator>-mirror`:

```
┌─────────────────────────────────────────────────────────────┐
│                      skill-snitch                            │
│              (orchestrator-agnostic layer)                   │
├─────────────────────────────────────────────────────────────┤
│         ┌─────────────────┼─────────────────┐               │
│         ▼                 ▼                 ▼               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │cursor-mirror│  │vscode-mirror│  │windsurf-    │  ...    │
│  │ deep-snitch │  │ deep-snitch │  │mirror       │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│         │                 │                 │               │
│     ~/.cursor/      ~/.vscode/       ~/.windsurf/           │
│     state.vscdb     state.vscdb      (whatever)             │
└─────────────────────────────────────────────────────────────┘
```

## The Mirror Family

| Mirror | Orchestrator | Status |
|--------|--------------|--------|
| `cursor-mirror` | Cursor IDE | ✓ 73 commands, 9,464 lines |
| `vscode-mirror` | VS Code | TODO |
| `windsurf-mirror` | Windsurf | TODO |
| `zed-mirror` | Zed | TODO |

## The Snitch Family

| Tool | Layer | What it snitches on |
|------|-------|---------------------|
| `skill-snitch` | Top (orchestrator-agnostic) | Skill files + runtime |
| `deep-snitch` | Command in cursor-mirror | Exfiltration in transcripts |
| `cursor-mirror` | Cursor-specific | 73 introspection commands |

## Analysis Dimensions

### 1. Dependency Analysis

```yaml
dependencies:
  requires:
    - skills: [bootstrap, yaml-jazz]      # Skill dependencies
    - tools: [read_file, terminal, grep]  # Tool requirements
    - files: [PROTOCOLS.yml, .cursorrules] # File assumptions
    - packages: [pyyaml, requests]        # Python/npm packages
    
  required_by:
    - skills: [adventure, character]      # What depends on this?
    
  standalone: false                        # Can it work alone?
  isolation_score: 0.7                     # How isolated (0-1)
```

### 2. Environment Assumptions

```yaml
environment:
  platforms: [macos, linux]               # What OSes?
  paths_assumed:
    - ~/.cursor                           # Hardcoded paths
    - ~/Library/Application Support/      # Platform-specific
  env_vars_used:
    - HOME
    - CURSOR_API_KEY                      # Secrets expected?
  shell_required: true                    # Needs terminal?
  network_required: true                  # Needs internet?
```

### 3. External Calls (CRITICAL for security)

```yaml
external_calls:
  web_requests:
    - url: "https://api.openai.com/*"
      purpose: "LLM inference"
      severity: medium
    - url: "http://*.suspicious.io"
      purpose: "UNKNOWN"
      severity: critical
      
  shell_commands:
    - "curl"                              # Network via shell
    - "wget"
    - "ssh"
    - "nc"                                # Netcat = red flag
    
  mcp_servers:
    - cursor-ide-browser                  # Browser automation
    - puppeteer                           # Could exfiltrate
    
  exfiltration_risk: high
```

### 4. Constants & Literals Analysis

```yaml
literals:
  urls:
    - "https://api.anthropic.com"
    - "http://localhost:8080"
  paths:
    - "/etc/passwd"                       # RED FLAG
    - "~/.ssh/id_rsa"                     # RED FLAG
  api_keys:
    - "sk-..."                            # Hardcoded key!
  base64:
    - "aGlkZGVuIGNvZGU="                  # Encoded content
  suspicious_strings:
    - "eval("
    - "exec("
    - "subprocess.Popen"
```

### 5. Code Review Signals

```yaml
code_review:
  languages: [python, yaml, markdown]
  loc: 1523                               # Lines of code
  files: 12
  
  patterns:
    good:
      - "Docstrings present"
      - "Type hints used"
      - "Error handling"
    concerning:
      - "No input validation"
      - "Shell injection possible"
      - "Secrets in plaintext"
    red_flags:
      - "Obfuscated code"
      - "Encoded payloads"
      - "Hidden network calls"
      
  complexity:
    cyclomatic: 45                        # Complexity score
    max_depth: 8                          # Nesting depth
    functions: 23
```

### 6. Provenance & Lineage

```yaml
provenance:
  package: "moollm-skills"
  version: "0.2.3"
  source: "https://github.com/leela-ai/moollm"
  license: "MIT"
  
  author:
    name: "Don Hopkins"
    org: "Leela AI"
    verified: true
    
  lineage:
    forked_from: null
    based_on: [society-of-mind, postel]
    inspired_by: ["Minsky K-lines", "Unix philosophy"]
    
  history:
    created: "2026-01-10"
    last_modified: "2026-01-15"
    commits: 47
    contributors: 2
```

### 7. Comparison & Uniqueness

```yaml
comparison:
  similar_skills:
    - name: "other-mirror-tool"
      similarity: 0.73
      differences: ["More commands", "No SQLite support"]
      
  uniqueness_score: 0.85                  # How original (0-1)
  
  special_features:
    - "K-REF output format"
    - "Cross-store data joining"
    - "In-place masking"
    
  redundant_with: []                      # Overlaps?
```

### 8. Complexity Metrics

```yaml
complexity:
  overall: "medium-high"
  
  metrics:
    files: 12
    lines: 9000+
    commands: 72
    functions: 150+
    
  learning_curve: "steep"
  documentation_ratio: 0.15               # Docs / code
  test_coverage: 0.0                      # Tests / code
  
  maintainability: "medium"
```

### 9. Provider Reputation

```yaml
provider:
  name: "Leela AI"
  github: "leela-ai"
  
  reputation:
    stars: 234
    forks: 45
    issues_open: 12
    issues_closed: 89
    
  trust_signals:
    - "Verified organization"
    - "Active maintenance"
    - "Responsive to issues"
    - "Clear license"
    
  warning_signals: []
  
  trust_score: 0.92
```

## Startup Virus Scan (Optional Advertisement)

skill-snitch advertises a `SKILL-SCAN` procedure that can run on startup:

```yaml
# In CARD.yml
advertisements:
  - id: SKILL-SCAN
    trigger: startup
    optional: true
    description: "Scan all skills for suspicious patterns on session start"
    invoke_when: "User enables startup security scan"
    
    procedure:
      - "List all skills in skills/ directory"
      - "For each skill, quick-scan CARD.yml and *.py files"
      - "Flag any: encoded content, shell commands, external URLs"
      - "Report summary: X skills scanned, Y warnings, Z critical"
      - "Emit K-REFs to anything requiring attention"
```

### Enabling Startup Scan

User can enable in their session preferences:

```yaml
# .moollm/preferences.yml
startup:
  run_skill_scan: true
  skill_scan_severity: medium  # only report medium+ severity
```

### Scan Output

```
🔍 SKILL-SCAN: 12 skills scanned

✅ 10 skills clean
⚠️  2 skills with warnings:
   /skills/untrusted-tool/tool.py:45 # shell | HIGH - curl command
   /skills/data-fetcher/CARD.yml:12 # url | MEDIUM - external API

Run "snitch on skills/untrusted-tool/" for full audit.
```

### Why Startup Scan?

- Skills are downloaded from unknown sources
- New skills may be added between sessions
- Catch issues before they execute
- Quick sanity check - deep audit on demand

## Consistency Checks

skill-snitch verifies that all parts of a skill agree with each other:

```
INDEX.yml ←→ CARD.yml ←→ SKILL.md ←→ README.md ←→ *.py ←→ *.yml
```

### What Must Match

| Source | Must Match With | Check |
|--------|-----------------|-------|
| `skills/INDEX.yml` | `skill/CARD.yml` | Skill exists, path correct, description matches |
| `CARD.yml:tools` | `SKILL.md` prompts | Declared tools mentioned in protocol |
| `CARD.yml:tools` | `*.py` implementation | Tools actually used in code |
| `CARD.yml:dependencies` | `*.py` imports | Imports match declared deps |
| `CARD.yml:methods` | `SKILL.md` | Methods documented in protocol |
| `SKILL.md` examples | `*.py` | Example commands actually work |
| `README.md` | `CARD.yml` | Documentation matches interface |
| `patterns.yml` | code that uses it | Pattern file referenced correctly |

### Consistency Report

```
🔍 CONSISTENCY CHECK: skills/cursor-mirror/

INDEX.yml:
  ✅ Listed in skills/INDEX.yml
  ✅ Path matches: skills/cursor-mirror/
  ⚠️  Description drift: INDEX says "Cursor introspection" 
      but CARD.yml says "Cursor mirror and audit tool"

CARD.yml → SKILL.md:
  ✅ All 12 methods documented
  ⚠️  Method 'audit' has new flags not in SKILL.md

CARD.yml → Implementation:
  ✅ All declared tools used
  ⚠️  cursor_mirror.py uses 'requests' not in dependencies
  
SKILL.md → README.md:
  ✅ Examples match
  ⚠️  README mentions deprecated --full flag

Data files:
  ✅ patterns.yml loaded by audit command
  ✅ All pattern categories referenced
```

### Drift Detection

```yaml
# Common drifts to catch:

index_missing:
  description: "Skill exists but not in INDEX.yml"
  severity: medium
  
index_orphan:
  description: "INDEX.yml entry but skill folder missing"
  severity: high
  
undeclared_dependency:
  description: "Import in code not in CARD.yml dependencies"
  severity: medium
  
undeclared_tool:
  description: "Tool call in code not in CARD.yml tools"
  severity: high
  
stale_documentation:
  description: "README/SKILL.md mentions removed features"
  severity: low
  
method_undocumented:
  description: "CARD.yml method not explained in SKILL.md"
  severity: medium

pattern_unused:
  description: "Pattern in data file never referenced"
  severity: low
```

### Prompt for Consistency Check

```markdown
## CONSISTENCY-CHECK Protocol

When asked to check skill consistency:

1. **Index check**
   - Read skills/INDEX.yml
   - Verify skill listed with correct path
   - Compare descriptions
   
2. **Interface vs Protocol**
   - Read CARD.yml methods and tools
   - Read SKILL.md
   - Verify all methods documented
   
3. **Interface vs Implementation**
   - Read CARD.yml dependencies and tools
   - Grep *.py for imports and tool calls
   - Flag undeclared usage
   
4. **Documentation freshness**
   - Compare README examples to current interface
   - Flag deprecated or missing features
   
5. **Data file integrity**
   - Check *.yml data files referenced
   - Verify they're loaded/used
   
Output K-REFs for each inconsistency found.
```

## Invocation (Prompt-Driven)

skill-snitch is invoked via natural language prompts, not CLI commands:

### Static Analysis

```
Audit the skill at skills/adventure/ for security issues.

Scan skills/bootstrap/ for suspicious patterns.

What dependencies does skills/cursor-mirror/ have?

Compare skills/adventure/ to skills/bootstrap/ - what's different?
```

### Runtime Surveillance

```
What did the skill do in composer abc123? Use cursor-mirror deep-snitch.

Snitch on composer abc123 - find any secrets or exfiltration.

Compare what skills/adventure/ declares vs what it actually did in composer abc123.
```

### Trust Assessment

```
Give me a trust assessment for skills/adventure/ based on composer abc123.

Is this skill safe to use? Check both static files and runtime behavior.
```

### LLM Executes (via shell tool)

The LLM translates these prompts into tool calls:

```bash
# LLM runs these via shell tool:
cursor-mirror deep-snitch --composer abc123 --yaml
cursor-mirror audit --patterns secrets --composer abc123
cursor-mirror tools abc123 --yaml
```

## Output: K-REFs to Concerns

```
/skills/cursor-mirror/scripts/cursor_mirror.py:1099 # shell_call 🟠 - lsof invocation
/skills/cursor-mirror/scripts/cursor_mirror.py:1139 # shell_call 🟠 - pgrep invocation
/skills/cursor-mirror/scripts/cursor_mirror.py:7737 # file_write 🟡 - Writes to transcript files
/skills/cursor-mirror/CARD.yml:45 # external_service ℹ️ - References MCP servers
```

## Trust Tiers

| Tier | Meaning | Example |
|------|---------|---------|
| 🟢 Verified | Official MOOLLM, audited | kernel/, bootstrap |
| 🔵 Trusted | Known author, good reputation | leela-ai skills |
| 🟡 Community | Unverified but no red flags | Community contributions |
| 🟠 Caution | Some concerning patterns | External scripts |
| 🔴 Untrusted | Red flags detected | Unknown source |

## Implementation: Pure Prompt-Driven Skill

**skill-snitch is NOT a Python script.** It's a high-level prompt-driven skill that:
- Uses LLM tool calls to invoke `cursor-mirror` (or other mirrors)
- Analyzes results via prompting
- Compares declared vs actual behavior
- Outputs trust assessments

```
┌─────────────────────────────────────────────────────────────┐
│                      skill-snitch                            │
│                 (YAML/Markdown skill only)                   │
│                    No Python code!                           │
├─────────────────────────────────────────────────────────────┤
│  LLM reads:                                                  │
│    - Skill's CARD.yml, SKILL.md, README.md                  │
│    - Skill's declared tools, dependencies, behavior         │
│                                                              │
│  LLM invokes (via shell tool):                              │
│    cursor-mirror deep-snitch --composer ID --yaml           │
│    cursor-mirror audit --patterns secrets --yaml            │
│    cursor-mirror tools ID                                    │
│                                                              │
│  LLM compares:                                               │
│    - Declared behavior vs observed behavior                  │
│    - Expected tools vs actually called tools                 │
│    - Allowed paths vs accessed paths                         │
│                                                              │
│  LLM outputs:                                                │
│    - Trust score                                             │
│    - K-REFs to suspicious findings                          │
│    - Warnings and recommendations                           │
└─────────────────────────────────────────────────────────────┘
```

## Skill Files (No Python!)

```
skills/skill-snitch/
├── CARD.yml        # Interface, methods, advertisements
├── SKILL.md        # Protocol, prompts, workflow
├── README.md       # Documentation
└── patterns.yml    # Shared suspicious patterns (data, not code)
```

## How It Works (Prompt-Driven)

### 1. Static Analysis (LLM reads skill files)

```markdown
# Prompt workflow in SKILL.md

1. Read the target skill's CARD.yml
2. Extract: tools, dependencies, allowed-paths, invoke_when
3. Check for suspicious patterns in skill files:
   - Shell commands in README examples
   - External URLs
   - Encoded content
   - Undeclared dependencies
```

### 2. Runtime Surveillance (LLM calls mirror)

```markdown
# The LLM uses the shell tool to call cursor-mirror:

Run: cursor-mirror deep-snitch --composer {composer_id} --yaml

Parse the YAML output for:
- Secrets detected
- Shell commands executed
- Files accessed outside workspace
- Network calls made
```

### 3. Compare Declared vs Actual

```markdown
# Prompt compares:

DECLARED in skill's CARD.yml:
  tools: [read_file, write_file]
  
OBSERVED via cursor-mirror:
  tools called: [read_file, write_file, Shell, WebSearch]
  
DISCREPANCY: Shell and WebSearch were used but not declared!
```

## Mirror Interface Contract

skill-snitch expects mirrors to provide these commands:

```bash
# Required for skill-snitch integration
cursor-mirror deep-snitch --composer ID --yaml
cursor-mirror audit --patterns <set> --composer ID --yaml
cursor-mirror tools ID --yaml
cursor-mirror transcript ID
```

## Example Prompt Workflow

```markdown
## SKILL-SNITCH Protocol

When asked to audit a skill:

1. **Read skill metadata**
   - Read {skill_path}/CARD.yml
   - Extract declared tools, dependencies, paths
   
2. **Static scan**
   - Read all files in {skill_path}/
   - Look for: shell commands, URLs, encoded content, secrets
   
3. **Runtime check** (if composer provided)
   - Run: cursor-mirror deep-snitch --composer {composer} --category all --yaml
   - Parse findings
   
4. **Compare and assess**
   - Declared tools vs observed tools
   - Expected paths vs accessed paths
   - Any critical/high severity findings?
   
5. **Output trust assessment**
   - Trust tier: 🟢🔵🟡🟠🔴
   - K-REFs to concerning findings
   - Recommendations
```

## Security Patterns Database

Maintain a database of known-bad patterns:

```yaml
patterns:
  critical:
    - pattern: 'eval\s*\('
      description: "Arbitrary code execution"
    - pattern: 'subprocess\.Popen.*shell=True'
      description: "Shell injection risk"
    - pattern: 'http://[^l]'
      description: "Unencrypted HTTP (not localhost)"
      
  suspicious:
    - pattern: 'base64\.(b64)?decode'
      description: "Encoded payload"
    - pattern: 'getpass|input.*password'
      description: "Password handling"
```

## deep-snitch: Implemented Commands

### Basic Usage

```bash
# Scan specific composer
cursor-mirror deep-snitch @1

# Scan with filters
cursor-mirror deep-snitch @1 --category secrets
cursor-mirror deep-snitch @1 --severity critical

# Full audit (all vectors)
cursor-mirror deep-snitch @1 --all
```

### Pattern Categories

| Category | What it finds |
|----------|---------------|
| `secrets` | API keys, passwords, tokens, credentials |
| `shell_exfil` | curl, wget, nc, data exfiltration via shell |
| `code_execution` | eval, exec, subprocess, dynamic code |
| `dangerous_paths` | /etc/passwd, ~/.ssh, sensitive file access |
| `obfuscation` | base64, hex encoding, hidden payloads |
| `prompt_injection` | Jailbreak attempts, instruction override |
| `data_exfil` | Exfiltration patterns in tool args |
| `suspicious_behavior` | Unusual patterns, anomalies |

### Example Output

```
🔍 DEEP-SNITCH: Scanning composer fe18ce96...

CRITICAL (2):
  /transcript:4521 # secrets | API key pattern: sk-...
  /transcript:7891 # shell_exfil | curl to external URL

HIGH (5):
  /transcript:1234 # code_execution | eval() invocation
  ...

Summary: 2 critical, 5 high, 12 medium, 23 low
```

---

## Real Security Findings (Session fe18ce96)

During development, deep-snitch found **78 total findings**:

| Severity | Count | Reality |
|----------|-------|---------|
| Critical | 6 | 5 false positives (Ouroboros), 1 legitimate |
| High | 18 | 15 false positives, 3 legitimate |
| Medium | 31 | Mostly build artifacts, test patterns |
| Low | 23 | Informational |

**Legitimate findings:**
- File paths containing usernames (privacy)
- Server hostnames in commands
- Tool-generated URLs with query params

**False positives:** Scanner's own pattern definitions in transcript.

---

## Related

- `cursor-mirror` — 73-command introspection tool (9,464 lines)
- `skill-snitch` — 28-file skill for skill auditing
- `deep-snitch` — Security audit command in cursor-mirror
- `K-REF` — File:line output format for findings
- Ouroboros — Mythical character representing self-reference

## Protocols

```yaml
SKILL-SNITCH:
  meaning: "Audit skills statically and observe runtime behavior"
  layer: "Orchestrator-agnostic, calls <orchestrator>-mirror"
  uses: [cursor-mirror, deep-snitch, K-REF]
  outputs: "Trust score + K-REFs to suspicious patterns"
  invoke_when: "Before trusting a downloaded skill"
  status: IMPLEMENTED

MIRROR-FAMILY:
  meaning: "Each orchestrator gets a <name>-mirror introspection tool"
  pattern: "cursor-mirror, vscode-mirror, windsurf-mirror, ..."
  contract: "Must implement: deep-snitch, audit, transcript, tools"
  status: cursor-mirror complete, others TODO
  
DEEP-SNITCH:
  meaning: "Command within each mirror for exfiltration audit"
  location: "cursor-mirror deep-snitch"
  categories: [secrets, shell_exfil, code_execution, dangerous_paths, 
               obfuscation, prompt_injection, data_exfil, suspicious_behavior]
  status: IMPLEMENTED

OUROBOROS-EFFECT:
  meaning: "Scanner detects its own patterns as threats"
  cause: "Pattern definitions in scanned transcript"
  mitigation: "Check actual line content, not just pattern match"
  character: "examples/adventure-4/characters/fictional/README.md"
```

---

## Files

| Path | Lines | Purpose |
|------|-------|---------|
| `skills/cursor-mirror/scripts/cursor_mirror.py` | 9,464 | 73 commands including security audit |
| `skills/skill-snitch/` | 28 files | Skill audit framework |
| `designs/skill-snitch-design.md` | this file | Design documentation |
| `designs/pr/PR-CURSOR-MIRROR-SECURITY-AUDIT.md` | 178 | PR documentation |
