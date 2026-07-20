# cursor-mirror 🪞

## Watch Yourself Think

Every AI coding session asks the same question sooner or later:

> **WHAT THE HELL WAS I THINKING?!?!?**

The chat context gets summarized and fades — but it's all still there. Cursor
records every prompt, every hidden reasoning block, every shell command, every
file it read, every context it assembled, in local SQLite databases and
plaintext transcripts. cursor-mirror knows how to read all of it and render it
in human-friendly and LLM-friendly ways.

It is an [Anthropic-compatible MOOLLM skill](../../designs/anthropic-skill-extensions.md)
wrapped around a Python library: 73 read-only commands, 7 output formats,
importable modules, and a YAML reference model of Cursor's internal data —
so the mirror stays accurate by editing a *model*, not by patching code.

```bash
# What just happened?
cursor-mirror timeline @1

# What files did it actually read?
cursor-mirror context-sources @1

# What was it thinking?
cursor-mirror thinking @1

# What did all those tool calls do?
cursor-mirror tools @1 -v
```

**This is not debugging. This is understanding.** Papert argued that
metacognition needs concrete artifacts — you can't think about thinking
without something to inspect. Your agent's session history is that artifact.
cursor-mirror puts it on the shelf where you can look at it.

Strictly read-only (`sqlite3 ... ?mode=ro`): it observes the record, it never
alters it. The archive stays fixed; only your understanding changes.

## The Killer Demo: Look Into Your Own Mind, Write a Skill

The reason to believe any of this works is that we just used it.

An agent spent an evening doing delicate, unprecedented work — surgically
correcting the author name in a 2014 ACM paper to honor its author, Vanessa
Freudenberg, with the original preserved and every change disclosed (the
[Prestoration case](../../designs/prestoration/)). The session wandered through
font-subset archaeology, kerning arithmetic, wrong turns, and error messages.

Then cursor-mirror was turned around and pointed at that session: every shell
command, every thought bubble, every mistake and recovery, searchable and
replayable. From that self-inspection the agent wrote
[**change-name**](../change-name/) — a reusable skill with a working scanner
script and a step-by-step playbook, including a "traps learned the hard way"
section distilled from its own recorded stumbles.

That's the loop:

1. **Play** — perform one concrete instance, solving problems as they come,
   mapping the shape of the problem.
2. **Learn** — shine cursor-mirror over the thought stream and tool commands.
   What actually happened? Where did understanding diverge from execution?
3. **Lift** — write it up as a skill anyone (human or agent) can reuse.

Programming by demonstration, where the demonstration is your own transcript.
The methodology is [play-learn-lift](../play-learn-lift/); an earlier worked
example is the [Confetti Crawler case study](docs/CASE-STUDY-CONFETTI-CRAWLER.md),
and cursor-mirror analyzing [its own development session](docs/SELF-ANALYSIS.md)
is the strange loop that started it.

## How It's Built

Three layers, deliberately separable:

| Layer | Where | What |
|-------|-------|------|
| **CLI** | [`scripts/cursor_mirror.py`](scripts/cursor_mirror.py) (~700 lines) | Thin argument-parsing shell; the LLM-readable docstring up top is the definitive interface |
| **Library** | [`lib/`](lib/) (~10,000 lines, 22 modules + 16 command modules) | The actual knowledge: databases, paths, bubbles, composers, transcripts, exports — importable without the CLI |
| **Reference model** | [`reference/`](reference/) | YAML schemas of Cursor's data and protocols: key catalogs, data schemas, a [universal SQLite model](reference/universal/CURSOR-SQLITE-MODEL.yml) |

The reference model is the part worth stealing. Cursor's internals are
undocumented and shift under us, so we track them as *data*: when a format
changes, we edit the model, not scattered Python. And we didn't map it alone —
[`reference/assimilated/`](reference/assimilated/) harvests findings from 21
other open-source projects that also reverse-engineered Cursor's internals,
triangulated against our own probes. Steal from the best; cite what you stole.

### Composability: Skills Wrapping CLI Tools Wrapping Libraries

The great thing about Anthropic's skill model is composition: skills wrapping
CLI tools, blending multiple skills in one shell pipeline, loops of standard
Unix commands mixed with specialized tools designed to be called by LLMs.

Wrapping a CLI tool in a skill means users — and plain shell scripts — can
call the tangible tool directly, **no LLM required**. And writing the CLI as a
thin wrapper around a rich modular library means other programs can plug the
modules together directly, without going through the arcane (but apparently
extremely LLM-friendly) bash syntactic sirup of ipecac.

```python
from lib import resolve_composer, load_bubbles, iter_bubbles

for bubble in iter_bubbles(resolve_composer("moollm")):
    ...  # your tool here
```

The broader vision is a **network of composable Python modules with CLI
wrappers**, factored at whatever granularity is most ergonomic and
LLM-friendly for the task at hand — from focused Unix-philosophy tools up to
kitchen-sink tools like `python`, `psql`, and `gcloud`; appropriate for the
skill and the scale, indie to enterprise.

The economics point one direction: **maximize determinism, efficiency,
composability, reproducibility, testability, and profilability — minimize
LLM calls, nondeterminism, and token cost.** The LLM's job is to explore a
problem once and lift the solution into deterministic code; after that, the
tool runs for free, forever, the same way every time. Latent knowledge is
prepaid; deterministic tools are paid off. cursor-mirror is both the
instrument for that lifting (inspect the exploration, extract the procedure)
and an example of its product (a testable CLI + library where there used to
be an agent fumbling through SQLite by hand).

MOOLLM names these patterns as K-lines, so they can be discussed, inherited
from, and operationalized rather than re-derived each session:

- **[sister-script](../sister-script/)** — the doc-first pattern where a
  skill's procedure is lifted into a script that *is* the documentation:
  deterministic ground truth the LLM (and the human, and the test suite) can
  triangulate against. `cursor_mirror.py` is the sister script of this skill;
  [`pdf_name_scan.py`](../change-name/scripts/pdf_name_scan.py) is
  change-name's.
- **[sniffable-python](../sniffable-python/)** — structure code (or any file
  format) so an LLM can learn the interface from the first screenful: the
  machine-readable docstring atop `cursor_mirror.py` with command summaries,
  reference syntax, and gotchas is the worked example.

Not new ideas — Unix philosophy and literate programming are decades old.
The point of naming them is Minskyan: a K-line is a name that re-activates a
whole constellation of practice at the cost of one word. And wrapping a
concept or a script in a MOOLLM skill is how it enters the MOOLLM object
system and operating system: it gains an interface (CARD), inheritance
(prototypes), composition (`related`, `composes_with`), security posture
(`permissions`, skill-snitch), and discoverability (advertisements) — while
remaining a plain script anyone can run.

None of which is exotic. In MOOLLM, directories are membranes; a skill is
just a directory with a known membrane protocol, and the same is true of any
MOOLLM object encapsulated in a directory — a character, a room, a reference
model. `ls` is the object browser. It's not profound, and that's the point:
the normalcy is what makes it calm but powerful to work with.

There's prior art with a good pedigree: Owen Densmore and David S. H.
Rosenthal — both of NeWS, where Densmore's `object.ps` made PostScript
dictionaries Smalltalk-shaped — patented implementing a class hierarchy of
objects directly in a hierarchical file system
([US 5,187,786](https://patents.google.com/patent/US5187786A), 1993):
directories as classes and instances, files as methods, inheritance by path.
MOOLLM skills are that idea running on an LLM instead of a shell. And the
layers above it come for free: **git is the multiverse layer** — every branch
a timeline, every commit a saved world-state, checkouts as travel between
them — and **GitHub is the social networking layer**, where the objects get
identities, followers, issues, and pull requests. Skills inherit all of it
just by being directories.

Skills that already compose with this one:
[skill-snitch](../skill-snitch/) (runtime security surveillance),
[thoughtful-commitment](../thoughtful-commitment/) (commit messages mined from
thinking blocks), [change-name](../change-name/) (born from a cursor-mirror
self-analysis, as above).

## Reverse Engineering Manifesto

Cursor is proprietary software, and it is reasonable to protect private APIs
and trade secrets; there is a natural tension between reverse engineering and
platform control, and we respect it. Cursor also stores its state in readable
local formats, which makes introspection possible.

We still need to get work done. So we reverse-engineer our own local data,
carefully, read-only, and accept that what we learn may change. We maintain
the schemas ourselves and keep them current. This is not hostility — it is
pragmatic engineering under uncertainty, with collaborative intent: we hope it
feeds back into Cursor and benefits its users, including us.

## Why This Exists

| Without cursor-mirror | With cursor-mirror |
|-----------------------|--------------------|
| "Why is this slow?" | `timeline @1` → 47 tool calls, 3 semantic searches |
| "What files did it read?" | `context-sources @1` → 12 files, 4 terminal snapshots |
| "Is my .cursorrules working?" | `request-context @1` → shows exact rules loaded |
| "What model ran?" | `models @1` → model + token counts |
| "Can I recover that chat?" | `export-chat @1 --yaml` → full transcript |
| "What did I do last night?" | `grep`, `thinking`, `tools` → write it up as a skill |

## I-Beam: Ask Those Questions in Chat

You don't have to learn the commands. cursor-mirror is integrated into the
MOOLLM adventure universe through **[I-Beam](docs/I-BEAM.md)** — a character
(a tall, blinking text cursor embodied; every platform has one) who provides
the natural-language interface. Nobody anthropomorphizes I-Beam, because
I-Beam is just a cursor. That you can talk to. And that talks back. And that
can change the world. Ask the left column of that table in plain
chat, and I-Beam performs the right column for you: composing the queries,
eliding the boring, highlighting what matters, and remembering your goals
across questions.

I-Beam has a personality and is the **anti-Clippy** — more trippy than
Clippy: it never interrupts, it
only answers when summoned, and it shows its work — every answer comes with
the commands it ran, so you learn the CLI by watching. It advertises its
services the way Sims objects do, so the right capability surfaces when you
need it, including compositions of cursor-mirror with other skills and tools.
And it's easily extensible: teach it new tricks by **programming by
demonstration** (do the thing once; it watches its own transcript with
cursor-mirror and lifts the procedure) or by natural-language "just asking"
training — tell it what you want it to remember, and it does.

Full character, methods, incarnation modes, and dialog examples:
[docs/I-BEAM.md](docs/I-BEAM.md).

## Installation

```bash
# Python 3.8+ and PyYAML; nothing else
cd skills/cursor-mirror
pip install pyyaml
python3 scripts/cursor_mirror.py --help
```

Works standalone on macOS (Linux/Windows paths modeled, not yet battle-tested).
Read-only by construction — it cannot corrupt Cursor's data.

```bash
cursor-mirror status              # health check: workspaces, composers, DB sizes
cursor-mirror tail @1 -n 10       # last 10 messages of the current chat
cursor-mirror --sources status    # show WHERE the data lives — teach a fish to LLM
```

## Documentation Map

The details live in `docs/` — the README you're reading is the trailhead:

| Doc | What's inside |
|-----|---------------|
| [docs/COMMANDS.md](docs/COMMANDS.md) | All 73 commands by category, output formats, reference shortcuts (`@1`, hash prefix, name fragment, `w3.c2`), example session |
| [docs/INTERNALS.md](docs/INTERNALS.md) | What you can inspect and where it lives: bubbles, context assembly, tool records, server config, both data stores, schemas |
| [docs/SELF-ANALYSIS.md](docs/SELF-ANALYSIS.md) | cursor-mirror analyzing the 18-hour session that created it |
| [docs/CASE-STUDY-CONFETTI-CRAWLER.md](docs/CASE-STUDY-CONFETTI-CRAWLER.md) | Play-learn-lift in action: why the LLM failed on prose, how inspection found the gaps, how the sister script fixed it |
| [docs/I-BEAM.md](docs/I-BEAM.md) | The anti-Clippy, the all-reflecting I-of-the-pyramid of attention: the adventure-universe character that wraps the CLI in conversation — personality, advertised services, canon (NOT a person), trainable by demonstration or by asking |
| [docs/MOOLLM-INTEGRATION.md](docs/MOOLLM-INTEGRATION.md) | Boot optimization, kernel drivers, probe caches, advisory files |
| [docs/ZIZEK-GERMAN-TOILET.md](docs/ZIZEK-GERMAN-TOILET.md) | Three bowls, three software souls: why cursor-mirror is the Inschpektor |
| [SKILL.md](SKILL.md) / [CARD.yml](CARD.yml) / [GLANCE.yml](GLANCE.yml) | The skill protocol at three resolutions |
| [reference/](reference/) | The reverse-engineered YAML model: schemas, key catalogs, 21 assimilated external projects |
| [gallery/IMAGE-GALLERY.md](gallery/IMAGE-GALLERY.md) | Image archaeology: 25+ images recovered from chats, with context |

> 💡 **For LLMs**: sniff the docstring atop
> [`scripts/cursor_mirror.py`](scripts/cursor_mirror.py) — it is the
> machine-readable interface, with command summaries, reference syntax, and gotchas.

## The Science (Why Introspection Matters)

> *"You can't think about thinking without thinking about thinking about something."*
> — Seymour Papert, *Mindstorms* (1980)

**Constructionism** (Papert, 1980) — the Logo turtle made geometry visible so
children could debug their mental models. cursor-mirror makes agent behavior
visible so you can debug your mental model of how your orchestrator works.

**Society of Mind** (Minsky, 1986) — intelligence emerges from interacting
agents. cursor-mirror shows which agents activated, what context was
assembled, how the orchestrator reasoned.

**Schema Mechanism** (Drescher, 1991) — learning as `Context → Action →
Result` schemas. cursor-mirror provides exactly those triples, from life.

- **Papert, S.** (1980). *Mindstorms: Children, Computers, and Powerful Ideas.*
- **Minsky, M.** (1986). *The Society of Mind.*
- **Drescher, G.** (1991). *Made-Up Minds: A Constructivist Approach to Artificial Intelligence.*
- **Laurel, B.** (1991). *Computers as Theatre.*

## See Also

- [Prestoration](../../designs/prestoration/) — the founding worked example: memorial edition, ethics, play-by-play
- [Vanessa's philosophy](../../designs/vanessa-freudenberg-philosophy.md) — why her SqueakJS work matters: JS not WASM, hybrid GC, MOOLLM parallels
- [change-name](../change-name/) — the skill lifted from that session's transcript
- [Anthropic Skill Extensions](../../designs/anthropic-skill-extensions.md) — how MOOLLM skills extend Anthropic's model
- [Skill Ecosystem](../../designs/SKILL-ECOSYSTEM.md) — trust tiers and curation via cursor-mirror + skill-snitch
- [MOOLLM for Hackers](../../designs/MOOLLM-FOR-HACKERS.md) — 5-minute tour

## License

**MIT License** — Copyright (c) 2026 Don Hopkins, Leela AI. See [LICENSE](./LICENSE).

---

*The filesystem is your memory. The database is your brain. Now you can see inside.*
