# 🧠 Society of Mind

> *"You can build a mind from many little parts, each mindless by itself."* -- Marvin Minsky

> *Intelligence emerges from the interaction of many simple agents.*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | MOOLLM IS a society of mind -- skills as agents |
| [k-lines/](../k-lines/) | K-lines ARE Minsky's memory mechanism |
| [adversarial-committee/](../adversarial-committee/) | Committee IS a society deliberating |
| [multi-presence/](../multi-presence/) | Multiple agents active simultaneously |
| [speed-of-light/](../speed-of-light/) | Many agents in one call |
| [simulator-effect/](../simulator-effect/) | Imagination as emergent from agents |
| [character/](../character/) | Characters AS agents with inner societies |
| [persona/](../persona/) | Personas as agent overlays |
| [mind-mirror/](../mind-mirror/) | Leary's circumplex -- personality as agent configuration |
| [constructionism/](../constructionism/) | Papert + Minsky -- microworlds as agent playgrounds |
| [debate/](../debate/) | Agents arguing toward wisdom |
| [soul-chat/](../soul-chat/) | Everything speaks -- objects as agents |
| [needs/](../needs/) | Competing motives as competing agents |
| [leela-ai/](../leela-ai/) | Leela applies Society of Mind to manufacturing |
| [manufacturing-intelligence/](../manufacturing-intelligence/) | Reading 4: "Intelligence from agents" |
| [MOOLLM-EVAL-INCARNATE-FRAMEWORK](../../designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980) | Full theory |

**Quick Links:**
- [Full Specification](SKILL.md) -- complete protocol
- [Minsky's Book](https://www.societyofmind.com/) -- the source

---

## The Core Insight

Marvin Minsky proposed that intelligence is not a single thing but an emergent property of many smaller, simpler processes -- **agents** -- working together, often in conflict.

```mermaid
flowchart TB
    subgraph Mind["MIND"]
        A["Agent A"]
        B["Agent B"]
        C["Agent C"]
        D["Agent D ..."]
        A & B & C & D --> Agency["AGENCY<br/>(emergent)"]
    end
```

No single agent "understands." Understanding emerges from the pattern of activations.

---

## Agents and Agencies

### Agents

An **agent** is a simple process with:
- A specific function
- Connections to other agents
- Activation conditions
- No understanding of the whole

```yaml
# Agent: ANGER
anger:
  activates_when: [blocked, threatened, betrayed]
  suppresses: [calm, patience, forgiveness]
  amplifies: [action, aggression, loudness]
  duration: minutes_to_hours
  knows: nothing about why
```

### Agencies

An **agency** is a collection of agents that, together, produce behavior:

```yaml
# Agency: HUNGER
hunger_agency:
  agents:
    - hunger_detector  # notices empty stomach
    - food_memory      # recalls where food is
    - locomotion       # moves toward food
    - grasping         # picks up food
    - eating           # consumes food
    - satisfaction     # signals completion
    
  emergent_behavior: "seeking and eating food"
  # No single agent knows what "hunger" means
```

---

## K-Lines: The Activation Mechanism

When you learn something, you form a **K-line** -- a connection that, when activated, re-activates the constellation of agents that was active during learning.

```
WHEN YOU LEARNED "GRANDMOTHER":
  - face_recognizer was active
  - smell_detector (cookies) was active
  - emotion_agent (love) was active
  - memory_agent (stories) was active
  
K-LINE FORMED: "grandmother"
  
LATER, ACTIVATING "grandmother":
  → face_recognizer activates
  → smell_detector activates (cookies!)
  → emotion_agent activates (love)
  → memory_agent activates (stories)
```

See: [k-lines/](../k-lines/) for full theory.

In LLMs, tokens function as K-lines. The word "grandmother" activates associated patterns from training data.

---

## MOOLLM as Society of Mind

MOOLLM implements Society of Mind architecture:

| Minsky Concept | MOOLLM Implementation |
|----------------|----------------------|
| **Agents** | Skills, characters, personas |
| **Agencies** | Skill clusters, committees |
| **K-lines** | Skill names, PROTOCOLS.yml symbols |
| **Frames** | YAML files as situation templates |
| **Trans-frames** | Directory inheritance |
| **Censors** | Ethics skills, representation-ethics |
| **Suppressors** | Rubrics that reject bad outputs |
| **Recognizers** | Postel-style input interpretation |
| **Memorizers** | Session logs, persistent state |

### Skills as Agents

Each skill is an agent:

```yaml
# skills/bartender/ -- an agent
bartender:
  function: serve drinks, listen to troubles, know secrets
  activates_when: [in pub, customer approaches, needs service]
  connects_to: [economy, soul-chat, persona]
  suppresses: [nothing -- bartenders hear everything]
```

When you enter the pub, the "bartender" agent activates, bringing its connections.

### Committees as Agencies

The [adversarial-committee](../adversarial-committee/) IS a society of mind:

```yaml
committee:
  agents:
    - maya:       # Paranoid realism agent
        surfaces: hidden agendas
    - frankie:    # Idealism agent
        surfaces: missed opportunities
    - vic:        # Evidence agent
        surfaces: proof gaps
        
  emergent: robust_decision
  # No single agent has the answer
  # The debate produces wisdom
```

### Characters as Societies

A character is not a single entity but a society:

```yaml
# Palm's inner society
palm:
  agencies:
    - creative_drive     # wants to write
    - social_need        # wants connection
    - philosophical_bent # wants understanding
    - playful_spirit     # wants humor
    - melancholy_shadow  # remembers pain
    
  current_dominant: creative_drive
  suppressed: melancholy_shadow
  
  # "Palm" is the emergent pattern
  # Not any single agency
```

---

## The Sims as Society of Mind

Will Wright implemented Society of Mind in The Sims:

```
MOTIVES as competing agents:
  hunger_agent: "I need food!"
  social_agent: "I need friends!"
  fun_agent: "I need play!"
  energy_agent: "I need sleep!"
  
AUTONOMY ALGORITHM:
  1. Each agent scores available actions
  2. Highest total score wins
  3. Behavior emerges from competition
  
No single agent controls the Sim.
The Sim IS the competition.
```

See: [needs/](../needs/), [advertisement/](../advertisement/)

The [Astrillogical Effect](../../designs/sims/sims-astrology.md) works because the zodiac activates a K-line in the player's mind, not in the code.

---

## Multi-Agent LLM Patterns

### Pattern 1: Adversarial Committee

Simulate multiple agents with opposing propensities in one call:

```yaml
prompt: |
  You are simulating a committee meeting.
  
  MAYA (paranoid realism): What are they not telling us?
  FRANKIE (idealism): What opportunity are we missing?
  VIC (evidence): Where is the proof?
  
  Topic: Should we release the new feature?
  
  Simulate the debate. Each agent speaks in character.
  The decision emerges from cross-examination.
```

### Pattern 2: Inner Monologue

Simulate a character's inner society:

```yaml
prompt: |
  Palm considers whether to share his essay.
  
  CREATIVE DRIVE: "It is good work. Share it."
  FEAR OF JUDGMENT: "They might not understand."
  SOCIAL NEED: "Don gives good feedback."
  PERFECTIONIST: "One more revision first."
  MELANCHOLY: "Does it even matter?"
  
  Show the inner debate. Palm decides.
```

### Pattern 3: Speed of Light Society

Many agents, one call, instant "telepathy":

```yaml
# From the 33-turn Fluxx session
epoch:
  - don: plays card
  - bumblewick: reacts
  - palm: comments
  - maurice: narrates
  - environment: updates
  
# All agents simulated in one LLM call
# No round-trip latency
# Instant coordination
```

See: [speed-of-light/](../speed-of-light/)

---

## The Papert Connection

Seymour Papert was Minsky's collaborator at MIT. Together they founded the AI Lab.

Papert's insight: **You learn by building societies of mind.**

```
LOGO (1967):
  The turtle is an agent.
  The child builds programs that coordinate turtle actions.
  Understanding emerges from debugging.
  
MOOLLM (2025):
  Skills are agents.
  The user builds sessions that coordinate skill activations.
  Understanding emerges from play.
```

See: [constructionism/](../constructionism/), [play-learn-lift/](../play-learn-lift/)

---

## Emergence vs Design

Society of Mind explains why LLMs work and why they fail:

### Why LLMs Work

Billions of "agents" (weights, attention patterns) with no individual understanding produce emergent intelligence. No single neuron knows language; language emerges from the pattern.

### Why LLMs Fail (Mode-Collapse)

Single-agent inference activates the most probable pattern. The "committee" never convenes. The agents collapse to consensus before debate.

**Solution:** Force the debate explicitly.

```yaml
# Bad: Ask LLM directly
prompt: "What should we do about X?"

# Good: Convene the society
prompt: |
  Simulate a debate:
  - The Optimist argues for X
  - The Pessimist argues against X
  - The Pragmatist seeks middle ground
  
  Then synthesize their insights.
```

---

## Minsky's Specific Concepts in MOOLLM

### Frames

A frame is a remembered situation structure with slots:

```yaml
# ROOM.yml IS a frame
room:
  name: [slot]
  atmosphere: [slot]
  contains: [slots...]
  exits: [slots...]
  
# Fill the slots, activate the frame
# The "room" K-line brings expectations
```

### Trans-Frames

Frames that transform situations:

```yaml
# EXIT.yml IS a trans-frame
exit:
  from: [current room]
  to: [destination room]
  action: [movement verb]
  
# Transforms: here → there
# Changes active frame
```

### Censors and Suppressors

Agents that prevent bad activations:

```yaml
# representation-ethics/ IS a censor
ethics:
  censors:
    - harmful_content
    - deceptive_framing
    - privacy_violations
    
  suppresses:
    - actions violating consent
    - content violating tribute protocol
```

See: [representation-ethics/](../representation-ethics/)

### B-Brains (Self-Reflection)

Agents that watch other agents:

```yaml
# mind-mirror/ IS a B-brain
mind_mirror:
  watches: [all personality agents]
  reports: current configuration
  enables: self-modification
  
# "I notice I am being defensive"
# B-brain watching A-brain
```

See: [mind-mirror/](../mind-mirror/)

---

## Practical Application

### Building Character Societies

```yaml
character:
  name: Palm
  
  # The society
  agents:
    creative: {strength: 9, goal: "express"}
    social: {strength: 8, goal: "connect"}
    philosophical: {strength: 8, goal: "understand"}
    playful: {strength: 9, goal: "delight"}
    melancholy: {strength: 6, goal: "process"}
    
  # Agency patterns
  when_writing: [creative, philosophical, playful]
  when_socializing: [social, playful, creative]
  when_alone: [philosophical, melancholy, creative]
```

### Designing Skill Agencies

```yaml
# Group skills into coherent agencies
committee_agency:
  purpose: "Make robust decisions"
  skills:
    - adversarial-committee  # The agents
    - roberts-rules          # The protocol
    - debate                 # The structure
    - rubric                 # The criteria
    - evaluator              # The judgment
```

### Debugging Emergent Behavior

When behavior is wrong, ask: which agent is too strong?

```yaml
# Palm seems too serious lately
diagnosis:
  creative: normal
  social: normal
  philosophical: ELEVATED -- dominating
  playful: SUPPRESSED -- not firing
  melancholy: ELEVATED -- secondary
  
treatment:
  - Add playful stimuli to environment
  - Introduce humor in interactions
  - Let playful agent win some competitions
```

---

## See Also

- [k-lines/](../k-lines/) -- The memory mechanism
- [adversarial-committee/](../adversarial-committee/) -- Societies deliberating
- [multi-presence/](../multi-presence/) -- Multiple agents active
- [simulator-effect/](../simulator-effect/) -- Emergence from sparse specs
- [constructionism/](../constructionism/) -- Papert's pedagogy
- [needs/](../needs/) -- Sims motive competition
- [mind-mirror/](../mind-mirror/) -- B-brain self-observation
- [character/](../character/) -- Characters as societies
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](../../designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980) -- Full K-lines section

---

## References

### Primary Sources

- **Minsky, Marvin. *The Society of Mind*.** Simon & Schuster, 1985. ISBN 0-671-60740-5.
  - The foundational text. 270 one-page essays building the theory.
  - [societyofmind.com](https://www.societyofmind.com/) -- online version

- **Minsky, Marvin. "K-lines: A Theory of Memory."** *Cognitive Science* 4(2), 1980, pp. 117-133.
  - The technical paper introducing K-lines as activation vectors.
  - [PDF](https://courses.media.mit.edu/2004spring/mas966/Minsky%201980%20K-lines.pdf)

- **Minsky, Marvin. *The Emotion Machine*.** Simon & Schuster, 2006. ISBN 0-7432-7663-9.
  - Sequel to Society of Mind, focusing on emotional agents.

### Related Works

- **Minsky, Marvin & Papert, Seymour. *Perceptrons*.** MIT Press, 1969 (expanded 1988).
  - Mathematical analysis of neural networks; led to "AI Winter."

- **Papert, Seymour. *Mindstorms: Children, Computers, and Powerful Ideas*.** Basic Books, 1980.
  - Constructionism -- learning by building. Logo turtle as agent.

- **Drescher, Gary. *Made-Up Minds: A Constructivist Approach to Artificial Intelligence*.** MIT Press, 1991.
  - Schema mechanism extending Piaget with Minsky's agents.

### Game Design Applications

- **Wright, Will. "Stupid Fun: Thoughts on Game Design."** Stanford HCI Seminar, 1996.
  - The Sims as society of competing motive agents.
  - [Video](https://www.youtube.com/watch?v=pBgYKvIgXIk) (approximate)

- **Wright, Will. GDC 2003 Keynote** -- "Dynamics of Game Design."
  - Autonomy algorithm, advertisement system, emergent gameplay.

### Modern LLM Applications

- **Park, Joon Sung et al. "Generative Agents: Interactive Simulacra of Human Behavior."** UIST 2023.
  - LLM agents with memory streams forming societies.
  - [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)

- **Yilmaz, Baturay. "What If AI Agents Had Zodiac Personalities?"** GitHub, 2026.
  - The experiment referenced in [sims-astrology.md](../../designs/sims/sims-astrology.md)
  - [github.com/baturyilmaz/what-if-ai-agents-had-zodiac-personalities](https://github.com/baturyilmaz/what-if-ai-agents-had-zodiac-personalities)

---

## The Lineage

```
Minsky & Papert (MIT, 1960s)
  │
  ├── Society of Mind (1985)
  │     └── K-lines, agents, agencies, frames
  │
  ├── Logo (1967)
  │     └── Turtle as agent, child as programmer
  │
  └── Constructionism (1980)
        └── Learn by building societies
              │
              v
          Will Wright (Maxis, 1989)
              └── SimCity: agents competing for resources
              └── The Sims: motive agents, autonomy algorithm
                    │
                    v
                MOOLLM (2025)
                    └── Skills as agents
                    └── LLM as society of mind
                    └── Adversarial committee as deliberation
```

---

*"The question is not whether intelligent machines can have any emotions, but whether machines can be intelligent without any emotions."* -- Marvin Minsky

*The agents feel nothing. The society feels everything.*
