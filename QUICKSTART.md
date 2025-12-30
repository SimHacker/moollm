# MOOLLM Quickstart

**Read time: 3 minutes** ⏱️

---

## What the Hell Is This?

**The problem:** LLM agents are black boxes. They have "memory" you can't inspect, "planning" you can't audit, and crash when they encounter missing data. You feed tokens into a void and hope.

**The solution:** MOOLLM makes the invisible visible. Every thought is a file. Every action is logged. Every plan is YAML you can read. The agent navigates its own memory like a filesystem because *it IS a filesystem*.

**Why it matters:**

| Black Box Agent | MOOLLM Agent |
|-----------------|--------------|
| "Trust me, I remembered" | Read `hot.yml` — see exactly what's loaded |
| Crashes on missing context | Self-heals, creates stub, continues |
| "I planned internally" | Read `PLAN.yml` — approve before execution |
| Isolated single-agent calls | Many agents talk in ONE LLM call (speed of light) |
| Hidden state | **Everything is files. No magic.** |

---

## What's Unique?

1. **Spatial programming.** Directories are rooms. Enter a room = push context. Exit = pop. Cards activate in rooms like function calls with state.

2. **Multi-agent without the bullshit.** Traditional: 3 agents × 5 turns = 15 LLM calls, file I/O between each. MOOLLM: 3 agents × 5 turns = 1 LLM call. They talk at the speed of light *inside the context*.

3. **Self-healing by design.** Missing file? Create it. Corrupted state? Rename `.corrupted`, start fresh, log what happened. NEVER crash. Inspired by Dave Ackley's robust-first computing.

4. **YAML Jazz.** Comments aren't decoration — they're semantic. `timeout: 30 # generous because API flaky on Mondays` tells the LLM *why*, not just *what*.

5. **No impersonation, just storytelling.** Reference real people's wisdom through "Hero-Stories" — K-line activation of their *tradition*, not simulation of their *identity*.

---

## One Sentence

MOOLLM treats LLMs as CPUs and filesystems as RAM — everything the agent knows is in files it can read.

---

## The Core Insight

| Traditional | MOOLLM |
|-------------|--------|
| LLM has hidden memory | All memory is files |
| Magic planning module | Plans are YAML files |
| Opaque agent state | Inspect everything |
| Crashes on missing data | Self-heals and continues |

---

## Ten Concepts to Know

| # | Concept | One Line |
|---|---------|----------|
| 1 | **FILES-AS-STATE** | No hidden memory. If it's not in a file, it doesn't exist. |
| 2 | **YAML-JAZZ** | Comments carry meaning. LLMs interpret, not just parse. |
| 3 | **WHY-REQUIRED** | Every tool call explains its intent. Self-documenting traces. |
| 4 | **APPEND-ONLY** | Logs never modified. Perfect audit trail. |
| 5 | **NEVER-CRASH** | Missing state triggers repair, not failure. |
| 6 | **ROOM-AS-FUNCTION** | Directories are activation records. Enter = call. Exit = return. |
| 7 | **TRADING-CARD** | Capabilities as instantiable templates. Play cards in rooms. |
| 8 | **PLAY-LEARN-LIFT** | Explore → find patterns → share wisdom. The methodology. |
| 9 | **SPEED-OF-LIGHT** | Many agents in one LLM call. No carrier pigeons. |
| 10 | **BPIP** | Best Possible Interpretation. Assume good faith always. |

---

## The Architecture

```
kernel/     → OS protocols (infrastructure)
skills/     → Userland protocols (capabilities)  
schemas/    → Data format definitions
PROTOCOLS.yml → Symbol index (K-lines)
```

**Kernel** defines *how* things work (tool calling, logging, self-healing).
**Skills** define *what* you can do (planning, rooms, cards, chat).

---

## File Format Hierarchy

| Format | Use For | Why |
|--------|---------|-----|
| **Markdown** | Logs, docs, conversations | Human-readable, embeds code blocks |
| **YAML** | Config, state, parameters | Has comments! Semantic. Editable. |
| **JSON** | Machine interchange only | No comments. Last resort. |

---

## Capability Tiers

| Tier | What You Can Do |
|------|-----------------|
| 0 | Text only (basic chat) |
| 1 | Read files |
| 2 | Read + write files |
| 3 | + Search |
| 4 | + Execute commands |
| 5 | + Custom tools (MCP) |
| 6 | + Full kernel control |

Protocols degrade gracefully. Works at any tier.

---

## Session Structure

```
.agent/
  sessions/
    current/
      session-log.md    # Append-only audit trail
      working_set.yml   # What's in context
      hot.yml           # Keep these files loaded
      cold.yml          # These can be evicted
      instances/        # Active skill instances
```

---

## The Self-Healing Promise

> [!IMPORTANT]
> When something is missing, MOOLLM **doesn't crash**:

| Problem | Solution |
|---------|----------|
| Missing file? | Create minimal stub, continue |
| Corrupted state? | Rename to `.corrupted`, create fresh, log recovery |
| Over budget? | Truncate lowest priority, continue |
| Unknown command? | BPIP — interpret charitably |

---

## Quick Commands (Protocol Symbols)

Type these as commands or reference in docs:

```
YAML-JAZZ       # Interpret semantically
BPIP            # Assume good faith  
PLAY-LEARN-LIFT # Start exploring
SOUL-CHAT       # Give something a voice
ENTER-ROOM      # Navigate to context
```

Full index: [PROTOCOLS.yml](./PROTOCOLS.yml)

---

## Standing on Giants

| System | What We Took | Why It Works |
|--------|--------------|--------------|
| **The Sims** | Objects advertise capabilities | Agent picks best action based on goals, not scripts |
| **HyperCard** | Stacks, cards, message delegation | Non-programmers built apps in 1987. We can too. |
| **Self** | Prototypes, no classes | Clone and modify beats rigid inheritance |
| **LambdaMOO** | Rooms as spatial programming | Navigation IS cognition |
| **MFM** | Robust-first, local repair | Survivability beats correctness |
| **Kilroy** | Decentralized swarms | Many small LLMs beat one big prison |

---

## Next Steps

- [ ] Read the kernel: [kernel/README.md](./kernel/README.md)
- [ ] Explore skills: [skills/README.md](./skills/README.md)
- [ ] Try a room: [skills/room/](./skills/room/)
- [ ] Play a card: [skills/trading-card/](./skills/trading-card/)
- [ ] Learn the methodology: [skills/play-learn-lift/](./skills/play-learn-lift/)

---

## The Mantra

> *The LLM is a token predictor.*
> *The filesystem is the brain.*
> *The protocols are the cognitive style.*

---

> [!NOTE]
> Ready? [Explore the palace →](./README.md#️-navigate-the-palace)
