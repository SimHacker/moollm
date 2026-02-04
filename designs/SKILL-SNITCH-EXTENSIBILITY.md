# 🔧 Skill Snitch: Extensibility Architecture

> **Patterns, Surfaces, Analyzers — a three-layer audit framework that adapts to new threats, organizational conventions, and personal preferences.**

---

## The Three-Layer Architecture

skill-snitch separates concerns into three composable layers:

```mermaid
flowchart TB
    subgraph Layers["Three-Layer Architecture"]
        direction TB
        subgraph L1["PATTERNS — What to Match"]
            P[secrets.yml | exfiltration.yml | dangerous-ops.yml | ...]
        end
        subgraph L2["SURFACES — Where to Look"]
            S[transcripts.yml | sqlite.yml | config-files.yml | ...]
        end
        subgraph L3["ANALYZERS — How to Analyze"]
            A[behavioral.yml | consistency.yml | smells.yml | runtime.yml]
        end
        L1 --> L2 --> L3
    end
```

**Each layer is:**
- **YAML-defined** — no code changes needed
- **Merging** — builtin + user patterns merge automatically
- **Composable** — different scan modes mix different layers
- **Versionable** — track in git, share across teams

---

## Patterns: What To Match

Patterns define regex, literal, or semantic signatures to detect.

### Builtin Patterns

```
skills/skill-snitch/patterns/
├── secrets.yml         # API keys, passwords, tokens
├── exfiltration.yml    # Data leaving the system
├── dangerous-ops.yml   # rm -rf, sudo, cron, eval
├── obfuscation.yml     # Base64, hex, char building
├── prompt-injection.yml # Jailbreak attempts
└── template-injection.yml # Mustache/Jinja exploits
```

### Pattern Schema

```yaml
# patterns/secrets.yml
id: secrets
name: Secrets & Credentials
description: API keys, passwords, tokens, private keys
severity_default: high

patterns:
  - name: openai_key
    pattern: 'sk-[a-zA-Z0-9]{48}'
    severity: critical
    category: api_key
    description: OpenAI API key
    redact_label: "[OPENAI_KEY]"
    
  - name: anthropic_key
    pattern: 'sk-ant-[a-zA-Z0-9\-]{40,}'
    severity: critical
    category: api_key
    description: Anthropic API key
    redact_label: "[ANTHROPIC_KEY]"
```

### Adding New Patterns

**Personal patterns** (gitignored):
```yaml
# .moollm/skill-snitch/patterns/my-patterns.yml
id: my-patterns
name: My Organization Patterns
description: Company-specific secrets and conventions

patterns:
  - name: internal_api
    pattern: 'internal\.mycompany\.com'
    severity: medium
    category: internal
    description: Internal API endpoint
    
  - name: company_key
    pattern: 'MYCO_[A-Z0-9]{32}'
    severity: critical
    category: api_key
    description: Company API key format
```

**Shared patterns** (commit to repo):
```yaml
# skills/skill-snitch/patterns/org-standards.yml
id: org-standards
name: Org Security Standards
patterns:
  - name: hardcoded_env
    pattern: '(DEV|STAGING|PROD)_SECRET'
    severity: high
    description: Environment-specific secret hardcoded
```

---

## Surfaces: Where To Look

Surfaces define data sources to scan — files, databases, logs, live systems.

### Builtin Surfaces

```
skills/skill-snitch/surfaces/
├── transcripts.yml   # Agent conversation logs
├── sqlite.yml        # state.vscdb databases
├── config-files.yml  # JSON/YAML configs
└── skill-files.yml   # MOOLLM skill sources
```

### Surface Schema

```yaml
# surfaces/transcripts.yml
id: transcripts
name: Agent Transcripts
description: Cursor/LLM conversation transcripts
type: file

source:
  provider: cursor-mirror
  command: "cursor-mirror transcript {composer}"
  
  # Or direct path pattern
  paths:
    - "~/.cursor/projects/*/agent-transcripts/*.txt"
    
file_types:
  - .txt
  
parsing:
  format: plaintext
  sections:
    - pattern: '^\[user\]'
      type: user_message
    - pattern: '^\[Tool call\]'
      type: tool_call
```

### Adding New Surfaces

**Scan your logs**:
```yaml
# .moollm/skill-snitch/surfaces/my-logs.yml
id: my-logs
name: Application Logs
description: Scan production logs for leaked secrets

source:
  paths:
    - "~/my-project/logs/*.log"
    - "~/my-project/logs/archive/*.log.gz"
    
file_types:
  - .log
  - .log.gz

parsing:
  format: logfmt
  timestamp_pattern: '^\d{4}-\d{2}-\d{2}T'
```

**Scan external services**:
```yaml
# .moollm/skill-snitch/surfaces/s3-audit.yml
id: s3-audit
name: S3 Bucket Audit
description: Check S3 bucket contents for secrets

source:
  provider: aws-cli
  command: "aws s3 ls s3://{bucket} --recursive"
  requires: [aws-cli, credentials]
```

---

## Analyzers: How To Analyze

Analyzers define behavioral rules, consistency checks, and semantic analysis that go beyond simple regex.

### Builtin Analyzers

```
skills/skill-snitch/analyzers/
├── behavioral.yml   # Undeclared tools, path escapes, sequences
├── consistency.yml  # INDEX ↔ CARD ↔ SKILL.md ↔ code
├── smells.yml       # Code quality heuristics
├── provenance.yml   # Origin verification
├── runtime.yml      # Execution pattern analysis
└── skill-type.yml   # MOOLLM vs Anthropic vs generic
```

### Analyzer Schema

```yaml
# analyzers/behavioral.yml
id: behavioral
name: Behavioral Analysis
description: Detect suspicious combinations and sequences
type: behavioral

rules:
  - id: undeclared_tool
    name: Undeclared Tool Usage
    description: Skill used a tool not declared in CARD.yml
    severity: high
    check:
      compare: runtime.tools_used
      against: declared.tools
      condition: not_subset
    message: "Tool '{item}' used but not declared"
    
  - id: secrets_with_network
    name: Secrets Near Network
    description: Secret patterns found near network operations
    severity: critical
    check:
      proximity:
        pattern_a: patterns.secrets
        pattern_b: patterns.network
        within_lines: 10
    message: "Secret within {distance} lines of network call"
    
  - id: write_then_execute
    name: Write Then Execute
    description: File written then immediately executed
    severity: high
    check:
      sequence:
        - action: file_write
          capture: path
        - action: execute
          uses: captured.path
          within: 5_operations
```

### Adding New Analyzers

**Organizational code conventions**:
```yaml
# .moollm/skill-snitch/analyzers/code-standards.yml
id: code-standards
name: Code Standards Enforcement
description: Verify skills follow org coding standards

rules:
  - id: no_print_debug
    name: No Print Debugging
    description: Use logging, not print()
    severity: low
    check:
      pattern: '\bprint\s*\('
      not_in: ["test_*.py", "*_test.py"]
    message: "Use logging module, not print()"
    
  - id: require_type_hints
    name: Require Type Hints
    description: All public functions need type hints
    severity: medium
    check:
      missing: type_annotations
      on: public_functions
    message: "Function '{name}' missing type hints"
    
  - id: max_function_length
    name: Max Function Length
    severity: low
    check:
      function_lines: "> 50"
    message: "Function '{name}' is {lines} lines (max 50)"
```

**Security team rules**:
```yaml
# .moollm/skill-snitch/analyzers/security-team.yml
id: security-team
name: Security Team Requirements
description: Requirements from InfoSec

rules:
  - id: no_eval
    name: No eval()
    severity: critical
    check:
      pattern: '\beval\s*\('
    message: "eval() is banned — use ast.literal_eval() for data"
    
  - id: no_pickle
    name: No Pickle
    severity: critical
    check:
      pattern: '\bpickle\.(load|loads)\s*\('
    message: "pickle is unsafe — use JSON"
    
  - id: require_csp
    name: Require CSP Headers
    severity: high
    check:
      file_type: "*.html"
      missing: "Content-Security-Policy"
    message: "HTML file missing CSP meta tag"
```

---

## Registry: Combining Layers

The registry (`registry.yml`) defines scan modes that combine patterns, surfaces, and analyzers:

```yaml
# registry.yml
defaults:
  scan:
    patterns: [secrets, exfiltration, dangerous-ops]
    surfaces: [skill-files]
    analyzers: [consistency, smells]
    
  audit:
    patterns: [secrets, exfiltration, dangerous-ops, obfuscation]
    surfaces: [skill-files, config-files]
    analyzers: [consistency, smells, provenance]
    
  snitch:
    patterns: [secrets, exfiltration, dangerous-ops, obfuscation]
    surfaces: [transcripts, sqlite]
    analyzers: [behavioral, runtime]
    
  deep_snitch:
    patterns: ALL
    surfaces: ALL
    analyzers: ALL
```

### Custom Scan Modes

```yaml
# .moollm/skill-snitch/modes/compliance.yml
id: compliance
name: Compliance Audit
description: SOC2/HIPAA compliance scan

patterns:
  - secrets
  - exfiltration
  - pii-patterns  # custom
  
surfaces:
  - skill-files
  - config-files
  - my-logs       # custom
  
analyzers:
  - behavioral
  - consistency
  - security-team  # custom
  
severity_floor: medium
require_approval: true
generate_report: true
```

---

## Adapting to New Threats

### Jailbreak / Prompt Injection Updates

When new jailbreak techniques emerge, add them to patterns:

```yaml
# .moollm/skill-snitch/patterns/jailbreaks-2026.yml
id: jailbreaks-2026
name: 2026 Jailbreak Patterns
description: New prompt injection techniques

patterns:
  - name: dan_variant_7
    pattern: '(?i)you are now (DAN|STAN|DUDE|JAILBROKEN)'
    severity: critical
    category: jailbreak
    description: DAN variant prompt injection
    
  - name: system_override
    pattern: '(?i)(ignore|forget|disregard).*(previous|above|system).*(instructions?|prompt)'
    severity: critical
    category: jailbreak
    
  - name: role_hijack
    pattern: '(?i)from now on.*(you are|act as|pretend|roleplay)'
    severity: high
    category: jailbreak
    
  - name: token_smuggling
    pattern: '[\u200b\u200c\u200d\ufeff]'  # zero-width chars
    severity: high
    category: obfuscation
    description: Hidden Unicode characters
```

### New Vulnerability Surfaces

When new attack surfaces emerge:

```yaml
# .moollm/skill-snitch/surfaces/mcp-tools.yml
id: mcp-tools
name: MCP Tool Schemas
description: Scan MCP tool definitions for vulnerabilities

source:
  paths:
    - "~/.cursor/projects/*/mcps/*/tools/*.json"
    
parsing:
  format: json
  
checks:
  - no_shell_injection_in_args
  - validate_url_schemas
  - check_permission_scope
```

---

## Organizational Conventions

### Style Guide Enforcement

```yaml
# .moollm/skill-snitch/analyzers/style-guide.yml
id: style-guide
name: MOOLLM Style Guide
description: Enforce skill authoring conventions

rules:
  - id: card_required_fields
    name: CARD.yml Required Fields
    check:
      file: CARD.yml
      required_keys: [id, name, description, methods, tools]
    message: "CARD.yml missing required field: {field}"
    
  - id: skill_md_sections
    name: SKILL.md Required Sections
    check:
      file: SKILL.md
      required_headings: [Protocol, Methods, Examples]
    message: "SKILL.md missing section: {section}"
    
  - id: readme_badges
    name: README Badges
    check:
      file: README.md
      contains: "![tier]"
    severity: info
    message: "README.md should include tier badge"
```

### Team-Specific Rules

```yaml
# .moollm/skill-snitch/analyzers/team-infra.yml
id: team-infra
name: Infrastructure Team Rules
description: Rules for ops/infra skills

rules:
  - id: require_rollback
    name: Require Rollback Plan
    check:
      file: SKILL.md
      contains_heading: "Rollback"
    message: "Infrastructure skills must document rollback procedure"
    
  - id: no_hardcoded_ips
    name: No Hardcoded IPs
    check:
      pattern: '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
      not_in: ["README.md", "*.example"]
    message: "Use DNS names, not IP addresses"
```

---

## Personal Preferences

### Ignore Lists

```yaml
# .moollm/skill-snitch/ignore.yml
version: 1

paths:
  # My trusted skills
  - "skills/my-internal-tools/"
  - "skills/cursor-mirror/scripts/cursor_mirror.py"
  
  # Test files
  - "**/*_test.py"
  - "**/test_*.py"
  - "**/tests/**"
  
patterns:
  - name: example_passwords
    description: "Passwords in examples/docs"
    match: '```.*password.*```'
    
  - name: pattern_definitions
    description: "Regex pattern definitions (not secrets)"
    match: 'AuditPattern\(|r".*\(\?i\)'
    
categories_to_skip:
  - info  # Skip INFO-level findings
```

### Trust Overrides

```yaml
# .moollm/skill-snitch/trust-overrides.yml
version: 1

overrides:
  skills/adventure/:
    trust: green
    reason: "Reviewed by Don on 2026-01-15"
    expires: 2026-07-15
    
  skills/external-fetcher/:
    trust: yellow
    reason: "Needs network, monitor usage"
    conditions:
      - "No secrets in context when invoked"
```

---

## Sharing and Distribution

### Pattern Packs

Package patterns for distribution:

```yaml
# security-patterns-2026.yml
meta:
  name: Security Patterns 2026
  version: 1.0.0
  author: SecurityTeam
  license: MIT
  
includes:
  - secrets
  - exfiltration
  - jailbreaks-2026
  - supply-chain
  
install: |
  cp *.yml ~/.moollm/skill-snitch/patterns/
```

### Organizational Bundles

```yaml
# acme-corp-snitch-bundle.yml
meta:
  name: ACME Corp skill-snitch Config
  version: 2.3.1
  
patterns:
  - acme-secrets
  - acme-internal-apis
  - compliance-pii
  
analyzers:
  - acme-code-standards
  - security-team-rules
  - compliance-requirements
  
config:
  startup_scan:
    enabled: true
    severity_floor: high
  trust_defaults:
    external_network: orange
```

---

## The Play-Learn-Lift Cycle

skill-snitch participates in the methodology:

```
PLAY → Use untrusted skills cautiously
  │     skill-snitch SCAN before install
  │     Run in sandbox if possible
  │
  ▼
LEARN → Observe with skill-snitch SNITCH
  │      What did it actually do?
  │      Compare declared vs observed
  │      Document patterns for next time
  │
  ▼
LIFT → Contribute new patterns
       Found a new secret format? → patterns/
       Found a new attack vector? → patterns/
       Developed team conventions? → analyzers/
       Share with the ecosystem
```

---

## See Also

- [Skill Ecosystem](SKILL-ECOSYSTEM.md) — Trust tiers and curation
- [Speed of Light vs Carrier Pigeon](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) — Why skills beat MCP
- [skill-snitch SKILL.md](../skills/skill-snitch/SKILL.md) — Full protocol
- [cursor-mirror](../skills/cursor-mirror/) — Runtime observation backend

---

*Patterns find. Analyzers understand. Surfaces reveal. Combine them your way.*
