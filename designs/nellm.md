# NeLLM: NeWS for Language Models

> Like NeWS (or AJAX) but between the GPU and CPU of the host. Demand paging the filesystem microworld at hardware speed.

## The Analogy

**NeWS** (Network Extensible Window System, Sun Microsystems): Instead of sending pixels over the network (X11 model), send PostScript PROGRAMS to execute locally on the display server. The program runs close to the hardware, eliminates network round-trips, enables feedback loops (rubber-banding, mouseover) at display refresh rate.

**NeLLM** (Network Extensible Language Model): Instead of sending prompts over the network to a data center and waiting for tool call round-trips, run the LLM locally and have a co-located orchestrator that interacts with the inference loop at GPU-to-CPU speed. The orchestrator runs close to the GPU, eliminates network round-trips, enables feedback loops (file loading, condition checking, context injection) at token generation rate.

NeWS moved computation to the display server. NeLLM moves orchestration to the inference server.

## The Latency Stack

| Path | Latency | Tokens per gap |
|------|---------|---------------|
| GPU ↔ CPU (PCIe/NVLink) | 1-10 us | 1,000-50,000 ops between tokens |
| CPU ↔ RAM | 0.1 us | Effectively instant |
| CPU ↔ NVMe SSD | 10-100 us | 100-5,000 ops between tokens |
| Localhost TCP | 50-500 us | 20-1,000 ops between tokens |
| Internet API call | 10-100 ms | 0 ops — you've lost the thread |
| Full tool call round-trip (today) | 100-500 ms | Model "dies" and restarts |

Between every single token (10-50ms), the CPU could:
- Read dozens of files from NVMe SSD
- Execute hundreds of Python operations
- Query an in-memory database
- Run regex scans across a codebase
- Make thousands of decisions about what to feed next

The physics allows it. The budget is enormous. Today's architecture wastes it by routing everything through the internet.

## Demand Paging the Microworld

The LLM's context window IS virtual memory. Files on disk ARE physical pages. The orchestrator IS the MMU.

| Virtual Memory | NeLLM |
|---------------|-------|
| Virtual address space | Context window |
| Physical pages | Files on disk |
| Page table | hot.yml / working-set.yml |
| Page fault | Model requests a file not in context |
| Page in | Orchestrator injects file into live KV cache |
| Page out | Summarize and evict (honest-forget) |
| Working set | Files currently in context |
| Thrashing | Context window full, constant page faults |
| TLB | Recently-accessed file cache in RAM |

MOOLLM's `.moollm/hot.yml` and `working-set.yml` are literally page table metadata — advisory lists of what should be in context. Today they're advisory because the orchestrator reads them on boot and makes loading decisions. With NeLLM, they become live page tables that the demand pager consults between tokens.

## Async Virtual Threads in the GPU

Each MOOLLM entity (character, room, object, skill) is a virtual thread:

1. The LLM is generating tokens for Character A's dialogue
2. Character A needs to check what's in Room B (file read)
3. **Today**: tool call → model dies → round trip → new completion → model rebuilds state
4. **NeLLM**: orchestrator intercepts → reads Room B from local cache → injects into live KV cache → Character A continues from the exact same point in high-dimensional space

The character never "died." The room came to the character, not the character to the room. The thread blocked on I/O and resumed when the page faulted in.

Multiple simulation threads can be "in flight" in the same completion call:
- Character A is talking (active thread, generating tokens)
- Character B's needs are decaying (background thread, orchestrator updates state file)
- Room C's environment is changing (background thread, orchestrator modifies room data)
- The coherence engine is checking consistency (background thread, orchestrator validates state)

All of this happens between tokens. The GPU does the expensive work (token generation). The CPU does the cheap work (file I/O, state management, consistency checking) in the gaps.

## The NeWS Heritage

Don Hopkins worked on NeWS at Sun Microsystems. The pattern is the same, 35 years later:

| NeWS (1986) | NeLLM (202x) |
|-------------|-------------|
| PostScript interpreter on display server | Orchestrator on inference server |
| Send programs, not pixels | Send skills, not prompts |
| Local execution eliminates network round-trips | Local file access eliminates API round-trips |
| Feedback loops at display refresh rate (60Hz) | Feedback loops at token generation rate (20-100 tokens/sec) |
| rubber-banding, mouseover, animation | file loading, condition checking, context injection |
| Display PostScript later replaced by X11+network | NeLLM would replace today's API+tool-call model |

The same architectural insight: move computation closer to the hardware that needs it. Don't serialize everything through a network bottleneck when the interesting feedback loop is between two things on the same machine.

## What Would MOOLLM Look Like on NeLLM

**speed-of-light** becomes real, not simulated. Multiple entities genuinely running concurrently in the GPU, blocking on I/O that resolves in microseconds.

**Rooms** become demand-paged. Enter a room → room contents fault into context. Leave a room → contents can be paged out. The filesystem IS the backing store for virtual memory.

**Advertisements** become interrupt-driven. An object's advertisement score changes → the orchestrator updates it between tokens → the model notices on the next token it generates.

**K-lines** become activation signals to the demand pager. A k-line fires → the pager loads the associated skill's GLANCE into the TLB (hot cache) → if the model needs more, the CARD page-faults in → if it needs full protocol, SKILL.md faults in. The Semantic Image Pyramid IS a multi-level page table.

**The bootstrap sequence** becomes the initial page-in: load kernel, load hot.yml page table, warm the TLB with GLANCE files, ready for demand paging.

## What's Needed to Build This

1. **A local model** — runs on your machine's GPU, not a data center. Llama, Mistral, Qwen, etc. via llama.cpp, vLLM, SGLang.

2. **A modified inference loop** — between token N and token N+1, check if the orchestrator has injected new context. Extend the KV cache if so. SGLang's RadixAttention is the closest starting point.

3. **The NeLLM orchestrator** — a process on the same machine that:
   - Watches the token stream for tool-call patterns
   - Reads files from local SSD/RAM cache
   - Injects file contents into the live KV cache
   - Manages the page table (hot.yml, working-set.yml)
   - Runs background threads (state decay, consistency checking)

4. **A hot-path file cache** — the project files pre-loaded into RAM on session start. The "TLB" for the demand pager. NVMe SSD as the "main memory." Git repo as the "swap space."

5. **MOOLLM skills that work at both scales** — speed-of-light (simulated, single call, any provider) as the fallback, NeLLM (real demand paging, local model) as the fast path. Same skill, different "device driver." The `.moollm/hot.yml` advisory files become real page tables when NeLLM is available.

## The Efficiency Argument

Today's architecture:
```
User types → internet → API server → GPU generates 50 tokens →
API server → internet → user's machine → tool call executes →
internet → API server → GPU rebuilds KV cache → generates 50 more →
...repeat 20 times for a complex task
```

Total: 20 round-trips × 200ms = 4 seconds of pure network waste. Plus KV cache rebuilds.

NeLLM architecture:
```
User types → local GPU generates tokens continuously →
orchestrator injects files between tokens (<1ms each) →
GPU never stops, never rebuilds, never loses state →
complex task completes in one unbroken stream
```

Total: 0 network waste. 0 KV cache rebuilds. The model stays "awake" and "in place" for the entire task.

The efficiency gain isn't 2x or 5x. It's a different kind of computation. The model maintains a continuous high-dimensional trajectory instead of repeatedly dying and being resurrected in approximately the right neighborhood.

## Heritage: The lloooomm NeLLM Vision

NeLLM was extensively designed in the lloooomm prototype (predecessor to MOOLLM). The archives contain 30+ documents exploring the concept. Key ideas that evolved into MOOLLM:

### The 4-Layer Architecture

```
GPUNeLLM   (0.1ms)  — on the GPU host, token-level feedback
CloudNeLLM (10ms)   — data center co-located, API-level feedback
EdgeNeLLM  (50ms)   — local network, session-level feedback
BrowserNeLLM (100ms) — in the browser, UI-level feedback
```

This maps directly to MOOLLM's device driver concept: `kernel/drivers/cursor.yml` for Cursor, a future `kernel/drivers/nellm.yml` for GPU-local operation. Same skills, different latency profiles. The driver adapts to what's available.

### Persistent Contexts (the Wolfram Insight)

Stephen Wolfram showed that ChatGPT can't do real computation — no loops, no state, no persistent memory. NeLLM's core answer: persistent JavaScript contexts (via ShadowRealm) that survive across completions. Variables, functions, accumulated knowledge persist.

This evolved into MOOLLM's `.moollm/` directory: `hot.yml`, `cold.yml`, `working-set.yml`, `session-log.md` — filesystem-based persistence that works with any orchestrator. Not as fast as in-memory contexts but universally portable.

### Dasher Navigation Through Probability Space

Dasher (the accessible text entry system) navigates through probability distributions using continuous gesture. NeLLM applied this to code: instead of discrete autocomplete suggestions, navigate continuously through the space of possible completions, seeing live execution previews of each path.

This connects to MOOLLM's `adventure` skill: navigate through rooms (probability regions), see what's in each direction (advertisements), choose based on scored relevance (information-theoretic efficiency). Dasher navigation through thought space IS room-based exploration of a semantic landscape.

### Think-Talk Protocol

Two modes of processing:
- **THINK**: internal, recursive, private — the model reasoning to itself
- **TALK**: external, dialogic, public — the model communicating with others
- **LOOP**: continuous feedback between thinking and talking

This maps to MOOLLM's `speed-of-light` (THINK — many turns in one call), `adversarial-committee` (TALK — debate between perspectives), and the evaluator's simulated/isolated modes (the choice between thinking privately and speaking publicly).

### NeWS Windows: Direct Manipulation of Computation

In NeWS, PostScript programs running on the display server could create interactive windows. In NeLLM, computation results become interactive visualizations — not static text but manipulable objects. Click a number to see its derivation. Drag a function to compose it with another.

This is the future adventure UI: direct manipulation of rooms and objects, not just text commands. The iLoci vision (drag nodes, kiss to connect, zoom to explore) applied to computation results.

### Society of Minds Conference

Multiple NeLLM contexts conferencing — each with their own persistent state, communicating via structured messages. Characters in different rooms, each running their own simulation, sharing observations.

This is exactly the MCP vision we documented today: entities as MCP servers, advertising their tools, calling each other's methods. Speed-of-light as the localhost loopback. Carrier pigeon as the real MCP calls between processes.

### Semantic Physics

From the Wolfram synthesis: language has "semantic laws of motion." Similar concepts attract (convergence). Aligned ideas amplify (resonance). Conflicting concepts create new patterns (interference). Connected contexts become entangled.

This is the theoretical foundation for k-lines (semantic activation), the coherence-engine (consistency as a physical law), and the advertisement system (relevance as gravitational attraction).

## lloooomm Source Files

The NeLLM concept is explored across 30+ files in `temp/lloooomm/03-Resources/`:

| File | Key Content |
|------|-------------|
| `discussions/SimNeLLM-Living-Design-Doc.md` | 4-layer architecture, WIZIDS characters, JIT consciousness compilation |
| `guides/nellm-quick-start-guide.md` | Minimum viable NeLLM, 4-week roadmap, 5 key principles |
| `discussions/nellm-technical-implementation-018.md` | CodeDasher, PersistentState, ContextAwareLLM, SecureRealm |
| `special/visions/a-day-with-nellm-020.md` | Narrative vision: morning contexts, collaborative computation, time-travel |
| `discussions/nellm-dasher-protocol-design.md` | 7-layer inside-out architecture, consciousness metrics |
| `discussions/nellm-dasher-think-talk-synthesis.md` | Navigation becomes thinking, thinking becomes visible |
| `discussions/wolfram-lloooomm-nellm-synthesis-019.md` | Semantic laws of motion, persistence revolution, consciousness emergence |
| `discussions/SimNeLLM-Code-Review-Session.md` | Code review of implementation |
| `discussions/nellm-dasher-implementation-examples.md` | Concrete implementation patterns |
| `discussions/nellm-html-showcase-summary.md` | Browser-based visualization design |
| `papers/wolfram-chatgpt-lloooomm-nellm-summary.md` | Wolfram's ChatGPT analysis applied to NeLLM |

---

*NeWS moved PostScript to the display server (1986). iLoci made the app and server peers (2009). NeLLM moves the orchestrator to the GPU host (202x). Same insight, same person, across four decades.*
