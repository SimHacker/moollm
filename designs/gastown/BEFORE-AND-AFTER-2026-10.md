# Gas Town, January to October 2026

A checkup, nine months after "Welcome to Gas Town". Gas Town's `main` hasn't moved since
23 July. The work went to a successor Yegge didn't write, and Yegge went to a private orchestrator
for his game that he hasn't read either.

Measured from the local clone at `d4126bb8` (24 Jan) and `649b832b` (23 Jul, still `main` on
20 Oct), plus GitHub and Yegge's essays. I didn't measure Gas City's code.

## Shape, mass, velocity

| | January (`d4126bb8`) | July (`649b832b`) |
|---|---|---|
| Commits | 2,996 | 7,770 |
| Commit authors | 83 | 375 |
| Go, non-test lines | 110,539 | 248,971 |
| Go, test lines | 52,971 | 225,753 |
| `internal/` packages | 51 | 70 |
| Files in `internal/cmd/` | 197 | 457 |
| Formula files (`*.formula.toml`) | 64 | 48 |
| Markdown files / files in `docs/` | 43 / 25 | 117 / 74 |
| README lines | 494 | 842 |
| `exec.Command("bd"` call sites | 231 | 168 |

Between the two commits: 1,529 files changed, 419,978 lines added, 52,661 removed, 976 files
added, 73 deleted. It mostly grew. Test code grew fastest, quadrupling, which is the healthiest number in
the table.

Commits per month:

| Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug–Oct |
|---|---|---|---|---|---|---|---|---|
| 1,985 | 1,199 | 2,245 | 1,426 | 234 | 381 | 159 | 141 | 0 |

The cliff is at v1.0.0 on 3 April. Releases ran v0.5.0 (22 Jan) through v0.13.0 (29 Mar), then
v1.0.0, v1.1.0, v1.2.0, and v1.2.1 on 6 June, which is the last release and Yegge's last commit
(a version bump).

GitHub on 20 Oct: 18,445 stars, 1,687 forks, 377 open issues, 131 open PRs, 138 branches. The
repo moved from `steveyegge/gastown` to `gastownhall/gastown`. Since July the pushes are
Dependabot bumps and PRs nobody merges; issues keep arriving.

Who wrote the 866 commits after v1.0.0: Bella-Giraffety 208, "coder" 104, "mayor" 92, Steve
Yegge 32, "chrome" 20, "pipboy" 15. Three of the top five are agent identities. In July, an
address at Fiserv (72) and Bella-Giraffety (66) wrote nearly all of it.

## What changed in the code

**Added packages:** `acp`, `doltserver`, `estop`, `reaper`, `scheduler`, `quota`, `telemetry`,
`wasteland`, `krc`, `nudge`, `proxy`, `github`, `bitbucket`, `worktree`, `health`, `hooks`,
`channelevents`, `agentlog`, and others. Several new things are supervisors: an emergency stop, a
reaper, a scheduler, a quota manager, health checks. Running more agents meant writing more code
to watch the agents.

**Removed packages:** `claude`, `opencode`, `swarm`. Per-vendor agent packages gave way to the
Agent Client Protocol (`acp`). The swarm vocabulary is gone; convoys won.

**Storage:** the move from SQLite+JSONL to Dolt, which Yegge says put Gas Town into maintenance
mode once it finished. Gas Town still forks `bd` and parses its JSON, at 168 call sites.

**New top-level:** Dockerfile, docker-compose, a Nix flake, `gt-model-eval/`, `plugins/`, and
`pr-sheriff-evidence/`, a directory of evidence files for an agent that polices PRs.

Formulas went down from 64 to 48. That and the swarm removal are the only places where
something got smaller.

## The README doesn't say it's over

The README grew by 350 lines and never mentions Gas City. Issue
[#4930](https://github.com/gastownhall/gastown/issues/4930) (18 Oct, no replies): "It's clear
that this repo was the base for Gascity, and support for this code has been dropped... But the
README doesn't even hint at it." The 18,445 stars point new users at the abandoned project.

## Two issues worth reading

[#4911](https://github.com/gastownhall/gastown/issues/4911), "Reaper stale auto-close treats
inactivity as resolution": the 6-hourly reaper closed five live bug reports in one day, each
still reproducible, one with 152,050 occurrences in the daemon log, the latest three minutes
after the close. Then it closed a task that a person had deliberately put on hold. The reporter:
"A bug report's age is uncorrelated with whether the bug is fixed."

That's what you get when status is a stored field and a patrol rewrites it on a timer. The
[task skill](../../skills/task/SKILL.md) handles the same situation with a stale buff that
advertises to the owner and expires on the next event. Nothing closes a task except its guard
passing.

[#4909](https://github.com/gastownhall/gastown/issues/4909), "Unrendered Handlebars block
helpers strip safety flags from destructive commands": the formula renderer substitutes
`{{var}}` but leaves `{{#if dry_run}}--dry-run{{/if}}` verbatim. The reaper formula wraps
`--dry-run` that way in four places, so `gt reaper purge` "has always run live", and setting
`dry_run="true"` has never done anything. The documented safety control was never reachable,
and the agent got template syntax in its command line and had to guess. A dry-run flag you've
never seen work is the cost of never reading the code, in one bug.

## Where Yegge went

**3 April, [Gas Town: from Clown Show to v1.0](https://steve-yegge.medium.com/gas-town-from-clown-show-to-v1-0-c239d9a407ec).**
Gas Town and Beads hit 1.0. "Gas Town has largely been in maintenance mode since the Dolt
migration finished up"; new effort goes to Gas City. At an IT Revolution talk around then: "we
just hit version 1.0 and we're just about to deprecate it. Am I Google or what?"

**24 April, [Welcome to Gas City](https://yegge.ai/essays/welcome-to-gas-city/).** Gas Town
"torn apart and rewritten from the ground up as an SDK", with composable "packs" for any agent
topology, "not just the hardwired original (and complex) Gas Town team shape". It ships a pack
that replicates Gas Town and imports its rigs and beads. "I did not write Gas City. It was
created by Julian Knutsen and Chris Sells", who he says are "far more serious and disciplined
engineers than me". In the talk he describes Gas Town's roles as "the funny costumes they were
wearing". The vocabulary survived into Gas City anyway: GUPP, NDI, molecules, convoys, seances,
MEOW.

**August, [The Shape of Things to Come, Part 1](https://yegge.ai/essays/the-shape-of-things-to-come/).**

> "Gas Town was intended to be reusable, but I only ever wound up using it to build itself.
> Gas Town fell apart at the seams with Opus 4.7... it always wanted to fiddle with Gas Town
> itself... so Gas Town effectively burned down."

Since Fable 5 arrived he has "returned full-time to my 30-year-old video game, Wyvern", which
he'd stopped developing in 2022 with "a 100-year work backlog". Wyvern is the multiplayer game
he began in 1996 and launched in 2001, with player-wizards who build and script the world; its
history and object model are in [YEGGE-ARC-ANALYSIS.md](YEGGE-ARC-ANALYSIS.md). He introduces
Wheelhouse, the private orchestrator his agents use to build it:
"reinvented something strangely Gas Town shaped from first principles", mostly Bash "because the
agents said that was best", 150k to 300k lines plus 25k lines of elisp. "Not that I have ever
seen any of it. But that's what they tell me."

**24 August, [Fences, not Sandboxes](https://yegge.ai/essays/fences-not-sandboxes/).** His
agents kept using words he didn't understand (fences, ratchets, governors, tripwires, latches,
falsifiers), so after "the 100th 'fence' reference" he had them audit themselves. They had built
a legal system: a constitution, case law, offices, registries, and about 450 legal artifacts,
with officers named Marshal, Seneschal, Reeve and Beadle. Rules tighten each time they're
violated: custom, then advisory, then constitutional law, then a program that refuses. He reports
50–60 agents, 21 Claude Max accounts, and $122k a month of API-equivalent token use.

**15 September, [Seats and Sunsets](https://yegge.ai/essays/seats-and-sunsets/).** The factory
is mostly idle because he can't afford the tokens: one account's week of quota goes in 2 to 4
hours, and he stopped adding accounts at 21. Earlier it had seized up from overfencing: "over 400
ruling/law beads, 185 rule rows in CLAUDE.md alone, and 650 distinct refusal sites across 173
scripts. Before too long, no work was legal." Fable cut it down to 14 fences, and new ones now
need his signature. He also cut almost 500k lines from Wheelhouse. And: "Gas Town was a better
name than even I realized at the time."

Cameron McAinsh's [summary of the three essays](https://cameronmcainsh.com/yegge-wheelhouse/)
adds context. The $122k is API-equivalent; his out-of-pocket is about $5,000 a month. Wheelhouse
is about 600k lines, mostly Bash, against about 1.2M lines of Wyvern. Wheelhouse maintenance takes
20–25% of his Wyvern time. His players asked him to slow down the features. An unplanned Beads
release broke users' systems.

**GitHub, October.** All his public activity is PRs on `gastownhall/beads`, none on Gas Town or
Gas City. His own repos show `efrit` (a native elisp coding agent, updated July) and `ejacs` (his
2008 JavaScript interpreter in Emacs Lisp, republished in June). His GitHub profile lists no
Twitter account; yegge.ai, Medium and LinkedIn are where he posts now.

## What it means for the comparison

**He agrees with the critique of the team shape.** Gas City exists because Gas Town's fixed cast
of costumed roles didn't generalize, and Yegge says so. The costumes stayed in the new
vocabulary all the same.

**"Never seen the code" became policy, and it cost him.** He didn't know what his own system's
jargon meant until he ordered an audit, and what he found was 450 artifacts he hadn't read. That
is [§2.1 and §2.2 of the analysis](GASTOWN-VS-MOOLLM-ANALYSIS.md) playing out a second time, at
larger scale: agents minted names nobody could decompress, and nobody read what got built. A
600k-line governance layer for a 1.2M-line game is "Code's Worst Enemy" with a ratio attached.

**Overfencing is scar tissue.** A rule that only tightens, created by every postmortem and
curated by nobody, is the SCAR-TISSUE sin in [no-ai-slop](../../skills/no-ai-slop/CARD.yml):
accumulated corrections that outlive their reason. His fix is a manual damper, a cap of 14 and
his signature on new ones. MOOLLM's version is structural. A restriction is a
[buff](../../skills/buff/SKILL.md) with a host, a reason and an expiration date, so it has to
earn renewal instead of staying by default. A fence with `expires:` can't pile up into 650
refusal sites.

**Seats are a convergence, and his phrase is good.** A seat is a durable role with its context,
authority and history, which any model can boot into. That's what MOOLLM's characters and
[incarnation](../../skills/incarnation/) skill do, and what cauldron does when an instance's
identity is its directory. His argument for seats, "caution you can look up is caution you can
afford", is the prepaid-context argument in
[no-ai-humansplaining](../../skills/no-ai-humansplaining/). The difference is where the lookup
lands. A seat's definition is context paid for in tokens on every boot. MOOLLM tries to make
the name do the work, pointing into what the model already knows, and spells out only what it
can't know.

**The fuel argument now comes with his numbers.** His list of fuel-efficiency levers includes
on-demand priming, smaller tasks, handing off earlier, and routing to cheaper models. Those are
the semantic image pyramid, cauldron's playbooks and per-phase model routing, and speed-of-light
simulation in one context. He reached them by running out of money. The analysis said the token
bill follows from the philosophy, and these essays are that bill.

**Credit where due.** The 2026 essays report failures plainly: the burned-down Gas Town, the
paralysis, the cost, the broken Beads release, players asking him to slow down. That's more
candor than "Welcome to Gas Town" had, and it makes them more useful to read. The throughput
claims (250 to 300 meaningful commits a day on Wyvern) are self-reported about a private system,
so I can't check them.

## Sources

- [gastownhall/gastown](https://github.com/gastownhall/gastown), issues
  [#4909](https://github.com/gastownhall/gastown/issues/4909),
  [#4911](https://github.com/gastownhall/gastown/issues/4911),
  [#4916](https://github.com/gastownhall/gastown/issues/4916),
  [#4930](https://github.com/gastownhall/gastown/issues/4930)
- [gastownhall/gascity v1.0.0 release](https://github.com/gastownhall/gascity/releases/tag/v1.0.0) (21 Apr 2026)
- Steve Yegge, [Gas Town: from Clown Show to v1.0](https://steve-yegge.medium.com/gas-town-from-clown-show-to-v1-0-c239d9a407ec) (3 Apr 2026)
- Steve Yegge, [Welcome to Gas City](https://yegge.ai/essays/welcome-to-gas-city/) (24 Apr 2026)
- Steve Yegge, [From Vibe Code to Fleet Mode](https://videos.itrevolution.com/watch/1184927954/) (IT Revolution talk)
- Steve Yegge, [The Shape of Things to Come, Part 1](https://yegge.ai/essays/the-shape-of-things-to-come/) (Aug 2026)
- Steve Yegge, [Fences, not Sandboxes](https://yegge.ai/essays/fences-not-sandboxes/) (24 Aug 2026)
- Steve Yegge, [Seats and Sunsets](https://yegge.ai/essays/seats-and-sunsets/) (15 Sep 2026)
- Cameron McAinsh, [Steve Yegge's Wheelhouse](https://cameronmcainsh.com/yegge-wheelhouse/) (4 Oct 2026)
- Thomas Jankowski, [The rulebook is the moat](https://thomasjankowski.com/writing/the-rulebook-is-the-moat/) (8 Oct 2026)
