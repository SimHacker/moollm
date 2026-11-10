# Welcome, LambdaMOO Friends

*For Pavel Curtis and everyone who built, played in, or was inspired by the MOO tradition.*

---

## What Is This?

**MOOLLM** (MOO + LLM) is LambdaMOO plus The Sims, with an LLM as parser, runtime, and player.

- **Filesystem as database** — Directories are rooms. YAML files are objects.
- **Git as backing store** — History, branches, distributed reality. GitHub-as-MMORPG.
- **LLMs as everything** — Parser, runtime, players, eval(), and coherence engine.

**Repository:** https://github.com/SimHacker/moollm

---

## Why This Matters to MOO People

You already know these concepts. We're just translating them:

| MOO | MOOLLM |
|-----|--------|
| Object-oriented database | Git repos as backing store |
| Parent chains | Prototype directories (Self-style delegation) |
| Verbs | Methods declared in YAML, executed by LLM |
| Properties | YAML fields with jazzy comments |
| `$corified` names | Path variables (`$SKILLS`, `$KERNEL`, `$ADVENTURE`) |
| In-world programming | YAML Jazz + empathic templates |
| The MOO programming language | LLM-as-runtime (the LLM IS the interpreter) |
| LambdaCore | The `moollm/` repo itself |

---

## What's Different

### Empathic Links (No Parser Needed)

MOO had a two-word parser. MUDs had complex NLP. We have... nothing.

When someone says "the cat skill," the LLM knows they mean `skills/cat/` because context. No dispatch table. No verb matching. The LLM infers intent.

We call these **empathic links** — references that work because the LLM understands what you mean.

### Comments as Semantic Data (YAML Jazz)

In MOO, descriptions were strings. In MOOLLM, **comments carry operational meaning**:

```yaml
# The coatroom — where transformation happens
# Maurice guards the entrance, checking for proper attire
# The mirror reflects not faces but souls
name: "The Coatroom"
guardian: maurice.yml
atmosphere: liminal  # 0.7 was too harsh, 0.3 too welcoming
```

Those comments bias LLM interpretation. The tuning note on `atmosphere`? That's operational metadata. The LLM reads ALL of this.

### Advertisements (from The Sims)

Objects don't wait to be used — they **announce what's possible**.

```yaml
advertisements:
  PET-A-CAT:
    score: 80
    condition: "Cat is present and approachable"
```

When the LLM enters a room, it collects advertisements from all objects. Highest-scoring actions surface. New objects plug in without changing core logic.

This is how The Sims worked. We're applying it to LLM-native worlds.

### Dithering (Also from The Sims)

When selecting actions, don't always pick the highest-scoring option:

1. Collect all available actions
2. Score them by context  
3. Take top N (e.g., top 3)
4. **Pick randomly** from those

This "dithering" prevents robotic behavior and leaves room for player improvement.

---

## Entry Points

| What | Where |
|------|-------|
| **The repository** | https://github.com/SimHacker/moollm |
| **Full design overview** | [LEELA-MOOLLM-DEMO-TRANSCRIPT.md](LEELA-MOOLLM-DEMO-TRANSCRIPT.md) |
| **A working text adventure** | [examples/adventure-4/](../examples/adventure-4/) |
| **The addressing system** | [kernel/naming/](../kernel/naming/) |
| **Epic transcript: Palm incarnation** | [marathon-session.md](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) |
| **Lane Neverending slideshow** | [street/lane-neverending/slideshow/](../examples/adventure-4/street/lane-neverending/slideshow/) |

---

## Deep Dive: MOO Heritage Analysis

For the detailed technical comparison — how MOO's object model, addressing, scoping, and governance map to MOOLLM — see:

📁 **[MOO-HERITAGE.md](MOO-HERITAGE.md)**

That document covers:
- Object addressing across distributed systems
- `$corified` names → layered path variables
- Parent chains → prototype inheritance with modulation
- Cross-MOO networking → MooCo
- Security, ownership, privacy considerations
- Location-independent skills
- The "agents all the way down" architecture

---

## Questions We're Exploring

### From MOO's Social History

1. **Community Governance** — LambdaMOO's petition/ballot system, the Bungle affair, the "New Direction." How did it evolve? What would you do differently?

2. **Wizard Fatigue** — The New Direction came from wizard burnout. How do you think about sustainable community stewardship now?

3. **Toading and Soft Reverts** — In Git, we have `revert`. But what's the equivalent of "newting" (toad without the scar)? Soft undo vs. hard undo?

### From MOO's Architecture

4. **Non-Monolithic Design** — MOO was a single database. Git naturally solves distribution, but what about the *conceptual* architecture? How would you design MOO today for a world where the "database" is spread across many repos, many owners, many trust levels?

5. **Distributed MOO Systems** — SunNET, GNA-NET connected MOOs. What problems arose? What solutions worked? What areas of research were you exploring? We're building MooCo for multi-repo coordination and would love to learn from what you discovered.

6. **Modularity and Minimal Cores** — LambdaCore, JHCore, enCore took different approaches. What's essential vs. accidental? What would a truly minimal MOO core look like?

7. **The MOO Programming Language** — Strengths, weaknesses, lessons learned. Security, ownership, privacy, modularity. What would you keep? What would you redesign?

### From LLM Integration

8. **What Would You Build Today?** — If you were starting fresh with LLMs as the runtime, what would you keep? What would you throw away?

---

## The Lineage

```
Crowther & Woods → Colossal Cave (1976)
Trubshaw & Bartle → MUD (1978)
Stephen White → TinyMUCK, MOO (1990)
Pavel Curtis → LambdaMOO (1990)
David Ungar → Self (1987)
Will Wright → The Sims (2000)
Marvin Minsky → K-lines, Society of Mind (1980-1985)
    ↓
MOOLLM (2025)
```

You're in the direct line. Thank you for building something that's still inspiring 35 years later.

---

## Contact

**Don Hopkins**  
Amsterdam, February 2026  
https://donhopkins.medium.com/

---

*"The best way to understand something is to build it. The best way to build something is to play with it first."*
