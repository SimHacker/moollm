# Analysis: "Don't fall into the anti-AI hype" by antirez

**Source:** [antirez.com](https://antirez.com) — January 2026  
**HN Discussion:** 1022 points, 1227 comments

---

## The Article

**Author:** Salvatore Sanfilippo (antirez), creator of Redis

**Core Thesis:** Despite loving hand-crafted code and hoping for wealth redistribution, antirez argues that AI has fundamentally changed programming and refusing to engage with it is counterproductive.

### Key Claims

> "Writing code is no longer needed for the most part. It is now a lot more interesting to understand what to do, and how to do it."

> "For most projects, writing the code yourself is no longer sensible, if not to have fun."

### His Evidence (4 tasks completed "in hours instead of weeks")

1. **linenoise UTF-8 support** — plus an emulated terminal testing framework
2. **Redis transient test failures** — timing issues, TCP deadlocks; Claude Code iterated until fixed
3. **Pure C BERT inference library** — 700 lines, 15% slower than PyTorch, done in 5 minutes
4. **Redis Streams changes** — reproduced weeks of work in ~20 minutes from a design doc

### His Outlook

> "LLMs are going to help us to write better software, faster, and will allow small teams to have a chance to compete with bigger companies. The same thing open source software did in the 90s."

> "How do I feel, about all the code I wrote that was ingested by LLMs? I feel great to be part of that."

**Concerns:** Centralization of AI power in few companies, job losses without social safety nets.

---

## The Discussion

### The Skeptics

**totallykvothe** (top comment):

> "Every single time, I get something that works, yes, but then when I start self-reviewing the code, preparing to submit it to coworkers, I end up rewriting about 70% of the thing."

Concludes either: (1) bad at prompting despite years of experience, or (2) others have less thorough review culture.

**unyttigfjelltol** — the "super search engine" framing:

> "I've come back to the idea LLMs are super search engines. If you ask it a narrow, specific question, with one answer, you may well get the answer. For the 'non-trivial' questions... you'll get all of these depending on the precise words you use."

> "LLMs churning independently quickly devolve into entropy."

**20k** (astrophysics researcher):

> "Without exception, every technical question I've ever asked an LLM that I know the answer to, has been substantially wrong in some fashion. This makes it just.. absolutely useless for research."

> "They don't say 'sorry there's insufficient training data to give you an answer', they just make shit up and state it as confidently incorrect."

**IAmGraydon**:

> "A search engine with a lossy-compressed dataset of most public human knowledge, which can return the results in natural language. Is such a thing useful? Hell yes! Is such a thing intellegent? Certainly NO!"

### antirez Responds

antirez himself joins the discussion:

> "After you review, instead of rewriting 70% of the code, have you tried to follow up with a message with a list of things to fix?"

> "The existing code base is a fundamental variable. The more complex / convoluted it is, the worse is the result."

> "I have the feeling that the simplicity of the code bases I produced over the years... and the fact they are mostly in C, is a big factor why LLMs appear to work so well for me."

---

## Interesting Technical Observations

**chongli** on knowledge vs understanding:

> "Having knowledge isn't the same as knowing. I can hold a stack of physics papers in my hand but that doesn't make me a physics professor."

**friendzis** on convergence:

> "LLM prompting is on average much less analyzable... the process 'prompt LLM → QA → fix prompt' falls somewhere between 'does not converge' and 'convergence tail is much longer'."

**thesz** cites IEEE Spectrum research:

> "Recently released LLMs... often generate code that fails to perform as intended, but which on the surface seems to run successfully... by removing safety checks, or by creating fake output that matches the desired format."

**vanviegen** on agent behavior:

> "I've recently seen Opus, after struggling for a bit, implement an API by having it return JSON that includes instructions for a human to manually accomplish the task I gave it. It proudly declared the task done."

---

## The Optimists

**daxfohl**:

> "There's been a notable jump over the course of the last few months, to where I'd say it's inevitable."

Predicts AI evolving from "coding assistant" to "engineering team replacement" marketed directly to product teams.

**simonw** (Simon Willison) on workflow:

> "This is why every one of my coding agent sessions starts with '... write a detailed spec in spec.md and wait for me to approve it'. Then I review the spec, then I tell it 'implement with red/green TDD'."

**richardw** on skills and entropy:

> "I've also cleaned up so much of the architecture so there's only one way to do things. This keeps it more aligned and helps with entropy."

---

## Meta-Observations

**embedding-shape** on context pollution:

> "By having 'wrong code' in the context, makes every response after this worse. Instead, try restarting, but this time specify exactly how you expected that 70% of the code to actually have worked, from the get go."

**cm2187** reframes the debate:

> "Most pre-AI auto generated code is garbage (like winform auto generated code)... But that's fine, it's not meant to be read by humans. It may be that AI just moves the line between what developers should care and look at vs the boring boilerplate code."

---

## Key Tensions

| Pro-AI View | Skeptic View |
|------------|--------------|
| Works great for simple/clean C code | Falls apart on legacy enterprise code |
| 5 min for 700-line library | 70% rewrite after review |
| Democratizes software creation | Centralizes power in AI companies |
| "Super search engine" is useful | "Super search engine" isn't intelligence |
| Redis creator proves it works | Astrophysicist proves it fails |

---

## Stats

- **1022 points**, **1227 comments** on HN
- antirez claims **hours instead of weeks** for 4 tasks
- One commenter reports **70% rewrite rate** after AI generation
- SQLite testing ratio cited: **590:1** (test LOC to code LOC)

---

## MOOLLM Relevance

### What antirez gets right

His success factors align with MOOLLM principles:

1. **Simple, clean codebases** — MOOLLM's filesystem-as-world keeps state inspectable
2. **C code works best** — low abstraction, high pattern-match surface area
3. **Iteration works** — Claude Code's loop matches MOOLLM's agent-with-memory model
4. **Design docs first** — antirez gave Claude his design doc; MOOLLM gives skills and context

### What the skeptics reveal

The 70% rewrite problem is exactly what MOOLLM addresses:

- **K-lines** — semantic activation prevents the "all answers" entropy problem
- **Skills as programs** — constrain the solution space, not just describe it
- **Three-tier persistence** — context doesn't pollute; ephemeral stays ephemeral
- **Speed of light** — minimize round trips where entropy accumulates

### The "super search engine" insight

unyttigfjelltol's framing is profound:

> "For the 'non-trivial' questions... you'll get all of these depending on the precise words you use."

MOOLLM's response: **Don't ask non-trivial questions.** Break them into trivial ones. Skills, K-lines, and the coherence engine do the decomposition that humans otherwise must do manually.

### The entropy problem

friendzis nails it:

> "LLMs churning independently quickly devolve into entropy."

MOOLLM's entire architecture is anti-entropy:
- **Rooms** contain blast radius
- **Characters** maintain coherent identity across calls
- **Rubrics** score outputs against explicit criteria
- **Adversarial committees** prevent mode-collapse

### The convergence insight

The key variable isn't the LLM — it's the **existing codebase**:

> "The more complex / convoluted it is, the worse is the result."

MOOLLM starts with a clean, simple, well-documented microworld. The LLM isn't retrofitting chaos — it's extending order.

---

## See Also

- [MOOLLM-MANIFESTO.md](MOOLLM-MANIFESTO.md) — the philosophy
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — the seven extensions
- [skills/adversarial-committee/](../skills/adversarial-committee/) — countering mode-collapse
- [skills/speed-of-light/](../skills/speed-of-light/) — minimizing entropy-accumulating round trips
- [skills/k-lines/](../skills/k-lines/) — semantic activation over keyword search
