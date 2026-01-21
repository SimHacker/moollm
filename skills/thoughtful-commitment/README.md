# 🎯📝 Thoughtful Commitment

> *"Commits should tell the story of why, not just what."*

Git commits that capture intent, reasoning, and narrative context by linking to the thinking that produced them.

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

## Related Skills

- [cursor-mirror](../cursor-mirror/) — Source of thinking blocks
- [session-log](../session-log/) — Where narrative lives
- [plain-text](../plain-text/) — Why text matters

## The Name

**Thoughtful Commitment** — because:
- Commits should be **thoughtful** (considered, intentional)
- They represent **commitment** (to the change, to the narrative)
- And they capture **thoughts** (the reasoning that produced them)
