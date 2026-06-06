# MOOCO + Moo VM — Browser and Server, Implemented and Composed

**Status:** Public design (May 2026)  
**Implementation:** The **moo** skill ships today in `skills/moo/`. MOOCO orchestrator wiring is partial.  
**Read first:** [MOOCO-MANIFESTO.md](MOOCO-MANIFESTO.md), [MOOCO-MOO-CUSTOM-ORCHESTRATOR.md](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md)

---

## The alignment

MOOCO's browser/server metaphor was always about **stable URLs**, **partial fetch**, and **tabs** — not about inventing a new HTTP stack.

The **moo** skill is the working implementation of that client side:

| MOOCO concept | moo skill (today) |
|---------------|-------------------|
| `GET moollm://…` | `moo read <moorl>` |
| Partial fetch / HEAD | `moo sniff`, `moo card`, `moo glance`, fragment `#key`, `-L` lines |
| URL resolution | `moo resolve <moorl>` |
| Open many tabs | `moo focus` (attention-tree overlay), `moo batch-glance` |
| Browse tree | `moo ls`, `moo tree` |
| Session cache | `.moollm/skills/moo/cache/` (per repo/branch/path) |

**Moorl** — MOO URL. Schemes: `moo://` (repo from env) and `moollm://` (full address). See [skills/moo/MOONUAL.md](../skills/moo/MOONUAL.md).

MOOCO orchestrator = **server** that can invoke moo (via `skill_manager` or sister scripts), persist traces, enforce policy.  
Moo CLI = **browser engine** usable directly in a shell — including Cursor running `python skills/moo/moo.py …` turn by turn.

They compose; neither replaces the other.

---

## What ships: the moo skill

**Location:** `skills/moo/` — entry `moo.py`, logic in `lib/` and `lib/commands/`, tests in `tests/`.

**Model** (from [moocroworld](../skills/moocroworld/)): GitHub **branches as objects** (`Issue_42`, `Character_Don`). Files on the branch are object state. `gh api` is the transport — no local clone required for read/browse.

**Config:** `REPOS.yml` lives in **moocroworld** (mooniverse aliases). Override with `MOO_REPOS_FILE`. Cache under `MOOLLM_WORKSPACE/.moollm/skills/moo/cache/`.

**Commands:** `repos`, `resolve`, `ls`, `tree`, `read`, `sniff`, `glance`, `card`, `scan`, `write`, `rm`, `batch-glance`, `focus`, `summarize`.

**Quick start:**

```bash
cd /path/to/moollm
python skills/moo/moo.py repos
python skills/moo/moo.py resolve 'moollm://SimHacker/moollm/main/skills/moo/CARD.yml'
python skills/moo/moo.py read 'moollm://SimHacker/moollm/main/skills/moo/SKILL.md'
python skills/moo/moo.py sniff 'moollm://SimHacker/moollm/main/skills/moo/lib/cli.py' --depth structure
```

Dense LLM reference: [skills/moo/MOOGLANCE.md](../skills/moo/MOOGLANCE.md). Full manual: [MOONUAL.md](../skills/moo/MOONUAL.md).

---

## MOOPMAP: semantic mipmap (related, local)

[MOOPMAP.md](MOOPMAP.md) and `skills/moollm/scripts/moopmap.py` measure the **GLANCE → CARD → SKILL → README** compression pyramid on a **local checkout**. That is the resolution ladder moo climbs at fetch time:

```text
moo glance / card     → resolution 0–1 (MOOPMAP levels)
moo read full file    → resolution 2–3
moo sniff --skeleton  → structural HEAD without values
moo focus overlay     → batch load by depth (attention tree)
```

Moo fetches remotely; moopmap analyzes locally. Same pyramid, different substrate.

---

## How MOOCO should use moo

```mermaid
flowchart LR
    LLM["LLM (tabs)"]
    MOOCO["MOOCO orchestrator"]
    Moo["moo skill / CLI"]
    GH["GitHub via gh api"]
    Local["Local git repos\n(workspace.json)"]

    LLM -->|"GET moollm://…"| MOOCO
    MOOCO -->|"skill_manager: moo read/sniff/resolve"| Moo
    Moo --> GH
    MOOCO -->|"git_* tools"| Local
```

### Orchestrator mapping (target wiring)

| Orchestrator request | moo invocation | Notes |
|---------------------|----------------|-------|
| `GET moollm://repo/branch/path` | `moo read <moorl>` | Full representation |
| `HEAD …/CARD.yml` | `moo card` or `read` + path | Card-only, no full SKILL.md |
| `GET …#payload/key` | `moo read` with fragment or `-k` | Fragment drill |
| `GET …?sniff` (future) | `moo sniff --depth glance` | Structural partial |
| Resolve before fetch | `moo resolve` | Audit trail in session |
| Multi-resource session | `moo focus <overlay.yml>` | Attention tree = tab batch |

Every invocation should carry **`--why`** (moo accepts it; orchestrator mandates it on tools).

### Two valid runtimes today

1. **Shell/browser loop** — Agent or human runs moo CLI repeatedly. Cache warms across invocations. No MOOCO required.
2. **MOOCO session** — Orchestrator streams SSE, calls moo sisters through `skill_manager`, logs what was fetched. Same moo binary, audited wrapper.

---

## What MOOCO still adds (not in moo alone)

| Concern | Owner |
|---------|--------|
| Moorl fetch, sniff, focus | **moo** (implemented) |
| K-line heat, skill_manager policy | **MOOCO** |
| Session traces, `--why` audit | **MOOCO** |
| Local multi-repo path map | **mooco** `workspace.json` + `git_*` tools (stub) |
| Shadow overlays (GRANT/AFFLICT) | **MOOFS** ([MOOFS-DESIGN.md](MOOFS-DESIGN.md)) |
| Local disk reification (symlink mounts) | **MOOT** (future — [private MOOKIE sketch](../../mooco/designs/MOOKIE.md)) |

Moo solves **remote virtual filesystem** over GitHub. MOOT/MOOKIE (when built) solves **local tree composition**. MOOFS solves **which layer wins**. MOOCO holds the session together.

---

## Namespace family (updated)

| Name | Role | Status |
|------|------|--------|
| **MOOLLM** | Content in git: skills, rooms, designs | Shipped |
| **moo** | Moo VM CLI — moorls, gh-backed browse/fetch | **Shipped** (`skills/moo/`) |
| **moocroworld** | Mooniverse model, REPOS.yml, attention trees | Shipped |
| **MOOCO** | Orchestrator protocol endpoint | Prototype |
| **MOOFS** | Overlay resolution semantics | Design |
| **MOOT** | Local git tree reifier | Future |
| **MOOMC** | Meta compiler: distill MiniMOO runtime repos | Future |
| **moopmap** | Local GLANCE pyramid analysis | Shipped (script) |

The old docs described **MOOKIE/MOOT** as if they were the moollm:// implementation. That was wrong. **moo** is the implementation. MOOT is a complementary local layer still on the drawing board.

---

## Private mooco repo alignment

The orchestrator prototype (`apps/mooco/`) today has:

- `~/.mooco/workspace.json` — name → absolute path for **local** repos
- `@moollm/tools-git` — scoped git operations

It should **delegate remote `moollm://` to the moo skill**, not reimplement URL parsing. See [mooco/designs/MOOCO-REPOS.md](../../mooco/designs/MOOCO-REPOS.md) and [MOOKIE.md](../../mooco/designs/MOOKIE.md) for the trimmed private sketches.

---

## Document map

| Document | What |
|----------|------|
| [MOOCO-MOO-VM.md](MOOCO-MOO-VM.md) | **This file** — moo + MOOCO composition |
| [MOOCO-MANIFESTO.md](MOOCO-MANIFESTO.md) | Runtime vision |
| [MOOCO-MOO-CUSTOM-ORCHESTRATOR.md](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md) | Browser/server protocol |
| [MOOFS-DESIGN.md](MOOFS-DESIGN.md) | Local overlay layers |
| [MOOPMAP.md](MOOPMAP.md) | Semantic mipmap / GLANCE pyramid |
| [skills/moo/MOONUAL.md](../skills/moo/MOONUAL.md) | Moo VM reference manual |
