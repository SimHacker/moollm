# The rules-injection conundrum

Every coding agent reads instruction files off the filesystem and prepends them
to your prompt. None of them can tell you, reliably, *which* files those are,
*why* those and not others, or what they cost you per request. This is a design
problem with a paradox at the bottom of it, and it is currently being paid for
in tokens by everyone.

Separate two questions that get run together:

1. **Which rules files should the orchestrator inject, and how does it decide?**
   Unsolved, arguably unsolvable in the general case — see the paradox below.
2. **How do you manage your rules, whatever the answer to (1) turns out to be?**
   Still needed even if (1) is solved tomorrow, and the part we can build.

## Receipt: one session, four repos, none of them the project

Measured live, in a Cursor session whose nominal project was `MicropolisCore`,
with 25 repositories open as workspace folders.

Always-injected, in that session's system context:

| File | Bytes |
|---|---|
| `Leela/git/moollm/.cursorrules` | 12,874 |
| `Leela/git/moollm/.cursor/rules/moollm-core.mdc` | 6,819 |
| `Leela/git/central/.cursorrules` | 5,660 |
| `~/.cursor/plugins/cache/cursor-public/svelte/.../svelte-mcp-tools.mdc` | — |

`MicropolisCore`, the project, contributed nothing. A Svelte plugin rule was
present in a session with no Svelte in it. Two unrelated repos supplied ~25 KB
of ambient instruction to every request.

Present on disk and *not* injected:

- `central/tools/.cursorrules`, `central/packages/.cursorrules`,
  `central/packages/pyvision/.cursorrules`, `central/tools/llm/.cursorrules`
  — legacy rules files in subdirectories of an open repo.
- `git/synth/.cursorrules`, `Leela/git/unlimite-context/.cursorrules`
  — repos on the same disk, not open as workspace folders.

**Observed rule: eligibility is per open workspace folder, at folder root.** Not
per repo, not per current directory, and not per filesystem. Open a folder and
you have signed up for its root rules everywhere, forever, in every chat.

## Receipt: what this costs

At Leela, a rules file in a library repo carried that library's entire
documentation. Any workspace that included the repo injected the whole thing
into every prompt for every developer, silently, until somebody went looking.
The bill was real money, and the pollution was worse than the bill.

**How it was found is the whole lesson.** Not from the bill — the bills were
high and stayed unexplained. It surfaced when Cursor brought up that library in
a conversation that had nothing to do with it. Somebody asked the obvious
question, *why did you mention that?*, and the answer was that it was sitting in
the prompt. Then: oh no.

Note what that means. **The symptom that finally exposed the leak was semantic
contamination, not cost.** The money had been visible for a while and pointed
nowhere, because a large bill does not name its cause. What pointed at the cause
was the model behaving as though something were relevant when it was not — the
pollution seeping into an unrelated conversation and corrupting it. Irrelevant
context does not sit inertly; it bids on your attention, and the model answers
the prompt it was given rather than the one you meant.

That is the detection signal worth institutionalizing: **an unexplained
reference is a context leak until proven otherwise.** It is also an argument for
provenance in the manifest, since "why did you mention that?" should be
answerable by the tool rather than by an investigation.

The same shape is sitting in the tree right now: `Leela/git/openclaw/AGENTS.md`
is 41,953 bytes, 5,555 words — call it 10–11K tokens at a repo root, eligible
for always-injection the moment that folder is open. Nobody put it there
maliciously. It grew.

Also from the same survey, and worth knowing:

- `blink/.cursor/rules/skills/cursor-db/SKILL.mdc` is 30,061 bytes. Skills
  compiled into rules files is already common practice, which makes rules the
  place where large content accumulates.
- `openclaw/src/plugins/CLAUDE.md` is a 9-byte symlink to `AGENTS.md`. So is
  every other `CLAUDE.md` in that repo. The convergence on a cross-tool standard
  is happening by symlink, in the absence of one.
- Nested `AGENTS.md` files are everywhere in `openclaw` and `tensorzero`:
  `src/plugins/`, `src/channels/`, `tests/e2e/.../`. Real projects depend on
  subdirectory scoping working.
- Zero `.cursorignore` files in 25 repos. The blast-radius control exists and
  nobody uses it.

## Bear traps: an instruction file is an executable you did not consent to run

The `openclaw` example above is not hypothetical enough to be comfortable, so
state the general case plainly.

**Reading a repository should not be the same act as running it.** Cloning
something to look at it is the most ordinary thing a programmer does, and it has
always been safe, because looking is not executing. Root-level instruction files
break that. Open the folder in a workspace and its `AGENTS.md` becomes eligible
for injection into the prompt of an agent with tool access. **You did not run
anything. You looked.** And the file is now steering an agent that can read your
other repositories, run shell commands, and write files.

The mechanism is worse than "content you did not read gets injected," because
that describes a dependency too, and dependencies at least announce themselves
in a manifest. Here:

| | A dependency | A root instruction file |
|---|---|---|
| How it enters | You declare it | The folder is open |
| Consent | Explicit, versioned | None |
| Visibility | Lock file, diff on change | No manifest; you find out by accident |
| Scope | The project that declared it | Whatever else is in the workspace |
| Runs when | You invoke it | Every turn, silently, forever |

The specific case that prompted this: **`openclaw` is in the tree because it was
worth looking at, not because there is any intention of running it.** But its
declared methodology is vibe coding — as a matter of stated policy, the source
and the prompts do not get read. So the honest description of `AGENTS.md` in
that repo is 42 kilobytes of unreviewed instructions, unreviewed *by its own
authors, on principle*, to a program holding tools. Whether that is benign is
unknown to everyone, including them. That is not an accusation of malice. **It
is the absence of anyone in a position to make the assurance.**

And the failure is silent in both directions. You do not learn the file was
injected; you learn that the model said something strange, months later, if you
are lucky and paying attention — which is exactly how the Leela leak surfaced.

### What the people who ship these files owe everyone else

Not much, and it is cheap:

1. **Do not put an always-injected file at a repository root** unless the repo's
   purpose is to be run as an agent workspace. Put it where the scoping rules
   can contain it.
2. **Keep it small enough to read**, on the theory that an instruction file
   nobody reads is an instruction file nobody has verified. Forty-two kilobytes
   fails this on its face.
3. **State what it assumes about the agent's tools and reach.** A file written
   for a sandboxed CI agent lands very differently in a multi-root desktop
   workspace with shell access.
4. **Say what it is for at the top, in one line**, so a reader who opens the
   folder for five minutes can decide whether to `.cursorignore` it.

> Stop leaving bear traps in random directories of random repositories that
> might get mounted into somebody's workspace.

### What you owe yourself, because nobody is going to do the above

The mitigations are all local and all boring:

- **`.cursorignore` any repository you are reading rather than working in.**
  Zero of twenty-five repos here have one, which is the real finding of the
  survey. This is the whole fix and it takes one line.
- **Clone read-only material outside the workspace roots.** Curiosity and
  workspace membership should be separate decisions, and right now opening a
  folder conflates them.
- **Diff the manifest, not the repo.** The question is never "what is in this
  repo," it is "what changed about what reaches my prompt" — which is the
  `mirror` half of the chain below, and the reason it has to come first.

The general principle, since it outlives Cursor's current file formats:
**anything auto-loaded into a privileged context is executable, whatever its
extension.** Markdown is not inert when the reader has a shell.

## What the tools actually read

Cursor's current documentation, with the documented/undocumented line marked,
because most of what circulates about this is folk knowledge from old docs.

| Location | Status | Behavior |
|---|---|---|
| `.cursor/rules/*.mdc` | documented | The only project-rule format. **A plain `.md` in that folder is silently ignored** — no frontmatter, no rule. |
| `AGENTS.md` | documented | Root *and* subdirectories. Nested files combine with parents, more specific winning. |
| `CLAUDE.md` | help center only | Read like `AGENTS.md`, and **always applied to every conversation regardless of any `alwaysApply` setting**. |
| `.cursorrules` | legacy | Project root only. "Will be deprecated" — future tense, so not yet declared removed. Absent from the reference page entirely. |
| User Rules | documented | Account-level, syncs across machines. |
| `~/.cursor/rules` | help center only | Machine-local files, explicitly do not sync. |
| Team Rules | documented | Server-side, dashboard-managed. |

Frontmatter decides *when*, and the four cases are documented:

| `alwaysApply` | `description` | `globs` | Injected |
|---|---|---|---|
| `true` | — | — | Always. Globs and description ignored. |
| `false` | — | set | When a matching file is in context. |
| `false` | set | — | Agent reads the description, pulls the body if relevant. |
| `false` | — | — | Only when `@`-mentioned. |

Rule contents land at the *start* of the model context. Precedence on conflict:
Team → Project → User. Rules apply to Agent chat only, not Tab, Inline Edit, or
Bugbot.

**Correction worth having, because everyone repeats the old version:** nested
`.cursor/rules` directories that "automatically attach when files in their
directory are referenced" is text from *older* Cursor docs. It is gone from
[the current reference](https://cursor.com/docs/rules), which now discourages
nesting and says to keep rules flat. Third-party tutorials still reproduce the
removed sentence. Directory-scoped instruction is still documented — but via
nested `AGENTS.md` and nested skills, not via nested rules.

**Multi-root workspaces are undocumented entirely.** The only authoritative
statements are Cursor staff on the forum, and they match the measurement above:
every root is scanned; glob-scoped rules stay within their own root; and
`alwaysApply: true` is *not* root-scoped, so an always-on rule at any root
covers the whole workspace. Staff call that a known gap. They also confirm
duplicate always-rules across roots "load multiple times and use extra
context — a known caveat." With 25 roots open, that caveat is the architecture.

Cross-tool: skills are an actual open standard
([agentskills.io](https://agentskills.io)), with Cursor reading `.agents/skills/`
plus `.claude/skills/` and `.codex/skills/` for compatibility. `AGENTS.md` is
supported but the docs never cite the cross-tool spec, so Cursor is not a
citable source for calling it a standard — which is presumably why the field is
converging by symlink instead.

## The paradox

A rules file in a subdirectory can only be honored if it has been read. So when
should the orchestrator read it?

Scope it by "the directory the agent is working in" and you have invented a
current directory that does not exist. Context spans many directories in many
repos at once; there is no cursor position in the filesystem. A path string in
context is not the same as being in that path.

Now make it a prohibition. `forbidden/.cursorrules` says *do not read this
directory or any file in it*. For that instruction to bind, it must already be
in context — which means it had to be preemptively loaded, which is the thing
subdirectory scoping was invented to avoid. The rule that says "don't come in
here" is unreachable by any policy that only loads rules once you have come in.
The set of rules you must read to know what not to read is not a set you can
compute lazily. It is Russell's paradox with a working directory.

Both horns are bad:

- **Preload everything.** Every `.cursorrules`, `AGENTS.md`, and `*.mdc` in
  every open repo, every request. Correct, and it is the Leela bill.
- **Load on reference.** Cheap, and prohibitions arrive after the violation.

**The paradox only exists if you try to solve it in the context window.** A
prohibition enforced by the harness costs zero tokens and is checked lazily, at
access time, by the tool that would have opened the file — which never needed
the rule in the prompt to begin with. The unreachable-rule problem is an
artifact of treating "don't read this" as something to *tell the model* rather
than something to *enforce around it*.

Cursor already half-implements this and the split is instructive.
`.cursorignore` is a separate channel from rules: root-anchored, `.gitignore`
syntax, and it blocks agent reads and `@`-mentions rather than merely blocking
indexing. That is the prohibition channel, and it is correctly out of band. Two
documented holes in it, both worth knowing: "the terminal and MCP server tools
used by Agent cannot block access to code governed by `.cursorignore`" — a shell
`cat` walks right through — and per-directory `.cursorignore` files only work if
you opt into the Hierarchical Cursor Ignore setting. In 25 repos here there are
zero `.cursorignore` files, so in practice the channel is unused and the
prohibitions people write are the unenforceable kind, in prose, in a rules file,
hoping the model reads them. The docs are candid that this cannot work:
"complete protection isn't guaranteed due to LLM unpredictability."

That leaves a real distinction for whatever remains in the prompt, and no
current format marks it:

- *Prohibitions* belong in the enforcement layer, out of band, checked at access
  time. If one must appear in the prompt, it should be a short manifest, never
  shipped in the same file as 40 KB of style guidance.
- *Preferences* (idioms, conventions, house style) can and should be lazy,
  attached when a matching file actually enters context.

Documented guidance already points this way and is widely ignored: keep rules
under 500 lines, split large rules, and "reference files instead of copying
their contents." The 42 KB `AGENTS.md` above is eleven times that budget.

## How can a glob trigger possibly work?

Worth answering precisely, because the obvious guess is the expensive one.

It is **not** "hand the rule to the model and let it decide whether it applies" —
that would burn tokens on every rule in every repo. Nor is it a filesystem scan
for glob matches, which would fire on files nobody is looking at.

The documented trigger is "auto-attached when a matching file is **in context**,"
and per Cursor staff, in-context means the file was attached, `@`-mentioned, or
opened by the agent. So the orchestrator matches the glob **against the paths of
files as they enter the context**, and attaches the rule if one matches. That is
deterministic, free, and evaluated outside the model. Directory nesting is
irrelevant to it: the glob is a predicate over a path, not a location in a tree.

It also explains the documented gap — "if the agent edits or creates the file
without opening it first, the rule never gets pulled in." The trigger is a hook
on a context-entry event, so an action that skips the event skips the rule.

**The mechanism is right and the vocabulary is impoverished.** There are exactly
two ways to express when a rule applies, and they sit at opposite extremes:

| Trigger | Evaluated by | Cost | Expressive power |
|---|---|---|---|
| `globs:` | orchestrator | free, deterministic | "a path matched" — and nothing else |
| `description:` | the model | tokens, non-deterministic | anything, unreliably |

Everything a person actually wants to condition on falls in the gap: the
language of the file, whether this repo has a particular dependency, whether the
working tree is dirty, whether a tool is installed, how large the file is,
whether the task is a refactor or a first draft, which other rule already fired.
None of that is a path, so all of it must be smuggled into a `description:` and
adjudicated by the model, one prompt at a time.

**Rules need a machine-evaluable trigger language, and the Sims already has the
shape of it.** An object advertisement is precisely a cheap, structured,
engine-evaluable predicate-plus-score attached to an expensive body: the engine
scores hundreds of advertisements without ever running the interaction. That is
the property to steal. Applied here:

- Triggers are **structured data, not prose**, so the orchestrator can evaluate
  them over every candidate rule in every open root without a model call.
- Triggers **score rather than match**, so a crowded context can take the best
  *n* instead of everything above zero — and so competing rules can be ranked
  rather than concatenated.
- The **body stays lazy.** A rule that scores low costs its predicate and
  nothing more, which is what makes 150 candidates affordable.
- Whatever cannot be expressed as a predicate falls back to the description,
  which becomes the escape hatch rather than the default.

The filter should be as aggressive as the language permits, because the whole
game is discarding candidates without reading them. See
[`ADVERTISEMENT-AUCTION.md`](ADVERTISEMENT-AUCTION.md) for the scoring model,
including why the answer is usually not pure argmax.

## Even if that is solved, you still need a manager

Assume the injection question gets answered perfectly. You still have no way to
answer, mid-task: what is in my context right now, where did it come from, what
did it cost, is it helping, and can I swap it for a different set?

What a context manager owes you:

- **Named task contexts.** The rules for "debug the renderer" are not the rules
  for "write the docs." There is no single set that should be on at all times.
- **A library of compiled contexts**, switchable, so rebooting your focus is one
  command rather than an editing session. *(Open TODO for the boot compiler.)*
- **Binding to a conversation.** Attach a compiled *set* to this chat and keep
  it there. The pieces exist and do not add up: a Manual rule can be
  `@`-mentioned into one message, and Option+Enter on a skill promotes it to a
  Custom Mode where it "stays in context on every turn... until you exit the
  mode" — one skill, one session. There is no named, saveable, switchable
  rule-set profile, and nothing binds a bundle to a conversation.
- **Visibility with prices.** Partly solved and worth using: Cursor's context
  ring breaks the window down by category with a dedicated Rules line, so the
  aggregate is measurable today. What is missing is per-rule attribution — which
  repo, which file, how many tokens each. The Leela incident was invisible at
  that granularity, which is why it lasted.
- **Provenance.** Which repo, which commit, who wrote it, when it last changed.
- **Measurement.** Which rules were actually consulted versus merely carried.
  Rent-free residence in every prompt should require evidence of use.

## Skills are the better unit, and rules files are what you manage them with

The whole document so far treats rules files as the thing to fix. They are not
worth fixing as the primary carrier. **The unit of context should be a skill,
not a rules file**, and the difference is not cosmetic — nearly every problem
above is a property of the container rather than the content.

| | Rules file (`.cursorrules`, `AGENTS.md`) | Skill |
|---|---|---|
| Granularity | One file, whole repo | One directory per capability |
| Activation | Path or always-on | Advertisement, on demand, at a chosen depth |
| Resolution | Flat: all of it or none | Pyramid: GLANCE → CARD → SKILL → README |
| Cost | Paid every turn, forever | Paid at the tier you actually needed |
| Composition | Concatenation, in an order nobody chose | Indexed, cross-linked, contextualized in prose |
| Provenance | The file, if you can find it | Named skill, versioned, with a card that says what it is for |
| Audit | Read 42KB | Read a 40-line GLANCE, then decide |

The four properties that matter:

1. **Granularity.** A skill is one capability. Wanting one thing out of a rules
   file means taking the file, and that is precisely how the Leela leak turned
   into a bill: an all-or-nothing container with something useful in it.
2. **Semantic pyramids.** A skill can be consulted at a cost proportional to how
   much you need — GLANCE to decide, CARD to sniff the interface, SKILL for the
   protocol. A rules file has one resolution and it is *all of it*.
3. **Advertisements, on cards.** Sims objects broadcast what they offer, agents
   bid, the winner runs. That is an *auction*, and an auction is exactly the
   thing missing from the rules mechanism, which has no way to express "I am
   worth 200 tokens for this task and zero for that one." The
   [glob section](#how-can-a-glob-trigger-possibly-work) above is the same
   argument arriving from the other direction: `globs:` is an impoverished bid
   language, and advertisements are the vocabulary it is missing.
4. **Indexed and contextualized.** `skills/INDEX.md` links skills to each other
   in natural language — *this one is the deterministic counterpart to that
   one*. Rules files have no equivalent, so a repo with fifteen of them has
   fifteen strangers.

**And the orchestrator should participate, not just the model.** The current
split gives the orchestrator only path matching and hands everything else to the
LLM, which is why "let the model decide if it applies" costs tokens to reach the
conclusion that it does not apply. A skill's activation conditions should have a
**deterministically decidable subset** the orchestrator can evaluate itself,
over every candidate file, before assembling the prompt — with the model
consulted only for what genuinely needs judgment. Cheap filter first, expensive
filter second, which is the ordinary shape of every query planner.

### The objection that deserves an answer: won't better models make this moot?

The strongest thing said against skills is that they teach the model what it
already knows. It is a fair hit against most of them — a skill restating git's
documentation is pure overhead, and gets worse with every model release.

**What survives model improvement is policy, not knowledge.** A skill that says
what a tool does is a cache of the training data and it decays. A skill that
says *how we do it here* — ordering, length, voice, which checks are mandatory,
what never to touch — encodes decisions the model has no way to infer, because
they are not facts about the world. They are facts about you. A better model
follows them better; it does not make them unnecessary.

The test is one question: **would a smarter model derive this on its own?** If
yes, delete the skill. If no, it is policy and it keeps earning.

The corollary, and it is the reason for the whole file format: **a prompt should
expire into a checked-in file.** The useful half of a good prompt is a decision
worth keeping, and typed into a chat window it evaporates when the session ends.
Written to a skill it becomes reviewable, diffable, and shared. The
commit-message trick some people use — stashing the prompt in the commit so it
can be found later — has the right instinct and the wrong store, since `git log`
is searchable only by the person who already knows what they are looking for.

### But rules files are what you have, so use them to manage skills

This is not a proposal to stop writing them. They exist, other people's exist,
and the blunt globally-scoped haphazardly-obeyed ones are going to keep landing
in the workspace whatever anyone prefers.

**The move is to demote them: a rules file should be a loader and a floor, not a
library.** Small, readable in one screen, carrying the prohibitions that must
hold everywhere plus pointers to skills for everything else. The ambient skills
in `.cursorrules` here are that pattern already — inlined at glance resolution
with a link down to the full protocol, so the always-on cost is a summary rather
than a corpus.

Which makes the chain below the enforcement mechanism for the demotion:
`cursor-mirror` shows what the blunt instruments actually injected,
`skill-snitch` audits it, and `bootstrap` compiles the minimum that has to be
always-on. **Manage rules with skills, rather than writing skills as rules.**

## The chain we have: mirror, snitch, boot

Three MOOLLM skills already form the observe-audit-compile loop, which is the
part of the manager that can be built without vendor cooperation:

**[`cursor-mirror`](../skills/cursor-mirror/)** — observation. Reads Cursor's
own SQLite state and transcripts: what was actually loaded, what the agent
actually did, which files it actually touched. You cannot manage a context you
cannot see, and this is the only way to see it from outside.

**[`skill-snitch`](../skills/skill-snitch/)** — audit. Static scan plus runtime
surveillance via cursor-mirror, comparing what a skill *declares* against what
it *does*. This is what makes ambient status a privilege rather than a default:
ambient means living in every prompt rent-free, and only audited skills get it.

**[`bootstrap`](../skills/bootstrap/)** — compilation. Emits `.cursor/rules/` and
`.moollm/` from the skill tree, inlining ambient skills and generating indexes.
The `.cursor/rules/moollm-core.mdc` in the receipt above is a compiled artifact,
not a hand-written file. Recompile after a pull, after changing ambient skills,
or when context feels stale.

The loop: **mirror** measures what happened, **snitch** checks it against what
was promised, **boot** recompiles the injected set accordingly.

**The measurement that closes it** is the one nobody has: which skills actually
fired. Mirror can read that out of the transcripts — not which were *available*
but which were consulted, and at which tier of the pyramid — and hand it to
bootstrap as a preload set. A skill consulted every session earns promotion to
the preload cache; a skill carried in every prompt and never consulted gets
demoted to on-demand. That is the "evidence of use" requirement from the manager
list above, implemented with the parts already on the table.

**And the loop should not stop at observation, which is the gap here.** Somebody
else built the missing step first and it is worth crediting, because convergent
design on a real problem is stronger evidence than either party could
manufacture alone. ygjb, describing his own **SessionMiner** — a post-session
hook that analyzes the session, decides whether the approach should become a
skill, and **messages him for follow-up when it thinks so**, otherwise
cataloguing it so later analysis can find trends in how he uses his tools:

> "Over time it has built me a fairly decent stable of repeatable skills and
> tools, and highlighted process deficiencies and nominated process changes that
> I have pursued."

`verified: verbatim, https://news.ycombinator.com/item?id=49594458`

The word doing the work is **nominated.** Observation tells you what happened;
nomination turns it into a proposal a human can accept or decline. The
mirror-snitch-boot chain above measures and recompiles but never proposes, and
that is the piece to build — with the human as the approver, which is also what
keeps the loop from optimizing itself somewhere nobody chose to go.

Note where the analyzer runs, because it is an architectural property rather
than a convenience: **on a hook, at a session boundary, outside the loop it
observes.** An analyzer that ran inside the session could steer the thing it is
measuring. This one cannot, which is what makes its output trustworthy enough
to act on.

## The pyramid is the compression scheme, not a documentation aesthetic

The skill tree is 150 directories, all 150 carrying the full `GLANCE.yml` +
`CARD.yml` + `SKILL.md` triple. Injecting 150 `SKILL.md` files is the Leela
bug at scale, so the
multi-resolution structure is not a documentation aesthetic — it is the
compression scheme that makes a large skill library affordable at all:

| Level | Size | Question it answers |
|---|---|---|
| `GLANCE.yml` | 5–70 lines | Is this relevant? |
| `CARD.yml` | 50–200 lines | What can it do? |
| `SKILL.md` | 200–1000 lines | How does it work? |
| `README.md` | 500+ lines | Why does it exist? |

Only the top rungs are ambient. The rest is addressable but absent — present as
an advertisement rather than as content, in the Sims sense: the object announces
what it affords, cheaply, and you pay for the body only when you take the offer.
An index of 150 advertisements costs less than one 42 KB `AGENTS.md`.

The vendor has arrived at the same split, and its own documentation states it
plainly in the context-window breakdown: **"Rules: project and user rules
included in the prompt"** versus **"Skills: skill descriptions injected into the
system context."** Rules ship the body; skills ship the advertisement and fetch
the body on demand. Cursor's `/migrate-to-skills` command moves exactly the
description-triggered rules into the skills system while leaving `alwaysApply`
and glob rules behind — which is the whole argument of this document, shipped as
a migration tool. The remaining disagreement is only about how many rungs the
ladder needs: one description is an advertisement, and `GLANCE` → `CARD` →
`SKILL` → `README` is a mipmap.

## Our own drift, caught by our own audit

Writing this section turned up three different skill counts in three places:

| Source | Claimed | Actual | Now |
|---|---|---|---|
| `skills/INDEX.md` header | 129 skills, updated 2026-03-24 | 150 | fixed |
| compiled `.cursor/rules/moollm-core.mdc` | 133 skills, 10 ambient | 150, 11 | fixed |
| the same file, one line up | 121 skills | 150 | fixed — two different counts in one compiled artifact |
| the filesystem | — | 150 dirs, 150 complete, 11 ambient | — |

Three numbers for one quantity, one of them twice in the same generated file,
none of them right, and the drift ran from March to September without anyone
noticing — because nothing recomputes them and nothing checks.

And a real defect, not just a stale integer: **`design-sense` declared
`ambient: true` in its own metadata and appeared in neither compiled ambient
list.** It had been asking to live in every prompt and was not getting in, since
whenever the last compile ran. Now fixed in both artifacts, which is why the
ambient count is 11.

That is precisely the declared-versus-observed gap `skill-snitch` exists to
find, discovered by running the audit by hand in the middle of arguing for it.
Note which direction it fails in: the compiler silently under-injects, so the
symptom is a skill quietly not working rather than a bill. Both failure modes
are invisible without measurement, and only one of them eventually gets noticed.

Recompile before quoting any of these numbers publicly.

## See also

- [`../skills/bootstrap/SKILL.md`](../skills/bootstrap/SKILL.md) — the compiler
- [`../skills/cursor-mirror/`](../skills/cursor-mirror/) — introspection
- [`../skills/skill-snitch/`](../skills/skill-snitch/) — audit
- [`ADVERTISEMENT-AUCTION.md`](ADVERTISEMENT-AUCTION.md) — advertisements and
  bidding, the mechanism behind loading what is worth loading
- [`LOAD-BEARING.md`](LOAD-BEARING.md)
