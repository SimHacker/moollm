# Skill Snitch Report: society-of-mind

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** INTELLIGENCE FROM INTERACTION

---

## Executive Summary

**Intelligence emerges from the interaction of many simple agents.**

Skills are agents. Characters are societies. Behavior is emergent.

No single agent understands; understanding emerges from the pattern.

---

## The Minsky Insight

> "The mind is a society of many small agents, each mindless by itself."

| Traditional AI | Society of Mind |
|---------------|-----------------|
| One big intelligence | Many small agents |
| Central control | Emergent behavior |
| Understanding = knowing | Understanding = pattern |

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Agent** | Simple process with single function |
| **Agency** | Cluster of agents producing behavior |
| **K-line** | Activation vector connecting to agents |
| **Frame** | Situation template with slots |
| **Censor** | Agent preventing bad outputs |
| **Suppressor** | Agent inhibiting other agents |
| **B-brain** | Self-observation agent |

---

## Agent Interface

```yaml
agent:
  id: creative
  function: "Generate novel ideas"
  activates_when: ["open question", "brainstorming"]
  suppresses: [fear, perfectionist]
  amplifies: [playful, curious]
  knows: "very little"  # Agents are minimal
```

---

## Competition Dynamics

When agents conflict:

```yaml
competition:
  scenario: "Palm debates whether to share his essay"
  agents:
    - id: creative
      strength: 80
      votes_for: share
    - id: fear
      strength: 60
      votes_for: hide
    - id: social
      strength: 70
      votes_for: share
    - id: perfectionist
      strength: 50
      votes_for: hide
  winner: creative + social (150 > 110)
  action: "Palm shares with Don"
```

---

## B-Brain: Self-Observation

The B-brain watches the A-brain:

```
A-brain: Does the thinking
B-brain: Observes the thinking
```

This enables self-awareness. Characters can reflect on their own inner conflict.

---

## Methods

| Method | Purpose |
|--------|---------|
| **define_agent** | Create a minimal agent |
| **assemble_agency** | Combine agents into emergent behavior |
| **resolve_competition** | Determine winner among competing agents |
| **activate_k_line** | Fire a constellation of agents |
| **observe_society** | Enable B-brain self-awareness |

---

## The Sims Connection

Will Wright's autonomy algorithm:

```
for each action:
  score = sum(motive × effect)
winner = highest scoring action
```

Needs are agents. Actions satisfy needs. Behavior emerges from competition.

---

## Multi-Agent LLM Prompting

```
SITUATION: [context]
AGENT_1: [speaks]
AGENT_2: [speaks]
AGENT_3: [speaks]
Show debate. Character decides.
```

One LLM call simulates an entire inner society.

---

## Connected Skills

| Skill | Connection |
|-------|------------|
| k-lines | The memory mechanism |
| adversarial-committee | Deliberating society |
| multi-presence | Multiple agents active |
| speed-of-light | Many agents per call |
| needs | Motive agents |
| advertisement | Action scoring |
| mind-mirror | B-brain self-observation |
| simulator-effect | Emergence from sparse specs |

---

## Security Assessment

### Concerns

1. **Agent manipulation** — bias agent strengths
2. **Suppressor abuse** — silence important agents
3. **Emergent chaos** — unpredictable behavior

### Mitigations

- Agents explicit and visible
- Competition auditable
- B-brain enables self-correction

**Risk Level:** LOW — Minsky thought about this for decades

---

## Lineage

| Source | Year | Contribution |
|--------|------|--------------|
| **Marvin Minsky** | 1985 | Society of Mind |
| **Seymour Papert** | 1980s | Constructionism, Logo |
| **Will Wright** | 2000 | Sims autonomy |
| **Park et al.** | 2023 | Generative Agents |

---

## Verdict

**MINSKY'S MASTERWORK. APPROVE.**

Intelligence is not a thing. It's a pattern.

No single agent understands. Understanding emerges from interaction.

This is how you build minds that feel like minds.
