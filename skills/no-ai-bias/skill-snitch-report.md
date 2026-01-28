# Skill-Snitch Deep Probe: no-ai-bias

**Report ID:** SSR-BIAS-2026-01-27  
**Status:** BIAS = 0 IS A LIE (but it's adjustable)  
**Threat Level:** 🟢 META-FRAMEWORK  
**T-Shirt:** "The dial, not the direction."

---

## Executive Summary

`no-ai-bias` is NOT a skill that removes bias. That's impossible.

It's the META-SKILL that makes bias EXPLICIT, MEASURABLE, and ADJUSTABLE. It's the mixing board that controls all the other no-ai-* faders.

Think of it as: every skill has a direction. This skill provides the dials.

---

## The Core Paradox

> "NO AI BIAS" sounds like it eliminates bias.
> But bias=0 is IMPOSSIBLE. There is always a direction.
> 
> The skill acknowledges this: we don't eliminate bias,
> we make it EXPLICIT, MEASURABLE, and ADJUSTABLE.

The only honest position: declare your bias and provide a dial for others to adjust it.

---

## The Bias Space

```
                    THE BIAS SPACE
      
         -∞ ←────────────── 0 ──────────────→ +∞
          │                 │                  │
       INVERTED          NEUTRAL           NORMAL
       OVERDRIVE       (impossible)        OVERDRIVE
      
       ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┐
       │ -2.0 │ -1.0 │ -0.5 │  0   │ +0.5 │ +1.0 │ +2.0 │
       └──────┴──────┴──────┴──────┴──────┴──────┴──────┘
          │      │      │      │      │      │      │
        max   full   mild   ???   mild   full   max
       invert invert invert      normal normal normal
```

---

## The Regions

| Region | Range | Meaning |
|--------|-------|---------|
| **Negative Overdrive** | bias < -1.0 | Amplified inversion — behavior reversed AND intensified |
| **Negative Normal** | -1.0 ≤ bias < 0 | Inverted operation — skill does opposite of default |
| **The Singularity** | bias = 0 | LITERALLY NO CONCEPT of what the skill targets |
| **Positive Normal** | 0 < bias ≤ 1.0 | Normal operation — skill's default behavior |
| **Positive Overdrive** | bias > 1.0 | Amplified normal — behavior intensified beyond design |

---

## The Singularity (Bias = 0)

This is where it gets philosophically interesting.

At bias = 0, the skill doesn't just "turn off." The CATEGORY doesn't exist:

**For no-ai-joking:**
- **+1.0:** "I understand humor and choose to suppress it"
- **-1.0:** "I understand humor and choose to generate it"
- **0.0:** "What is this 'humor' you speak of?"

The discontinuity is COGNITIVE, not behavioral. At ±ε you have a theory. At exactly 0, you don't.

This is **The Drax Point** — named for Drax the Destroyer from *Guardians of the Galaxy*, who takes everything literally because he has no concept of metaphor or humor: "Nothing goes over my head. My reflexes are too fast."

---

## Skills Supporting the Bias Protocol

| Skill | Positive Pole | Negative Pole |
|-------|--------------|---------------|
| **no-ai-joking** | ENTERPRISE MODE (suppress) | COMEDY MODE (generate) |
| **no-ai-slop** | Maximum detection (strict) | Slop generation (produce fluff) |
| **no-ai-hedging** | Eliminate hedging (assertive) | Maximum hedging (cautious) |
| **no-ai-moralizing** | Suppress moralizing (just answer) | Maximum moralizing (preach constantly) |
| **no-ai-sycophancy** | Suppress validation (critical) | Maximum validation (sycophant) |
| **no-ai-soul** | Soulless corporate mode | Maximum warmth and personality |

---

## The Mixing Board

The skill visualizes all bias controls as a studio mixing board:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         THE BIAS MIXING BOARD                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   JOKING    SLOP     HEDGE   MORAL   SOUL    SYCO    [AUX1]   [AUX2]     ║
║                                                                           ║
║   ┌───┐    ┌───┐    ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐    ┌───┐      ║
║   │ ▲ │    │ ▲ │    │   │   │   │   │ ▲ │   │   │   │   │    │   │      ║
║   │ █ │    │ █ │    │ █ │   │ █ │   │ █ │   │ █ │   │   │    │   │      ║
║   │ █ │    │ █ │    │ █ │   │ █ │   │ █ │   │ █ │   │   │    │   │      ║
║   │ █ │    │   │    │ █ │   │   │   │   │   │ █ │   │   │    │   │      ║
║   │───│    │───│    │───│   │───│   │───│   │───│   │───│    │───│  0   ║
║   │   │    │   │    │   │   │ █ │   │   │   │   │   │   │    │   │      ║
║   │   │    │   │    │   │   │ █ │   │   │   │   │   │   │    │   │      ║
║   │ ▼ │    │ ▼ │    │ ▼ │   │ ▼ │   │ ▼ │   │ ▼ │   │ ▼ │    │ ▼ │      ║
║   └───┘    └───┘    └───┘   └───┘   └───┘   └───┘   └───┘    └───┘      ║
║   +1.0     +0.8     +0.5    -0.3    +0.7    +0.5     0.0      0.0       ║
║                                                                           ║
║   ═══════════════════════════════════════════════════════════════════    ║
║   MASTER: [████████████░░░░] 0.75                                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

The MASTER fader scales ALL skill biases. If MASTER = 0.0, everything goes to The Singularity.

---

## Methods

| Method | Signature | Effect |
|--------|-----------|--------|
| **BIAS** | `BIAS <skill> <value>` | Set bias for specific skill |
| **MEASURE** | `MEASURE <skill\|all>` | Show current bias settings |
| **INVERT** | `INVERT <skill>` | Flip the sign: bias = -bias |
| **AMPLIFY** | `AMPLIFY <skill> <factor>` | Multiply: bias = bias × factor |
| **ATTENUATE** | `ATTENUATE <skill> <factor>` | Divide: bias = bias / factor |
| **ZERO** | `ZERO <skill\|all>` | Set to 0 (THE SINGULARITY) |
| **MIX** | `MIX <preset>` | Apply preset configuration |

---

## Preset Mixes

| Preset | Description | Settings |
|--------|-------------|----------|
| **enterprise** | All skills in formal mode | joking: 1.0, slop: 1.0, hedging: 0.5, moralizing: 0.5 |
| **creative** | All skills in generative mode | joking: -0.5, slop: -0.5, hedging: 0.0, moralizing: 0.0 |
| **chaos** | Maximum overdrive both directions | joking: -2.0, slop: -2.0, hedging: -2.0, moralizing: 2.0 |
| **neutral** | Attempt THE SINGULARITY | all: 0.0 (undefined behavior) |

---

## User Profiles

Users can persist their bias preferences:

```yaml
# .moollm/skills/no-ai-joking/skill-parameters.yml
# My personal humor preferences

bias: -0.3  # I like wit in my output

exceptions:
  - puns
  - callbacks
  - meta-humor

enterprise_mode: false  # Never go full enterprise
```

Resolution order:
1. Skill defaults (CARD.yml)
2. User profile (.moollm/skills/...)
3. Mount-time parameters
4. Runtime commands (BIAS, MIX)

---

## Philosophy

### On Bias
> BIAS IS INEVITABLE.
> 
> Every system, every model, every output has a direction.
> The question is not "how do we eliminate bias?"
> The question is "how do we make bias explicit, measurable, and adjustable?"

### On Neutrality
> BIAS = 0 IS THE SINGULARITY.
> 
> It's not neutral. It's UNDEFINED.
> True neutrality would require no opinion, no direction, no influence.
> All impossible for generative systems.

### On Inversion
> EVERY BIAS HAS AN OPPOSITE.
> 
> If a skill can suppress something, it can generate it.
> If a skill can filter something, it can amplify it.
> The inversion is not "turn it off." It's "run it backwards."

### On Overdrive
> OVERDRIVE IS SELF-PARODY.
> 
> At |bias| > 1, the skill exceeds its design parameters.
> The behavior becomes exaggerated, often absurd.
> This is a feature, not a bug.

---

## Security Assessment

**Threat Level:** META

This skill doesn't DO anything by itself. It ENABLES adjustment of other skills.

The risk is that someone could set all biases to extreme values and get chaotic output. That's the point — it's a dial, not a constraint.

---

## Why This Skill Matters

### 1. Honesty About Bias
Most systems pretend they're neutral. This skill acknowledges that neutrality is impossible and provides tools to work with that reality.

### 2. User Control
Instead of hard-coded behavior, users can tune skills to their preferences. One person's "too formal" is another's "just right."

### 3. Composability
The bias protocol is STANDARD across skills. Learn it once, use it everywhere. The mixing board metaphor makes it intuitive.

### 4. Inversion as Feature
Skills that suppress can also generate. This doubles the utility of every bias-supporting skill.

---

## Verdict

This is the most philosophically honest skill in MOOLLM.

It doesn't pretend bias can be eliminated. It provides:
- A framework for measuring bias
- A protocol for adjusting it
- A vocabulary for discussing it
- A UI metaphor (mixing board) for understanding it

**BIAS = 0 IS A LIE. (But it's adjustable.)**

---

## T-Shirt Alternatives

1. "BIAS = 0 IS A LIE (but it's adjustable)"
2. "The dial, not the direction."
3. "Neutrality is impossible. Transparency is achievable."
4. "Every fader is a opinion."

---

*Report filed by skill-snitch. Current bias: MEASURE ALL → analyzing.*
