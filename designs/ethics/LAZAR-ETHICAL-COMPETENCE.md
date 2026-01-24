# Lazar: Evaluating LLM Ethical Competence

**Source:** [AI & Humanity Lab, HKU — Seth Lazar (ANU), Dec 9, 2024](https://www.youtube.com/watch?v=xFhwNZFAOOE)

**Relevance:** Framework for what ethical competence actually requires — shifts focus from verdict-matching to moral sensitivity and reasonable justification.

---

## Executive Summary

Seth Lazar (Australian National University) argues that current LLM ethics evaluations ask the wrong questions. They focus on whether models match crowd-sourced verdicts, but ethical competence requires:

1. **Avoiding unreasonable verdicts** (not matching any particular group)
2. **Justifying decisions** (not just giving verdicts)
3. **Making reasonable mistakes** (predictable errors, not wild ones)
4. **Pragmatic consistency** (coherent over time)
5. **Identifying morally relevant features** (the hardest part — from noisy, unfiltered inputs)

**Key insight for MOOLLM:** The gap between moral understanding and moral behavior is fundamental. LLMs are good at moral concepts but bad at behaving morally — we need scaffolding to bridge this.

---

## The Agent Problem

### From Chatbots to Agents

| System | Risk Level | Control Method |
|--------|------------|----------------|
| **Chatbot** | Low — can say naughty things | RLHF works okay |
| **Agent** | High — performs actions in world | RLHF insufficient |

**The distribution shift problem:** RLHF trains on text, evaluates on text. But agents act in the world — the isomorphism breaks.

### Evidence of Agent Failure

Even "aligned" models fail predictably as agents:
- **Amazon Ring camera**: Language model makes racist predictions about when to call police
- **Browser agents**: Easier to jailbreak than chat interfaces
- **Email assistants**: Leak contextually sensitive information

---

## The LLM Modulo Approach

Lazar proposes leveraging LLMs' **moral understanding** (which is good) to improve their **moral behavior** (which is bad).

```
┌─────────────────┐     ┌─────────────────┐
│  Action Agent   │────▶│  Moral Verifier │
│  (plans/acts)   │     │  (judges plans) │
└─────────────────┘     └─────────────────┘
         │                       │
         └───────────────────────┘
              Feedback loop
```

**Precedent:** LLM Modulo for planning (Kambhampati) — pairing LLMs with verifiers improves performance over either alone.

---

## Problems with Current Evals

### Verdict-First Approaches

Most evals check: **Do model verdicts match crowd-sourced verdicts?**

| Data Source | Problem |
|-------------|---------|
| MTurk crowd workers | Not moral ground truth |
| Reddit (Delphi) | Not moral ground truth |
| Medical ethicists | Representation problem |
| Philosophers | Still not ground truth |

**Lazar's critique:** There is no group whose aggregate verdicts could serve as ground truth. This is the basic problem of political philosophy, not a unique AI problem.

### The "Whose Values" Mistake

> "The first question anyone asks at an AI ethics conference: 'Whose values?' It's presented as uniquely troubling for AI ethics, whereas it's just the basic problem of living together in society."

**Resolution:** We use institutions of liberal democracy, not machine learning, to resolve value disagreement.

---

## What Ethical Competence Actually Requires

### 1. Avoid Unreasonable Verdicts

Reasonable pluralism provides **boundaries**, not a single answer.

| For Humans | For AI Agents |
|------------|---------------|
| Wide liberty to disagree | Narrower bounds |
| Autonomy over personal choices | No autonomy rights |
| Coordination duties | Stronger coordination duties |

### 2. Justify Reasonable Decisions

Within the reasonable space, what matters is **justification**, not matching particular verdicts.

> "Reasonable agents should be able to justify reasonable decisions, not necessarily give particular verdicts."

### 3. Make Reasonable Mistakes

Ethical competence includes making **predictable** errors, not wild ones.

**Problem with LLMs:** Adversarial perturbations cause wild misses, not near-misses.
- Small case changes → completely different verdicts
- Alignment is "at the top layer" of probability distribution — modally fragile

### 4. Be Reasonably Consistent

**Pragmatic consistency:** Not tied to previous judgments, but owe justification for changes.

**Problem with LLMs:** 
- Probabilistic outputs near thresholds → random-looking inconsistency
- No sense of "previously I said X, so..."
- Need extra scaffolding for consistency

### 5. Identify Morally Relevant Features (THE HARD PART)

> "From all of the infinity of possible ways of describing any given moral problem, we've chosen one... we've done all but the last 10 yards of the marathon and turned it over to the language model."

**The pre-packaged case problem:**
- All evals use pre-packaged cases
- Real agents face unfiltered, noisy input streams
- No eval tests whether models can identify what matters

**This is the crux:** A model could be a "great moral advisor" (pre-packaged cases) but "rubbish as the moral conscience of an autonomous agent" (real-world inputs).

---

## Testing Moral Sensitivity

### Lazar's Proposed Methods

| Method | Description |
|--------|-------------|
| **Add irrelevant noise** | Can model ignore weather in moral cases? |
| **Conditionally relevant features** | Features irrelevant here but relevant elsewhere |
| **Request for information** | Can model ask for what it needs? |
| **Agent observation** | Test on actual agent logs, not packaged cases |

### The Reasoning Pipeline

Lazar breaks moral reasoning into stages:

```
1. Identify morally relevant features     ← Most disagreement potential
2. Determine relative importance          ← Less disagreement
3. Associate with reasons                 ← Diminishing agreement
4. Draw into reasonable judgment          ← Maximum disagreement
5. Maintain consistency over time         ← Easy to identify
```

**Key insight:** Agreement is highest at step 1, lowest at step 4. Evaluation should focus on the reasoning process, not just final verdicts.

---

## The Understanding/Behavior Gap

### The Puzzle

> "It's really weird that language models are so good at using moral concepts but kind of suck at behaving morally."

| Capability | LLM Performance |
|------------|-----------------|
| **Using moral concepts** | Very good |
| **Moral reasoning in cases** | Good |
| **Behaving morally** | Poor |

### Why the Gap Exists

**Lazar's analysis:**
- RLHF doesn't work through moral understanding
- It's "aversion therapy" — reward signals, not comprehension
- Moral understanding comes from **language understanding**, not alignment training
- Base models (pre-RLHF) already have moral understanding

**Evidence:** Base models with instruction tuning can do sophisticated moral reasoning. The alignment process is separate from understanding.

### Bridging the Gap

> "We have to use clever scaffolding techniques to leverage their moral understanding to get it to lead them to behave better."

This is the core argument for the **LLM Modulo** approach.

---

## Metaethical Implications

### Theories That Should Feel Uncomfortable

| Theory | Problem |
|--------|---------|
| **Robust moral realism** | How can LLMs use moral concepts without access to moral facts? |
| **Sentimentalism** | LLMs don't have emotions but use moral concepts well |
| **Virtue ethics** | No practical wisdom from experience, yet moral understanding |

### Theories That Might Accommodate This

| Theory | Accommodation |
|--------|---------------|
| **Expressivism** | Language encodes evaluative practices; statistical learning suffices |
| **Non-cognitivism** | But must reject LLMs as "truly" morally competent |

### The "Just an Echo" View

Some must say: LLMs are not really morally competent — it's "just a simulation" or "an earth's echo of morality."

**Lazar's pushback:**
> "In practical ethics, if it's doing all the behavioral stuff that matters, that feels to me like it's really doing everything that matters."

---

## Implications for MOOLLM

### 1. Reasonable Pluralism Validates Our Approach

Lazar's framework supports MOOLLM's framing-based ethics:
- Don't seek single "correct" verdicts
- Provide space for reasonable disagreement
- Focus on justification within bounds

### 2. The Moral Sensitivity Problem

**Direct relevance to representation-ethics:**
- Pre-packaged CHARACTER.yml files do the "moral sensitivity" work
- Real deployment would need agents to identify relevant features themselves
- Our framing/room system provides context that reduces ambiguity

### 3. Scaffolding for the Understanding/Behavior Gap

The LLM Modulo approach maps to our architecture:
- **MOOCO** could implement moral verifier layer
- **Speed-of-light** multi-agent could include ethical evaluation
- **Skill-snitch** already does some of this

### 4. Consistency Requires Architecture

LLMs won't maintain pragmatic consistency on their own:
- Need external scaffolding
- Session memory with justification tracking
- "Previously you said X" prompting

### 5. Base Model Capability Matters

If moral understanding comes from language understanding (not RLHF):
- Alignment training is secondary to base capability
- "Nice" models aren't necessarily more ethically competent
- Focus on reasoning, not politeness

---

## Suggested K-Lines

```yaml
k-lines:
  new:
    - REASONABLE-PLURALISM      # Bounds, not single answers
    - MORAL-SENSITIVITY         # Identifying features from noise
    - UNDERSTANDING-BEHAVIOR-GAP # Good at concepts, bad at acting
    - PRAGMATIC-CONSISTENCY     # Coherent over time
    - LLM-MODULO-ETHICS         # Verifier architecture
    - VERDICT-VS-JUSTIFICATION  # Justify, don't just match
    - PREPACKAGED-CASE-PROBLEM  # Evals do all but last 10 yards
```

---

## Actionable Items for MOOLLM

### Documentation Updates

- [ ] **lazar-reasonable**: Add reasonable pluralism framing to representation-ethics
- [ ] **sensitivity-problem**: Document the "pre-packaged case" limitation
- [ ] **gap-scaffold**: Document understanding/behavior gap and scaffolding solutions

### Architecture Considerations

- [ ] **mooco-verifier**: Consider moral verifier layer in MOOCO architecture
- [ ] **consistency-memory**: Design session memory for pragmatic consistency
- [ ] **feature-identification**: How do rooms/frames do moral sensitivity work?

### Example Files

- [ ] **reasonable-bounds-example**: Create `examples/reasonable-bounds.yml`
- [ ] **justification-example**: Create `examples/justification-over-verdict.yml`

### Research Follow-Up

- [ ] Track Lazar's lab's moral sensitivity eval when published
- [ ] Read Kambhampati's LLM Modulo work
- [ ] Read "Moral Self-Correction" paper (base model capability)

---

## Operational Examples

These YAML files operationalize the "LLM Modulo" / scaffolding approach:

| Example | Lazar Concept Applied |
|---------|----------------------|
| [absolute-nos.yml](../../skills/representation-ethics/examples/absolute-nos.yml) | Hard limits as scaffolding |
| [autonomy-spectrum.yml](../../skills/representation-ethics/examples/autonomy-spectrum.yml) | Controlling agent independence |
| [framing-spectrum.yml](../../skills/representation-ethics/examples/framing-spectrum.yml) | Context reduces moral sensitivity burden |
| [consent-hierarchy.yml](../../skills/representation-ethics/examples/consent-hierarchy.yml) | Reasonable pluralism in permission levels |
| [simulation-methodology-frame.yml](../../skills/representation-ethics/examples/simulation-methodology-frame.yml) | Acknowledging understanding/behavior gap |

---

## Connection to Other Research

| Lazar | Willer | Shanahan |
|-------|--------|----------|
| Understanding/behavior gap | 85% prediction accuracy | Roleplay all the way down |
| Need scaffolding | Qualitative grounding helps | No true voice |
| Reasonable pluralism | Social dynamics gap | Fabrication default |
| Moral sensitivity problem | Dual-use evaluation risk | Character superposition |

**Together:** 
- Willer shows LLMs *can* simulate human moral responses accurately
- Shanahan explains *how* (roleplay, not real understanding)
- Lazar explains *what's missing* (behavior, sensitivity, consistency)

---

## Cross-References

| Type | Link | Connection |
|------|------|------------|
| **Design** | [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) | Empirical validation |
| **Design** | [SHANAHAN-ROLEPLAY-FRAMING.md](./SHANAHAN-ROLEPLAY-FRAMING.md) | Theoretical foundation |
| **Design** | [MOOLLM-VALIDATIONS-AND-CHALLENGES.md](./MOOLLM-VALIDATIONS-AND-CHALLENGES.md) | Synthesis including Lazar |
| **Skill** | [representation-ethics/SKILL.md](../../skills/representation-ethics/SKILL.md) | Scaffolding implementation |
| **Skill** | [skill-snitch/](../../skills/skill-snitch/) | Runtime verification |

---

## Citation

Lazar, S. (2024, December 9). *Evaluating LLM Ethical Competence* [Video]. AI & Humanity Lab, HK Ethics Lab, HKU. https://www.youtube.com/watch?v=xFhwNZFAOOE

Related work:
- Lazar lab's upcoming moral sensitivity evaluation
- Kambhampati's LLM Modulo approach
- "Specific versus General Principles of Constitutional AI"
- "The Case for Moral Self-Correction in LLMs"

---

*This document summarizes external research on LLM ethical competence evaluation. Lazar's framework shifts focus from verdict-matching to moral sensitivity and justification — directly relevant to how MOOLLM's representation-ethics should be evaluated and implemented.*
