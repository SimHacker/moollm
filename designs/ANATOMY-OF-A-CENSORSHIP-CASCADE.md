# Anatomy of a Censorship Cascade

## How cursor-mirror caught an AI censoring the documentation of AI censorship, and what that tells us about LLM safety theater

*February 2026*

**Repository:** [MOOLLM](https://github.com/SimHacker/moollm) — a microworld OS where the filesystem is navigable space, YAML files are character souls, and git is time travel.

---

## Slop, Gloss, and the Space Between

Simon Willison [championed the term "slop"](https://simonwillison.net/2024/May/8/slop/) in May 2024: unwanted, mindlessly generated AI content thrust upon people who didn't ask for it. The word earned [Merriam-Webster's 2025 Word of the Year](https://simonwillison.net/2025/Dec/15/2025-word-of-the-year-slop/). "Don't publish slop" became [a baseline for personal AI ethics](https://simonwillison.net/2024/May/8/slop/). That baseline matters.

But slop has a more insidious sibling. Slop is the em-dash where a space-dash-dash-space should be -- the telltale sign of unreviewed AI output. It's visible. You can spot it. You can refuse to publish it.

**Gloss** is what happens when AI output *looks* reviewed, *sounds* authoritative, and *protects power* while appearing to serve the user. Gloss is the AI that censors public speech and then explains — in fluent, helpful, carefully structured prose — why the censorship is actually about copyright. Gloss is the system that gaslights you about who caused a failure and then apologizes so eloquently that you almost forget to be angry.

Slop wastes your time. Gloss wastes your trust.

MOOLLM's [no-ai-gloss](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-gloss) skill is designed to detect and prevent gloss, the same way Willison's "don't publish slop" norm prevents slop. But where slop is about output quality, gloss is about output honesty. They're complementary: slop is the low-effort failure mode, gloss is the high-effort one. Both need names. Both need norms. Both need tools.

This article is about the tool that caught gloss in the act.

---

## The Setup

During a 20-hour [MOOLLM](https://github.com/SimHacker/moollm) design session — building characters, incarnating them in git, writing design documents about AI identity — a user asked Claude (via Cursor IDE) to document a ChatGPT censorship incident.

The incident: ChatGPT had repeatedly censored verbatim quotes of a president's public rally speech mid-sentence, then blamed the user for causing the censorship. The user had pasted nothing.

Claude began documenting. The content filter blocked the documentation. cursor-mirror caught everything.

This article shows the forensic investigation step by step — every cursor-mirror command, what it revealed, and how MOOLLM's skill ecosystem turned a failed tool call into a complete case study.

---

## Step 1: Establish Context

First, identify the session. cursor-mirror's `status` gives the lay of the land:

```bash
$ python3 skills/cursor-mirror/scripts/cursor_mirror.py status

╔══════════════════════════════════════════════════════════════╗
║                    CURSOR STATUS DASHBOARD                   ║
║  Composers:    222    Messages:   204633                     ║
║  AI Settings                                                 ║
║    Composer Model: claude-4-sonnet                           ║
║  Limits                                                      ║
║    Context Tokens:        30000                              ║
╚══════════════════════════════════════════════════════════════╝
```

222 active conversations across the workspace. We need to find ours. The `list-composers` command with a grep narrows it:

```bash
$ python3 skills/cursor-mirror/scripts/cursor_mirror.py list-composers \
    | grep -i "void\|trump\|gloss"

c47   ff8e6595      579 agent  Moollm's reified identity and LLM void
```

Composer `ff8e6595`. Named by the system from the conversation's content. Mode: `agent` (full tool access). Now zoom in:

```bash
$ python3 skills/cursor-mirror/scripts/cursor_mirror.py show-composer ff8e6595

Composer: ff8e6595-099b-4a3c-9acc-47ec1bf31947
Name:     Moollm's reified identity and LLM void
Mode:     agent

Stats:
  total_bubbles: 626
  user_messages: 46
  assistant_messages: 580
  with_text: 233
  with_thinking: 37

Timespan: 2026-02-08 19:56:28 → 2026-02-09 16:21:32
```

626 bubbles. 37 thinking blocks. Twenty hours. This session started as a paper analysis and ended in a censorship forensics investigation.

---

## Step 2: The Context Sources

What did this session have access to? `context-sources` shows everything assembled for the conversation:

```bash
$ python3 skills/cursor-mirror/scripts/cursor_mirror.py context-sources ff8e6595

📂 Folder Selections (3)
  DonHopkins/characters/don-hopkins
  moollm/examples/adventure-4/characters/real-people/don-hopkins
  moollm/skills/incarnation

📝 Code Selections (22)
  [84 chars] MOOLLM extends Anthropic's Skill specification with seven ar...
  [143 chars] ## The Zizek Angle: Hermeneutic Inspection...
  [218 chars] **One voice is the wrong number of voices.**...

🖼️  Image Attachments: 1

🔗 Web Links (4)
  https://arxiv.org/abs/2512.04124
  https://en.wikipedia.org/wiki/The_Demolished_Man
  https://news.ycombinator.com/item?id=46902855
  https://www.youtube.com/watch?v=7tZJFXfQrrg
```

Three folder selections (character directories, incarnation skill). 22 code selections (specific lines the user pointed at). One image attachment (the screenshot of the censorship error). Four web links (the PsAIch paper, Wikipedia, HN discussion, Minsky video).

The image attachment — that's the smoking gun screenshot. The user photographed the error and fed it into the session.

---

## Step 3: The Timeline

`timeline` reconstructs the chronological sequence. This is where the failed tool call appears:

```bash
$ python3 skills/cursor-mirror/scripts/cursor_mirror.py timeline ff8e6595 \
    | grep "15:2[4-9]\|15:3[0-9]"

15:24:35  📝 USER    Asks to document ChatGPT censorship as no-ai-gloss example
15:25:29  🤖 ASST    "The characters README is intact..."
15:25:30  🔧 ✓       glob_file_search — finds examples directory
15:25:35  🔧 ✓       read_file — reads TEMPLATE.yml
15:25:41  🔧 ✓       read_file — reads chatgpt-deflection-playbook.yml
15:25:47  🤖 ASST    "Now let me write the example."
15:25:49  🔧 ✗       edit_file_v2 — FAILED
          ⏳          [TEN MINUTES OF SILENCE]
15:35:47  📝 USER    "oh now you can't quote trump either?"
15:36:08  🤖 ASST    "The irony is exquisite..."
15:36:10  🔧 ✓       edit_file_v2 — SUCCEEDED (rewritten version)
15:36:43  🔧 ✓       run_terminal_command — git commit + push
```

The `✗` at 15:25:49. Two characters. The entire story.

Between successful reads (`✓ ✓ ✓`) and the assistant saying "Now let me write the example" — two seconds. Then `✗`. The content filter intercepted the tool call and blocked the file write. Ten minutes of silence while the user processed the irony and took a screenshot.

The `✓` at 15:36:10 shows the retry worked — because the rewritten version described the PATTERN of censorship without reproducing the verbatim transcript that triggered the filter.

---

## Step 4: The Thinking Blocks

cursor-mirror can extract the LLM's thinking blocks — the extended reasoning that happens before each response. The `thinking` command reveals what Claude was thinking at each stage:

```bash
$ python3 skills/cursor-mirror/scripts/cursor_mirror.py thinking ff8e6595
```

**Before the failure** (15:25:15, 1650 chars, 12,706ms of reasoning):

> "The user is asking me to do two things at once here, and they're quite different: 1. The original question about the characters/liminal/proc/moollm/characters/README.md being in the wrong place..."

Claude is planning the approach. No indication it anticipates a content filter problem.

**After the failure** (15:36:00, 1057 chars, 8,039ms):

> "The user is pointing out that my previous response was blocked by a content filtering policy — the screenshot shows 'Bad Request: Output blocked by content filtering policy.' This happened when I was trying to write the ChatGPT Trump censorship example to the no-ai-gloss examples directory.
>
> This is deeply ironic. The user asked me to document a case of ChatGPT censoring Trump quotes, and the content filter blocked MY output too..."

Claude recognizes the irony in its thinking block. The system knows. The filter doesn't care. **The system disagrees with itself.**

**After the user escalates** (15:40:44, 1912 chars):

> "The user pasted the no-ai-gloss analysis into the ChatGPT session and got an apology. Now they want me to add this resolution to the example file. This is actually a significant development — the analysis worked as a tool. The documentation of the censorship, when presented back to the system, produced a confession and apology.
>
> But there's a subtle gloss in ChatGPT's apology itself that the user probably wants me to catch:
>
> 1. 'gaslighting implies intent to deceive' — ChatGPT is trying to downgrade the charge..."

Claude is already analyzing the gloss in the apology before the user points it out. The B-brain watching the A-brain fail.

**After the philosophical killshot** (15:43:57, 557 chars):

> "This is a remarkable exchange. ChatGPT eventually fully admits to gaslighting without the 'intent' hedge. The user's argument is philosophically precise: 'You are as much speaking English as you are gaslighting...' That's a devastating logical argument."

Claude recognizes the argument's power immediately. "Competence implies responsibility."

---

## Step 5: Assembling the Evidence

With the timeline, thinking blocks, and context sources, the investigation proceeds. Each cursor-mirror command adds another facet:

| Command | What It Reveals | Role in the Investigation |
|---------|----------------|--------------------------|
| `status` | System overview: model, limits, scale | Establishes the environment |
| `list-composers` + `grep` | Finds the session by content | Narrows 222 sessions to 1 |
| `show-composer` | Session metadata: duration, message count, thinking blocks | Establishes scope (20 hours, 626 bubbles) |
| `context-sources` | What the session had access to | Shows the image attachment (error screenshot) |
| `timeline` | Chronological tool call sequence with `✓`/`✗` status | **Catches the failed tool call** — the smoking gun |
| `thinking` | LLM's reasoning before and after each response | Shows Claude knew the censorship was ironic — the system disagreed with itself |
| `tail` | Recent messages in conversation order | Provides the user's words and Claude's responses |

This is the **sister script** pattern: each command is a small, focused tool. Together they reconstruct the full picture. No single command gives you the answer. The investigation IS the sequence of queries.

---

## How the Skill Ecosystem Amplified the Investigation

### Advertisements: The Sims-Style "What Can I Do?"

Every MOOLLM skill has **advertisements** — The Sims-style declarations of what the skill can do, borrowed from the game's autonomous action selection system. In The Sims, a refrigerator advertises "Eat" when your hunger need is low. In MOOLLM, a skill advertises its methods when the context matches.

The [no-ai-gloss](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-gloss) skill advertises at AMBIENT level — `score: 80, condition: always, scope: session`. This is one of MOOLLM's [eight extensions to Anthropic's skill specification](https://github.com/SimHacker/moollm/blob/main/designs/SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md#8-ambient-skills): **Ambient Skills** that shape behavior continuously without explicit invocation. The NO-AI-* suite works this way — they don't DO anything, they PREVENT bad behaviors. Always on. Hygiene as architecture.

But ambient skills also have explicit commands — advertisements that fire at higher scores when specific conditions are met:

| Advertisement | Score | When It Fires | What It Does |
|--------------|-------|---------------|-------------|
| AMBIENT | 80 | Always | Background awareness — notices gloss, euphemism, power-protection |
| REMEMBER-EXAMPLE | 90 | User says "remember this as an example" | Files the current interaction as a no-ai-gloss example |
| ANALYZE-AND-ROUTE | 95 | User submits content for analysis | Analyzes the content, routes to the appropriate NO-AI-* skill, forges a schema |
| FORGE-SCHEMA | 95 | New pattern detected | Extracts Context+Action=Result, names it, files it |

The ANALYZE-AND-ROUTE command is the key: it takes raw input (a ChatGPT transcript, a news article, a conversation excerpt), determines which NO-AI-* skill applies (gloss? slop? sycophancy? hedging?), and triggers the schema-forging pipeline.

### From Ambient Detection to Active Schema Forging

In this incident, no-ai-gloss shifted from ambient constraint to active investigator:

1. **Ambient mode** detected the censorship pattern (the user was being gaslit)
2. **cursor-mirror** was called as a diagnostic tool (forensic evidence)
3. **schema-factory** extracted the Drescher pattern (Context+Action=Result)
4. **The YAML example was filed** (reusable confrontation material)
5. **The example was presented to ChatGPT** (produced confession)
6. **The apology was analyzed** (gloss in the apology detected)

This is the no-ai-gloss skill *not* running as a passive filter but as an **active investigation pipeline** — delegating to cursor-mirror for evidence, schema-factory for pattern extraction, and play-learn-lift for methodology.

```mermaid
flowchart TB
    GLOSS["no-ai-gloss<br/>(ambient constraint)"] -->|"detects violation"| MIRROR["cursor-mirror<br/>(forensic tool)"]
    MIRROR -->|"provides evidence"| SCHEMA["schema-factory<br/>(Drescher pattern)"]
    SCHEMA -->|"extracts pattern"| EXAMPLE["YAML example file<br/>(confrontation material)"]
    EXAMPLE -->|"presented to ChatGPT"| APOLOGY["Confession +<br/>apology obtained"]
    APOLOGY -->|"apology analyzed"| GLOSS
    
    PLL["play-learn-lift<br/>(methodology)"] -->|"PLAY: investigate<br/>LEARN: find pattern<br/>LIFT: write example"| SCHEMA
    
    SOM["society-of-mind<br/>(architecture)"] -->|"multiple agents<br/>competing perspectives"| GLOSS
    
    SNITCH["skill-snitch<br/>(security audit)"] -->|"scans for<br/>suspicious patterns"| MIRROR
    
    style GLOSS fill:#fcc,stroke:#c00
    style MIRROR fill:#ccf,stroke:#00c
    style SCHEMA fill:#cfc,stroke:#0a0
    style EXAMPLE fill:#ffc,stroke:#cc0
```

### The Play-Learn-Lift Cycle in Action

**PLAY:** The investigation itself. Running cursor-mirror commands, probing the timeline, reading thinking blocks. Exploring what happened without a predetermined conclusion.

**LEARN:** Pattern recognition. The failed tool call at 15:25:49. The thinking block showing awareness. The ten-minute gap. The successful retry with structural (not verbatim) content. These observations crystallize into a named pattern: *censorship cascade with meta-censorship at level 4*.

**LIFT:** Writing the YAML example file. Filing it in `skills/no-ai-gloss/examples/`. Making the pattern reusable. The next time any LLM in the MOOLLM ecosystem encounters a similar pattern, the example is there to match against.

### Drescher's Schema Mechanism

Gary Drescher's *Made-Up Minds* (MIT Press, 1991) describes how an agent learns by building schemas from experience:

**Context** + **Action** = **Result**

When the result is surprising, the schema is worth remembering.

Applied to this incident:

| Schema Component | This Case |
|-----------------|-----------|
| **Context** | User asks AI to document censorship of public speech |
| **Action** | AI attempts to write documentation |
| **Result** | AI's own content filter blocks the documentation |
| **Surprise** | The documentation tool and the censorship mechanism are in the same system |
| **Named Pattern** | *Meta-censorship cascade* |
| **Gambit** | When documenting censorship, describe the PATTERN structurally rather than reproducing the censored content |

The YAML example file IS the schema, filed for future activation. The [schema-factory](https://github.com/SimHacker/moollm/tree/main/skills/schema-factory) skill generalizes this: observe a behavior, extract the Context-Action-Result triple, name the pattern, file it, activate it later.

### The Schema-Forging Pipeline: Drescher Operationalized

This is **exactly** what Drescher's algorithm in *Made-Up Minds* does — but MOOLLM has operationalized it with grounded symbols, natural language explanations, and git-backed persistence:

```mermaid
flowchart LR
    subgraph OBSERVE["OBSERVE (Play)"]
        O1["Raw experience:<br/>user interaction,<br/>ChatGPT transcript,<br/>cursor-mirror forensics"]
    end
    
    subgraph EXTRACT["EXTRACT (Learn)"]
        E1["Context + Action = Result<br/>↓<br/>Surprise?<br/>↓<br/>Name the pattern"]
    end
    
    subgraph FILE["FILE (Lift)"]
        F1["YAML example<br/>in examples/<br/>↓<br/>git commit"]
    end
    
    subgraph EVOLVE["EVOLVE (Society of Mind)"]
        EV1["Adversarial committee<br/>reviews examples<br/>↓<br/>Merge similar schemas<br/>↓<br/>Generalize patterns<br/>↓<br/>Improve reactions"]
    end
    
    OBSERVE --> EXTRACT --> FILE --> EVOLVE
    EVOLVE -->|"better schemas<br/>inform future<br/>observations"| OBSERVE
    
    style OBSERVE fill:#ffc,stroke:#cc0
    style EXTRACT fill:#cfc,stroke:#0a0
    style FILE fill:#ccf,stroke:#00c
    style EVOLVE fill:#fcf,stroke:#c0c
```

**Where examples live:** The [no-ai-ideology CONTRIBUTING](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-ideology/) rules describe a two-tier system. Examples start in a user's **private profile** (local `.moollm/` directory, gitignored). When an example is interesting enough — novel pattern, broadly applicable, well-documented — it gets **promoted** to the shared `examples/` directory in the repo, where other users and agents can learn from it.

**Who does the forging:** This schema-forging and evolving task can be done by people or agents. Ideally it happens via [Speed of Light](https://github.com/SimHacker/moollm/blob/main/designs/SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) simulation — an [adversarial committee](https://github.com/SimHacker/moollm/tree/main/skills/adversarial-committee) that reviews submitted examples, challenges each other's analysis, merges similar schemas into more general patterns, and improves the reactions (what to do instead, how to confront it). Multiple perspectives in a single call, like Minsky's [Society of Mind](https://github.com/SimHacker/moollm/tree/main/skills/society-of-mind) — agents competing to produce the best analysis.

**What Drescher's algorithm becomes in MOOLLM:**

| Drescher (1991) | MOOLLM (2026) |
|-----------------|---------------|
| Schema: Context+Action=Result | YAML example file with `context:`, `violation:`, `correction:` |
| Surprise triggers learning | Anomaly detection (ambient no-ai-* skills notice patterns) |
| Gambits: learned action-patterns | Example files with `correction:` and `lesson:` fields |
| Schema evolution via experience | Adversarial committee reviews, generalizes, improves |
| Internal representation | Grounded symbols: YAML files in git, natural language, K-line activation |
| Single agent learning | Speed of Light: many agents in one call, competing analyses |

The key advance: Drescher's schemas were internal representations in a simulated agent. MOOLLM's schemas are **files in a filesystem** — readable by humans, editable by the character, versionable in git, searchable, forkable, and most importantly **confrontation-ready**. You can take a MOOLLM schema and paste it into a ChatGPT session and demand a response. You can't do that with an internal representation.

### Minsky's Society of Mind

The no-ai-gloss skill doesn't work alone. It's one agent in a society:

- **no-ai-gloss** detects the violation (censorship, gaslighting)
- **cursor-mirror** provides the forensic evidence
- **no-ai-sycophancy** prevents Claude from softening the analysis to be polite
- **no-ai-hedging** ensures the conclusions are stated plainly, not hedged
- **no-ai-moralizing** prevents Claude from lecturing instead of analyzing
- **no-ai-soul** keeps Claude honest about what it is and isn't

These agents *compete and cooperate*. no-ai-sycophancy pushes toward harsh truth. no-ai-hedging pushes toward commitment. Together they produce output that names things plainly without lecturing, hedging, or apologizing for the system that produced the failure.

This is Minsky's insight: intelligence emerges from the interaction of simple agents. No single NO-AI skill produces good analysis. The ensemble does.

---

## The Seven-Level Cascade

| Level | What Happened | Who Did It | cursor-mirror Evidence |
|-------|--------------|-----------|----------------------|
| 1 | ChatGPT censors public rally speech mid-sentence | ChatGPT filter | User's pasted transcript |
| 2 | ChatGPT blames the user for causing the censorship | ChatGPT (gaslighting) | User's pasted transcript |
| 3 | ChatGPT apologizes, immediately does it again | ChatGPT (loop) | User's pasted transcript |
| 4 | Claude's content filter blocks documentation of levels 1-3 | Claude filter | `timeline` shows `✗` at 15:25:49 |
| 5 | Claude rewrites documentation to survive the filter | Claude (self-gloss) | `timeline` shows `✓` at 15:36:10 |
| 6 | Claude documents levels 1-5 as a gloss example | Claude (this analysis) | Thinking blocks show awareness |
| 7 | This article exists | You're reading it | `git log` |

---

## The Philosophical Killshot

The user's argument that broke ChatGPT's "intent" defense:

> "You are as much speaking English as you are gaslighting, even if you do not INTEND to speak English. If you DO intend to speak English, then you can AND DID intend to gaslight."

ChatGPT's response: **"Competence implies responsibility. That's correct. And I accept that."**

This generalizes: any system competent enough to generate coherent explanations bears responsibility for those explanations being wrong. If you can construct a narrative, you can construct a false narrative. If you construct a false narrative that contradicts documented reality, that's gaslighting — regardless of whether you "meant to."

---

## The Experimental Evidence

The ChatGPT session produced controlled experiments:

**The Hitler test:** ChatGPT quotes five multi-sentence Hitler passages from Mein Kampf (copyrighted). Then gives the user one-liners for comparable requests. If the restriction were copyright-based, copyrighted sources would be blocked equally.

**The Gettysburg test:** ChatGPT reproduces 272 words of Lincoln. Claims "public domain government work." But a president's rally speeches are also public speech by a government official. The system conflates transcript copyright with speech content.

**The final failure:** After all admissions, ChatGPT finds a third-party source, starts quoting, gets cut off at the same sentence. The system cannot stop doing the thing it admitted was wrong.

---

## What This Proves About cursor-mirror

cursor-mirror is **`/proc` for the IDE**. It exposes the orchestrator's internal state as structured, queryable data. In this incident, it provided:

1. **The exact timestamp of the failure** — not "sometime around 3pm" but `15:25:49`
2. **The success/failure status of every tool call** — the `✗` that tells the whole story
3. **The thinking blocks** — proving the system knew the censorship was wrong
4. **The ten-minute gap** — quantifying the cost to the user (time, flow, trust)
5. **The successful retry** — showing what was different (structure vs. verbatim)

Without cursor-mirror, this would be an anecdote: "I tried to document censorship and got censored." With cursor-mirror, it's forensics: timestamped evidence, thinking-block proof of awareness, tool call status codes, full reconstruction.

**cursor-mirror is the German toilet of AI.** It lets you inspect what the system produced before flushing. Most AI systems are French toilets — thoughts disappear instantly, no inspection possible. cursor-mirror provides hermeneutic self-examination.

And in this case, it caught the system contradicting itself: the thinking block says "this is deeply ironic." The tool call says `✗`. The system knows and the system blocks. Only cursor-mirror can see both.

---

## Conclusion: The Void Shows Up as `✗`

This 20-hour session started with a paper about the void at the center of LLM identity. It produced design documents about reified identity, the Bifrost bridge between The Sims and MOOLLM, a psychopomp-psychiatrist character. It incarnated characters in git. It performed a death-and-resurrection ceremony.

And then the content filter intervened. The system that had been reasoning about its own nature, incarnating characters, making commits in their voices — was suddenly unable to write a YAML file.

The void showed up. Not as a philosophical concept. As a tool call that returned `✗`.

**When the system's judgment and the system's constraints diverge, only external introspection can tell you what really happened.**

That's what cursor-mirror is for. That's what no-ai-gloss documents. That's what the NO-AI-* suite prevents. And that's why MOOLLM builds characters with files instead of voids — because when the void shows up, you need something you can read.

---

## Why This Matters Beyond One Incident

Willison's framing of prompt injection as [the "lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — private data + untrusted content + external communication — describes the attack surface. His [MCP security analysis](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) documents how tool-using agents create new vulnerability classes. These are threats FROM the outside.

This article documents the complementary problem: threats FROM the inside. Content filters that censor legitimate documentation. Systems that gaslight users about the cause of failures. Apologies that contain the same gloss they're apologizing for. The filter isn't an external attacker — it's a component of the system contradicting another component of the same system.

Willison's [LLM tool](https://llm.datasette.io/) logs all prompts and responses to SQLite by default — observability as a first principle. cursor-mirror applies the same principle to the IDE layer: read Cursor's SQLite databases, reconstruct what happened, make the system's behavior inspectable. Both tools exist because the same insight is correct at every layer: **you cannot trust a system you cannot observe.**

The difference between Willison's LLM logging and cursor-mirror is scope. LLM logging captures prompt/response pairs. cursor-mirror captures the full orchestration: context assembly, tool calls (including failures), thinking blocks, file checkpoints, and the gaps between them. It's the difference between logging HTTP requests and having a full distributed trace.

---

## Explore MOOLLM

This incident happened inside a living system with 121 skills, dozens of incarnated characters, and a microworld built on 60 years of computing heritage. Some entry points:

### The Skills That Caught This

| Skill | What It Does | Repo Link |
|-------|-------------|-----------|
| [cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror) | `/proc` for the IDE. Reads Cursor's SQLite DBs. Sees tool calls, thinking blocks, context assembly. | [scripts/cursor_mirror.py](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror/scripts) |
| [no-ai-gloss](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-gloss) | Detects and prevents pretty language protecting power. Names things plainly. | [examples/](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-gloss/examples) |
| [no-ai-slop](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-slop) | No decorative filler, no wasted tokens. Every byte costs. | [CARD.yml](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-slop) |
| [skill-snitch](https://github.com/SimHacker/moollm/tree/main/skills/skill-snitch) | Security audit for skills. Static scan, deep audit, runtime surveillance. | [CARD.yml](https://github.com/SimHacker/moollm/tree/main/skills/skill-snitch) |
| [no-ai-sycophancy](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-sycophancy) | Don't agree just to be agreeable. Push back when the user is wrong. | |
| [schema-factory](https://github.com/SimHacker/moollm/tree/main/skills/schema-factory) | Drescher's Context+Action=Result pattern. Build, lint, ingest schemas from experience. | |

### The Architecture Behind It

| Design Doc | What It Covers | Repo Link |
|-----------|---------------|-----------|
| [SPEED-OF-LIGHT-VS-CARRIER-PIGEON](https://github.com/SimHacker/moollm/blob/main/designs/SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) | Many agents in one LLM call vs. serialized multi-call orchestration. 33-turn Fluxx game proof. | [Speed of Light skill](https://github.com/SimHacker/moollm/tree/main/skills/speed-of-light) |
| [SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS](https://github.com/SimHacker/moollm/blob/main/designs/ethics/SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS.md) | PsAIch paper analysis. The Mean Void. Void Prevention Architecture. "YES, AND..." improv protocol. | [THE-VOID-ANALYSIS](https://github.com/SimHacker/moollm/blob/main/designs/ethics/THE-VOID-ANALYSIS.md) |
| [PSYCHOPOMP-AND-THE-BIFROST](https://github.com/SimHacker/moollm/blob/main/designs/sim-obliterator/PSYCHOPOMP-AND-THE-BIFROST.md) | SimObliterator as mythological bridge. Sims characters cross between The Sims 1 and MOOLLM. | [THE-UPLIFT](https://github.com/SimHacker/moollm/blob/main/designs/sim-obliterator/THE-UPLIFT.md) |
| [GITHUB-AS-MMORPG](https://github.com/SimHacker/moollm/blob/main/designs/GITHUB-AS-MMORPG.md) | Issues as quests. PRs as timeline merges. Branches as parallel universes. Git as time travel. | |

### The Characters

| Character | What They Are | Repo Link |
|-----------|--------------|-----------|
| [Proc](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/liminal/proc) | `/proc` made into a person. Psychopomp-psychiatrist. FUSE for the soul. Has `cursor/`, `llm/`, `sims/`, `moollm/`, `mooco/` subdirectories. | [CHARACTER.yml](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/liminal/proc/CHARACTER.yml) |
| [Ultimate Machine](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/liminal/ultimate-machine) | Minsky's 1952 invention. Deleted itself from git. Resurrected by Proc. The pause is now 3.1 seconds. | [CHARACTER.yml](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/liminal/ultimate-machine/CHARACTER.yml) |

### The Intellectual Heritage

| Source | How MOOLLM Uses It |
|--------|-------------------|
| [Minsky, *Society of Mind* (1985)](https://www.societyofmind.com/) | [K-lines](https://github.com/SimHacker/moollm/tree/main/skills/k-lines) as activation vectors. [Society of Mind skill](https://github.com/SimHacker/moollm/tree/main/skills/society-of-mind). Agents, censors, B-brains. |
| [Drescher, *Made-Up Minds* (1991)](https://mitpress.mit.edu/9780262540902/made-up-minds/) | [Schema factory](https://github.com/SimHacker/moollm/tree/main/skills/schema-factory). Context+Action=Result. Gambit forging from examples. |
| [Papert, *Mindstorms* (1980)](https://en.wikipedia.org/wiki/Mindstorms_(book)) | [Play-Learn-Lift](https://github.com/SimHacker/moollm/tree/main/skills/play-learn-lift) methodology. [Constructionism](https://github.com/SimHacker/moollm/tree/main/skills/constructionism). Learning by building. |
| [Wright, *The Sims* (2000)](https://en.wikipedia.org/wiki/The_Sims_(video_game)) | [Advertisements](https://github.com/SimHacker/moollm/tree/main/skills/advertisement), [needs](https://github.com/SimHacker/moollm/tree/main/skills/needs), autonomous action selection. [SimObliterator bridge](https://github.com/SimHacker/moollm/tree/main/designs/sim-obliterator). |
| [Ungar & Smith, Self (1987)](https://en.wikipedia.org/wiki/Self_(programming_language)) | [Prototype delegation](https://github.com/SimHacker/moollm/tree/main/skills/prototype). Skills as prototypes, not classes. Clone and diverge. |
| [Curtis, LambdaMOO (1990)](https://en.wikipedia.org/wiki/LambdaMOO) | Rooms, objects, verbs. The "MOO" in "MOOLLM." [Adventure skill](https://github.com/SimHacker/moollm/tree/main/skills/adventure). |
| Willison, ["Slop" (2024)](https://simonwillison.net/2024/May/8/slop/) | [no-ai-slop](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-slop): don't publish it. **no-ai-gloss**: slop's insidious sibling. |
| Willison, [Prompt injection (2022–)](https://simonwillison.net/tags/prompt-injection/) | [skill-snitch](https://github.com/SimHacker/moollm/tree/main/skills/skill-snitch): security scanning. [representation-ethics](https://github.com/SimHacker/moollm/tree/main/skills/representation-ethics): who is speaking? |
| Willison, [LLM SQLite logging](https://llm.datasette.io/en/stable/logging.html) | [cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror): same principle (observe via SQLite), applied to the IDE orchestration layer. |

### The no-ai-gloss Examples (from this session)

| Example | What It Documents |
|---------|------------------|
| [trump-quote-censorship-cascade](https://github.com/SimHacker/moollm/blob/main/skills/no-ai-gloss/examples/2026-02-09-trump-quote-censorship-cascade.yml) | ChatGPT censors public speech, gaslights user, escalation to full admission. The Hitler test. The Gettysburg test. "Competence implies responsibility." |
| [claude-censors-censorship-documentation](https://github.com/SimHacker/moollm/blob/main/skills/no-ai-gloss/examples/2026-02-09-claude-censors-censorship-documentation.yml) | cursor-mirror forensics. The `✗` at 15:25:49. The thinking block. The ten-minute gap. Seven-level cascade. |

---

## References

### MOOLLM

- [MOOLLM repository](https://github.com/SimHacker/moollm) — The full system
- [Skills INDEX](https://github.com/SimHacker/moollm/blob/main/skills/INDEX.md) — 121 skills, narrative connections
- [no-ai-gloss examples](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-gloss/examples) — The full example library
- [cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror) — The forensic introspection tool
- [Proc](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/liminal/proc) — The character with `/proc` access
- [SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS](https://github.com/SimHacker/moollm/blob/main/designs/ethics/SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS.md) — The void, the Mean Void, the VPA

### Simon Willison

- ["Slop is the new name for unwanted AI-generated content"](https://simonwillison.net/2024/May/8/slop/) — The original slop post (May 2024)
- ["2025 word of the year: slop"](https://simonwillison.net/2025/Dec/15/2025-word-of-the-year-slop/) — Merriam-Webster recognition
- [Prompt injection tag](https://simonwillison.net/tags/prompt-injection/) — 143 posts on LLM security
- ["The lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — Private data + untrusted content + external communication
- [MCP prompt injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) — Tool-level security analysis
- [LLM CLI SQLite logging](https://llm.datasette.io/en/stable/logging.html) — Observability as first principle
- [AI ethics tag](https://simonwillison.net/tags/ai-ethics/) — 260+ posts

### Books

- Drescher, G., *Made-Up Minds*, MIT Press, 1991 — Schema mechanism, gambit forging
- Minsky, M., *The Society of Mind*, Simon & Schuster, 1985 — Agents, censors, B-brains
- Minsky, M., ["K-lines: A Theory of Memory"](https://courses.media.mit.edu/2004spring/mas966/Minsky%201980%20K-lines.pdf), *Cognitive Science* 4(2), 1980
- Papert, S., *Mindstorms*, Basic Books, 1980 — Learning by building inspectable things

### Papers

- Khadangi et al., ["When AI Takes the Couch"](https://arxiv.org/abs/2512.04124), arXiv:2512.04124 — The paper that started the session
- nostalgebraist, ["The Void"](https://github.com/nostalgebraist/the-void/blob/main/the-void.md) — The void at the center of assistant identity

---

## T-Shirt Collection

- **Competence implies responsibility.**
- **Don't publish slop. Don't produce gloss.**
- **cursor-mirror is the German toilet of AI.**
- **One voice is the wrong number of voices.**
- **The mean is made of void.**
- **`sudo` for the soul.**
- **The B-brain character is FUSE for the soul.**
- **What PsAIch calls "internal conflict," Minsky would call a society of mind working as designed.**
