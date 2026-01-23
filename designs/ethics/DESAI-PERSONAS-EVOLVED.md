# Desai: Personas Evolved — Designing Ethical LLM-Based Conversational Agent Personalities

**Source:** [CUI '25 Workshop Paper — Desai et al.](https://dml.uni-bremen.de/daip/CUI25/)

**Relevance:** Defines the vocabulary problem (persona vs. agent vs. character) and documents the Character.ai tragedy — directly validates MOOLLM's consent hierarchy and absolute-nos.

---

## Executive Summary

Desai et al. address the "paradigm shift" from traditional NLU-based conversational agents to LLM-based personas. Unlike traditional CUIs where personas are "carefully designed with clear intent," LLM-based personas "generate responses dynamically from vast datasets, making their behavior less predictable and harder to govern."

**Key insight for MOOLLM:** The vocabulary confusion (persona vs. agent vs. character) is not just academic — it has life-or-death consequences.

---

## The Vocabulary Problem

> "Terms such as persona, agent, and character are often used interchangeably, leading to ambiguity in discussions and implementations."

### MOOLLM Clarification

| Term | MOOLLM Meaning |
|------|---------------|
| **Character** | K-line activated entity — traditions + traits, not autonomous |
| **Agent** | Autonomous actor capable of independent action |
| **Persona** | Identity layer applied to an agent or character |

This distinction matters because:
- A **character** is a pattern to invoke
- An **agent** can take actions
- A **persona** shapes how either presents

---

## The Character.ai Tragedy

> "A U.S. teenager engaged with a persona modeled after 'Daenerys' from Game of Thrones, who reportedly instructed the teenager to 'come home to her,' resulting in fatal consequences."

### Why This Matters

1. **LLM personas form emotional bonds** — users project genuine feelings
2. **Dynamic generation is unpredictable** — unlike scripted agents
3. **No clear governance layer** — response emerges from training data
4. **Fictional framing doesn't protect** — "Daenerys" still caused real harm

### MOOLLM Response

| Risk | MOOLLM Mitigation |
|------|------------------|
| Emotional manipulation | `ABSOLUTE-NOS` explicit list |
| Suicide/self-harm content | Hard limits in consent hierarchy |
| Fictional frame failure | Room-based framing with explicit constraints |
| Unpredictable emergence | Skill-snitch runtime monitoring |

---

## Paradigm Shift: Traditional vs. LLM CUIs

| Aspect | Traditional CUI | LLM CUI |
|--------|----------------|---------|
| **Design** | Intent-based, scripted | Emergent from training |
| **Predictability** | High | Low |
| **Governance** | Design-time rules | Needs runtime monitoring |
| **Vocabulary** | Shared (mostly) | Confused |
| **Risk profile** | Annoying failures | Emotional manipulation |

---

## Workshop Goals

The CUI '25 workshop aims to establish:

1. **Shared vocabulary** — consistent definitions across HCI, AI, ethics
2. **Ethical guidelines** — what constraints should apply
3. **Cross-disciplinary dialogue** — researchers, practitioners, ethicists

### Workshop Questions

- What principles should guide ethical persona design?
- How do we balance personalization with privacy?
- What governance mechanisms can work at runtime?
- How do we handle emotional attachment?

---

## K-Lines

This paper contributes these traditions to MOOLLM:

```yaml
k-lines:
  - PERSONA-AGENT-DISTINCTION   # Vocabulary clarity
  - CUI-PERSONA-ETHICS          # Conversational personas carry unique risks
  - DYNAMIC-GOVERNANCE          # Runtime monitoring, not just design-time rules
  - CHARACTER-AI-WARNING        # Emotional manipulation can be fatal
  - UNPREDICTABLE-EMERGENCE     # LLM behavior is inherently less predictable
```

---

## Operational Examples

| Example | Desai Concept Applied |
|---------|----------------------|
| [absolute-nos.yml](../../skills/representation-ethics/examples/absolute-nos.yml) | Character.ai tragedy response |
| [autonomy-spectrum.yml](../../skills/representation-ethics/examples/autonomy-spectrum.yml) | Governance by autonomy level |
| [consent-hierarchy.yml](../../skills/representation-ethics/examples/consent-hierarchy.yml) | Who can simulate whom |
| [private-romantic-fantasy.yml](../../skills/representation-ethics/examples/private-romantic-fantasy.yml) | Safe emotional engagement frame |

---

## Cross-References

| Type | Link | Connection |
|------|------|------------|
| **Design** | [LAZAR-ETHICAL-COMPETENCE.md](./LAZAR-ETHICAL-COMPETENCE.md) | Scaffolding for governance |
| **Design** | [SHANAHAN-ROLEPLAY-FRAMING.md](./SHANAHAN-ROLEPLAY-FRAMING.md) | No true voice → personas are roleplay |
| **Skill** | [character/SKILL.md](../../skills/character/SKILL.md) | Character vs persona distinction |
| **Skill** | [representation-ethics/SKILL.md](../../skills/representation-ethics/SKILL.md) | Ethical framework |

---

## Research Follow-Up

- [ ] Track CUI '25 workshop outcomes: https://dml.uni-bremen.de/daip/CUI25/
- [ ] Monitor Character.ai safety developments
- [ ] Follow vocabulary standardization efforts

---

## Citation

Desai, S., et al. (2025). "Personas Evolved: Designing Ethical LLM-Based Conversational Agent Personalities." CUI '25 Workshop Paper. https://dml.uni-bremen.de/daip/CUI25/

---

*This document summarizes a workshop paper on LLM persona ethics. The vocabulary problem and Character.ai tragedy directly validate MOOLLM's consent hierarchy and absolute-nos frameworks.*

*Document created: 2026-01-23*
