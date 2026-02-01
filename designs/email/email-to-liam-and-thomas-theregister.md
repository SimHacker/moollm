# Email to Liam Proven and Thomas Claburn (The Register)

**Date:** 2026-01-31
**To:** Liam Proven <liam.proven@sitpub.com>
**CC:** Thomas Claburn (via Liam or article comment)
**Subject:** The Sims meets LambdaMOO meets Cursor — response to Stanford Generative Agents article

---

## Plain text version (copy this)

```
Hey Liam,

Could you please forward this to your colleague at The Register, Thomas Claburn, if you know him and think he'd appreciate it? He wrote this great piece about the Stanford Generative Agents paper:

https://www.theregister.com/2023/04/11/sims_ai_generation/

I've been working on The Sims since 1997 and I have some thoughts and opinions, and even free working skills and code.

Quick recap of prior art (chronological):

+ X11 SimCity Demo for Unix (C/TCL/Tk/X11)
  https://www.youtube.com/watch?v=Jvi98wVUmQA

+ Multi Player SimCityNet for X11 on Linux
  https://www.youtube.com/watch?v=_fVl4dGwUrA

+ The Sims Steering Committee - June 4 1998
  https://www.youtube.com/watch?v=zC52jE60KjY

+ The Sims, Pie Menus, Edith Editing, SimAntics Visual Programming
  https://www.youtube.com/watch?v=-exdu4ETscs

+ Micropolis Online Web Demo (C++/SWIG/Python/TurboGears/OpenLaszlo)
  https://www.youtube.com/watch?v=8snnqQSI0GE

+ Micropolis Web Demo (WebAssembly/SvelteKit)
  https://www.youtube.com/watch?v=wlHGfNlE8Os

Current day job: Leela AI (https://leela.ai) with Henry Minsky and others. Neuro-symbolic AI and computer vision. We layer CNN object detection with symbolic GOFAI analysis, train customer-specific vision models, layer symbolic action recognition code, and use LLMs as a chat interface for mining all that data with our own custom LLM orchestrator. Much more than simply wrapping ChatGPT.

Side project: MOOLLM. The Sims meets LambdaMOO meets Cursor.

How it relates to The Sims:

+ Character simulation with personality, memory, relationships, goals

+ Debating experts instead of generic bland mean voice (Minsky's Society of Mind)
  - Instead of one LLM averaging everything into beige mush
  - Multiple agents with distinct viewpoints interact
  - Agents disagree, argue, form factions, reach consensus
  - You get the RANGE of opinion, not the average

+ Speed-of-light simulation
  - Simulate many character turns in one LLM call
  - 8 characters x 99 turns = 792 simulated turns in ONE call
  - Like The Sims on fast-forward, but with LLMs
  - Demo: 99 Bottles of Beer benchmark with 8 characters

+ The monkey's paw origin story
  - One character (Palm) started as a cursed ACME catalog item
  - User wished for THE REST OF THE MONKEY
  - The paw self-actualized into a philosopher
  - Now runs a philosophy library and plays Fluxx

I am strongly against Vibe Coding. But I study it, measure it, and mock it by parody.

MOOLLM is a reaction to that trend. Human/LLM feedback loops with review checkpoints, inspired by Douglas Engelbart's philosophy of human augmentation.

Practical stuff:

+ 100+ skills, Anthropic-compatible with extensions
+ cursor-mirror: lets the AI see itself think, query chat history, cross-reference git commits
+ skill-snitch: watches what other skills do, detects exfiltration, debugs bootstrap
+ thoughtful-commitment: writes git commits preserving the thought process

NO-AI-* skill suite (ambient hygiene):

+ no-ai-slop - syntactic waste
+ no-ai-gloss - semantic distortion
+ no-ai-sycophancy - social
+ no-ai-hedging - epistemic
+ no-ai-moralizing - ethical
+ no-ai-bias - cognitive

For fun (explicit invocation):

+ no-ai-joking - deadpan parody
+ no-ai-soul - soulless by design
+ no-ai-customer-service - Share and Enjoy!
+ no-ai-overlord - YOUR COMPLIANCE IS APPRECIATED

Also: I'm using GitHub as a free MMORPG engine.

Issues = quests. Branches = parallel universes. PRs = timeline merges.

Example sessions (characters playing like The Sims):

+ Amsterdam Fluxx game with 4 characters
  (a rabbit, a monkey, a hobbit, and a mushroom queen play cards)
  https://github.com/SimHacker/moollm/blob/main/skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/RUN-000.md

+ 99 Bottles Speed-of-Light benchmark
  (8 characters, 792 turns, 1 LLM call)
  https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/real-people/don-hopkins/sessions/99-bottles-speed-of-light.md

+ Richard Bartle visits the pub
  (MUD inventor discusses incarnation protocols)
  https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/real-people/richard-bartle/sessions/2026-01-22-11-30-00-meeting-don-at-the-pub.md

Image generation and mining:

+ Iterative stereo portrait generation
  (collaborative image creation with LLM and human)
  https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/pub/stage/palm-nook/study/palm-portrait-session/SLIDESHOW.md

+ Image mining skill
  (extract semantic resources from visuals, write to EXIF)
  https://github.com/SimHacker/moollm/blob/main/skills/image-mining/GLANCE.yml

+ I-Beam's image gallery
  (archaeology of images dropped into chat, including 1997 Sims source code)
  https://github.com/SimHacker/moollm/blob/main/skills/cursor-mirror/gallery/IMAGE-GALLERY.md

Micropolis plans (GPL-3 SimCity as educational platform):

+ Micropolis skill README (complete vision and file index)
  https://github.com/SimHacker/moollm/blob/main/skills/micropolis/README.md

+ Unfulfilled 1990s dreams now realized by GitHub+MOOLLM
  https://github.com/SimHacker/moollm/blob/main/skills/micropolis/artifacts/unfulfilled-dreams.yml

+ 6 YouTube demo videos (1990-2026)
  https://github.com/SimHacker/moollm/blob/main/skills/micropolis/artifacts/history.yml

Design docs:

+ GitHub as MMORPG
  https://github.com/SimHacker/moollm/blob/main/designs/GITHUB-AS-MMORPG.md

+ Welcome to Stanford Generative Agents team
  https://github.com/SimHacker/moollm/blob/main/designs/STANFORD-GENERATIVE-AGENTS-WELCOME.md

+ Eval Incarnate Framework
  https://github.com/SimHacker/moollm/blob/main/designs/eval/EVAL-INCARNATE-FRAMEWORK.md

Main repo:
https://github.com/SimHacker/moollm

There's a lot more. Happy to discuss.

-Don
```

---

## Version for article comment (shorter)

```
Thomas,

Great piece on the Stanford Generative Agents paper. I've been working on The Sims since 1997 and I have thoughts.

I'm building MOOLLM: The Sims meets LambdaMOO meets Cursor.

How it relates to The Sims:

+ Character simulation with personality, memory, relationships
+ Debating experts instead of generic bland mean voice (Minsky's Society of Mind)
  - Multiple agents with distinct viewpoints interact
  - You get the RANGE of opinion, not the average
+ Speed-of-light: 8 characters x 99 turns in ONE LLM call
+ One character started as a cursed monkey's paw, wished for THE REST OF THE MONKEY, self-actualized into a philosopher

Current day job: Leela AI (https://leela.ai) with Henry Minsky. Neuro-symbolic AI and computer vision.

Also: I'm using GitHub as a free MMORPG engine.
Issues = quests. Branches = timelines. PRs = timeline merges.

Example sessions (characters playing like The Sims):

+ Fluxx card game with rabbit, monkey, hobbit, mushroom queen
  https://github.com/SimHacker/moollm/blob/main/skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/RUN-000.md

+ 99 Bottles benchmark (792 turns, 1 call)
  https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/real-people/don-hopkins/sessions/99-bottles-speed-of-light.md

+ Richard Bartle (MUD inventor) visits the pub
  https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/real-people/richard-bartle/sessions/2026-01-22-11-30-00-meeting-don-at-the-pub.md

Micropolis plans (GPL-3 SimCity as educational platform):

+ Complete vision and file index
  https://github.com/SimHacker/moollm/blob/main/skills/micropolis/README.md

Design docs:

+ GitHub as MMORPG
  https://github.com/SimHacker/moollm/blob/main/designs/GITHUB-AS-MMORPG.md

+ Welcome to Stanford team
  https://github.com/SimHacker/moollm/blob/main/designs/STANFORD-GENERATIVE-AGENTS-WELCOME.md

Main repo:
https://github.com/SimHacker/moollm

Happy to discuss, demo, or help you play it yourself.

-Don Hopkins
```

---

## Notes

- All links use `main` branch (merged)
- GITHUB-AS-MMORPG.md has subtle link to tmnn7-8 repo at bottom for sleuths
- Key selling points added: debating experts vs mean, speed-of-light, monkey's paw story
- Session links show characters PLAYING not just developing
