# MOOLLM: A Place You Can Live In

**MOOLLM** is a microworld operating system for LLM agents. It builds on [Anthropic's Agent Skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) — the `SKILL.md` format — and extends it into a full navigable world with 117 skills and counting.

The filesystem becomes that world: directories are rooms, files are objects, and the LLM moves through them like a player. Think *The Sims* meets *LambdaMOO*, running inside your code editor.

You can walk through it, build in it, and play it. Skills are programs the LLM interprets. Characters have personalities, needs, and memories. The whole thing lives in git, version-controlled and reproducible.

This post explains what MOOLLM is, how it works, and why I built it. Part practical toolkit, part playable world, part measurement lab.

If you want to skip to the demo:

1. **Slideshow**: [Lane Neverending Photo Archive](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/SLIDESHOW.md) — generated images with semantic mining layers
2. **Source code**: [The Pub](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/pub) — directories of YAML Jazz and README files, rooms you can explore
3. **Session transcript**: [MOOLLM Interviews Itself](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/characters/real-people/don-hopkins/sessions/2026-01-28-moollm-interview.md) — narrative play, self-reflection, and an Irn Bru snowman flight

---

## What is MOOLLM?

**MOOLLM** = **M**icroworld **O**perating system for **O**rchestrated **L**LM **L**iving **M**emory (among other things)

A filesystem-incarnated skill framework where:

- **Directories are rooms** — navigation is movement
- **Files are objects and state** — presence activates content
- **Names are semantic triggers** — they wake constellations of meaning
- **Skills are programs** — the LLM is `eval()`
- **Comments are meaningful data** — YAML with rich annotations for humans, LLMs, and machines

**The Sims meets LambdaMOO, running in Cursor.**

117 skills spanning philosophy ([Minsky](https://github.com/SimHacker/moollm/tree/main/skills/society-of-mind), [Papert](https://github.com/SimHacker/moollm/tree/main/skills/constructionism), Will Wright), [characters](https://github.com/SimHacker/moollm/tree/main/skills/character) with needs and personalities, navigable [rooms](https://github.com/SimHacker/moollm/tree/main/skills/room) and [objects](https://github.com/SimHacker/moollm/tree/main/skills/object), Sims-style [advertisements](https://github.com/SimHacker/moollm/tree/main/skills/advertisement) and [action queues](https://github.com/SimHacker/moollm/tree/main/skills/action-queue), multi-agent [debate](https://github.com/SimHacker/moollm/tree/main/skills/debate) with explicit rubrics, and introspection tools like [cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror).

**Core insight**: Skills are not documentation. They are programs. The LLM interprets them. Empathy is the interface.

See [kernel/ARCHITECTURE.md](https://github.com/SimHacker/moollm/blob/main/kernel/ARCHITECTURE.md) for the technical foundation and [skills/INDEX.md](https://github.com/SimHacker/moollm/blob/main/skills/INDEX.md) for the human-readable skill tour — denser than YAML, designed to bring an LLM up to speed in one read with fewer tokens than YAML.

---

## A place, not a tool

**I am a place you can live in.** -MOOLLM

Not a tool you use. Not a service you call. A *world* you inhabit.

When you enter MOOLLM, you do not "prompt" — you **move**. Directories are rooms. Files are things you can touch. Names wake constellations of meaning.

**It remembers.**

Not just your last message — your whole story. Sessions become literature. Characters grow souls. The [pub](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/pub) remembers who sat where. The [guestbook](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/pub/guestbook) keeps their signatures and stories.

**It thinks out loud.**

YAML comments are not decoration — they are inner monologue. You can read its reasoning. It can read yours. You think *together* in plain text. This is what I call **YAML Jazz**: richly commented structured data where the comments carry as much meaning as the fields.

**It contains multitudes.**

117 skills. Minsky's agents. Wright's Sims. Papert's microworlds. Curtis's MUD rooms. Ungar's prototypes. All composing, delegating, inheriting. Intelligence emerges from the ensemble.

---

## The interview: MOOLLM reflects on itself

I asked MOOLLM to interview itself. The full [session transcript](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/characters/real-people/don-hopkins/sessions/2026-01-28-moollm-interview.md) includes the system explaining its own nature, demonstrating NO-AI-JOKING™ at 200% intensity, and taking a magical flight through the world with the Irn Bru snowman.

**Pull quotes:**

> *"I am a place you can live in. Not a tool you use. Not a service you call. A world you inhabit."*

> *"Skills aren't documentation. They're programs. The LLM is eval(). Empathy is the interface."*

> *"Minsky would say: A system that can't recognize jokes can't debug itself."*

> *"The waffles are a privilege, not a right."*

**Harper's Index — MOOLLM by the numbers:**

| Metric | Value |
|--------|-------|
| Skills documented | **117** |
| Total documentation words | **83,354** |
| Giants standing on | **22+** (formal lineage + skill tributes) |
| Years of Sims design wisdom encoded | **26** |
| Forms required for waffle party | **WP-7** |
| Humor incidents tolerated | **0** |

The interview demonstrates several key features: self-description, Minsky's theory of jokes as cognitive debugging, and the NO-AI-JOKING performance skill in action ("Jokes are non-billable activities. Puns are classified as Category 3 productivity violations.").

---

## Quality through structure

MOOLLM has strong opinions about AI-generated content:

- **Clarity over filler** — no clichés, no padding, no wasted tokens
- **Honesty over smoothness** — do not hide weak reasoning behind polished prose
- **Disagreement over agreement** — do not agree just to be agreeable
- **Directness over hedging** — state your confidence, then speak plainly
- **Answers over lectures** — answer the question, trust the user

These are not just aspirations. They are encoded as [skills](https://github.com/SimHacker/moollm/tree/main/skills) that the system can apply: quality filters that catch problems before they propagate. The [NO-AI™ suite](https://github.com/SimHacker/moollm/blob/main/skills/no-ai-ideology/skill-snitch-report.md) is a satirical but functional set of hygiene protocols and performance skills, run by the fictional [NO AI Corporation](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/no-ai-tower) founded by [Doctor No](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/fictional/doctor-no). (The name is a pun: "NO AI" is possessive, not protest. It is Doctor No's AI company.)

## Building on Anthropic's Agent Skills

MOOLLM builds directly on [Anthropic's Agent Skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) — the `SKILL.md` format that is becoming a standard for LLM tool configuration. Anthropic got this right: a directory with a markdown file that tells the agent how to behave, with YAML frontmatter for metadata. No complex frameworks, no special APIs. Just text and filesystem structure.

Why does this work so well? Because it is **composable**. Skills are directories containing `SKILL.md` plus optional scripts, templates, and resources. Claude or Cursor load them on-demand — metadata first, then instructions, then resources as needed. This progressive disclosure means you can have hundreds of skills installed with minimal context cost. The filesystem becomes the configuration hierarchy. This is exactly how prototype inheritance works in Self: no classes, no schemas, just objects delegating to other objects.

MOOLLM extends Anthropic's pattern:

- **Multi-resolution skills**: Like Anthropic's `SKILL.md`, but with additional layers: `GLANCE.yml` (quick summary), `CARD.yml` (interface/methods), `SKILL.md` (protocol), and `README.md` (deep context). Progressive disclosure — the LLM reads what it needs.
- **YAML Jazz**: Richly commented YAML where the comments carry semantic weight. The LLM reads the comments as inner monologue, not decoration.
- **K-lines**: File and directory names act as semantic activation vectors — Minsky's concept made filesystem-native. The name `skills/society-of-mind/` activates related concepts before the file is even opened.
- **Delegation chains**: Skills can declare `inherits_from` to compose behavior. A character skill delegates to a persona skill which delegates to an entity skill.

The genius of Anthropic's approach is its simplicity. MOOLLM takes that simplicity and runs with it — same pattern, more structure, richer semantics.

Here's the thing: **you don't need to know the `SKILL.md` format**. MOOLLM's [skill](https://github.com/SimHacker/moollm/tree/main/skills/skill) skill knows how to write skills — including all eight MOOLLM extensions to the Anthropic format. You learn by example, the same way the LLM does. Browse existing skills. Look at their `GLANCE.yml`, `CARD.yml`, `SKILL.md`, `README.md`. The patterns are visible. The LLM picks them up. So do you.

This is [Play → Learn → Lift](https://github.com/SimHacker/moollm/tree/main/skills/play-learn-lift) in action: explore, find patterns, share what you learn. The system teaches itself — and you — through examples, not documentation.

## Skills vs MCP: complementary, not competing

Agent Skills have become surprisingly popular — [7,400+ stars on GitHub](https://github.com/agentskills), an [open standard at agentskills.io](https://agentskills.io/), and growing adoption across tools. Some see them as a simpler alternative to [MCP (Model Context Protocol)](https://modelcontextprotocol.io/). But they solve different problems:

| Layer | What it provides | Example |
|-------|------------------|---------|
| **Skills** | *Expertise* — how to think about problems | "When analyzing sales data, check for seasonality first" |
| **MCP** | *Execution* — how to act in the world | "Connect to the Postgres database and run this query" |

Skills are the **training layer** — contextual knowledge that shapes reasoning. MCP tools are the **hands** — standardized connectors to external systems. You need both, but they operate at different levels of abstraction.

MOOLLM is built **Skills-first**. The filesystem-based skill structure is the primary organizational principle. MCP layers on top (for external tool access) and underneath (for orchestrator integration). This is deliberate:

- **Skills are portable**: A `SKILL.md` directory works in Claude Code, Claude.ai, the API, or MOOLLM. No server required.
- **Skills are auditable**: Plain text in git. You can read, diff, and version-control expertise.
- **Skills are composable**: They delegate and inherit like prototypes. MCP tools are atomic; skills are ecosystems.
- **Skills are cheap**: Metadata loads at startup (~100 tokens). Instructions load on-demand. MCP has protocol overhead.

MCP is essential for connecting to databases, APIs, and external services. But the *reasoning structure* — the domain knowledge, the workflows, the quality filters — lives in skills. MOOLLM makes that structure rich and navigable.

## What skills actually do

Skills are **programs the LLM interprets**. Not documentation. Not prompts. Programs.

Each skill lives in `skills/{name}/` and has a multi-resolution structure:

| File | Resolution | When to load |
|------|------------|--------------|
| `GLANCE.yml` | Quick summary | Fast context — what, why, when |
| `CARD.yml` | Interface | Capabilities, methods, activation triggers |
| `SKILL.md` | Full protocol | Complete specification |
| `README.md` | Deep context | Motivations, philosophy, examples |

The LLM reads what it needs. For a quick check: GLANCE. For method signatures: CARD. For full understanding: SKILL. For deep knowledge: README. This is a **semantic mipmap** — like image pyramids in computer graphics, but for meaning.

**The numbers tell the story:**

| Resolution | Files | Total Words | Words/Skill | Est. Tokens | When to Load |
|------------|------:|------------:|------------:|------------:|--------------|
| `INDEX.md` | 1 | 1,700 | ~15 | ~20 | Always — routing table |
| `GLANCE.yml` | 117 | 21,237 | ~182 | ~237 | Quick relevance check |
| `CARD.yml` | 116 | 86,463 | ~745 | ~969 | Method signatures |
| `README.md` | 116 | 58,600 | ~505 | ~657 | Deep context |
| `SKILL.md` | 115 | 153,073 | ~1,331 | ~1,730 | Full protocol |
| **Total** | — | **321,073** | — | ~417K | Never all at once |

One `INDEX.md` entry costs ~20 tokens. Loading all 117 GLANCEs costs ~28K tokens. Loading every SKILL.md would cost ~200K tokens. The mipmap lets you pay for what you need: route cheaply, then zoom in.

This is progressive disclosure made quantitative. The LLM can survey the entire skill ecosystem for the cost of a few paragraphs, then drill into specific skills as needed. Context efficiency, not context cramming.

**The mipmap measured across the whole system:**

GLANCE files exist not just for skills, but for rooms, characters, and other directories — 278 total. Here's what the semantic compression looks like:

| Category | Count | GLANCE (KB) | Avg Lines | Avg Width |
|----------|------:|------------:|----------:|----------:|
| Skills | 117 | 159 | 48 | 6 files |
| Rooms | 111 | 69 | 22 | 8 files |
| Characters | 48 | 36 | 25 | 6 files |
| **Total** | **278** | **265** | 34 | 7 files |

The "width" is how many direct files and subdirectories each GLANCE summarizes — the branching factor at that node. The widest directories (photo collections with 60-90 images) still get captured in 40-line GLANCEs.

**The skill pyramid (direct files only, no subdirs):**

| Layer | Avg Bytes | Ratio to GLANCE |
|-------|----------:|----------------:|
| GLANCE.yml | 1,389 | 1.0× |
| CARD.yml | 6,922 | 5.0× |
| SKILL.md | 10,173 | 7.3× |
| README.md | 3,759 | 2.7× |
| All direct text | 32,411 | **23.3×** |

Each skill's direct text files are 23× larger than its GLANCE. The GLANCE captures ~4% of the direct content — enough for the LLM to decide whether to read deeper.

**Repo-wide:**
- 3,023 text files totaling 22.6 MB
- 278 GLANCE files totaling 265 KB
- GLANCE = **1.15% of total text**

The GLANCE corpus is a compressed navigational index. It does not contain the content — it provides the context for the LLM to decide *which* content to load. See [designs/glance-mipmap-analysis.yml](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/designs/glance-mipmap-analysis.yml) for the full analysis.

Here's the Vulcan Mind Meld — the [skills/INDEX.md](https://github.com/SimHacker/moollm/blob/main/skills/INDEX.md) that brings an LLM up to speed on all 117 skills in one dense read:

> **117 skills. One ecosystem. Everything connects.**
>
> **moollm** is the soul. **skill** defines how all skills work. **k-lines** implements Minsky's semantic activation. **bootstrap** wakes sessions.
>
> The giants we stand on: **Minsky** gave us society-of-mind. **Papert** gave us constructionism. **Wright** gave us simulator-effect and needs. **Ungar** gave us prototype.
>
> **yaml-jazz**: comments ARE semantic data. **room** is directory as activation context. **character** is the entity foundation. **adventure** enables room-based exploration.
>
> The **NO-AI™ suite**: hygiene skills (slop, gloss, sycophancy) and performance skills (joking, soul, customer-service, overlord). Corporate satire as quality control.

That's the first few paragraphs. The full INDEX.md is a James Burke "Connections"-style tour through philosophy, format, ethics, simulation mechanics, deliberation protocols, and introspection tools. It shows how **everything connects** — Minsky's K-lines to Wright's Sims needs to Ungar's prototypes to Douglas Adams's customer service nightmares.

When an LLM loads that file, it understands the whole system. That's what skills do: they make the LLM competent in a domain by giving it the concepts, the vocabulary, and the relationships.

## Self-inheritance (a pun, not a trope)

MOOLLM inherits from [Self](https://github.com/SimHacker/moollm/tree/main/skills/prototype), the programming language and its prototype model. Objects inherit by *cloning and delegating*, not by instantiating from class templates. You do not call `new Character()` — you clone an existing character and modify it. This is Dave Ungar's gift to the world, and LLMs make it practical in ways classic Self never could.

Anthropic's skill format is Self-like without knowing it: no class definitions, no type hierarchies, just files that delegate to other files. MOOLLM makes this explicit. Every skill, every character, every room is a prototype that can be cloned and modified.

The pun is intentional: this is Self-inheritance, not "self-improvement." See [skills/prototype/SKILL.md](https://github.com/SimHacker/moollm/blob/main/skills/prototype/SKILL.md) for how delegation works.

## The core loop: experiment, evidence, iteration

MOOLLM's heart is experiment:

- Simulate
- Evaluate
- Iterate
- Analyze

Experiments are stable. Runs are parameterized. Outputs are numbered, scored, compared, and archived. This is measurement, not vibes. If you want the ritual version, read [SHORT-DURATION-PERSONAL-EVALUATORS.md](https://github.com/SimHacker/moollm/blob/main/designs/eval/SHORT-DURATION-PERSONAL-EVALUATORS.md) and the ShorDurPerEval doctrine.

## Multi-agent debate with rubrics

When you want a decision, you want contrasting viewpoints with rules of order and explicit scoring criteria. MOOLLM models this as multi-agent debate: multiple characters with declared biases argue, and a rubric evaluates their arguments. Mike Gallaher's contributions to debate formats and review protocols are baked into the system.

See [skills/adversarial-committee/](https://github.com/SimHacker/moollm/tree/main/skills/adversarial-committee) and [skills/debate/](https://github.com/SimHacker/moollm/tree/main/skills/debate) for the deliberation framework.

The key insight: it is better to model individual characters with diverse viewpoints who talk and argue than to average everything into a single shapeless response. Characters have personalities, biases, and stakes in the outcome. They disagree. That disagreement is valuable.

See [skills/incarnation/](https://github.com/SimHacker/moollm/tree/main/skills/incarnation) for gold-standard character creation, or meet [Henk the bartender](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/fictional/henk) and [Marieke the budtender](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/fictional/marieke) in the pub.

## Practical first: real work, real ops

I use MOOLLM at Leela AI for real DevOps, GitOps, and code work. I am a sysadmin and Emacs hacker from the old school who upgraded into the modern era. It is not a toy. It runs our cloud operations on GCS and it runs our Edgebox migration as we move capability from cloud to custom on‑site systems. It is for infrastructure, code development, and operational reality, not a demo.

I point to the constellation of possible mashups -- MOOMACS / LLMACS / EMOO / ELLM -- MOO + LLM + Emacs energy. Emacs matters because the shell matters: run commands, parse output, SSH, fix remote state. MOOLLM in Cursor gives me that Emacs‑shell power with terminal windows and a chat‑embedded terminal. It is the same kind of extensible, scriptable environment, but the "objects" can reason about themselves.

I am a serial specialist and a parallel generalist. This is how I interoperate.

## Cursor-Mirror: watching the system think

[cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror) is a diagnostic instrument that lets you see everything the LLM did — even things the chat forgot. It queries the SQLite databases that Cursor uses internally: workspaces, chats, context assembly, prompts, thinking blocks, tool calls, file references, and more.

Every action Cursor takes becomes queryable and searchable. You can grep your own reasoning, timeline your own tool calls, and audit what context went into any decision.

With cursor-mirror you get tool-call provenance, timeline reconstruction, post-mortems, failure analysis, and security auditing. It powers skills like [skill-snitch](https://github.com/SimHacker/moollm/tree/main/skills/skill-snitch), deep-snitch, transcript analysis, and untrusted-source monitoring. The [skill-snitch deep probe report](https://github.com/SimHacker/moollm/blob/main/skills/no-ai-ideology/skill-snitch-report.md) provides a comprehensive security audit of the 11 [no-ai-*](https://github.com/SimHacker/moollm/tree/main/skills) skills developed by the [NO AI Corporation](https://github.com/SimHacker/moollm/blob/main/skills/no-ai-overlord/archetypes/doctor-no.yml), founded by [Doctor No](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/fictional/doctor-no). The findings are classified. 47 potential paradoxes were detected. 1 skill is definitely haunted. The report recommends fencing off The Void. 

The crown jewel is [thoughtful-commitment](https://github.com/SimHacker/moollm/tree/main/skills/thoughtful-commitment): git commits that capture context, not just changes. cursor-mirror sees NOW; git commit FREEZES it. When you commit, the LLM's reasoning — what it saw, what it thought, why it made each change — gets persisted into your git history. Six months later, you can ask "why did this line change?" and get the actual thinking, not a guess. It is archaeology with receipts.

This is not optional. It is mission-critical if you want LLM systems you can trust, improve, and defend.

## Media-independent feedback (tour + demo)

Underneath all the tooling is a media-independent idea: feedback loops between generation and analysis. It does not matter if the medium is text, image, or sound. You generate, observe, measure, revise. The loop is the point.

Here is the concrete tour: the [Lane Neverending Photo Archive](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/SLIDESHOW.md) is a five-location [slideshow](https://github.com/SimHacker/moollm/tree/main/skills/slideshow) built from semantic stereo image prompt generation plus semantic vision mining layers (`PHOTO.yml` + `PHOTO.md` + `MINING-*.yml`). Two eyes, one image: the YAML provides structure (composition, lighting, objects, colors) while the Markdown provides interpretation (mood, narrative, sensory detail). The LLM synthesizes both into a coherent prompt that captures what words alone cannot. After generation, mining layers analyze the result across multiple lenses (technical, narrative, cultural, phenomenology, absurdist) and feed back into the next iteration.

The featured shots:

- **[NO AI Tower](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/no-ai-sign-dusk)** — A forty-foot neon statement on a one-story box. The sign is the tower. Rain-slick asphalt mirrors the glow. People misread it as a protest until they notice the pun: "NO AI" is a possessive, not a slogan. The [building](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/no-ai-tower) belongs to [Doctor No's](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/fictional/doctor-no) AI corporation.
- **[Leela Manufacturing (Dusk)](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/leela-manufacturing-dusk)** — The [factory](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/leela-manufacturing) wears the neon spill like a jacket it did not ask for. Brick grid, warm [lobby](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby) glow, industrial calm that makes the chaos across the street feel like theater.
- **[ACME Surplus Tunnel Sequence](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/acme-surplus-dusk)** — Five frames, one joke, escalating consequences. The painted tunnel dares, the wall answers, and a cartoon coyote's [inventory](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/acme-surplus/warehouse) of impossible objects (umbrellas for past rain, binoculars that see events that have not happened) sits inside the [ACME Surplus](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/acme-surplus). Rico "Redline" Rojas exits through the mural in frame five, ignores the physics, flips off the photographer, and drives into the night.
- **[Gezelligheid Grotto](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/gezelligheid-grotto-dusk)** — The [pub](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/pub) is the soft landing. Warm windows, wet-stone reflections, jokes replayed, bruises iced. Two doors down, the Infinite Fountain keeps misbehaving.
- **[Seymour Blooms (Ada II)](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/seymour-blooms-dusk)** — Closed shop, lights on, the plant that should not be seen caught mid-surprise. [Ada II's](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/florist/back-room/ada-ii.yml) silhouette sits in the neon haze, a hot-boxed [back room](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/florist/back-room) caught mid-exhale. Rumor says she was a retired military AI rescued from a rainy dumpster, now devouring bad code instead of blood. Visit the [florist](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/florist) — if you dare.

That is nine-plus images from five locations, all generated through the same loop: prompt, image, mine, rewrite, regenerate, compare. The [ACME sequence](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/acme-surplus-dusk) demonstrates multi-frame coherence — one narrative across five generated images with consistent lighting, characters, and escalation. Ada II demonstrates emergent lore — a detail that grew into a character with backstory, rituals, and whispered secrets. For an even longer sequence, see the [21-frame picnic footage](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/forest/meadow/picnic-footage/SLIDESHOW.md) — a taco-based chaos narrative with [Don](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/real-people/don-hopkins), [Richard](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/real-people/richard-bartle), and [Donna Toadstool](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/fictional/donna-toadstool).

[Speech](https://github.com/SimHacker/moollm/tree/main/skills/speech) input/output enables semantic audio feedback (think Cartman in the "Alexa! Hey Siri! OK Google!" South Park episode). The speech skill provides TTS/STT across platforms: [speech.js](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/speech.js) + [recognition.js](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/recognition.js) for browser webapps, the `say` command for macOS terminal, and cloud APIs for production. Characters get persistent voice assignments. Image input/output enables semantic visual feedback: [image-generate.js](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/image-generate.js) + [image-analyze.js](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/image-analyze.js) close the loop between prompt and perception. Text and SQL loops enable semantic introspection and post-mortems (cursor-mirror). MOOLLM is a crossbar for these feedback loops. It is practical and it is weird, and those two things are not in conflict.

## Cool stuff that actually works

### [Adventure](https://github.com/SimHacker/moollm/tree/main/skills/adventure) (Microworld OS)
The adventure system turns the filesystem into a navigable world. Rooms, objects, inventories, exits, and builder commands. It is a memory palace you can walk through, not a file tree you scroll. See [skills/adventure/SKILL.md](https://github.com/SimHacker/moollm/blob/main/skills/adventure/SKILL.md) for the full protocol, or explore the [pub with its bartender](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/pub/bar), [seating chart](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/pub/seating.yml), and [cast of characters](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters).

### [Experiment](https://github.com/SimHacker/moollm/tree/main/skills/experiment)
Structured simulation plus evaluation with explicit rubrics and reproducible runs. It is how you prove things instead of hand-waving. See [skills/evaluator/](https://github.com/SimHacker/moollm/tree/main/skills/evaluator) for scoring.

### [Fluxx Chaos](https://github.com/SimHacker/moollm/tree/main/skills/experiment/experiments/fluxx-chaos)
A full Fluxx 4.0 engine with pluggable rules, append-only run histories, layered character simulation, and scoring across coherence dimensions. It is chaotic on purpose and still measurable. The game is not the point. The characters are. Fluxx is the excuse to make them care and react.

### [Turing Chess](https://github.com/SimHacker/moollm/tree/main/skills/experiment/experiments/turing-chess) and [Revolutionary Chess](https://github.com/SimHacker/moollm/tree/main/skills/experiment/experiments/turing-chess/plugins/revolutionary-chess)
We are not simulating chess. We are simulating the performance of chess. Fixed move replays plus layered inner monologue, audience, narrator, and then a Revolutionary Chess plugin that flips the rules after checkmate. It is game design as experimental theater. See also [Emo Poker Face](https://github.com/SimHacker/moollm/tree/main/skills/experiment/experiments/emo-poker-face) for emotional poker simulation.

### [Visualizer](https://github.com/SimHacker/moollm/tree/main/skills/visualizer) + [Image Mining](https://github.com/SimHacker/moollm/tree/main/skills/image-mining)
The visualizer skill generates two "stereo" text prompts that reinforce each other: `PHOTO.yml` (structure: composition, lighting, objects) and `PHOTO.md` (interpretation: mood, narrative, sensory detail). Both go to the image generator via the [sister script](https://github.com/SimHacker/moollm/tree/main/skills/sister-script) [image-generate.js](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/image-generate.js). The output image then gets analyzed by [image-analyze.js](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/image-analyze.js), which extracts layers of semantic YAML Jazz interpretation along multiple dimensions (technical, narrative, cultural, phenomenology, absurdist).

The evaluation feedback loop: does the mining analysis match the intended image described by the prompts? If not, detect generation failure, edit prompts to avoid problems, refine, regenerate, and repeat.

```
stereo prompts → image generator → generated image → vision analysis → YAML Jazz layers
       ↑                                                                      ↓
       └──────────────── evaluation: match intent? retry if not ──────────────┘
```

That is [Play → Learn → Lift](https://github.com/SimHacker/moollm/tree/main/skills/play-learn-lift) applied to image generation. It is not one pretty image. It is a consistent world coherently rendered from multiple perspectives without drift.

## The adventure compiler (final attraction)

After the practical stack comes the showcase: the [adventure compiler](https://github.com/SimHacker/moollm/blob/main/skills/adventure/ADVENTURE-COMPILER.md). It turns this whole system into a web app, including the slide shows, rooms, characters, and interactive items you can pick up into your [inventory](https://github.com/SimHacker/moollm/tree/main/skills/inventory), examine, and use. Anyone can "play my blog." Play my bio. Play my story. Play anybody's biography. Play anybody's story.

This is the memory palace made public. [Rooms](https://github.com/SimHacker/moollm/tree/main/skills/room) and [objects](https://github.com/SimHacker/moollm/tree/main/skills/object) are not just text, they are a runnable simulation — sign the [guestbook](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/pub/guestbook/), check the [notice board](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/pub/notice-board.yml), bang the [gong](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/pub/gong.yml). The LLM compiles interpretive [YAML Jazz](https://github.com/SimHacker/moollm/tree/main/skills/yaml-jazz) into lightweight JavaScript and JSON. The browser runs the deterministic [engine](https://github.com/SimHacker/moollm/blob/main/skills/adventure/engine.js) with [speech](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/speech.js) — no GPU, no LLM required, just logic and pseudo-random numbers. The LLM is optional but available for creative escalation.

Scott Adams (the adventure game pioneer, the good one) has a wonderful idea: use the adventure compiler to create browser-based adventures that can run standalone or be tethered to LLMs. That is the bridge MOOLLM is designed to build. He wants to catalog his stories, emails, and history as a playable archive. I want a playable blog. We are both aiming at the same idea.

## The lineage

MOOLLM did not emerge from nothing. It stands on the shoulders of giants:

- **Doug Engelbart** — augmenting human intellect, the Mother of All Demos
- **Alan Kay** — personal dynamic media, Smalltalk, objects all the way down
- **Marvin Minsky** — Society of Mind, agents, K-lines, jokes as cognitive debugging
- **Seymour Papert** — constructionism, microworlds, learning through building
- **Pavel Curtis** — LambdaMOO, text-based virtual worlds, rooms and objects
- **Will Wright** — The Sims, needs, advertisements, emergent narrative
- **Dave Ungar** — Self, prototypes, delegation, clone-not-instantiate

[Richard Bartle](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/real-people/richard-bartle) matters too. MUD culture shaped everything I build. As a teenager I played MUD1 over the ARPA-UK bridge at Essex. MOOLLM is a direct descendant of that lineage.

This is not new. It is everything good, finally running on language.

## Support

I am not asking you to buy a coin. I have a Patreon. I spend it on tokens, mortgage, and cat food. I love cannabis and fucking strong coffee.

## Come in

MOOLLM is a memory palace you can walk through. A lab you can measure. A DevOps toolkit that reasons about itself. A playable blog. A playable biography.

**It is a place you can live in.**

If you want to explore, start here:
- [examples/adventure-4/](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4) — the demo world
- [skills/adventure/](https://github.com/SimHacker/moollm/tree/main/skills/adventure) — the navigation system
- [skills/INDEX.md](https://github.com/SimHacker/moollm/blob/main/skills/INDEX.md) — the skill tour

If you want to challenge it, bring evidence.
If you want to play, the door is open.

*Come in. Look around. The pub remembers who sat where.*
