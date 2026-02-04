# Structure and Interpretation of Community Programs

> **A tribute to SICP, teaching MOOLLM/YAML programming the way Abelson & Sussman taught Scheme.**

---

## Status: STUB

**TODO:** This is a placeholder for a future book/design document.

**Dream:** Ask Hal Abelson if he'd be interested in collaborating or advising.

---

## The Vision

SICP taught a generation how to think about computation through Scheme — not because Scheme was the point, but because it was a **minimal, elegant vehicle** for exploring ideas about abstraction, state, and interpretation.

MOOLLM could be that for a new generation — teaching how to think about **community, simulation, and emergent behavior** through YAML and markdown. Not because YAML is the point, but because it's a minimal, elegant vehicle for exploring ideas about:

- **Microworlds** as learning environments
- **Skills as programs** that compose and inherit
- **Characters as objects** with state, behavior, and relationships
- **Rooms as contexts** that shape what's possible
- **The LLM as eval()** — the interpreter that gives meaning to our programs

---

## Table of Contents

*Parallels SICP's structure but extends into community, simulation, and multi-object-system interpretation.*

### Foreword (Aspirational: Hal Abelson?)

### Preface: From Procedures to Communities

---

## Part I: Building Abstractions with Skills

### Chapter 1: The Elements of Skill Programming

1.1 Expressions and Naming
- YAML as data, YAML as code
- The skill directory as the unit of abstraction
- GLANCE.yml, CARD.yml, SKILL.md, README.md

1.2 Comments as Semantic Content
- YAML Jazz: comments the LLM reads
- `# gentle but firm` as executable specification
- The interpreter that understands intent

1.3 Evaluation and the Substitution Model
- The LLM as eval()
- Context window as environment
- Prompt + skills + state → response

1.4 Conditional Expressions and Advertisements
- The Sims-style "what can I do here?"
- Skill advertisements as conditional activation
- Score-based method selection

1.5 Black-Box Abstraction
- Skills as opaque units
- Interface (CARD.yml) vs implementation (SKILL.md)
- The semantic image pyramid as abstraction barrier

### Chapter 2: Skills and the Processes They Generate

2.1 Linear Skill Activation
- Single skill invocation
- Method dispatch
- State accumulation

2.2 Recursive Skill Composition
- Skills calling skills
- K-lines as activation vectors
- Transitive closure of skill networks

2.3 Tree Recursion and Deliberation
- Adversarial committee as branching deliberation
- Multiple voices, one context
- Ensemble inference

2.4 Orders of Growth
- Token economics
- Context window limits
- MOO-Maps as memoization

### Chapter 3: Formulating Abstractions with Higher-Order Skills

3.1 Skills as Arguments
- Passing skills to skills
- Meta-skills that operate on skills
- skill-snitch as higher-order auditor

3.2 Constructing Skills with Lambda
- Anonymous skill fragments
- Inline skill definitions
- The BOOP operator (Build Object On Prompt)

3.3 Skills as General Methods
- Templates and empathic generation
- Closures: skills capturing context
- Continuations: suspended skill states

3.4 Skills as Returned Values
- Skills that generate skills
- The Cosmic Dealer generating cards
- Dynamic personalized content as closure

---

## Part II: Building Abstractions with Data

### Chapter 4: Introduction to Character Abstraction

4.1 Characters as Data
- Traits, relationships, memories
- The CHARACTER.yml specification
- Abstraction barriers between character and behavior

4.2 Hierarchical Character Structures
- Relationships as graphs
- Social dynamics as data flow
- Bond strength affecting information sharing

4.3 Multiple Representations for Characters
- Lightweight vs incarnated characters
- Familiar characters as interface wrappers
- I-Beam as platform-agnostic persona

### Chapter 5: Symbolic Simulation

5.1 Quotation and Reference
- K-lines as symbolic pointers
- Saying "adversarial-committee" activates a constellation
- Names as semantic activation vectors

5.2 Symbolic Card Generation
- Cards as data structures
- Dynamic card creation as symbolic differentiation
- The Fluxx plugin architecture

5.3 Sets and Decks
- Deck as ordered set with state
- Shuffle, draw, discard operations
- Full state persistence in iteration files

### Chapter 6: Systems with Generic Operations

6.1 Generic Skill Dispatch
- Skills responding to multiple contexts
- Room-based polymorphism
- Character-appropriate behavior

6.2 Combining Skills
- Suite composition (no-ai-* suite)
- Ensemble composition (introspection suite)
- Stack composition (adventure stack)

6.3 The Cosmic Dealer Pattern
- Multi-objective optimization as generic operation
- Drama + fun + fairness + teaching
- Karma as symbolic algebra on moral debts

---

## Part III: Modularity, Objects, and State

### Chapter 7: Assignment and Local State

7.1 Local State Variables
- The `.moollm/` scratch space
- Session state vs persistent state
- Platform / Narrative / State tiers

7.2 The Benefits of State
- Characters that remember
- Games that evolve
- Karma ledgers that accumulate

7.3 The Costs of State
- Context window pressure
- State synchronization
- Append-only vs edit semantics

### Chapter 8: The Environment Model of Evaluation

8.1 Rooms as Environments
- Directory as activation context
- Inheriting room properties
- Ethical framing from context

8.2 Scoping and Delegation
- Skills inheriting from directories
- Character behavior shaped by room
- Prototype chains

8.3 Multiple Interlocking Object Systems
- Self: prototype-based inheritance
- ScriptX/CLOS: generic functions
- Shell scripting: $PATH as method resolution (Densmore/Rosenthal)
- NeWS: PostScript object system
- Smalltalk: message passing
- COM IUnknown: interface discovery
- OLE IDispatch: late binding

### Chapter 9: Streams and Infinite Structures

9.1 Speed of Light as Stream Processing
- Many turns as lazy evaluation
- One API call, unbounded turns
- State snapshots as stream elements

9.2 Iteration Files as Materialized Streams
- `fluxx-run-000.yml`, `-001.yml`, `-002.yml`...
- Replayable, forkable, auditable
- Time travel through state history

9.3 Delayed Evaluation
- Dealer "holding" cards for later
- Karma as deferred consequence
- Continuations as suspended game state

---

## Part IV: Metalinguistic Abstraction

### Chapter 10: The Metacircular Evaluator

10.1 The LLM as Eval
- Divine acting: omniscient simulating limited
- Constitutional role-fidelity
- The shared context window as environment

10.2 Separating Syntax from Semantics
- YAML as syntax
- Intent as semantics
- Comments carrying meaning

10.3 The Cosmic Interpreter
- How skills are "executed"
- Prompt assembly as linking
- Response as return value

### Chapter 11: Plugin Architectures

11.1 Fluxx as Extensible Substrate
- Base rules as core language
- Expansion packs as plugins
- Dynamic rule modification

11.2 Extension Points
- Dealer plugins (Cosmic, Karma, Tutor)
- Card generator plugins
- Rule modifier plugins

11.3 Cards as Closures
- Cards capturing game state
- Personalized cards as closures over relationships
- Playing a card as invoking a continuation

### Chapter 12: Lazy Evaluation and Thunks

12.1 The BOOP Operator
- Build Object On Prompt
- Lazy instantiation of characters
- Just-in-time skill compilation

12.2 Memoization via MOO-Maps
- GLANCE.yml as cached summary
- Progressive loading based on need
- Token-efficient skill access

---

## Part V: Computing with Context Machines

### Chapter 13: The Architecture of the Context Window

13.1 Registers and Operations
- Input, output, skills, state
- Token budgets
- Attention as addressing

13.2 The Instruction Sequence
- Prompt assembly order
- Priority and recency
- Advisory files (hot.yml, working-set.yml)

### Chapter 14: Compilation and Optimization

14.1 cursor-mirror as Profiler
- Watching yourself think
- Tool call traces
- Context assembly analysis

14.2 Play-Learn-Lift as JIT
- Exploration → pattern → crystallization
- Frequently-used patterns → optimized skills
- Programming by demonstration via cursor-mirror

14.3 Polymorphic Inline Caching for Skills
- Self-style optimization
- Skill dispatch optimization
- Hot paths through skill networks

### Chapter 15: Community and Emergence

15.1 The Simulator Effect
- Minimal simulation + imagination = emergence
- The Sims design philosophy
- Players doing the heavy lifting

15.2 Structure and Interpretation of Community Programs
- Communities as programs
- Social dynamics as computation
- Shared meaning-making as evaluation

15.3 The Black Hole Attractor
- Where this architecture naturally goes
- Optimization horizons
- The deep structure we're discovering

---

## Appendices

### Appendix A: The Object System Lineage

| System | Key Pattern | MOOLLM Parallel |
|--------|-------------|-----------------|
| **Self** | Prototype delegation | Skills as prototypes |
| **ScriptX/CLOS** | Generic functions | Multi-method dispatch |
| **Shell/$PATH** | Directory-based resolution | Room as context |
| **NeWS** | PostScript objects | Executable data |
| **Smalltalk** | Message passing | Method invocation |
| **COM IUnknown** | Interface discovery | CARD.yml sniffing |
| **OLE IDispatch** | Late binding | Dynamic skill loading |

### Appendix B: The Densmore-Rosenthal Patent

The shell's `$PATH` as a method resolution order — directories searched in sequence until a matching executable is found. In MOOLLM: rooms searched in sequence until a matching skill/method is found.

### Appendix C: Harper's Numbers and Analytics

Metrics for evaluating simulation quality, character fidelity, dramatic arc, teaching effectiveness.

---

## Acknowledgments (Aspirational)

- **Hal Abelson & Gerald Jay Sussman** — For SICP, which shaped how generations think about computation
- **Seymour Papert** — For Logo and constructionism
- **Marvin Minsky** — For Society of Mind and K-lines
- **Will Wright** — For The Sims and the simulator effect
- **David Ungar & Randall B. Smith** — For Self and prototype-based inheritance
- **John Densmore & Larry Rosenthal** — For the $PATH insight
- **James Gosling & David S.H. Rosenthal** — For NeWS
- **Alan Kay & the Smalltalk team** — For message passing and live objects

---

## Contact

If Hal Abelson (or anyone from the SICP tradition) reads this and is interested in discussing, please reach out.

This is a love letter to SICP. We'd be honored to have guidance.

---

*"Programs must be written for people to read, and only incidentally for machines to execute."*
— Abelson & Sussman, SICP

*"Skills must be written for minds to understand, and only incidentally for LLMs to interpret."*
— MOOLLM

*"Communities must be written for humans to inhabit, and only incidentally for simulations to animate."*
— SICP-MOOLLM
