# Cursor Mirror Bundle

> *Watch yourself think.*

**cursor-mirror** is a deep introspection tool for Cursor IDE. It lets you:

- **Review past conversations** — Search, export, and analyze your chat history
- **Watch yourself think** — See the LLM's reasoning blocks and tool calls
- **Trace context assembly** — Understand what files and code went into each response
- **Debug agent behavior** — Analyze tool usage patterns and performance
- **Export transcripts** — Create documentation from your development sessions

## Quick Start

```bash
# Check your Cursor status
python3 skills/cursor-mirror/scripts/cursor_mirror.py status

# List all workspaces
python3 skills/cursor-mirror/scripts/cursor_mirror.py list-workspaces

# See recent conversations
python3 skills/cursor-mirror/scripts/cursor_mirror.py tail --limit 20

# Browse hierarchically
python3 skills/cursor-mirror/scripts/cursor_mirror.py tree

# Watch yourself think
python3 skills/cursor-mirror/scripts/cursor_mirror.py thinking @1

# Export a conversation
python3 skills/cursor-mirror/scripts/cursor_mirror.py export-markdown @1 > my-session.md
```

## Requirements

- **Python 3.8+**
- **Cursor IDE** (macOS, Linux, or Windows)
- No additional dependencies — uses only Python standard library

## What's in This Bundle

| Skill | Priority | Purpose |
|-------|----------|---------|
| **cursor-mirror** | Core | The main introspection tool (59 commands, ~9800 lines) |
| **skill-snitch** | Required | Security auditing for skills and transcripts |
| **thoughtful-commitment** | Recommended | Git commits that capture reasoning context |
| **trekify** | Optional | Privacy masking before sharing transcripts |
| **session-log** | Supporting | Structured logging patterns |
| **sister-script** | Methodology | Document-first automation (explains cursor_mirror.py design) |
| **sniffable-python** | Methodology | Why cursor_mirror.py is structured for LLM comprehension |
| **play-learn-lift** | Methodology | The exploration→learning→sharing cycle |
| **k-lines** | Protocol | K-REF pointer format used by cursor-mirror |

## Part of a Larger Ecosystem

This bundle is extracted from **MOOLLM** — a skill framework that builds on and extends the [Anthropic skill standard](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching). 

### What Works Standalone

- **cursor_mirror.py** — Full functionality, all 59 commands
- **Security scanning** — skill-snitch's static analysis
- **Export & documentation** — Transcripts, timelines, thinking blocks
- **Git integration** — thoughtful-commitment's commit workflows

### What's Degraded Without Full MOOLLM

| Feature | Status | What's Missing |
|---------|--------|----------------|
| K-line activation | Degraded | Protocol symbols won't auto-activate related context |
| Hot/cold memory | Unavailable | Advisory memory management requires kernel |
| Session bootstrapping | Degraded | No automatic context warmup |
| Room-based navigation | Unavailable | Adventure game skills not included |
| Speed-of-light simulation | Unavailable | Multi-turn ensemble patterns |

### What Full MOOLLM Adds

MOOLLM extends the Anthropic skill model with:

1. **Instantiation** — Skills as prototypes that create instances
2. **Three-tier persistence** — Platform → Narrative → State
3. **K-lines** — Names that activate knowledge constellations (Minsky)
4. **Empathic templates** — Smart generation, not string substitution
5. **Speed of light** — Many agents, many turns, one LLM call
6. **CARD.yml** — Machine-readable interfaces with advertisements
7. **Ethical framing** — Room-based inheritance of performance context

## Skill Dependency Graph

```
cursor-mirror (core)
├── skill-snitch (required)
│   └── uses: cursor-mirror deep-snitch
├── thoughtful-commitment (recommended)
│   ├── composes: cursor-mirror (introspection)
│   ├── composes: git (version control)
│   └── composes: trekify (privacy)
├── trekify (optional)
│   └── composes: cursor-mirror (probing)
└── methodology skills (context)
    ├── sister-script (explains the pattern)
    ├── sniffable-python (code structure)
    ├── play-learn-lift (development cycle)
    └── k-lines (protocol reference)
```

## Key Commands

### Navigation
```bash
cursor-mirror tree                    # Browse all workspaces
cursor-mirror tree w3                 # Composers in workspace 3
cursor-mirror tree w3.c2              # Details of a specific chat
cursor-mirror find "search term"      # Find conversations
```

### Introspection
```bash
cursor-mirror thinking @1             # See reasoning blocks
cursor-mirror tools @1                # Tool call history
cursor-mirror timeline @1             # Chronological events
cursor-mirror context-sources @1      # What context was assembled
```

### Export
```bash
cursor-mirror export-markdown @1      # Readable transcript
cursor-mirror export-jsonl @1         # Training data format
cursor-mirror image-gallery           # Find cached images
```

### Database Access
```bash
cursor-mirror dbs                     # List all databases
cursor-mirror sql --db global "SELECT ..."  # Direct SQL
cursor-mirror keys --pattern "bubble*"      # Search keys
```

### Status
```bash
cursor-mirror status                  # Overall dashboard
cursor-mirror status-config           # Server limits
cursor-mirror status-mcp              # MCP servers
cursor-mirror dotcursor-status        # ~/.cursor directory
```

## File Locations

cursor-mirror reads from Cursor's local data stores:

| Platform | Application Support |
|----------|---------------------|
| macOS | `~/Library/Application Support/Cursor/` |
| Linux | `~/.config/Cursor/` |
| Windows | `%APPDATA%\Cursor\` |

Plus `~/.cursor/` for plaintext transcripts and AI tracking.

## Security Notes

- **Read-only** — cursor-mirror never writes to Cursor's data stores
- **Local only** — All data stays on your machine
- **Use trekify** — Mask sensitive data before sharing transcripts publicly

## Try Full MOOLLM

If you find cursor-mirror useful, consider exploring the full MOOLLM ecosystem:

```bash
git clone https://github.com/SimHacker/moollm.git
cd moollm
# Read kernel/README.md for architecture
# Read skills/INDEX.yml for skill catalog
```

MOOLLM includes 60+ skills for:
- **Text adventures** — Room-based exploration with narrative evidence
- **Character simulation** — Sims-style needs, personalities, relationships
- **Decision-making** — Adversarial committees, rubrics, evaluators
- **Development tools** — Debugging, code review, refactoring patterns

The **skill skill** teaches you how to create your own skills using the **play-learn-lift** methodology: explore freely, document patterns, share as reusable capabilities.

## Credits

- **cursor-mirror** — Don Hopkins, Leela AI
- **MOOLLM** — Don Hopkins, Leela AI
- **Inspiration** — Seymour Papert (*Mindstorms*), Marvin Minsky (*Society of Mind*)

## License

MIT License — Use freely, credit required.

---

*"You can't think about thinking without thinking about thinking about something."*
— Seymour Papert
