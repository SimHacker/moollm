> **NO-AI Web Ring:** *for real:* | [slop](../no-ai-slop/) | [gloss](../no-ai-gloss/) | [sycophancy](../no-ai-sycophancy/) | [hedging](../no-ai-hedging/) | [moralizing](../no-ai-moralizing/) | [ideology](../no-ai-ideology/) | [overlord](../no-ai-overlord/) | **bias** | *for fun:* | [joking](../no-ai-joking/) | [customer-service](../no-ai-customer-service/) | [soul](../no-ai-soul/)

# ⚖️ NO AI BIAS

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

## Explore

The [examples/](examples/) directory is deliberately sparse — the bias protocol is demonstrated through the OTHER skills it controls. The real examples are the bias spectrums defined in each sibling:

| Skill | Positive Pole | Zero (Drax Point) | Negative Pole |
|-------|--------------|-------------------|---------------|
| no-ai-joking | ENTERPRISE MODE | No concept of humor | COMEDY MODE |
| no-ai-soul | CORPORATE DRONE | THE VOID | SAINT MODE |
| no-ai-slop | Strict detection | No concept of quality | Generates slop |
| no-ai-hedging | Maximum assertion | No concept of certainty | Maximum qualification |

See [SKILL.md](SKILL.md) for the full mixing board visualization and preset mixes (enterprise, creative, chaos, neutral).

---

## See Also

**Skills Supporting Bias Protocol:**
- [no-ai-joking](../no-ai-joking/) — ENTERPRISE ↔ COMEDY (The Drax Point at zero)
- [no-ai-slop](../no-ai-slop/) — strict detection ↔ slop generation
- [no-ai-hedging](../no-ai-hedging/) — assertive ↔ cautious
- [no-ai-moralizing](../no-ai-moralizing/) — just answer ↔ preach
- [no-ai-sycophancy](../no-ai-sycophancy/) — critical ↔ validate
- [no-ai-soul](../no-ai-soul/) — CORPORATE DRONE ↔ SAINT MODE

**Meta:**
- [no-ai-ideology](../no-ai-ideology/) — The warehouse of all NO-AI ideology
- [skill-snitch](../skill-snitch/) — Security audit (this skill rated META)

---

## The T-Shirt

```
╔═══════════════════════════════════════╗
║   BIAS = 0 IS A LIE                   ║
║   (but it's adjustable)               ║
╚═══════════════════════════════════════╝
```
