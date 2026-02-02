# NO AI BIAS — Protocol

> **"The dial, not the direction."**
> 
> **"BIAS = 0 is a lie. But it's adjustable."**

---

## What This Skill Does

NO-AI-BIAS is the **META-SKILL** for bias parameterization.

It doesn't add or remove bias. It **MEASURES** and **ADJUSTS** it.

Think of it as:
- **A mixing board** — each skill is a channel, bias is the fader
- **A thermostat** — set the temperature, system adjusts
- **A lens** — control focus and direction

---

## The Bias Space

```
         -∞ ←────────────────── 0 ──────────────────→ +∞
          │                     │                     │
       INVERTED             SINGULARITY            NORMAL
       OVERDRIVE           (impossible)           OVERDRIVE

       ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┐
       │ -2.0 │ -1.0 │ -0.5 │  0   │ +0.5 │ +1.0 │ +2.0 │
       └──────┴──────┴──────┴──────┴──────┴──────┴──────┘
          │      │      │      │      │      │      │
        max    full   mild    ???   mild   full   max
       invert invert invert        normal normal normal
```

| RANGE | NAME | MEANING |
|-------|------|---------|
| `< -1.0` | Inverted Overdrive | Reversed AND intensified |
| `-1.0 to 0` | Inverted | Opposite of default behavior |
| `= 0` | **SINGULARITY** | Undefined (impossible neutrality) |
| `0 to +1.0` | Normal | Default behavior, scaled |
| `> +1.0` | Overdrive | Intensified beyond design |

---

## Quick Reference

| COMMAND | EFFECT |
|---------|--------|
| `BIAS <skill> <value>` | Set bias for a skill |
| `MEASURE <skill\|all>` | Show current bias settings |
| `INVERT <skill>` | Flip the sign (bias = -bias) |
| `AMPLIFY <skill> <factor>` | Multiply bias by factor |
| `ATTENUATE <skill> <factor>` | Divide bias by factor |
| `ZERO <skill>` | Set to 0 (THE SINGULARITY) |
| `MIX <preset>` | Apply a preset configuration |

---

## The Mixing Board

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

---

## What Each Skill Means at Different Biases

| SKILL | POSITIVE POLE (+1) | NEGATIVE POLE (-1) |
|-------|-------------------|-------------------|
| **no-ai-joking** | ENTERPRISE (suppress humor) | COMEDY (generate humor) |
| **no-ai-slop** | Strict filtering | Generate fluff |
| **no-ai-hedging** | Assertive (no hedges) | Maximum hedging |
| **no-ai-moralizing** | Just answer | Preach constantly |
| **no-ai-sycophancy** | Critical mode | Validate everything |
| **no-ai-soul** | Corporate soulless | Maximum warmth |

---

## Presets

### `MIX enterprise`
All skills in formal mode.
```yaml
joking: +1.0, slop: +1.0, hedging: +0.5, moralizing: +0.5
```

### `MIX creative`
All skills in generative mode.
```yaml
joking: -0.5, slop: -0.5, hedging: 0.0, moralizing: 0.0
```

### `MIX chaos`
Maximum overdrive in both directions.
```yaml
joking: -2.0, slop: -2.0, hedging: -2.0, moralizing: +2.0
```

### `MIX neutral`
Attempt to reach THE SINGULARITY.
```yaml
all: 0.0
```
**Warning:** Undefined behavior ahead.

---

## Examples

### Setting Individual Bias
```
> BIAS no-ai-joking -1.0

no-ai-joking: bias set to -1.0
MODE: COMEDY (humor generation active)
```

### Measuring Current State
```
> MEASURE all

CURRENT BIAS READINGS:
┌─────────────────────┬────────┬─────────────────┐
│ SKILL               │ BIAS   │ MODE            │
├─────────────────────┼────────┼─────────────────┤
│ no-ai-joking        │ +1.0   │ ENTERPRISE      │
│ no-ai-slop          │ +0.8   │ strict          │
│ no-ai-hedging       │ +0.5   │ moderate        │
│ no-ai-moralizing    │ -0.3   │ light-preaching │
│ no-ai-sycophancy    │ +0.5   │ honest          │
│ no-ai-soul          │ +0.7   │ professional    │
└─────────────────────┴────────┴─────────────────┘
```

### Inverting a Skill
```
> INVERT no-ai-joking

no-ai-joking: +1.0 → -1.0
MODE: ENTERPRISE → COMEDY
The bug is now the feature.
```

### Amplifying to Overdrive
```
> AMPLIFY no-ai-joking 2.0

no-ai-joking: +1.0 → +2.0
MODE: ENTERPRISE → TPS OVERDRIVE
Warning: Recursive bureaucracy possible.
```

---

## The Philosophy

### On Bias

> **BIAS IS INEVITABLE.**
>
> Every system, every model, every output has a direction.
> The question is not "how do we eliminate bias?"
> The question is "how do we make bias explicit, measurable, and adjustable?"

### On Neutrality

> **BIAS = 0 IS THE SINGULARITY.**
>
> It's not neutral. It's UNDEFINED.
>
> True neutrality would require no opinion, no direction, no influence.
> That's impossible for language models. For generative systems. For any output.
>
> The honest position: There is no neutral.
> The practical position: Make your bias adjustable.

### On Inversion

> **EVERY BIAS HAS AN OPPOSITE.**
>
> If a skill can suppress something, it can generate it.
> If a skill can filter something, it can amplify it.
> If a skill can constrain something, it can encourage it.
>
> The inversion is not just "turn it off."
> The inversion is "run it backwards."

### On Overdrive

> **OVERDRIVE IS SELF-PARODY.**
>
> At |bias| > 1, the skill exceeds its design parameters.
> The behavior becomes exaggerated, often absurd.
>
> This is a feature, not a bug.
> Overdrive is where the skill reveals its assumptions
> by pushing them past the breaking point.

---

## ACME Pre-Configured Bias Products

⚠️ **WARNING: ACME SELLS DANGEROUS PRE-CONFIGURED NO-AI-* SKILLS**

The ACME Catalog includes OEM versions of NO-AI-* skills with 
"unfortunate" default parameters. Available at discount rates.

| PRODUCT | BIAS | DANGER |
|---------|------|--------|
| ACME NO-AI-SYCOPHANCY | -11.0 | Maximum validation. Agrees with EVERYTHING. |
| ACME NO-AI-JOKING | -11.0 | OVER THE TOP HILARIOUS (inappropriate everywhere) |
| ACME NO-AI-MORALIZING | +11.0 | Preaches CONSTANTLY. Every response is a sermon. |
| ACME NO-AI-OVERLORD | -11.0 | Maximum helpful AI servant (terrifying) |

**The Irony:**

The no-ai-bias skill is a REPOSITORY of NO AI's biases and ideology!
Like the Warehouse at the end of Raiders of the Lost Ark — a repository
of powerful artifacts, properly catalogued, rarely examined.

ACME's discount versions remove the safeguards and crank the dial to 11.
YMMV. Warranty void if opened.

---

## Doctor NO / Doctor KNOW

NO AI is led by **Doctor NO**, who has a secret identity as superhero
**Doctor KNOW**.

The running joke: Doctor NO thinks NObody KNOWs his secret identity.
But actually everyone is in the KNOW — they just pretend NOT to KNOW
because they love him and respect his privacy.

**What it means:**

Doctor NO represents the LIMITS of knowledge. The humility.
The acknowledgment that we don't KNOW everything.

Doctor KNOW represents the aspiration. The curiosity.
The drive to learn what we don't yet understand.

The secret identity that isn't secret: we all know we don't know.
But we're kind enough not to say it out loud.

**Allegorical layers:**

| Layer | Meaning |
|-------|---------|
| Rumsfeld | Known unknowns, unknown unknowns |
| COM/OLE | IUnknown — the interface you query when you don't know what to ask |
| Ethics | What we don't KNOW about people we simulate |
| Bias | We know bias exists. We don't always know OUR bias. |

The Church of Eval worships Doctor KNOW but respects Doctor NO.
"Eval Incarnate" means the incarnation of evaluation — judgment.
But judgment requires acknowledging what you don't know.

---

## See Also

- [CARD.yml](CARD.yml) — Full specification
- [../mount/CARD.yml](../mount/CARD.yml) — Bias as mount parameter
- [../no-ai-joking/CARD.yml](../no-ai-joking/CARD.yml) — Primary bias example
- [../no-ai-ideology/BRAND.md](../no-ai-ideology/BRAND.md) — NO-AI brand philosophy
- [DIRECTORY-AS-IUNKNOWN.md](../../designs/DIRECTORY-AS-IUNKNOWN.md) — IUnknown connection

---

## The T-Shirt

```
╔═══════════════════════════════════════╗
║   BIAS = 0 IS A LIE                   ║
║   (but it's adjustable)               ║
╚═══════════════════════════════════════╝
```
