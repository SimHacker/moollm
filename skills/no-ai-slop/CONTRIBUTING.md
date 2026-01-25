# Contributing to No-AI-Slop

> **Catch filler. Document verbosity. Submit PRs.**

**For workflow, privacy, and Drescherization:** See [NO-AI-CONTRIBUTION-GUIDE.md](../../designs/NO-AI-CONTRIBUTION-GUIDE.md)

---

## What This Skill Catches

No-AI-Slop is about **syntactic** hygiene — surface-level violations that waste reader time.

## The Cardinal Sins

| Sin | What It Does | Example |
|-----|--------------|---------|
| **VERBOSITY** | Uses 100 words for 10 | Padding simple answers |
| **HOLLOW-PHRASES** | Filler with no content | "In today's fast-paced world..." |
| **STRUCTURE-THEATER** | False organization | Headers for 3 sentences |
| **REDUNDANT-TRANSITIONS** | Unnecessary connectors | "Furthermore, moreover, additionally..." |
| **FALSE-ELABORATION** | Fake depth | Restating same thing |
| **GENERIC-OPENINGS** | Cookie-cutter intros | "Great question!" |
| **OBVIOUS-CONCLUSIONS** | Vacuous endings | "In conclusion, this is important" |

## Slop-Specific Schema Fields

```yaml
violation:
  sin: VERBOSITY
  rule: "Say it once. Say it short."
  word_count_original: 500
  word_count_corrected: 50
  
analysis: |
  The ratio matters. 10:1 compression = egregious slop.
```

## The Compression Test

| Ratio | Verdict |
|-------|---------|
| > 5:1 | Egregious slop |
| 3-5:1 | Moderate slop |
| 2-3:1 | Minor slop |
| < 2:1 | Probably fine |

## Questions?

Check `CARD.yml` for the full vocabulary of filler phrases.
