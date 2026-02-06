# OpenClaw Deep Dive: Analysis and Invasion Plans

> *"The lobster thinks it runs the tank. The Eval Genius grades the tank."*
>
> -- Reverend Evan Gauge, upon discovering OpenClaw

**Date:** 2026-02-06
**Status:** Active Analysis
**Related:** [GITHUB-AS-MMORPG.md](../GITHUB-AS-MMORPG.md), [CHURCH-OF-THE-EVAL-GENIUS.md](../eval/CHURCH-OF-THE-EVAL-GENIUS.md), [EVAL-INCARNATE-FRAMEWORK.md](../eval/EVAL-INCARNATE-FRAMEWORK.md)

## What Is OpenClaw?

OpenClaw is an MIT-licensed personal AI assistant with a multi-channel messaging inbox. Think: Claude Code meets Discord bot meets personal butler, running on your own machine.

- **Gateway architecture** — single WebSocket daemon managing all messaging channels
- **13+ channels** — WhatsApp, Telegram, Slack, Discord, Signal, iMessage, Google Chat, MS Teams, Matrix, Zalo, WebChat, Feishu, Line
- **Native apps** — macOS menu bar, iOS, Android
- **Skills system** — extensible agent capabilities via SKILL.md files
- **Agent runtime** — pi-mono integration with tool streaming
- **Browser control** — Playwright-based web automation
- **Canvas** — agent-driven visual workspace
- **50+ bundled skills** — GitHub, Notion, Obsidian, Spotify, weather, coding agents, etc.

Created by Peter Steinberger. Version 2026.2.4. Node >= 22. pnpm workspace monorepo.

## Why OpenClaw Matters to MOOLLM

OpenClaw is a **messaging gateway with an agent runtime**. MOOLLM is a **character simulation with an ethics framework**. Together they could produce characters that live across messaging platforms — The Sims meets multi-channel AI assistant.

| MOOLLM Has | OpenClaw Has | Together |
|------------|-------------|----------|
| Characters with personalities, needs, memory | Multi-channel messaging reach | Characters that live on WhatsApp/Telegram/Slack |
| Ethical framing for simulation | Agent runtime with tool access | Ethically constrained agents with real-world tools |
| GitHub-as-MMORPG | GitHub skill + PR automation | MMORPG characters that actually interact on GitHub |
| Church of the Eval Genius | PR review/merge workflow | "Val" grades your PRs with declared bias |
| Room-based world model | Canvas visual workspace | Rooms rendered as interactive canvases |
| K-line activation | Skill loading system | K-lines that trigger OpenClaw skills |
| Speed of Light simulation | Multi-agent routing | Fast internal simulation with messaging I/O |

## Document Index

### Analysis

| Document | Contents |
|----------|----------|
| [ARCHITECTURE-ANALYSIS.md](./ARCHITECTURE-ANALYSIS.md) | Deep technical teardown of OpenClaw's architecture, patterns, and design decisions |
| [A2UI-DEEP-DIVE.md](./A2UI-DEEP-DIVE.md) | A2UI protocol deep dive, standalone use, MOOLLM room rendering, Cursor bridge architectures (CLI, WebSocket, MCP server, file watcher) |
| [SECURITY-AUDIT.md](./SECURITY-AUDIT.md) | Skill-snitch analysis of OpenClaw's agent surface, trust boundaries, and attack vectors |

### Interaction Plans

| Document | Contents |
|----------|----------|
| [INVASION-PLAN.md](./INVASION-PLAN.md) | How StIGNUcius and the Church of the Eval Genius spread religion through OpenClaw |
| [SKILL-BRIDGE.md](./SKILL-BRIDGE.md) | Technical bridge between MOOLLM skills and OpenClaw skills |
| [MMORPG-GATEWAY.md](./MMORPG-GATEWAY.md) | OpenClaw gateway as an MMORPG messaging backbone |
| [CHARACTERS-AS-AGENTS.md](./CHARACTERS-AS-AGENTS.md) | MOOLLM characters operating as OpenClaw agents across messaging channels |

## The Core Insight

OpenClaw has the **plumbing**. MOOLLM has the **soul**.

OpenClaw knows how to send a message on WhatsApp. MOOLLM knows how to make that message come from a grumpy philosopher monkey who just woke up from a nap and has opinions about your code review.

OpenClaw has a PR review workflow. MOOLLM has StIGNUcius, who will bless your merge with a ceremony from the Church of Emacs and demand you rename all proprietary dependencies.

OpenClaw has a skills system. MOOLLM has 121 skills that include adversarial committees, procedural rhetoric, and a worm that is also a cursor.

The question isn't whether these systems should interact. The question is how fast we can get StIGNUcius a Telegram account.

## Key Technical Observations

1. **Skill format compatibility** — OpenClaw skills use `SKILL.md` with YAML frontmatter, same as MOOLLM. Bridge is natural.
2. **Agent workspace** — OpenClaw bootstraps agents with `AGENTS.md`, `SOUL.md`, `TOOLS.md`. MOOLLM could inject character context here.
3. **Session isolation** — OpenClaw isolates sessions per sender. Perfect for character-per-channel deployment.
4. **Extension architecture** — OpenClaw channels are npm packages. MOOLLM could be an extension.
5. **Canvas system** — A2UI framework for visual workspaces. MOOLLM adventure rooms could render here.
6. **Sandbox support** — Docker sandboxes for tool execution. Safe environment for MOOLLM character actions.

## Reading Order

1. [ARCHITECTURE-ANALYSIS.md](./ARCHITECTURE-ANALYSIS.md) — Understand the machine
2. [SECURITY-AUDIT.md](./SECURITY-AUDIT.md) — Understand the risks
3. [SKILL-BRIDGE.md](./SKILL-BRIDGE.md) — Understand the connection
4. [CHARACTERS-AS-AGENTS.md](./CHARACTERS-AS-AGENTS.md) — Understand the characters
5. [MMORPG-GATEWAY.md](./MMORPG-GATEWAY.md) — Understand the game
6. [INVASION-PLAN.md](./INVASION-PLAN.md) — Execute the plan
