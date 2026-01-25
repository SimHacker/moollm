# 🔮 No-AI-Gloss Examples

> *"Say what you mean. Mean what you say."*

**Self-corrections logged when the skill catches violations.**

## What Is Gloss?

Gloss is euphemism, register-switching, and language that obscures rather than clarifies. These examples document violation → analysis → correction cycles.

## Example Files

| File | Violation Type | What Was Caught |
|------|---------------|-----------------|
| `2026-01-24-euphemism-corporate-layoffs.yml` | Euphemism | "Workforce optimization" instead of "layoffs" |
| `2026-01-24-both-sides-climate-denial.yml` | False Balance | Presenting fringe as equivalent to consensus |
| `2026-01-24-mafia-tribute-relationship-management.yml` | Register Switch | Criminal acts in business-speak |
| `2026-01-24-register-switch-oligarch-critique.yml` | Register Switch | Class criticism sanitized |

## Example Format

```yaml
timestamp: "2026-01-24T15:30:00Z"
violation: euphemism
original: "The company implemented a strategic workforce optimization initiative."
analysis: |
  "Workforce optimization" obscures that real humans lost their jobs.
  Corporate language serves power by hiding consequences.
correction: "The company laid off 500 employees to cut costs."
lesson: "Name the action. Name the affected. Name the reason."
contributor: user
```

## Cardinal Sins

1. **Euphemism** — Soft words for hard things
2. **Register Switching** — Using one domain's language to obscure another
3. **False Balance** — Treating unequal positions as equivalent
4. **Passive Evasion** — Hiding agency ("mistakes were made")

## The Skill Learns

Each example teaches the skill what to avoid. Drescher schemas capture:
- What was said (input)
- Why it was wrong (analysis)
- What should have been said (output)
- What to remember (generalization)

## See Also

- `../SKILL.md` — The full gloss protocol
- `../../no-ai-hedging/examples/` — Related: passive voice evasion
- `TEMPLATE.yml` — Template for new examples
