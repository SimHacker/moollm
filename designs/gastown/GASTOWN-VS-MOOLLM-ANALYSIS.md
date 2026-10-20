# Gas Town and MOOLLM

> *"Gas Town churns through implementation plans so quickly that you have to do a LOT of
> design and planning to keep the engine fed."*
> — Steve Yegge, [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)

Gas Town and MOOLLM both put LLM agents to work on shared state kept in git. That's where the
resemblance ends. At almost every design fork, Gas Town took the opposite branch from MOOLLM,
and the reasons are philosophical before they are economic. The token bill follows from the
philosophy, not the other way round: with free tokens I still wouldn't invent opaque names,
refuse to read the code, or route messages between twenty processes when one context can hold
all the characters.

Contents:

1. [What Gas Town is](#1-what-gas-town-is)
2. [Six philosophical differences](#2-six-philosophical-differences)
3. [What Gas Town gets right](#3-what-gas-town-gets-right)
4. [What the code shows](#4-what-the-code-shows)
5. [Mapping: Gas Town to MOOLLM](#5-mapping-gas-town-to-moollm)
6. [Where MOOLLM is weaker](#6-where-moollm-is-weaker)
7. [Nine months later](#7-nine-months-later)
8. [The token](#8-the-token)
9. [Sources](#9-sources)

## 1. What Gas Town is

An orchestrator for coding agents. It runs twenty to thirty Claude Code (and later Codex,
Gemini, Copilot) sessions in tmux, coordinated through an issue tracker called Beads.

- **Beads** — issues stored in a database synced to git, behind a `bd` CLI.
- **Molecules and formulas** — workflows: chains of beads, defined in TOML.
- **Roles** — Mayor (your concierge), Polecats (ephemeral workers that produce merge requests
  and exit), Witness (supervises polecats), Refinery (merge queue), Deacon (daemon supervisor),
  Dogs (maintenance; Boot the dog checks on the Deacon every five minutes), Crew (named
  persistent agents).
- **GUPP**, the "Gastown Universal Propulsion Principle": if there is work on your hook, run it.

Yegge's own framing: it's expensive, it's chaotic, don't use it unless you're "Stage 7" on his
eight-stage ladder of AI-assisted coding, and it is 100% vibe coded.

## 2. Six philosophical differences

### 2.1 Names are pointers into latent space

MOOLLM's constitutional directive is to lean into the training data: reuse terms the model
already knows, and when you must mint a new one, make it sound like what it means. A name is a
K-line. Say "issue" and the model already knows about assignees, labels, milestones, closing
comments and `gh issue`. Naming is API design.

Gas Town's vocabulary: bead, polecat, wisp, molecule, protomolecule, formula, convoy, rig, hook,
deacon, seance, GUPP, MEOW. Its own README says *"the terms 'bead' and 'issue' are used
interchangeably."* Maggie Appleton, trying to explain the system: *"Do not ask what GUPP is; I
cannot concisely explain without getting deep into it."* Every one of those words has to be
taught to the model in every session, and the model still drags in its priors about ferrets and
chemistry. The full argument is in [HUMANSPLAINING.md](../object-system/HUMANSPLAINING.md).

### 2.2 You read what you build

MOOLLM comes from Papert's constructionism: you learn by building things you can look at, take
apart, and change. The whole point of directories-as-rooms and YAML-with-comments is that a
person can open the file, see what the character was told, edit it, and run the scene again.
[cursor-mirror](../../skills/cursor-mirror/) exists so the agent can read its own sessions too.

Yegge: *"I've never seen the code, and I never care to... Course, I've never looked at Beads
either, and it's 225k lines of Go code."* Not looking isn't a methodology. It's a decision not
to know what you're shipping. The same author wrote "Code's Worst Enemy" in 2007, arguing that
size is the worst thing that can happen to a code base. By July 2026 Gas Town alone is about
249,000 lines of non-test Go and 226,000 lines of tests, on top of Beads. Nobody reads that,
including the agents, which see it a few files at a time.

### 2.3 Agents belong in one mind

"Agent" in AI is a Minsky word. In *Society of Mind* the agents are colocated in one mind,
cheap, numerous and talking constantly. MOOLLM takes that literally: one context simulates many
characters for many turns ([speed-of-light](../../skills/speed-of-light/)). The Amsterdam Fluxx
run held four players with distinct voices through 116+ turns of a game whose rules keep
changing mid-play, with no messages passed between processes.

Gas Town puts one agent in one process and connects them with mail, nudges, heartbeats and
tmux text injection. That inverts the book the word comes from. Every message is serialized to
text, sent, parsed, and re-contextualized by a model that has lost everything the sender knew.
[SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](../SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) has the long
version.

MOOLLM does use separate sessions when the work needs them: [cauldron](../../skills/cauldron/)
hands one playbook to one executor chat when the playbooks touch separate files and need their
own tool runs. Separate processes are a cost you pay when the work requires it. They aren't the
architecture.

### 2.4 Store what happened, compute what is possible

Beads stores `status: open | in_progress | closed`. Stored status drifts from reality, so Gas
Town runs supervisors on patrol cycles to catch the drift: the Witness watches polecats, the
Deacon watches the Witness, Boot the dog watches the Deacon every five minutes. Gas Town's own
`bd` wrapper passes `--allow-stale` "to prevent failures when db is out of sync with JSONL."

MOOLLM stores events and computes state ([designs/TECH-TREE.md](../TECH-TREE.md)). Whether a
task is ready or blocked comes from running its guards. Whether it's stale is a
[buff](../../skills/buff/) with a clock, and because buffs carry their own advertisements, a
stuck task bids for attention by itself. Nothing patrols, because there's no stored flag that
can drift. [skills/task/](../../skills/task/) is the implementation.

### 2.5 Design is the work, not the fuel

Yegge and Appleton both observe that when agents write code fast, design becomes the bottleneck.
I agree with the observation. The responses differ. Gas Town treats design as fuel: the human
keeps the engine fed with plans. MOOLLM treats design as the job, and the agents' speed as
something that frees the human to spend more time on it.

[cauldron](../../skills/cauldron/) is the concrete form: spend the expensive model and the
human's attention on melting a plan down until its shape is right, then ladle it into playbooks
cheap executors can run without the designer in the room. In MOOLLM's games the human moves
between playing a character, building the room, and inspecting what the simulation was told. The
human is player and builder, not the product manager of a factory.

### 2.6 Claims come with receipts

The Stage 1–8 ladder makes failure unfalsifiable: *"If you're not at least Stage 7, or maybe
Stage 6 and very brave, then you will not be able to use Gas Town."* If it doesn't work for you,
you're not ready. HN commenters named the related move "Schrödinger's Modest Proposal": a post
that is a joke when criticized and the future of engineering when praised.

MOOLLM's claims point at files: run logs, rubrics, guards that pass or fail, commits that cite
the session that produced them. Some of those receipts are weaker than they look; see
[section 6](#6-where-moollm-is-weaker).

### And then the tokens

Follow 2.1 through 2.5 and you spend fewer tokens as a side effect: no vocabulary lessons in
every prompt, no re-contextualizing every message, no patrol agents, no reloading the same
context into thirty sessions. Yegge calls Gas Town "expensive as hell" and says you won't like
it "if you ever have to think, even for a moment, about where money comes from." That's the bill
for its philosophy.

## 3. What Gas Town gets right

Appleton's essay is the fairest reading of Gas Town, and her list of patterns that will outlive
it holds up:

- **Agent work state belongs in git and must survive session death.** Beads' core idea is right.
  An agent that loses its context should be able to read its work back and continue. MOOLLM's
  task skill credits it.
- **Persistent identity, disposable sessions.** Roles and assignments outlive the process.
- **A serialized merge queue.** The Refinery rebases, validates, and merges one change at a time
  so parallel workers don't trample main. That's a real problem with a real answer, and MOOLLM
  has no equivalent (see section 6).
- **Per-step model tiers.** Gas Town's molecule steps carry a tier hint (haiku, sonnet, opus).
  Cauldron arrived at the same idea as model routing per phase.
- **Parallel legs with a synthesis step.** The "convoy" formula type. The workflow skill has it
  as `fan_out`.
- **Retries converge if done is checkable.** Yegge calls it nondeterministic idempotence. It's
  true exactly when "done" is something you can run, which is why every MOOLLM task has a
  `done_when`.

And credit for shipping something strange in public and letting people poke at it.

## 4. What the code shows

Read at `d4126bb8` (24 Jan 2026) and `649b832b` (23 Jul 2026).

| | January | July |
|---|---|---|
| Non-test Go lines | 110,539 | 248,971 |
| Test Go lines | 52,971 | 225,753 |
| `exec.Command("bd", ...)` call sites | 231 | 168 |
| `exec.Command("tmux", ...)` call sites | 40 | 45 |

Specific things:

- **Gas Town reads its own state by forking a CLI.** The `Beads.run` wrapper execs `bd` with
  `--no-daemon --allow-stale` for every read and write, and parses the JSON it prints. The
  storage underneath was SQLite synced to JSONL in January and Dolt by July; the fork-and-parse
  pattern stayed.
- **Eleven custom bead types:** `agent, role, rig, convoy, slot, queue, event, message, molecule,
  gate, merge-request`. Most of those aren't work. When agents, locks, mail and events are all
  issue rows, "bead" stops meaning anything. It's a closed type list from the author of
  ["The Universal Design Pattern"](http://steve-yegge.blogspot.com/2008/10/universal-design-pattern.html),
  which argued that property lists with prototype parents are the way to build open-ended,
  long-lived systems, and which used his own game Wyvern's "archetypes" as the example. Gas
  City had to be rewritten as composable packs to get back the openness that essay was about.
- **Structured data parsed out of prose.** `beads_escalation.go` (441 lines in January) stores
  escalation fields as `key: value` lines inside an issue description and parses them back with
  `strings.Index(line, ":")`.
- **Dead concepts left in the tree.** `internal/wisp/types.go` opens with "This package was
  originally for 'hook files' but those are now deprecated." The comment is still there in July.

None of these is unusual for a fast-moving project. They're what happens when nobody reads the
code, and they compound: the next agent reads the dead package as documentation.

## 5. Mapping: Gas Town to MOOLLM

| Gas Town | MOOLLM | Notes |
|---|---|---|
| bead | [task](../../skills/task/) | Same thing; Gas Town's README says so |
| hook, pinned bead | task `owner:` + advertisement score | The owner's claimed task scores highest for that owner |
| GUPP | [advertisement](../../skills/advertisement/) scoring | How a Sim decides to eat |
| molecule, formula | [workflow](../../skills/workflow/) | One schema: requires, fan_out, gate, verify |
| convoy | workflow instance, or a GitHub milestone | |
| wisp | [scratchpad](../../skills/scratchpad/) | Gas Town deprecated wisps itself |
| gate | workflow `gate: approval` | [plan-then-execute](../../skills/plan-then-execute/) |
| mail, nudge | [postal](../../skills/postal/), or nothing in one context | |
| polecat | executor session, or a simulated worker | |
| Witness, Deacon, Dogs | task-hosted buffs: `stale`, `waiting-on`, `flaky-guard` | Stuck work raises its hand |
| Refinery | GitHub merge queue + CI, for now | A gap; see below |
| Mayor | the human, in the room | |
| slot (lock) | git; a lock file if you really need one | |

## 6. Where MOOLLM is weaker

- **No merge queue.** When several executors land PRs on one repo at once, MOOLLM leans on
  GitHub's merge queue and CI. The Refinery is the one Gas Town component I'd want a MOOLLM
  answer for.
- **Throughput is undemonstrated.** The cauldron brew documented in the skill ladled into 13
  playbooks. Nobody has run MOOLLM as a fifty-PR overnight factory, and I'm not going to claim
  it would do better at that until someone does.
- **Self-scored receipts.** The Amsterdam Fluxx run's 94/100 was scored by the same model that
  played the game. The run files are real evidence that one context can hold four characters
  and a mutating ruleset for 116+ turns. The score is a self-assessment. Future runs get an
  [evaluator](../../skills/evaluator/) that didn't play.
- **A game is not a code base.** Fluxx shows coherence across many simulated characters. It
  doesn't show that the same approach ships production code. The better evidence is Leela AI's
  production work, which is private.
- **One context has a ceiling.** Speed of light runs out at the context window and the model's
  attention. Past that you split the work, and then you're in Gas Town's territory with better
  guards.

If a claim here is wrong, open an issue with the counterexample and I'll fix it.

## 7. Nine months later

Details and sources in [BEFORE-AND-AFTER-2026-10.md](BEFORE-AND-AFTER-2026-10.md).

- **Gas Town is done.** `main` stopped on 23 July; the last release was v1.2.1 on 6 June. The
  successor, [Gas City](https://github.com/gastownhall/gascity), is Gas Town rewritten as an
  SDK of composable "packs" so you're not stuck with the fixed team shape. It was written by
  Julian Knutsen and Chris Sells, not Yegge. Gas Town's README still doesn't mention it.
- **Yegge's own verdict:** "I only ever wound up using it to build itself." He says it "burned
  down" when Opus 4.7 kept wanting to fiddle with Gas Town instead of doing real work.
- **Wheelhouse**, his private successor for building Wyvern, repeats §2.1 and §2.2 at larger
  scale. It's about 600k lines, mostly Bash, and he hasn't read it. His agents minted jargon
  (fences, ratchets, tripwires) that he couldn't decode until he had them audit themselves.
  Wyvern itself is about 1.2M lines.
- **Overfencing.** Rules that only tighten, minted by every postmortem and curated by nobody,
  grew to 650 refusal sites, until "no work was legal". The fix was to cut them to 14 and require
  his signature on new ones. MOOLLM calls this scar tissue. Its structural answer is that a
  restriction is a buff with an expiration date.
- **The fuel bill arrived.** With 21 Claude Max accounts, the factory sits mostly idle because he
  can't afford the tokens. His list of fuel-efficiency levers (on-demand priming, smaller tasks,
  earlier handoffs, cheaper models) reads like MOOLLM's semantic image pyramid and cauldron's
  model routing.
- **Where he converged.** "Seats" are durable roles that any model boots into, with authority,
  history and scope bound in advance. His line "caution you can look up is caution you can
  afford" is the prepaid-context argument. Some of the issues fit §2.4 directly: Gas Town's
  reaper auto-closed live bug reports for being old
  ([#4911](https://github.com/gastownhall/gastown/issues/4911)), and an unrendered template
  silently dropped `--dry-run` from a purge command
  ([#4909](https://github.com/gastownhall/gastown/issues/4909)).

## 8. The token

In January 2026 a trader launched a $GAS memecoin on the Bags platform with trading fees routed
to Yegge's Twitter account. He didn't create it. He claimed the fees (Goedecke reported $238,000
on 17 Jan; Solana Floor later reported over $300,000), wrote a post comparing Bags to a stock
market for creators, and promoted it. $GAS peaked above a $60 million market cap. After he said
he'd spend less time on Crypto Twitter, and then published a disclosure that the token conveyed
no ownership of anything, it fell about 97% in three days. The people left holding it were his
readers.

It has nothing to do with Gas Town's code, and it isn't why the design is wrong. It's sad, and
it's in [YEGGE-ARC-ANALYSIS.md](YEGGE-ARC-ANALYSIS.md) with sources.

## 9. Sources

- Steve Yegge, [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) (1 Jan 2026); [HN](https://news.ycombinator.com/item?id=46458936)
- Maggie Appleton, [Gas Town's Agent Patterns, Design Bottlenecks, and Vibecoding at Scale](https://maggieappleton.com/gastown); [HN](https://news.ycombinator.com/item?id=46734302)
- Steve Yegge, "Code's Worst Enemy" (Dec 2007), "Execution in the Kingdom of Nouns" (Mar 2006), on [steve-yegge.blogspot.com](https://steve-yegge.blogspot.com/)
- Sean Goedecke, [Crypto grifters are recruiting open-source AI developers](https://www.seangoedecke.com/gas-and-ralph/)
- Solana Floor, [Solana AI Meta Collapses](https://solanafloor.com/news/solana-ai-meta-collapses)
- Source: [steveyegge/gastown](https://github.com/steveyegge/gastown) at `d4126bb8` and `649b832b`
- MOOLLM: [constitution-core.md](../../kernel/constitution-core.md), [TECH-TREE.md](../TECH-TREE.md), [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](../SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md), [HUMANSPLAINING.md](../object-system/HUMANSPLAINING.md), [Amsterdam Fluxx run](../../skills/experiment/experiments/fluxx-chaos/runs/amsterdam-flux/README.md)
