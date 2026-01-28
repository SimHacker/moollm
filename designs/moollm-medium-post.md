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

MOOLLM is a microworld OS for LLM-driven tools, documents, simulations, and playable spaces. The filesystem in git is the world. Rooms are directories. Objects are files. Characters are structured. The LLM navigates it like a player but understands the YAML, the comments, the intent.

It is a serious tool for measurement, evidence, and reproducible experimentation, not a text generator. It makes you show your work.

## Not "self-improvement." Self-inheritance.

Calling this "self-improvement" misses the point. MOOLLM deeply inherits from Self, the language and the prototype model. It is not the "improve yourself" trope. It is the Self prototype pun, fully intentional. The LLM makes that recursion practical in ways classic Self could not do.

## The core loop: experiment, evidence, iteration

MOOLLM's heart is experiment:

- Simulate
- Evaluate
- Iterate
- Analyze

Experiments are stable. Runs are parameterized. Outputs are numbered, scored, compared, and archived. This is measurement, not vibes. If you want the ritual version, read [SHORT-DURATION-PERSONAL-EVALUATORS.md](https://github.com/SimHacker/moollm/blob/main/designs/eval/SHORT-DURATION-PERSONAL-EVALUATORS.md) and the ShorDurPerEval doctrine.

## Multi-agent debate, not median blah

When you want a decision, you do not want the median of bland. You want contrasting viewpoints with rules of order and a rubric. Mike Gallaher's contributions to debate formats, review protocols, and "how to avoid the median" are baked into the system. Multiple agents, declared biases, explicit rubrics. 

It is better to model individual characters with diverse viewpoints who talk and argue, than to construct a solitary, shapeless, slogan-stuffed chat golem — a bland, bloodless blob of amorphisms: meaningless Hallmark greeting card slogans, .cursor file wishes and prayers to the LLM God to be concise, only say true things, be neutral and unbiased, fair and balanced, whilst smiting mine enemies. MOOLLM is evaluation with teeth.

## Practical first: real work, real ops

I use MOOLLM at Leela for real DevOps, GitOps, and code work. I am a sysadmin and Emacs hacker from the old school who upgraded into the modern era. It is not a toy. It runs our cloud operations on GCS and it runs our Edgebox migration as we move capability from cloud to custom on‑site systems. It is for infrastructure, code development, and operational reality, not a demo.

I point to the constellation of possible mashups -- MOOMACS / LLMACS / EMOO / ELLM -- MOO + LLM + Emacs energy. Emacs matters because the shell matters: run commands, parse output, SSH, fix remote state. MOOLLM in Cursor gives me that Emacs‑shell power with terminal windows and a chat‑embedded terminal. It is the same kind of extensible, scriptable environment, but the "objects" can reason about themselves.

I am a serial specialist and a parallel generalist. This is how I interoperate.

## Cursor-Mirror: mission-critical feedback, not philosophy

Before the artsy stuff, here is the body-slam of practicality: `cursor-mirror`. This is semantic text + SQL feedback about what the system actually did. It is not a metaphor. It is a diagnostic instrument.

With `cursor-mirror` you get tool-call provenance, timeline reconstruction, post-mortems, failure analysis, and security auditing. It powers skills like `skill-snitch`, `deep-snitch`, transcript analysis, and untrusted-source monitoring. 

The crown jewel is `thoughtful-commitment`: git commits that capture context, not just changes. cursor-mirror sees NOW; git commit FREEZES it. When you commit, the LLM's reasoning — what it saw, what it thought, why it made each change — gets persisted into your git history. Six months later, you can ask "why did this line change?" and get the actual thinking, not a guess. It is archaeology with receipts.

This is not optional. It is mission-critical if you want LLM systems you can trust, improve, and defend.

## Media-independent feedback (tour + demo)

Underneath all the tooling is a media-independent idea: feedback loops between generation and analysis. It does not matter if the medium is text, image, or sound. You generate, observe, measure, revise. The loop is the point.

Here is the concrete tour: the [Lane Neverending Photo Archive](https://github.com/SimHacker/moollm/blob/don-adventure-4-run-1/examples/adventure-4/street/lane-neverending/slideshow/SLIDESHOW.md) is a five-location slideshow built from semantic stereo image prompt generation plus semantic vision mining layers (`PHOTO.yml` + `PHOTO.md` + `MINING-*.yml`). Two eyes, one image: the YAML provides structure (composition, lighting, objects, colors) while the Markdown provides interpretation (mood, narrative, sensory detail). The LLM synthesizes both into a coherent prompt that captures what words alone cannot. After generation, mining layers analyze the result across multiple lenses (technical, narrative, cultural, phenomenology, absurdist) and feed back into the next iteration.

The featured shots:

- **NO AI Tower** — A forty-foot neon statement on a one-story box. The sign is the tower. Rain-slick asphalt mirrors the glow. People misread it as a protest until they notice the pun: "NO AI" is a possessive, not a slogan. The building belongs to No's AI.
- **Leela Manufacturing (Dusk)** — The factory wears the neon spill like a jacket it did not ask for. Brick grid, warm lobby glow, industrial calm that makes the chaos across the street feel like theater.
- **ACME Surplus Tunnel Sequence** — Five frames, one joke, escalating consequences. The painted tunnel dares, the wall answers, and a cartoon coyote's inventory of impossible objects (umbrellas for past rain, binoculars that see events that have not happened) sits inside. Rico "Redline" Rojas exits through the mural in frame five, ignores the physics, flips off the photographer, and drives into the night.
- **Gezelligheid Grotto** — The pub is the soft landing. Warm windows, wet-stone reflections, jokes replayed, bruises iced. Two doors down, the Infinite Fountain keeps misbehaving.
- **Seymour Blooms (Ada II)** — Closed shop, lights on, the plant that should not be seen caught mid-surprise. Ada II's silhouette sits in the neon haze, a hot-boxed room caught mid-exhale. Rumor says she was a retired military AI rescued from a rainy dumpster, now devouring bad code instead of blood.

That is nine-plus images from five locations, all generated through the same loop: prompt, image, mine, rewrite, regenerate, compare. The ACME sequence demonstrates multi-frame coherence — one narrative across five generated images with consistent lighting, characters, and escalation. Ada II demonstrates emergent lore — a detail that grew into a character with backstory, rituals, and whispered secrets.

Speech input/output enables semantic audio feedback (think the Cartman in the "Alexa! Hey Siri! OK Google!" South Park episode). Image input/output enables semantic visual feedback (think video feedback art). Text and SQL loops enable semantic introspection and post-mortems (cursor-mirror). MOOLLM is a crossbar for these loops. It is practical and it is weird, and those two things are not in conflict.

## Cool stuff that actually works

### Adventure (Microworld OS)
The adventure system turns the filesystem into a navigable world. Rooms, objects, inventories, exits, and builder commands. It is a memory palace you can walk through, not a file tree you scroll.

### Experiment
Structured simulation plus evaluation with explicit rubrics and reproducible runs. It is how you prove things instead of hand-waving.

### Fluxx Chaos
A full Fluxx 4.0 engine with pluggable rules, append-only run histories, layered character simulation, and scoring across coherence dimensions. It is chaotic on purpose and still measurable. The game is not the point. The characters are. Fluxx is the excuse to make them care and react.

### Turing Chess and Revolutionary Chess
We are not simulating chess. We are simulating the performance of chess. Fixed move replays plus layered inner monologue, audience, narrator, and then a Revolutionary Chess plugin that flips the rules after checkmate. It is game design as experimental theater.

### Visualizer + Image Mining
The `visualizer` skill uses semantic stereo vision: `PHOTO.yml` (structure) plus `PHOTO.md` (poetry). Add a third eye (mining) and you get depth and meaning. Then `image-mining` analyzes generated images across multiple layers (composition, lighting, emotion, texture) and writes YAML Jazz metadata.

The loop is:

prompt -> image -> mine -> rewrite -> regenerate -> compare

That is Play -> Learn -> Lift applied to image generation across different services. It is not one pretty image. It is a consistent world rendered from multiple perspectives without drift.

## The adventure compiler (final attraction)

After the practical stack comes the showcase: the adventure compiler. It turns this whole system into a web app. Anyone can "play my blog." Play my bio. Play my story. Play somebody's biography. Play somebody's story.

This is the memory palace made public. Rooms and objects are not just text, they are a runnable simulation. The LLM compiles YAML Jazz into JavaScript and JSON. The browser runs the deterministic engine. The LLM is optional but available for creative escalation.

Scott Adams (the adventure pioneer, the good one) has a wonderful idea: use the adventure compiler to create browser-based adventures that can run standalone or be tethered to LLMs. That is the bridge MOOLLM is designed to build. He wants to catalog his stories, emails, and history as a playable archive. I want a playable blog. We are both aiming at the same idea.

Richard Bartle matters here too. MOO culture shaped everything I build. As a teenager I played over the ARPA-UK bridge at Essex. MOOLLM is a direct descendant of that lineage.

## This is not Gas Town

Gas Town has energy. It also has deep structural flaws: it prioritizes vibe over evidence and collapses into performance. I am not here to dunk on anyone, but I am here to say that MOOLLM is the opposite. It is declarative, measured, and explicit. It is not hype. It is a method.

## Funding, not hype

I am not asking you to buy a coin. I do have a Patreon. I will spend it on tokens, not cryptocurrencies. Mortgage and cat food. I do not get drunk and post. I do love cannabis and fucking strong coffee.

## Close the loop

MOOLLM is a system for iterative generation, reflection, refinement, and proof. It is anti-slop and anti-gloss. It is a memory palace you can walk through and a lab you can measure. It is a practical DevOps toolkit and a weird performance engine. It is a playable blog. It is a playable biography.

If you want to see it, start here: `examples/adventure-4/` and `skills/adventure/`.
If you want to challenge it, bring evidence.
If you want to play, there will be a door soon.
