# MOOLLM: A Tour for Hackers

> **If you like taking things apart to see how they work, building things to understand them, or making systems do things they weren't supposed to — welcome.**

---

## What You're Looking At

MOOLLM treats the LLM as `eval()` for a microworld operating system.

That might sound abstract. Here's what it means concretely:

| Metaphor | Reality |
|----------|---------|
| The filesystem | is the world |
| Directories | are rooms |
| YAML files | are state |
| Walk around | by changing directories |
| Pick things up | by reading files |
| Change the world | by writing files |

Skills are programs. Characters are objects. The LLM runs them.

If you've ever:
- Written Lisp macros to extend the language
- Built MUDs/MOOs and watched players surprise you
- Made games where emergent behavior exceeded your simulation
- Argued about Minsky vs McCarthy vs Papert
- Believed that systems should be inspectable

...you'll recognize what we're doing here.

---

## The Core Hack: Speed of Light

Most "AI agent" systems work like carrier pigeons:

```
Agent A thinks → serialize → API call → wait 500ms →
  Agent B parses → thinks → serialize → API call → wait 500ms →
    Agent C parses → thinks → ...
```

Every boundary crossing: +latency, +noise, +cost, -coherence.

**MOOLLM runs multiple agents inside one LLM call.**

No serialization between them. No API round-trips. They share context. They interrupt each other. They riff. They argue.

We ran a 33-turn card game with 12 characters in one API call. Traditional approach: 33+ round-trips. [Read the transcript](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-day-2--speed-of-light-simulation).

[Full architectural argument](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md)

---

## Stop 1: The Skill Ecosystem

There are 117+ skills. Here are some categories:

### Introspection (Watch Yourself Think)

| Skill | What It Does |
|-------|--------------|
| [cursor-mirror](../skills/cursor-mirror/) | 59 commands to inspect Cursor's internals — what it read, what it thought, what tools it called |
| [skill-snitch](../skills/skill-snitch/) | Security audit for skills — static analysis + runtime surveillance |
| [thoughtful-commit](../skills/thoughtful-commit/) | Git commits that link to the reasoning that produced them |

cursor-mirror lets you watch the LLM's context assembly, tool calls, and thinking blocks. It's `strace` for AI.

### Constraints (What Not To Do)

```
no-ai-slop       no-ai-bias        no-ai-joking
no-ai-sycophancy no-ai-hedging     no-ai-gloss
no-ai-moralizing no-ai-ideology    no-ai-customer-service
no-ai-overlord   no-ai-soul
```

These don't DO anything — they PREVENT behaviors. Load them all and the output becomes stark, direct, honest. No corporate-speak. No hedging. No sycophancy.

### Simulation (Many Agents, One Mind)

| Skill | The Hack |
|-------|----------|
| [adversarial-committee](../skills/adversarial-committee/) | Multiple personas with incompatible values debate in real-time |
| [society-of-mind](../skills/society-of-mind/) | Minsky's architecture: intelligence as agent interactions |
| [speed-of-light](../skills/speed-of-light/) | The protocol for running many turns in one call |

Standard ChatGPT gives you the statistical center — the bland, inoffensive average. An adversarial committee gives you the *shape* of the opinion space.

---

## Stop 2: The Semantic Image Pyramid

How do you organize documentation for 121 skills without drowning in text?

**MOO-Maps**: multi-resolution reading, like MIP-maps for textures.

```
Level        Size        Question
─────────────────────────────────────────────────
👁️ GLANCE.yml   5-70 lines    "Is this relevant?"
📇 CARD.yml     50-200 lines  "What can it do?"
📜 SKILL.md     200-1000      "How does it work?"
📚 README.md    500+          "Why was it built?"
```

**The rule:** Never load a lower level without loading the level above first.

You can inject ALL glances into every prompt — they're tiny. CARD.yml gives you the interface. SKILL.md gives you the protocol. README.md is for deep context you rarely need.

---

## Stop 3: The Lineage

This isn't new. It's a synthesis:

| Tradition | What MOOLLM Takes |
|-----------|-------------------|
| **Adventure / Zork / LambdaMOO** | Filesystem as navigable space. Directories are rooms. |
| **Logo (Papert, 1980)** | Microworlds that teach by being explored. The turtle was just the beginning. |
| **Society of Mind (Minsky, 1986)** | K-lines: names as activation vectors. Many agents as one mind. |
| **Self (Ungar/Smith, 1987)** | Prototype-based inheritance. Objects as clones, not classes. |
| **The Sims (Wright, 2000)** | Object advertisements. Minimal simulation + player imagination = emergence. |
| **Constructionism (Papert/Resnick)** | Build to understand. Play first, formalize later. |

If you're from the MIT AI Lab tradition: **this is that, for LLMs.**

If you built MUDs: **this is that, with an LLM as the runtime.**

If you made games: **this is The Sims design philosophy applied to agents.**

---

## Stop 4: YAML Jazz

Why YAML instead of code?

Because comments aren't ignored — they're semantic.

```yaml
character:
  name: Marcus
  traits:
    - cynical           # but secretly wants to believe
    - well-read         # quotes obscure authors
    - protective        # of those he considers family
```

The LLM reads `# but secretly wants to believe` and acts accordingly. The comment IS part of the program.

This is **YAML Jazz**: structured data with semantic annotation. The model doesn't parse it — it *understands* it.

---

## Stop 5: Play-Learn-Lift

The methodology:

```
PLAY → Try things. Make mistakes. Explore freely.
  │     Low stakes. No spec. Just tinker.
  │
  ▼
LEARN → Notice patterns. What worked? What failed?
  │      Document for yourself.
  │
  ▼
LIFT → Share for others. Make it reusable.
       Turn your learning into a skill.
```

This is how MOOLLM grows. Someone plays with an idea. They notice a pattern. They lift it into a skill others can use.

The Confetti Crawler (an emoji-spraying "worm familiar") started as play. Failed repeatedly as prose instructions. Got lifted into a Python sister script. Now it's a reusable skill.

---

## Stop 6: Introspection

**cursor-mirror** is the German toilet of AI.

> *German toilets have a shelf. You can inspect what you've produced before flushing.*

Most AI systems are French toilets — thoughts disappear instantly. cursor-mirror lets you examine:

- What files did it read?
- What was it thinking? (reasoning blocks)
- What tools did it call?
- What context was assembled?

```bash
cursor-mirror timeline @1      # Full event sequence
cursor-mirror thinking @1      # Reasoning blocks
cursor-mirror context-sources @1  # What went into context
cursor-mirror tools @1 -v      # Every tool call
```

This is `strace` + `tcpdump` + `lsof` for LLMs.

---

## Stop 7: Trust and Security

**skill-snitch** audits skills:

- **Static analysis**: Patterns for secrets, exfiltration, dangerous ops
- **Runtime surveillance**: What did it *actually* do vs what it *declared*?
- **Trust tiers**: GREEN (core) → BLUE (verified) → YELLOW (community) → RED (dangerous)

The whole thing is [extensible via YAML](SKILL-SNITCH-EXTENSIBILITY.md):
- Add your own patterns for new threats
- Define surfaces (where to look)
- Write analyzers (behavioral rules)

It's Little Snitch for LLM agents.

---

## Getting Started

```bash
git clone https://github.com/SimHacker/moollm
cd moollm
cursor .
```

The `.cursorrules` and `.cursor/rules/` auto-load.

**Read in this order:**

1. `skills/INDEX.md` — 121 skills, narrative form
2. `skills/bootstrap/CARD.yml` — how sessions wake up
3. This document — you are here
4. `designs/SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md` — the core architectural argument

**Try something:**

```
"Invoke the adversarial-committee skill to debate whether MOOLLM is useful"
```

Watch what happens. Use cursor-mirror to see what it did.

---

## FAQ

**Q: Is this prompt engineering?**

Prompt engineering optimizes one prompt. MOOLLM creates a persistent microworld with state, inheritance, and composition. Skills call skills. Characters remember. Sessions build on sessions.

**Q: Is this just The Sims in text?**

Yes. The Sims proved: object advertisements + minimal simulation + player imagination = emergent behavior. We're applying that to LLM agents.

**Q: Why not just use MCP/function calling?**

MCP operates BETWEEN calls — carrier pigeons. MOOLLM operates DURING one call — speed of light. For multi-agent simulation, the difference is 33 round-trips vs 1.

**Q: Can I use this with Claude Code / other systems?**

MOOLLM is designed to be portable. The current implementation targets Cursor, but the architecture (skills as YAML + markdown, filesystem as world) works anywhere.

---

## Keep Exploring

| Where | What |
|-------|------|
| [skills/INDEX.md](../skills/INDEX.md) | All 121 skills |
| [examples/adventure-4/](../examples/adventure-4/) | A pub with characters, games, and cats |
| [skills/cursor-mirror/](../skills/cursor-mirror/) | Introspection tool |
| [designs/](.) | Architecture documents |
| [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) | Core argument |
| [SKILL-ECOSYSTEM.md](SKILL-ECOSYSTEM.md) | npm for skills |

---

*Skills are programs. The LLM is eval(). The filesystem is the world.*

*Welcome to the microworld.*
