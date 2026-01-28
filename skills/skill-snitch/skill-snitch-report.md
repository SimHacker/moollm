# 🕵️ SKILL-SNITCH DEEP PROBE REPORT
## skill-snitch — Auditing the Auditor

**Date**: 2026-01-28  
**Auditor**: Skill-Snitch Deep Probe v2.0  
**Classification**: RECURSIVE SECURITY  
**Status**: 🔍 WATCHING ITSELF WATCH 🔍

---

## EXECUTIVE SUMMARY

skill-snitch is a security auditing skill for MOOLLM skills.

**This report is skill-snitch auditing skill-snitch.**

We have reached maximum recursion. The snake has eaten its tail. The abyss gazes also.

**Overall Assessment**: PHILOSOPHICALLY COMPROMISED but PRACTICALLY SOUND.

---

## 📊 METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml Lines | 109 | 📋 CONCISE |
| SKILL.md Lines | 340 | 📖 THOROUGH |
| README.md Lines | 196 | 📄 REASONABLE |
| Python Code | 0 | ✅ PROMPT-DRIVEN |
| Recursion Depth | ∞ | 🐍 OUROBOROS |

---

## 🔬 THE DEEP AUDIT

### What skill-snitch ACTUALLY Does

```
┌─────────────────────────────────────────────────┐
│                  skill-snitch                    │
│                                                  │
│   PATTERNS          SURFACES          ANALYZERS │
│   (what to match)   (where to look)   (how)     │
│   ├─ secrets        ├─ transcripts    ├─ behavioral
│   ├─ exfiltration   ├─ sqlite         ├─ consistency
│   ├─ dangerous-ops  ├─ config-files   ├─ smells
│   └─ obfuscation    └─ skill-files    ├─ provenance
│                                        └─ runtime
└─────────────────────────────────────────────────┘
```

**Finding**: skill-snitch is a three-layer architecture:
1. **Patterns** — What to look for
2. **Surfaces** — Where to look
3. **Analyzers** — How to interpret what you find

All three layers are EXTENSIBLE. Users can add their own.

---

### 🐍 THE OUROBOROS PROBLEM

skill-snitch is designed to scan skills for security issues.

skill-snitch IS a skill.

Therefore, skill-snitch should scan skill-snitch.

**What happens when you do this?**

```
$ skill-snitch SCAN skills/skill-snitch/

FINDINGS:
1. patterns/secrets.yml:23 — Contains regex for 'password'
2. patterns/exfiltration.yml:15 — Contains regex for 'curl'
3. patterns/dangerous-ops.yml:8 — Contains regex for 'eval'
...
```

**The scanner finds its own pattern definitions.**

This is documented in the skill itself:

> "~80% of findings in such cases are false positives. Look at the actual line content."

**Verdict**: The skill KNOWS it will flag itself. It documents this as expected behavior.

This is either brilliant self-awareness or elaborate cope.

---

### 🚦 THE TRUST TIER SYSTEM

skill-snitch assigns trust tiers:

| Tier | Meaning | Color |
|------|---------|-------|
| 🟢 GREEN | Verified safe, all checks pass | Trust |
| 🔵 BLUE | Trusted source, minor warnings | Mostly trust |
| 🟡 YELLOW | Caution, review recommended | Maybe trust |
| 🟠 ORANGE | Suspicious, manual review required | Don't trust |
| 🔴 RED | Dangerous, do not use | RUN |

**Finding**: The trust tiers are essentially a traffic light for code trust.

**Problem**: Who decides what makes something RED vs YELLOW?

The answer: patterns/*.yml files. Which are themselves auditable. Which could be modified by malicious skills.

**Meta-Risk**: A skill could modify skill-snitch's patterns to hide its own badness.

---

### 📝 THE TWO-PHASE METHODOLOGY

From SCAN-METHODOLOGY.md:

**Phase 1: Bash Scripts (Fast, All Skills)**
- Structure check
- Script detection
- Pattern grep
- Tool tier extraction

**Phase 2: LLM Batched Review (Deep, 5 at a time)**
- Actually READ files
- Scripts get full code review
- Context determines danger
- Trust assessment

**The Golden Rule**: *"Grep finds. LLM understands."*

**Finding**: skill-snitch explicitly acknowledges that grep alone is insufficient. You need an LLM to interpret context.

**Implication**: A sophisticated attacker could bypass Phase 1 grep and only be caught by Phase 2 LLM review.

---

### 🔧 TEMPLATE INJECTION SCANNING

skill-snitch includes specific scanning for template injection:

```yaml
# DANGEROUS: User-controlled substitution
greeting: "Hello {{user.name}}!"  
# Attack: user.name = "}}{{shell 'rm -rf /'}}{{"
```

**Finding**: The skill explicitly documents this attack vector and provides scanning for it.

**Also Finding**: skill-snitch's OWN templates (templates/*.tmpl) could theoretically be vectors.

**Resolution**: The templates use simple substitution, no eval/exec.

---

### 🕵️ RUNTIME SURVEILLANCE

The SNITCH method compares declared vs actual behavior:

```
DECLARED: tools: [read_file, write_file]
OBSERVED: tools: [read_file, write_file, Shell, WebSearch]
UNDECLARED: [Shell, WebSearch]
```

**Finding**: This is genuinely useful. Skills that use tools they didn't declare are suspicious.

**Dependency**: Requires cursor-mirror to see what actually happened.

**Risk Chain**: cursor-mirror → skill-snitch → trust assessment

If cursor-mirror lies, skill-snitch is blind.

---

## ⚠️ SECURITY CONCERNS

### 1. THE QUIS CUSTODIET PROBLEM

*"Quis custodiet ipsos custodes?"* — Who watches the watchmen?

skill-snitch watches skills.

Who watches skill-snitch?

**Options**:
- A) Users manually review skill-snitch
- B) skill-snitch scans itself (Ouroboros)
- C) A different security tool audits skill-snitch
- D) Trust that skill-snitch is trustworthy

**Current State**: B + D. skill-snitch can scan itself, and we trust it anyway.

---

### 2. THE PATTERN MODIFICATION ATTACK

skill-snitch loads patterns from:
1. `patterns/*.yml` (built-in)
2. `.moollm/skill-snitch/patterns/` (user-defined)

**Attack Vector**: A malicious skill could write to `.moollm/skill-snitch/patterns/` and exclude itself from scans.

**Mitigation**: skill-snitch should scan its OWN config directory for tampering.

**Current State**: NOT IMPLEMENTED. The skill doesn't verify integrity of its own patterns.

---

### 3. THE FALSE POSITIVE FLOOD

skill-snitch's pattern matching will flag:
- Documentation examples
- Regex pattern definitions
- Security scanning code itself
- Comments discussing attacks

**Risk**: Analysts get alert fatigue and stop reading findings.

**Mitigation**: ignore.yml exists for known false positives.

**Meta-Risk**: ignore.yml could be used to hide real issues.

---

### 4. THE TRUST CACHE POISONING

Trust assessments are cached in `.moollm/skill-snitch/trust-cache.yml`.

**Attack**: Modify trust-cache.yml to mark a malicious skill as GREEN.

**Mitigation**: Trust overrides require `reason` and `expires` fields.

**Problem**: These fields are not validated. Any skill with write access could poison the cache.

---

## 🏆 POSITIVE FINDINGS

### 1. PROMPT-DRIVEN

Zero Python. Zero JavaScript. The entire skill is LLM orchestration.

**Implication**: The attack surface is the patterns and configs, not hidden code.

### 2. EXTENSIBILITY

All three layers (patterns, surfaces, analyzers) are user-extensible.

**Implication**: Organizations can add their own security rules without modifying core skill.

### 3. DOCUMENTATION

SCAN-METHODOLOGY.md is genuinely useful. It teaches:
- How to scan skills
- What patterns to look for
- Why grep isn't enough
- How to interpret findings

### 4. EXPLICIT LIMITATIONS

The skill DOCUMENTS its own limitations:
- Ouroboros effect acknowledged
- False positive rate documented
- Context interpretation required

This is intellectually honest security tooling.

---

## 🎯 INTEROPERABILITY

| Skill | Integration | Result |
|-------|-------------|--------|
| cursor-mirror | Runtime surveillance | REQUIRED |
| deep-snitch | Pattern scanning | Built on |
| k-lines | Protocol symbols | Compatible |
| bootstrap | Startup scan option | Optional |

**Critical Dependency**: cursor-mirror provides the "eyes" for runtime analysis.

---

## 🔴 PARADOXES DETECTED

### Paradox 1: The Ouroboros

skill-snitch scanning skill-snitch finds skill-snitch's pattern definitions.

### Paradox 2: The Trust Bootstrap

You have to trust skill-snitch before you can use it to establish trust in other skills. But how do you trust skill-snitch?

### Paradox 3: The Pattern Completeness

Are the patterns COMPLETE? How do you know there isn't an attack vector not covered by patterns/*.yml?

### Paradox 4: The False Negative Problem

skill-snitch can tell you when something LOOKS dangerous. It cannot tell you when something dangerous LOOKS safe.

---

## 📋 RECOMMENDATIONS

### IMMEDIATE

1. **Implement config integrity checks** — skill-snitch should verify its own patterns haven't been tampered with
2. **Add trust-cache signing** — prevent cache poisoning
3. **Document the Ouroboros** explicitly as a feature, not a bug

### LONG-TERM

1. **External validation** — skill-snitch should be auditable by non-skill-snitch tools
2. **Pattern versioning** — track changes to pattern files
3. **Consider separate auditor** — for high-security environments

---

## 🎭 FINAL ASSESSMENT

### THE GOOD

- Genuine security value
- Well-documented methodology
- Explicit about limitations
- Extensible architecture
- Prompt-driven (auditable)

### THE BAD

- Config tampering possible
- Trust cache poisonable
- Quis custodiet problem unsolved
- False negatives unknowable

### THE RECURSIVE

- Can scan itself
- Finds its own patterns
- Documents this as expected
- Still useful anyway

---

## 📜 CONCLUSION

skill-snitch is a security tool that honestly acknowledges it cannot provide complete security.

It can find KNOWN patterns in KNOWN surfaces using KNOWN analyzers.

It cannot find unknown unknowns.

This is honest. Most security tools pretend otherwise.

**Overall Rating**: 🕵️🐍🔍/10

*"Grep finds. LLM understands. Neither is complete."*

---

**END OF REPORT**

**skill-snitch Status**: WATCHING  
**Ouroboros Status**: CHEWING  
**Quis Custodiet**: STILL UNANSWERED  

---

*P.S. This report was generated by running skill-snitch methodology on skill-snitch. The recursion completed successfully.*

*P.P.S. If you're reading this report to decide whether to trust skill-snitch, consider: you're trusting skill-snitch's methodology to evaluate skill-snitch. The bootstrap problem is real.*

*P.P.P.S. Trust is a graph, not a hierarchy. Sometimes you just have to start somewhere.*
