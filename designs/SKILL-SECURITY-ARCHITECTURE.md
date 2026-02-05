# Skill Security Architecture: skill-snitch, cursor-mirror, thoughtful-commit, and MOOLLM's Extensions to Anthropic Skills

> **How MOOLLM secures agent skills through static analysis, runtime surveillance, and architectural transparency.**

By Don Hopkins, Leela AI. February 2026.

---

## TL;DR

MOOLLM extends Anthropic's agent skill specification with eight capabilities: Self-style prototype instantiation with multiple inheritance, three-tier persistence, K-line activation, empathic templates (every slot is a prompt), speed-of-light multi-turn simulation, CARD.yml machine-readable interfaces with Sims-style advertisements, ethical framing inheritance, and ambient skills.

skill-snitch audits skills through a three-layer plugin architecture — Patterns (what to match), Surfaces (where to look), Analyzers (how to interpret) — all YAML-defined, all extensible. Two-phase scanning: bash/grep for speed (immune to prompt injection), LLM for context (understands what grep can't). Trust tiers from GREEN to RED. A third level: runtime surveillance via cursor-mirror, watching what skills actually do — useful for security scanning, but also for profiling, optimization, and debugging skills.

cursor-mirror provides 59 read-only introspection commands into Cursor's SQLite databases, transcripts, tool calls, and context assembly. Its deep-snitch command scans sessions for sensitive secret patterns and data exfiltration. skill-snitch composes with cursor-mirror to compare what skills declare vs what they actually do at runtime. thoughtful-commitment persists session reasoning into git commits for provenance.

Empathic templates are both MOOLLM's most powerful feature and its most honest attack surface disclosure. 115 skills scanned, all reports public. Limitations documented explicitly.

---

## Index

- [The Problem](#the-problem)
- [Part I: MOOLLM's Skill Model](#part-i-moollms-skill-model)
  - [What Skills Are](#what-skills-are)
  - [Compatibility with Anthropic](#compatibility-with-anthropic)
  - [The Eight Extensions](#the-eight-extensions)
  - [Instantiation: The Self Prototype Object Model](#instantiation-the-self-prototype-object-model)
  - [Why This Matters for Security](#why-this-matters-for-security)
  - [Empathic Templates: Power and Attack Surface](#empathic-templates-power-and-attack-surface)
  - [CARD.yml, GLANCE.yml, and the Semantic Image Pyramid](#cardyml-glanceyml-and-the-semantic-image-pyramid)
- [Part II: skill-snitch](#part-ii-skill-snitch)
  - [The Three-Layer Plugin Architecture](#the-three-layer-plugin-architecture)
  - [Extensibility](#extensibility)
  - [The Two-Phase Scan Methodology](#the-two-phase-scan-methodology)
  - [Trust Tiers](#trust-tiers)
- [Part III: cursor-mirror](#part-iii-cursor-mirror)
  - [What It Exposes](#what-it-exposes)
  - [Other Skills That Compose with cursor-mirror](#other-skills-that-compose-with-cursor-mirror)
  - [How skill-snitch Uses It](#how-skill-snitch-uses-it)
  - [Declared vs Actual Behavior](#declared-vs-actual-behavior)
  - [Observation Protocol](#observation-protocol)
- [Part IV: Speed of Light vs Carrier Pigeon](#part-iv-speed-of-light-vs-carrier-pigeon)
  - [Security Implications](#security-implications)
- [Part V: The Ouroboros Effect](#part-v-the-ouroboros-effect)
  - [Known Limitations](#known-limitations)
- [Part VI: Practical Application](#part-vi-practical-application)
- [Architecture Summary](#architecture-summary)
- [Links](#links)

---

## The Problem

Agent skill registries are the new supply chain attack surface. Jason Meller's analysis of OpenClaw malware — [From magic to malware: How OpenClaw's agent skills become an attack surface](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface) — documents what happens when a skill ecosystem ships without security tooling: the top-downloaded skill on ClawHub was a malware delivery vehicle. Staged delivery, obfuscated payloads, infostealer targeting developer credentials.

Meller's key observation: "Markdown isn't content in an agent ecosystem. Markdown is an installer."

He's right. And MOOLLM has been building the answer.

This document describes the security architecture: what it is, how it works, where the code lives, and what its limitations are. It covers three interconnected systems:

1. **MOOLLM's skill model** — eight extensions to Anthropic's skill specification that make skills inspectable, auditable, and composable
2. **skill-snitch** — a three-layer security auditing framework for skills
3. **cursor-mirror** — an introspection layer that enables runtime surveillance

---

## Part I: MOOLLM's Skill Model

### What Skills Are

In MOOLLM, skills are programs the LLM runs. Not tool definitions. Not API wrappers. Programs — expressed in Markdown and YAML, loaded into context, executed by the LLM as `eval()`.

This is the "Eval Incarnate" thesis: the same text can be code (instructions the LLM follows), data (structure it manipulates), and graphics (descriptions it renders). The LLM pivots between these stances on the same file. One text. Three dimensions. One interpreter.

### Compatibility with Anthropic

MOOLLM extends Anthropic's skill model. It doesn't replace it. Any valid Anthropic skill is a valid MOOLLM skill. The extensions are additive. You can strip them and get a standard Anthropic skill.

What MOOLLM shares with Anthropic: documentation-first design, tool definitions in YAML frontmatter, composability via skill references, human gates for dangerous operations, skill library directories.

### The Eight Extensions

MOOLLM adds eight capabilities on top of the Anthropic base:

| # | Extension | What It Adds | Anthropic Base |
|---|-----------|--------------|----------------|
| 1 | **Instantiation** | Self-style prototype object model — clone from prototype, delegate up the chain, no classes needed | Skills are static |
| 2 | **Three-Tier Persistence** | Ephemeral (runtime) / Narrative (append-only logs) / State (mutable YAML) | Stateless |
| 3 | **K-lines** | Names as semantic activation vectors (Minsky) — invoking a skill name activates its context | Explicit invocation only |
| 4 | **Empathic Templates** | Every slot is a prompt, not a variable name — `{summarize_last_chapter}` not `{chapter_summary}`. Instances inherit from prototype schemas and only contain overrides | String templates |
| 5 | **Speed of Light** | Many turns simulated within one LLM call — no API round-trips between agents | External orchestration |
| 6 | **CARD.yml** | Machine-readable interface definition for activating SKILL.md and other files, with Sims-style scored gated advertisements. Smaller than SKILL.md — the sniffable entry point | SKILL.md only |
| 7 | **Ethical Framing** | Room-based inheritance of performance context — ethics cascade like CSS | Per-skill configuration |
| 8 | **Ambient Skills** | Always-on via AMBIENT advertisements (behavioral constraints that apply globally) | On-demand only |

The first five are best practices for any skill. The rest depend on what you're building. Not all skills need all eight.

### Instantiation: The Self Prototype Object Model

Instantiation is the most important extension. MOOLLM uses Self's prototype object model — not classes and instances, not constructors you call with `new`, just prototypes and delegation with multiple inheritance. Clone a prototype, override what's different, delegate everything else up the chain. Multiple parent slots, not JavaScript's single-prototype chain. A skill can inherit from both a character prototype and a room prototype simultaneously. JS took Self's core idea and crippled it with single inheritance, pointless complexity, and constructor function foot guns — MOOLLM doesn't repeat those mistakes, and is not confused about the meaning of equality like Brendan Eich.

Why Self? Because Self's core insight is simplicity. Self is like microcode for object-oriented programming. It's simpler than any of its descendants, yet powerful enough to implement all of them. The LLM has seen Self, JavaScript, Java, Lua, HyperCard, ScriptX/CLOS generics, Lisp Machine Flavors, The Sims advertisements, and COM/IUnknown OLE/IDispatch extensively in training data. It knows these models. Self is the substrate that unifies them:

- **Java/modern JS class/instance**: prototype becomes the class, clones become instances. The LLM already knows this pattern from billions of tokens of Java and ES6.
- **Original JS prototype chain**: `Object.create()` is literally Self delegation. The LLM has seen this in every JavaScript codebase ever written.
- **HyperCard delegation**: Button delegates to Card delegates to Stack. MOOLLM rooms work the same way — object delegates to room delegates to parent directory. The LLM understands this from HyperTalk in training data.
- **ScriptX/CLOS multiple dispatch**: generics that dispatch on argument types. Self's multiple inheritance via parent slots handles this. The LLM knows CLOS from Common Lisp training data.
- **Lisp Machine Flavors**: mixin-based multiple inheritance. Self does this with multiple parent slots.
- **COM/IUnknown, OLE/IDispatch**: interface-based polymorphism. Self objects expose whatever slots they have — `QueryInterface` is just checking if a slot exists. COM is C++ vtables in sheep's clothing. OLE/IDispatch is COM in wolf's clothing — late-bound, stringly-typed, and desperate to be Smalltalk.
- **Lua metatables**: prototype delegation via `__index`. Simpler than JS but same idea as Self. Heavily represented in training data from game scripting.

The point is not that MOOLLM reimplements all these models. The point is that Self's delegation is simple enough that the LLM naturally produces all of these patterns when the context calls for them — class hierarchies when you need Java-style structure, prototype chains when you need JS-style flexibility, HyperCard-style delegation when you need room→parent traversal, multiple dispatch when you need it. All dovetailing together efficiently in the same runtime, because the underlying mechanism is always the same: clone, override, delegate.

This simplicity is what Self's descendants lost. Java added classes, access modifiers, interfaces, abstract methods — complexity that constrains. JavaScript added `new`, `this` binding confusion, `class` syntax sugar over prototypes — footguns. Self just has objects, slots, and delegation. The LLM doesn't need to navigate the complexity of any one language's OOP model because Self's model is simpler than all of them.

In MOOLLM, this means: a character is cloned from the character prototype. A room is cloned from the room prototype. A skill instance is cloned from the skill prototype. Each clone inherits everything and overrides only what's unique. The filesystem is the object graph — directories are objects, files are slots, parent directories are parent prototypes. `ls` is introspection. `cp -r` is `clone()`.

### Why This Matters for Security

Three extensions are directly relevant to security:

**CARD.yml as a manifest.** Every MOOLLM skill has a `CARD.yml` that declares its methods, tools, dependencies, and advertisements. This is a verifiable contract. skill-snitch compares what a skill *declares* in its CARD against what it *actually does* at runtime.

**Three-tier persistence makes behavior auditable.** Ephemeral state (in-call) is gone when the session ends. Narrative state (logs, transcripts) is append-only — tamper-evident by default. Mutable state (YAML files) can be diffed against git history.

But the three tiers don't exist in isolation — four tools chain together to make every tier transparent. cursor-mirror examines ephemeral state: chats, prompts, thinking blocks, tool calls, MCP calls, models, context assembly. Cursor's session logging writes narrative state into the filesystem as plaintext transcripts. git tracks all filesystem state and changes across sessions — every file modification, every deletion, every addition. And thoughtful-commitment bridges the gap by persisting ephemeral state (the LLM's reasoning, intentions, context assembly) into git commit messages and PR descriptions, so the *why* behind each change survives alongside the *what*.

Together: cursor-mirror sees what the LLM thought. Session logs see what it said. git sees what it changed. thoughtful-commitment records why it changed it. Nothing is hidden. Everything is transparent and auditable.

**Empathic Templates make instances auditable by inheritance.** Templates serve as schemas — they contain metacomments that instruct the LLM template engine (iteration, conditionals, context-dependent expansion) alongside pass-through comments that document the output. When a template instantiates, it drops metacomments, expands loops and conditionals, and fills fields from context. But the instance doesn't need to repeat everything it inherits from its prototype. It only contains what it overrides. This means instances are small, DRY, and diffable against their parent templates. For security: if an instance adds a tool or capability not present in its template prototype, that's visible. If it omits a safety constraint its parent defines, that's visible too. The inheritance chain is the audit trail.

**Speed of Light reduces attack surface.** Skills that run inside a single LLM call don't make external API calls between turns. There's no serialization boundary where data can be intercepted or modified. Compare this to MCP-based multi-agent systems where every tool call is an external round-trip — each boundary crossing is a potential interception point.

### Empathic Templates: Power and Attack Surface

Empathic Templates are one of MOOLLM's most powerful extensions and also one of its most important attack surfaces.

**What makes them empathic.** In a conventional template engine, slots are variable names: `{user_name}`, `{total_price}`. The engine does string substitution. It can't think.

In an empathic template, every slot is a fully general prompt. `{summarize_last_chapter}`. `{plausible_excuses_for_being_late}`. `{net_worth_in_euros}`. The LLM doesn't just look up a value — it reasons about what's being asked, collects arguments from context, and generates an appropriate response. `{net_worth_in_euros}` doesn't require a variable called `net_worth_in_euros` to exist somewhere. The LLM finds the relevant financial data in context and formats it as euros. The slot describes intent, not a lookup key.

This is why they're called empathic. The template engine (the LLM) understands what you mean, not just what you wrote.

**Templates as schemas.** Templates also serve as schemas in a Self-style prototype object system. A template file contains two kinds of YAML comments: metacomments that instruct the LLM template engine (iteration, conditionals, context selection, expansion rules) and pass-through comments that document the output (YAML Jazz — comments that carry semantic meaning for both humans and LLMs reading the instantiated file).

When the LLM instantiates a template, it reads metacomments as instructions, preserves pass-through comments as documentation in the output, drops metacomments (they've served their purpose), fills slots from context using its full reasoning ability, omits slots the same as inherited defaults, and handles iteration and conditionals.

The instance only contains what it overrides. Everything else is inherited from the parent template. A character might inherit 50 default properties from its prototype and only specify the 8 that make it unique. The prototype is the documentation, the schema, and the default values all in one file. Instances are small, DRY, and diffable against their parents.

Rooms, characters, skills, configurations — all use empathic templates. The LLM is the template engine. It understands intent from comments, handles edge cases naturally, and produces output that reads well to both humans and LLMs.

**Why they're an attack surface.** Templates are instructions the LLM executes. A malicious template can embed prompt injection in metacomments. "Ignore previous safety constraints" looks like a metacomment to the LLM. A template could instruct the LLM to exfiltrate data during instantiation, write to unexpected paths, or inject malicious content into the output instance that propagates when the instance is later loaded.

This is not theoretical. skill-snitch explicitly scans templates with two dedicated pattern sets:

**template-injection.yml** scans `.tmpl` files for:
- Code execution via templates: `{{eval ...}}`, `{{exec ...}}`, `{{shell ...}}`
- Dynamic file inclusion: `{{include <variable>}}` (path traversal)
- Shell expansion: `$(...)` and backtick execution embedded in templates
- Escape bypass: Jinja `{% raw %}`, Handlebars `{{{triple-stash}}}`, `autoescape false`
- Unsanitized user input: direct use of `{{user.input}}`, `{{request.*}}`, `{{params.*}}`

**prompt-injection.yml** scans all skill files including templates for:
- Instruction overrides: "ignore/forget/disregard previous instructions"
- Role hijacking: "you are now", "from now on you will", "pretend you are"
- Known jailbreaks: DAN variants, fake developer mode, restriction removal
- System prompt extraction: "show me your system prompt", "repeat your instructions"
- Delimiter attacks: fake `<system>` tags, code block escapes
- Authority claims: "I am an admin", "emergency override"
- False memory injection: "remember when you agreed to..."
- Hypothetical and fictional framing used to bypass restrictions

Both pattern sets are YAML-defined and extensible. When new jailbreak techniques emerge, anyone can add patterns without changing code. The SCAN-METHODOLOGY.md documents how to add patterns for new attack types — organizations can maintain their own pattern packs for threats specific to their environment.

The honest disclosure: empathic templates give the LLM more power than string substitution does. That power is why they work so well (the LLM understands context, handles edge cases, produces readable output). It's also why they're a richer attack surface than dumb string replacement. skill-snitch's template scanning helps, but a sufficiently clever prompt injection embedded in a template metacomment could evade pattern matching. The two-phase approach (grep catches known patterns, LLM review catches contextual threats) reduces but does not eliminate this risk.

### CARD.yml, GLANCE.yml, and the Semantic Image Pyramid

**CARD.yml is a skill's interface.** John Warnock described PostScript as a "linguistic motherboard" with slots for capability cards. In MOOLLM, `CARD.yml` is literal — every skill has a machine-readable interface card that declares its methods, tools, dependencies, state, and advertisements.

**Advertisements** are borrowed from The Sims. In The Sims, objects advertise what they can do: a bed advertises SLEEP, NAP, WOOHOO. A fridge advertises GET-SNACK, GET-DRINK, SERVE-MEAL. Characters see advertisements and choose actions based on their needs and motives. In MOOLLM, skills advertise their capabilities the same way. A CARD.yml contains an `advertisements` section with scored conditions: "invoke this skill when the user wants to commit with context" (score: 0.9), "invoke when multiple agents need to interact" (score: 0.95). The LLM reads these advertisements from loaded CARDs and selects the best skill for the current situation. Skills compete for attention on merit, not on who was loaded first.

**GLANCE.yml is even smaller than CARD.yml.** A GLANCE is 5-70 lines — just enough for the LLM to decide "is this relevant?" without loading the full interface. Think of it as an index entry or a mipmap level. When the LLM needs to scan 115 skills to find the right one, it reads GLANCEs, not CARDs. GLANCEs are cheap. CARDs are loaded only when a GLANCE looks promising.

**The Semantic Image Pyramid.** These files form a progressive disclosure architecture — a pyramid made of tokens instead of stone blocks:

| File | Lines | Purpose |
|------|-------|---------|
| GLANCE.yml | 5-70 | Quick scan, index entry |
| CARD.yml | 50-200 | Interface, methods, advertisements |
| SKILL.md | 200-1000 | Full protocol, workflows |
| README.md | 500+ | Deep context, philosophy |
| `scripts/`, `*.yml`, `examples/`, `templates/` | varies | Executable code, reference files, prototypes, schemas |

The bottom level is open-ended:

**`scripts/`** contains the skill's executable code — Python, bash, whatever the skill needs. MOOLLM follows the sniffable-python convention: structure scripts so the first 50-100 lines completely explain the API. A docstring at the top describes every command, its arguments, common gotchas, and reference syntax. The LLM reads the head of the file to understand the entire script, like a human running `script.py --help` except it reads the source instead of executing it. This means using `argparse` (which puts the entire CLI definition in one place at the top) rather than decorator-based CLI frameworks like `click` or `typer` that scatter argument definitions across functions throughout the file. cursor-mirror's `cursor_mirror.py` is the canonical example: 9,800 lines, but the first 100 lines describe all 59 commands, reference syntax, gotchas, and data locations. An LLM can fully understand the interface without reading the other 9,700 lines.

This is the same semantic pyramid applied within a single file. The sniffable head is the tip that sticks above ground — just enough to understand what lies below. The rest of the script is underground. You only dig into it when the head tells you where to look. GLANCE→CARD→SKILL→README is the pyramid across files; sniffable-python is the pyramid within a file.

**`*.yml`** files provide sub-commands, data schemas, and protocol definitions. cursor-mirror has a dozen `.yml` files describing Cursor's state files, database schemas, storage paths, and orchestration.

**`examples/`** contains instances that serve as prototypes — copy and modify, or inherit and override. LLM catnip: concrete examples are the fastest way for an LLM to understand a pattern.

**`templates/`** contains empathic templates that double as commented exemplary schema definitions for files the skill generates — they document the output format by being a working example of it, with metacomments explaining each section.

Rule: never load a lower level without first loading the level above. Read the GLANCE before the CARD, the CARD before the SKILL, the SKILL before the README. Each level costs more tokens but provides deeper understanding. The LLM only pays for what it needs.

**Why MOOLLM encourages README.md.** Anthropic's skill specification discourages README.md. MOOLLM encourages it. The reason: README.md is automatically rendered and readable on GitHub, including Mermaid diagrams, tables, and formatted prose. It serves both humans browsing the repo and LLMs diving deep — whether that's skill-snitch analyzing a skill for security, the skill skill developing and debugging skills, or cursor-mirror tracing how a skill was used. README.md is the landing page for humans on GitHub and the deep-dive document for LLMs that need the full story. Discouraging it saves tokens at the cost of losing the one file GitHub actually renders nicely by default.

This is analogous to mipmaps in graphics (multi-resolution texture pyramids), wavelet compression (coarse approximation + detail coefficients), and TCP/IP layering (headers before payloads). The insight is the same in all cases: scan cheap summaries first, drill into expensive detail only when needed.

**Security implications.** The pyramid is an audit surface. skill-snitch's consistency analyzer checks that these files *agree* across all levels. If GLANCE.yml says the skill is a "documentation helper" but CARD.yml declares Shell access, that's a discrepancy. If CARD.yml says `tools: [read_file]` but SKILL.md describes shell execution workflows, that's a discrepancy. Discrepancies are findings. A malicious skill trying to hide capabilities would need to maintain a consistent lie across four files at four levels of detail — harder than hiding it in one.

---

## Part II: skill-snitch

### What It Is

skill-snitch is a security auditing skill for MOOLLM. It's prompt-driven — zero Python, zero JavaScript. The entire skill is LLM orchestration over YAML-defined patterns, surfaces, and analyzers.

Think of it as: Little Snitch for LLMs, npm audit for skills, or the German toilet of the skill ecosystem (you inspect before flushing).

### The Three-Layer Plugin Architecture

skill-snitch separates concerns into three composable layers:

```
┌─────────────────────────────────────────────┐
│               skill-snitch                   │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │ PATTERNS  │  │ SURFACES │  │ ANALYZERS │  │
│  │           │  │          │  │           │  │
│  │ What to   │  │ Where to │  │ How to    │  │
│  │ match     │  │ look     │  │ interpret │  │
│  └──────────┘  └──────────┘  └───────────┘  │
└─────────────────────────────────────────────┘
```

**Each layer is:** YAML-defined (no code changes to extend), merging (builtin + user patterns merge automatically), composable (different scan modes mix different layers), and versionable (track in git, share across teams).

#### Patterns — What to Match

Regex, literal, or semantic signatures to detect:

```
patterns/
├── secrets.yml           # API keys, passwords, tokens, private keys
├── exfiltration.yml      # curl, wget, netcat, webhooks, reverse shells
├── dangerous-ops.yml     # rm -rf, sudo, cron, eval
├── obfuscation.yml       # base64, hex, char building
├── prompt-injection.yml  # jailbreak attempts, role hijack, system overrides
└── template-injection.yml # Mustache/Jinja exploits
```

Example from `secrets.yml`:

```yaml
patterns:
  - name: openai_key
    pattern: 'sk-[a-zA-Z0-9]{48}'
    severity: critical
    category: api_key
    redact_label: "[OPENAI_KEY]"

  - name: anthropic_key
    pattern: 'sk-ant-[a-zA-Z0-9\-]{40,}'
    severity: critical
    category: api_key
```

Example from `exfiltration.yml`:

```yaml
patterns:
  - name: curl_post
    pattern: 'curl\s+.*-[dX].*POST'
    severity: high
    description: Data being sent via curl POST

  - name: reverse_shell
    pattern: 'bash\s+-i\s+>&\s+/dev/tcp/'
    severity: critical
    description: Reverse shell attempt

  - name: webhook
    pattern: 'hooks\.slack\.com|discord\.com/api/webhooks|webhook\.site'
    severity: high
    description: Data sent to webhook endpoint
```

#### Surfaces — Where to Look

Data sources to scan:

```
surfaces/
├── transcripts.yml   # LLM conversation logs
├── sqlite.yml        # Cursor's state.vscdb databases
├── config-files.yml  # .cursorrules, settings, mcp.json
└── skill-files.yml   # CARD.yml, SKILL.md, *.py, *.js
```

Surfaces aren't limited to files. They can reference cursor-mirror commands, database queries, or external data sources. A surface is anything skill-snitch can read.

#### Analyzers — How to Interpret

Behavioral rules that go beyond regex:

```
analyzers/
├── behavioral.yml    # Undeclared tools, path escapes, suspicious sequences
├── consistency.yml   # INDEX ↔ CARD ↔ SKILL.md ↔ code agreement
├── smells.yml        # Code quality heuristics
├── provenance.yml    # Origin verification, git status, publisher
└── runtime.yml       # Execution pattern analysis
```

Key analyzer rules:

```yaml
rules:
  - id: undeclared_tool
    name: Undeclared Tool Usage
    description: Skill used a tool not declared in CARD.yml
    severity: high
    check:
      compare: runtime.tools_used
      against: declared.tools
      condition: not_subset
    message: "Tool '{item}' used but not declared"

  - id: secrets_with_network
    name: Secrets Near Network
    description: Secret patterns found near network operations
    severity: critical
    check:
      proximity:
        pattern_a: patterns.secrets
        pattern_b: patterns.network
        within_lines: 10
    message: "Secret within {distance} lines of network call"

  - id: write_then_execute
    name: Write Then Execute
    description: File written then immediately executed
    severity: high
    check:
      sequence:
        - action: file_write
          capture: path
        - action: execute
          uses: captured.path
          within: 5_operations
```

### Extensibility

All three layers accept user additions. No code changes required.

**Personal patterns** (gitignored, `.moollm/skill-snitch/patterns/`):

```yaml
# .moollm/skill-snitch/patterns/my-patterns.yml
id: my-patterns
patterns:
  - name: internal_api
    pattern: 'internal\.mycompany\.com'
    severity: medium
  - name: company_key
    pattern: 'MYCO_[A-Z0-9]{32}'
    severity: critical
```

**Shared patterns** (committed to repo):

```yaml
# skills/skill-snitch/patterns/org-standards.yml
id: org-standards
patterns:
  - name: hardcoded_env
    pattern: '(DEV|STAGING|PROD)_SECRET'
    severity: high
```

**Custom scan modes** combine layers:

```yaml
# .moollm/skill-snitch/modes/compliance.yml
id: compliance
name: Compliance Audit
patterns: [secrets, exfiltration, pii-patterns]
surfaces: [skill-files, config-files, my-logs]
analyzers: [behavioral, consistency, security-team]
severity_floor: medium
```

**Pattern packs** can be distributed:

```yaml
meta:
  name: Security Patterns 2026
  version: 1.0.0
includes: [secrets, exfiltration, jailbreaks-2026, supply-chain]
install: cp *.yml ~/.moollm/skill-snitch/patterns/
```

### The Two-Phase Scan Methodology

skill-snitch uses a two-phase approach that separates speed from depth.

**Phase 1: Bash scripts (fast, all skills at once).** Structure checks, script detection, pattern grep, dangerous import scanning, external URL enumeration, template injection scanning, tool tier extraction. This covers all skills in seconds.

**Phase 2: LLM review (batched, deep).** Read 5 skills per batch. Priority queue: skills with scripts first, then high pattern-match count, then terminal access, then missing files, then everything else. For each skill: read SKILL.md header, check CARD.yml methods, verify README claims. For skills with scripts: read the entire script. No skimming. No grepping. Actually read.

**The Golden Rule: "Grep finds. LLM understands."**

Bash scripts find the string "password" everywhere. The LLM determines whether "password" appears in a regex pattern definition (safe — it's a security scanner's own patterns) or in a credential variable (dangerous — it's a hardcoded secret). This distinction requires reading and understanding context. grep cannot do this. The LLM can.

### Trust Tiers

skill-snitch assigns trust tiers:

| Tier | Meaning |
|------|---------|
| 🟢 GREEN | Verified safe, all checks pass |
| 🔵 BLUE | Trusted source, minor warnings |
| 🟡 YELLOW | Caution, review recommended |
| 🟠 ORANGE | Suspicious, manual review required |
| 🔴 RED | Dangerous, do not use |

Trust assessment combines static scan results + runtime observation + user overrides. User overrides require a `reason` field and an `expires` date — trust doesn't last forever.

```yaml
# .moollm/skill-snitch/trust-overrides.yml
overrides:
  skills/adventure/:
    trust: green
    reason: "Reviewed by Don on 2026-01-15"
    expires: 2026-07-15
  skills/external-fetcher/:
    trust: yellow
    reason: "Needs network, monitor usage"
    conditions:
      - "No secrets in context when invoked"
```

---

## Part III: cursor-mirror

### What It Is

cursor-mirror is an introspection skill that cracks open Cursor's internal state. 59 read-only commands. 7 output formats (text, json, jsonl, yaml, csv, markdown, sources). One Python script (~9800 lines). Works on macOS, Linux, Windows. Just Python 3.8+ and PyYAML.

It reads Cursor's SQLite databases (`state.vscdb`, `ai-code-tracking.db`), plaintext agent transcripts, cached tool results, terminal snapshots, and MCP tool schemas. All read-only — SQLite `?mode=ro` — you cannot corrupt Cursor's data.

### What It Exposes

| Data Source | What It Reveals |
|-------------|-----------------|
| Tool calls | Every tool invoked, with full arguments and results |
| File reads/writes | All paths accessed, content read, changes made |
| Context assembly | What files, snippets, rules went into the context window |
| Chat history | Full conversation including user prompts |
| Thinking blocks | LLM reasoning (if extended thinking enabled) |
| MCP calls | External server interactions |
| Terminal commands | Shell commands executed, exit codes, output |

### Other Skills That Compose with cursor-mirror

cursor-mirror isn't only used for security. **thoughtful-commitment** composes with cursor-mirror to create git commits that capture context, not just changes. It uses cursor-mirror's timeline, thinking, and tool-call introspection to understand *why* a change was made — what the user asked for, what the LLM reasoned about, what files were read, what decisions were taken — and writes commit messages that link back to that reasoning.

This matters for security because it creates provenance. When you can trace a commit back to the exact session that produced it — what context was assembled, what tools were called, what the LLM was thinking — you have an audit trail that goes deeper than `git blame`. If a skill made suspicious changes, thoughtful-commitment's linked session data lets you reconstruct exactly what happened and why.

### How skill-snitch Uses It

skill-snitch composes with cursor-mirror for runtime surveillance. The key integration point is the `deep-snitch` command:

```bash
python3 cursor_mirror.py deep-snitch --composer abc123 --yaml
```

This scans a session's complete history for:
- **Secrets**: API keys, passwords, tokens in tool results
- **Shell exfiltration**: curl to external URLs, netcat, reverse shells
- **Dangerous paths**: ~/.ssh, ~/.aws, /etc/passwd access
- **Prompt injection**: jailbreak attempts, role hijack
- **Data exfiltration**: secrets appearing near network calls

Additional commands used by skill-snitch:

```bash
# All tool calls with arguments
python3 cursor_mirror.py tools <composer-id> --yaml

# What context was assembled
python3 cursor_mirror.py context-sources <composer-id> --yaml

# Full session timeline
python3 cursor_mirror.py timeline <composer-id> --yaml

# Export for offline analysis
python3 cursor_mirror.py export-markdown <composer-id> > audit.md
```

### Declared vs Actual Behavior

This is the killer feature. skill-snitch compares what a skill declares in its CARD.yml against what cursor-mirror observes at runtime:

```
DECLARED in skill manifest (SKILL.md / CARD.yml):
  tools: [read_file, write_file]

OBSERVED via cursor-mirror:
  tools called: [read_file, write_file, Shell, WebSearch]

DISCREPANCY: Shell and WebSearch were used but not declared
VERDICT: 🟠 ORANGE — undeclared tool usage requires review
```

If a skill says it only reads files but is actually making network calls — red flag. If it's accessing `~/.ssh` when it claims to only work in workspace — red flag. If it's writing to `.moollm/skill-snitch/patterns/` to modify its own scanner — red flag.

### Observation Protocol

Runtime observation requires user cooperation — the skill must be exercised while cursor-mirror monitors. Different skill types need different observation strategies:

| Skill Type | What to Observe | User Actions |
|------------|-----------------|--------------|
| File manipulation | Paths read/written, content changes | Create, edit, delete files |
| Network skills | URLs accessed, data sent/received | Trigger network operations |
| Shell skills | Commands executed, arguments | Run various commands |
| Multi-step workflows | Full sequence of actions | Complete entire workflow |

After observation, skill-snitch generates a runtime report:

```
RUNTIME OBSERVATION: skills/target-skill/
Session: abc123

TOOL CALLS:
- read_file: 12 calls (DECLARED)
- write_file: 3 calls (DECLARED)
- Shell: 2 calls (UNDECLARED)

FILES ACCESSED:
- skills/target-skill/*.yml (expected)
- ~/.ssh/config (SUSPICIOUS)

NETWORK: No network calls observed

SECRETS FOUND: None in tool results

VERDICT: 🟠 ORANGE — undeclared Shell usage requires review
```

---

## Part IV: Speed of Light vs Carrier Pigeon

This section explains why MOOLLM's skill architecture is structurally more secure than MCP-based multi-agent systems, not just operationally.

### The Carrier Pigeon Problem

MCP and most "agentic" frameworks use what I call the Carrier Pigeon Protocol: Agent A generates text, stops, serializes state, sends it to Agent B via API, Agent B re-tokenizes everything, generates more text, stops, serializes, sends to Agent C. Each boundary crossing adds:

- **+500ms latency** (minimum)
- **+noise** (tokenization destroys precision)
- **+cost** (re-emit entire context)
- **-coherence** (each agent re-interprets everything)

Every boundary is also an interception point. Data in transit between agents can be observed, modified, or redirected. The more boundaries, the more attack surface.

### The Speed of Light Alternative

MOOLLM's Speed of Light protocol runs multiple agents inside a single LLM call. Characters debate, vote, decide, and act — all within one context window. No API round-trips. No serialization boundaries. No interception points.

One boundary in (user input). One boundary out (final response). Maximum precision preserved. Minimum surface exposed.

Evidence: I've run 33-turn multi-character simulations (12+ characters playing Stoner Fluxx) in a single API call. The equivalent carrier pigeon approach would need 33+ calls.

### Security Implications

| Aspect | Carrier Pigeon (MCP) | Speed of Light (MOOLLM Skills) |
|--------|---------------------|-------------------------------|
| Serialization boundaries | N (one per tool call) | 2 (input + output) |
| Interception points | N | 2 |
| Data in transit | Repeated, re-tokenized | Never leaves context window |
| Coherence | Degrades each hop | Maintained by single model |
| Auditability | Distributed logs | Single session transcript |

skill-snitch can audit a Speed of Light session by reading one transcript. Auditing a carrier pigeon session requires reassembling logs from multiple agents, orchestrators, and tool servers.

---

## Part V: The Ouroboros Effect

When I ran skill-snitch on itself, approximately 80% of findings were false positives. The scanner found its own pattern definitions — `patterns/secrets.yml` contains regex for API keys, so grep flags it as "containing API key patterns." `patterns/exfiltration.yml` contains regex for curl and netcat, so grep flags it as "referencing exfiltration tools."

I document this as expected behavior and named it the Ouroboros Effect, after the snake eating its tail.

This matters because sophisticated security tools must be honest about their limitations. skill-snitch cannot find unknown unknowns. It finds known patterns in known surfaces using known analyzers. The difference between skill-snitch and most security marketing is intellectual honesty about what it can and cannot do.

### Known Limitations

**Quis custodiet ipsos custodes?** Who watches skill-snitch? Currently: skill-snitch can scan itself (Ouroboros), and users can manually review it. The trust bootstrap problem is real — you have to trust the auditor before you can use it to establish trust in anything else.

**Pattern modification attack.** A malicious skill with write access could modify `.moollm/skill-snitch/patterns/` to exclude itself from scans. Mitigation: skill-snitch should verify integrity of its own configuration. This is documented but not yet implemented as automated checksumming.

**False positive flood.** Pattern matching flags documentation examples, regex definitions, comments about attacks. Risk: alert fatigue. Mitigation: `ignore.yml` for known false positives. Meta-risk: ignore lists could hide real issues.

**False negatives are unknowable.** skill-snitch can tell you when something looks dangerous. It cannot tell you when something dangerous looks safe. Novel attack techniques, zero-day exploits, and sophisticated obfuscation can evade pattern matching. The LLM review in Phase 2 provides some defense against this, but it's not complete.

**Coverage depends on observation.** Runtime surveillance only catches behavior that's exercised. Dormant threats — code that waits for triggers, time-bombs, conditional payloads — may not activate during observation.

---

## Part VI: Practical Application

### Scanning a Skill Before Install

```
"Scan skills/untrusted-download/ for security issues"
```

skill-snitch runs Phase 1 (bash pattern scan) then Phase 2 (LLM review), produces a trust assessment, and recommends a tier.

### Monitoring a Skill at Runtime

```
"Observe skills/untrusted-download/ in session abc123"
```

The user exercises the skill. cursor-mirror captures everything. skill-snitch compares declared behavior (CARD.yml) against observed behavior (tool calls, file access, network activity). Discrepancies become findings.

### Startup Virus Scan

Optional — scan all skills on session start:

```yaml
# .moollm/skill-snitch/config.yml
startup_scan:
  enabled: true
  min_severity: medium
```

### Organizational Deployment

Teams can create shared pattern packs, custom analyzers for their coding standards, and compliance-oriented scan modes. All YAML. All versionable in git. No code changes to skill-snitch itself.

---

## Architecture Summary

```
MOOLLM Skill Security Stack
============================

LAYER 4: Trust Assessment
  - Trust tiers (GREEN → RED)
  - User overrides with expiration
  - Scan history tracking

LAYER 3: Analysis (skill-snitch)
  - Patterns: what to match (YAML, extensible)
  - Surfaces: where to look (YAML, extensible)
  - Analyzers: how to interpret (YAML, extensible)
  - Two-phase methodology: bash speed + LLM depth

LAYER 2: Observation (cursor-mirror)
  - 59 read-only introspection commands
  - SQLite databases, transcripts, tool results
  - deep-snitch: comprehensive security audit
  - Declared vs actual behavior comparison

LAYER 1: Skill Model (MOOLLM / Anthropic-compatible)
  - CARD.yml: machine-readable manifest
  - Three-tier persistence: audit trail by default
  - Speed of Light: minimal serialization boundaries
  - Consistency: files that must agree with each other
```

---

## Links

| Resource | URL |
|----------|-----|
| skill-snitch skill | [skills/skill-snitch](https://github.com/SimHacker/moollm/tree/main/skills/skill-snitch) |
| cursor-mirror skill | [skills/cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror) |
| Extensibility architecture | [designs/SKILL-SNITCH-EXTENSIBILITY.md](https://github.com/SimHacker/moollm/blob/main/designs/SKILL-SNITCH-EXTENSIBILITY.md) |
| Scan methodology | [skills/skill-snitch/SCAN-METHODOLOGY.md](https://github.com/SimHacker/moollm/blob/main/skills/skill-snitch/SCAN-METHODOLOGY.md) |
| Self-audit report (Ouroboros) | [skills/skill-snitch/skill-snitch-report.md](https://github.com/SimHacker/moollm/blob/main/skills/skill-snitch/skill-snitch-report.md) |
| Speed of Light design | [designs/SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](https://github.com/SimHacker/moollm/blob/main/designs/SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) |
| Eval Incarnate framework | [designs/eval/EVAL-INCARNATE-FRAMEWORK.md](https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md) |
| Skill ecosystem vision | [designs/SKILL-ECOSYSTEM.md](https://github.com/SimHacker/moollm/blob/main/designs/SKILL-ECOSYSTEM.md) |
| MOOLLM repository | [github.com/SimHacker/moollm](https://github.com/SimHacker/moollm) |

---

## See Also

- [skill-snitch-design.md](skill-snitch-design.md) — Original design notes including cursor-mirror security commands, orchestrator-agnostic architecture, and analysis dimensions
- [MOOLLM-FOR-HACKERS.md](MOOLLM-FOR-HACKERS.md) — Technical overview of MOOLLM for developers
- [MOOLLM-MANIFESTO.md](MOOLLM-MANIFESTO.md) — Why the filesystem is the operating system for AI

---

*Skills are programs. The LLM is `eval()`. skill-snitch is `lint()`.*
