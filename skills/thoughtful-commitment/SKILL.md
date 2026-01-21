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

---

## Reference: Detail Knob

Adjustable output from terse to comprehensive:

| Level | Name | Tokens | Output |
|-------|------|--------|--------|
| 1 | terse | ~10 | `fix: auth bug` |
| 2 | brief | ~50 | Title + paragraph |
| 3 | standard | ~100 | Title + narrative + changes |
| 4 | detailed | ~300 | Full sections + session link |
| 5 | comprehensive | ~500+ | Everything + alternatives + metrics |

**Focus areas:** `technical`, `narrative`, `process`, `provenance`, `changelog`, `metrics`

---

## Reference: Emoji Palette

### Attribution
| Emoji | Meaning |
|-------|---------|
| 👤 | Human-written (place at top) |
| 🤖 | LLM-generated |
| 👤🤖 | Collaboration |
| 👁️ | Human-reviewed |

### Skill Signature
`🤔💭` — Thoughtful Commitment namespace anchor

### Section Markers
| Emoji | Section |
|-------|---------|
| 📍 | Context |
| 🧠 | Thinking |
| 🔍 | Investigation |
| 💡 | Solution |
| 🔀 | Alternatives |
| 📝 | Changes |
| 📊 | Metrics |
| 🔗 | Session link |

### Output Structure
```
👤 User's prompt (head position, their words)
---
🤖🤔💭 LLM analysis (skill's voice)
```

---

## Reference: Git Time Travel

### Archaeology Commands

```bash
# BLAME — Who wrote each line?
git blame <file>
git blame -L 10,20 <file>           # Specific range
git blame <commit>^ -- <file>       # Blame BEFORE a commit

# LOG — Trace evolution
git log --oneline <file>
git log -S 'pattern'                # Pickaxe: who added this?
git log --follow <file>             # Track through renames

# SHOW — Inspect any point
git show <commit>:<file>            # File at that moment
git show <commit> --stat            # What changed
```

### Planning Commands

```bash
# MERGE PLANNING
git log main..feature --oneline     # Commits to merge
git diff main...feature             # Changes to merge
git merge-base main feature         # Common ancestor

# CHERRY-PICK PLANNING
git cherry -v upstream branch       # What's not upstream?
git show <commit>                   # Inspect before picking
```

---

## Reference: Cursor-Mirror Integration

cursor-mirror provides 59 commands for introspection:

```bash
# Navigation
cursor-mirror tree                  # Browse workspaces
cursor-mirror tail --limit 20       # Recent activity

# Extraction
cursor-mirror timeline <composer>   # Full event stream
cursor-mirror thinking <composer>   # Reasoning blocks
cursor-mirror tools <composer>      # Tool call history

# Search
cursor-mirror tgrep 'pattern'       # Search transcripts
cursor-mirror sql --db <ref> 'query' # Direct SQL

# Analysis
cursor-mirror analyze <composer>    # Session statistics
```

---

## Reference: Shell Patterns

```bash
# Counting
wc -l file                          # Lines
grep -c 'pattern' file              # Matches

# Frequency
sort | uniq -c | sort -rn           # Histogram

# Extraction
grep -o 'pattern' file              # Matches only
awk '{print $1, $3}'                # Select columns

# Aggregation
awk '{sum+=$1} END{print sum}'      # Sum
```

---

## Reference: Trekify Integration

For privacy, compose with [trekify](../trekify/) to mask sensitive data:

```bash
trekify MASK-SESSION e8587ace -o masked.txt
```

| Sensitive | Trekified |
|-----------|-----------|
| API keys | Quantum entanglement tokens |
| Servers | Starbase {N} |
| Databases | Memory Core Alpha |

---

# Philosophy (The Rear End 🐕)

Where dogs sniff. The deep stuff.

## The Persistence Insight

> *"All those moments will be lost in time, like tears in rain."*
> — **Roy Batty**, Patron Saint of Thoughtful Commitment

**Git commits PERSIST ephemeral IDE state into permanent history.**

When you're working in Cursor, your session holds:
- **Thinking blocks** — the LLM's reasoning
- **Context assembly** — what files were gathered
- **Tool calls** — every action taken
- **Design process** — iterations, dead ends

**All of this vanishes** when you close the IDE.

Git commit FREEZES the NOW into FOREVER:
- Permanent record in repository
- Shareable with team
- Traceable through blame/log
- Survives years

## Full Disclosure

Every commit can disclose the complete development session:

| Level | What's Disclosed |
|-------|------------------|
| Minimal | Just the diff |
| Narrative | Intent summarized |
| Linked | `cursor-mirror://e8587ace` |
| Full | Complete transcript archived |

**Benefits:**
- Future self: Remember why you made decisions
- Team: Onboard with full history
- Auditing: Demonstrate AI assistance
- Debugging: See context that led to bugs

## Composition Philosophy

### Why Sister Scripts?

`cursor_mirror.py` is a "sister script" — standalone, invoked via shell, outputting text.

**NOT a library. NOT an import. A PROCESS you talk to via stdin/stdout.**

This matters because:
- The LLM invokes it the same way a human would
- Output is inspectable, greppable, pipeable
- No hidden state, no tight coupling
- The skill doesn't "own" cursor-mirror; it USES it

Sister scripts are tools in your belt, not organs in your body.

### Why Shell as Glue?

Shell pipelines are the universal connector:
```
cursor-mirror (Python) → grep (C) → awk (C) → git (C)
```

The LLM thinks in shell because:
- Lingua franca of Unix tools
- Pipes are dataflow made visible
- Each stage independently testable
- You can see the data at every step

**Shell isn't primitive — it's COMPOSABLE.**

### Why Not Monolith?

A monolithic tool would:
- Hide the data flow
- Couple components tightly
- Be hard to debug
- Not compose with other skills

By composing cursor-mirror + shell + git:
- Transparent data flow
- Loose coupling
- Reuse across skills
- Debuggable (run each stage manually)

### The Pattern

```
skill = ORCHESTRATION     (knows WHAT to do)
sister_scripts = CAPABILITY   (knows HOW)
shell = GLUE              (connects them)
```

The skill is the conductor. The tools are the orchestra.
