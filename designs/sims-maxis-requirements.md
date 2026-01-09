# Maxis Sim Game Requirements

> *"What makes a game a 'Sim'?"*
> — M. Perry, December 20, 1996

---

## Summary

This document comprehensively summarizes an internal Maxis marketing study (December 1996) that identified seven core requirements for what makes a game a "Sim game." These principles — born from studying customer expectations and distilled into design requirements — directly inform MOOLLM's architecture.

The Seven Points of Sim are not just game design guidelines. They're principles for creating **compelling simulations that teach through play**.

---

## Table of Contents

1. [The Seven Points of Sim](#the-seven-points-of-sim)
2. [Bonus: The Joy of Destruction](#bonus-requirement-the-joy-of-destruction)
3. [MOOLLM Design Alignment](#moollm-design-alignment)
4. [The Meta-Lesson](#the-meta-lesson-why-sim-games-teach)

---

## The Study Context

The Maxis marketing department studied customer expectations of Maxis Sim games. The study revealed **seven descriptions** of what the Maxis Sim player thought a Sim game should be.

Key insight from M. Perry:

> *"While the 'Seven Points of Sim' descriptions reflect customer expectations, they are not all necessarily the ingredients for a Sim game. To understand why Sim players perceive Sim games the way they do, we can look at the key factors that make a game a 'Sim'."*

The seven points aren't a checklist — they're **emergent properties** of well-designed simulation games. Players *expect* them because successful Sim games naturally produce them.

---

## The Seven Points of Sim

### 1. Dilemma

> *"Players must always grapple with difficult decisions."*

**The Principle:** Good decisions are never easy. Every choice involves trade-offs.

**Maxis Examples:**
- **SimCity:** Pollution may be a problem, but there might be a strong industrial demand. Do you accept pollution for jobs?
- **SimTower:** Condo-dwellers will need elevators heading down (to leave), while office workers will need elevators heading up (to arrive). How do you serve both?

**Key Insight:** Dilemma creates engagement. If the optimal choice is obvious, there's no game.

**MOOLLM Implementation:**

| Sims Dilemma | MOOLLM Parallel |
|--------------|-----------------|
| Pollution vs. industry | Character needs conflict (fun vs. rest) |
| Elevator direction | Resource allocation, time budgeting |
| Growth vs. sustainability | Short-term vs. long-term character development |

The [`needs`](../skills/needs/) skill creates dilemmas by design:
- Satisfying **fun** takes time away from **productivity**
- Satisfying **social** requires other characters
- Satisfying **hygiene** costs resources or time
- Characters can't maximize everything — they must choose

The [`economy`](../skills/economy/) skill creates resource dilemmas:
- Spend money now for comfort, or save for bigger purchase?
- Invest in relationships (social), or invest in skills (career)?

**MOOLLM Skill:** [`needs`](../skills/needs/), [`economy`](../skills/economy/), [`scoring`](../skills/scoring/)

---

### 2. Crisis

> *"Crisis can also mean disasters. Players occasionally need to abandon long term strategy in favor of short-term success."*

**The Principle:** Plans fail. Emergencies happen. Adaptability is more important than optimization.

**Maxis Examples:**
- **SimCity/SimTower:** If a fire is burning, *"players might need to destroy all their creations in the surrounding area"* to contain it
- Disasters force **immediate response** — long-term planning goes out the window

**Key Insight:** Crisis tests mastery. It reveals whether players truly understand the system or just memorized an optimal path.

**MOOLLM Implementation:**

| Sims Crisis | MOOLLM Parallel |
|-------------|-----------------|
| Fire spreading | The Grue (darkness hazard in [`adventure`](../skills/adventure/)) |
| Natural disasters | Random events, character emergencies |
| Forced destruction | Difficult choices with permanent consequences |

Crisis events in MOOLLM:
- **The Grue:** Darkness kills. Characters must find light or die.
- **Buff expiration:** Temporary advantages end, forcing adaptation
- **NPC actions:** Other characters make choices that disrupt plans
- **External events:** Messages, visitors, emergencies arrive

The [`buff`](../skills/buff/) skill creates temporary states that players must manage. The [`adventure`](../skills/adventure/) skill introduces hazards and emergencies.

**MOOLLM Skill:** [`adventure`](../skills/adventure/), [`buff`](../skills/buff/), [`time`](../skills/time/)

---

### 3. Budgeting

> *"The amount of funding a player has acts as both a limiting factor and a kind of score."*

**The Principle:** Resources are finite. Every action has a cost. Even mistakes cost money — and there are no refunds.

**Key Insight:**

> *"'Cheats' to gain more money are the most popular cheats."*

Money constraints are **felt deeply** by players. The desire to bypass them proves how central budgeting is to the game experience.

**MOOLLM Implementation:**

| Sims Budgeting | MOOLLM Parallel |
|----------------|-----------------|
| Money as score and constraint | Economy skill tracks resources |
| No refunds | Actions have permanent costs |
| Popular money cheats | Abundance mode for different play styles |

The [`economy`](../skills/economy/) skill tracks:
- **Money/resources:** What characters can afford
- **Costs:** Every action's price
- **Value:** What things are worth
- **Flow:** Income and expenses over time

Budgeting creates meaning. If everything is free, nothing matters. MOOLLM uses resource constraints to make choices meaningful.

**MOOLLM Skill:** [`economy`](../skills/economy/), [`needs`](../skills/needs/)

---

### 4. Aesthetics

> *"Artwork is important for players to admire their creations."*

**The Principle:** Players need to see the results of their work. Beauty is a reward.

**Three Purposes of Aesthetics:**

1. **Admiration:** Players admire their creations
2. **False superiority:** The ability to place things in various places *"fakes players into believing that their city or tower designs are 'better' than other's"*
3. **Reward:** Aesthetics mark achievement — *"In SimTower, an aesthetic reward for reaching the 100th floor is the ability to place a cathedral. This is akin to 'winning'."*

**Key Insight:** Aesthetics aren't decoration. They're **feedback loops** and **motivation systems**.

**MOOLLM Implementation:**

| Sims Aesthetics | MOOLLM Parallel |
|-----------------|-----------------|
| Visual artwork | Rich room descriptions |
| Admiring creations | Object inventories, character presentations |
| Achievement markers | Special items, titles, room decorations |
| Cathedral at floor 100 | Legendary items, achievement objects |

While MOOLLM is text-based, it provides aesthetic feedback through:
- **Rich descriptions:** Rooms aren't just lists — they have atmosphere
- **Object inventories:** See what you've collected
- **Character presentations:** Appearance, clothing, expressions
- **Session logs:** The narrative record of what you've built

The [`visualizer`](../skills/visualizer/) skill can render locations. The [`room`](../skills/room/) skill supports detailed descriptions.

**MOOLLM Skill:** [`visualizer`](../skills/visualizer/), [`room`](../skills/room/)

---

### 5. Change in Rules over Time

> *"Rule changes cause players to change their playing strategy."*

**The Principle:** What works early may not work late. The game evolves.

**Maxis Examples:**
- **SimCity:** Demand for Industry is high at first, but then swings to Commerce as the city develops
- **SimTower:** The placement of condos is important at first, but *"nearly irrelevant after the 3rd Star"*

**Key Insight:** Rule changes prevent stagnation. Players must adapt, not just execute a known optimal strategy.

**MOOLLM Implementation:**

| Sims Rule Changes | MOOLLM Parallel |
|-------------------|-----------------|
| Demand shifts | Character development, changing needs |
| Strategy obsolescence | Buff/debuff mechanics |
| Phase transitions | Room state evolution |

Rule changes in MOOLLM:
- **Character development:** As characters grow, their needs and abilities change
- **Buff/debuff mechanics:** Temporary modifiers alter what's optimal
- **Room evolution:** Spaces change over time (day/night, events, damage)
- **Relationship evolution:** Friends become family, strangers become allies

The [`buff`](../skills/buff/) skill applies temporary and permanent modifiers. The [`time`](../skills/time/) skill advances the world state.

**MOOLLM Skill:** [`buff`](../skills/buff/), [`character`](../skills/character/), [`time`](../skills/time/)

---

### 6. Visual/Graphical Feedback

> *"A Simulator is nothing but formulae operating on a data set. The player's main interpretation of the change in data is graphical."*

**The Principle:** Players can't see numbers. They see buildings, faces, environments. The visual representation IS the interface to the simulation.

**Counter-example:**

> *"An example failure in graphical feedback is Outpost from Sierra, where player feedback is in the form of numbers in a dialog box."*

Numbers in a dialog box are **not** feedback. They're raw data. Players need to SEE the consequences.

**Key Insight:** The visual layer isn't just presentation — it's **translation**. It converts simulation state into human-understandable form.

**MOOLLM Implementation:**

| Sims Visual Feedback | MOOLLM Parallel |
|----------------------|-----------------|
| Buildings growing | Rich narrative descriptions |
| Faces showing emotion | Character expressions in prose |
| Environmental changes | Room state descriptions |
| Not "numbers in dialog box" | Not raw YAML dumps |

MOOLLM provides feedback through:
- **Narrative descriptions:** What the room looks like, how characters feel
- **State changes communicated narratively:** "The fire spreads to the next room" not "fire_spread: true"
- **Character expressions:** "She smiles warmly" not "mood: happy"
- **Environmental atmosphere:** "The room grows cold and dark" not "temperature: 0"

The [`empathic-expressions`](../skills/empathic-expressions/) skill provides emotional vocabulary. The [`room`](../skills/room/) skill provides environmental descriptions.

**MOOLLM Skill:** [`empathic-expressions`](../skills/empathic-expressions/), [`room`](../skills/room/)

---

### 7. Cause & Effect Not Immediately Apparent

> *"Because of the interleaving data sets in the simulators, players may not initially understand why certain actions have unexpected effects."*

**The Principle:** Discovery is the game. If causality is obvious, there's nothing to learn.

**Key Insight:**

> *"One of the compelling reasons to play is to discover and understand various causes and effects."*

Players are **motivated** by mystery. The hidden causality creates a puzzle that rewards exploration and experimentation.

**MOOLLM Implementation:**

| Sims Hidden Causality | MOOLLM Parallel |
|-----------------------|-----------------|
| Interleaving data sets | Skill interactions |
| Unexpected effects | Emergent behavior |
| Discovery as gameplay | LLM's "eval" nature |

Hidden causality in MOOLLM:
- **Skill interactions:** Skills affect each other in non-obvious ways
- **Character relationships:** Social dynamics create surprising outcomes
- **Object combinations:** Using items together produces unexpected results
- **LLM emergence:** Even the designer doesn't always predict what the LLM will generate

The LLM's nature as an "eval" interpreter means that MOOLLM has **genuine emergence** — the system can surprise its creators.

**MOOLLM Skill:** Emergent property of skill composition

---

## Bonus Requirement: The Joy of Destruction

> *"Who says there is no violence in Sim games?"*

**The Principle:** Players want to destroy their creations. This is not a bug — it's a feature.

**The Pattern:**

> *"A favorite activity of the Sim player is to save a 'masterpiece' copy of their creation, then unleash disaster after disaster, and bulldoze like crazy."*

**Why It Works:**
1. **Catharsis:** Destruction is satisfying
2. **Experimentation:** See what breaks, learn how systems work
3. **No permanent consequence:** The masterpiece is saved, destruction is reversible
4. **The Calvin Syndrome:** (See [sims-will-wright-microworlds-1996.md](./sims-will-wright-microworlds-1996.md#the-calvin-syndrome)) Players test validity by destruction

**MOOLLM Implementation:**

| Sims Destruction | MOOLLM Parallel |
|------------------|-----------------|
| Save masterpiece, then destroy | Git branching, session saves |
| Unleash disasters | Experimental sessions |
| Bulldoze like crazy | Edit YAML files freely |
| "What if" experiments | Branching timelines |

MOOLLM supports destruction through:
- **Git branching:** Create a branch, experiment destructively, discard if unwanted
- **Session saves:** Return to earlier states
- **Editable files:** Direct manipulation of world state
- **"What if" scenarios:** Explore alternatives without commitment

The filesystem-as-world means players can always restore from git history. Destruction is always reversible.

---

## MOOLLM Design Alignment

### Summary Table

| Maxis Requirement | MOOLLM Implementation | Key Skill |
|-------------------|----------------------|-----------|
| **Dilemma** | Conflicting needs, resource constraints | [`needs`](../skills/needs/), [`economy`](../skills/economy/) |
| **Crisis** | Emergent events, the Grue, hazards | [`adventure`](../skills/adventure/), [`buff`](../skills/buff/) |
| **Budgeting** | Economy skill, resource tracking | [`economy`](../skills/economy/) |
| **Aesthetics** | Rich room descriptions, object inventories | [`room`](../skills/room/), [`visualizer`](../skills/visualizer/) |
| **Rule Changes** | Buffs/debuffs, character development | [`buff`](../skills/buff/), [`time`](../skills/time/) |
| **Visual Feedback** | Narrative descriptions, not data dumps | [`empathic-expressions`](../skills/empathic-expressions/) |
| **Hidden Causality** | Emergent behavior, skill interactions | Skill composition |
| **Destruction** | Branching sessions, git saves, what-if | Filesystem + git |

### Deep Alignment

The Seven Points are not arbitrary. They describe **what makes simulations compelling to humans**:

1. **Dilemma** → Players feel agency when choices matter
2. **Crisis** → Players feel mastery when they overcome emergencies
3. **Budgeting** → Players feel consequence when resources are scarce
4. **Aesthetics** → Players feel pride when creations are beautiful
5. **Rule Changes** → Players feel growth when strategies evolve
6. **Visual Feedback** → Players feel immersion when they see the world
7. **Hidden Causality** → Players feel discovery when they learn secrets

MOOLLM implements all seven because it's designed to create **compelling simulations** — not just functional ones.

---

## The Meta-Lesson: Why Sim Games Teach

The Seven Points explain why Sim games are **educational without trying to be**:

| Point | Educational Mechanism |
|-------|----------------------|
| Dilemma | Teaches trade-off thinking |
| Crisis | Teaches adaptability and resilience |
| Budgeting | Teaches resource management |
| Aesthetics | Teaches pride in craft |
| Rule Changes | Teaches continuous learning |
| Visual Feedback | Teaches systems thinking |
| Hidden Causality | Teaches scientific inquiry |

Will Wright understood this deeply:

> *"The digital models running on a computer are only compilers for the mental models users construct in their heads."*
> — Will Wright, 1996

The game isn't the simulation running on the computer. The game is the **mental model** implanted in the player's mind. The Seven Points are the mechanisms by which this implantation occurs.

MOOLLM inherits this philosophy. Skills aren't just game mechanics — they're **mental model compilers** that teach through play.

---

## Source

**Document:** MAXIS SIM GAME REQUIREMENTS  
**Author:** M. Perry  
**Date:** December 20, 1996  
**Pages:** 2

---

## See Also

- [sims-happy-friends-home.md](./sims-happy-friends-home.md) — Project X proposal (October 1996)
- [sims-will-wright-microworlds-1996.md](./sims-will-wright-microworlds-1996.md) — Will Wright's Stanford lecture (April 1996)
- [sims-design-index.md](./sims-design-index.md) — Master index of Sims documents
- [sims-team-history.md](./sims-team-history.md) — Team history
- [sims-find-best-action.md](./sims-find-best-action.md) — Action selection algorithm
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — Incarnate framework

---

*"To understand why Sim players perceive Sim games the way they do, we can look at the key factors that make a game a 'Sim'."*
— M. Perry, 1996

*MOOLLM is a Sim game. It follows the Seven Points. It teaches through play.*
