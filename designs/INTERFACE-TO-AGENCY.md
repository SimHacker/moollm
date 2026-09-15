# An interface to agency, not agents instead of an interface

The 1997 argument between Ben Shneiderman and Pattie Maes at IUI was never settled, it was
shipped in one direction. Maes's interface agents won the product war: the assistant, the
recommender, the chat window that stands between you and the thing you are working on.
Shneiderman's objection was not that software should be dumb. It was that automation must
arrive as **comprehensible, predictable, and controllable** machinery, with the object of
interest continuously visible and every action rapid, incremental, and reversible.

That objection describes a filesystem in a git repository, and nobody involved planned it
that way.

*"An interface to agency" is Don's formulation of Shneiderman's position, not a phrase of
Shneiderman's. His own vocabulary is direct manipulation, universal usability, supertools,
and human-centered AI. The formulation is a good one because it names what the alternative
gets wrong: agency is the thing you want, and an agent is only one way to package it.*

## The claim

**A MOOLLM repository is a direct-manipulation interface to a population of agents, where
the agents are files.** A coffeeshop is a directory. A cat is a YAML file. A memorial is a
file with citations in it. A consent record is a file that gates whether another file may be
rendered at all. Every one of them can be opened, read, edited by hand, diffed, reverted, and
grepped -- and every one of them can equally be operated on by an LLM through chat.

Two interfaces onto one set of continuously visible objects. Neither is privileged, and
neither hides state from the other.

## Why this satisfies the direct-manipulation test

Shneiderman's 1983 criteria, checked against the artifact rather than asserted:

| Criterion | How the repo does it |
|---|---|
| Continuous representation of the object of interest | the directory listing; `PLACE.yml` is the shop, not a description of a record about the shop |
| Physical action instead of syntax | edit the file; drop a photograph into `survey/`; delete a character to remove them |
| Immediate visible feedback | the diff |
| Rapid, incremental, reversible | commit, revert, branch. Reversibility is the substrate rather than a feature |
| Overview first, zoom and filter, details on demand | `ls`, then `GLANCE.yml`, then `CARD.yml`, then `SKILL.md`. The semantic image pyramid is his visual information-seeking mantra with a different sensor |

The last row is the one that surprised me. MOOLLM's reading-order discipline was designed to
manage LLM context, and it independently reinvented "overview first, zoom and filter, then
details on demand" -- because the constraint is the same whether the reader is an eye with a
fovea or a model with a window.

## What the agent-as-interface pattern takes away

An assistant with private state is unfalsifiable. You cannot open it, diff it, or revert it,
and when it is wrong about you there is no artifact to correct -- only more conversation,
which is why every such product eventually feels like arguing with a hotel clerk.

The MOOLLM inversion: **the agent has no state that is not a file you can open.** What the
cat at the 420 Café knows about John Sinclair is `memorial/john-sinclair.yml`, and if the cat
says something wrong, you fix the file. What the robot budtender may say is bounded by
`refuses:` in its own YAML. Whether a real person may be portrayed at all is decided by
`characters/consent.yml`, which a human wrote and can delete.

Control stops being a promise in a privacy policy and becomes a readable fact on disk. That
is the whole difference, and it is the reason the licensing, the provenance, and the consent
records in [amsterdank](https://github.com/SimHacker/amsterdank) are files rather than
policies: **a constraint that lives in the object travels with it.**

## Tangible agents

The objects are agents in the MOO sense -- they advertise what can be done to them, they hold
their own methods, they refuse things -- and simultaneously ordinary files. A coffeeshop
advertises `VISIT` and `READ-BOARD`. A cat advertises stories and refuses to speak as the dead.
A place refuses to average two coordinates. None of that requires a running process, because
the LLM supplies the interpreter and the directory supplies the state.

This is what makes them tangible rather than metaphorically tangible. You can `cp` a cat. You
can `git blame` a memorial and find out who claimed what, when. You can hand somebody the file
that is them, which is the design principle underneath
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md),
a budtender's tier-4 self-authored character, and a patron's `incarnate` grant. Handing over a
file is a transfer of authorship that no assistant-shaped product can offer, because there is
nothing to hand over.

## Chat is a second manipulator, not the interface

The natural-language channel earns its place by being **one of two ways in**, and it is
strongest exactly where direct manipulation is weakest: across many objects at once, on
underspecified intent, and on work that needs judgment about wording. Editing 228 places by
hand is miserable; asking for them all to be regenerated is easy. Conversely, fixing one
comment in one file by hand is instant, and doing it through chat is silly.

The discipline that keeps this honest: **the chat channel may only do things that leave a
diff.** No hidden memory, no learned preferences, no state in the assistant. If it cannot be
expressed as a change to a file, it did not happen.

## Where this sits

- [`DIRECTORY-AS-IUNKNOWN.md`](./DIRECTORY-AS-IUNKNOWN.md) — the mechanism: a directory as an interface-bearing object
- [`skills/design-sense/masters/ben-shneiderman.md`](../skills/design-sense/masters/ben-shneiderman.md) — his votes and vetoes as a loadable head
- [`skills/design-sense/lenses/direct-manipulation.md`](../skills/design-sense/lenses/direct-manipulation.md) — the lens
- [`skills/cursor-mirror/characters/i-beam/CONSTITUTION.md`](../skills/cursor-mirror/characters/i-beam/CONSTITUTION.md) — the anti-Clippy constitution, which is this argument applied to one character
- [`skills/representation-ethics/`](../skills/representation-ethics/) — consent as a file, which is control as a fact
- [wwsff `characters/ben-shneiderman/agents-debate-1997.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ben-shneiderman/agents-debate-1997.md) — the debate itself, and he is an [invited guest](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ben-shneiderman/invitation.md), so this doc should expect to be corrected by its subject

## The uncomfortable part

Shneiderman's veto list includes *don't ship an irreversible operation and call it power*, and
an LLM writing files is exactly that unless the reversibility is real. It is real here only
because of git, and only while the human keeps reading diffs. An agent that commits without
review, or a human who stops reading, converts this whole arrangement back into the thing it
was built to avoid -- an opaque process with private state, wearing a repository as a costume.

The interface to agency is not a property of the file format. It is a practice, and the diff
is where it is enforced.
