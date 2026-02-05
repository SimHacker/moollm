# SKILL-SNITCH DEEP PROBE REPORT
## empathic-templates — Every slot is a prompt, not a variable name

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: INSTANTIATION SKILL
**Status**: Tier 1, requires read_file and write_file, Self-style prototype schemas

---

## EXECUTIVE SUMMARY

Templates where `{{describe_atmosphere}}` replaces `{{description}}`. The LLM doesn't substitute strings — it generates semantically appropriate content from context. Two slot types: metacomments (instructions the LLM executes during instantiation) and pass-through (standard variable substitution). Self-style prototype inheritance means templates delegate to parents.

**Overall Assessment**: APPROVE — powerful instantiation with known attack surface

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 121 lines | NONE |
| GLANCE.yml | 48 lines | NONE |
| SKILL.md | 937 lines | NONE |
| README.md | 75 lines | NONE |
| Executable code | None | NONE |
| Total skill size | 1181 lines (excl. report) | NONE |
| Required tools | read_file, write_file | LOW |
| Tier | 1 | LOW |

---

## WHAT IT DOES

Four methods for template lifecycle:

| Method | Purpose |
|--------|---------|
| INSTANTIATE | Create instance from template with context → writes file |
| PARSE | Analyze template structure, extract required/optional slots |
| PREVIEW | Show what instantiation would produce without writing |
| VALIDATE | Check if provided context satisfies template requirements |

Two slot types:

| Type | Example | Behavior |
|------|---------|----------|
| Metacomment | `{{describe_based_on_context}}` | LLM generates content semantically |
| Pass-through | `{{character_name}}` | Standard variable substitution |

The front-matter pattern (first 50 lines) lets the LLM sniff template name, purpose, required variables, and example context before instantiation begins. Anti-patterns: dumb passthrough (`{{description}}`), no context hints, over-specification (50 required variables instead of few required + many inferrable).

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 (LLM + write_file tool, no scripts) | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |
| Template injection patterns | 0 | CLEAN (scanned with template-injection.yml) |
| Prompt injection patterns | 0 | CLEAN (scanned with prompt-injection.yml) |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Metacomment vs pass-through distinction |
| CARD.yml | YES | 4 methods, tier 1, empathic syntax examples |
| SKILL.md | YES | Full template protocol, front-matter pattern, anti-patterns |
| README.md | YES | Landing page, relationship to Self inheritance |

---

## SECURITY ASSESSMENT

**Risk Level**: LOW

| Concern | Severity | Detail |
|---------|----------|--------|
| LLM content generation | LOW | Empathic slots instruct the LLM to generate content. Output quality depends on context and model capability. |
| File creation | LOW | INSTANTIATE writes files via write_file tool. Output paths visible in method call. |
| Context injection | MEDIUM | Malicious context passed to INSTANTIATE could steer LLM generation. Templates are instructions the LLM executes — a crafted context could produce unintended output. |
| Template as attack surface | MEDIUM | Documented in SKILL-SECURITY-ARCHITECTURE.md. Templates are effectively prompts. A malicious .tmpl file is a prompt injection vector. |

Mitigations: skill-snitch scans templates with dedicated pattern sets (template-injection.yml, prompt-injection.yml). All templates are visible files in version control. PREVIEW method allows dry-run before INSTANTIATE. The attack surface is known, documented, and actively scanned.

---

## TRUST TIER

**GREEN** — All templates visible in repository. Dedicated snitch pattern sets for template and prompt injection. Attack surface documented and monitored.

---

## VERDICT

Semantic template instantiation with a known and documented attack surface. Context injection is the real risk; mitigated by template scanning and preview capability. APPROVE.
