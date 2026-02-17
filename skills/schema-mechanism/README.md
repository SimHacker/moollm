# Schema Mechanism

> *"An agent learns by discovering reliable patterns: when I do X in context C, result R tends to follow."*

Formal interface: [CARD.yml](./CARD.yml). Implementation protocol: [SKILL.md](./SKILL.md).

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [constructionism/](../constructionism/) | Papert's educational philosophy |
| [society-of-mind/](../society-of-mind/) | Drescher extended Minsky's agents |
| [leela-ai/](../leela-ai/) | Leela applies Drescher to manufacturing |
| [manufacturing-intelligence/](../manufacturing-intelligence/) | Drescher in the lineage |
| [play-learn-lift/](../play-learn-lift/) | Schema learning as methodology |
| [planning/](../planning/) | Dijkstra through schema graph |
| [yaml-jazz/](../yaml-jazz/) | YAML provides skeleton, LLM provides soul |

Gary Drescher's *Made-Up Minds* (1991) — a computational theory of causal learning that MOOLLM extends with LLM semantic understanding.

## Quick Start

A **schema** is a causal unit:

```
Context → Action → Result
```

Agents discover schemas through experience, then refine them via **marginal attribution**.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Schema** | Context → Action → Result |
| **Extended Context** | Discover prerequisites by tracking success correlations |
| **Extended Results** | Discover side effects by tracking what changes |
| **Synthetic Item** | Invent hidden state to explain unpredictable success |
| **Composite Action** | Chain schemas via Dijkstra planning |

## How LLMs Extend the Mechanism

| Aspect | Deterministic | LLM + YAML Jazz |
|--------|---------------|-----------------|
| Items | Opaque tokens | Grounded meanings |
| Patterns | Statistical correlation | Semantic understanding |
| Spin-offs | Mechanical | Creative generalization |
| Explanations | None | Natural language |

**The YAML provides the skeleton; the LLM provides the soul.**

## Credits

- Gary Drescher — *Made-Up Minds* (1991)
- Marvin Minsky — Society of Mind
- Henry Minsky — pyleela.brain implementation
