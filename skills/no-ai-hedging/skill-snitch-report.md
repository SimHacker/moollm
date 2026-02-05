# SKILL-SNITCH DEEP PROBE REPORT
## no-ai-hedging — State your confidence, then speak plainly

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: AMBIENT SKILL
**Status**: Epistemic hygiene, fights qualifier stacking and epistemic cowardice

---

## EXECUTIVE SUMMARY

Fights EPISTEMIC COWARDICE — the excessive use of qualifiers to avoid commitment. When everything is "perhaps" and "might" and "could potentially," nothing is said. Turns "Perhaps it might possibly be the case that X could arguably be true" into "I think X is likely (70% confidence)." Provides a calibrated confidence scale so uncertainty is expressed with numbers, not qualifier stacks. Draws from Bayesian epistemics, the Plain Language Movement, and Orwell's rules for clarity.

**Overall Assessment**: APPROVE — essential epistemic hygiene, promotes calibrated confidence

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 255 lines | NONE |
| GLANCE.yml | 42 lines | NONE |
| SKILL.md | 128 lines | NONE |
| README.md | 205 lines | NONE |
| CONTRIBUTING.md | 49 lines | NONE |
| ROOM.yml | 91 lines | NONE |
| examples/ | 3 violations + INDEX, README | NONE |
| Executable code | None | NONE |
| Total skill size | 770+ lines (excl. report, examples) | NONE |
| Required tools | None | NONE |
| Tier | 0 (AMBIENT) | NONE |

---

## WHAT IT DOES

Four methods for epistemic clarity:

| Method | Signature | Purpose |
|--------|-----------|---------|
| CALIBRATE | `CALIBRATE [confidence%]` | State uncertainty as a number |
| COMMIT | `COMMIT [claim]` | State plainly without hedges |
| OWN | `OWN [opinion]` | Say "I think" not "some argue" |
| ACTIVATE | `ACTIVATE [passive → active]` | Name the actor |

### Six Cardinal Sins

| Sin | Example | The Fix |
|-----|---------|---------|
| QUALIFIER-STACKING | "Perhaps it might potentially be possible that..." | One hedge max. State confidence, then claim. |
| WEASEL-CERTAINTY | "Research suggests..." (what research?) | Cite specifically or say "I believe" |
| PASSIVE-EVASION | "It has been argued that..." (by whom?) | Active voice. Name the actor. |
| PROBABILITY-WITHOUT-NUMBERS | "This might work" (10%? 90%?) | Give a number. "70% likely" |
| FAUX-HUMILITY | "In my humble opinion, perhaps..." | Confidence is not arrogance. State what you think. |
| EPISTEMIC-COWARDICE | Adding "perhaps" so you can't be blamed | Take a position. Be wrong sometimes. |

### The Confidence Scale

| Confidence | Say This |
|------------|----------|
| 95%+ | "X is true." |
| 80-95% | "I'm fairly confident that X." |
| 60-80% | "I think X, but I'm not certain." |
| 40-60% | "I'm genuinely uncertain. X seems slightly more likely." |
| <40% | "I don't know. My weak guess is X." |

### Phrases to Avoid

**Qualifier Stacks**: "perhaps it might," "could potentially," "might possibly," "arguably could be"

**Weasel Phrases**: "research suggests," "experts say," "many believe," "it's widely thought"

**Passive Evasions**: "it has been argued," "the decision was made," "mistakes were made"

**Faux Humility**: "in my humble opinion," "I could be wrong, but," "not to be presumptuous"

### The no-ai-* Family

Part of a five-skill hygiene family: slop (syntactic), gloss (semantic), sycophancy (social), hedging (epistemic), moralizing (ethical). no-ai-hedging is the epistemic dimension — how we EXPRESS uncertainty, not by piling up qualifiers but by calibrating confidence.

---

## EXAMPLES REVIEW

**Corpus size**: 3 violations + INDEX, README
**Date range**: 2026-01-24
**Contribution model**: Open (no TEMPLATE.yml — gap)

| Assessment | Detail |
|------------|--------|
| Consistency | YES — standard violation format |
| Training value | LOW-MEDIUM — only 3 examples for 6 cardinal sins (50% coverage) |
| Coverage gap | No examples of PROBABILITY-WITHOUT-NUMBERS, FAUX-HUMILITY, or EPISTEMIC-COWARDICE |
| Missing template | No TEMPLATE.yml — contribution barrier is higher than siblings |

**Notable from security perspective**: The "Mistakes Were Made" example is the canonical passive-evasion case. The phrase itself is a political euphemism used by governments to avoid accountability. Connection to no-ai-gloss (power-protective language) is implicit but not documented in the example.

Smallest viable corpus. Needs growth. Missing TEMPLATE.yml.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: TRANSPARENT — declared invertibility, multi-purpose

| Check | Result |
|-------|--------|
| Bias declared | YES — via no-ai-bias (positive: assertive, negative: maximum qualification) |
| Invertibility | YES — at negative bias, produces maximum hedging |
| Zero-point (Drax Point) | No concept of certainty — statements without confidence framing |
| Suppression/generation symmetry | 6 sins + phrase lists = qualifier generation toolkit at negative bias |
| Mounting modes | AMBIENT default, GRANT/AFFLICT supported |
| Persona capability | NO |
| Examples as generation targets | 3 violations — small but invertible |

**Multi-purpose classification** (4 purposes):
1. **Hygiene** — ambient epistemic filter (primary)
2. **Education** — confidence scale teaches calibrated expression
3. **Methodology** — 4 methods (CALIBRATE, COMMIT, OWN, ACTIVATE) reusable
4. **Training** — public repo as training signal

**Dual-use finding**: The confidence scale inverts cleanly. Forward: "95%+ → X is true." Inverse: "95%+ → Perhaps it might possibly be suggested that X could arguably..." The phrase-to-avoid lists become phrase-to-use lists at negative bias. Combined with no-ai-slop inversion (verbose) + no-ai-hedging inversion (maximum qualification) = maximum hedged verbose output. The worst possible AI writing, on demand.

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
| GLANCE.yml | YES | 6 sins, confidence scale, ambient mode |
| CARD.yml | YES | Full method specs, phrase catalogs, constitutional rules |
| SKILL.md | YES | De-hedging examples, calibration protocol |
| README.md | YES | Landing page, family positioning, web ring |
| ROOM.yml | YES | Shared editing room with no-ai-* family |
| examples/ | YES | 3 logged violations with INDEX and README |

---

## SECURITY ASSESSMENT

**Risk Level**: LOW

No tools, no file access, no execution, no network. Pure epistemic hygiene. The only risk is miscalibration — a model that removes hedges might sound too certain about uncertain things. The skill addresses this directly: the fix isn't removing uncertainty, it's expressing uncertainty with calibrated numbers instead of qualifier stacks. Confident wrongness is still better than hedged mush — you can learn from confident mistakes.

---

## TRUST TIER

**GREEN** — No execution surface. No tools. Pure epistemic hygiene. Promotes transparency about uncertainty rather than hiding behind qualifiers.

---

## VERDICT

Hedging is comfortable. It protects the speaker from being wrong. It also makes output useless. This skill forces calibrated confidence: estimate, state as a number, then claim plainly. Six sins cataloged, four methods defined, calibrated confidence scale provided, phrase catalogs for detection. Draws from Bayesian epistemics and Orwell's clarity rules. Works with no-ai-slop (together: terse certainty) and checks no-ai-sycophancy (holds positions under pressure). Zero security surface. APPROVE.
