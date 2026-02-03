# Brief Intro for Pavel Curtis

**To:** Pavel Curtis  
**From:** Don Hopkins  
**Subject:** LambdaMOO's ideas live on — quick intro

---

Hi Pavel,

Great to hear back from you so swiftly! 

I've built MOOLLM (MOO + LLM), an open-source framework where:
- The **filesystem** is the object database (directories = rooms, YAML and Markup files = objects and sessions)
- **LLMs** are the parser, runtime, players, eval() and coherence engine all at once
- **Git repos** are the fabric of the multiverse — history, backing store, and distributed reality beyond the local filesystem. GitHub is the community backbone, the server — GitHub-as-MMORPG. (We're building MooCo as our own coordinator, but currently run on Cursor, Claude Code, and other LLM-native IDEs.)

It's what would happen if LambdaMOO and The Sims had a baby, raised by Claude.

**Why I wanted to reach you:**

I'm especially interested in LambdaMOO's object model, programming language, and the lessons learned — strengths, weaknesses, security, ownership, privacy, modularity. I've been building on ideas you pioneered (`$corified` names, parent chains, in-world programming) but adapted for distributed repos and LLM-native computation. Some things translated directly. Others needed rethinking.

I'm also delighting in Self abuse — David Ungar's prototype system maps beautifully onto directories-as-objects. Slots become files. Parent chains become prototype links. It's Self meets MOO meets Git.

I'd love your perspective on a few architectural questions, but no rush — happy to just share what we're doing and hear your thoughts whenever.

**Entry points if you're curious:**

| What | Link |
|------|------|
| The repo | https://github.com/SimHacker/moollm |
| What we learned from MOO | [designs/MOO-HERITAGE.md](https://github.com/SimHacker/moollm/blob/main/designs/MOO-HERITAGE.md) |
| A working text adventure | [examples/adventure-4/](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4) |
| The addressing/naming system | [kernel/naming/](https://github.com/SimHacker/moollm/tree/main/kernel/naming) |
| Full design overview | [LEELA-MOOLLM-DEMO-TRANSCRIPT.md](https://github.com/SimHacker/moollm/blob/main/designs/LEELA-MOOLLM-DEMO-TRANSCRIPT.md) |

**Quick questions I'm pondering (no pressure to answer now):**

1. **Cross-MOO networking** — You had SunNET, GNA-NET. We're building MooCo for multi-repo coordination. What worked?

2. **Location-independent objects** — In MOO, objects lived at fixed `#` addresses. We need skills addressable by symbolic name, resolvable through search paths. Any prior art I'm missing?

3. **Core vs. user-space** — LambdaCore, JHCore, enCore. How did you think about what belongs in the kernel?

I wrote a longer "deep dive" letter with more questions, but figured I'd start simple. Happy to share that or just chat.

Thanks for building something that's still inspiring 35 years later.

Best,

**Don Hopkins**  
Amsterdam, February 2026

---

*P.S. — The genealogy I keep in my head: Crowther & Woods → Trubshaw & Bartle → Stephen White → Pavel Curtis → Will Wright → MOOLLM. You're in the direct line.*
