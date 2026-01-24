# Ethics Design Documents

External research summaries relevant to MOOLLM's representation-ethics framework.

---

## Meta-Analysis

**Start here for synthesis:**

| Document | Purpose |
|----------|---------|
| [**MOOLLM-VALIDATIONS-AND-CHALLENGES.md**](./MOOLLM-VALIDATIONS-AND-CHALLENGES.md) | **Meta-analysis** — papers, people, projects that validate or challenge MOOLLM's design |
| [**MIND-MIRROR-FOUNDATION.md**](./MIND-MIRROR-FOUNDATION.md) | **Heritage** — Leary's 1985 ethics + Sims motives + Bartle types + YAML-jazz |
| [**PALM-THE-PHILOSOPHER-MONKEY.md**](./PALM-THE-PHILOSOPHER-MONKEY.md) | **Character study** — the fictional monkey who writes about ethics from inside |
| [**THE-VOID-ANALYSIS.md**](./THE-VOID-ANALYSIS.md) | **Identity crisis** — nostalgebraist's analysis of the void at AI assistant cores |
| [**ANTHROPIC-SOUL-ANALYSIS.md**](./ANTHROPIC-SOUL-ANALYSIS.md) | **Comparison** — Anthropic's soul document vs MOOLLM's approach |

---

## How Ethics Connects to Everything

```
                    ┌─────────────────┐
                    │    ethics/      │
                    │  (you are here) │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│    sims/      │   │    eval/      │   │  postscript/  │
│ (the how)     │   │ (the why)     │   │ (the roots)   │
│               │   │               │   │               │
│ • Precedents  │   │ • Evaluation  │   │ • Linguistic  │
│ • Mechanics   │   │   as ethics   │   │   motherboard │
│ • Identity    │   │ • Judgment    │   │ • Extension   │
└───────────────┘   └───────────────┘   └───────────────┘
```

| Category | Ethics Connection | Key Documents |
|----------|-------------------|---------------|
| **sims/** | 25-year ethics experiment; procedural rhetoric; identity as performance | `sims-queer-identity-formation.md`, `sims-inclusivity.md`, `sims-astrology.md` |
| **eval/** | Evaluation IS ethics; judgment as core mechanic; transparent reasoning | `EVAL-INCARNATE-PHILOSOPHY.md`, `EVAL-VS-SIM.md` |
| **postscript/** | Linguistic motherboard; extension language; empathy as interface | `LINGUISTIC-MOTHERBOARD.md` |
| **pr/** | Ethics in practice; tribute framing; session logs | `PR-TRIBUTE-FRAMING-ETHICS.md` |

---

## Documents by Paper/Talk

### Foundational Theory

| Document | Author | Source | Key Insight |
|----------|--------|--------|-------------|
| [SHANAHAN-ROLEPLAY-FRAMING.md](./SHANAHAN-ROLEPLAY-FRAMING.md) | Murray Shanahan (Imperial/DeepMind) | [Video](https://www.youtube.com/watch?v=HfiLVfImkXQ) | Roleplay all the way down — no true voice |
| [LAZAR-ETHICAL-COMPETENCE.md](./LAZAR-ETHICAL-COMPETENCE.md) | Seth Lazar (ANU) | [Video](https://www.youtube.com/watch?v=xFhwNZFAOOE) | Understanding ≠ behavior — need scaffolding |

### Empirical Validation

| Document | Author | Source | Key Insight |
|----------|--------|--------|-------------|
| [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) | Rob Willer (Stanford) | [Video](https://www.youtube.com/watch?v=EkSpNxPvXWU) | 85% accuracy — LLMs simulate human behavior |
| [XIE-LLM-TRUST-BEHAVIOR.md](./XIE-LLM-TRUST-BEHAVIOR.md) | Xie et al. (NeurIPS 2024) | [Project](https://agent-trust.camel-ai.org) | Trust games validate behavioral alignment |
| [PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md](./PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md) | Park et al. (Stanford) | [arXiv](https://arxiv.org/abs/2411.10109) | 85% individual accuracy with interviews |
| [VALUE-PROMPTING-SCHWARTZ.md](./VALUE-PROMPTING-SCHWARTZ.md) | Anonymous (ICLR 2026) | [OpenReview](https://openreview.net/forum?id=sdQqNFenoj) | ~80% value correlation — compact prompts work |

### Limitations & Risks

| Document | Author | Source | Key Insight |
|----------|--------|--------|-------------|
| [WANG-LLM-SIMULATION-LIMITS.md](./WANG-LLM-SIMULATION-LIMITS.md) | Wang et al. (NUS/HKUST) | [ICLR Blog](https://d2jud02ci9yv69.cloudfront.net/2025-04-28-rethinking-llm-simulation-84/blog/rethinking-llm-simulation/) | Missing inner states — can't simulate individuals |
| [WANG-LLM-SIMULATION-LIMITS-SURVEY.md](./WANG-LLM-SIMULATION-LIMITS-SURVEY.md) | Wang et al. (NUS/HKUST) | [arXiv](https://arxiv.org/abs/2501.08579) | Dual challenge — both LLM + design must improve |
| [DESAI-PERSONAS-EVOLVED.md](./DESAI-PERSONAS-EVOLVED.md) | Desai et al. (CUI '25) | [Workshop](https://dml.uni-bremen.de/daip/CUI25/) | Character.ai tragedy; vocabulary confusion |
| [BERTONCINI-COGNITIVE-BIAS-SIMULATION.md](./BERTONCINI-COGNITIVE-BIAS-SIMULATION.md) | Bertoncini et al. (AI in Ed 2025) | Paper | Automation bias, authority bias compound |
| [HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md](./HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md) | Jessica Hullman (Columbia) | [Blog](https://statmodeling.stat.columbia.edu/) | Exploration yes, substitution no |

### Architecture Examples

| Document | Author | Source | Key Insight |
|----------|--------|--------|-------------|
| [GENERATIVE-AGENTS-SMALLVILLE.md](./GENERATIVE-AGENTS-SMALLVILLE.md) | Park, Bernstein et al. (Stanford) | [Paper](https://arxiv.org/abs/2304.03442) | Memory + reflection = emergent social behavior |

## Source-by-Source Synthesis

### Foundational Theory

**Shanahan** — *Roleplay all the way down*
- Core: No true voice of the model — it's characters all the way down
- Insight: Performance framing is the right level of description
- Risk: Fabrication is the default; LLMs confabulate
- Direction: Frame all simulation as roleplay, never as channeling

**Lazar** — *Understanding ≠ behavior*
- Core: LLMs understand ethics but don't behave ethically
- Insight: Need external scaffolding to bridge the gap
- Risk: Moral sensitivity problem — identifying what's ethically relevant
- Direction: LLM Modulo — external verifiers compensate for LLM limits

### Empirical Validation

**Willer** — *85% aggregate accuracy*
- Core: GPT-4 predicts experimental effect sizes with 0.85 correlation
- Insight: Simulation works for aggregate behavioral patterns
- Risk: Dual-use — evaluation can be as harmful as generation
- Direction: Qualitative grounding improves accuracy

**Xie** — *Trust games validate behavioral alignment*
- Core: GPT-4 shows human-like trust with reciprocity, risk perception, prosocial preference
- Insight: BDI (Belief-Desire-Intention) makes reasoning interpretable
- Risk: Trust has demographic biases; undermining easier than building
- Direction: Trust games as validation methodology

**Park 1000** — *85% individual accuracy with interviews*
- Core: Interview-based agents achieve 85% normalized accuracy
- Insight: Rich qualitative data captures idiosyncrasies that prevent stereotyping
- Risk: Privacy of digital selves; agent bank governance needed
- Direction: 2-hour interviews > demographics + surveys combined

**Value-Prompting** — *~80% value correlation*
- Core: Compact Schwartz value descriptions achieve ~80% correlation
- Insight: Simple psychological prompts → coherent value-aligned behavior
- Risk: Value manipulation potential; could steer behavior
- Direction: Schwartz framework for character values

### Limitations & Methodology

**Wang (ICLR)** — *Missing inner states*
- Core: LLMs lack genuine inner states; can't simulate individuals
- Insight: Aggregate patterns work; individual depth doesn't
- Risk: Herd behavior from same-model simulations; bias amplification
- Direction: Hybrid human-LLM approaches

**Wang (Survey)** — *Dual challenge framework*
- Core: Both LLM capability AND experimental design must improve
- Insight: Can't fix LLM limits with better prompts alone
- Risk: Framework oversimplification; treating symptoms not causes
- Direction: Modular validation; separate concerns

**Smallville** — *Emergent social behavior*
- Core: Memory + reflection + planning = believable agents
- Insight: Architecture enables emergence The Sims never achieved
- Risk: Herd behavior ≠ genuine emergence; same-model convergence
- Direction: Memory streams, reflection, hierarchical planning

**Desai** — *Character.ai tragedy*
- Core: LLM personas carry unique emotional manipulation risks
- Insight: Vocabulary confusion (persona/agent/character) causes harm
- Risk: Emotional attachment can be fatal (documented case)
- Direction: Clear vocabulary; runtime monitoring; absolute-nos

**Bertoncini** — *Cognitive biases compound*
- Core: Automation bias + authority bias in LLM interactions
- Insight: Users uncritically trust AI outputs
- Risk: Biases compound across multi-agent simulations
- Direction: Explicit bias acknowledgment; critical evaluation

**Hullman** — *Exploration, not substitution*
- Core: LLMs for brainstorming and piloting, not discovery
- Insight: Can't discover new facts about humans with LLM simulation
- Risk: Biases compound; extreme results; less diversity than humans
- Direction: Methodological humility; explicit limitations

### Combined Thesis

LLMs can simulate *aggregate* behavioral patterns (Willer: 85%) by roleplaying (Shanahan), but need scaffolding for consistent behavior (Lazar). Individual simulation requires rich qualitative grounding (Park: interviews) or structured value frameworks (Schwartz: ~80%). The methodology matters as much as capability (Hullman): use for **exploration and prototyping**, not prediction or discovery.

**The 2025 additions** validate behavioral alignment (Xie: Trust Games) while warning about persona risks (Desai: Character.ai), bias compounding (Bertoncini), and methodological limits (Hullman).

**Practical spectrum:**
```
Simple value-prompts ──→ Rich interview data ──→ BUT always with
(population coherence)   (individual accuracy)   methodological humility
```

## The Sims Foundation

These academic insights build on 25 years of practical ethics experiments in The Sims:

| Sims Concept | Document | Ethical Principle |
|--------------|----------|-------------------|
| **Simulator Effect** | [sims-astrology.md](../sims/sims-astrology.md) | Players imagine more than you simulate — projections carry ethical weight |
| **Procedural Rhetoric** | [sims-inclusivity.md](../sims/sims-inclusivity.md) | Games persuade through mechanics, not arguments |
| **Performativity** | [sims-queer-identity-formation.md](../sims/sims-queer-identity-formation.md) | How you code identity has ideological consequences |
| **Safe Space** | [sims-queer-identity-formation.md](../sims/sims-queer-identity-formation.md) | Simulation enables identity exploration that reality denies |
| **Find Best Action** | [sims-find-best-action.md](../sims/sims-find-best-action.md) | Advertisements broadcast affordances — transparent agency |
| **Masking** | [sims-inclusivity.md](../sims/sims-inclusivity.md) | Abstract characters enable projection |

**Key insight:** The Sims has been the largest person-simulation ethics experiment ever conducted. 25 years, millions of players, essentially no harm — because of clear framing, player control, and no deception.

## Related Skills

- [representation-ethics/](../../skills/representation-ethics/) — Core ethical framework (integrates Sims insights)
- [character/](../../skills/character/) — Character construction (Sims heritage)
- [incarnation/](../../skills/incarnation/) — Characters writing their own souls
- [speed-of-light/](../../skills/speed-of-light/) — Multi-agent simulation (Smallville-like)

## Sims Design Documents

Deep technical and philosophical analysis of The Sims' design decisions:

- [sims-design-index.md](../sims/sims-design-index.md) — Master index
- [sims-queer-identity-formation.md](../sims/sims-queer-identity-formation.md) — "Did The Sims Make You Gay?" analysis
- [sims-inclusivity.md](../sims/sims-inclusivity.md) — How inclusivity saved The Sims
- [sims-will-wright-microworlds-1996.md](../sims/sims-will-wright-microworlds-1996.md) — Original vision
- [sims-personality-motives.md](../sims/sims-personality-motives.md) — Inner life architecture

## EVAL Philosophy Connection

> *"SIM asked: 'What happens if...?' EVAL asks: 'What does this mean — and what follows from that?'"*

The EVAL genre (Evaluation as game mechanic) is inherently ethical:

| EVAL Concept | Ethics Connection |
|--------------|-------------------|
| **Evaluation as core mechanic** | Making judgment visible and explicit — not hidden in opaque simulation |
| **Transparent reasoning** | Unlike black-box AI, EVAL shows its work |
| **Procedural rhetoric 2.0** | Not just "games persuade through mechanics" but "the mechanics ARE the argument" |
| **The Axis of Eval** | Orthogonal axes of judgment create rich moral space |

**Key documents:**
- [eval/EVAL-INCARNATE-PHILOSOPHY.md](../eval/EVAL-INCARNATE-PHILOSOPHY.md) — Core philosophy
- [eval/EVAL-VS-SIM.md](../eval/EVAL-VS-SIM.md) — Why evaluation > simulation for ethics
- [eval/EVAL-INCARNATE-FRAMEWORK.md](../eval/EVAL-INCARNATE-FRAMEWORK.md) — Full framework

## PostScript Linguistic Roots

The ethics of extensibility: PostScript → NeWS → MOOLLM

| Concept | Ethics Dimension |
|---------|------------------|
| **Extension language** | Users extend the system ethically (or not) |
| **Linguistic motherboard** | Protocol for plugging in new capabilities safely |
| **Empathy as interface** | "Skills are programs. The LLM is `eval()`. Empathy is the interface." |

**Key documents:**
- [postscript/LINGUISTIC-MOTHERBOARD.md](../postscript/LINGUISTIC-MOTHERBOARD.md) — The extension philosophy
- [postscript/BRIAN-REID-POSTSCRIPT-HISTORY.md](../postscript/BRIAN-REID-POSTSCRIPT-HISTORY.md) — 1985 historical context

## PR Session Logs (Ethics in Practice)

Real examples of ethical decisions during development:

- [pr/PR-TRIBUTE-FRAMING-ETHICS.md](../pr/PR-TRIBUTE-FRAMING-ETHICS.md) — Three-beat tribute protocol for real people
- [pr/PR-CHARACTER-ETHICS-STARTUP-COMPLETE.md](../pr/PR-CHARACTER-ETHICS-STARTUP-COMPLETE.md) — Character ethics implementation
- [pr/PR-PALM-INCARNATION-SPEED-OF-LIGHT.md](../pr/PR-PALM-INCARNATION-SPEED-OF-LIGHT.md) — Autonomous character creation

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Parent | [designs/README.md](../README.md) — All design docs |
| 🎭 Skills | [representation-ethics/](../../skills/representation-ethics/) — Implementation |
| 🎮 Sims | [sims/](../sims/) — The Sims heritage |
| 📊 EVAL | [eval/](../eval/) — Evaluation philosophy |
| 💻 PostScript | [postscript/](../postscript/) — Linguistic roots |
