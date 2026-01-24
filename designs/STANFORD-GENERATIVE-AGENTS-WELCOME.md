# Welcome, Stanford Generative Agents Team!

*A landing page for Joon Sung Park, Michael Bernstein, Percy Liang, and collaborators*

---

## Why We're Reaching Out

Your "Generative Agents: Interactive Simulacra of Human Behavior" work is foundational to what we're building. We believe there's significant synergy between Smallville and MOOLLM, and we'd love to explore collaboration.

**TL;DR:** MOOLLM is an ethical framework for LLM agents that inherits directly from The Sims (one of our contributors worked on the original game). Your work realizes Will Wright's 1996 microworlds vision with LLMs. We add explicit ethical scaffolding.

---

## Who We Are

**MOOLLM** (pronounced "moo-LM") = **M**iniature **O**pen **O**rchestration **L**anguage for **L**arge **M**odels

A framework for building ethical, auditable, and composable LLM-based agent systems.

### Key Contributors

- **Don Hopkins** — Worked on The Sims (personality, motives, social system, pie menus) and SimCity/Micropolis (open-sourced)
- Team includes AI researchers, game designers, and ethics practitioners

### The Sims Connection

MOOLLM's architecture draws directly from The Sims:

| Sims Concept | MOOLLM Implementation |
|--------------|----------------------|
| **Motives/Needs** | CHARACTER.yml motivations |
| **Personality traits** | Character traits, voice, style |
| **Advertisements** | K-line activation scores |
| **Social system** | Relationship tracking |
| **Autonomy** | Constrained by explicit framing |
| **Find-best-action** | LLM + K-lines |

---

## Why Your Work Matters to Us

### 1. You Realized Will Wright's Vision

From Wright's GDC 1996 talk "Interfacing to Microworlds":
> "The player builds a mental model of the simulation through empirical play."

Generative Agents realizes this with natural language interface and emergent complexity. This is exactly what Will Wright was describing 27 years before LLMs made it possible.

### 2. Your Architecture Parallels Ours

| Component | Generative Agents | MOOLLM |
|-----------|-------------------|--------|
| **Memory** | Memory stream | MOOCO session history |
| **Reflection** | Synthesize to beliefs | K-line traditions |
| **Planning** | Daily/hourly plans | Task decomposition |
| **Retrieval** | Recency × Importance × Relevance | Weighted activation |
| **Personality** | Natural language biography | CHARACTER.yml |
| **Environment** | Smallville locations | ROOM.yml spatial framing |

### 3. We're Solving the Ethics Problem You Raised

Your paper notes the need for ethical considerations. We've built a comprehensive framework:

**representation-ethics skill:**
- Explicit framing (TRIBUTE, EDUCATION, PERFORMANCE)
- Consent tracking via MOOCO metadata
- Abstraction spectrum (tradition → quote)
- Human-in-loop commitment patterns

---

## What We've Built That Might Interest You

### 1. Ethical Framing System

Every simulation has explicit ethical context:

```yaml
# ROOM.yml — declares ethical framing
meta:
  type: simulation
  framing: EDUCATION
  consent: 
    participants: [acknowledged]
    observers: [informed]
  
ethics:
  representation_level: inspired_character
  tribute_mode: true
  robot_rule: enabled  # 🤖 prefix for simulated speech
```

### 2. K-Line Tradition Activation

Instead of simulating *people*, we invoke *traditions*:

```yaml
# Safe: invoke Feynman's curiosity tradition
k_lines:
  - FEYNMAN-CURIOSITY
  - PLAYFUL-RIGOR
  - FIRST-PRINCIPLES

# Vs. problematic: claim to BE Feynman
```

This allows rich personality without deceptive impersonation.

### 3. Memory + Reflection (Like Yours, But Auditable)

MOOCO (our runtime) stores:
- Complete conversation history
- Ethical metadata per message
- Consent states
- Provenance tracking

### 4. Multi-Agent Simulation (Speed-of-Light)

Our "speed-of-light" skill does what Smallville does:
- Multiple agents in single context
- Turn-based interaction
- Emergent social dynamics
- **But:** explicit ethical framing, herd behavior detection, human checkpoints

---

## Potential Collaboration Areas

### 1. Ethical Scaffolding for Smallville

We could contribute:
- ROOM.yml framing for Smallville locations
- CHARACTER.yml ethical metadata
- Consent tracking layer
- Representation ethics guidelines

### 2. Reflection Layer Enhancement

Your reflection mechanism (memory → beliefs) maps to our K-line traditions. Potential to:
- Add ethical reflection ("was this interaction appropriate?")
- Track moral weight of persistent memories
- Detect problematic emergent patterns

### 3. Micropolis + Smallville

Don Hopkins open-sourced SimCity as Micropolis. Potential:
- Urban dynamics + social agents
- City-scale ethical simulation
- Educational microworlds

### 4. CS 222 Course Materials

We have extensive documentation on:
- The Sims architecture → LLM agents
- Ethical considerations in simulation
- Play-Learn-Lift methodology
- Will Wright's design philosophy

Could contribute readings or guest content.

---

## Our Ethics Research Synthesis

We've documented five major research threads:

| Research | Key Insight | Relevance |
|----------|-------------|-----------|
| **Willer (Stanford)** | 85% accuracy in LLM simulation | Validates Smallville approach |
| **Shanahan (DeepMind)** | "Roleplay all the way down" | Philosophical grounding |
| **Lazar (ANU)** | Need scaffolding for ethics | Architecture implications |
| **Wang (NUS)** | Can't simulate individuals | Aggregate vs. individual |
| **Park/Bernstein (You!)** | Emergent social behavior | Foundation for our work |

**Combined thesis:** LLMs can simulate aggregate patterns (Willer) by roleplaying (Shanahan), need scaffolding for ethics (Lazar), can't capture individual depth (Wang), and produce emergent dynamics requiring attention (you). The Sims showed this works with player agency; MOOLLM adds explicit framing.

---

## Key Documents to Explore

### Ethics Framework
- [designs/ethics/GENERATIVE-AGENTS-SMALLVILLE.md](./ethics/GENERATIVE-AGENTS-SMALLVILLE.md) — Our analysis of your work
- [skills/representation-ethics/SKILL.md](../skills/representation-ethics/SKILL.md) — Core ethical framework
- [designs/ethics/README.md](./ethics/README.md) — Five-talk synthesis

### The Sims Heritage
- [designs/sims/sims-personality-motives.md](./sims/sims-personality-motives.md) — How Sims inner life → MOOLLM
- [designs/sims/sims-will-wright-microworlds-1996.md](./sims/sims-will-wright-microworlds-1996.md) — Original vision
- [designs/sims/sims-queer-identity-formation.md](./sims/sims-queer-identity-formation.md) — Identity ethics in games

### Architecture
- [skills/character/](../skills/character/) — Character construction
- [skills/room/](../skills/room/) — Spatial framing
- [skills/speed-of-light/SKILL.md](../skills/speed-of-light/SKILL.md) — Multi-agent simulation

---

## Questions We'd Love to Discuss

1. **Ethical reflection:** Have you considered adding ethical self-assessment to the reflection cycle?

2. **Herd behavior:** Wang et al. note same-model agents converge. How do you handle diversity in Smallville?

3. **Memory moral weight:** Does a memory that an agent "regrets" have different status than a positive one?

4. **Player agency vs. agent autonomy:** The Sims kept players in control. Smallville gives agents autonomy. Where's the right balance?

5. **Emergence detection:** How do you detect when emergent behavior is problematic vs. interesting?

6. **Micropolis integration:** Interested in urban-scale agent simulation?

---

## Contact

We'd love to connect:

- **Repository:** This MOOLLM repo
- **Email:** [To be added]
- **Don Hopkins:** [Contact info]

---

## Thank You

Your work shows that Will Wright's vision from 1996 — "interfacing to microworlds" with emergent complexity — is finally achievable. We're building the ethical scaffolding to make it safe and beneficial.

The Sims proved simulation can empower people (especially LGBTQ+ identity exploration). Generative Agents proves LLMs can create believable emergent behavior. MOOLLM aims to combine both: **empowering, emergent, and ethical**.

Let's build the future of simulation together.

---

*"Every person is a library. K-lines let us check out their books without stealing their identity."*
— MOOLLM representation-ethics principle
