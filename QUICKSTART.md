# MOOLLM Quickstart

**Read time: 3 minutes** ⏱️

---

## What the Hell Is This?

**The problem:** LLM agents are black boxes. They have "memory" you can't inspect, "planning" you can't audit, and crash when they encounter missing data. You feed tokens into a void and hope.

**The solution:** MOOLLM turns the filesystem into a **microworld** — a place where agents go on adventures, summon characters, build memory palaces, and navigate by meaning. Every thought is a file you can read. Every session is a story you can replay. The agent doesn't just *use* the filesystem — it *lives* there.

**Why it matters:**

| Black Box Agent | MOOLLM Agent |
|-----------------|--------------|
| "Trust me, I remembered" | Read `hot.yml` — see exactly what's loaded |
| Crashes on missing context | Self-heals, creates stub, continues |
| "I planned internally" | Read `PLAN.yml` — approve before execution |
| Isolated single-agent calls | Many agents talk in ONE LLM call (speed of light) |
| Hidden state | **Everything is files. No magic.** |
| Text generator | **Coherence Engine** — referee, orchestrator, consistency checker |

---

## What's Unique?

1. **It's a microworld, not a database.** The filesystem isn't storage — it's a *place*. Directories are **rooms** you enter. Files are **objects** you examine. You don't query data, you **go on adventures**.

2. **Characters live here.** Summon a Skeptic card into your research room. Have documents debate each other. Let the codebase explain itself. Everything can speak — files, concepts, rooms, tools.

3. **Memory palaces, not memory dumps.** Organize knowledge spatially. Put the important stuff in the Treasury. Archive old experiments in the Catacombs. Navigate by *meaning*, not by filename.

4. **Extreme parallelism.** Forget ChatGPT's one-user-one-assistant model. MOOLLM runs **many conversations at once**: `design-debate.md` (Architect vs Critic), `security-review.md` (3 reviewers), `api-discussion.md` (Frontend + Backend) — all simulated in **ONE LLM call**. 50+ interactions, 1 API call. Like The Sims updating all characters in one frame.

5. **Self-healing by design.** Missing file? Create it. Corrupted state? Rename `.corrupted`, start fresh. NEVER crash. The adventure continues.

6. **YAML Jazz.** Comments carry meaning. `timeout: 30 # generous, API flaky on Mondays` — the LLM understands *why*.

7. **Hero-Stories.** Invoke Dave Ungar's wisdom without pretending to *be* Dave Ungar. Compose skill sets from real people in the training data — ethically, coherently.

8. **Characters are apps.** Each character has a `SKILL.md` (man page), `PROTOTYPE.yml` (interface), and commands it responds to. Like CLI tools with personality.

9. **Hybrid LLM + Python.** YAML schemas let deterministic code do what LLMs shouldn't: sorting, aggregating, validating, calculating. LLM reasons → Python transforms → LLM synthesizes. No wasted tokens on math.

10. **Sister scripts.** Proven chat patterns crystallize into automation. The slow LLM conversation becomes a fast Python script. Document-first development.

11. **Chat is the new shell.** `SUMMON critic | architect > decisions.yml` — compose characters like Unix pipes. The conversation IS the command line.

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
| 10 | **POSTEL** | Be liberal in what you accept. Interpret charitably. |

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
| Unknown command? | POSTEL — interpret charitably |

---

## Quick Commands (Protocol Symbols)

Type these as commands or reference in docs:

```
YAML-JAZZ       # Interpret semantically
POSTEL          # Interpret charitably  
PLAY-LEARN-LIFT # Start exploring
SOUL-CHAT       # Give something a voice
ENTER-ROOM      # Navigate to context
```

Full index: [PROTOCOLS.yml](./PROTOCOLS.yml)

---

## Standing on Giants

MOOLLM is **constructionist computing** for LLM agents:

| Tradition | Person | What We Took |
|-----------|--------|--------------|
| **Constructionism** | Papert, Kay | Learning by building inspectable things |
| **The Sims / SimCity** | Will Wright, Don Hopkins | Objects advertise, agents select autonomously |
| **OLPC SimCity** | Don Hopkins | Simulation as learning microworld |
| **HyperCard** | Bill Atkinson | Non-programmers building apps (1987!) |
| **Self** | Dave Ungar | Prototypes, "It's About Time" |
| **Robust-First** | Dave Ackley | Survivability over correctness |
| **K-Lines** | Marvin Minsky | Names activate conceptual clusters |
| **Kilroy** | Chuck Shotton | Decentralized swarms, small LLMs |

> *"If you can build it, you can understand it. If you can inspect it, you can trust it."*

---

## Next Steps

- [ ] Read the kernel: [kernel/README.md](./kernel/README.md)
- [ ] Explore skills: [skills/README.md](./skills/README.md)
- [ ] Try a room: [skills/room/](./skills/room/)
- [ ] Play a card: [skills/card/](./skills/card/)
- [ ] Learn the methodology: [skills/play-learn-lift/](./skills/play-learn-lift/)

---

## The Mantra

> *The LLM is a token predictor.*
> *The filesystem is the brain.*
> *The protocols are the cognitive style.*

---

> [!NOTE]
> Ready? [Explore the palace →](./README.md#️-navigate-the-palace)
