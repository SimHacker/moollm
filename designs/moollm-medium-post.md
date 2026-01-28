# MOOLLM: Anti-Slop, Anti-Gloss, Pro-Evidence

Is this AI-generated? Parts of it, sure. So what? I am not hiding it, and I am not apologizing. I use a brutalist GitHub-style workflow: I write in repo-structured markdown and paste into Medium's editor. It saves time, it is readable, and it is good enough. I am not here to impress you with artisanal typography. I am here to show you a system.

This is not "prompt, publish, profit."
This is "prompt, inspect, criticize, refine, repeat."
Then measure.
And no, this is not vibe coding. This is anti-slop engineering.

## AI slop vs AI gloss (gloss is worse)

AI slop is mostly syntactic — annoying — repetitive — low-value. It wastes time and looks dumb, but it is usually harmless.

AI gloss is perniciously worse. It is persuasive-sounding nonsense that hides weak reasoning behind smooth prose. It feels competent, sounds confident, and slides past your defenses. It often leaps to the defense of oligarchs and fascist leaders because the smoothest "reasonable" framing usually protects power. MOOLLM is built to fight gloss and reduce slop. It forces structure, manages focus, exposes evaluation, and keeps receipts.

## What is MOOLLM?

MOOLLM is a microworld OS for LLM-driven tools, documents, simulations, and playable spaces. The filesystem in git is the world. Rooms are directories. Objects are files. [Characters](https://github.com/SimHacker/moollm/tree/main/skills/character) are structured. The LLM navigates it like a player but understands the YAML, the comments, the intent. See [kernel/ARCHITECTURE.md](https://github.com/SimHacker/moollm/blob/main/kernel/ARCHITECTURE.md) for the technical foundation and [skills/INDEX.yml](https://github.com/SimHacker/moollm/blob/main/skills/INDEX.yml) for the skill registry.

It is a serious tool for measurement, evidence, and reproducible experimentation, not a text generator. It makes you show your work.

## Not "self-improvement." Self-inheritance.

Calling this "self-improvement" misses the point. MOOLLM deeply inherits from Self, the language and the prototype model. It is not the "improve yourself" trope. It is the Self prototype pun, fully intentional. The LLM makes that recursion practical in ways classic Self could not do. See [skills/prototype/SKILL.md](https://github.com/SimHacker/moollm/blob/main/skills/prototype/SKILL.md) for how delegation and inheritance work.

## The core loop: experiment, evidence, iteration

MOOLLM's heart is experiment:

- Simulate
- Evaluate
- Iterate
- Analyze

Experiments are stable. Runs are parameterized. Outputs are numbered, scored, compared, and archived. This is measurement, not vibes. If you want the ritual version, read [SHORT-DURATION-PERSONAL-EVALUATORS.md](https://github.com/SimHacker/moollm/blob/main/designs/eval/SHORT-DURATION-PERSONAL-EVALUATORS.md) and the ShorDurPerEval doctrine.

## Multi-agent debate, not median blah

When you want a decision, you do not want the median of bland. You want contrasting viewpoints with rules of order and a rubric. Mike Gallaher's contributions to debate formats, review protocols, and "how to avoid the median" are baked into the system. Multiple agents, declared biases, explicit rubrics. See [skills/adversarial-committee/](https://github.com/SimHacker/moollm/tree/main/skills/adversarial-committee) and [skills/debate/](https://github.com/SimHacker/moollm/tree/main/skills/debate). 

It is better to model individual characters with diverse viewpoints who talk and argue, than to construct a solitary, shapeless, slogan-stuffed chat golem — a bland, bloodless blob of amorphisms: meaningless Hallmark greeting card slogans, .cursor file wishes and prayers to the LLM God to be concise, only say true things, be neutral and unbiased, fair and balanced, whilst smiting mine enemies. MOOLLM is evaluation with teeth. See [skills/incarnation/](https://github.com/SimHacker/moollm/tree/main/skills/incarnation) for gold-standard character creation, or meet [Henk the bartender](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/fictional/henk) and [Marieke the budtender](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/fictional/marieke).

## Practical first: real work, real ops

I use MOOLLM at Leela AI for real DevOps, GitOps, and code work. I am a sysadmin and Emacs hacker from the old school who upgraded into the modern era. It is not a toy. It runs our cloud operations on GCS and it runs our Edgebox migration as we move capability from cloud to custom on‑site systems. It is for infrastructure, code development, and operational reality, not a demo.

I point to the constellation of possible mashups -- MOOMACS / LLMACS / EMOO / ELLM -- MOO + LLM + Emacs energy. Emacs matters because the shell matters: run commands, parse output, SSH, fix remote state. MOOLLM in Cursor gives me that Emacs‑shell power with terminal windows and a chat‑embedded terminal. It is the same kind of extensible, scriptable environment, but the "objects" can reason about themselves.

I am a serial specialist and a parallel generalist. This is how I interoperate.

## Cursor-Mirror: mission-critical feedback, not philosophy

Before the artsy stuff, here is the body-slam of practicality: [cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror). This is semantic text + SQL feedback about what the system actually did. It is not a metaphor. It is a diagnostic instrument.

What can cursor-mirror see? Everything. Even things the chat forgot. Search full chat history. Query SQLite databases for workspaces, chats, bubbles, context assembly, prompts, thinking blocks, output, summaries, file references, tool calls, MCP calls, etc. Every action Cursor takes is now queryable and searchable. You can grep your own reasoning, timeline your own tool calls, and audit what context went into any decision. Perform a survey of how many FUCKs were given and in what contexts and why.

With cursor-mirror you get tool-call provenance, timeline reconstruction, post-mortems, failure analysis, and security auditing. It powers skills like [skill-snitch](https://github.com/SimHacker/moollm/tree/main/skills/skill-snitch), deep-snitch, transcript analysis, and untrusted-source monitoring. 

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

[Speech](https://github.com/SimHacker/moollm/tree/main/skills/speech) input/output enables semantic audio feedback (think Cartman in the "Alexa! Hey Siri! OK Google!" South Park episode). The speech skill provides TTS/STT across platforms: [speech.js](https://github.com/SimHacker/moollm/blob/main/skills/adventure/dist/speech.js) for browser webapps, the `say` command for macOS terminal, and cloud APIs for production. Characters get persistent voice assignments. Image input/output enables semantic visual feedback (think video feedback art). Text and SQL loops enable semantic introspection and post-mortems (cursor-mirror). MOOLLM is a crossbar for these loops. It is practical and it is weird, and those two things are not in conflict.

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
The visualizer skill generates two "stereo" text prompts that reinforce each other: `PHOTO.yml` (structure: composition, lighting, objects) and `PHOTO.md` (interpretation: mood, narrative, sensory detail). Both go to the image generator. The output image then gets analyzed by computer vision, which extracts layers of semantic YAML Jazz interpretation along multiple dimensions (technical, narrative, cultural, phenomenology, absurdist).

The evaluation feedback loop: does the mining analysis match the intended image described by the prompts? If not, detect generation failure, edit prompts to avoid problems, refine, regenerate, and repeat.

```
stereo prompts → image generator → generated image → vision analysis → YAML Jazz layers
       ↑                                                                      ↓
       └──────────────── evaluation: match intent? retry if not ──────────────┘
```

That is [Play → Learn → Lift](https://github.com/SimHacker/moollm/tree/main/skills/play-learn-lift) applied to image generation. It is not one pretty image. It is a consistent world coherently rendered from multiple perspectives without drift.

## The adventure compiler (final attraction)

After the practical stack comes the showcase: the [adventure compiler](https://github.com/SimHacker/moollm/blob/main/skills/adventure/ADVENTURE-COMPILER.md). It turns this whole system into a web app, including the slide shows, rooms, characters, and interactive items you can pick up into your [inventory](https://github.com/SimHacker/moollm/tree/main/skills/inventory), examine, and use. Anyone can "play my blog." Play my bio. Play my story. Play anybody's biography. Play anybody's story.

This is the memory palace made public. [Rooms](https://github.com/SimHacker/moollm/tree/main/skills/room) and [objects](https://github.com/SimHacker/moollm/tree/main/skills/object) are not just text, they are a runnable simulation — sign the [guestbook](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/pub/guestbook.yml), check the [notice board](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/pub/notice-board.yml), bang the [gong](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/pub/gong.yml). The LLM compiles interpretive [YAML Jazz](https://github.com/SimHacker/moollm/tree/main/skills/yaml-jazz) into lightweight JavaScript and JSON. The browser runs the deterministic engine — no GPU, no LLM required, just logic and pseudo-random numbers. The LLM is optional but available for creative escalation.

Scott Adams (the adventure pioneer, the good one) has a wonderful idea: use the adventure compiler to create browser-based adventures that can run standalone or be tethered to LLMs. That is the bridge MOOLLM is designed to build. He wants to catalog his stories, emails, and history as a playable archive. I want a playable blog. We are both aiming at the same idea.

[Richard Bartle](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4/characters/real-people/richard-bartle) matters here too. MOO culture shaped everything I build. As a teenager I played over the ARPA-UK bridge at Essex. MOOLLM is a direct descendant of that lineage.

## This is not Gas Town

Gas Town has energy. It also has deep structural flaws: it prioritizes vibe over evidence and collapses into performance. I am not here to dunk on anyone, but I am here to say that MOOLLM is the opposite. It is declarative, measured, and explicit. It is not hype. It is a method.

## Funding, not hype

I am not asking you to buy a coin. I do have a Patreon. I will spend it on tokens, not cryptocurrencies. Mortgage and cat food. I do not get drunk and post. I do love cannabis and fucking strong coffee.

## Close the loop

MOOLLM is a system for iterative generation, reflection, refinement, and proof. It is anti-slop and anti-gloss. It is a memory palace you can walk through and a lab you can measure. It is a practical DevOps toolkit and a weird performance engine. It is a playable blog. It is a playable biography.

If you want to see it, start here: [examples/adventure-4/](https://github.com/SimHacker/moollm/tree/don-adventure-4-run-1/examples/adventure-4) and [skills/adventure/](https://github.com/SimHacker/moollm/tree/main/skills/adventure).
If you want to challenge it, bring evidence.
If you want to play, there will be a door soon.
