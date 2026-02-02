# Letter to Pavel Curtis

**To:** Pavel Curtis (LambdaMOO creator, Xerox PARC alumnus)  
**From:** Don Hopkins  
**Subject:** MOO's Ideas Live On — Object Addressing in the Age of LLMs

---

Dear Pavel,

I've been thinking about LambdaMOO for decades, and I finally built the thing I kept trying to build on top of it.

## The Short Version

I created **MOOLLM** (MOO + LLM) — a framework where:
- The **filesystem** is the MOO database
- **Directories** are rooms
- **YAML files** are objects with verbs (code) and properties (data)
- **LLMs** are the parser, the runtime, AND the players

It's what would happen if LambdaMOO, The Sims, and Claude had a baby. Open source: https://github.com/SimHacker/moollm

## The Long Version: What MOO Got Right

I've been re-reading the MOO documentation and Wikipedia, and I'm struck by how much you anticipated. Here's what I'm building on:

### 1. Object Numbers vs. Paths

MOO's `#42` addressing was brilliant for a monolithic database. But it breaks across distributed repos. MOOLLM's equivalent:

```
moollm://github/SimHacker/moollm/skills/adventure/CARD.yml
```

Human-readable, Git-native, works across any number of repos. The "object number" is the path.

### 2. $Corified Names

Your `$room`, `$player`, `$thing` global names — we call them **path variables**:

```yaml
$SKILLS  → moollm/skills/
$KERNEL  → moollm/kernel/
$ADVENTURE → examples/adventure-4/  # Runtime-bound, like a closure
```

But here's where it gets interesting: MOOLLM supports **layered search paths** like Unix `$PATH`:

```yaml
$SKILLS:
  search_path:
    - ./skills/           # Local repo first
    - moollm://github/SimHacker/moollm/skills/  # Core fallback
```

Local skills can override core skills. First match wins.

### 3. Parent Chains

MOO's parent chain (`my_cat → $animal → $thing → #1`) maps directly to prototype directories:

```
skills/cat/ → skills/animal/ → skills/character/ → skills/object/
```

Each skill has a `prototype:` field pointing to its parent. Same inheritance model, filesystem-native.

### 4. The System Object (#0)

Your `#0` managed global names, connections, and system state. MOOLLM's equivalent is the `kernel/` directory:

```
kernel/
├── constitution-core.md      # Operating principles
├── naming/                   # Addressing protocols
│   ├── NAMING.yml
│   ├── NAMING-K-LINES.yml
│   └── URLS.yml              # moollm:// URI scheme
├── drivers/                  # Platform-specific behavior
│   ├── cursor.yml
│   └── claude-code.yml
└── memory-management-protocol.md
```

### 5. In-World Programming

MOO let users program verbs inside the world. MOOLLM does this with:
- **YAML Jazz** — Richly commented YAML that LLMs can parse AND understand
- **Empathic Templates** — LLM-evaluated template expressions
- **JavaScript Guards** — Compile-time room scripts for the web

## What We've Discovered

### Empathic Links (Beyond Parsers)

MOO had a two-word parser. MUDs had more complex NLP. But here's what LLMs enable:

When a user says "the cat skill," the LLM knows they mean `skills/cat/` because context. No registration. No dispatch table. The LLM infers intent.

We call these **empathic links** — references that only work because the LLM understands what you mean.

### Comments as Semantic Data

In MOO, descriptions were strings. In MOOLLM, **comments carry meaning**:

```yaml
# The coatroom — where transformation happens
# Maurice guards the entrance, checking for proper attire
# The mirror reflects not faces but souls
name: "The Coatroom"
guardian: maurice.yml
atmosphere: liminal  # 0.7 was too harsh, 0.3 too welcoming
```

Those comments bias LLM interpretation. The atmosphere comment with the tuning note? That's operational metadata. YAML Jazz.

### Dithering (from The Sims)

Will Wright's Sims team discovered that when selecting actions, you shouldn't always pick the highest-scoring option. Instead:

1. Collect all available actions
2. Score them by context
3. Take top N (e.g., top 3)
4. **Pick randomly** from those

This "dithering" prevents robotic behavior and leaves room for player improvement. We use the same principle for skill selection.

## Questions I'd Love Your Perspective On

1. **MOO's Social Architecture**: LambdaMOO's petition/ballot system and the Bungle affair — how did community governance evolve? MOOLLM needs thinking about distributed permissions across repos.

2. **Toading and Soft Reverts**: In Git, we have `revert` instead of `toad`. But what's the equivalent of "newting" (toad without the scar)? Soft undo vs. hard undo?

3. **Cross-MOO Networking**: You had SunNET and GNA-NET for inter-MOO communication. We're building **MooCo** as a multiplayer MOOLLM coordinator. What worked and what didn't in the networking experiments?

4. **Wizard Fatigue**: The "New Direction" came from wizard burnout. How do you think about sustainable community stewardship now?

5. **The Core Database Concept**: LambdaCore, JHCore, enCore — different starting points. How did you think about what belongs in core vs. what's user-space?

6. **Location-Independent Objects**: In MOO, objects lived at fixed `#` addresses. But what if objects need to be **location-independent** — addressable by symbolic name, resolvable through a search path? Skills in MOOLLM can be nested arbitrarily deep, organized in categories, containing sub-skills. The path shouldn't matter — only the name and what triggers its activation.

7. **Translucent/Union Filesystems**: We're thinking about MooCo virtualizing a **layered filesystem** — multiple repos overlaid on the same virtual paths, like Plan 9 union directories or Docker layers. Did MOO ever explore anything like federated object spaces where the "same" object could have different implementations depending on context?

8. **The Two-Layer Architecture**: MOOLLM needs to run on any platform (Cursor, VS Code, Claude Code, bare terminal) without special runtime. But MooCo can **optimize** when available — caching, translucent mounts, real-time cross-repo resolution. How do you think about "enhanced but not required" runtime layers?

9. **Registry vs. Convention**: MOO used `$corified` names registered in `#0`. But what if the registry is just a **text file** (INDEX.md) that maps skill names → paths → activation triggers? Markdown turns out to be more compact than YAML for narrating relationships between skills. The LLM reads the index, understands when to activate what. No special runtime needed.

## The Heritage

I wrote a design document tracing what MOOLLM inherits from MOO: `designs/MOO-HERITAGE.md`

The genealogy:
- **Crowther & Woods** → Colossal Cave (1976)
- **Trubshaw & Bartle** → MUD (1978)
- **Stephen White** → TinyMUCK, MOO (1990)
- **Pavel Curtis** → LambdaMOO (1990)
- **Will Wright** → The Sims (2000)
- **David Ungar** → Self (1987)
- **Marvin Minsky** → K-lines (1980)
- **Now** → MOOLLM (2025)

You're in the direct line. Thank you for building something that's still inspiring 35 years later.

## Want to Explore?

The repo: https://github.com/SimHacker/moollm

Interesting starting points:
- `kernel/naming/URLS.yml` — The moollm:// URI scheme
- `designs/MOO-HERITAGE.md` — What we learned from MOO
- `examples/adventure-4/` — A working text adventure
- `skills/` — The skill prototype hierarchy

I'd love to hear what you think. The ideas you put into MOO are still bearing fruit.

Best,

**Don Hopkins**  
Amsterdam, February 2026

---

## Background Links

- MOOLLM Repository: https://github.com/SimHacker/moollm
- MOO Heritage Analysis: https://github.com/SimHacker/moollm/blob/main/designs/MOO-HERITAGE.md
- Original MOO Wikipedia: https://en.wikipedia.org/wiki/MOO
- LambdaMOO Wikipedia: https://en.wikipedia.org/wiki/LambdaMOO
- My Medium: https://donhopkins.medium.com/

## Topics to Discuss

- Object addressing across distributed systems
- $corified names → layered path variables (like $PATH, like Self parent slots)
- Parent chains → prototype inheritance
- Wizards → kernel maintainers
- In-world programming → YAML Jazz + LLM evaluation
- Toading → Git revert (softer!)
- Cross-MOO networking → MooCo
- The social architecture experiments
- Location-independent skills (symbolic name → arbitrary path)
- Translucent/union filesystem mounts for multi-repo layering
- The "enhanced but not required" runtime architecture
- INDEX.md as skill registry (compact markdown over verbose YAML)
- What you'd do differently if you built it today
