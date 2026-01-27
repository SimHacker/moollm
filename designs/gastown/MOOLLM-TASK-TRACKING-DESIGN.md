# MOOLLM Task Tracking: Beads vs Issues vs Tasks

> *"A rose by any other name would smell as sweet — but a bead by any other name might just be an issue."*

**Status:** Design Analysis  
**Date:** 2026-01-26  
**Author:** Don Hopkins, with Claude  
**Related:** [GASTOWN-VS-MOOLLM-ANALYSIS.md](GASTOWN-VS-MOOLLM-ANALYSIS.md), [BEADS-2026-01.md](BEADS-2026-01.md), [BEAD-ORCHESTRATION.yml](BEAD-ORCHESTRATION.yml), [README.md](README.md)

---

## Executive Summary

After deep analysis of Gas Town's source code (`gastown/internal/`), this document evaluates whether MOOLLM should adopt the "bead" nomenclature or use simpler, more universal terms. **Recommendation: Use "task" as the primary term with YAML Jazz expressiveness, adopting useful patterns from Gas Town without the jargon.**

---

## Part 1: What Gas Town's "Bead" Actually Is

### The Underlying Reality

Examining `gastown/internal/beads/beads.go` and `constants.go`, a "bead" is:

```go
// From gastown/internal/beads/beads.go
type Issue struct {
    ID          string   `json:"id"`
    Title       string   `json:"title"`
    Description string   `json:"description"`
    Status      string   `json:"status"`      // "open", "in_progress", "closed"
    Priority    int      `json:"priority"`    // 0-4
    Type        string   `json:"issue_type"`  // see below
    CreatedBy   string   `json:"created_by,omitempty"`
    Parent      string   `json:"parent,omitempty"`
    Children    []string `json:"children,omitempty"`
    DependsOn   []string `json:"depends_on,omitempty"`
    Labels      []string `json:"labels,omitempty"`
    // ... agent-specific fields
}
```

**It's an issue tracker entry.** The struct is literally named `Issue`. The CLI tool is `bd` (beads), but it creates, updates, and closes *issues*.

### The Custom Types

From `constants.go`, Gas Town registers these "bead" types:

```go
BeadsCustomTypes = "agent,role,rig,convoy,slot,queue,event,message,molecule,gate,merge-request"
```

| Type | What It Actually Is |
|------|---------------------|
| `agent` | Agent identity record |
| `role` | Role definition |
| `rig` | Project/repo identity |
| `convoy` | Work batch (group of issues) |
| `slot` | Exclusive lock/mutex |
| `queue` | Message queue |
| `event` | Log entry |
| `message` | Mail message |
| `molecule` | Workflow template |
| `gate` | Async coordination point |
| `merge-request` | PR/MR tracking |

**Observation:** Half of these aren't "work items" at all — they're system records, messages, and locks. The term "bead" obscures what's actually happening.

---

## Part 2: The Nomenclature Problem

### Why "Bead"?

Steve Yegge chose "bead" as a physical metaphor — beads strung on a thread, prayer beads, jewelry. The metaphor suggests:
- Atomic, self-contained units
- Can be strung together (chains, dependencies)
- Persistent, tangible
- Decorative? (unclear benefit)

### The Cognitive Load

Every new user must learn:
- "bead" = issue/task
- "molecule" = workflow template
- "convoy" = batch of tasks
- "wisp" = ephemeral task
- "hook" = assigned work
- "polecat" = worker agent
- "refinery" = merge processor

**That's 7+ new terms** before you understand "worker gets assigned a task."

### The MOOLLM Alternative

MOOLLM uses terms users already know:

| Gas Town | MOOLLM | Universal Term |
|----------|--------|----------------|
| bead | task | task, issue |
| molecule | workflow | workflow, recipe |
| convoy | batch | batch, sprint |
| wisp | ephemeral task | scratch, temp |
| hook | assignment | assignment, inbox |
| polecat | worker | agent, worker |
| refinery | merger | CI/CD, integrator |

**Training data leverage**: LLMs know "task" deeply. They know "workflow." They know "assignment." Novel jargon requires explanation tokens.

---

## Part 3: YAML Jazz Superiority

### What Gas Town Stores

Beads are stored as JSONL in `.beads/` directories:

```jsonl
{"id":"gt-abc12","title":"Fix auth","status":"open","priority":2}
```

- Machine-first format
- No comments allowed
- No embedded reasoning
- Requires `bd show` to read
- Diffs are noisy

### What MOOLLM Stores

From `BEAD-ORCHESTRATION.yml`:

```yaml
task:
  id: task-001
  title: "Implement feature X"
  status: pending
  priority: high
  # HIGH because user explicitly asked for this feature
  # and it blocks three other tasks. See: task-015
  # Inner voice: "This is the bottleneck."
  
  reasoning:
    why_high: "Blocks downstream work"
    escalated_by: "User request 2026-01-24"
    dependencies: [task-012, task-013, task-015]
    
  context: |
    This task emerged from the planning session.
    It connects the postal system to orchestration.
    The insight: tasks ARE the universal message capsule.
```

**THE COMMENTS ARE DATA.**

| Aspect | JSONL (Gas Town) | YAML Jazz (MOOLLM) |
|--------|------------------|---------------------|
| Comments | Not allowed | First-class data |
| Reasoning | Lost | Travels with task |
| Context | Separate | Embedded |
| Human-readable | Barely | Fully |
| LLM-readable | Requires parsing | Native |
| Git diffs | Noisy | Semantic |
| Edit-in-editor | Awkward | Natural |

### The Empirical Evidence

From `BEAD-ORCHESTRATION.yml`:

> **Sunil Kumar (Groundlight AI, 2025):**
> "Switching from JSON to YAML massively improved entropy stability."
> JSON constrains. YAML gives room to breathe.

---

## Part 4: Gas Town Abstractions Worth Evaluating

### Abstractions That Interact with Beads

From deep analysis of `gastown/internal/`:

#### 1. **Molecule** (workflow template)
```go
// From molecule.go
type MoleculeStep struct {
    Ref          string   // Step reference
    Title        string   // Step title
    Instructions string   // Prose instructions
    Needs        []string // Dependencies
    WaitsFor     []string // Dynamic conditions
    Tier         string   // Model tier hint
    Type         string   // task, wait, etc.
    Backoff      *BackoffConfig
}
```

**MOOLLM equivalent:** Skills with templates. But MOOLLM skills are more expressive — they have methods, advertisements, state, and can invoke other skills.

**Verdict:** The "step with dependencies" pattern is useful. The "tier hint" for model selection is interesting. The rest is over-engineered.

#### 2. **Formula** (workflow definition)
```go
// From formula/types.go
type FormulaType string
const (
    TypeConvoy    = "convoy"    // Parallel legs + synthesis
    TypeWorkflow  = "workflow"  // Sequential steps
    TypeExpansion = "expansion" // Template expansion
    TypeAspect    = "aspect"    // Multi-aspect analysis
)
```

Four different workflow types with different execution semantics. TOML format.

**MOOLLM equivalent:** The **[adventure skill](../skills/adventure/)** handles this more organically — rooms have exits, characters have actions, the narrative flows. No need for separate "convoy" vs "workflow" vs "aspect" types.

**Verdict:** Overcomplication. MOOLLM's single-call simulation handles all these patterns internally.

#### 3. **Convoy** (work batch)
```go
// From convoy/observer.go
// Tracks which tasks belong together
// Notifies when all complete
```

**MOOLLM equivalent:** Simply a task with children. Or a directory with multiple task files.

**Verdict:** Useful pattern, trivial implementation. Call it a "batch" or "sprint."

#### 4. **Hook** (persistent assignment)
```go
// An agent's pinned task
// Survives session death
// GUPP: "If work is on your hook, RUN IT"
```

**MOOLLM equivalent:** Three-tier persistence already handles this. Character state files in git. The assignment is just a field in the character's state.

**Verdict:** GUPP ("run your assignment") is good discipline. The hook *mechanism* is redundant if you have proper persistence.

#### 5. **Wisp** (ephemeral task)
```go
// Package wisp provides utilities for working with the .beads directory.
// This package was originally for "hook files" but those are now deprecated
// in favor of pinned beads.
const WispDir = ".beads"
```

**Note:** The wisp concept has been deprecated in Gas Town itself!

**MOOLLM equivalent:** Scratchpad, working memory. Not everything needs to be persisted.

**Verdict:** Don't adopt. Use scratchpad/ephemeral tier as-is.

#### 6. **Gate** (async coordination)
```go
// From constants.go
// gate - Async coordination (bd gate wait, park/resume)
```

**MOOLLM equivalent:** Not needed for single-call simulation. For multi-session work, just use file-based state.

**Verdict:** Skip. This is infrastructure for external orchestration.

#### 7. **Slot** (exclusive lock)
```go
// slot - Exclusive access / merge slots
```

**MOOLLM equivalent:** Not needed. Single-call means no concurrent access to state.

**Verdict:** Skip.

---

## Part 5: Patterns Worth Adopting

### From Gas Town

| Pattern | Description | MOOLLM Adoption |
|---------|-------------|-----------------|
| **Persistent assignment** | Work survives session death | Already have: three-tier persistence |
| **Dependency tracking** | Tasks can depend on other tasks | Already have: `depends_on` in YAML |
| **Batch tracking** | Group related tasks | Trivial: task with children |
| **Workflow templates** | Reusable multi-step processes | Already have: skills with templates |
| **Agent attribution** | Who did what | Already have: git blame, commit messages |
| **Progress signals** | Step completion markers | Use: status field + events |

### From The Sims (via MOOLLM action-queue)

The **[action-queue skill](../skills/action-queue/)** already implements the useful patterns:

```yaml
methods:
  DO:     "Add action to end of queue"
  NEXT:   "Execute next queued action"
  QUEUE:  "Show current action queue"
  URGENT: "Insert action at front of queue"
  CANCEL: "Remove action from queue"
  CLEAR:  "Empty the entire queue"
  PAUSE:  "Stop executing, keep queue"
  RESUME: "Continue executing queue"
```

This is cleaner than Gas Town's bead/hook/molecule/formula stack.

---

## Part 6: Recommended MOOLLM Vocabulary

### Primary Terms

| Term | Definition | Replaces |
|------|------------|----------|
| **task** | Atomic unit of work with status and dependencies | bead, issue |
| **workflow** | Multi-step process template | molecule, formula |
| **batch** | Group of related tasks | convoy |
| **assignment** | Task assigned to an agent | hook, hook_bead |
| **worker** | Agent that executes tasks | polecat |
| **queue** | Ordered list of pending work | action-queue |

### Task Schema (YAML Jazz)

```yaml
# MOOLLM task format — human-readable, LLM-native
task:
  id: moollm-042
  title: "Implement feature X"
  status: pending | in_progress | done | blocked | cancelled
  priority: low | medium | high | critical
  
  # Reasoning travels with the task
  why: "User requested, blocks dashboard"
  
  # Dependencies
  depends_on: [moollm-040, moollm-041]
  blocks: [moollm-045]
  
  # Context
  source: "Session 2026-01-26"
  assigned_to: null  # or agent ID
  
  # Progress
  progress:
    started: null
    completed: null
    notes: []
```

### Directory Structure

```
project/
├── tasks/
│   ├── INDEX.yml           # Task index with status summary
│   ├── moollm-042.yml      # Individual task file
│   ├── moollm-043.yml
│   └── archive/            # Completed tasks
├── workflows/
│   ├── release.yml         # Workflow templates
│   └── code-review.yml
└── batches/
    └── sprint-2026-01.yml  # Batch tracking
```

---

## Part 7: What NOT to Adopt

### Avoid These Gas Town Patterns

| Pattern | Problem | MOOLLM Alternative |
|---------|---------|-------------------|
| **JSONL storage** | No comments, hard to edit | YAML Jazz in markdown |
| **Novel jargon** | Cognitive load, training data waste | Universal terms |
| **External CLI** | Extra dependency, parsing overhead | Direct file access |
| **Type proliferation** | 11+ types, confusing | task + workflow + batch |
| **tmux orchestration** | Complex infrastructure | Single-call simulation |
| **Custom types registry** | Maintenance burden | YAML schema validation |

### Avoid These Concepts Entirely

| Concept | Why Skip |
|---------|----------|
| **Wisp** | Deprecated in Gas Town itself |
| **Gate** | Only needed for external orchestration |
| **Slot** | Locking for concurrency we don't have |
| **Role bead** | Just use role files/templates |
| **Agent bead** | Just use character state files |

---

## Part 8: Implementation Recommendations

### Immediate Actions

1. **Consider renaming BEAD-ORCHESTRATION.yml** → `TASK-ORCHESTRATION.yml` (if adopting task vocabulary)
2. **Update BEADS-2026-01.md** → `TASKS-2026-01.md` (or keep as historical)
3. **Create skills/task/** — the core task tracking skill
4. **Create skills/workflow/** — multi-step process templates

### Task Skill Interface

```yaml
# skills/task/CARD.yml
card:
  id: task
  name: "Task"
  type: [skill, tracking, essential]
  emoji: ✅
  
  description: |
    Track work items with status, priority, and dependencies.
    YAML Jazz format — comments carry reasoning.

methods:
  CREATE:
    description: "Create a new task"
    parameters:
      title: required
      priority: optional (default: medium)
      depends_on: optional
    output: task file created
    
  UPDATE:
    description: "Update task status or fields"
    parameters:
      id: required
      status: optional
      notes: optional
    output: task file updated
    
  COMPLETE:
    description: "Mark task done"
    parameters:
      id: required
      notes: optional
    output: task moved to archive
    
  LIST:
    description: "Show tasks by status"
    parameters:
      status: optional (default: pending)
    output: chat
    
  TREE:
    description: "Show task dependency tree"
    parameters:
      root: optional
    output: chat
```

### Keep Bead Orchestrators

The **bead orchestrator metaphors** (bracelet, curtain, borg) from `BEAD-ORCHESTRATION.yml` are good! They're just orchestrating *tasks*, not "beads":

- **Task Bracelet** (1D): Sequential task list
- **Task Curtain** (2D): Kanban board
- **Task Borg** (3D): Multi-dimensional analysis

The physical metaphor works. Just call the things being organized "tasks."

---

## Part 9: Migration Path

### From Current MOOLLM Beads

1. The `designs/gastown/BEADS-2026-01.md` document uses `moollm-NNN` IDs — keep these
2. The format is already YAML Jazz — just rename fields
3. Change `bead:` → `task:` in schemas
4. Keep the orchestrator metaphors (bracelet, curtain, borg)

### Compatibility with Gas Town

If bridge is ever needed (moollm-013):

```yaml
# Mapping MOOLLM → Gas Town
task_to_bead:
  task.id → bead.id (prefix mapping)
  task.title → bead.title
  task.status:
    pending → open
    in_progress → in_progress
    done → closed
    blocked → open (with label)
    cancelled → closed (with label)
  task.priority:
    low → 3
    medium → 2
    high → 1
    critical → 0
```

The formats are compatible. The semantics align. Only the vocabulary differs.

---

## Part 9: The Harsh Truth About Gas Town

### Code Quality Assessment

After examining `gastown/internal/`, the code exhibits classic signs of **vibe-coded AI slop**:

#### Shell-Out Architecture
```go
// From swarm/manager.go — EVERYTHING shells out to bd CLI
cmd := exec.Command("bd", "show", epicID, "--json")
cmd.Dir = m.beadsDir

var stdout, stderr bytes.Buffer
cmd.Stdout = &stdout
cmd.Stderr = &stderr

if err := cmd.Run(); err != nil {
    return nil, fmt.Errorf("bd show: %s", strings.TrimSpace(stderr.String()))
}
```

**This is Go code that spawns Python CLI to read JSONL from disk.** Three language hops to read a file. The overhead is absurd.

#### Deprecated Packages Still in Tree
```go
// Package wisp provides utilities for working with the .beads directory.
//
// This package was originally for "hook files" but those are now deprecated
// in favor of pinned beads.
package wisp

const WispDir = ".beads"
```

The "wisp" concept is **deprecated in the codebase itself**. They couldn't even clean up their own abstractions.

#### Redundant Wrapper Layers
```go
// GetSwarm loads a swarm from beads. Alias for LoadSwarm for compatibility.
func (m *Manager) GetSwarm(id string) (*Swarm, error) {
    return m.LoadSwarm(id)
}
```

Alias methods for "compatibility" in a project that's barely released. Who is this compatible with?

#### Boilerplate Explosion

The `beads_escalation.go` file is 442 lines to manage... escalation status on issues. It manually parses key-value pairs from description strings:

```go
for _, line := range strings.Split(description, "\n") {
    line = strings.TrimSpace(line)
    colonIdx := strings.Index(line, ":")
    key := strings.TrimSpace(line[:colonIdx])
    value := strings.TrimSpace(line[colonIdx+1:])
    switch strings.ToLower(key) {
    case "severity":
        fields.Severity = value
    // ... 20 more cases
    }
}
```

**They're storing structured data as text in a description field and parsing it by hand.** This is amateur hour.

### Nomenclature Incoherence

The naming violates every principle of good design:

| Term | What It Actually Is | Training Data Presence |
|------|---------------------|----------------------|
| **Bead** | Issue/task | Near zero |
| **Polecat** | Worker agent | Near zero (it's a ferret) |
| **Wisp** | Ephemeral task | Near zero |
| **Molecule** | Workflow | Near zero (in this context) |
| **Hook** | Assignment | Ambiguous (git hooks?) |
| **Convoy** | Batch | Low |
| **Refinery** | Merge processor | Low (in this context) |
| **Deacon** | Daemon | Near zero |
| **GUPP** | "Run your work" | Zero |
| **MEOW** | "Molecular Expression of Work" | Zero (invented acronym) |

**Every term requires explanation.** Every explanation costs tokens. The naming is **actively hostile to LLM comprehension**.

### "Never Look At It" — Coward's Philosophy

Steve's recommendation: "Never look at the generated code."

This is **atrocious**. It's **terrible engineering**. It's the attitude of someone who:

1. **Won't dogfood their own product** — How can you use what you refuse to examine?
2. **Can't debug** — When vibe code breaks (and it DOES break), what then?
3. **Abdicates responsibility** — "The AI did it" is not a defense
4. **Confuses convenience with wisdom** — Not looking ≠ not needing to look

**Eat your own shit.** That's the dogfooding principle. 

If you generate code, READ the code. If it's unreadable, that's a signal — either improve the prompts or acknowledge you don't understand what you're shipping.

The Gas Town codebase is the result of "never look at it":
- Manual string parsing for structured data
- Shell-outs where native calls would work  
- Deprecated code sitting alongside active code
- Inconsistent naming, conflicting patterns
- Alias methods for "compatibility" in unreleased software

**MOOLLM's approach:** Skills ARE code. The LLM reads them, runs them, improves them. Every line is reviewed because every line matters. You can't understand what you refuse to examine.

### "Abundant Tokens" Is A Lie

The claim that Gas Town is for "abundant tokens" is nonsense:

1. **Parallel costs multiply, not add** — 20 agents = 20× cost minimum
2. **Coordination overhead** — Messages between agents add more tokens
3. **Context duplication** — Each agent reloads the same context
4. **Error recovery** — Failed agents retry, multiplying again

**Efficient parallelism requires efficiency, not abundance.** Gas Town's architecture maximizes waste.

### The Crypto Situation

From the Hacker News discussion:

> "Steve Yegge sold his credibility when he did a meme coin rug pull"
> 
> "He pumped, and dumped. He stopped shilling at the moment that the dump was proceeding."

The `$GAS` memecoin pump-and-dump is not tangential — it reveals something about judgment and ethics. When someone promotes a worthless token to their audience and profits from the dump, their technical recommendations deserve extra scrutiny.

### What The Code Actually Shows

| Claim | Reality |
|-------|---------|
| "Industrial-grade orchestration" | Shell-out wrappers around a Python CLI |
| "Sophisticated agent coordination" | tmux sessions with text injection |
| "Persistent work tracking" | JSONL files parsed by hand |
| "Novel architecture" | Copy-pasted boilerplate |
| "Stage 8 developer required" | Or maybe just... bad design? |

### The Unfalsifiable Escape Hatch

> "If you're not at least Stage 7, or maybe Stage 6 and very brave, then you will not be able to use Gas Town."

Translation: When it doesn't work, it's your fault for not being advanced enough. This is not engineering — it's hand-waving.

---

## Conclusion

### The Answer

**Don't call it "bead."** Call it what it is:

- **task** — a unit of work
- **workflow** — a multi-step process
- **batch** — a group of related tasks
- **assignment** — work given to an agent

### Why

1. **Training data leverage**: LLMs know these terms deeply
2. **User familiarity**: No learning curve
3. **Documentation clarity**: Self-explanatory
4. **Tool integration**: Standard terms map to existing tools

### What to Keep

- **YAML Jazz format** — comments as data, reasoning travels with state
- **Dependency tracking** — tasks can depend on other tasks
- **Orchestrator metaphors** — bracelet (1D), curtain (2D), borg (3D)
- **Persistent assignment** — work survives session death
- **Git-backed storage** — version control, blame, history

### What to Skip — And Why

| Pattern | Problem |
|---------|---------|
| **Novel jargon** | Hostile to LLM comprehension, training data waste |
| **JSONL format** | No comments, hard to edit, no reasoning |
| **Shell-out architecture** | Three language hops to read a file |
| **Type proliferation** | 11+ types for what should be 3 |
| **tmux orchestration** | Fragile, unobservable, debugging nightmare |
| **CLI wrappers** | Layers of indirection for no benefit |
| **Deprecated concepts in tree** | Can't even maintain their own abstractions |

### The Fundamental Difference

**Gas Town:** Interpretive dance performance art with branding. No intellectual lineage. Invented terminology hostile to LLMs. Claims "design is the bottleneck" while having no coherent design.

**MOOLLM:** Built on 60+ years of proven foundations:

| Pattern | Proven Source | Training Presence |
|---------|---------------|-------------------|
| Prototype delegation | Self → JavaScript | Massive |
| Rooms and objects | LambdaMOO, Zork, MUDs | Deep |
| Advertisement coordination | The Sims ($5B+ franchise) | Deep |
| K-lines, activation | Minsky's Society of Mind | Foundational |
| Comments as data | YAML Jazz (Kubernetes, etc.) | Ubiquitous |
| Files as state | Unix philosophy | Universal |

**MOOLLM's patterns WORK because they're in training data DEEPLY and with MULTIFACETED COHERENCE.**

Gas Town's patterns are:
- Invented from whole cloth
- Absent from training data
- Internally inconsistent
- Defended with unfalsifiable claims

### The Bottom Line

Steve Yegge is a brilliant writer. His rants about LLMs contain genuine insights. But Gas Town is:

1. **Performance art, not engineering** — Branding over substance
2. **Vibe-coded AI slop** — Generated, not designed
3. **"Never look at it" cowardice** — Won't dogfood, can't debug
4. **Nomenclature as hostile action** — Every term requires explanation
5. **Architecturally wasteful** — Shell-outs, layers, overhead
6. **Unfalsifiably defended** — "You're not Stage 7" is not debugging

The philosophy sometimes sounds good. The implementation is garbage. The crypto rug pull reveals the judgment behind both.

Take the ONE trivial insight (work persists in git) and implement it properly with standard vocabulary. Skip everything else.

### The Obvious Alternative: Just Use GitHub Issues

Why invent "beads" when GitHub Issues exist?

| Aspect | Gas Town Beads | GitHub Issues |
|--------|----------------|---------------|
| Storage | Custom JSONL, shell-outs | GitHub's database |
| API | Custom `bd` CLI | Standard `gh` CLI |
| UI | None | GitHub web interface |
| Mobile | None | GitHub mobile app |
| Search | Grep JSONL files | GitHub search |
| Training data | **Zero** | **Billions of examples** |

```bash
# Instead of beads:
gh issue create --title "Implement auth" --label "task"
gh issue edit 123 --milestone "Sprint 1"
gh issue edit 123 --assignee @worker
gh issue close 123 --comment "Done"
```

Every LLM knows `gh issue`. No LLM knows "beads".

**See:** [CONSTRUCTIONIST-TERMINOLOGY.md](CONSTRUCTIONIST-TERMINOLOGY.md) for the full vocabulary analysis.

**See also:** [README.md](README.md) for the executive summary of this analysis.

---

## References

- [gastown/internal/beads/](../../gastown/internal/beads/) — Bead implementation
- [gastown/internal/formula/](../../gastown/internal/formula/) — Workflow definitions
- [gastown/internal/constants/](../../gastown/internal/constants/) — Type registry
- [BEAD-ORCHESTRATION.yml](BEAD-ORCHESTRATION.yml) — Bead research (not official)
- [skills/action-queue/](../skills/action-queue/) — Sims-style task scheduling
- [skills/goal/](../skills/goal/) — Quest objective tracking
- [skills/planning/](../skills/planning/) — Flexible task decomposition
