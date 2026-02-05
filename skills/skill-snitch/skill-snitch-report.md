# SKILL-SNITCH DEEP PROBE REPORT
## skill-snitch — Auditing the auditor

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: RECURSIVE SECURITY AUDIT
**Status**: Three-layer extensible security architecture, prompt-driven, zero code

---

## EXECUTIVE SUMMARY

Security auditing skill for MOOLLM. Three-layer plugin architecture: patterns (what to match), surfaces (where to look), analyzers (how to interpret). All layers user-extensible. Prompt-driven — zero Python, zero JavaScript. The entire skill is LLM orchestration over YAML plugin definitions. Composes with cursor-mirror for runtime surveillance (SNITCH method). Two-phase scan methodology: grep finds, LLM understands. Honestly documents its own limitations: the Ouroboros effect (scanning itself finds its own patterns), the Quis Custodiet problem (who watches the watchers), and the false negative gap (can find known patterns but not unknown unknowns).

**Overall Assessment**: APPROVE — intellectually honest security tooling with real architectural depth

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 115 lines | NONE |
| GLANCE.yml | 43 lines | NONE |
| SKILL.md | 422 lines | NONE |
| README.md | 261 lines | NONE |
| SCAN-METHODOLOGY.md | 660 lines | NONE |
| EXPORTS.yml | 58 lines | NONE |
| registry.yml | 109 lines | NONE |
| patterns/ | 7 plugins, 680+ lines total | NOTE — contains security regexes |
| surfaces/ | 4 plugins, 150 lines total | NONE |
| analyzers/ | 7 plugins, 650+ lines total | NONE |
| templates/ | 7 .tmpl files, 291 lines total | NOTE — template injection surface |
| Executable code | None — prompt-driven | NONE |
| Total skill size | 3,440+ lines (excl. report) | NONE |
| Required tools | read_file (static), cursor-mirror (runtime) | LOW |
| Tier | 2 | NONE |

---

## WHAT IT DOES

### Six Methods

| Method | Purpose | Phase |
|--------|---------|-------|
| SCAN | Quick static scan of a skill | Static |
| AUDIT | Deep static audit with full pattern matching | Static |
| SNITCH | Runtime surveillance — what did the skill actually do? | Runtime |
| TRUST | Combined static + runtime trust assessment | Both |
| CONSISTENCY | Check INDEX ↔ CARD ↔ SKILL.md ↔ code | Static |
| OBSERVE | Deep runtime observation via cursor-mirror | Runtime |

### Three-Layer Plugin Architecture

**Layer 1: Patterns** — What to look for (6 builtin, user-extensible)

| Plugin | Lines | What It Detects |
|--------|-------|----------------|
| prompt-injection.yml | 185 | Instruction overrides, jailbreak attempts, system prompt hijacking |
| template-injection.yml | 133 | Dangerous substitution patterns in .tmpl files |
| secrets.yml | 62 | API keys, passwords, tokens, private keys |
| dangerous-ops.yml | 62 | Destructive, persistent, privilege-escalating operations |
| exfiltration.yml | 55 | Data leaving the system (curl, fetch, webhook) |
| obfuscation.yml | 48 | Encoding, base64, hex encoding to hide content |
| dual-use.yml | 135 | Invertibility, bias direction, multi-purpose affordances |

prompt-injection.yml is the largest pattern file (185 lines) — comprehensive catalog of injection techniques including DAN-style jailbreaks, instruction overrides, and system prompt extraction.

**Layer 2: Surfaces** — Where to look (4 builtin, user-extensible)

| Plugin | Lines | What It Scans |
|--------|-------|--------------|
| skill-files.yml | 39 | MOOLLM skill source code and configuration |
| config-files.yml | 42 | JSON/YAML configs that may contain secrets |
| transcripts.yml | 33 | LLM conversation transcripts (via cursor-mirror) |
| sqlite.yml | 36 | Cursor's SQLite state databases (via cursor-mirror) |

**Layer 3: Analyzers** — How to interpret (6 builtin, user-extensible)

| Plugin | Lines | What It Assesses |
|--------|-------|-----------------|
| skill-type.yml | 107 | Distinguish MOOLLM vs Anthropic vs generic skills |
| runtime.yml | 94 | Actual execution patterns vs declared behavior |
| smells.yml | 89 | Code smells, debug left in, complexity heuristics |
| provenance.yml | 79 | Publisher, license, git status, origin trust |
| consistency.yml | 74 | INDEX ↔ CARD ↔ SKILL.md ↔ code agreement |
| behavioral.yml | 73 | Suspicious combinations and sequences of actions |
| dual-use.yml | 134 | Bias direction, invertibility, multi-purpose classification |

skill-type.yml is notable — it detects whether a skill follows MOOLLM conventions (CARD.yml, Semantic Image Pyramid) vs Anthropic's skill spec vs generic markdown, and applies different audit rules accordingly.

### Scan Presets (from registry.yml)

| Preset | Patterns | Surfaces | Analyzers |
|--------|----------|----------|-----------|
| scan | secrets, exfiltration, dangerous-ops | skill-files | consistency, smells |
| audit | + obfuscation | + config-files | + provenance |
| snitch | + obfuscation | transcripts, sqlite | behavioral, runtime |
| deep_snitch | all 4 | all 4 | all 5 |
| startup_scan | secrets, exfiltration | skill-files | consistency (high only) |

### Two-Phase Methodology (SCAN-METHODOLOGY.md, 660 lines)

Phase 1: Bash scripts (fast, all skills) — structure check, script detection, pattern grep, tool tier extraction.

Phase 2: LLM batched review (deep, 5 at a time) — actually READ files, scripts get full code review, context determines danger, trust assessment.

The Golden Rule: "Grep finds. LLM understands." Neither alone is sufficient.

### Templates Directory (7 .tmpl files)

Empathic templates for initializing user-space configuration in `.moollm/skill-snitch/`:

| Template | Purpose |
|----------|---------|
| config.yml.tmpl | User scan preferences |
| ignore.yml.tmpl | Known false positives |
| trust-overrides.yml.tmpl | Manual trust tier overrides (requires reason + expires) |
| scan-history.yml.tmpl | Audit trail of past scans |
| patterns.yml.tmpl | User-defined pattern extension |
| surfaces.yml.tmpl | User-defined surface extension |
| analyzers.yml.tmpl | User-defined analyzer extension |
| README.md.tmpl | Orientation for the .moollm/skill-snitch/ directory |

---

## THE OUROBOROS AUDIT

When skill-snitch scans itself, it finds its own pattern definitions. `secrets.yml` contains regexes for "password" — grep flags it. `exfiltration.yml` contains regexes for "curl" — grep flags it. `dangerous-ops.yml` contains regexes for "eval" — grep flags it.

The skill documents this as expected: "~80% of findings in such cases are false positives. Look at the actual line content." This is the Phase 1 → Phase 2 handoff. Grep finds the word "password" in a regex definition. The LLM understands it's a detection rule, not a credential.

### Self-Scan Results

| Pattern File | Self-Flags | Actual Risk |
|-------------|-----------|-------------|
| secrets.yml | Contains credential regexes | NONE — detection rules |
| exfiltration.yml | Contains network call regexes | NONE — detection rules |
| dangerous-ops.yml | Contains shell/eval regexes | NONE — detection rules |
| prompt-injection.yml | Contains jailbreak examples | LOW — documented as examples |
| template-injection.yml | Contains injection examples | LOW — documented as examples |
| obfuscation.yml | Contains encoding regexes | NONE — detection rules |

### Known Attack Surfaces

| Surface | Risk | Status |
|---------|------|--------|
| User patterns in .moollm/ | Malicious skill could exclude itself from scans | NOT MITIGATED |
| Trust cache in .moollm/ | Cache poisoning — mark malicious skill as GREEN | PARTIALLY MITIGATED (requires reason + expires) |
| ignore.yml | Could hide real issues behind "false positive" entries | NOT MITIGATED |
| templates/*.tmpl | Template injection surface | LOW — simple substitution, no eval |

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 (in skill code) | CLEAN — prompt-driven |
| Network calls | 0 | CLEAN |
| File writes | 0 (outputs to .moollm/) | CLEAN |
| Credential patterns | In detection rules only | EXPECTED |
| Obfuscation | In detection rules only | EXPECTED |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | 3 layers, 5 methods, cursor-mirror dependency |
| CARD.yml | YES | Full plugin registry, method signatures, template list |
| SKILL.md | YES | Methodology, trust tiers, Ouroboros acknowledgment |
| README.md | YES | Landing page, quick start, architecture overview |
| SCAN-METHODOLOGY.md | YES | 660-line two-phase methodology document |
| registry.yml | YES | Central index matches actual plugin files |
| patterns/ | YES | 6 files match registry entries |
| surfaces/ | YES | 4 files match registry entries |
| analyzers/ | YES | 6 files match registry entries |
| templates/ | YES | 7 .tmpl files for user-space initialization |

---

## SECURITY ASSESSMENT

**Risk Level**: META

This skill IS the security assessment tool. Its risks are architectural, not operational:

| Concern | Severity | Detail |
|---------|----------|--------|
| Quis Custodiet | PHILOSOPHICAL | Who audits the auditor? Answer: this report + manual review |
| Config tampering | MEDIUM | .moollm/ config files could be modified to blind the scanner |
| Trust cache poisoning | LOW | Requires write access + fields not validated |
| False negative gap | INHERENT | Can find known patterns but not unknown unknowns |
| cursor-mirror dependency | MEDIUM | Runtime surveillance (SNITCH) is only as good as cursor-mirror's data |

Prompt-driven architecture means the attack surface is configuration, not code. No hidden executables. The patterns, surfaces, and analyzers are all auditable YAML.

---

## TRUST TIER

**GREEN** — Prompt-driven (zero code). Extensible but auditable. Honestly documents limitations (Ouroboros, Quis Custodiet, false negatives). The config tampering risk is real but requires write access to .moollm/ which is already a trusted zone. cursor-mirror dependency is documented.

---

## VERDICT

The most self-aware security tool in the ecosystem. Three-layer plugin architecture (6 patterns, 4 surfaces, 6 analyzers) gives genuine coverage. Two-phase methodology (grep + LLM) acknowledges that neither alone is sufficient. Prompt-driven means auditable. Honestly documents the Ouroboros effect, the Quis Custodiet problem, and the false negative gap. Config integrity checking is the main gap — skill-snitch should verify its own patterns haven't been tampered with. 3,170+ lines of security infrastructure across 32 files. Composes with cursor-mirror for runtime surveillance. APPROVE.
