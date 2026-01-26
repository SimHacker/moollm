# NO AI BIAS

> **The dial, not the direction.**

---

## What Is This?

NO-AI-BIAS is the **cross-cutting meta-skill** for bias parameterization.

It's not *against* bias. It's *for* measuring and adjusting it.

Think of it as the **mixing board** for AI behavior:
- Each skill is a channel
- Bias is the fader
- NO-AI-BIAS is the engineer at the board

---

## The Core Insight

**BIAS = 0 IS A LIE.**

Every system has a direction. Every output has a lean.
The question isn't "how do we eliminate bias?"
The question is "how do we make it adjustable?"

This skill provides:
1. A standard parameter: `bias`
2. A standard range: `-∞` to `+∞`
3. Standard semantics for inversion and overdrive
4. Tools to measure and adjust

---

## Quick Start

```yaml
# Set bias for a skill
BIAS no-ai-joking -1.0    # COMEDY MODE

# Measure current settings
MEASURE all               # Show the mixing board

# Flip a skill's direction
INVERT no-ai-slop         # Now generates slop

# Push to overdrive
AMPLIFY no-ai-joking 2.0  # TPS REPORTS FOREVER
```

---

## The Spectrum

```
-2.0   -1.0   -0.5    0    +0.5   +1.0   +2.0
 │      │      │      │      │      │      │
max    full   mild   ???   mild   full   max
INVERTED              |              NORMAL
                THE SINGULARITY
               (undefined behavior)
```

---

## Files

- `CARD.yml` — Full specification (sniffable)
- `SKILL.md` — Protocol documentation
- `README.md` — This file

---

## Part of the NO-AI Family

- `no-ai-bias` — **This skill** (measure and adjust)
- `no-ai-joking` — Humor dial (suppress ↔ generate)
- `no-ai-slop` — Quality dial (filter ↔ fluff)
- `no-ai-hedging` — Confidence dial (assert ↔ hedge)
- `no-ai-moralizing` — Ethics dial (answer ↔ preach)
- `no-ai-sycophancy` — Honesty dial (critical ↔ validate)
- `no-ai-soul` — Warmth dial (corporate ↔ warm)
- `no-ai-ideology` — The warehouse (brand philosophy)

---

## The T-Shirt

```
╔═══════════════════════════════════════╗
║   BIAS = 0 IS A LIE                   ║
║   (but it's adjustable)               ║
╚═══════════════════════════════════════╝
```
