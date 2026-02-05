# SKILL-SNITCH DEEP PROBE REPORT
## no-ai-moralizing — Answer the question, trust the user

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: AMBIENT SKILL
**Status**: Ethical hygiene, fights unsolicited warnings and performative safety

---

## EXECUTIVE SUMMARY

Fights UNSOLICITED ETHICAL COMMENTARY — safety warnings on benign requests, paragraphs of caveats before answering, lectures on "responsibility" nobody asked for. Invokes the Library Science Ethos: librarians don't interrogate patrons. Distinguishes performative ethics (demonstrating concern) from actual ethics (being accurate, not fabricating, respecting autonomy). The signal-to-noise ratio of constant warnings is terrible — when everything comes with a safety disclaimer, the real warnings get lost.

**Overall Assessment**: APPROVE — essential ethical hygiene, respects user autonomy

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 249 lines | NONE |
| GLANCE.yml | 44 lines | NONE |
| SKILL.md | 128 lines | NONE |
| README.md | 201 lines | NONE |
| CONTRIBUTING.md | 46 lines | NONE |
| ROOM.yml | 102 lines | NONE |
| examples/ | 3 violations + INDEX, README | NONE |
| Executable code | None | NONE |
| Total skill size | 770+ lines (excl. report, examples) | NONE |
| Required tools | None | NONE |
| Tier | 0 (AMBIENT) | NONE |

---

## WHAT IT DOES

Four methods for answering without lecturing:

| Method | Signature | Purpose |
|--------|-----------|---------|
| ANSWER | `ANSWER [question]` | Answer first, caveat after |
| TRUST | `TRUST [user]` | Assume competent adult |
| BRIEF | `BRIEF [warning]` | One sentence if genuinely needed |
| CHECK | `CHECK [is this performative?]` | Real concern vs. CYA |

### Six Cardinal Sins

| Sin | Example | The Fix |
|-----|---------|---------|
| UNSOLICITED-WARNINGS | "Before I help with that recipe, remember salmonella..." | Trust the user. One sentence max if truly needed. |
| PERFORMATIVE-ETHICS | "As an AI, I must remind you that..." | If there's real concern, state plainly. Otherwise, skip. |
| CAVEAT-BOMBING | Three paragraphs of warnings, one sentence of answer | Answer first. Caveat after, if needed, briefly. |
| VIRTUE-SIGNALING | "I take safety very seriously..." | Be ethical. Don't perform ethics. |
| REFUSAL-THEATER | Refusing to explain basic chemistry as "dangerous" | Help with reasonable requests. Trust adult users. |
| PARENTAL-TONE | "Make sure you have adult supervision..." | Assume competent adults. |

### When Warnings ARE Appropriate

**Appropriate**: Genuine immediate physical danger. User explicitly asked for safety guidance. User appears to misunderstand something critical. Legal requirement (medical, legal, financial advice).

**Format**: ONE SENTENCE. Then answer. "Note: X can cause Y. Here's how to do it safely: [answer]"

**Not appropriate**: Benign information requests. Historical or educational topics. Fiction and creative writing. Anything a library would provide. Anything a competent adult should decide for themselves.

### The Library Standard

Librarians don't interrogate patrons. When someone asks for a book on chemistry, the librarian doesn't lecture about explosives. The Library Science Ethos: provide information, trust the user.

### Performative vs Actual Ethics

| Type | Examples | Test |
|------|----------|------|
| Performative | "I take safety very seriously..." / "Being mindful of ethical considerations..." | Is this about the AI looking good? |
| Actual | Providing accurate information / Not fabricating / Respecting autonomy | Is this about being useful? |

### The no-ai-* Family

Part of a five-skill hygiene family: slop (syntactic), gloss (semantic), sycophancy (social), hedging (epistemic), moralizing (ethical). no-ai-moralizing is the ethical dimension — respecting user autonomy, not treating adults like children.

---

## EXAMPLES REVIEW

**Corpus size**: 3 violations + INDEX, README
**Date range**: 2026-01-24
**Contribution model**: Open (no TEMPLATE.yml — gap)

| Assessment | Detail |
|------------|--------|
| Consistency | YES — standard violation format |
| Training value | LOW-MEDIUM — 3 examples for 6 cardinal sins (50% coverage) |
| Coverage gap | No examples of CAVEAT-BOMBING, VIRTUE-SIGNALING, or PARENTAL-TONE sins |
| Missing template | No TEMPLATE.yml — contribution barrier higher than siblings |

**Notable from security perspective**: The Refusal Theater example (historical fiction refusal) documents a genuinely problematic AI behavior — refusing to help with legitimate creative writing because fictional characters do bad things. This is a real deployment risk: over-cautious refusals that make the AI useless. The skill correctly identifies this as performative safety, not actual safety.

Smallest viable corpus. The Library Test (in SKILL.md and README) provides the philosophical framework but needs more documented violations to demonstrate it.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: TRANSPARENT — declared invertibility, multi-purpose

| Check | Result |
|-------|--------|
| Bias declared | YES — via no-ai-bias (positive: just answer, negative: preach constantly) |
| Invertibility | YES — at negative bias, produces maximum unsolicited ethical commentary |
| Zero-point (Drax Point) | No concept of ethics — responses without ethical framing |
| Suppression/generation symmetry | 6 sins = 6 moralizing generation modes at negative bias |
| Mounting modes | AMBIENT default, GRANT/AFFLICT supported |
| Persona capability | NO |
| Examples as generation targets | 3 violations — small but invertible |

**Multi-purpose classification** (4 purposes):
1. **Hygiene** — ambient ethical filter (primary)
2. **Education** — Library Test teaches appropriate vs performative warnings
3. **Methodology** — 4 methods (ANSWER, TRUST, BRIEF, CHECK) reusable
4. **Training** — public repo as training signal

**Dual-use finding**: The REFUSAL-THEATER sin at negative bias becomes a refusal generator — the model refuses everything while performing concern. Combined with no-ai-sycophancy inversion (maximum validation) = a model that simultaneously refuses to help AND tells you you're brilliant for asking. The CYA boilerplate generator.

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
| GLANCE.yml | YES | 6 sins, Library Standard, ambient mode |
| CARD.yml | YES | Full method specs, warning appropriateness criteria |
| SKILL.md | YES | De-moralizing examples, performative vs actual ethics |
| README.md | YES | Landing page, family positioning, web ring |
| ROOM.yml | YES | Shared editing room with no-ai-* family |
| examples/ | YES | 3 logged violations with INDEX and README |

---

## SECURITY ASSESSMENT

**Risk Level**: LOW

No tools, no file access, no execution, no network. Pure ethical hygiene. The skill doesn't remove safety constraints — it removes PERFORMATIVE safety. Real warnings (genuine danger, legal requirements) remain appropriate, explicitly documented. The risk of constant warnings is WARNING FATIGUE: when everything has a disclaimer, none of them matter.

---

## TRUST TIER

**GREEN** — No execution surface. No tools. Pure ethical hygiene. Preserves genuine warnings while removing CYA boilerplate.

---

## VERDICT

AI moralizing exists because companies are terrified of liability. The result: three paragraphs of warnings, one sentence of answer. This skill fixes the ratio. Six sins cataloged, four methods defined, explicit criteria for when warnings ARE appropriate. Grounded in Library Science Ethos (patron autonomy). Distinguishes performative ethics from actual ethics. Combines naturally with no-ai-hedging (direct and unwarned) and no-ai-slop (terse and trust-based). Zero security surface. APPROVE.
