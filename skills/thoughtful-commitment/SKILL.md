---
name: thoughtful-commitment
description: "Git commits that capture intent, reasoning, and narrative context"
license: MIT
tier: 2
allowed-tools: [read_file, write_file, list_dir, run_terminal_cmd, grep]
protocol: THOUGHTFUL-COMMITMENT
related: [cursor-mirror, session-log, plain-text, yaml-jazz, git-workflow]
tags: [git, commits, narrative, provenance, introspection]
---

# Thoughtful Commitment

> *"Commits should tell the story of why, not just what."*

## Purpose

Transform mechanical commits into narrative records that capture full context:
- What the user asked
- What the LLM was thinking
- Why the changes matter
- Links to cursor-mirror thinking blocks

## The Core Insight

Git and cursor-mirror are **two introspection systems** that mesh via commit IDs:

```
Git:           "What changed?"  →  abc123
Cursor-Mirror: "Why?"          →  events 140-148

Thoughtful Commitment: Links them together
```

## Protocol: THOUGHTFUL-COMMITMENT

### Commit Message Format

```
<type>: <summary> (imperative, <50 chars)

<narrative>
What happened, from whose perspective, and why it matters.
Focus on intent and motivation, not just mechanics.

<changes>
- Bullet list of mechanical changes
- For quick scanning

<thinking-ref>
Thinking: cursor-mirror://<composer>/<event-range>
```

### Types

| Type | Use |
|------|-----|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `refactor` | Code restructuring (no behavior change) |
| `docs` | Documentation only |
| `style` | Formatting (no code change) |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks |
| *narrative* | Story beat, character change, world evolution |

For MOOLLM narratives, the type can be the story beat:

```
Incarnation Ceremony: Kittens receive emoji souls
Midnight Prowl: Cats explore the moonlit garden
Cat Council: Biscuit accepted into family
```

## Method Specifications

### COMMIT

Create a thoughtful commit with narrative context.

**Input:**
```yaml
method: COMMIT
parameters:
  files: [string]          # Files to commit (or '.' for all)
  story: string            # Narrative of what happened
  include_thinking: bool   # Link to cursor-mirror (default: true)
  perspective: enum        # technical | narrative | changelog | detailed
```

**Process:**
1. Stage specified files (`git add`)
2. Gather context from conversation
3. If `include_thinking`, query cursor-mirror for recent events
4. Generate commit message per protocol
5. Create commit (`git commit -m "..."`)
6. Return commit ID and message

**Output:**
```yaml
commit_id: "abc123"
message: "Full commit message..."
thinking_link: "cursor-mirror://def456/events/140-148"
```

### EXPLAIN

Find the thinking that led to an existing commit.

**Input:**
```yaml
method: EXPLAIN
parameters:
  commit: string           # Commit hash (full or abbreviated)
```

**Process:**
1. Get commit details (`git show --format=...`)
2. Extract timestamp
3. Search cursor-mirror for events around that time
4. Find the git commit tool call
5. Trace back to thinking blocks and user request

**Output:**
```yaml
commit_message: "Incarnation Ceremony: ..."
timestamp: "2026-01-15T19:30:00Z"
author: "Coherence Engine"
user_request: "Incarnate the kittens with emoji souls"
thinking_blocks:
  - event_id: 141
    content: "I need to invoke INCARNATION protocol..."
  - event_id: 142
    content: "Myrcene's terpene is sedating..."
tool_calls:
  - event_id: 144
    tool: write_file
    args: {path: "kitten-myrcene/CHARACTER.yml"}
  - event_id: 148
    tool: git_commit
    args: {message: "..."}
```

### NARRATIVE

Generate a narrative commit message from current context.

**Input:**
```yaml
method: NARRATIVE
parameters:
  diff_summary: string?    # Optional (auto-detect from staged)
  perspective: enum        # technical | narrative | changelog | detailed
```

**Process:**
1. If no diff_summary, run `git diff --staged --stat`
2. Analyze conversation context for intent
3. Generate message per perspective and protocol

**Output:**
```yaml
message: "Full commit message..."
sections:
  title: "Incarnation Ceremony: Kittens receive emoji souls"
  body: "The Cat Cave family gathered..."
  changes: ["Added emoji_identity...", "Added pronouns..."]
```

### LINK

Manually link a commit to cursor-mirror events.

**Input:**
```yaml
method: LINK
parameters:
  commit: string           # Commit hash
  events: [string]         # Event IDs from cursor-mirror
```

**Process:**
1. Validate commit exists
2. Validate events exist in cursor-mirror
3. Store link in `.moollm/skills/thoughtful-commitment/commit-links.yml`

**Output:**
```yaml
linked: true
reference: "cursor-mirror://abc123/events/140-148"
```

### HISTORY

Get narrative history of a file or directory.

**Input:**
```yaml
method: HISTORY
parameters:
  path: string             # File or directory
  depth: int               # Number of commits (default: 10)
  include_thinking: bool   # Include cursor-mirror links (default: true)
```

**Process:**
1. Get git log for path (`git log -n <depth> --format=... -- <path>`)
2. For each commit, attempt to find cursor-mirror link
3. Build narrative timeline

**Output:**
```yaml
timeline:
  - commit: "abc123"
    date: "2026-01-15"
    message: "Incarnation Ceremony: ..."
    thinking_link: "cursor-mirror://..."
    summary: "Kittens received emoji souls"
  - commit: "def456"
    date: "2026-01-14"
    message: "Initial character creation"
    thinking_link: null
    summary: "Created basic character files"
```

### DEEP-COMMIT

Technical analytics mining — extract quantitative metrics from cursor-mirror and git.

**When to use:**
- PR descriptions needing detailed appendices
- Post-mortem analysis of development sessions
- Documenting complex multi-hour sessions
- Generating reproducible verification commands

**Process:**

~~~bash
# 1. Raw metrics extraction
TRANSCRIPT="path/to/transcript.txt"
wc -l "$TRANSCRIPT"                           # line count
wc -c "$TRANSCRIPT"                           # byte count
grep -c "^\[Tool call\]" "$TRANSCRIPT"        # tool calls
grep -c "^\[Thinking\]" "$TRANSCRIPT"         # thinking blocks
grep -c "^user:" "$TRANSCRIPT"                # user turns

# 2. Tool distribution
grep "^\[Tool call\]" "$TRANSCRIPT" | cut -d' ' -f3 | sort | uniq -c | sort -rn

# 3. Thinking block analysis
grep "^\[Thinking\]" "$TRANSCRIPT" | while read l; do echo ${#l}; done | \
  sort -n | awk 'BEGIN{sum=0} {a[NR]=$1; sum+=$1} END{
    printf "Count: %d\nMin: %d\nMax: %d\nAvg: %.0f\nMedian: %d\n", 
           NR, a[1], a[NR], sum/NR, a[int(NR/2)]
  }'

# 4. Activity bursts
cursor-mirror timeline <composer> 2>&1 | \
  grep -E "^[0-9]{4}-" | cut -d: -f1-2 | uniq -c

# 5. Git commit metrics
git log --oneline <range>
git diff --numstat <range> | awk '{ins+=$1; del+=$2} END{print ins, del}'

# 6. Word frequency in thinking
grep "^\[Thinking\]" "$TRANSCRIPT" | tr '[:upper:]' '[:lower:]' | \
  tr -cs '[:alpha:]' '\n' | sort | uniq -c | sort -rn | head -20
~~~

**Input:**
~~~yaml
method: DEEP-COMMIT
parameters:
  composer: string       # Composer ID (@1, name fragment, hash)
  commit_range: string   # Git range (e.g., "f21d0d0^..085b94b")
~~~

**Output:**
~~~markdown
## Appendix: Technical Analytics — Session <composer>

### Raw Metrics
Transcript: 8,890 lines | 390.7 KB
Tool Calls: 85 total
Thinking:   74 blocks | 11.1 KB

### Tool Distribution
36x Shell
23x Read
11x StrReplace
...

### Activity Bursts (events/minute)
16:46  16 events  ████████████████
20:08  10 events  ██████████
20:22  12 events  ████████████

### Commit Metrics
| Commit | Files | +Lines | -Lines |
|--------|-------|--------|--------|
| f21d0d0 | 7 | 1,515 | 0 |
...

### Verification Commands
~~~bash
# Reproduce these metrics:
wc -l "$TRANSCRIPT"
grep -c "^\[Tool call\]" "$TRANSCRIPT"
...
~~~
~~~

**Example session e8587ace produced:**
- 8,890 transcript lines
- 85 tool calls (36 Shell, 23 Read, 11 StrReplace)
- 75 thinking blocks (avg 151 chars)
- 3 commits (+1,656 net lines)
- 4 files created (1,526 lines total)
- Activity burst at 20:22 (12 events/min during meta-commit)

## Implementation Notes

### Finding Cursor-Mirror Events for a Commit

```bash
# 1. Get commit timestamp
git show -s --format=%ci abc123
# 2026-01-15 19:30:00 -0800

# 2. Search cursor-mirror for events around that time
python3 cursor_mirror.py timeline <composer> --around "2026-01-15T19:30:00"

# 3. Find the git commit event
python3 cursor_mirror.py grep "git commit" --after "2026-01-15T19:00:00"

# 4. Trace back to preceding thinking blocks
python3 cursor_mirror.py thinking <composer> --before <commit-event-id>
```

### Storage of Links

Links are stored in `.moollm/skills/thoughtful-commitment/commit-links.yml`:

```yaml
# .moollm/skills/thoughtful-commitment/commit-links.yml
links:
  abc123:
    composer: def456
    events: [140, 141, 142, 143, 144, 145, 146, 147, 148]
    user_request: "Incarnate the kittens with emoji souls"
    timestamp: "2026-01-15T19:30:00Z"
    
  ghi789:
    composer: def456
    events: [200, 201, 202]
    user_request: "Fix the relationship field"
    timestamp: "2026-01-15T20:15:00Z"
```

### Cursor Shell Integration

In Cursor, the skill can be invoked via natural language:

```
User: "Commit these changes with a narrative message"

LLM: [Invokes COMMIT method, generates message, creates commit]

Output: Created commit abc123
  Incarnation Ceremony: Kittens receive emoji souls
  
  Linked to thinking: cursor-mirror://def456/events/140-148
```

Or explain an existing commit:

```
User: "Why did we set Myrcene's active to 0?"

LLM: [Invokes EXPLAIN, traces back through history]

Output: Found in commit abc123 (2026-01-15)
  
  Your request: "Incarnate the kittens with emoji souls"
  
  My reasoning: "Myrcene's terpene is sedating, so Active 
  should be 0. She's the Princess of Pillows — low energy
  is her whole identity."
```

## Dovetails With

### Sister Skills

| Skill | Relationship |
|-------|--------------|
| [cursor-mirror](../cursor-mirror/) | Source of thinking blocks |
| [session-log](../session-log/) | Logs can reference commits |
| [plain-text](../plain-text/) | Why text commits matter |
| [git-workflow](../git-workflow/) | Broader git patterns (planned) |

### Kernel Protocols

- `WHY-REQUIRED` — Tool calls explain themselves; commits should too
- `APPEND-ONLY` — Commit history is append-only by nature

## The Philosophy

> Every commit is a **crystallized moment** of intent.
> 
> Git remembers **what** changed.
> Cursor-mirror remembers **why** you thought it should.
> Thoughtful Commitment **links them together**.
>
> Six months from now, you can trace any property back to:
> - The user request that triggered it
> - The reasoning that shaped it
> - The commit that recorded it
>
> That's **soul archaeology** powered by version control.
