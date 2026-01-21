# Git as Foundation: The Universal Substrate of MOOLLM

**Status:** Design Document  
**Date:** 2026-01-21  
**Author:** Don Hopkins, with Claude  
**Related:** [MOOCO-TOOLS.md](../../mooco/designs/MOOCO-TOOLS.md), [kernel/](../kernel/), [skills/plain-text/](../skills/plain-text/)

---

## Executive Summary

Git is not merely a version control system for MOOLLM — it is the **universal substrate** upon which all persistent state, narrative provenance, and temporal navigation depend. This document explains why git is foundational, what capabilities it provides, and how it meshes with the Coherence Engine and cursor-mirror to create unprecedented introspective power.

---

## Part 1: Why Git Is Foundational

### 1.1 The TARDIS Property

A MOOLLM adventure directory is a **TARDIS** — bigger on the inside than it appears:

```
adventure-4/
├── characters/          # Current state of all characters
├── pub/                 # Current state of all rooms
├── sessions/            # Current narrative records
└── .git/                # THE TARDIS ENGINE
    └── objects/         # Every version that ever existed
    └── refs/            # Every timeline (branch) ever created
```

The `.git` directory contains **the complete history** of the micro-world:
- Every character's evolution
- Every room's changes
- Every decision point
- Every branch (parallel universe)
- The ability to travel to any moment

### 1.2 Files as State, Git as Time Machine

MOOLLM's design principle: **files ARE state**.

| Other Systems | MOOLLM |
|---------------|--------|
| Database stores state | YAML files store state |
| Queries return current state | `cat` returns current state |
| History in logs (maybe) | History in git (always) |
| Branching in application logic | Branching via `git branch` |
| Undo via application feature | Undo via `git revert` |

This is a deliberate architectural choice:

1. **Plain text is forever** — No format lock-in, no corruption, no migration hell
2. **Diffs are meaningful** — You can read a git diff and understand the narrative change
3. **Branches are free** — Fork a universe with one command
4. **Merge is built-in** — Reconcile parallel narratives with established tooling
5. **Collaboration is native** — Push/pull between storytellers

### 1.3 Narrative Provenance

Every property of every character has a **complete history**:

```bash
# Who gave Terpie this relationship?
$ git blame characters/animals/cat-terpie/CHARACTER.yml

abc123 (Don Hopkins 2026-01-06) relationships:
def456 (Coherence   2026-01-15)   biscuit:
def456 (Coherence   2026-01-15)     feeling: "He's family now"
```

Every line was written by someone (human or Coherence Engine) at some moment for some reason.

The **commit message** captures intent:

```
commit def456
Author: Coherence Engine
Date: 2026-01-15

    Incarnation Ceremony: Cat Council votes Biscuit into family
    
    After three hours of deliberation (mostly napping), the cats
    rendered their verdict on Biscuit's petition for family membership.
    
    - Terpie: Abstained (was meditating)
    - Stroopwafel: Yes (he catches the good crickets)
    - Motion carried. Biscuit is family.
```

This is **soul archaeology** — the complete history of how every character became who they are.

---

## Part 2: Git Operations as Narrative Operations

### 2.1 The Multiverse Metaphor

| Git Operation | Narrative Meaning |
|---------------|-------------------|
| `git commit` | Crystallize a moment in the universe |
| `git log` | Navigate through time |
| `git show` | Retrieve an old universe state |
| `git diff` | Compare parallel realities |
| `git branch` | Create a parallel timeline |
| `git checkout` | Jump between universes |
| `git merge` | Reconcile parallel timelines |
| `git blame` | Forensic archaeology — who/when/why |
| `git stash` | Pocket dimension for work-in-progress |

### 2.2 Branching as "What If"

```bash
# Main timeline
$ git log --oneline
abc123 Incarnation Ceremony: Kittens receive emoji souls
def456 Midnight Prowl: Cats explore the garden
ghi789 Biscuit arrives at the Cat Cave

# Create alternate timeline
$ git checkout -b what-if-biscuit-rejected
$ # Edit characters/animals/dog-biscuit/CHARACTER.yml
$ git commit -m "Alternate: Cat Council rejects Biscuit"

# Now two universes exist
$ git branch
* main
  what-if-biscuit-rejected
```

Each branch is a **parallel universe** that can:
- Evolve independently
- Be merged back if interesting
- Remain as an alternate canon
- Be compared via `git diff`

### 2.3 Time Travel as Debugging

```bash
# Terpie is acting strange. When did this start?
$ git log --oneline -- characters/animals/cat-terpie/CHARACTER.yml

# Go back to before the problem
$ git checkout abc123 -- characters/animals/cat-terpie/CHARACTER.yml

# Or branch from that point to explore
$ git checkout abc123 -b investigate-terpie-bug
```

Every debugging session is a time travel expedition.

---

## Part 3: Coherence Engine + Git Integration

### 3.1 The Commit Message as Intent Record

When the Coherence Engine makes changes, it writes commit messages that explain **narrative intent**, not just mechanical changes:

**Bad commit (mechanical):**
```
Updated CHARACTER.yml
```

**Good commit (narrative):**
```
Midnight Prowl: Terpie achieves zen state in moonlit garden

Terpie led the expedition but spent most of it meditating
on a warm stone. Stroopwafel did the actual hunting.
Myrcene fell asleep in a flower bed.

- Added memory: midnight_prowl
- Updated location: returned to cat_cave
- Mind mirror adjustment: stable +1 (garden was peaceful)
```

The commit message is **the story of what happened**. The diff is the mechanical record. Together, they're complete narrative provenance.

### 3.2 The Meshing of Git and Cursor-Mirror

MOOLLM has two introspection systems:

| System | What It Sees | Dimension |
|--------|--------------|-----------|
| **Git** | The multiverse — all timelines, branches, history | World history |
| **Cursor-mirror** | The orchestrator's brain — thinking, tool calls | Mind history |

These systems **mesh together** via commit IDs:

```
┌─────────────────────────────────────────────────────────────┐
│                     CURSOR-MIRROR                           │
│                     (Mind History)                          │
│                                                             │
│  [Event 142] Thinking: "The kittens need emoji souls..."    │
│  [Event 143] Tool: write_file(kitten-myrcene/CHARACTER.yml) │
│  [Event 145] Tool: git commit -m "Incarnation..."           │
│       │                                                     │
│       │ commit_id: abc123                                   │
│       ▼                                                     │
└───────┼─────────────────────────────────────────────────────┘
        │
        │  ← THE GEAR TOOTH (commit ID links both systems)
        │
┌───────┼─────────────────────────────────────────────────────┐
│       ▼                                                     │
│  commit abc123                                              │
│  Author: Coherence Engine                                   │
│  Date: 2026-01-15                                           │
│                                                             │
│      Incarnation Ceremony: Kittens receive emoji souls      │
│                                                             │
│                      GIT                                    │
│                 (World History)                             │
└─────────────────────────────────────────────────────────────┘
```

The commit ID appears in **both** systems, linking:
- What the Engine was thinking (cursor-mirror)
- What the Engine did (git)
- The result (current file state)

### 3.3 Full Causal Chain

For any piece of state, you can trace the complete chain:

```
User message: "Incarnate the kittens"
     ↓
[cursor-mirror: Event 140]
  User request received
     ↓
[cursor-mirror: Event 141]
  Thinking: "I need to invoke INCARNATION protocol..."
     ↓
[cursor-mirror: Event 142]
  Thinking: "Myrcene's terpene is sedating, so Active should be 0..."
     ↓
[cursor-mirror: Event 143]
  Tool call: write_file(kitten-myrcene/CHARACTER.yml)
     ↓
[cursor-mirror: Event 145]
  Tool call: git commit → abc123
     ↓
[git: commit abc123]
  "Incarnation Ceremony: Kittens receive emoji souls"
  diff: +active: 0  # Myrcene
     ↓
[current state]
  kitten-myrcene/CHARACTER.yml contains active: 0
```

**Full provenance from user intent → Engine reasoning → world change → current state.**

---

## Part 4: Current Implementation

### 4.1 mooco tools-git Package

The `@moollm/tools-git` package provides basic git operations:

```typescript
// packages/tools-git/src/index.ts
export const gitTools = [
    gitStatus,     // Get repo status
    gitDiff,       // Show changes
    gitLog,        // View history
    gitAdd,        // Stage files
    gitCommit,     // Create commits
    gitBranch,     // Manage branches
    gitCheckout,   // Switch branches/restore files
    repoAdd,       // Add repo to workspace
    repoRemove,    // Remove repo from workspace
    repoList,      // List accessible repos
];
```

Each tool includes:
- **`why` parameter** — Explanation of intent (becomes part of history)
- **Zod validation** — Type-safe inputs
- **Workspace scoping** — Repos must be explicitly added

### 4.2 Cursor's Shell Approach

Cursor handles git via the Shell tool. This works well because:

1. **Full git power** — Any git command, any option
2. **No API to maintain** — git CLI is stable
3. **Familiar to developers** — Same commands they use manually

```bash
# Cursor can run any git command via Shell
git log --oneline -n 10
git diff --staged
git commit -m "$(cat <<'EOF'
Narrative commit message here.
EOF
)"
```

For Cursor, Shell is often sufficient. The MOOCO tools-git package provides:
- **Structured output** — Parsed results, not raw text
- **Workspace safety** — Only access declared repos
- **Why tracking** — Intent captured in tool call history

---

## Part 5: Design Principles

### 5.1 Git-Native by Design

MOOLLM is designed to be git-native:

| Design Choice | Git Benefit |
|---------------|-------------|
| Plain text files | Meaningful diffs |
| YAML for structured data | Human and git readable |
| One file per entity | Changes are localized |
| Append-only logs | Merge-friendly |
| No binary formats | No git-lfs needed |

### 5.2 Commit Message Protocol

The Coherence Engine should write commit messages following this protocol:

```yaml
commit_message:
  first_line: "Story beat title (imperative mood, <50 chars)"
  blank_line: true
  body: |
    Narrative description of what happened and why.
    From whose perspective? What were the motivations?
    What changed emotionally, not just mechanically?
  blank_line: true
  changes:
    - "Bullet points of mechanical changes"
    - "For quick scanning"
```

**Example:**

```
Midnight Prowl: Cats explore the moonlit garden

The Cat Cave family ventured out for their first group expedition.
Terpie led (nominally) while Stroopwafel organized the actual
logistics. The kittens discovered fireflies for the first time.

- Added memory: midnight_prowl to all participating cats
- Updated relationships: pack bonding increased
- Stroopwafel: added "expedition_leader" to roles
- Myrcene: fell asleep in a flower bed (documented in memory)
```

### 5.3 Branch Naming Convention

For narrative branches:

```
main                          # Canon timeline
what-if/biscuit-rejected      # Alternate scenario
experiment/new-character      # Testing new additions
session/2026-01-21            # Session-specific work
backup/before-ceremony        # Safety checkpoint
```

### 5.4 The Interdimensional Transtemporal Ghosts

Every past version of every character still exists in git. They're **ghosts** — past selves that can be summoned:

```bash
# Summon Terpie as he was on January 6th
$ git show abc123:characters/animals/cat-terpie/CHARACTER.yml
```

The Coherence Engine can:
- **Diff** past vs present to understand evolution
- **Branch** from past to explore alternate paths
- **Read** any historical state
- **Trace** exactly how each property evolved

---

## Part 6: Extended Git Tools (Proposed)

### 6.1 Narrative-Aware Operations

Beyond basic git, MOOLLM could benefit from narrative-aware wrappers:

```typescript
// git_history_for_character
// Get the complete narrative history of a character
export const gitCharacterHistory: ToolDefinition = {
    name: 'git_character_history',
    description: 'Get the narrative history of a character',
    inputSchema: withWhy(z.object({
        character: z.string().describe('Character ID or path'),
        since: z.string().optional().describe('Starting point'),
        format: z.enum(['timeline', 'changes', 'commits']).default('timeline'),
    })),
    async execute(input, context) {
        // Returns narrative-formatted history
        // Not just git log, but story beats
    },
};

// git_branch_universe
// Create a "what if" branch with narrative framing
export const gitBranchUniverse: ToolDefinition = {
    name: 'git_branch_universe',
    description: 'Create an alternate timeline for exploration',
    inputSchema: withWhy(z.object({
        name: z.string().describe('Branch name (will be prefixed with what-if/)'),
        premise: z.string().describe('The alternate premise to explore'),
        from: z.string().optional().describe('Starting point (default: HEAD)'),
    })),
    async execute(input, context) {
        // Creates branch and documents the premise
    },
};

// git_merge_timelines
// Merge branches with narrative conflict resolution
export const gitMergeTimelines: ToolDefinition = {
    name: 'git_merge_timelines',
    description: 'Reconcile two timelines into one',
    inputSchema: withWhy(z.object({
        source: z.string().describe('Branch to merge from'),
        strategy: z.enum(['canon', 'alternate', 'reconcile']).default('reconcile'),
        narrative: z.string().optional().describe('How to frame the reconciliation'),
    })),
};
```

### 6.2 Soul Archaeology Tools

```typescript
// git_soul_archaeology
// Deep dive into a character's evolution
export const gitSoulArchaeology: ToolDefinition = {
    name: 'git_soul_archaeology',
    description: 'Analyze the complete evolution of a character',
    inputSchema: withWhy(z.object({
        character: z.string(),
        property: z.string().optional().describe('Specific property to trace'),
    })),
    async execute(input, context) {
        // Returns structured analysis:
        // - Creation date and circumstances
        // - Major evolution points
        // - Relationship changes over time
        // - Memory accumulation
        // - Who wrote each part of their soul
    },
};
```

### 6.3 Introspection Bridge

```typescript
// git_cursor_link
// Find cursor-mirror events for a commit
export const gitCursorLink: ToolDefinition = {
    name: 'git_cursor_link',
    description: 'Find the thinking/reasoning that led to a commit',
    inputSchema: withWhy(z.object({
        commit: z.string().describe('Commit hash'),
    })),
    async execute(input, context) {
        // 1. Get commit timestamp
        // 2. Search cursor-mirror for events around that time
        // 3. Find the git commit tool call
        // 4. Return the thinking blocks that preceded it
    },
};
```

---

## Part 7: Implementation Notes

### 7.1 Cursor Already Does Git Well

For Cursor-based MOOLLM work, the Shell tool is often sufficient:

```bash
# Status
git status --porcelain

# History
git log --oneline -n 20

# Blame
git blame characters/animals/cat-terpie/CHARACTER.yml

# Time travel
git show abc123:characters/animals/cat-terpie/CHARACTER.yml

# Branch
git checkout -b what-if/experiment
```

The main value of dedicated git tools is:
1. **Structured output** for programmatic use
2. **Workspace safety** boundaries
3. **Why tracking** in tool call history
4. **Narrative wrappers** for story-aware operations

### 7.2 mooco tools-git Extension Path

The current `@moollm/tools-git` package can be extended with:

1. **History visualization** — Timeline and graph output
2. **Blame parsing** — Structured blame results
3. **Show parsing** — Extract file content from any commit
4. **Narrative wrappers** — Story-aware operations
5. **Cursor-mirror integration** — Link commits to thinking

### 7.3 The Protocol Symbol

```yaml
GIT-AS-FOUNDATION
```

Invoke when: Discussing why git matters, designing state management, or explaining temporal navigation.

---

## Part 8: The Crawford Connection

Chris Crawford spent 30 years trying to build interactive storytelling by creating a bespoke engine with branching narratives encoded in algorithms.

MOOLLM takes a different approach:
- **The filesystem is the state**
- **Git is the time machine**
- **The Coherence Engine reads and writes plain text files**
- **Branching happens in git, not in application code**

Crawford's approach required artists to learn algorithms. MOOLLM's approach requires them to learn... nothing new. Git is already the universal version control system. YAML is already readable. The infrastructure exists.

> *"Crawford wanted to build a machine for storytelling and failed. MOOLLM built storytelling on top of the most powerful time machine humanity has ever created for text."*

---

## Summary

Git provides MOOLLM with:

| Capability | Git Feature |
|------------|-------------|
| **Time travel** | `git checkout`, `git show` |
| **Parallel universes** | `git branch` |
| **Timeline reconciliation** | `git merge` |
| **Soul archaeology** | `git blame`, `git log` |
| **Narrative provenance** | Commit messages |
| **Collaboration** | Push/pull |
| **Undo** | `git revert` |
| **Pocket dimensions** | `git stash` |

And when combined with cursor-mirror:
- **Full introspection** over both world and mind
- **Commit IDs as synchronization keys** linking the two
- **The ability to trace** any state change back to its reasoning

Git is not a version control system for MOOLLM.

Git is **the multiverse engine** that makes MOOLLM possible.

---

## References

- [mooco/packages/tools-git/](../../mooco/packages/tools-git/) — Current implementation
- [mooco/designs/MOOCO-TOOLS.md](../../mooco/designs/MOOCO-TOOLS.md) — Tool system design
- [skills/plain-text/](../skills/plain-text/) — Why plain text matters
- [skills/cursor-mirror/](../skills/cursor-mirror/) — Orchestrator introspection
- [kernel/](../kernel/) — Core protocols
