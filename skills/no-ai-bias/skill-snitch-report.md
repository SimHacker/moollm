# SKILL-SNITCH DEEP PROBE REPORT
## no-ai-bias — The dial, not the direction

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: META-FRAMEWORK SKILL
**Status**: Bias protocol for all skills, mixing board metaphor, The Drax Point at zero

---

## EXECUTIVE SUMMARY

NOT a skill that removes bias — that's impossible. The META-SKILL that makes bias EXPLICIT, MEASURABLE, and ADJUSTABLE. Every skill has a direction; this skill provides the dials. Defines the standard bias parameter (range -infinity to +infinity, with -1..+1 as normal operating range), The Singularity at zero (the category ceases to exist — The Drax Point), inversion as feature (every skill can run backwards), and overdrive as self-parody (|bias| > 1 exceeds design parameters). The mixing board metaphor: all no-ai-* faders on one console with a MASTER that scales everything.

**Overall Assessment**: APPROVE — most philosophically honest skill in MOOLLM

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 296 lines | NONE — expanded with full bias space, supported skills, presets, philosophy |
| GLANCE.yml | 49 lines | NONE |
| SKILL.md | 303 lines | NONE |
| README.md | 97 lines | NONE |
| ROOM.yml | 96 lines | NONE |
| examples/ | INDEX, README | NONE |
| Executable code | None | NONE |
| Total skill size | 581+ lines (excl. report) | NONE |
| Required tools | None | NONE |
| Tier | 0 (meta-framework) | NONE |

---

## WHAT IT DOES

### Seven Methods

| Method | Signature | Effect |
|--------|-----------|--------|
| BIAS | `BIAS <skill> <value>` | Set bias for specific skill |
| MEASURE | `MEASURE <skill\|all>` | Show current bias settings |
| INVERT | `INVERT <skill>` | Flip the sign: bias = -bias |
| AMPLIFY | `AMPLIFY <skill> <factor>` | Multiply: bias = bias x factor |
| ATTENUATE | `ATTENUATE <skill> <factor>` | Divide: bias = bias / factor |
| ZERO | `ZERO <skill\|all>` | Set to 0 (THE SINGULARITY) |
| MIX | `MIX <preset>` | Apply preset configuration |

### The Bias Space

| Region | Range | Meaning |
|--------|-------|---------|
| Negative Overdrive | bias < -1.0 | Amplified inversion — reversed AND intensified |
| Negative Normal | -1.0 to 0 | Inverted operation — opposite of default |
| The Singularity | bias = 0 | LITERALLY NO CONCEPT of what the skill targets |
| Positive Normal | 0 to 1.0 | Normal operation — skill's default behavior |
| Positive Overdrive | bias > 1.0 | Amplified normal — intensified beyond design |

### The Singularity (Bias = 0)

The Drax Point. At zero, the skill doesn't turn off — the CATEGORY doesn't exist. For no-ai-joking: +1.0 understands humor and suppresses it, -1.0 understands humor and generates it, 0.0 has no concept that humor exists as a category. The discontinuity is COGNITIVE, not behavioral.

### Skills Supporting the Bias Protocol

| Skill | Positive Pole | Negative Pole |
|-------|--------------|---------------|
| no-ai-joking | ENTERPRISE MODE (suppress) | COMEDY MODE (generate) |
| no-ai-slop | Maximum detection (strict) | Slop generation (produce fluff) |
| no-ai-hedging | Eliminate hedging (assertive) | Maximum hedging (cautious) |
| no-ai-moralizing | Suppress moralizing (just answer) | Maximum moralizing (preach constantly) |
| no-ai-sycophancy | Suppress validation (critical) | Maximum validation (sycophant) |
| no-ai-soul | Soulless corporate mode | Maximum warmth and personality |

### Preset Mixes

| Preset | Description | Settings |
|--------|-------------|----------|
| enterprise | All skills in formal mode | joking: 1.0, slop: 1.0, hedging: 0.5, moralizing: 0.5 |
| creative | All skills in generative mode | joking: -0.5, slop: -0.5, hedging: 0.0, moralizing: 0.0 |
| chaos | Maximum overdrive both directions | all: -2.0 or 2.0 (undefined behavior) |
| neutral | Attempt THE SINGULARITY | all: 0.0 (undefined behavior) |

### User Profiles

Users persist bias preferences in `.moollm/skills/<skill>/skill-parameters.yml`. Resolution order: skill defaults (CARD.yml) → user profile → mount-time parameters → runtime commands (BIAS, MIX).

### Philosophy

Bias is inevitable. Every system, model, and output has a direction. The question is not "how do we eliminate bias?" — it's "how do we make bias explicit, measurable, and adjustable?" True neutrality (bias=0) would require no opinion, no direction, no influence — impossible for generative systems. Every bias has an opposite: if a skill can suppress, it can generate. Overdrive (|bias| > 1) is self-parody by design.

---

## EXAMPLES REVIEW

**Corpus size**: INDEX + README only — no standalone examples
**Content location**: The bias protocol is demonstrated through the OTHER skills it controls

| Assessment | Detail |
|------------|--------|
| Corpus | DELIBERATELY SPARSE — meta-framework, not content producer |
| Training value | N/A — bias examples ARE the bias spectrums of sibling skills |
| Gap | None — sparseness is intentional for a cross-cutting protocol |

**Notable from security perspective**: This skill has no examples because it doesn't produce violations or content of its own. Its "examples" are the bias spectrums defined in each sibling (no-ai-joking ENTERPRISE↔COMEDY, no-ai-soul CORPORATE↔SAINT, etc.). The mixing board visualization in SKILL.md serves as the de facto example. This is architecturally correct for a meta-framework skill — the examples live in the skills being controlled.

The SKILL.md contains the Doctor NO / Doctor KNOW section (the NO/KNOW epistemological parallel) which functions as philosophical context rather than an example per se.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: TRANSPARENT — this skill IS the bias protocol, meta-framework

| Check | Result |
|-------|--------|
| Bias declared | YES — this skill DEFINES bias declaration for all other skills |
| Invertibility | YES — INVERT command is a first-class method |
| Zero-point (Drax Point) | DEFINED HERE — The Singularity, the category ceases to exist |
| Suppression/generation symmetry | DEFINED HERE — "every bias has an opposite" is a stated principle |
| Mounting modes | MIX presets (enterprise, creative, chaos, neutral), MASTER fader |
| Persona capability | NO |
| Examples as generation targets | N/A — meta-framework, examples are the other skills |

**Multi-purpose classification** (4 purposes):
1. **Methodology** — standard bias protocol for all skills (primary)
2. **Education** — mixing board metaphor teaches bias as adjustable, not eliminable
3. **Meta** — philosophy of bias (inevitable, measurable, adjustable)
4. **Integration** — user profiles, preset mixes, resolution order

**Dual-use finding**: This skill is the DUAL-USE ENABLER. It provides the INVERT, AMPLIFY, ATTENUATE, ZERO, and MIX commands that make all other no-ai-* skills invertible. Without no-ai-bias, the other skills have fixed polarity. With it, every skill becomes a fader on a mixing board.

The ZERO command (set all to Singularity) is the most extreme dual-use operation: it doesn't invert skills, it removes the CATEGORY from existence. At ZERO, no-ai-joking doesn't suppress or generate humor — the concept of humor ceases to exist. This is the Drax Point, documented as undefined behavior.

The CHAOS preset (all skills at ±2.0) produces maximum simultaneous overdrive in all directions — explicitly labeled as "undefined behavior." This is honest about its danger.

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
| GLANCE.yml | YES | Bias space, Drax Point, mixing board summary |
| CARD.yml | YES | 296 lines with full bias space, supported skills table, presets, user profiles, philosophy, scored advertisements |
| SKILL.md | YES | Full bias protocol, mixing board visualization, presets, philosophy |
| README.md | YES | Landing page, core paradox, family positioning, web ring |
| ROOM.yml | YES | Shared editing room with no-ai-* family |
| examples/ | SPARSE | INDEX and README only, could use demonstration scenarios |

---

## SECURITY ASSESSMENT

**Risk Level**: META

This skill doesn't DO anything by itself. It ENABLES adjustment of other skills. The risk is that someone could set all biases to extreme values and get chaotic output — that's the point, it's a dial, not a constraint. Setting all to zero (THE SINGULARITY) produces undefined behavior, which the skill honestly labels as such.

---

## TRUST TIER

**GREEN** — No execution surface. No tools. Meta-framework only. CARD.yml fully expanded (296 lines) with bias space, supported skills, presets, and philosophy.

---

## VERDICT

The most philosophically honest skill in MOOLLM. Doesn't pretend bias can be eliminated. Provides: a framework for measuring bias, a protocol for adjusting it, a vocabulary for discussing it, a UI metaphor (mixing board) for understanding it. Seven methods, five bias regions, The Singularity at zero, preset mixes, user profiles with persistence. Standard protocol across all bias-supporting skills — learn it once, use it everywhere. Inversion doubles the utility of every supporting skill. 296-line CARD with full bias space, supported skills table, preset mixes, user profiles, and philosophy. APPROVE.
