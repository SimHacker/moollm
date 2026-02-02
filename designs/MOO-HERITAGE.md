# What MOOLLM Can Learn from MOO and LambdaMOO

> "Every object in the MOO is assigned a number, and may be referred to by this number, prefixed with a #, as well as its name when the user is in the object's presence. Administrators, also known as wizards, who can manage the MOO, and assign certain global names to these objects, which are prefixed with $, a process known as corifying."
> — Wikipedia, MOO

## The Core Problem: Addressing Across Distributed Repos

MOO used **object numbers** (#0, #1, #42) as universal addresses within a single persistent database. This worked brilliantly for a monolithic system but fails immediately in MOOLLM's distributed world:

- Multiple repos (moollm, central, customer repos)
- Multiple workspaces (Cursor, VS Code, Claude Code)
- Cross-repo references that must resolve consistently
- No central authority assigning numbers

MOOLLM's answer: **Paths are the universal address space**.

```
moollm://github/SimHacker/moollm/skills/adventure/CARD.yml
```

This is our equivalent of MOO's `#42` — but it works across repos, is human-readable, and maps cleanly to Git's native addressing, and allows additional namespaces besides github.

## MOO's Addressing Layers (and MOOLLM Equivalents)

### 1. Object Numbers (#42)

**MOO**: Every object gets a unique numeric ID. `#0` is the system object. `#1` is the root class.

**MOOLLM**: Paths replace numbers.
- System object → `kernel/` directory
- Root class → `skills/object/` (the ur-prototype)

**Why paths are better for us**:
- Numbers require a central allocator — impossible across repos
- Paths are self-documenting (`skills/cat/` vs `#7834`)
- Paths survive forks, merges, cross-repo references
- Git already provides content-addressable hashes if we need them

### 2. $Corified Names ($room, $player, $thing)

**MOO**: Wizards assign human-readable global names prefixed with `$`. These are stored in `#0` (the system object) and resolve to object numbers.

```
$room → #3
$player → #6  
$thing → #5
```

**MOOLLM**: Path variables serve this role.

```yaml
$SKILLS  → moollm/skills/
$KERNEL  → moollm/kernel/
$ADVENTURE → examples/adventure-4/  # runtime-bound
```

**Key difference**: MOO's `$` names are **globally unique** (one namespace). MOOLLM's `$` variables support **scoped layering** like Unix `$PATH`:

```yaml
$SKILLS:
  search_path:
    - ./skills/                    # Local repo first
    - moollm://github/SimHacker/moollm/skills/  # Core second
    - moollm://github/community/skills/         # Community third
```

First match wins. This enables **local override** of core skills.

### 3. Parent Chain (→ Root Class #1)

**MOO**: Every object has a parent. Inheritance follows the parent chain up to Root Class (#1).

```
my_cat → $animal → $thing → #1
```

**MOOLLM**: Prototype directories.

```
skills/cat/ → skills/animal/ → skills/character/ → skills/object/
```

The chain is encoded in each skill's `parents:` field — **plural**, because MOOLLM supports **multiple inheritance with modulation**:

```yaml
# skills/cat/CARD.yml — Simple list form
parents:
  - animal      # Primary prototype
  - pet         # Adds domestic behaviors
  - predator    # Hunting instincts
```

```yaml
# skills/linus-torvalds/CHARACTER.yml — Modulated inheritance
parents:

  # Primary personality sources
  - programmer:
      import: [technical-depth, code-review-style]
      modulate: "Finnish directness, no sugarcoating"
      
  - leader:
      import: [delegation, vision-setting]
      exclude: [corporate-speak, HR-friendly]
      modulate: "Benevolent dictator, not consensus-seeker"
      
  # Behavioral modifiers (like giving Linus coffee and a joint)
  - caffeine:                    # Morning Linus
      intensity: 0.8
      effect: "Sharp, impatient, productive"
      
  - mellowed:                    # Evening Linus  
      intensity: 0.3
      effect: "Reflective, philosophical, still blunt"
      
  # Pure K-line activations (no modulation, just activate)
  - finnish-culture
  - open-source-philosophy
  - kernel-development
```

This is like Python's module imports but for personality/behavior:

```python
# Python analogy
from minsky.marvin import k_lines, society_of_mind
from sims.wright import advertisements, needs_system
from self.ungar import prototype_delegation  # with modifications
```

The YAML equivalent:

```yaml
parents:
  - minsky:
      import: [k-lines, society-of-mind]
      note: "Memory as K-line activation, mind as agent society"
      
  - sims:
      import: [advertisements, needs]
      exclude: [isometric-graphics]  # We're text-based
      modulate: "Needs drive behavior, ads signal capability"
      
  - self:
      import: [prototype-delegation, slots]
      modulate: "Everything is slots and messages"
```

**Key insight**: Parents can be:
- **Simple K-lines** — just names that activate knowledge
- **Structured imports** — what to take, what to exclude
- **Modulated** — how to adjust the inherited behavior
- **Commented** — YAML Jazz style, the WHY matters

### 4. Presence-Based Naming

**MOO**: Objects can be referred to by name "when the user is in the object's presence."

```
> look at cat
(resolves "cat" to whatever cat object is in the room)
```

**MOOLLM**: **Empathic links** — the LLM resolves names by context.

When you say "the cat skill," the LLM knows you mean `skills/cat/` because:
- You're in a MOOLLM context
- The conversation is about skills
- There's only one `cat` skill

No formal resolver needed. **Context is the resolver.**

## Scoping: A Unified Model

MOOLLM needs multiple scoping mechanisms working together. Here's how they layer:

### Level 1: Local (Directory)

```yaml
./ROOM.yml           # This directory
./guards/entrance.js # Subdirectory
../pub/              # Sibling directory
```

Like **lexical scope** in programming — what's visible from where you stand.

### Level 2: Adventure (Runtime Context)

```yaml
$ADVENTURE/coatroom/     # Resolves to examples/adventure-4/coatroom/
$CHARACTERS/don-hopkins/ # $ADVENTURE/characters/don-hopkins/
$PUB/bar/               # $ADVENTURE/pub/bar/
```

Like **closure scope** — values bound at session start, captured in `startup.yml`.

### Level 3: Repository

```yaml
$REPO/skills/       # This repo's skills
$REPO/kernel/       # This repo's kernel
```

Like **module scope** — what's visible within one package.

### Level 4: Core (moollm:// namespace)

```yaml
moollm://github/SimHacker/moollm/skills/character/
moollm://github/SimHacker/moollm/kernel/constitution-core.md
```

Like **global scope** — the shared infrastructure all repos can reference.

### Level 5: External (Other Repos)

```yaml
moollm://github/customer/their-adventure/characters/
moollm://github/community/shared-animals/
```

Like **import scope** — explicit references to other packages.

### Level 6: Empathic (LLM-Inferred)

```
"the schema mechanism skill"
"Don's character"
"that room we were just in"
```

No formal syntax. **The LLM figures it out.** This is MOOLLM's superpower.

## The Self-Like Microcode of Pointers

Can we build all addressing from a small set of primitive operations?

### Primitive Operations

```yaml
primitives:

  resolve:
    signature: "resolve(path) → object"
    description: "Find object at path, traversing search paths"
    examples:
      - "resolve('$SKILLS/cat/') → skills/cat/"
      - "resolve('./guards/') → ./guards/"
    
  inherit:
    signature: "inherit(parents, modulations) → merged_prototype"
    description: "Merge multiple parents with modulation"
    examples:
      - "inherit([animal, pet, predator]) → merged traits"
      - "inherit({programmer: {import: [code-review], modulate: 'blunt'}}) → selective import"
    
  advertise:
    signature: "advertise(name, score) → advertisement"
    description: "Make capability discoverable with priority"
    example: "advertise('hunt_mouse', 0.9)"
    
  scope:
    signature: "scope(level) → namespace"
    description: "Return namespace at scoping level"
    levels: [local, adventure, repo, core, external]
    
  search:
    signature: "search(pattern, scopes) → [objects]"
    description: "Find all matching objects across scopes"
    example: "search('cat-*', [local, repo, core])"
```

### Everything Else Compiles Down

```yaml
# $SKILLS/cat/ compiles to:
resolve(
  search('cat', [
    scope('repo') + '/skills/',
    scope('core') + '/skills/'
  ])
)

# prototype: $SKILLS/animal/ compiles to:
inherit(resolve('$SKILLS/animal/'))

# "the cat skill" compiles to:
empathic_resolve('cat skill', context)
# → LLM infers: resolve('$SKILLS/cat/')
```

This is like Self's **slots and delegation** — everything reduces to:
- **Slots** = named references (paths)
- **Delegation** = prototype chain (inherit)
- **Messages** = resolution (resolve + advertise)

## Corifying in a Distributed Multi-Repo World

MOO's corifying: Wizards register global names in `#0`.

MOOLLM's equivalent: **The kernel is the shared core.**

```
moollm://github/SimHacker/moollm/kernel/  # The "$0" equivalent
moollm://github/SimHacker/moollm/skills/  # Corified skill namespace
```

### What Gets Corified?

| MOO | MOOLLM |
|-----|--------|
| `$room` | `$SKILLS/room/` |
| `$player` | `$SKILLS/character/` |
| `$thing` | `$SKILLS/object/` |
| `#0` system object | `kernel/` |
| `#1` root class | `skills/object/` |

### Local Corifying

Each repo can have its own "corified" names that shadow or extend the core:

```yaml
# In customer-repo/startup.yml
local_core:
  $SKILLS: 
    - ./skills/           # Local skills first
    - moollm://github/SimHacker/moollm/skills/  # Core fallback
  
  $ROOM: ./skills/room/   # Override core room skill
```

### Cross-Repo Corifying

MooCo (the planned MOOLLM orchestrator) could maintain a global registry:

```yaml
# mooco://registry/corified
$leela-cat: moollm://github/leela-ai/moollm/skills/cat/
$community-cat: moollm://github/community/skills/cat/
```

But this is **optional** — most resolution is local or empathic.

## Dithering for Object Selection

Connecting to The Sims' advertisement dithering (from the demo transcript):

When an LLM needs to choose which object/skill to use:

1. Collect all **advertisements** from available objects
2. Score them by relevance to current context
3. Take top N candidates
4. **Pick randomly** from top tier

This prevents robotic "always pick optimal" behavior and leaves room for discovery.

```yaml
# Pseudo-algorithm
candidates = search('*', [local, adventure, repo, core])
scored = candidates.map(c => [c, score(c, context)])
top_n = scored.sort_by_score().take(3)
selected = random_choice(top_n)  # Dithering!
```

## Summary: MOO → MOOLLM Translation

| MOO Concept | MOOLLM Equivalent |
|-------------|-------------------|
| Object numbers (#42) | File paths |
| $corified names | Path variables ($SKILLS, $ADVENTURE) |
| #0 system object | kernel/ directory |
| #1 root class | skills/object/ |
| Parent chain (single) | `parents:` list (multiple inheritance with modulation) |
| Presence-based naming | Empathic links (LLM context resolution) |
| Single database | Distributed repos |
| Wizards | Kernel maintainers |
| Toading/Newting | Git revert (softer!) |

## The Deeper Problem: Location-Independent Skills

The `$SKILLS` path variable is a step, but not enough. Real requirements:

### Skills Must Be Location-Independent

Skills can't be tied to a flat `skills/` directory:
- Skills need **subdirectory organization** (categories, domains)
- Skills can **contain sub-skills** in arbitrary nested structures  
- Skills need **symbolic names** that resolve to arbitrary paths
- The same skill might exist at different paths in different repos

This means: **skill name → path** must be a managed registry, not filesystem convention.

```yaml
# Symbolic skill registry (conceptual)
skills:
  adventure: 
    path: skills/adventure/
    why: "Text adventure framework, room/object/character architecture"
    triggers: [adventure, room, mud, moo, text game]
    
  cat:
    path: skills/animal/cat/           # Nested under animal/
    why: "Feline character behaviors"
    triggers: [cat, meow, feline, pet]
    
  fluxx-chaos:
    path: skills/experiment/experiments/fluxx-chaos/  # Deep nesting
    why: "Card game experiment framework"
    triggers: [fluxx, card game, chaos]
```

### $VARS as Prioritized Search Paths

Think of `$SKILLS` not as a single path but as a **search list** — like:
- Unix `$PATH` (prioritized directory search)
- Self's parent slots (delegation chain)
- Union/translucent filesystem mounts (overlay directories)

```yaml
$SKILLS:
  - ./skills/                              # Local repo (highest priority)
  - ./vendor/skills/                       # Vendored dependencies
  - moollm://github/SimHacker/moollm/skills/  # Core
  - moollm://github/community/shared-skills/   # Community
```

Resolution: walk the list, first match wins. Just like Self delegation.

### MooCo Orchestrator: Translucent Mounts

When running under MooCo, we can virtualize a **unified filesystem** that:
- **Layers** multiple repo sections over the same virtual path
- **Combines** skill directories from multiple sources
- Provides **translucent mounts** (changes write to top layer, reads merge all layers)

```
Virtual filesystem (MooCo view):
/skills/
  ├── adventure/      # from moollm core
  ├── cat/            # from moollm core
  ├── custom-cat/     # from local repo (shadows nothing, adds)
  └── adventure/      # from local repo (shadows core adventure/)
      └── custom-rooms/  # local extension
```

This is like Docker's layered filesystem, or Plan 9's union directories.

### Platform-Agnostic Degradation

Critical constraint: **MOOLLM must run on any platform** — Cursor, Claude Code, VS Code, bare terminal.

When MooCo isn't available, the system must degrade to:
1. **A skill INDEX file** that maps names → paths → descriptions
2. **Markdown over YAML** for the index (more compact, narrative relationships)
3. **Relative paths** that work in any checkout

```markdown
<!-- skills/INDEX.md — works without any runtime -->

## Core Skills

### adventure
**Path:** `./adventure/`  
**Triggers:** adventure, room, text game, MUD, MOO  
**Why:** Text adventure framework. Rooms are directories, objects are YAML.
Inherits from: simulation. Used by: any interactive fiction.

### character  
**Path:** `./character/`
**Triggers:** character, NPC, player, persona
**Why:** Base prototype for all characters. Personality, memory, dialogue.
Inherits from: object. Extended by: animal, person, fictional.

### cat → animal → character → object
**Path:** `./animal/cat/`
**Triggers:** cat, feline, meow, pet
**Why:** Feline behaviors. Hunting, sleeping, demanding attention.
The prototype chain shows inheritance.
```

This INDEX.md:
- Works as documentation (humans read it)
- Works as LLM context (compact, narrative)
- Lists activation triggers (when to load)
- Shows relationships (inherits from, extended by)
- Needs no runtime — just text

### The Two-Layer Architecture

```
┌─────────────────────────────────────────────┐
│  MooCo Orchestrator (when available)        │
│  - Translucent mounts                       │
│  - Real-time cross-repo resolution          │
│  - Caching, optimization                    │
│  - Multiplayer coordination                 │
└─────────────────────────────────────────────┘
            ▼ enhances, doesn't require
┌─────────────────────────────────────────────┐
│  Base MOOLLM (always works)                 │
│  - INDEX.md skill registry                  │
│  - Relative paths                           │
│  - LLM-based resolution                     │
│  - Works on any platform                    │
└─────────────────────────────────────────────┘
```

MooCo **optimizes** but doesn't **require**. The base layer always works.

## Open Questions

1. **Content addressing**: Should MOOLLM support git commit hashes as version pins?
   ```
   moollm://github/SimHacker/moollm@abc123/skills/cat/
   ```

2. **Empathic link caching**: Can we cache LLM-resolved references for performance?

3. **Cross-repo permissions**: How do we handle private repos? OAuth? Tokens?

4. **Conflict resolution**: When two repos define `skills/cat/`, which wins beyond search order?

5. **Live linking**: Can MooCo provide real-time cross-repo references like MOO's networked SunNET?

6. **INDEX format**: Markdown vs YAML for skill registries? MD is more compact for narrative relationships, YAML more structured for machine parsing. Hybrid?

7. **Skill containment**: When a skill contains sub-skills, how do we represent that in the registry? Nested entries? Path prefixes?

8. **Translucent mount semantics**: When layering repos, what happens on write? Always to top layer? Explicit layer selection?

## See Also

- `kernel/naming/URLS.yml` — moollm:// URI scheme
- `kernel/naming/NAMING-PATH-VARIABLES.yml` — $SKILLS, $ADVENTURE
- `kernel/naming/NAMING-K-LINES.yml` — Virtual parents, naming patterns
- `skills/advertisement/` — The Sims-style advertisement system
- `designs/LEELA-MOOLLM-DEMO-TRANSCRIPT.md` — Demo covering these concepts
