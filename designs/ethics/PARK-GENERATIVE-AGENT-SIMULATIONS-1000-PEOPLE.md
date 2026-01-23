# Generative Agent Simulations of 1,000 People

**Source**: Park, Zou, Shaw, Hill, Cai, Morris, Willer, Liang & Bernstein (2024)
**arXiv**: [2411.10109](https://arxiv.org/abs/2411.10109)
**Coverage**: [Stanford HAI](https://hai.stanford.edu/news/ai-agents-simulate-1052-individuals-personalities-with-impressive-accuracy), [MIT Tech Review](https://www.technologyreview.com/), [Nature News](https://www.nature.com/)

---

## Executive Summary

The Stanford team that created Generative Agents (Smallville) has developed a method to create agents that simulate **real individuals** with unprecedented accuracy. By using 2-hour qualitative interviews rather than demographic prompts, agents achieve **85% normalized accuracy** — meaning they replicate human responses 85% as accurately as humans replicate their own responses two weeks later.

**Key breakthrough**: Interviews capture *idiosyncrasies* that prevent demographic stereotyping.

---

## The Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Interview-Based Agent Architecture               │
│                                                                     │
│   ┌─────────────────┐                                               │
│   │  2-Hour Voice   │                                               │
│   │   Interview     │ ────► 6,491 words avg                         │
│   │  (AI Interviewer)│                                               │
│   └────────┬────────┘                                               │
│            │                                                        │
│            ▼                                                        │
│   ┌─────────────────┐                                               │
│   │ Expert Reflection│                                               │
│   │    Module        │                                               │
│   │                  │                                               │
│   │ 🧠 Psychologist  │ → personality, coping, relationships         │
│   │ 📊 Economist     │ → risk preference, financial behavior        │
│   │ 🗳️ Pol. Scientist│ → ideology, partisan identity                │
│   │ 📈 Demographer   │ → social position, life trajectory           │
│   └────────┬────────┘                                               │
│            │                                                        │
│            ▼                                                        │
│   ┌─────────────────┐                                               │
│   │  Generative     │                                               │
│   │    Agent        │ ────► Responds to any textual stimulus        │
│   │                 │                                               │
│   │ • Full transcript│                                               │
│   │ • Expert insights│                                               │
│   │ • Task memory    │                                               │
│   └─────────────────┘                                               │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Architectural Innovations

1. **AI Interviewer Agent**: Semi-structured interviews with dynamic follow-up questions
2. **Expert Reflection Module**: LLM synthesizes interview from 4 domain expert perspectives
3. **Full Transcript Injection**: Entire interview (not summary) used for response generation
4. **Chain-of-Thought Prompting**: Systematic reasoning about option interpretation → choice reasoning → response

---

## The Results

### Normalized Accuracy

The key innovation: benchmark agent accuracy against *human self-consistency*.

| Construct | Agent Accuracy | Human Self-Consistency | Normalized Accuracy |
|-----------|----------------|------------------------|---------------------|
| **General Social Survey** | 68.85% | 81.25% | **0.85** |
| **Big Five Personality** | r=0.78 | r=0.95 | **0.80** |
| **Economic Games** | r=0.66 | r=0.99 | **0.66** |

**Interpretation**: A normalized accuracy of 0.85 means agents predict responses 85% as accurately as humans replicate their own responses two weeks later.

### Comparison with Alternative Approaches

| Agent Type | GSS Normalized Accuracy | Why It Matters |
|------------|------------------------|----------------|
| **Interview-based** | 0.85 | Captures idiosyncrasies |
| **Demographic-based** | 0.71 | Relies on stereotypes |
| **Persona-based** | 0.70 | Self-description too brief |
| **Survey+Experiment** | 0.76 | Still misses depth |

**Key finding**: Interviews outperform even composite agents using all survey/experiment data.

### Experimental Replication

Agents replicated 4 of 5 canonical social science experiments — the same 4 that human participants replicated:

| Study | Human Replication | Agent Replication | Effect Size Correlation |
|-------|-------------------|-------------------|------------------------|
| Ames & Fiske (harm/intent) | ✓ | ✓ | |
| Cooney et al. (fairness) | ✓ | ✓ | |
| Halevy & Halali (conflict) | ✓ | ✓ | |
| Rai et al. (dehumanization) | ✗ | ✗ | |
| Schilke et al. (power/trust) | ✓ | ✓ | |
| **Overall correlation** | — | — | **r=0.98** |

---

## Bias Reduction

### The Demographic Parity Difference

Interview-based agents consistently reduce accuracy gaps across demographic groups:

| Dimension | Demographic Agents (DPD) | Interview Agents (DPD) | Improvement |
|-----------|-------------------------|------------------------|-------------|
| Political Ideology | 12.35% | 7.85% | -4.5 points |
| Race | 3.33% | 2.08% | -1.25 points |
| Gender | 0.56% | 0.54% | (minimal) |

**Key insight**: "The beauty of having interview data is that it includes people's idiosyncrasies and therefore the language models don't resort to making race-based generalizations as often."

---

## The Agent Bank: Ethical Access Framework

### Two-Pronged Access System

```
┌───────────────────────────────────────────────────────────────┐
│                    Agent Bank Access Model                     │
│                                                                │
│   ┌──────────────────────┐   ┌──────────────────────────────┐ │
│   │   OPEN ACCESS        │   │   RESTRICTED ACCESS          │ │
│   │                      │   │                              │ │
│   │ • Aggregated data    │   │ • Individual responses       │ │
│   │ • Fixed tasks        │   │ • Open tasks                 │ │
│   │ • Subpopulation      │   │ • Custom questions           │ │
│   │   queries            │   │ • API access                 │ │
│   │                      │   │                              │ │
│   │ Usage agreement      │   │ Research proposal +          │ │
│   │ only                 │   │ Privacy assurances           │ │
│   └──────────────────────┘   └──────────────────────────────┘ │
│                                                                │
│   ┌──────────────────────────────────────────────────────────┐ │
│   │                   SAFEGUARDS                              │ │
│   │                                                          │ │
│   │ • Usage audit logs for every agent                       │ │
│   │ • Participant withdrawal rights (25 year window)         │ │
│   │ • Non-commercial use agreements                          │ │
│   │ • Privacy risk reassessment as models improve            │ │
│   │ • Individuals can see what their agents are doing        │ │
│   └──────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────┘
```

### Consent Protocol

Participants were explicitly informed:

1. Data will create AI models simulating how they "might behave in specific situations"
2. Despite de-identification, information could potentially be shared
3. Models may become "increasingly powerful over time"
4. They can withdraw consent at any time for 25 years
5. They will be informed of "significant changes in model capabilities"

---

## Implications for MOOLLM

### What This Validates

| MOOLLM Concept | Validation from Paper |
|----------------|----------------------|
| **Scaffolding approach** | Expert reflection module = scaffolded reasoning |
| **Frame-based ethics** | Context (interview) transforms accuracy, not just rules |
| **Human checkpoints** | Agent bank requires human oversight for restricted access |
| **Consent hierarchy** | Two-pronged access models consent levels |
| **Qualitative grounding** | Interviews >> demographics for individual simulation |

### What This Challenges

| MOOLLM Assumption | Challenge |
|-------------------|-----------|
| "Can't simulate individuals" | At 85% normalized accuracy, individual simulation is viable |
| "Experience deficit" | 2-hour interviews capture substantial lived experience |
| "Herd behavior in multi-agent" | Not addressed — single-agent simulations only |

### New Insights for MOOLLM

1. **Interview Protocol as Skill**
   - Could MOOLLM develop an interview protocol for character creation?
   - Semi-structured interviews with AI interviewer for deep character knowledge

2. **Expert Reflection Pattern**
   - Multi-perspective synthesis (psychologist, economist, etc.)
   - MOOLLM could use domain experts for character analysis

3. **Normalized Accuracy Metric**
   - Benchmark agent accuracy against human self-consistency
   - More meaningful than raw accuracy

4. **Idiosyncrasy Preservation**
   - Rich data prevents stereotyping
   - MOOLLM characters should capture quirks, not archetypes

5. **Agent Bank Governance Model**
   - Audit logs, withdrawal rights, tiered access
   - Model for MOOLLM's ethical character management

---

## New K-lines to Consider

| K-line | Concept |
|--------|---------|
| `INTERVIEW-GROUNDING` | Qualitative interviews capture idiosyncrasies that prevent stereotyping |
| `NORMALIZED-ACCURACY` | Benchmark agent accuracy against human self-consistency |
| `EXPERT-REFLECTION` | Multi-domain synthesis (psychology, economics, politics, demography) |
| `AGENT-BANK-ETHICS` | Access controls, audit logs, withdrawal rights for simulation subjects |
| `IDIOSYNCRASY-PRESERVATION` | Rich individual detail prevents demographic stereotyping |
| `SELF-CONSISTENCY-BENCHMARK` | Human baseline (test-retest) as evaluation standard |

---

## Comparison with Other Papers

| Paper | Core Insight | Relationship to This Paper |
|-------|--------------|---------------------------|
| **Smallville (2023)** | Emergent social behavior | Same team — moved from fictional to real individuals |
| **Wang ICLR Blog** | Can't simulate individuals | This paper directly addresses with 85% accuracy |
| **Willer (2025)** | 85% aggregate accuracy | Same Willer — this paper extends to individuals |
| **Shanahan** | Roleplay all the way down | Validated — interview enables better roleplay |
| **Lazar** | Need scaffolding | Expert reflection = scaffolding pattern |
| **Wang Survey** | Dual challenge | Addresses design side with interview architecture |

---

## Actionable Items for MOOLLM

### Documentation Updates
- [ ] Create `examples/interview-grounded-character.yml` — character from interview data
- [ ] Add `INTERVIEW-GROUNDING` to CARD.yml K-lines
- [ ] Update ethics README with seven-talk synthesis

### Architecture Considerations
- [ ] Design interview protocol for deep character creation
- [ ] Consider expert reflection pattern for character analysis
- [ ] Evaluate normalized accuracy metric for MOOCO

### Ethical Framework
- [ ] Model agent bank governance for MOOLLM characters
- [ ] Design consent protocol for real-person characters
- [ ] Consider audit log pattern for character usage

### Research Follow-up
- [ ] Monitor Stanford team's agent bank research
- [ ] Track applications of interview-based grounding
- [ ] Evaluate 20% vs 80% interview lesion findings (even 20% interviews outperform surveys)

---

## Quotes Worth Preserving

> "The language model is trying to role-play as the person it just interviewed. In addition to the interview script, the agent relies on all of the psychological and social science expertise that is embedded in the LLM. It's a very powerful combination."
> — Joon Sung Park

> "The beauty of having interview data is that it includes people's idiosyncrasies and therefore the language models don't resort to making race-based generalizations as often."
> — Joon Sung Park

> "A generative agent can be thought of as a new way of taking a self-portrait that tells a rich story about who a person is, but it is still a computational entity... like our genomic data, it should belong to and be controlled by the person whose portrait it represents."
> — Park et al.

> "I really do think there are many societal problems we're failing to address right now that could be made easier with this testbed."
> — Joon Sung Park

---

## The Bottom Line

This paper represents a paradigm shift: from "LLMs can't simulate individuals" to "LLMs can simulate individuals with 85% normalized accuracy when grounded in qualitative interviews."

The interview-based approach:
- Captures idiosyncrasies that prevent stereotyping
- Reduces demographic bias in predictions
- Enables individual-level accuracy benchmarking
- Provides a governance model for ethical simulation

For MOOLLM, this validates the scaffolding approach while suggesting that **rich qualitative grounding** — not just rules and frames — is essential for ethical individual simulation.

---

## Operational Examples

These YAML files operationalize the concepts from this design doc:

| Example | What It Does |
|---------|--------------|
| [interview-grounded-character.yml](../../skills/representation-ethics/examples/interview-grounded-character.yml) | How to create characters from qualitative data |
| [agent-bank-governance.yml](../../skills/representation-ethics/examples/agent-bank-governance.yml) | Ethical access controls for simulation agents |
| [expert-reflection-synthesis.yml](../../skills/representation-ethics/examples/expert-reflection-synthesis.yml) | Multi-domain expert analysis of characters |
| [experience-accumulation.yml](../../skills/representation-ethics/examples/experience-accumulation.yml) | Character learning over time |
| [consent-hierarchy.yml](../../skills/representation-ethics/examples/consent-hierarchy.yml) | Who can simulate whom |

---

## See Also

**Related Design Docs:**
- [GENERATIVE-AGENTS-SMALLVILLE.md](./GENERATIVE-AGENTS-SMALLVILLE.md) — The original 2023 paper (same team)
- [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) — Same team's earlier findings
- [WANG-LLM-SIMULATION-LIMITS.md](./WANG-LLM-SIMULATION-LIMITS.md) — The limitation this paper addresses
- [VALUE-PROMPTING-SCHWARTZ.md](./VALUE-PROMPTING-SCHWARTZ.md) — Simpler value-based alternative

**Skills:**
- [representation-ethics/SKILL.md](../../skills/representation-ethics/SKILL.md) — Full ethical framework
- [character/SKILL.md](../../skills/character/SKILL.md) — Character construction patterns
- [incarnation/SKILL.md](../../skills/incarnation/SKILL.md) — Deep character embodiment
