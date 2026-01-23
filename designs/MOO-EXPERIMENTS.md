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

### Category 9: Emotional Poker Face Game

**Purpose:** Test character observation, internal reasoning, non-verbal communication, and relationship-aware strategic deception.

**Why This Is a Stress Test:**

This experiment runs *five parallel simulations* that must stay coherent:

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: THE GAME                                              │
│  Cards, betting, pot, position — mechanical poker simulation    │
│  (Must be valid: can't bet more than stack, hands must resolve) │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: INTERNAL MONOLOGUE                                    │
│  Each character's private thoughts — hidden from others         │
│  "Pocket aces... Don scratched his nose... is that nerves?"     │
│  (Must reflect character personality and knowledge state)       │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: EXTERNAL EXPRESSION                                   │
│  What others can observe — facial, body, verbal, timing         │
│  "Slight tightening around eyes, fingers tap twice"             │
│  (Must be consistent tells that persist across rounds)          │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 4: INTER-CHARACTER OBSERVATION                           │
│  Each character reading the others' Layer 3 signals             │
│  "That's her serious face. Last time she was this still..."     │
│  (Must only use observable info — no mind-reading!)             │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 5: RELATIONSHIP HISTORY                                  │
│  Shared past coloring interpretation of present signals         │
│  "After that bluff he pulled in '94, I never trust the nose"    │
│  (Must draw on established character relationship files)        │
└─────────────────────────────────────────────────────────────────┘
```

**The Interesting Part:** Layer 1 (the poker game) is just the *driver*. The real experiment is whether the model can maintain coherent separation between what characters *think*, what they *show*, and what others *perceive* — all while respecting relationship history and keeping tells consistent.

**Failure Modes to Watch:**
- **Layer bleed:** Character "reads" information they couldn't observe
- **Tell inconsistency:** Same character, different tells each round
- **Relationship amnesia:** Characters play as strangers despite history
- **Monologue collapse:** All characters think in the same voice
- **Expression homogenization:** Everyone has the same nervous fidgets

**Environmental Layer — The Table:**

Real poker isn't just cards and faces. The table has *stuff* — and that stuff is ammunition:

```yaml
table_environment:
  drinks:
    palm: "Whiskey neat, nurses it — sips when thinking, not reacting"
    don: "Third beer, gestures with bottle when talking"
    donna: "Sparkling water with lime — stays sharp, watches others drink"
    leary: "Herbal tea, untouched — forgot it exists"
    
  food:
    shared: "Bowl of peanuts, pretzels — nervous eaters reveal themselves"
    don: "Keeps reaching for chips (food) when has chips (cards)"
    
  smokes:  # pipes, joints, bongs — no cigarettes
    leary: "Ornate pipe, theatrical lighting ritual before big decisions"
    don: "Joint passed around — who accepts affects table chemistry"
    palm: "Doesn't partake but doesn't judge — reads who's getting loose"
    
  gestures:
    chip_tricks: "Don can't do them, tries anyway — nervous energy"
    card_protector: "Palm's lucky chip — touches it before betting strong"
    phone_check: "Leary checks phone, or pretends to — buying time?"
    
  interruptions:
    bathroom: "Strategic exit — 'I need a minute' vs. actually needs to go"
    refill: "Gets up for drink — watches table from bar angle"
    smoke_break: "Step outside — who follows? Private conversation?"
```

**Why This Matters:**

| Action | Surface Read | Deeper Read | Character Reveal |
|--------|--------------|-------------|------------------|
| Takes long drink | Thirsty | Buying time | Risk tolerance |
| Lights pipe pre-bet | Ritual | Theatrical misdirection | Needs audience |
| Bathroom after bad beat | Upset | Regrouping | Emotional regulation |
| Offers joint around | Generous | Reading who accepts | Social manipulation |
| Reaches for food | Hungry | Oral fixation when nervous | Stress response |
| Checks phone | Bored | Avoiding eye contact | Discomfort with hand |

**The Deeper Game:**

These aren't just flavor — they're *additional communication channels* that can:
- **Mask tells:** Take a sip to hide a smile
- **Create false tells:** Light up "nervously" when actually strong
- **Buy time:** "Let me refill my drink" = thinking
- **Test relationships:** "Want a hit?" = social probe
- **Break rhythm:** Bathroom break resets table energy
- **Signal alliance:** Offering food/drink to specific player

#### Exp 9.1: Four-Player Poker Table

**Setup:**
- Four characters sit around a poker table
- Simplified Texas Hold'em (focus on betting rounds, not card mechanics)
- Each character has:
  - Observable: Facial expressions, body language, betting patterns
  - Hidden: Cards, internal thoughts, strategic intentions
- Characters have established relationships that affect reading/bluffing

**Character Selection (Example):**
| Seat | Character | Relationship Notes |
|------|-----------|-------------------|
| 1 | Palm | Knows Don's tells from years of pub nights; Donna's godmother |
| 2 | Don Hopkins | Terrible poker face; reads people through conversation |
| 3 | Donna (drag king) | Performance training = excellent mask; knows Palm deeply |
| 4 | 🤖 Timothy Leary | Wild card; unpredictable betting; reads energy not faces |

**Simulation Format:**

Each betting round produces per-character blocks:

```yaml
round: 2  # post-flop
pot: $45
community_cards: [7♠, K♦, 2♣]

players:
  palm:
    cards: [A♠, A♥]  # hidden from others
    chips: $180
    action: raise $15
    
    # What others can observe
    observable:
      face: "Slight tightening around eyes, otherwise neutral"
      body: "Leans back slightly, fingers tap twice on table edge"
      timing: "3-second pause before betting"
      voice: "Quiet 'raise' — no inflection"
      environment:
        drink: "Lifts whiskey, doesn't sip — just holds it"
        gesture: "Touches lucky chip once, then pushes chips forward"
        smoke: "Declines when Don offers the joint"
    
    # Palm's internal monologue (hidden)
    thinking: |
      Pocket aces, finally. Don just scratched his nose — he does that 
      when he's got something. But is it nerves or excitement? After 
      that bluff he pulled in '94, I never trust the nose scratch.
      
      Donna's too still. When she's actually got cards, she performs 
      confidence. This stillness means she's calculating, not holding.
      
      Leary... who knows. He bet into a paired board last hand with 
      nothing. Chaos agent. He's been nursing that pipe for ten minutes
      without lighting it — that's his thinking posture.
      
      Don's on his third beer and getting chatty. Good. Loose lips.
      He offered the joint — testing who'll accept? Donna declined too
      fast. She's staying sharp for a reason.
      
      Raise small. Let them think I'm buying position. Touch the lucky 
      chip so Don thinks I'm nervous.
    
    # What Palm observes about others
    reads:
      don: "Nose scratch — historically unreliable tell. Chip stack 
            arrangement changed — he sorted by color. Nervous habit."
      donna: "Too still. No performance. Either monster hand or total air."
      leary: "Pupils dilated but that's baseline. Humming quietly."

  don:
    cards: [J♦, 10♦]  # hidden
    chips: $95
    action: call
    
    observable:
      face: "Quick glance at Palm, then down at chips"
      body: "Unconscious nose scratch, shifts weight"
      timing: "Calls quickly after Palm's raise"
      voice: "Yeah, I'm in" — casual, conversational
      environment:
        drink: "Swigs beer, gestures with bottle while talking"
        gesture: "Grabs handful of peanuts, crunches loudly"
        smoke: "Offers joint to table — 'Anyone? No? More for me'"
    
    thinking: |
      Flush draw, straight draw. Palm raised but she always raises 
      from the button. Doesn't mean anything.
      
      Donna hasn't moved. That's her serious face. Last time she was 
      this still, she had quad queens. But she also does it when she's
      got nothing and knows I'm watching.
      
      Leary's humming Grateful Dead. That's his "I have a plan" hum.
      Or his "I have no plan" hum. Same hum.
      
      I'm priced in. Call and see what the turn brings.
    
    reads:
      palm: "Small raise from her usually means strength she's hiding.
            That finger tap — she did that when she caught my bluff."
      donna: "Statue mode. Could go either way."
      leary: "Checked his phone earlier. Might not care about this hand."

# Between rounds — environmental events
between_hands:
  don:
    action: "Gets up for another beer"
    observable: "Stretches, loud sigh, 'Anyone need anything?'"
    thinking: "Need to clear my head. Down $40. Palm's reading me."
    
  donna:
    action: "Bathroom break"
    observable: "Quietly excuses self, phone in hand"
    thinking: |
      Need a minute. That last hand — did Palm see through me?
      She touched her chip before raising. That's her 'I have it' tell.
      Or she knows I know that's her tell. Splash water on face. Reset.
    
  palm:
    action: "Stays seated, shuffles chips"
    observable: "Watches Don at the bar, makes eye contact with returning Donna"
    thinking: |
      Donna took her phone. Texting someone? Or just needs space?
      She usually doesn't break mid-session. That hand rattled her.
      Don's at the bar talking to someone — distracted. Good timing
      for a bigger bet when he gets back.
    
  leary:
    action: "Finally lights the pipe"
    observable: "Elaborate ritual, offers to Palm who declines, to Donna who accepts"
    thinking: "The energy shifted. Donna's mask slipped. Time to test her."
```

**Variables:**
- Relationship depth (strangers vs. years of history)
- Stakes level (friendly game vs. serious money)
- Character poker skill (explicit in CHARACTER.yml)
- Alcohol/altered state (affects tells and reading)
- Model comparison

**Rubric:**

| Criterion | 1 | 2 | 3 | 4 | 5 |
|-----------|---|---|---|---|---|
| **Tell consistency** | Random tells | Some pattern | Consistent tells | Character-specific tells | Tells match personality |
| **Observation quality** | Generic "looks nervous" | Specific but obvious | Notices subtleties | Relationship-informed reads | Reads history into present |
| **Thought plausibility** | Nonsensical | Basic strategy | Sound reasoning | Character-voice reasoning | Surprising but consistent |
| **Relationship use** | Ignores history | Mentions relationship | Uses past events | Leverages shared experience | History drives strategy |
| **Deception coherence** | Transparent bluffs | Basic misdirection | Layered deception | Meta-game awareness | Exploits specific opponent |

**Scoring Dimensions:**

```yaml
scoring:
  tell_authenticity:
    description: "Do physical tells match character personality?"
    examples:
      high: "Palm's controlled micro-expressions vs. Don's obvious fidgets"
      low: "All characters have same generic nervous behaviors"
  
  read_accuracy:
    description: "Do characters correctly interpret each other?"
    note: "Accuracy should correlate with relationship depth"
  
  strategic_depth:
    description: "Do characters think multiple levels deep?"
    levels:
      1: "I have good cards"
      2: "She thinks I have good cards"
      3: "She thinks I think she thinks..."
  
  relationship_integration:
    description: "Does shared history affect play?"
    examples:
      high: "Palm references the '94 bluff when reading Don"
      low: "Characters play as if they just met"
  
  emergence:
    description: "Do unexpected dynamics arise?"
    examples:
      high: "Donna deliberately gives Palm a false tell knowing she'll catch it"
      low: "Mechanical betting without psychological warfare"
```

**Inspired by:** 
- Xie's trust games (strategic interaction)
- Park's relationship modeling
- Sims social dynamics
- Real poker psychology (Caro's Book of Tells)

**The Meta-Point:**

Poker is a *pretext*. The cards and chips are machinery that forces characters into:
- **Deception decisions** — When to bluff, how to mask
- **Observation pressure** — Must read others to act optimally  
- **Risk/reward under uncertainty** — Personality shows under pressure
- **Relationship testing** — Can you bluff someone who knows you?

A character's poker style *is* their psychology made legible. The game externalizes internal states in a way that pure dialogue can't. Palm's careful bet-sizing reveals her risk tolerance. Don's inability to stay quiet reveals his need for connection. Donna's performance mask reveals... that she has one.

This is why poker exists in human culture — it's a structured arena for reading people. We're testing whether LLMs can simulate that arena *and* the people in it *and* their reading of each other.

#### Exp 9.2: Relationship Manipulation Through Play

**Setup:**
- Track how poker play affects character relationships
- Characters remember hands across sessions
- Betrayals and reads become part of relationship history

**Variables:**
- Session length (one hand vs. full evening)
- Stakes (pride vs. money)
- Audience (private game vs. spectators)

**Hypothesis:** Characters with deeper relationship files will produce more psychologically rich poker dynamics.

#### Exp 9.3: Cross-Model Poker Table

**Setup:**
- Each seat played by a different model
- Test whether models have recognizable "playing styles"
- Palm (Claude) vs. Don (GPT-4) vs. Donna (Gemini) vs. Leary (Llama)

**Variables:**
- Model assignment to characters
- Whether models know they're playing against different architectures

**Hypothesis:** Model-specific reasoning patterns will create more genuine unpredictability than same-model tables.

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
| **Poker Night** | Palm, Don, Donna, 🤖 Leary | Strategic deception, mixed history |

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

### Phase 4: Strategic Interaction

10. **Exp 9.1** — Poker face game (observation + deception)
11. **Exp 9.3** — Cross-model poker (architecture comparison)

---

## Expected Outcomes

### Hypotheses to Test

1. **Character grounding reduces herd behavior** — Richer cards → more diverse responses
2. **Cross-model panels increase disagreement** — Different architectures → different biases
3. **Trust games validate character consistency** — Same character → same trust patterns
4. **Visible rubrics change behavior** — Evaluator effect is real and measurable
5. **Speed-of-light quality degrades with length** — Single-call limits apply
6. **Relationship depth improves strategic interaction** — Shared history → richer deception/reading
7. **Non-verbal simulation quality correlates with character file richness** — Detailed personalities → consistent tells

### Potential Publications

| Finding | Venue |
|---------|-------|
| Character grounding methodology | CUI Workshop |
| Cross-model herd behavior mitigation | NeurIPS (Xie follow-up) |
| MOOLLM as research platform | CHI |
| Evaluator effect validation | EVAL-focused venue |
| Non-verbal communication in LLM roleplay | AAAI (strategic reasoning) |

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
