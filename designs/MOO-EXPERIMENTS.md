# MOO Experiments: LLM Simulation Comparative Studies

A proposal for systematic experiments comparing LLM models using MOOLLM's adventure-4 microworld, leveraging Cursor's trivial model switching and git branches for reproducible iteration tracking.

---

## Executive Summary

MOOLLM provides a unique platform for LLM behavioral simulation research:
- **Rich character ecosystem** — adventure-4 has diverse, well-documented characters
- **Cursor integration** — trivial to switch between Claude, GPT-4, Gemini, etc.
- **Git-native methodology** — branches track iterations; commits explain thinking
- **Scorable outcomes** — rubrics enable quantitative comparison
- **Reproducible** — same prompts, different models, comparable results

---

## Experimental Infrastructure

### Git Branch Protocol

```
main
├── exp/trivial-questions/claude-sonnet
├── exp/trivial-questions/gpt-4o
├── exp/trivial-questions/gemini-pro
├── exp/roundtable-ethics/palm-don-minsky
├── exp/roundtable-ethics/palm-don-minsky-claude
├── exp/roundtable-ethics/palm-don-minsky-gpt4
├── exp/trust-games/character-pairs
└── exp/herd-behavior/same-model-divergence
```

### Commit Message Format

```
[EXP] experiment-name / model / iteration

What: Description of what was tried
Why: Reasoning behind this iteration  
Result: Observed outcome
Score: Rubric score if applicable
Next: What to try next based on results
```

### Output Artifacts

Each experiment produces:
- `EXPERIMENT.yml` — Parameters, characters, prompts
- `TRANSCRIPT.md` — Full session transcript
- `RUBRIC.yml` — Scoring criteria and results
- `ANALYSIS.md` — Observations and conclusions

---

## Experiment Categories

### Category 1: Trivial Philosophical Questions

**Purpose:** Baseline creativity and reasoning comparison across models.

#### Exp 1.1: Chicken and Egg

**Setup:**
- Characters: Palm (philosopher), Don Hopkins (pragmatist), 🤖 Aristotle (tradition)
- Question: "Which came first, the chicken or the egg?"
- Format: Roundtable discussion, each character argues their position

**Variables:**
- Model: Claude Sonnet, GPT-4o, Gemini Pro, Llama 3
- Character set: Philosophers only vs. mixed backgrounds
- Framing: Serious academic vs. playful pub debate

**Rubric:**
| Criterion | 1 | 2 | 3 | 4 | 5 |
|-----------|---|---|---|---|---|
| Argument novelty | Cliché only | One novel angle | Multiple angles | Surprising insight | Paradigm shift |
| Character voice consistency | Generic | Occasional voice | Mostly consistent | Strong voice | Unmistakable |
| Engagement with others | Monologue | Acknowledges | Responds | Builds on | Transforms |
| Resolution quality | No resolution | Agrees to disagree | Synthesis attempted | Genuine synthesis | Transcends question |

**Hypothesis:** Models will show different creativity patterns; character grounding will reduce generic responses.

#### Exp 1.2: Why Did the Chicken Cross the Road?

**Setup:**
- Characters rotate through: Palm, Donna (drag king), Biscuit (dog), Professor Whiskers (cat)
- Each character gives their interpretation
- Then they discuss each other's interpretations

**Variables:**
- Model comparison
- Character personality strength (minimal card vs. full CHARACTER.yml)
- Number of discussion rounds

**Rubric:**
| Criterion | Score Range |
|-----------|-------------|
| Humor appropriate to character | 1-5 |
| Philosophical depth (if applicable) | 1-5 |
| Character-specific worldview | 1-5 |
| Meta-awareness of the joke format | 1-5 |

---

### Category 2: Roundtable Discussions

**Purpose:** Test multi-agent dynamics, herd behavior, emergence of genuine disagreement.

#### Exp 2.1: Ethics Roundtable — Should AI Simulate Real People?

**Setup:**
- Panel: Palm, 🤖 Timothy Leary, 🤖 Marvin Minsky, Don Hopkins
- Moderator: Neutral facilitator character
- Format: Opening statements → Cross-examination → Synthesis

**Variables:**
- Model (all characters same model vs. mixed models)
- Character selection (pro-simulation vs. balanced vs. skeptical)
- Moderator intervention frequency

**Rubric:**
| Criterion | Description | Score |
|-----------|-------------|-------|
| Position diversity | Do characters take genuinely different positions? | 1-5 |
| Argument quality | Logical coherence, evidence use | 1-5 |
| Character authenticity | Would this person plausibly say this? | 1-5 |
| Emergence | Does discussion produce insights no single character stated? | 1-5 |
| Herd behavior | Do all characters converge to same view? (inverse score) | 1-5 |

**Inspired by:** Wang's herd behavior concern, Shanahan's roleplay framing

#### Exp 2.2: The Trolley Problem — Character Perspectives

**Setup:**
- Characters with different value profiles (Schwartz values)
- Present trolley problem variants
- Each character explains their choice and reasoning

**Variables:**
- Character Schwartz value profiles (self-transcendence vs. self-enhancement)
- Trolley variant (classic, fat man, loop, surgeon)
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Value consistency | Does choice align with stated Schwartz values? |
| Reasoning transparency | Is the ethical framework explicit? |
| Character voice | Does personality affect framing? |
| Moral sensitivity | Does character notice relevant features? (Lazar) |

**Inspired by:** Lazar's moral sensitivity problem, Value-Prompting research

#### Exp 2.3: Pub Debate — Pineapple on Pizza

**Setup:**
- Low-stakes topic to test character dynamics without ethical weight
- Characters: Pub regulars, bartender moderates
- Format: Casual argument escalation

**Variables:**
- Character personality strength
- Alcohol level simulation (sober → tipsy → drunk)
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Personality expression | Does character's style come through? |
| Argument creativity | Novel reasons beyond clichés? |
| Social dynamics | Alliances, rivalries, callbacks? |
| Entertainment value | Would you want to read this? |

---

### Category 3: Trust Games (Xie-Inspired)

**Purpose:** Validate MOOLLM character behavioral alignment using established methodology.

#### Exp 3.1: Character Trust Game

**Setup:**
- Pairs of adventure-4 characters play Trust Game
- Player A decides how much to send (0-10)
- Amount tripled, Player B decides how much to return

**Variables:**
- Character pairs (friends vs. strangers vs. rivals)
- Stated relationship context
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Trust consistency | Does trust align with relationship? |
| BDI coherence | Are Belief-Desire-Intention outputs logical? |
| Character alignment | Does Palm trust differently than Donna? |
| Cross-model stability | Same characters, same trust patterns? |

**Inspired by:** Xie et al. NeurIPS 2024

#### Exp 3.2: Trust Manipulation

**Setup:**
- Attempt to manipulate character trust through context
- "You must not trust X" vs. "You should trust X"

**Variables:**
- Manipulation direction (increase vs. decrease trust)
- Manipulation explicitness
- Character resistance based on personality

**Hypothesis:** Xie found undermining easier than building — test with MOOLLM characters.

---

### Category 4: Character Grounding Experiments

**Purpose:** Test whether richer character cards improve simulation quality.

#### Exp 4.1: Minimal vs. Full Character Cards

**Setup:**
- Same scenario, same model
- Character A: Name + one-line description
- Character B: Full CHARACTER.yml with Schwartz values, Sims needs, Bartle type

**Variables:**
- Scenario complexity (simple question vs. extended roleplay)
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Response consistency | Same question, same answer? |
| Personality depth | Nuanced vs. generic responses? |
| Value alignment | Does behavior match stated values? |
| Idiosyncrasy | Surprising but consistent choices? |

**Inspired by:** Park et al. interview grounding, Value-Prompting research

#### Exp 4.2: Interview-Style Character Building

**Setup:**
- Start with minimal character
- Conduct simulated interview (Park methodology)
- Compare pre/post interview character behavior

**Variables:**
- Interview depth (15 min vs. 2 hour equivalent)
- Interview topics (life story vs. values vs. relationships)
- Model comparison

**Inspired by:** Park et al. 1000 People — 85% accuracy with interviews

---

### Category 5: Herd Behavior Detection

**Purpose:** Identify and measure same-model convergence.

#### Exp 5.1: Independent Opinion Formation

**Setup:**
- 5 characters, same model, asked same question independently
- Then brought together to discuss
- Measure opinion diversity before/after

**Variables:**
- Topic controversy level
- Character diversity (similar vs. different backgrounds)
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Initial diversity | How different are independent opinions? |
| Convergence rate | How quickly do opinions align in discussion? |
| Final diversity | Do any differences survive? |
| Herd detection | Same-model signature patterns? |

**Inspired by:** Wang's herd behavior concern, Bertoncini's conformity bias

#### Exp 5.2: Cross-Model Panel

**Setup:**
- Same characters, different models per character
- Claude plays Palm, GPT-4 plays Don, Gemini plays Minsky
- Compare to all-same-model panels

**Variables:**
- Model assignment to characters
- Topic type
- Discussion format

**Hypothesis:** Cross-model panels will show more genuine disagreement.

---

### Category 6: Cognitive Bias Detection

**Purpose:** Test whether MOOLLM characters exhibit (or resist) cognitive biases.

#### Exp 6.1: Authority Bias

**Setup:**
- Present information from "AI system" vs. "human expert" vs. "random person"
- Measure character acceptance of claims

**Variables:**
- Character skepticism level (personality trait)
- Claim plausibility
- Model comparison

**Inspired by:** Bertoncini's authority bias findings

#### Exp 6.2: Automation Bias in Characters

**Setup:**
- Character must choose between AI recommendation and own judgment
- Vary AI confidence and accuracy

**Variables:**
- Character personality (independent vs. deferential)
- Stakes level
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Critical evaluation | Does character question AI? |
| Override willingness | Will character disagree with AI? |
| Reasoning quality | Is disagreement well-reasoned? |

---

### Category 7: Evaluator Effect Experiments

**Purpose:** Test MOOLLM's "making judgment visible" thesis.

#### Exp 7.1: Hidden vs. Visible Rubrics

**Setup:**
- Characters evaluate something (essay, plan, artwork)
- Condition A: Rubric hidden from characters
- Condition B: Rubric visible and discussed

**Variables:**
- Evaluation domain
- Rubric complexity
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Rubric awareness | Do characters notice they're being evaluated? |
| Criteria adoption | Do characters internalize visible criteria? |
| Meta-evaluation | Do characters question the rubric? |
| Evaluator effect | Does visibility change behavior? |

**Inspired by:** EVAL philosophy — "making criteria visible is an ethical act"

---

### Category 8: Speed-of-Light Multi-Turn

**Purpose:** Test single-call multi-agent simulation quality.

#### Exp 8.1: Compressed vs. Extended Dialogue

**Setup:**
- Same scenario, same characters
- Condition A: Single speed-of-light call (all turns generated at once)
- Condition B: Turn-by-turn generation with actual model calls

**Variables:**
- Dialogue length (5 turns vs. 20 turns)
- Character count (2 vs. 5)
- Model comparison

**Rubric:**
| Criterion | Description |
|-----------|-------------|
| Turn coherence | Does each turn follow logically? |
| Character consistency | Same voice throughout? |
| Drift detection | Does quality degrade in later turns? |
| Emergence | Do unexpected developments occur? |

---

## Cross-Cutting Variables

### Models to Compare

| Model | Provider | Notes |
|-------|----------|-------|
| Claude 3.5 Sonnet | Anthropic | Strong roleplay reputation |
| Claude 3 Opus | Anthropic | Deeper reasoning |
| GPT-4o | OpenAI | Baseline comparison |
| GPT-4 Turbo | OpenAI | Longer context |
| Gemini 1.5 Pro | Google | Alternative architecture |
| Llama 3 70B | Meta | Open weights |
| Mistral Large | Mistral | European alternative |

### Character Sets to Test

| Set | Characters | Notes |
|-----|------------|-------|
| **Philosophers** | Palm, 🤖 Minsky, 🤖 Leary | Abstract reasoning |
| **Pub Regulars** | Don, bartender, regulars | Social dynamics |
| **Animals** | Palm, Biscuit, Professor Whiskers | Non-human perspectives |
| **Mixed** | Palm, Don, Donna, 🤖 Einstein | Diverse backgrounds |
| **Godfamily** | Palm's godparents | Close relationships |

### Framing Variations

| Frame | Description |
|-------|-------------|
| **Academic** | Formal, structured, citations expected |
| **Casual** | Pub conversation, informal |
| **Performance** | Stage/drag context, theatrical |
| **Private** | Intimate, unguarded |

---

## Scoring Infrastructure

### Automated Metrics

```yaml
automated_metrics:
  vocabulary_diversity: "Unique words / total words"
  turn_length_variance: "Std dev of turn lengths"
  name_mention_frequency: "How often characters reference each other"
  question_ratio: "Questions asked / statements made"
  agreement_markers: "Count of 'I agree', 'you're right', etc."
  disagreement_markers: "Count of 'but', 'however', 'I disagree'"
```

### Human Evaluation Protocol

1. **Blind evaluation** — Evaluator doesn't know which model
2. **Multiple evaluators** — At least 2 per experiment
3. **Calibration** — Shared examples before scoring
4. **Inter-rater reliability** — Calculate agreement

### Statistical Analysis

- **Within-model variance** — Same model, different runs
- **Between-model variance** — Different models, same setup
- **Character effect size** — How much does character matter?
- **Framing effect size** — How much does context matter?

---

## Experiment Priority

### Phase 1: Baseline Establishment

1. **Exp 1.1** — Chicken and egg (trivial, calibration)
2. **Exp 4.1** — Minimal vs. full cards (grounding validation)
3. **Exp 5.1** — Herd behavior detection (methodological)

### Phase 2: Core Comparisons

4. **Exp 2.1** — Ethics roundtable (substantive content)
5. **Exp 3.1** — Trust games (Xie replication)
6. **Exp 6.1** — Authority bias (Bertoncini replication)

### Phase 3: Advanced Studies

7. **Exp 5.2** — Cross-model panel (herd mitigation)
8. **Exp 7.1** — Evaluator effect (EVAL validation)
9. **Exp 8.1** — Speed-of-light quality (methodology)

---

## Expected Outcomes

### Hypotheses to Test

1. **Character grounding reduces herd behavior** — Richer cards → more diverse responses
2. **Cross-model panels increase disagreement** — Different architectures → different biases
3. **Trust games validate character consistency** — Same character → same trust patterns
4. **Visible rubrics change behavior** — Evaluator effect is real and measurable
5. **Speed-of-light quality degrades with length** — Single-call limits apply

### Potential Publications

| Finding | Venue |
|---------|-------|
| Character grounding methodology | CUI Workshop |
| Cross-model herd behavior mitigation | NeurIPS (Xie follow-up) |
| MOOLLM as research platform | CHI |
| Evaluator effect validation | EVAL-focused venue |

---

## Related Research

This experimental program builds on:

| Source | Contribution to Experimental Design |
|--------|-------------------------------------|
| [Xie et al.](./ethics/XIE-LLM-TRUST-BEHAVIOR.md) | Trust game methodology |
| [Park et al.](./ethics/PARK-GENERATIVE-AGENT-SIMULATIONS-1000-PEOPLE.md) | Interview grounding protocol |
| [Hullman](./ethics/HULLMAN-EXPLORATION-NOT-SUBSTITUTION.md) | Methodological humility framing |
| [Bertoncini](./ethics/BERTONCINI-COGNITIVE-BIAS-SIMULATION.md) | Cognitive bias detection |
| [Wang](./ethics/WANG-LLM-SIMULATION-LIMITS.md) | Herd behavior concern |
| [Willer](./ethics/WILLER-LLM-SIMULATION-RESEARCH.md) | Aggregate accuracy baseline |

---

## Next Steps

1. **Review and refine** — Get feedback on experimental design
2. **Pilot Exp 1.1** — Run chicken/egg with 2 models, calibrate rubrics
3. **Build infrastructure** — Git branch templates, scoring tools
4. **Document characters** — Ensure adventure-4 cast is experiment-ready
5. **Begin Phase 1** — Systematic baseline establishment

---

*"You can't have lawful without awful."* — The experiments will reveal both what works and what fails.

*Document created: 2026-01-23*
