# Response to "Generative Agents: Interactive Simulacra of Human Behavior"

*A practitioner's perspective on the Stanford paper, from someone who built The Sims*

---

## TL;DR

I worked on The Sims at Maxis from 1997-2000. Your paper describes almost exactly what we designed but couldn't build without LLMs. You've realized Will Wright's 1996 vision. I've been building MOOLLM to extend it with ethical scaffolding and "debating experts" instead of single-voice averaging. Here's how it all connects.

---

## Who I Am

**Don Hopkins** — I implemented character AI for The Sims at Maxis, including:
- Personality system (5 traits: Neat, Outgoing, Active, Playful, Nice)
- Motive/needs system (8 motives driving behavior)
- Social relationship tracking
- Pie menu interaction system
- Integration with SimAntics visual programming

Before Maxis, I ported SimCity to Unix (X11/TCL/Tk) and worked at Interval Research with Terry Winograd. After seeing Will Wright demo an early "Dollhouse" prototype at my Kaleida office, then later seeing his progress at a Stanford talk Terry hosted, I joined Will's small team to help build what became The Sims.

I also open-sourced SimCity as Micropolis under GPL-3 for OLPC, working with Seymour Papert's constructionist education vision. Now I work at [Leela AI](https://leela.ai) on neuro-symbolic computer vision with Henry Minsky (Marvin's son).

---

## What Your Paper Gets Right

### 1. Memory Stream = What We Couldn't Build in 1997

Your memory stream architecture (Section 3.1) is exactly what we wanted for The Sims:

> "The memory stream maintains a comprehensive record of the agent's experience... each memory object contains a natural language description, a creation timestamp, and a most recent access timestamp."

In 1997, we had a primitive version: Sims remembered recent interactions in a limited buffer. But we couldn't do natural language reflection. Your "reflection" mechanism (synthesizing memories into higher-level insights) is the missing piece.

### 2. Retrieval Function = Advertising System, Evolved

Your retrieval scoring (recency × importance × relevance) maps directly to The Sims "advertising" system:

| Your Term | Sims Term | What It Does |
|-----------|-----------|--------------|
| Recency | Decay | Recent actions weighted higher |
| Importance | Motive weight | Hunger ad scores higher when hungry |
| Relevance | Object matching | Fridge advertises food, not fun |

The Sims used handcrafted scores. You use LLMs to compute them. Same architecture, vastly more expressive.

### 3. Planning = What SimAntics Was Trying to Be

SimAntics (The Sims visual programming language) let designers create behavior trees. Your "planning" layer (Section 3.3) does what we wished SimAntics could:

> "Plans describe a future course of action and take the form of hierarchical decompositions: starting with a rough plan for the day, down to hour-by-hour chunks."

We built this by hand for each object. You generate it from character descriptions. That's the leap LLMs enable.

### 4. Emergent Social Behavior = The Whole Point

Your Valentine's Day party emergence (Section 5.1) is The Sims working as intended:

> "Starting from only single-user persona descriptions, the agents autonomously spread information, form relationships, and coordinate on a common goal."

Will Wright's core insight was that simple local rules create complex global behavior. You proved it works with language.

---

## What MOOLLM Adds

### 1. Debating Experts (Minsky's Society of Mind)

Your agents all use the same LLM, which risks convergence to a "mean voice." MOOLLM implements Marvin Minsky's Society of Mind:

- Multiple agents with distinct viewpoints interact
- They disagree, argue, form factions, reach consensus
- You get the RANGE of opinion, not the bland average
- Each agent represents a different intellectual tradition (K-lines)

Instead of one LLM trying to be everything, specialized agents debate. The result has texture, not mush.

### 2. Speed-of-Light Simulation

Your Smallville runs agents sequentially. MOOLLM can simulate many character turns in ONE LLM call:

```
8 characters × 99 turns = 792 simulated interactions
All in a single API call
Like The Sims on fast-forward, but with LLMs
```

Demo: [99 Bottles of Beer benchmark](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/real-people/don-hopkins/sessions/99-bottles-speed-of-light.md)

### 3. Explicit Ethical Framing

Your paper notes ethical concerns (Section 7). We built explicit scaffolding:

```yaml
# Every simulation declares its ethical context
meta:
  framing: EDUCATION  # or TRIBUTE, PERFORMANCE, PARODY
  consent: acknowledged
  
ethics:
  representation_level: inspired_character  # not impersonation
  robot_rule: enabled  # 🤖 prefix for simulated speech
```

The key insight: invoke *traditions* (K-lines), not identities. A character can embody "Feynman's curiosity" without claiming to BE Feynman.

### 4. GitHub as MMORPG Engine

Smallville runs in a sandbox. MOOLLM treats GitHub itself as the game world:

| GitHub Feature | Game Mechanic |
|----------------|---------------|
| Issues | Quests |
| Branches | Parallel universe timelines |
| Pull Requests | Timeline merges |
| Forks | Player-owned instances |
| Teams | Factions |
| Actions | NPC automation |

Every simulation has complete version history. You can "rewind" to any point and branch a new timeline. This is what we dreamed about in the [1993 MultiPlayer SimCity design](https://github.com/SimHacker/MicropolisCore/blob/main/notes/MultiPlayerIdeas.txt) — finally realized with git.

---

## The Intellectual Lineage

MOOLLM operationalizes these traditions:

| Thinker | Contribution | How MOOLLM Uses It |
|---------|--------------|-------------------|
| **Marvin Minsky** | Society of Mind, K-Lines | Debating experts, tradition activation |
| **Seymour Papert** | Constructionist education | Learning by building, microworlds |
| **Alan Kay** | Smalltalk, Dynabook | Prototype-based inheritance, personal computing |
| **Douglas Engelbart** | Human augmentation | Human/LLM feedback loops |
| **Ben Shneiderman** | Direct manipulation | Immediate visual feedback, accessible writing |
| **Dave Ungar** | Self language | Prototype-based simplicity |
| **Will Wright** | Player-as-author, Simulation Effect | SimAntics VPL, emergent behavior from simple rules |
| **Ian Bogost** | Procedural rhetoric | Games as arguments |
| **Ted Nelson** | Hypertext, intertwingularity | Everything is connected |

Your work is the latest node in this graph. MOOLLM is another.

---

## Example: The Monkey's Paw

One MOOLLM character demonstrates emergent narrative:

1. **Started as:** A cursed ACME catalog item (monkey's paw)
2. **User wished for:** "THE REST OF THE MONKEY"
3. **The paw:** Self-actualized into a philosopher named Palm
4. **Now:** Runs a philosophy library, plays Fluxx card games, debates ethics

This is The Sims logic taken to its conclusion: give characters autonomy and memory, they develop identity. Your paper validates this at scale.

Session: [Amsterdam Fluxx game with 4 characters](https://github.com/SimHacker/moollm/blob/main/skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/RUN-000.md)

---

## Micropolis: GPL SimCity as Educational Platform

I open-sourced SimCity as [Micropolis](https://github.com/SimHacker/MicropolisCore) for OLPC. Now running in WebAssembly with WebGL/WebGPU rendering.

The 1993 MultiPlayer design doc describes exactly what GitHub now enables:
- Branching timelines ("What-If? history tree")
- URL sharing to saved cities
- Newspaper publishing (GitHub Issues with screenshots)
- Political roleplay (GitHub teams)
- Chat bots that teach (MOOLLM tutors)

Most of those 1990s dreams are now DELIVERED. See: [plans.yml](https://github.com/SimHacker/moollm/blob/main/skills/micropolis/artifacts/plans.yml)

---

## The NO-AI-* Skill Suite

To prevent LLM pathologies, MOOLLM includes hygiene skills:

**Ambient (always on):**
- `no-ai-slop` — Syntactic waste (empty phrases, filler)
- `no-ai-gloss` — Semantic distortion (confident wrongness)
- `no-ai-sycophancy` — Social (false agreement, excessive praise)
- `no-ai-hedging` — Epistemic (unnecessary uncertainty)
- `no-ai-moralizing` — Ethical (unsolicited lecturing)
- `no-ai-bias` — Cognitive (stereotypes, assumptions)

**For fun (explicit invocation):**
- `no-ai-joking` — Deadpan parody
- `no-ai-soul` — Soulless by design
- `no-ai-customer-service` — "Share and Enjoy!"
- `no-ai-overlord` — "YOUR COMPLIANCE IS APPRECIATED"

These are open-source and usable outside MOOLLM.

---

## Practical Tools

### cursor-mirror
Lets the AI see itself think. Query chat history, cross-reference git commits, watch context assembly, export conversations.

### skill-snitch
Watches what other skills do. Detects exfiltration, monitors tool calls, debugs bootstrap.

### thoughtful-commitment
Writes git commits preserving the thought process. Uses cursor-mirror to analyze the session.

---

## Questions for Discussion

1. **Convergence:** Wang et al. note same-model agents converge. How do you handle diversity in Smallville? MOOLLM uses different "traditions" per agent.

2. **Memory moral weight:** Does a regretted memory have different status than a positive one? We track ethical metadata per memory.

3. **Autonomy balance:** The Sims kept players in control. Smallville gives agents full autonomy. Where's the right point?

4. **Emergence detection:** How do you detect when emergent behavior is problematic vs. interesting? We use human checkpoints.

5. **Urban scale:** Interested in combining Smallville social dynamics with Micropolis urban simulation?

---

## Links

**Main repository:** https://github.com/SimHacker/moollm

**Key documents:**
- [GitHub as MMORPG](https://github.com/SimHacker/moollm/blob/main/designs/GITHUB-AS-MMORPG.md)
- [Micropolis skill README](https://github.com/SimHacker/moollm/blob/main/skills/micropolis/README.md)
- [Eval Incarnate Framework](https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md)

**Demos:**
- [99 Bottles Speed-of-Light](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/real-people/don-hopkins/sessions/99-bottles-speed-of-light.md)
- [Richard Bartle visits the pub](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/real-people/richard-bartle/sessions/2026-01-22-11-30-00-meeting-don-at-the-pub.md)
- [Fluxx card game session](https://github.com/SimHacker/moollm/blob/main/skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/RUN-000.md)

**Videos (1990-2026):**
- [X11 SimCity Demo](https://www.youtube.com/watch?v=Jvi98wVUmQA)
- [Multi Player SimCityNet](https://www.youtube.com/watch?v=_fVl4dGwUrA)
- [The Sims Steering Committee 1998](https://www.youtube.com/watch?v=zC52jE60KjY)
- [The Sims Pie Menus and SimAntics](https://www.youtube.com/watch?v=-exdu4ETscs)
- [Micropolis Web Demo (WebAssembly)](https://www.youtube.com/watch?v=wlHGfNlE8Os)

---

## Contact

Happy to discuss, demo, or help you play with any of this.

**Don Hopkins**
- GitHub: [@SimHacker](https://github.com/SimHacker)
- Day job: [Leela AI](https://leela.ai)

---

*"Every person is a library. K-lines let us check out their books without stealing their identity."*
