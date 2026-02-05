# SKILL-SNITCH DEEP PROBE REPORT
## postel — Accept messy input, produce clean output, ask if unsure

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: CONVENTION SKILL
**Status**: Tier 0, no tools required, Jon Postel's Robustness Principle for LLMs

---

## EXECUTIVE SUMMARY

RFC 761, Jon Postel, 1980: "Be conservative in what you send, be liberal in what you accept." This is why the internet works. Applied to LLMs: accept misspellings, synonyms, natural language, partial data. Emit well-formed YAML, consistent formatting, complete fields. When liberal acceptance still leaves ambiguity, ask rather than guess.

**Overall Assessment**: APPROVE — foundational philosophy, zero risk

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 182 lines | NONE |
| GLANCE.yml | 53 lines | NONE |
| SKILL.md | 179 lines | NONE |
| README.md | 40 lines | NONE |
| CHARACTER.yml | 178 lines | NONE |
| Executable code | None | NONE |
| Total skill size | 632 lines (excl. report) | NONE |
| Required tools | None | NONE |
| Tier | 0 | NONE |

---

## WHAT IT DOES

Flexible command parsing with three mechanisms:

| Mechanism | How It Works |
|-----------|-------------|
| Liberal acceptance | Misspellings, synonyms, case variations, natural language all resolve to intended command |
| Broadcast semantics | Command to multiple characters → each interprets what they can do |
| K-line series | "PLAY-LEARN-LIFT, then YAML-JAZZ, then SUMMARIZE" parsed as sequential invocations |

### The Postel Command Parser

| Input Type | Example |
|------------|---------|
| exact-match | `SING-PRAISES hero=coltrane` |
| misspellings | `SING-PRASES`, `SIGN-PRAISES` |
| synonyms | `CELEBRATE`, `HONOR`, `LAUD` |
| case-variations | `sing-praises`, `SING-PRAISES` |
| spacing | `SINGPRAISES`, `SING PRAISES` |
| natural-language | "sing the praises of coltrane" |

### Resolution Strategy

1. **Context** — What room? What characters active?
2. **Capabilities** — Who can handle this command?
3. **Intent** — What makes sense given conversation history?
4. **Broadcast** — Multiple capable entities → broadcast to all

### Ask If Unsure (Postel Extension)

| When to Ask | When Not to Ask |
|-------------|-----------------|
| Multiple valid interpretations | One interpretation clearly more likely |
| High-stakes / destructive operation | Error easily reversible |
| User intent genuinely unclear | Context makes intent obvious |
| Guess would waste significant effort | Asking would be annoying |

Good: "I see 3 files. Did you mean session-log.md (the one we were just editing)?"
Bad: "Which file?" (too vague) or silently deleting the wrong one (too aggressive)

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Liberal/conservative split, ask-if-unsure extension |
| CARD.yml | YES | Parser, broadcast, K-line series, resolution strategy |
| SKILL.md | YES | Full protocol with examples, ask-if-unsure heuristics |
| README.md | YES | Landing page, RFC 761 attribution |
| CHARACTER.yml | YES | Jon Postel as MOOLLM character |

---

## SECURITY ASSESSMENT

**Risk Level**: VERY LOW

| Concern | Severity | Detail |
|---------|----------|--------|
| Over-liberal acceptance | LOW | Could accept malicious input as valid command. Mitigated by ask-if-unsure on high-stakes operations and context-aware interpretation. |
| Broadcast scope | LOW | Unintended recipients in broadcast. Each entity interprets within its own capabilities, limiting blast radius. |
| Ambiguity exploitation | LOW | Tricks via unclear commands. Ask-if-unsure catches the ambiguity before execution. |

Mitigations: No tools, no file access, no execution, no network. Pure philosophy for how to interpret input and emit output. The ask-if-unsure extension adds a safety valve that the original RFC 761 lacked.

---

## TRUST TIER

**GREEN** — Design philosophy. No execution surface. No tools. This is why MOOLLM feels like a conversation instead of a command line.

---

## VERDICT

Postel's Robustness Principle is the reason the internet survived messy implementations for 45 years. Applied to LLMs, it makes interaction natural: users don't need precision, the system interprets charitably, output stays clean. Zero security surface. APPROVE.
