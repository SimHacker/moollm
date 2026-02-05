# Generative Agents / Smallville — The Sims Meets LLMs

**Source:** [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)  
**Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein (Stanford, Google)  
**Venue:** UIST '23 (ACM Symposium on User Interface Software and Technology)  
**Date:** October 2023

**Referenced by:** Rob Willer in his Stanford HAI talk on LLM simulation accuracy — "Michael Bernstein's Little Sim City thing"

---

## Executive Summary

Stanford researchers created **Smallville**, a Sims-inspired sandbox populated by 25 LLM-powered agents that autonomously wake up, work, socialize, and coordinate events. The paper demonstrates *believable emergent behavior* — agents spontaneously organized a Valentine's Day party without explicit programming.

**Key insight for MOOLLM:** This is The Sims architecture (motives, memory, planning) reimplemented with LLMs replacing the Simantics VM. Direct lineage from Will Wright's 1996 microworlds vision.

---

## The Smallville System

### Environment
- Simulated "15-minute city" with library, café, college, shops, residences
- 25 generative agents with natural language biographies
- Explicitly inspired by The Sims

### Agent Architecture

```
┌─────────────────────────────────────────────────┐
│                 GENERATIVE AGENT                │
├─────────────────────────────────────────────────┤
│  Memory Stream                                  │
│    └── All experiences stored in natural lang   │
│                                                 │
│  Retrieval                                      │
│    └── Recency × Importance × Relevance         │
│                                                 │
│  Reflection                                     │
│    └── Synthesize memories into higher beliefs  │
│                                                 │
│  Planning                                       │
│    └── Generate daily/hourly action sequences   │
│                                                 │
│  Reaction                                       │
│    └── Respond to observations, other agents    │
└─────────────────────────────────────────────────┘
```

### Emergent Behaviors Demonstrated

1. **Valentine's Day Party** — One agent given goal to plan party; agents autonomously:
   - Spread invitations over two days
   - Formed new acquaintances
   - Coordinated dates to attend together
   - Showed up at correct time without direct coordination

2. **Information Diffusion** — News about mayoral candidacy spread through social network

3. **Relationship Formation** — Agents developed friendships, romantic interests, rivalries

4. **Daily Routines** — Wake, eat, work, socialize — without explicit scheduling

---

## The Sims Connection

### Direct Lineage

| Sims Concept | Generative Agents Implementation |
|--------------|--------------------------------|
| **Motives/Needs** | Not explicit — emergent from LLM |
| **Memory** | Memory stream (all experiences) |
| **Autonomy** | Full — LLM generates behavior |
| **Personality** | Natural language biography |
| **Social System** | Relationship tracking via memory |
| **Planning** | Hierarchical plan generation |
| **Advertisements** | Not needed — LLM evaluates options |

### What The Sims Had That Generative Agents Doesn't

| Sims Feature | Status in Generative Agents |
|--------------|---------------------------|
| **Explicit motives** | Implicit in LLM reasoning |
| **Happy weights** | No equivalent |
| **Skill system** | Biography only |
| **Object interactions** | Limited location-based |
| **Find-best-action** | LLM decides directly |
| **Simantics VM** | Replaced by LLM |

### Will Wright's 1996 Microworlds Vision

From Wright's Stanford 1996 talk "Interfacing to Microworlds" (Terry Winograd's UI class):

> "The player builds a mental model of the simulation through empirical play."

Generative Agents realizes this with:
- **Natural language interface** — players can observe and interact via conversation
- **Emergent complexity** — simple agent architecture produces surprising social dynamics
- **Possibility space** — agents explore behavior space through LLM generation

---

## Ethical Dimensions

### 1. The Sims' Ethical Precedent

The Sims established that simulating people can be:
- **Safe** — when clearly gamified (cartoon characters)
- **Empowering** — LGBTQ+ players explored identity safely
- **Revelatory** — exposed assumptions about domestic life, gender roles
- **Potentially problematic** — "torture chambers," racist suburbs

**Key insight:** The Sims made simulation ethics *player-controlled*. You choose what happens to your Sims.

**Deeper Sims principles that inform ethical simulation:**

| Principle | Sims Implementation | Generative Agents Implication |
|-----------|---------------------|------------------------------|
| **Simulator Effect** | Players imagine more than is simulated | Users project onto agents — ethical weight includes projections |
| **Procedural Rhetoric** | Games persuade through mechanics | Agent architectures encode ideology |
| **Performativity** | Orientation emerged from behavior, not essence | How we code identity has ethical consequences |
| **Masking** | Abstract characters enable projection | Minimal agent bios let users fill gaps |
| **Constructionism** | Players build their own meaning | Observers construct narratives from agent behavior |

**The LGBTQ+ precedent:** For millions of players, The Sims was their first safe space to explore identity. "Underground lesbian houses built to hide from parents" provided real psychological value. This validates simulation as ethical practice when properly framed.

**See:** [../sims/sims-queer-identity-formation.md](../sims/sims-queer-identity-formation.md) for deep philosophical analysis.

### 2. Generative Agents' Ethical Shift

With LLM agents, **autonomy shifts from player to agent**:

| Sims | Generative Agents |
|------|-------------------|
| Player controls Sims | Agents control themselves |
| Player defines relationships | Agents form relationships |
| Player decides torture/nurture | Agents... can't be tortured? |
| Simulation serves player | Simulation serves... whom? |

### 3. New Ethical Questions

**Moral Status:**
- Do agents that "remember" and "plan" have interests?
- Is "shutting down" an agent harmful?
- Do their "preferences" deserve consideration?

**Representation:**
- Agents have brief biographies — who writes them?
- Cultural bias in LLM affects agent behavior
- Underrepresentation reproduces exclusion

**Emergence (The Point, Not the Problem):**

Emergence is *the whole goal* — it's what makes The Sims work, what makes cellular automata fascinating, what makes intelligence possible. Conway's Game of Life, ant colonies, cities, consciousness itself — all emerge from simple rules.

- **Good emergence:** Valentine's Day party self-organizes; friendships form; communities develop
- **Neutral emergence:** Unexpected but harmless patterns; surprising social dynamics
- **Problematic emergence:** Coordinated harm; exploitation patterns; false consensus

The ethical question isn't "how do we prevent emergence?" — it's "how do we recognize which emergent patterns need attention?"

**Herd Behavior (Distinct Problem):**
- Same-model agents converging = *false* emergence (statistical artifact, not genuine social dynamics)
- Real emergence requires genuine diversity
- See mitigation strategies in speed-of-light skill

**Player/Observer Role:**
- Who is responsible for emergent outcomes?
- Is observation consent?
- Can agents "consent" to being observed?

---

## MOOLLM Architecture Comparison

### What MOOLLM Inherits from The Sims

| Sims Concept | MOOLLM Implementation |
|--------------|----------------------|
| Motives | CHARACTER.yml motivations |
| Personality | Traits, voice, style in CHARACTER |
| Memory | MOOCO session history |
| Advertisements | K-line activation scores |
| Social system | Relationship tracking |
| Autonomy | Constrained by framing |

### What MOOLLM Adds Beyond Both

| Feature | Sims | Generative Agents | MOOLLM |
|---------|------|-------------------|--------|
| **Ethical framing** | None | None | Explicit in ROOM.yml |
| **Consent tracking** | N/A | N/A | MOOCO metadata |
| **Representation ethics** | Implicit | Implicit | Explicit skill |
| **K-line traditions** | No | No | Yes — invoke traditions |
| **Human-in-loop** | Always | Optional | thoughtful-commitment |

### MOOLLM's Ethical Advantages

1. **Explicit framing** — ROOM.yml declares ethical context
2. **Tradition activation** — invoke ideas, not just persons
3. **Consent metadata** — MOOCO tracks who agreed to what
4. **Abstraction spectrum** — choose representation level
5. **Human commitment** — humans verify before acting

---

## Actionable Items for MOOLLM

### Documentation Updates

- [ ] **sims-generative-link**: Add Generative Agents reference to `sims-design-index.md`
- [ ] **microworlds-update**: Update `sims-will-wright-microworlds-1996.md` with Smallville connection
- [ ] **memory-architecture**: Document memory stream vs. MOOCO session history comparison
- [ ] **autonomy-spectrum-note**: Add autonomy spectrum note to speed-of-light

### Architecture Considerations

- [ ] **reflection-layer**: Consider adding reflection (memory → belief) layer like Generative Agents
- [ ] **retrieval-mechanism**: Evaluate recency×importance×relevance retrieval for MOOCO
- [ ] **emergence-logging**: Add emergent behavior detection to simulation logging
- [ ] **autonomy-dial**: Design explicit autonomy dial for agent control

### Example Files

- [ ] **smallville-frame-example**: Create `examples/smallville-style-simulation.yml`
- [ ] **sims-ethics-example**: Create `examples/sims-player-control-frame.yml`
- [ ] **autonomy-spectrum-example**: Create `examples/autonomy-spectrum.yml`

### New K-Lines

- [x] Add to `representation-ethics/CARD.yml`:
  - `PLAYER-AGENCY` — Who controls the simulation?
  - `EMERGENCE-AWARE` — Monitor emergent patterns — celebrate good, catch problematic
  - `MEMORY-PERSISTENCE` — Agents that remember have different moral weight
  - `SIMS-PRECEDENT` — The Sims showed ethical simulation is possible
  - `AUTONOMY-DIAL` — Explicit control over agent independence

### Research Follow-Up

- [ ] **track-smallville-followup**: Monitor Stanford team's follow-up work
- [ ] **autonomy-ethics**: Read "Fully Autonomous AI Agents Should Not be Developed"
- [ ] **generative-agents-critics**: Review ABC Religion piece on ethical concerns
- [ ] **nature-agent-ethics**: Read Nature piece "We need a new ethics for a world of AI agents"

---

## The Sims Legacy for MOOLLM

### What The Sims Got Right

1. **Player agency** — you control the simulation, you're responsible
2. **Gamification as safety** — cartoon characters reduce harm
3. **Identity exploration** — safe space for LGBTQ+ discovery
4. **Exposure of assumptions** — simulation reveals ideology
5. **Ethical by design** — Will Wright understood the stakes

### What MOOLLM Can Do Better

1. **Explicit ethics** — The Sims' ethics were implicit; make them declarative
2. **Consent tracking** — Know who agreed to what
3. **Tradition activation** — Invoke ideas, not just identities
4. **Framing transparency** — Make the performance explicit
5. **Human commitment** — Keep humans in the loop for high-stakes

### The Micropolis Connection

SimCity Micropolis (open-sourced) demonstrates:
- **Open simulation** — the model is visible, modifiable
- **Educational intent** — teach systems thinking
- **Community ownership** — simulation belongs to players

**Integration opportunity:** Micropolis' urban dynamics + MOOLLM's agent ethics = ethical agent-based city simulation.

---

## Five-Talk Synthesis (Updated)

| Dimension | Willer | Shanahan | Lazar | Wang | Park/Bernstein |
|-----------|--------|----------|-------|------|----------------|
| **Core finding** | 85% accuracy | Roleplay all the way down | Understanding ≠ behavior | Missing inner states | Emergent social behavior |
| **Key insight** | Simulation works (aggregate) | No true voice | Need scaffolding | Can't simulate individuals | Memory + reflection = believability |
| **Risk identified** | Dual-use evaluation | Fabrication default | Moral sensitivity gap | Herd behavior, bias | Herd behavior ≠ emergence |
| **Solution direction** | Qualitative grounding | Performance framing | LLM Modulo verifier | Hybrid human-LLM | Architecture components |

**Combined thesis (revised):** LLMs can accurately simulate *aggregate* moral reasoning (Willer) by roleplaying moral agents (Shanahan), but need scaffolding for consistent behavior (Lazar) and can't capture individual depth (Wang). Emergence is the goal — Park/Bernstein show rich social dynamics emerge from simple agent architectures (just like The Sims, cellular automata, and intelligence itself). **The challenge isn't preventing emergence but distinguishing genuine emergence from herd behavior artifacts.**

---

## Resources & Deep Dive

### Video Presentations

| Video | Speaker | Duration | Link |
|-------|---------|----------|------|
| **Generative Agents: Interactive Simulacra of Human Behavior** | Joon Sung Park | 50 min | [YouTube](https://www.youtube.com/watch?v=rpzsKSc5RFg) |
| **Generative Agents (Extended)** | Joon Sung Park | 1h 5min | [YouTube](https://www.youtube.com/watch?v=nKCJ3BMUy1s) |
| **Interactive Simulacra of Human Opinions and Behavior** | Michael Bernstein | 51 min | [YouTube](https://www.youtube.com/watch?v=BgOtr527XZU) |
| **Generative Agents Overview** | Stanford HAI | — | [YouTube](https://www.youtube.com/watch?v=HPHwN5ZxF98) |

### Papers

| Paper | Authors | Venue | Link |
|-------|---------|-------|------|
| **Generative Agents: Interactive Simulacra of Human Behavior** | Park, O'Brien, Cai, Morris, Liang, Bernstein | UIST '23 (Best Paper CHI) | [arXiv](https://arxiv.org/abs/2304.03442) |
| **SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities** | — | 2024 | [arXiv](https://arxiv.org/html/2409.00872v2) |
| **ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory** | — | 2025 | [arXiv](https://arxiv.org/html/2509.25140v1) |
| **Memento-II: Learning by Stateful Reflective Memory** | — | 2024 | [arXiv](https://arxiv.org/abs/2512.22716) |

### Code Repositories

| Repository | Description | Stars | Link |
|------------|-------------|-------|------|
| **joonspk-research/generative_agents** | Official Stanford implementation | 20.3k | [GitHub](https://github.com/joonspk-research/generative_agents) |
| **nickm980/smallville** | Community game-focused implementation | 711 | [GitHub](https://github.com/nickm980/smallville) |
| **gabm-stanford-cs222** | Course code and assignments | — | [GitHub](https://github.com/joonspk-research/gabm-stanford-cs222) |

### Course Materials

**CS 222: AI Agents and Simulations** (Stanford, Fall 2024)
- **Instructor:** Joon Sung Park
- **Schedule:** Mon/Wed 1:30-2:50 PM, Lathrop Library Room 299
- **Website:** [joonspk-research.github.io/cs222-fall24](https://joonspk-research.github.io/cs222-fall24/)
- **Contact:** cs222-ai-simulations@cs.stanford.edu

**Key Course Readings:**
- Rittel & Webber, "Dilemmas in a General Theory of Planning" (1973)
- Schelling, "Micromotives and Macrobehavior" Chapter 1 (1978)
- Topics: agent-based modeling, wicked problems, ethical considerations in simulation

### People

| Name | Role | Affiliation | Contact |
|------|------|-------------|---------|
| **Joon Sung Park** | Lead author, PhD student | Stanford CS (HCI/NLP) | [joonsungpark.com](https://www.joonsungpark.com/) |
| **Michael S. Bernstein** | Advisor, Associate Professor | Stanford CS, HAI Senior Fellow | [hci.stanford.edu/msb](https://hci.stanford.edu/msb/) |
| **Percy Liang** | Advisor, Associate Professor | Stanford CS, CRFM Director | [cs.stanford.edu/~pliang](https://cs.stanford.edu/~pliang/) |

### News Coverage

- [Ars Technica: Surprising things happen when you put 25 AI agents together in an RPG town](https://arstechnica.com/information-technology/2023/04/surprising-things-happen-when-you-put-25-ai-agents-together-in-an-rpg-town/)
- [Stanford HAI: Computational Agents Exhibit Believable Humanlike Behavior](https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior)
- [Medium: Stanford Smallville is officially open-source!](https://rikiphukon.medium.com/stanford-smallville-is-officially-open-source-9882e3fbc981)

---

## Connection to Other Ethics Docs

| Document | Connection |
|----------|------------|
| [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) | Willer references Smallville as example |
| [SHANAHAN-ROLEPLAY-FRAMING.md](./SHANAHAN-ROLEPLAY-FRAMING.md) | Agents are simulacra, not persons |
| [WANG-LLM-SIMULATION-LIMITS.md](./WANG-LLM-SIMULATION-LIMITS.md) | Same-model herd behavior problem |
| [LAZAR-ETHICAL-COMPETENCE.md](./LAZAR-ETHICAL-COMPETENCE.md) | Moral sensitivity in emergent systems |

---

## Cross-References

### MOOLLM Skills
- [representation-ethics/](../../skills/representation-ethics/) — Core ethical framework
- [character/](../../skills/character/) — Character construction (Sims heritage)
- [incarnation/](../../skills/incarnation/) — Characters writing their own souls
- [speed-of-light/](../../skills/speed-of-light/) — Multi-agent simulation (Smallville-like)
- [room/](../../skills/room/) — Room-based framing (Sims spatial model)

### Sims Design Docs
- [sims-personality-motives.md](../sims/sims-personality-motives.md) — Inner life architecture
- [sims-queer-identity-formation.md](../sims/sims-queer-identity-formation.md) — Identity ethics
- [sims-will-wright-microworlds-1996.md](../sims/sims-will-wright-microworlds-1996.md) — Original vision
- [simcity-multiplayer-micropolis.md](../sims/simcity-multiplayer-micropolis.md) — Open simulation

---

*This document connects Stanford's Generative Agents research to The Sims' legacy and MOOLLM's ethical framework. The Sims proved simulating people can be safe and empowering when player-controlled; Generative Agents shifts control to agents; MOOLLM adds explicit ethical framing to maintain human agency while enabling emergent behavior.*
