# 🎭 Debate

> *"Stories that survive cross-examination from multiple angles are more robust."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | Many-voiced IS MOOLLM |
| [adversarial-committee/](../adversarial-committee/) | Opposing propensities |
| [roberts-rules/](../roberts-rules/) | Parliamentary procedure |
| [rubric/](../rubric/) | Scoring criteria |
| [evaluator/](../evaluator/) | Independent assessment |
| [soul-chat/](../soul-chat/) | Multi-agent dialogue |
| [persona/](../persona/) | Debaters have personas |
| [card/](../card/) | Data flow ensembles |
| [speed-of-light/](../speed-of-light/) | Many agents, one call |
| [designs/mike-gallaher-ideas.md](../../designs/mike-gallaher-ideas.md) | Origin methodology |

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Structured multi-perspective deliberation using adversarial committees, Robert's Rules, and rubric-based evaluation.

**Origin:** Mike Gallaher's "Stories All the Way Down" + Parliamentary procedure + The Sims autonomous agents.

## Quick Example

```yaml
> PLAY debate.card
> CREATE_TOPIC "Should we adopt microservices?"
> CREATE_SIDE "Pro" position="flexibility, scalability"
> CREATE_SIDE "Con" position="complexity, latency"
> CREATE_MODERATOR style="roberts_rules"
> CREATE_AUDIENCE expertise=["architect", "ops", "dev"]
> START_DEBATE rounds=3
```

## The Gong Show Option

For entertainment-style debates, add celebrity moderators and THE GONG:

```yaml
> CREATE_MODERATOR style="gong_show"
> SUMMON_JUDGES ["jaye_p_morgan", "arte_johnson", "rip_taylor"]
> GONG  # Mercifully end a failing argument
```

The gong isn't cruel — it's merciful. Sometimes the kindest thing is to end what isn't working.

## Components

| Component | Role |
|-----------|------|
| **Topic** | The question being debated |
| **Sides** | Generators of arguments (positions) |
| **Moderator** | Transformer — routes, times, enforces rules |
| **Audience** | Consumers — react, score, evaluate |
| **Clock** | Controls round timing |
| **Transcript** | Records everything |

## Commands

| Command | Effect |
|---------|--------|
| `DEBATE [topic]` | Quick-start a debate |
| `CREATE_SIDE [name]` | Add a position |
| `CREATE_MODERATOR` | Add facilitation |
| `MOTION [text]` | Propose for vote |
| `SECOND` | Second a motion |
| `VOTE` | Call the question |

## Templates

| File | Purpose |
|------|---------|
| [DEBATE.yml.tmpl](DEBATE.yml.tmpl) | Debate session state |
| [SIDE.yml.tmpl](SIDE.yml.tmpl) | Position/side definition |
| [TRANSCRIPT.md.tmpl](TRANSCRIPT.md.tmpl) | Debate record |

---

*See [SKILL.md](SKILL.md) for complete specification.*
