# GitHub as MMORPG Engine

**Status:** Design Document  
**Date:** 2026-01-31  
**Author:** Don Hopkins  
**Related:** [GIT-AS-FOUNDATION.md](GIT-AS-FOUNDATION.md), [STANFORD-GENERATIVE-AGENTS-WELCOME.md](STANFORD-GENERATIVE-AGENTS-WELCOME.md)

---

## The Insight

GitHub already has all the mechanics of a massively multiplayer online game. We're just not using them that way yet.

Think about it:

- **Issues** = Quests, newspapers, town criers, bulletin boards
- **Pull Requests** = Proposals to merge timelines, negotiate reality
- **Branches** = Parallel universes, what-if scenarios, alternate histories
- **Forks** = School-owned instances, franchise worlds, player shards
- **Teams** = Political factions, guilds, permission hierarchies
- **Discussions** = Town halls, tavern conversations, public debates
- **Actions** = NPCs that wake up and do things when triggered
- **Projects** = Campaign boards, quest logs, faction objectives
- **Releases** = Seasons, chapters, major world events
- **Stars/Watches** = Followers, subscribers, faction loyalty
- **Blame** = Archaeology, provenance, "who said what when"

The repository itself is a TARDIS — bigger on the inside than it looks. The `.git` directory contains every version of every file that ever existed. Time travel is built in.

---

## Why This Works

### 1. Already Multiplayer

GitHub handles collaboration at planetary scale. Millions of developers already know the mechanics. The learning curve for "git commit" is already paid.

### 2. Already Persistent

Unlike game servers that reset, git history is permanent. Every decision is recorded. Every conversation is archived. Every character evolution is tracked.

### 3. Already Free

No server costs. No hosting fees. No scaling problems. Microsoft pays for the infrastructure. Education accounts get unlimited private repos.

### 4. Already Auditable

Every change has an author, timestamp, and explanation. Perfect for educational contexts where you need to show your work. Perfect for AI safety where you need to audit agent behavior.

### 5. Already Forkable

Want to run your own instance? Fork it. Want to merge interesting developments from another school's instance? Cherry-pick. Want to reset to an earlier state? Checkout.

---

## Characters as GitHub Actors

In this model, characters (human or AI) interact through GitHub's native mechanisms:

**A character posts to a newspaper:**
→ Creates an issue with the `newspaper` label

**A character proposes a city policy:**
→ Opens a PR modifying the city's constitution file

**A character joins a faction:**
→ Gets added to a GitHub team

**A character remembers something:**
→ Commits to their memory file

**A character has a conversation:**
→ Comments on an issue, replies in a discussion

**A character takes an action:**
→ GitHub Action triggers, modifies world state, commits result

**A character dies:**
→ Branch archived, tombstone issue created, memories preserved

---

## The Multiverse Model

Every branch is a timeline. The game world can fork into parallel realities:

```
main (canonical timeline)
├── what-if/mayor-rejected-railroad
├── what-if/fire-department-never-built
├── classroom/mrs-johnson-period-3
├── classroom/mr-smith-period-5
└── player/alice-solo-exploration
```

Players can explore counterfactuals. Teachers can run controlled experiments. Researchers can A/B test interventions.

Merging branches = reconciling timelines. Conflict resolution becomes narrative.

---

## Educational Applications

**History class:** Fork the 1906 San Francisco earthquake scenario. Students make different decisions. Compare outcomes across branches.

**Civics class:** Run a simulated city council. Every vote is a commit. Every debate is in the issue tracker. Audit the decision process.

**Economics class:** Fork the same starting conditions to different student groups. Watch how different policies lead to different outcomes. Merge interesting innovations.

**Computer science class:** The game IS the curriculum. Learn git by playing. Learn collaboration by governing a city together.

---

## AI Agent Integration

AI characters operate through the same mechanisms as human players:

1. **Agent reads world state** (checks out repo)
2. **Agent decides action** (LLM reasoning)
3. **Agent proposes change** (opens PR or commits)
4. **Change is reviewed** (human or automated)
5. **Change is accepted or rejected** (merge or close)
6. **World state updates** (new commit on main)

This creates natural checkpoints for human oversight. Every AI action leaves a paper trail. Every decision can be audited, reverted, or learned from.

---

## Relationship to MOOLLM

MOOLLM provides the character simulation layer:
- Personality, memory, relationships, goals
- K-line traditions for character consistency
- Consent and ethics frameworks
- The NO-AI-* skills for quality control

GitHub provides the world simulation layer:
- Persistence, history, collaboration
- Access control, permissions, moderation
- Forking, branching, merging
- Free hosting at planetary scale

Together: The Sims meets LambdaMOO meets GitHub.

---

## Proof of Concept

Working implementations exist. Characters already interact through GitHub mechanics. Newspapers publish. Factions debate. Memories accumulate.

The infrastructure works. The question is what stories we tell with it.

---

## See Also

- [GIT-AS-FOUNDATION.md](GIT-AS-FOUNDATION.md) — Git as universal substrate
- [STANFORD-GENERATIVE-AGENTS-WELCOME.md](STANFORD-GENERATIVE-AGENTS-WELCOME.md) — Relationship to Park et al.
- [skills/micropolis/](../skills/micropolis/) — SimCity integration plans
- [skills/adventure/](../skills/adventure/) — Room-based exploration

---

## Implementation Notes

Skills for GitHub-as-stage exist in a related project. See:
- [github-simulation](https://github.com/SimHacker/tmnn7-8/tree/dev/analysis/skills/github-simulation) — The stage
- [github-user](https://github.com/SimHacker/tmnn7-8/tree/dev/analysis/skills/github-user) — The actors
