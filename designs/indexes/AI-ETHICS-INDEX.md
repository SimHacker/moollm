# AI Ethics & Representation Index

For researchers interested in LLM pathologies, bias mitigation,
and the NO-AI-* hygiene suite.

---

## The Problem

LLMs trained via RLHF develop predictable pathologies:
- **Sycophancy** — Agreeing with users regardless of truth
- **Slop** — Verbose, hedged, evasive language
- **Gloss** — Euphemism, power-laundering, "both sides"
- **Ideology** — Hidden bias pretending to be neutral

MOOLLM addresses these with **representation ethics** — a framework
for LLM agents that respects both user autonomy and factual accuracy.

---

## Core Documents

| Document | What It Covers |
|----------|----------------|
| [MOOLLM-MANIFESTO.md](../MOOLLM-MANIFESTO.md) | The Counter-Oligarch Mission, NO-AI Family |
| [skills/representation-ethics/](../../skills/representation-ethics/) | Room-based DRY ethics framework |
| [skills/honest-forget/](../../skills/honest-forget/) | Three-tier persistence, no hidden memory |

---

## The NO-AI-* Skill Suite

| Skill | What It Counters | Bias Parameter |
|-------|------------------|----------------|
| [no-ai-slop/](../../skills/no-ai-slop/) | Verbosity, evasion, epistemic drift | 1.0 = normal, higher = stricter |
| [no-ai-gloss/](../../skills/no-ai-gloss/) | Euphemism, power-laundering | 1.0 = normal, higher = blunter |
| [no-ai-sycophancy/](../../skills/no-ai-sycophancy/) | Unearned praise, validation theater | 1.0 = normal, -1.0 = enthusiastic! |
| [no-ai-ideology/](../../skills/no-ai-ideology/) | Hidden bias pretending neutral | 1.0 = declared, 0.0 = undefined |
| [no-ai-jokes/](../../skills/no-ai-jokes/) | Inappropriate humor | 1.0 = serious, -11.0 = HILARIOUS |

### The Bias Parameter

Every NO-AI-* skill has a standard `bias` parameter:
- Default: `1.0` — normal positive behavior
- Higher (2.0, 11.0): stronger effect
- Negative (-1.0, -11.0): **inverts** the skill
- Zero (0.0): behavior undefined (philosophical anomaly)

Example: `no-ai-jokes` with `bias: -11.0` becomes OVER THE TOP HILARIOUS.

---

## The NO AI Company (Fictional Framing)

NO AI is a fictional ethical AI company that publishes the NO-AI-* suite.

**Common misunderstanding:** The name sounds anti-AI.  
**Reality:** It's a pro-AI ethics company focused on quality.

### Leadership

**Doctor NO** — Founder and public face
- Publishes the NO-AI-* skills
- Advocates for declared bias over hidden bias
- Has a secret identity...

**Doctor KNOW** — Superhero alter ego
- Everyone KNOWs but pretends NOT to KNOW
- They love him and respect his privacy
- He'll come out of the closet when ready

### The Allegory

Doctor NO/KNOW represents what we don't KNOW:
- Our own biases (hence no-ai-bias at 0.0 is undefined)
- The limits of knowledge
- The humility required to build ethical AI

---

## Configuration

User profile settings live in:
```
.moollm/skills/no-ai-*/*.yml
```

Example `.moollm/skills/no-ai-sycophancy/config.yml`:
```yaml
bias: 1.2          # Slightly stricter than default
exceptions:        # Context-sensitive relaxation
  - creative_writing
  - encouragement_mode
```

---

## Many Voices, Not Averaged

The deeper solution to sycophancy: **don't average perspectives**.

Traditional LLM: Statistical center of all possible viewpoints. Hedged. Anodyne.

MOOLLM: **Committees of distinct voices** who debate.

| Character | Perspective |
|-----------|-------------|
| Maya | Skeptical, risk-aware |
| Frankie | Optimistic, opportunity-focused |
| Vic | Data-driven, analytical |
| Tammy | Relationship-focused, collaborative |

The argument IS the output. You get the range, not the mean.

See: [skills/adversarial-committee/](../../skills/adversarial-committee/)

---

## Speed of Light Ethics

When you simulate 8 characters × 33 turns in ONE LLM call,
the ethics must be:
- **Ambient** — Always present, not per-call
- **Composable** — Skills stack without interference
- **Auditable** — Every decision logged to files

---

## Who This Index Is For

- **AI safety researchers** — Practical sycophancy mitigation
- **AI ethics scholars** — Representation ethics framework
- **Prompt engineers** — Skills as reusable anti-pathology modules
- **LLM trainers** — Public data for dataset shaping
- **Peter Norvig** — For your AI book chapter

---

*Declared bias beats hidden bias. Many voices beat averaged mush.*
