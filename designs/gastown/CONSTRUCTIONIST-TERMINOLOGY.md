# Constructionist AI Terminology: Better Than "Bead"

> *Terms from Minsky, Papert, Kay, Wright, and the MIT AI Lab tradition*

**Status:** Design Reference  
**Date:** 2026-01-26  
**Purpose:** Find terms with deep training data presence and intellectual coherence

---

## The Problem with "Bead"

Gas Town's "bead" has near-zero training data presence. It's invented jargon that LLMs don't know. Every use requires explanation, costing tokens.

**Goal:** Find terms from the constructionist tradition that are:
1. Deeply represented in training data
2. Intellectually coherent (part of a system)
3. Universal (work across domains)
4. Self-documenting (meaning is obvious)

---

## Part 1: Minsky's Society of Mind Terminology

### For Units of Work

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **Agent** | Simple process that does one thing | High (but overloaded now) | Medium |
| **Goal** | Difference between desired and actual state | High | **Excellent** |
| **Neme** | Small unit of knowledge | Low | Poor |
| **Polyneme** | Signal that activates multiple agents | Low | Poor |

### For Memory/Context

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **K-line** | Memory that reactivates a mental state | Medium (in AI context) | **Excellent for MOOLLM** |
| **Frame** | Structured expectation/template | High | **Excellent** |
| **Microneme** | Subtle contextual signal | Low | Poor |

### For Control

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **Censor** | Agent that prevents bad actions | Medium | Good |
| **Suppressor** | Agent that stops ongoing actions | Low | Poor |

**Best Minsky terms:** `goal`, `frame`, `k-line`

---

## Part 2: Papert/Logo Terminology

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **Procedure** | Named sequence of instructions | Very High | **Excellent** |
| **Bug** | Thing to debug (learning opportunity) | Very High | Good (but overloaded) |
| **Microworld** | Constrained environment for exploration | Medium | Good |
| **Project** | Meaningful work with purpose | Very High | **Excellent** |

**Best Papert terms:** `procedure`, `project`

---

## Part 3: Self Language Terminology (Ungar & Smith)

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **Slot** | Unified container (data or behavior) | High | **Excellent** |
| **Message** | Communication triggering behavior | Very High | **Excellent** |
| **Prototype** | Object to clone from | High | Good |
| **Clone** | Copy that can be modified | High | Good |
| **Delegation** | Forward to parent for lookup | Medium | Good |

**Self's insight:** Everything is slots and messages. No distinction between data and behavior. MOOLLM already uses delegation chains.

**Best Self terms:** `slot`, `message`, `delegation`

---

## Part 4: The Sims Terminology (Will Wright)

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **Motive** | Drive that selects actions | High | **Excellent** |
| **Advertisement** | What an object offers | Medium (in this context) | **Excellent for MOOLLM** |
| **Action** | Queued behavior unit | Very High | **Excellent** |
| **Queue** | Ordered list of pending work | Very High | **Excellent** |
| **Autonomy** | Self-directed execution | High | Good |

**Sims insight:** Objects *advertise* what they can do. Agents select based on *motives*. Work is *queued* and executed. MOOLLM's `action-queue` skill is directly Sims-inspired.

**Best Sims terms:** `action`, `queue`, `motive`, `advertisement`

---

## Part 5: LambdaMOO Terminology

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **Verb** | Action that can be performed | Very High | Good |
| **Property** | Attribute of an object | Very High | Good |
| **Room** | Container/context for objects | Very High | **Excellent** |

**MOO insight:** The database IS the world. Objects have verbs (methods) and properties (state). Rooms contain objects. MOOLLM uses rooms extensively.

**Best MOO terms:** `room`, `verb`, `property`

---

## Part 6: Smalltalk Terminology (Alan Kay)

| Term | Meaning | Training Presence | Fit |
|------|---------|-------------------|-----|
| **Message** | Request sent to an object | Very High | **Excellent** |
| **Method** | Response to a message | Very High | **Excellent** |
| **Class** | Template for objects | Very High | Good (but hierarchical) |
| **Instance** | Concrete object from class | Very High | Good |

**Kay's insight:** "Objects communicate by sending and receiving messages." Everything is objects all the way down.

**Best Kay terms:** `message`, `method`

---

## Part 7: Recommended MOOLLM Vocabulary

### For "Bead" (Unit of Work)

**Primary recommendation: `action`**

| Why `action` | Benefit |
|--------------|---------|
| Sims-native | Integrates with MOOLLM's Sims-inspired architecture |
| Universal | Works in any domain |
| Training presence | Massive — games, programming, everyday usage |
| Self-documenting | "Do this action" needs no explanation |
| Verb-friendly | "Queue an action", "execute the action" |

**Alternative: `goal`**

For work items that have completion conditions, `goal` (from Minsky) is excellent:
- Has `complete_when` condition
- Can have `fail_when`
- Supports `progress` tracking
- MOOLLM already has a `goal` skill

### For "Molecule" (Workflow)

**Primary recommendation: `procedure`**

| Why `procedure` | Benefit |
|-----------------|---------|
| Papert/Logo native | Deep constructionist lineage |
| Training presence | Massive — programming, math, medicine |
| Self-documenting | "Follow this procedure" |
| Hierarchical | Procedures can call procedures |

**Alternative: `frame`**

For structured templates with slots to fill, `frame` (from Minsky) works:
- Has fixed structure with variable slots
- Represents stereotyped situations
- Training data from AI/cognitive science

### For "Convoy" (Batch)

**Primary recommendation: `project`**

| Why `project` | Benefit |
|---------------|---------|
| Papert native | "Meaningful work with purpose" |
| Training presence | Massive — everywhere |
| Self-documenting | Everyone knows what a project is |
| Narrative | Has beginning, middle, end |

**Alternative: `queue`**

For strictly ordered work: `queue` (from Sims)

### For "Hook" (Assignment)

**Primary recommendation: `slot`**

| Why `slot` | Benefit |
|------------|---------|
| Self language native | Unified container concept |
| Training presence | High |
| Elegant | Can hold work or worker |
| Delegation-friendly | Empty slots delegate to parent |

---

## Part 8: The Complete Vocabulary Mapping

| Gas Town Term | MOOLLM Term | Source | Why Better |
|---------------|-------------|--------|------------|
| bead | **action** | Sims | Universal, self-documenting |
| molecule | **procedure** | Logo | Deep training, hierarchical |
| convoy | **project** | Papert | Meaningful work with purpose |
| hook | **slot** | Self | Unified, elegant |
| wisp | **ephemeral** | English | Standard adjective |
| polecat | **worker** | English | What it actually is |
| refinery | **merger** | Git | What it actually does |
| GUPP | *delete* | — | Useless acronym |
| MEOW | *delete* | — | Useless acronym |

---

## Part 9: Why This Matters

### Training Data Depth

| Term | Approximate Presence |
|------|---------------------|
| action | Billions of examples |
| goal | Billions of examples |
| procedure | Billions of examples |
| project | Billions of examples |
| bead | Near zero (in this context) |
| polecat | Near zero (means ferret) |
| convoy | Low (means vehicle group) |
| molecule | Low (means chemistry) |

### Intellectual Coherence

MOOLLM's vocabulary comes from a coherent tradition:

```
MIT AI Lab (1960s-80s)
├── Minsky → Society of Mind → K-lines, frames, goals
├── Papert → Logo → procedures, microworlds, bugs
└── Kay → Smalltalk → messages, methods, objects
    └── Self → slots, delegation, prototypes
        └── JavaScript (prototype inheritance)

Game Design (1990s-2000s)
├── Wright → The Sims → motives, advertisements, queues
└── MUD/MOO → rooms, verbs, properties

→ MOOLLM: actions, goals, procedures, slots, rooms, queues, k-lines
```

Every term has ancestors. Every term activates related knowledge. The vocabulary IS the architecture.

### Gas Town's Incoherence

```
Gas Town Vocabulary
├── Mad Max movie (1979)
├── Kubernetes (surface-level)
├── Invented acronyms (GUPP, MEOW)
└── Random animals (polecat, dogs)

No intellectual tradition. No training data. No coherence.
```

---

## Part 10: The GitHub Option — Maximum Integration

Wait. Why invent *anything* when GitHub's terms are:
1. **Massively trained** — Every developer knows them
2. **Already integrated** — `gh` CLI, git workflows, APIs
3. **Zero translation** — No explanation needed
4. **Tooling exists** — `gh issue create`, `gh pr merge`

### GitHub Terminology Mapping

| Gas Town | GitHub Native | Training Presence | Integration |
|----------|---------------|-------------------|-------------|
| bead | **issue** | **Massive** | `gh issue` |
| molecule | **workflow** | **Massive** | GitHub Actions |
| convoy | **milestone** | **High** | `gh milestone` |
| hook | **assignee** | **High** | `gh issue edit --assignee` |
| wisp | issue + label `ephemeral` | **High** | Labels are native |
| polecat | **assignee** (bot account) | **High** | Bot accounts are standard |
| refinery | **PR review** | **Massive** | `gh pr merge` |

### The Synergy

```yaml
# Instead of beads.jsonl, use GitHub Issues
gh issue create --title "Implement auth" --label "task"

# Instead of convoy, use Milestone
gh issue edit 123 --milestone "Sprint 1"

# Instead of molecule, use GitHub Actions workflow
# .github/workflows/task.yml

# Instead of hook, use assignee
gh issue edit 123 --assignee @worker-bot

# Tracking is automatic
gh issue list --milestone "Sprint 1" --state all
```

### Why This Is Better

| Aspect | Gas Town Beads | GitHub Issues |
|--------|----------------|---------------|
| Storage | Custom JSONL, shell-outs | GitHub's database |
| API | Custom `bd` CLI | Standard `gh` CLI |
| UI | None | GitHub web interface |
| Mobile | None | GitHub mobile app |
| Notifications | None | GitHub notifications |
| Permissions | Custom | GitHub permissions |
| Search | Grep JSONL | GitHub search |
| History | Git blame on JSONL | Issue timeline |
| Cross-repo | Manual | GitHub cross-references |
| Training data | Zero | **Billions of examples** |

### The Integration Pattern

```yaml
# MOOLLM can use GitHub as its work tracker natively

task:
  create: gh issue create --title "$title" --body "$body" --label "moollm-task"
  assign: gh issue edit $id --assignee "$worker"
  complete: gh issue close $id --comment "Completed: $summary"
  list: gh issue list --label "moollm-task" --state open
  
workflow:
  trigger: gh workflow run task.yml -f issue=$id
  
milestone:
  create: gh api repos/:owner/:repo/milestones -f title="$name"
  add: gh issue edit $id --milestone "$milestone"
```

### LLM Native Understanding

When you say "create an issue", Claude/GPT:
- Knows exactly what that means
- Knows the `gh` commands
- Knows the API structure
- Knows issue templates
- Knows labels, milestones, assignees
- Has seen billions of examples

When you say "create a bead", the LLM:
- Has no idea what you mean
- Needs extensive explanation
- Will hallucinate wrong patterns
- Costs tokens explaining

---

## Conclusion: Two Good Paths

### Path 1: GitHub Native (Maximum Integration)

Use GitHub's vocabulary directly:

| Concept | Term | Tool |
|---------|------|------|
| Unit of work | **issue** | `gh issue` |
| Workflow | **workflow** | GitHub Actions |
| Batch | **milestone** | `gh milestone` |
| Assignment | **assignee** | `gh issue edit` |
| Category | **label** | `gh label` |
| Completion | **close** | `gh issue close` |

**Pros:** Massive training data, zero explanation, full tooling, web UI, mobile, notifications, cross-repo, free.

**Cons:** Tied to GitHub specifically.

### Path 2: Constructionist Vocabulary (Maximum Meaning)

Use terms from Minsky/Papert/Kay/Wright:

| Concept | Term | Source |
|---------|------|--------|
| Unit of work | **action** | The Sims |
| Objective | **goal** | Minsky |
| Workflow | **procedure** | Papert |
| Batch | **project** | Papert |
| Container | **slot** | Self |
| Context | **room** | MOO |

**Pros:** Intellectually coherent, domain-independent, activates related concepts, beautiful.

**Cons:** Requires MOOLLM-specific tooling.

### Recommendation: Hybrid

Use **GitHub issues** as the persistence layer, but describe them using **constructionist semantics**:

```yaml
# The issue IS the action
# The milestone IS the project
# The workflow IS the procedure
# The label IS the k-line activation

action:
  storage: github-issue
  fields:
    goal: issue.title
    procedure: issue.body
    project: issue.milestone
    k-lines: issue.labels
    slot: issue.assignee
    complete_when: issue.state == "closed"
```

**Best of both worlds:**
- GitHub tooling for persistence and integration
- Constructionist vocabulary for semantics and documentation
- LLM understands both layers

**Gas Town's vocabulary is hostile to both LLMs and tools. MOOLLM can be native to both.**
