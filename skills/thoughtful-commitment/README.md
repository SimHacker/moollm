# Thoughtful Commitment

**Git commits that link to the thinking that produced them.**

When you work with an AI coding assistant, the session holds valuable context: what you asked, what the AI considered, what alternatives were rejected, why it made certain choices. When you close the IDE, all of that vanishes. Your commit says "fix: auth bug" but six months later you have no idea *why*.

This skill captures that ephemeral reasoning and freezes it into permanent git history.

## How MOOLLM Skills Work

MOOLLM is a protocol for structuring LLM capabilities as composable "skills." Each skill has:

- **[CARD.yml](CARD.yml)** — The interface. What methods exist, what parameters they take, what they return. Designed to be "sniffable" by an LLM in ~50 lines.
- **[SKILL.md](SKILL.md)** — The protocol. Full implementation details, philosophy, examples. Read when you need depth.
- **README.md** — You're reading it. Landing page and quick start.

Skills compose. This one doesn't reinvent introspection — it uses [cursor-mirror](../cursor-mirror/). It doesn't reinvent version control — it uses git. It doesn't reinvent data processing — it uses shell pipelines.

```
thoughtful-commitment
        │
        ├── cursor-mirror ──→ SQLite databases, plaintext transcripts
        │                     thinking blocks, tool calls, 59 commands
        │
        ├── git ─────────────→ blame, log, diff, show, commit history
        │
        └── shell ───────────→ grep, awk, sort, uniq, python -c
```

## The Insight

Cursor stores everything in SQLite databases and plaintext transcripts:

```
~/.cursor/projects/*/agent-transcripts/*.txt    # Full conversations
~/Library/Application Support/Cursor/User/workspaceStorage/*/state.vscdb
```

The `cursor-mirror` skill can query these directly:

```bash
cursor-mirror thinking e8587ace    # Extract reasoning blocks
cursor-mirror tools e8587ace       # Every tool call with arguments
cursor-mirror sql --db e8587ace "SELECT * FROM bubbles WHERE text LIKE '%password%'"
```

This skill synthesizes that into commit messages:

```
Incarnation Ceremony: Kittens receive emoji souls

The Cat Cave family gathered for the ceremony. Each kitten's
terpene essence was captured in 5 emojis. Pronouns self-chosen.

- Added emoji_identity to 8 kittens
- Added pronouns (she/her, self-chosen)
- Updated Cat Cave README

Session: cursor-mirror://e8587ace
Events: 140-148
```

Later, you can trace back:

```bash
invoke thoughtful-commitment EXPLAIN --commit abc123

# Returns:
# User Request: "Incarnate the kittens with emoji souls"
# Thinking: [Event 141] "I need to invoke INCARNATION protocol..."
#           [Event 142] "Myrcene's terpene is sedating, so Active=0..."
# Tool Calls: [Event 144] write_file(kitten-myrcene/CHARACTER.yml)
```

## The Bridge

The commit ID links two systems:

| System | What It Knows |
|--------|---------------|
| **Git** | What changed, when, by whom |
| **Cursor-Mirror** | Why it changed, what the thinking was |

```
CURSOR (ephemeral)                    GIT (permanent)
━━━━━━━━━━━━━━━━━━                    ━━━━━━━━━━━━━━━━
thinking blocks ────┐
context assembly ───┼──→ commit msg ──→ FOREVER
attention focus ────┤         ↓
design process ─────┤    blame/log
tool calls ─────────┘         ↓
                         years later:
(vanishes on close)      git blame → commit → thinking
```

> *"All those moments will be lost in time, like tears in rain."*
> — **Roy Batty**, Patron Saint of Thoughtful Commitment

## Methods

| Method | Purpose |
|--------|---------|
| `COMMIT` | Create commit with narrative context |
| `EXPLAIN` | Find thinking that led to existing commit |
| `BLAME` | Who wrote each line, when, why |
| `ARCHAEOLOGY` | Deep dig into file/pattern history |
| `DEEP-COMMIT` | Mine session for technical analytics |

See [CARD.yml](CARD.yml) for full method signatures.

## Deep Commits

For complex sessions, `DEEP-COMMIT` extracts quantitative data:

```yaml
invoke:
  skill: thoughtful-commitment
  method: DEEP-COMMIT
  parameters:
    composer: "e8587ace"
    commit_range: "f21d0d0^..085b94b"
```

Output includes:
- Raw metrics: transcript lines, tool calls, thinking blocks
- Tool distribution histogram
- Thinking analysis: min/max/avg/median character counts  
- Activity bursts: events per minute
- Verification commands: bash one-liners to reproduce every metric

## Detail Knob

Adjustable output from terse to comprehensive:

| Level | Output | Tokens |
|-------|--------|--------|
| 1 | `fix: auth bug` | ~10 |
| 2 | Title + paragraph | ~50 |
| 3 | Title + narrative + changes | ~100 |
| 4 | Full narrative + session link | ~300 |
| 5 | Everything + alternatives + metrics | ~500+ |

Focus areas: `technical`, `narrative`, `process`, `provenance`, `changelog`, `metrics`

## Full Disclosure

Every commit can disclose the complete development session:

| Level | What's Disclosed |
|-------|------------------|
| Minimal | Just the diff |
| Narrative | Intent summarized |
| Linked | `cursor-mirror://e8587ace` |
| Full | Complete transcript archived |

This enables:
- **Auditing**: Demonstrate AI assistance with human oversight
- **Debugging**: See context that led to bugs
- **Learning**: Study how problems were approached
- **Onboarding**: Full history, not just final code

## Privacy: TREKIFY

The [trekify](../trekify/) skill masks sensitive data with Star Trek technobabble:

```
# Before
Connected to prod-db-west-2.company.internal:5432

# After  
Established uplink to Memory Core Alpha, Starbase 47
```

| Sensitive | Trekified |
|-----------|-----------|
| API keys | Quantum entanglement tokens |
| Servers | Starbase {N} |
| Databases | Memory Core Alpha |
| AWS/GCP | Utopia Planitia Fleet Yards |

## Git Time Travel

The skill knows how to peel layers off files:

```bash
# Who wrote each line?
git blame <file>
git blame <commit>^ -- <file>    # Blame BEFORE a commit

# Trace evolution
git log -S 'pattern'              # Pickaxe: who added this string?
git log --follow <file>           # Track through renames

# Plan operations
git log main..feature --oneline   # What would merge bring?
git cherry -v upstream branch     # What's not upstream?
```

## Source

- **Interface**: [CARD.yml](CARD.yml) — method signatures, parameters, returns
- **Protocol**: [SKILL.md](SKILL.md) — full implementation, philosophy, examples
- **Dependencies**: [cursor-mirror](../cursor-mirror/), [trekify](../trekify/)

## The Name

**Thoughtful Commitment** — commits should be thoughtful (considered), represent commitment (to the change), and capture thoughts (the reasoning that produced them).

---

*Part of [MOOLLM](https://github.com/SimHacker/moollm) — skills for LLM-native development.*
