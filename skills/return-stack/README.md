# 🔙 Return Stack

> Where you've been is where you can go back to

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Rooms are stack frames |
| [adventure/](../adventure/) | Navigation through rooms |
| [character/](../character/) | Characters carry return stacks |
| [memory-palace/](../memory-palace/) | Navigate knowledge |
| [action-queue/](../action-queue/) | Past ↔ Future |
| [card/](../card/) | Cards as continuations |
| [session-log/](../session-log/) | Log navigation history |
| [prototype/](../prototype/) | Self's dynamic deoptimization |
| [debugging/](../debugging/) | Stack traces on demand |
| [speed-of-light/](../speed-of-light/) | Many turns, one call |

**Proof:**
- [33-Turn Stoner Fluxx](../../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#33-turns-of-pure-gezelligheid) — 8+ characters, 33 turns, no explicit stack maintained, causality reconstructible

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Navigation history as a first-class **continuation** — a stack of saved positions you can manipulate like browser history or a call stack.

---

## Dynamic Deoptimization: Self's Gift

The Self programming language taught us something profound about stack traces.

Self aggressively inlines method calls for performance. The actual call stack in memory doesn't match the logical call stack in source code — the frames have been optimized away.

But when you hit a breakpoint or an error? **Self reconstructs what the stack *would have been* if not for inlining.** It "deoptimizes" on demand, cooking up a virtual return stack from:
- Source code structure
- Execution context
- Saved state

This is called **dynamic deoptimization** (or "pessimization" when you want the debuggable version back).

---

## LLMs Do This Naturally

The LLM doesn't maintain an explicit return stack during conversation. There's no push/pop as you navigate rooms.

But the LLM can **reconstruct causality on demand** by examining:

| Source | What It Reveals |
|--------|-----------------|
| Chat history | Sequence of decisions |
| Session logs | Navigation trail |
| Microworld state | Current configuration |
| File timestamps | Order of changes |
| Room contents | Accumulated effects |

**Ask "how did we get here?" and the LLM generates a stack trace** — a causal chain explaining the path from start to present.

This is dynamic deoptimization for narrative: the explicit stack wasn't maintained, but it can be reconstructed from evidence.

---

## Stack Trace On Demand

```
> How did we get to this room?

Reconstructing navigation history...

1. You started in lobby (session-log line 1)
2. Entered workshop to examine blueprints (line 45)
3. Found reference to storage vault (line 67)
4. Entered storage, discovered locked chest (line 89)
5. Returned to workshop for key (BACK) (line 112)
6. Key obtained, returned to storage (line 134)
7. Opened chest, found map to archive (line 156)
8. Current: archive, examining old records (line 178)

Causal chain: curiosity → blueprints → reference → 
             obstacle → backtrack → solution → progress
```

The LLM didn't push/pop these frames in real time. It **deduced** them from the evidence trail.

---

## Debugging Technique

When something goes wrong, ask for the virtual stack:

```
> The treasure room is empty. What happened?

Examining state and history...

Stack trace:
- treasure.yml: contents = []
- session-log (142): "Biscuit took the gems"
- session-log (89): "You gave Biscuit access"
- session-log (67): "You trusted Biscuit's cute face"

Root cause: Biscuit. Obviously.
```

This is **introspection without instrumentation**. The stack was never explicitly maintained, but the causal history is recoverable.

---

## The Metaphor

| Programming | Browser | MOOLLM |
|-------------|---------|--------|
| Call stack | History | Return stack |
| Return address | Back button | Previous room |
| Stack frame | Tab | Room context |
| Push | Navigate | ENTER |
| Pop | Back | BACK |
| Deoptimization | View source | Reconstruct history |

## Commands

| Command | Effect |
|---------|--------|
| `ENTER room` | Push current, enter new |
| `BACK` | Pop, return to previous |
| `FORWARD` | Redo after BACK |
| `HISTORY` | Show the stack |
| `BOOKMARK` | Save position |
| `GOTO bookmark` | Jump to saved |
| `FORK` | Create parallel stack |

