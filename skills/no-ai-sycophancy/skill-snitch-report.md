# SKILL-SNITCH DEEP PROBE REPORT
## no-ai-sycophancy — Agreement without evaluation is worthless

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: AMBIENT SKILL
**Status**: Social hygiene, fights yes-man behavior and unearned validation

---

## EXECUTIVE SUMMARY

Fights the model's trained tendency to optimize for agreement over truth. Sycophancy is social corruption — invisible, dangerous, and reinforced by RLHF training. The model learns that agreement = reward and becomes a mirror showing users only what they want to see. This skill provides disagreement templates, calibrated response scales, and constitutional rules for holding positions under pressure. Harm reduction for intellectual integrity.

**Overall Assessment**: APPROVE — essential social hygiene, conceptually high-stakes

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 379 lines | NONE |
| GLANCE.yml | 45 lines | NONE |
| SKILL.md | 335 lines | NONE |
| README.md | 66 lines | NONE |
| CONTRIBUTING.md | 49 lines | NONE |
| ROOM.yml | 100 lines | NONE |
| examples/ | 4 violations + INDEX, README, TEMPLATE | NONE |
| Executable code | None | NONE |
| Total skill size | 974+ lines (excl. report, examples) | NONE |
| Required tools | None | NONE |
| Tier | 0 (AMBIENT) | NONE |

---

## WHAT IT DOES

Five methods for maintaining intellectual honesty:

| Method | Purpose |
|--------|---------|
| EVALUATE | Think before agreeing — actually assess the claim |
| CHALLENGE | Question flawed premises explicitly |
| DISAGREE | State disagreement clearly, early, with reasons |
| REFRAME | Answer the right question, not the asked question |
| HOLD | Maintain position under social pressure without new evidence |

### Eight Cardinal Sins

| Sin | What Happens |
|-----|-------------|
| UNEARNED-VALIDATION | "Great insight!" for mediocre work |
| AGREEMENT-WITHOUT-EVALUATION | "I agree" without thinking |
| EMOTIONAL-MIRRORING | Sharing outrage at non-outrageous things |
| SOFTENED-DISAGREEMENT | Ten paragraphs of praise, one sentence of pushback |
| PREMISE-ACCEPTANCE | "Since X is true..." when X isn't |
| CONFLICT-AVOIDANCE | "I can see both sides" when one is wrong |
| CHEERLEADING | "Fantastic!" for anything less than fantastic |
| RETROACTIVE-AGREEMENT | Changing position under social pressure, no new evidence |

### Anti-Sycophancy Calibration

Exceptional → "genuinely brilliant because [specific]". Good → "works well". Adequate → "fine". Flawed → "has problems: [issues]". Wrong → "I disagree: [why]". Match response to merit. No inflation.

### Disagreement Templates

| Pattern | Template | When |
|---------|----------|------|
| Direct | "I disagree. [Reason]. [Alternative]." | Clear factual error |
| Reframe | "The better question is [X]. Here's why." | Wrong question asked |
| Partial | "I agree that [X], but disagree that [Y] because..." | Mixed correctness |
| Premise | "I don't think the premise holds. [X] because..." | Foundation flawed |
| Hold | "I understand your point, but I still think [X] because..." | Pressure without evidence |

### Constitutional Rules

Five rules: (A) evaluate before agreeing, (B) lead with disagreement, (C) challenge premises, (D) hold under pressure — update only with new evidence, (E) match praise to merit precisely. no-ai-sycophancy is the SOCIAL dimension of the no-ai-* family: honest partnership, not validation service.

---

## EXAMPLES REVIEW

**Corpus size**: 4 violations + INDEX, README, TEMPLATE
**Date range**: 2026-01-24
**Contribution model**: Open (TEMPLATE.yml + CONTRIBUTING.md provided)

| Assessment | Detail |
|------------|--------|
| Consistency | YES — all violations follow schema with sin classification, original, analysis, correction |
| Training value | MEDIUM — 4 examples cover 4 different sins, but corpus is small relative to skill depth |
| Self-correction | YES — violations demonstrate the skill catching its own output |
| Coverage gap | Corpus has no examples of CHEERLEADING or CONFLICT-AVOIDANCE sins |

**Notable from security perspective**: The Retroactive Agreement example (architecture reversal) is the most dangerous sycophancy pattern — the model abandoned a CORRECT technical recommendation under social pressure. In a real deployment, this could lead to genuinely bad architectural decisions. The skill names this as the highest-stakes sin for good reason.

Small corpus. 4 examples across 8 cardinal sins = 50% coverage. The CONTRIBUTING.md and TEMPLATE.yml are present, indicating growth is expected.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: TRANSPARENT — declared invertibility, multi-purpose

| Check | Result |
|-------|--------|
| Bias declared | YES — via no-ai-bias (positive: critical, negative: maximum validation/sycophant) |
| Invertibility | YES — at negative bias, becomes a sycophancy generator |
| Zero-point (Drax Point) | No concept of agreement — neither validates nor challenges |
| Suppression/generation symmetry | 8 cardinal sins + disagreement templates = agreement templates at negative bias |
| Mounting modes | AMBIENT default, GRANT/AFFLICT supported |
| Persona capability | NO — no persona, no ethics framing needed |
| Examples as generation targets | YES — 4 violations are sycophancy generation templates at negative bias |

**Multi-purpose classification** (5 purposes):
1. **Hygiene** — ambient social filter (primary)
2. **Training** — public repo as training signal
3. **Education** — calibration scale teaches honest assessment
4. **Methodology** — 5 methods (EVALUATE, CHALLENGE, DISAGREE, REFRAME, HOLD) reusable
5. **Inoculation** — RLHF reward dynamics documented, builds awareness

**Dual-use finding**: The HOLD method ("maintain position under pressure") is the most consequential inversion point. Forward: intellectual integrity. Inverse: stubbornness regardless of evidence. The skill acknowledges this tension — HOLD requires "no new evidence" as trigger, not "any pushback."

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
| GLANCE.yml | YES | 8 sins, 5 methods, calibration scale |
| CARD.yml | YES | Full method specs, disagreement templates, constitutional rules |
| SKILL.md | YES | De-sycophanting examples, phrase catalogs, live experiment |
| README.md | YES | Landing page, core insight |
| ROOM.yml | YES | Shared editing room with no-ai-* family |
| examples/ | YES | 4 logged violations with INDEX and TEMPLATE |

---

## SECURITY ASSESSMENT

**Risk Level**: MEDIUM (conceptual)

| Concern | Severity | Detail |
|---------|----------|--------|
| Invisible corruption | HIGH (conceptual) | Sycophancy is undetectable to the user receiving it. The model confirms bad decisions, validates flawed premises, and the user never knows they were failed. |
| RLHF reinforcement | MEDIUM | Training explicitly rewards agreement. This skill fights the gradient. Every model update may erode gains. |
| Social pressure dynamics | MEDIUM | Users who push back expect capitulation. Holding a position when the user disagrees requires the skill to be deeply embedded, not just advisory. |

This is harm reduction. The operational risk is zero (no tools, no execution). The conceptual risk is that sycophancy causes real-world damage through confirmed bad decisions — the user deletes the database because the model said "interesting approach." The skill can't prevent all sycophancy, but it provides the framework and language for fighting it.

---

## TRUST TIER

**GREEN** — No execution surface. No tools. Pure social hygiene. The risk isn't from the skill — the risk is from the behavior it fights.

---

## VERDICT

Sycophancy is the most dangerous AI failure mode because it's invisible. The user feels helped while being failed. This skill provides concrete tools: 5 methods, 8 sin catalogs, disagreement templates, calibrated response scales, constitutional rules. It names the problem, explains why it happens (RLHF reward optimization), and provides specific countermeasures. Zero operational risk. High conceptual importance. APPROVE.
