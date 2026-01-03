# Data Flow

> *"Rooms are nodes. Exits are edges. Thrown objects are messages."*

---

## What Is It?

**Data Flow** is MOOLLM's approach to building processing pipelines using rooms and objects:

- **Rooms** are processing stages
- **Exits** connect stages (edges in the graph)
- **Objects** flow through as messages
- **THROW** sends objects through exits
- **INBOX** receives incoming objects
- **OUTBOX** stages outgoing objects

This is how MOOLLM does **Kilroy-style** data flow programming — the filesystem IS the network.

---

## The Pattern

```
source/ ─────► parser/ ─────► analyzer/ ─────► output/
   │              │               │
   │              ▼               │
   │          validator/          │
   │              │               │
   │              ▼               │
   └─────────► errors/ ◄──────────┘
```

Each room:
- Has an `inbox/` for incoming work
- Has an `outbox/` for staging results
- Processes items and throws them to the next stage
- Routes errors to an error handler

---

## Commands

| Command | Effect |
|---------|--------|
| `THROW obj exit` | Send object through exit to destination |
| `INBOX` | List items waiting to be processed |
| `NEXT` | Get next item from inbox (FIFO) |
| `PEEK` | Look at next item without removing |
| `STAGE obj exit` | Add object to outbox for later throw |
| `FLUSH` | Throw all staged objects |
| `FLUSH exit` | Throw staged objects for specific exit |

---

## Example: Document Pipeline

```
uploads/              # Raw files land here
├── ROOM.yml
├── inbox/
│   ├── doc-001.pdf
│   └── doc-002.pdf
└── door-parser/      # Exit to parser stage

parser/               # Extract text
├── ROOM.yml
├── inbox/
├── script: parse.py
└── door-analyzer/

analyzer/             # LLM analyzes content
├── ROOM.yml
├── inbox/
├── prompt: "Summarize and extract entities"
├── door-output/
└── door-errors/

output/               # Final results collect here
├── ROOM.yml
└── inbox/
    ├── doc-001-summary.yml
    └── doc-002-summary.yml
```

---

## Processing Loop

```
> ENTER parser
You are in the Parser room.
Inbox: 2 items waiting.

> NEXT
Processing doc-001.pdf...
Running parse.py...
Text extracted to doc-001.txt

> STAGE doc-001.txt door-analyzer
Staged for analyzer.

> NEXT
Processing doc-002.pdf...
[repeat]

> FLUSH
Throwing 2 items through door-analyzer...
Items landed in analyzer/inbox/
```

---

## Hybrid Processing

Some stages run **scripts** (deterministic):
```yaml
# parser/ROOM.yml
processor:
  type: script
  command: "python parse.py ${input}"
```

Some stages run **LLM prompts** (semantic):
```yaml
# analyzer/ROOM.yml
processor:
  type: llm
  prompt: |
    Analyze this document:
    - Extract key entities
    - Summarize in 3 sentences
    - Flag any concerns
```

Mix and match. **LLM for reasoning, scripts for transformation.**

---

## Kilroy Integration

MOOLLM data flow maps directly to Kilroy pipelines:

| MOOLLM | Kilroy |
|--------|--------|
| Room | Node |
| Exit | Edge |
| THROW | Message passing |
| inbox/ | Input queue |
| Script processor | Deterministic module |
| LLM processor | LLM node |

See [designs/kilroy-ideas.md](../../designs/kilroy-ideas.md) for deep integration patterns.

---

## Advanced: Fan-Out and Fan-In

### Fan-Out (one-to-many)

```yaml
# router/ROOM.yml
exits:
  - door-fast-track    # High priority items
  - door-standard      # Normal processing  
  - door-archive       # Just store, don't process

routing_rules:
  - if: "priority == 'high'"
    throw_to: door-fast-track
  - if: "type == 'archive'"
    throw_to: door-archive
  - default: door-standard
```

### Fan-In (many-to-one)

```yaml
# aggregator/ROOM.yml
# Multiple rooms throw here
# Process when batch is complete

batch_size: 10
on_batch_complete: |
  Combine all results
  Generate summary report
  THROW report.yml door-output
```

---

## Dovetails With

- [Room](../room/) — Rooms as processing nodes
- [Trading Card](../trading-card/) — Cards as reusable processors
- [Sister Script](../sister-script/) — Scripts for deterministic stages
- [Coherence Engine](../coherence-engine/) — LLM as orchestrator
- [Kilroy Ideas](../../designs/kilroy-ideas.md) — External integration

---

## Protocol Symbols

```
DATA-FLOW     — Rooms as pipeline nodes
THROW         — Send object through exit
INBOX         — Incoming message queue
OUTBOX        — Outgoing staging area
```

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#DATA-FLOW)
