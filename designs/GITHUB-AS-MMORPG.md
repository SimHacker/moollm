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

## Prior Art and Related Work

Research confirms: many pieces exist, but nobody has combined them all.

### GitHub Gamification (Exists)

Projects that gamify GitHub contributions:

- **Space Commit** — GitHub Actions Hackathon 2021 winner. Contributors become heroes.
- **Commit Conquest** — Leaderboard competition for commits.
- **Git-Gamify** — CLI that turns git workflow into RPG with levels and achievements.
- **GitHub Achievements** (2022) — Official badges for milestones (first commit, Mars missions).
- **Profile games** — Pacman/Snake contribution graphs, dynamic trophies.

**Gap:** These gamify *individual developer metrics*, not collaborative world-building.

### GitHub Collaborative Fiction (Exists)

Projects using Git for branching narratives:

- **Gitaverse Odyssey** — Each commit = one sentence. Branches = parallel universes. 
  Literally calls it a "gitaverse" of interconnected narratives.
- **Collaborative-Fiction** — Rust app for group storytelling.
- **Try-Writing-a-Story** — Learn Git by adding to story.md via PRs.
- **Passages** — Platform for branching collaborative narratives.
- **Living Story World** — AI-generated illustrated story chapters across universes.

**Gap:** These lack persistent characters, world simulation, or AI agents.

### GitHub as Social Simulation (Academic Research)

The DARPA SocialSim Challenge (2019) treated GitHub as a complex techno-social system:

- **3 million simulated agents** producing 30 million actions across 6 million repositories
- Best models sampled from stationary probability distributions per agent
- Key finding: GitHub users change behavior slowly; individual characterization matters
- Stigmergy approaches (like ant colonies) model how developers coordinate

Research on GitHub network structure:
- Power-law distributions in contributions, followers, watchers
- Geographic distance influences collaboration patterns
- Remarkably low reciprocity in social connections

**Gap:** These simulate *developer behavior*, not fictional character roleplay.

### Stanford Generative Agents / AI Town (2023)

The famous Smallville simulation:

- 25 LLM-powered agents in a virtual town
- Memory, reflection, planning architecture
- **Valentine's Day emergence**: One agent decides to throw party → invitations spread → dates form → everyone attends
- Human evaluators found agents more believable than human roleplayers

**Gap:** Not on GitHub. Custom simulation engine. No collaborative forking model.

### Git History as Narrative (Emerging)

Tools that treat commit history as story:

- **GitNarrative** — Analyzes repos to generate development stories in multiple styles
- **GitStory** — Transforms repos into cinematic narratives, anime epics, Shakespearean monologues
- **git-story** — Video animations of commit history

**Gap:** Treats commits as *documentation of work*, not *fiction*.

### LLM Training on GitHub (Research)

Leela's own Steve Kommrusch's PhD research:

- **Training LLMs to fix bugs** using GitHub commits, PRs, discussions
- Learning from the *conversation* around code changes, not just the code
- Understanding *why* changes were made from issue context
- Extracting repair patterns from commit messages and PR reviews

This connects to GitHub-as-MMORPG: agent characters can learn from the "game history" of past players (commits), improving their strategies over time.

### Autonomous AI Coding Agents (2024-2025)

AI that operates through GitHub natively:

- **Devin AI** — Autonomous developer. Plans, edits files, runs tests, opens PRs, asks for clarification.
- **GitHub Copilot Workspace** — AI-assisted PR creation.
- **Cursor agents** — Background tasks that commit and create PRs.

**Gap:** These are *coding assistants*, not *characters in a world simulation*.

### What's Novel in GitHub-as-MMORPG

Nobody has combined:

| Component | Exists? | In MOOLLM? |
|-----------|---------|------------|
| GitHub gamification | ✓ | ✓ |
| Branching narrative | ✓ | ✓ |
| Social simulation research | ✓ | ✓ (applied) |
| Generative agents with memory | ✓ | ✓ |
| Autonomous AI on GitHub | ✓ | ✓ |
| **Fictional characters as GitHub actors** | ✗ | ✓ |
| **Educational simulation with forkable worlds** | ✗ | ✓ |
| **Newspapers/quests as Issues** | ✗ | ✓ |
| **Timelines as branches, merge = negotiate reality** | ✗ | ✓ |
| **Free planetary-scale MMO infrastructure** | ✗ | ✓ |

The insight isn't any single piece — it's seeing GitHub's existing features 
as game mechanics that were there all along, waiting to be named.

---

## See Also

- [GIT-AS-FOUNDATION.md](GIT-AS-FOUNDATION.md) — Git as universal substrate
- [STANFORD-GENERATIVE-AGENTS-WELCOME.md](STANFORD-GENERATIVE-AGENTS-WELCOME.md) — Relationship to Park et al.
- [skills/micropolis/](../skills/micropolis/) — SimCity integration plans
- [skills/adventure/](../skills/adventure/) — Room-based exploration

---

## Implementation Notes

Skills for GitHub-as-stage exist in a related project. See:
- [github-simulation](https://github.com/SimHacker/tmnn7-8/tree/main/analysis/skills/github-simulation) — The stage
- [github-user](https://github.com/SimHacker/tmnn7-8/tree/main/analysis/skills/github-user) — The actors

---

## MOOLLM Gaps and Potential Skills

### Current Gaps

| Gap | Description | Priority |
|-----|-------------|----------|
| **Issue as Quest** | No skill for treating GitHub Issues as quests with objectives, rewards | High |
| **Newspaper Publisher** | No skill for generating in-world news from repository activity | High |
| **Timeline Manager** | No skill for managing parallel branch narratives | Medium |
| **Faction System** | No skill for GitHub Teams as political factions | Medium |
| **Merge Negotiation** | No skill for PR as "reality negotiation" between timelines | Medium |
| **Character Death** | No skill for archiving characters, creating tombstones | Low |
| **Achievement System** | No skill for tracking and awarding accomplishments | Low |

### Proposed Skills

#### `skill:github-quest`
Transform GitHub Issues into structured quests:
- Parse issue labels for quest type (main quest, side quest, daily)
- Extract objectives from issue body and checklist items
- Track completion via issue state and comments
- Award XP/reputation on issue close

#### `skill:github-newspaper`
Generate newspapers from repository activity:
- Aggregate commits, PRs, issues from time period
- Classify events as news categories (politics, crime, economy)
- Generate narrative summaries using LLM
- Publish as Issue with `newspaper` label

#### `skill:github-timeline`
Manage parallel universe branches:
- Track `what-if/*` branches as counterfactual timelines
- Visualize timeline divergence and convergence
- Support "timeline merge" narratives
- Cherry-pick interesting developments across timelines

#### `skill:github-faction`
Model GitHub Teams as political factions:
- Track faction membership via team APIs
- Model inter-faction relationships (ally, rival, neutral)
- Generate faction objectives as milestone issues
- Track faction influence via contribution metrics

#### `skill:github-merge-negotiation`
Model PRs as reality negotiations:
- Characters with stakes in different branches
- Structured debate in PR comments
- Voting mechanism via reactions
- Conflict resolution protocols

### Integration Points

These skills should integrate with existing MOOLLM infrastructure:

- **K-lines**: Quest objectives as activatable K-line bundles
- **Character memory**: Quest history persisted in character files
- **Adventure rooms**: Repository as explorable space
- **Consent framework**: NO-AI-DESTROY for irreversible actions

### Anti-Patterns to Avoid (Negative Examples)

From Gastown GitHub "cluster fuck experiences":
- Overuse of automation that obscures human intent
- PRs with hundreds of files that can't be reviewed
- Bot wars where automated processes conflict
- Loss of narrative coherence from too many parallel changes

---

## Media Coverage and References

### Academic Papers

- **Park et al. (2023)** — "Generative Agents: Interactive Simulacra of Human Behavior"
  - 25 LLM agents in Smallville simulation
  - Memory, reflection, planning architecture
  - Valentine's Day party emergence

- **DARPA SocialSim Challenge (2019)**
  - 3 million simulated agents, 30 million actions, 6 million repos
  - GitHub as techno-social system
  - Key finding: individual characterization matters

### Related Projects

- **Space Commit** (2021) — GitHub Actions Hackathon winner
- **Gitaverse Odyssey** — Each commit = one sentence, branches = parallel universes
- **Devin AI** (2024) — Autonomous developer opening PRs
- **GitHub Copilot Workspace** — AI-assisted PR creation

### Blog Posts and Articles

- [Don Hopkins on Pie Menus](https://medium.com/@donhopkins/pie-menus-936fed383ff1) — UI patterns applicable to game menus
- [Gesture Space](https://medium.com/@donhopkins/gesture-space-842e3cdc7102) — Input model concepts for character control

### DevOps to MooOps

The evolution: DevOps → GitOps → MooOps (MOOLLM Operations)

- **DevOps**: Developers doing operations
- **GitOps**: Git as single source of truth for infrastructure
- **MooOps**: MOOLLM characters as autonomous operators, with GitHub as the stage

Characters maintain infrastructure, respond to alerts, propose fixes via PR, and learn from past incidents through their memory systems.
