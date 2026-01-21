# 🎯📝 Thoughtful Commitment

> *"Commits should tell the story of why, not just what."*

Git commits that capture intent, reasoning, and narrative context by linking to the thinking that produced them.

## A Showcase for Skill Composability

**This skill demonstrates how MOOLLM skills compose like LEGO bricks.**

thoughtful-commitment doesn't reinvent introspection — it *uses* cursor-mirror.
It doesn't reinvent version control — it *uses* git.
It doesn't reinvent data processing — it *uses* shell pipelines.

```
┌─────────────────────────────────────────────────────────────┐
│              thoughtful-commitment                          │
│                   (this skill)                              │
├─────────────────────────────────────────────────────────────┤
│ COMPOSES:                                                   │
│                                                             │
│  cursor-mirror ──→ Raw introspection data                   │
│       │            • Chat history & thinking blocks         │
│       │            • SQLite databases (direct SQL!)         │
│       │            • Plaintext transcripts (greppable)      │
│       │            • Tool call patterns                     │
│       │            • 59 commands, 6 output formats          │
│       ↓                                                     │
│  shell ──────────→ Data transformation                      │
│       │            • grep, awk, sort, uniq, wc              │
│       │            • python3 -c for complex analysis        │
│       │            • Frequency histograms                   │
│       │            • Aggregation & statistics               │
│       ↓                                                     │
│  git ────────────→ Version control substrate                │
│                    • Commit history & diffs                 │
│                    • Blame annotations                      │
│                    • Branch topology                        │
└─────────────────────────────────────────────────────────────┘
```

## The Problem

Most commits look like this:

```
Updated CHARACTER.yml
```

Or at best:

```
fix: bug in auth
```

These tell you **what** changed, but not **why**. When you're debugging six months later, you need the story.

## The Solution

Thoughtful Commitment creates commits like this:

```
Incarnation Ceremony: Kittens receive emoji souls

The Cat Cave family gathered for the Public Incarnation Ceremony.
Each kitten's terpene essence was captured in 5 emojis.
Pronouns were self-chosen. The gong rang thrice.

- Added emoji_identity to all 8 kittens
- Added pronouns (she/her, self-chosen)  
- Added memories: incarnation_ceremony
- Updated Cat Cave README with Emoji Soul Registry

Thinking: cursor-mirror://abc123/events/140-148
```

And it can **link back** to the thinking that produced it:

```bash
$ invoke thoughtful-commitment EXPLAIN --commit abc123

Commit: abc123
Message: Incarnation Ceremony: Kittens receive emoji souls
Timestamp: 2026-01-15T19:30:00Z

User Request:
  "Incarnate the kittens with emoji souls"

Thinking Blocks:
  [Event 141] "I need to invoke INCARNATION protocol..."
  [Event 142] "Myrcene's terpene is sedating, so Active should be 0..."
  [Event 143] "Each emoji should capture a facet of their soul..."

Tool Calls:
  [Event 144] write_file(kitten-myrcene/CHARACTER.yml)
  [Event 145] write_file(kitten-limonene/CHARACTER.yml)
  ...
  [Event 148] git commit
```

## Quick Start

### Create a thoughtful commit

```yaml
invoke:
  skill: thoughtful-commitment
  method: COMMIT
  parameters:
    files: [.]
    story: "Midnight Prowl: Cats explore the moonlit garden"
```

### Explain an existing commit

```yaml
invoke:
  skill: thoughtful-commitment
  method: EXPLAIN
  parameters:
    commit: "abc123"
```

### Generate a narrative message

```yaml
invoke:
  skill: thoughtful-commitment
  method: NARRATIVE
  parameters:
    perspective: narrative
```

## The Mesh: Git + Cursor-Mirror

This skill bridges two introspection systems:

| System | What It Knows |
|--------|---------------|
| **Git** | What changed, when, by whom |
| **Cursor-Mirror** | Why it changed, what the thinking was |

The **commit ID** is the key that links them:

```
┌─────────────────────────────────────┐
│         CURSOR-MIRROR               │
│                                     │
│  [Event 141] Thinking: "..."        │
│  [Event 148] git commit → abc123    │
│              ↓                      │
└──────────────┼──────────────────────┘
               │
               │  commit_id: abc123
               │
┌──────────────┼──────────────────────┐
│              ↓                      │
│  commit abc123                      │
│  "Incarnation Ceremony..."          │
│                                     │
│              GIT                    │
└─────────────────────────────────────┘
```

## Commit Message Protocol

### Structure

```
<title>: <summary> (imperative, <50 chars)

<body>
Narrative description of what happened and why.
From whose perspective? What were the motivations?

<changes>
- Bullet points of mechanical changes
- For quick scanning

<thinking-ref> (optional)
Thinking: cursor-mirror://<composer>/<event-range>
```

### Perspectives

| Perspective | Use For |
|-------------|---------|
| `technical` | Code changes, refactoring, bug fixes |
| `narrative` | MOOLLM adventures, character evolution |
| `changelog` | Release notes, user-facing changes |
| `detailed` | Significant changes, debugging archaeology |

## Methods

| Method | Purpose |
|--------|---------|
| `COMMIT` | Create a thoughtful commit with narrative context |
| `EXPLAIN` | Find the thinking that led to an existing commit |
| `NARRATIVE` | Generate a narrative commit message from context |
| `LINK` | Link a commit to cursor-mirror events |
| `HISTORY` | Get narrative history of a file or directory |
| `DEEP-COMMIT` | Intensive introspection — mine cursor-mirror for patterns |

### Deep Commits

For complex sessions, use `DEEP-COMMIT` to mine technical analytics:

```yaml
invoke:
  skill: thoughtful-commitment
  method: DEEP-COMMIT
  parameters:
    composer: "e8587ace"
    commit_range: "f21d0d0^..085b94b"
```

This will extract and report:
- **Raw metrics** — transcript lines, tool calls, thinking blocks
- **Tool distribution** — frequency histogram of tools used
- **Thinking analysis** — min/max/avg/median character counts
- **Activity bursts** — events per minute with ASCII visualization
- **Commit metrics** — files changed, insertions, deletions
- **Files created/modified** — with line/word/byte counts
- **Top thinking words** — concept frequency analysis
- **Verification commands** — bash one-liners to reproduce every metric

Output is a markdown appendix suitable for PR descriptions.

## Why This Matters

### For Debugging

Six months from now:
- `git log` tells you Terpie's `active` became `0`
- `EXPLAIN` tells you it was because "Myrcene's terpene is sedating"

### For Collaboration

When reviewing a PR:
- The diff shows the changes
- The commit message tells the story
- The thinking link shows the reasoning

### For Soul Archaeology

Tracing a character's evolution:
- `git blame` shows who changed each line
- `HISTORY` shows the narrative journey
- Each commit captures a moment of intent

## Git Time Travel

thoughtful-commitment knows how to peel layers off files and trace intent through history:

### Archaeology Commands

```bash
# BLAME — Who wrote each line, when, and why?
git blame <file>                      # Line-by-line attribution
git blame -L 10,20 <file>             # Specific range
git blame <commit>^ -- <file>         # Blame BEFORE a commit

# LOG ARCHAEOLOGY — Trace evolution
git log --oneline <file>              # Commits touching file
git log -p <file>                     # With patches
git log -S 'pattern'                  # Pickaxe: who added this string?
git log -G 'regex'                    # Where did regex match change?
git log --follow <file>               # Track through renames

# SHOW — Inspect any point in time
git show <commit>:<file>              # File at that moment
git show <commit> --stat              # What changed
```

### Planning Operations

```bash
# MERGE PLANNING — Understand before merging
git log main..feature --oneline       # Commits to merge
git diff main...feature               # Changes to merge
git merge-base main feature           # Common ancestor

# CHERRY-PICK PLANNING — Surgical extraction
git cherry -v upstream branch         # What's not upstream?
git show <commit>                     # Inspect before picking

# PR ARCHAEOLOGY — Trace through PRs
gh pr view <num>                      # PR details and discussion
gh pr diff <num>                      # What the PR changed
git log --merges --grep='#123'        # Find merge commit
```

### Methods for Time Travel

| Method | Purpose |
|--------|---------|
| `BLAME` | Peel layers off a file — who, when, why for each line |
| `ARCHAEOLOGY` | Deep dig into file/pattern history |
| `PLAN-MERGE` | Understand what a merge brings before merging |
| `PLAN-CHERRY-PICK` | Plan surgical commit extraction |
| `HISTORY` | Narrative timeline of a path |

## What cursor-mirror Can Access

thoughtful-commitment leverages cursor-mirror's full introspection capabilities:

| Data Source | What You Can Search | Commands |
|-------------|---------------------|----------|
| **Chat History** | All messages, user/assistant turns | `timeline`, `tail`, `transcript` |
| **Thinking Blocks** | LLM reasoning (the "why") | `thinking` |
| **Tool Calls** | Every action taken, with args | `tools`, `tool-result` |
| **SQLite Databases** | Raw data, custom queries | `sql --db <ref> "SELECT..."` |
| **Plaintext Transcripts** | Full conversations, greppable | `agent-transcript`, `tgrep` |
| **Context Assembly** | What files/code were gathered | `context-sources`, `searches` |
| **MCP Servers** | External tool usage | `mcp`, `mcp-tools` |

### Example: Mining a Session

```bash
# Find the session
cursor-mirror tree                          # Navigate workspaces
cursor-mirror tail --limit 20               # Recent activity

# Extract data
cursor-mirror timeline e8587ace             # Full event stream
cursor-mirror thinking e8587ace             # Reasoning blocks
cursor-mirror tools e8587ace                # Tool call patterns

# Search transcripts
cursor-mirror tgrep "thoughtful"            # Find pattern
cursor-mirror agent-transcript e8587ace     # Raw plaintext

# Direct SQL
cursor-mirror sql --db moollm "SELECT COUNT(*) FROM bubbles"

# Process with shell
cursor-mirror tools e8587ace | grep Shell | wc -l
```

## Related Skills

- [cursor-mirror](../cursor-mirror/) — The reflection engine (59 commands!)
- [session-log](../session-log/) — Where narrative lives
- [plain-text](../plain-text/) — Why text matters

## The Name

**Thoughtful Commitment** — because:
- Commits should be **thoughtful** (considered, intentional)
- They represent **commitment** (to the change, to the narrative)
- And they capture **thoughts** (the reasoning that produced them)
