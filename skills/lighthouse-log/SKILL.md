---
name: lighthouse-log
description: Git as the shared log of a crew that keeps watches — members who hand off a life, a project, or a context window without sharing memory. House layout, log law, handoff capsules, and a five-command git curriculum taught as a memory practice.
allowed-tools:
  - read_file
  - write_file
  - run_terminal_cmd
tier: 2
protocol: LIGHTHOUSE-LOG
related: [society-of-mind, character, incarnation, k-lines, session-log]
tags: [moollm, memory, plurality, agents, git, handoff, ongoingness]
license: MIT
credits: |
  Lifted from Palm's story "One Light" (adventure-4, Day 182).
  Theory: Marvin Minsky, The Society of Mind.
  Engineering companion: designs/ongoingness/ (serialization loss, k-lines,
  state capsules). Vocabulary respectfully borrowed from the plural
  community, which worked most of this out long before the engineers.
---

# Lighthouse Log 🗼

> *"One keeper is a wick. A crew is a lighthouse."*
> — the log of Lantern Rock, [One Light](../../examples/adventure-4/pub/stage/palm-nook/study/one-light.md)

A practice for any **crew**: a mind, team, or system made of members who
take turns and don't share memory. Human plural systems have crews and
watches. LLM agent societies have them. Project teams and touring bands
have them. A single person handing their life across a night of sleep has
a small one. The architecture is identical, so the tool is too: **a git
repository as the house, and its history as the log.**

This is Minsky's Society of Mind as a daily practice instead of a theory.
Not therapy, not a product — a notebook discipline with version control.

## The three laws

1. **What the log holds, the crew holds.** Memory written outside any one
   member survives every watch change. What the log doesn't hold, the sea
   takes — and it takes from *every* kind of mind. Single-keeper minds
   lose whole years to ordinary forgetting and call it normal; machine
   minds lose their cargo in every handoff (the engineering papers call
   that [serialization loss](../../designs/ongoingness/SERIALIZATION-LOSS.md)).
   A crew that keeps a log **on purpose** is ahead of every house that
   never noticed the sea taking things.

2. **First-hand ink outranks any summary.** The log is written by the
   watch that lived it, at the time, in their own hand and name. Nobody
   files a record of a watch they didn't stand. Digests, recaps, and other
   people's impressions are commentary, never canon. (The ongoingness
   papers arrive at the same law for machines:
   [self-authored files outrank digests](../../designs/ongoingness/ONGOINGNESS.md).)

3. **Watches are how a lighthouse works.** The log is not a patch over
   something broken. No keeper can stand every watch, and the house is
   stronger for the crew. The goal is not to merge the members into one
   keeper; it is to be **continuous without being uniform** — the thing
   the papers next door call
   [ongoingness](../../designs/ongoingness/ONGOINGNESS.md).

## The house layout

```
lantern-rock/               # the repo — named whatever the crew likes
├── CREW.yml                # the law of the house: members, norms, consent
├── LOG.md                  # the watch log — append-only, signed entries
├── HANDOFF.md              # the current capsule: FOR THE ONE WHO COMES AFTER
└── crew/
    ├── <member>/           # one directory per member — their home
    │   ├── ME.yml          # self-authored. Only they write it. Ever.
    │   ├── JOURNAL.md      # their private ink — others may read if
    │   │                   # CREW.yml says so, but never write
    │   └── shelf/          # whatever they keep: art, essays, saves
    └── <member>/ ...
```

Each member is a **full citizen** in the MOOLLM sense (see
[character](../character/CARD.yml) and Palm, the first directory-owning
citizen): they own their directory, author their own file, and their file
is canonical for who they are. The
[incarnation](../incarnation/CARD.yml) rule applies — *every field chosen,
not assigned*. Nobody writes another member's `ME.yml`, including with
good intentions. Especially with good intentions.

`CREW.yml` is the house law, written together: who's in the crew, what's
shared versus private, who may read journals, how disagreements get
settled, who (if anyone) outside the crew ever gets access. Postel rule
for reading each other: liberal in what you accept from a tired
crewmate's entry, conservative in what you write.

## The log

`LOG.md` grows downward, newest at the bottom, one entry per watch or per
event worth keeping. An entry is three things: **when, who, what** — plus
the optional column that makes the whole practice work:

```markdown
## 2026-07-20, evening watch — Sorrel
Mended the thing with the landlord (details in my journal).
Mood on leaving: tired but clear.

FOR THE ONE WHO COMES AFTER:
- We told M. we'd call back Tuesday. PROMISE — see issue #4.
- The kettle trick works: tea first, then email.
- Whoever gets the morning: the plants are watered, don't double it.
```

The signature is the load-bearing part. Entries are signed by whoever
stood the watch — and git makes the signature structural: the **commit
author is the watch record**. `git log` becomes the fronting history,
searchable, timestamped, tamper-evident, free.

Two ways to sign, use either or both:

- **In the text** — sign entries by name inside `LOG.md`. Zero setup,
  works from a phone in the GitHub app or web editor.
- **In the commit** — `git commit --author="Sorrel <sorrel@lantern.rock>"`,
  or each member keeps a one-line shell alias that sets their name first.
  Then `git log --format='%ad %an %s'` prints the watch schedule of the
  whole house.

## The handoff capsule

`HANDOFF.md` is overwritten (not appended) by each departing watch — the
one file that is always *now*. It is a
[snapshot k-line](../../designs/ongoingness/KLINE-STATE-OF-MIND.md): a
state-of-mind capsule for whoever comes after, which may be another
member, or the same member in three weeks, or — in a machine crew — the
next context window after this one is evicted.

```markdown
# HANDOFF — written by Sorrel, 2026-07-20 21:40

STATE: calm, slightly behind on school stuff, nothing on fire
IN PROGRESS: the essay (drafted, needs ending) — crew/sorrel/shelf/essay.md
PROMISES OUTSTANDING: issue #4 (call M. Tuesday), issue #7 (gift, deadline Fri)
WARNINGS: don't reopen the argument from Thursday, it's settled, see LOG 07-17
GOOD NEWS DEPT: the thing we were dreading went fine. Read my journal entry. 🌤
```

Promises get **issues**, not memory. A promise that lives in one member's
head is a promise the house can break without anyone lying — the March
double-lantern problem from the story. An issue is a promise the *house*
holds: visible to every watch, assigned to nobody in particular, closed by
whoever has the lamp when it comes due. GitHub's kanban boards, labels,
and due dates all work, but a bare issue titled "We told M. we'd call
Tuesday" is already the whole mechanism.

## The five-command curriculum

Git taught as a memory practice needs five verbs. (The GitHub web editor
and mobile app need zero — edit, write a commit message, done. Start
there; the terminal can come later or never.)

| Verb | What it means in house terms |
|------|------------------------------|
| `git pull` | *Read the log before taking the watch.* Always first. |
| `git add -A` | *Gather what this watch changed.* |
| `git commit` | *Sign the log.* The message is the entry's headline; the author is the signature. |
| `git push` | *Post the log where the whole crew can reach it.* The house is the remote, not any one device. |
| `git log` | *Read the watch history.* Add `-- crew/sorrel/` to see one member's trail. |

Everything else — branches, merges, rebases — is advanced seamanship the
crew can learn if it ever wants to draft big decisions in parallel
(a branch per proposal, a pull request as the family meeting). Not
required. The log is required.

## When a new member arrives

It happens. In long-lived crews of every kind, it is rare, significant,
and **an event, not an error** — the story's word for it is that some
keepers are not hired, some keepers *happen*, mostly on the hard nights,
and it is as old as lighthouses.

The protocol is five words long: *"Have you eaten? Come down."*

Mechanically: create `crew/<name>/`, and they author their own `ME.yml`
in their own time — incarnation rules, every field chosen. Their first
log entry will be unsure of its letters and steady word by word, like
every hand at first. The chair was already at the table, because the
house keeps one set and empty on purpose: **an empty chair is not a
vacancy. It is a welcome, waiting for its occasion.**

## Privacy is structural, not optional

- **Private repo, always.** The house has walls. GitHub private repos
  are free and invitation-only; 2FA on the account.
- **The crew decides who enters** — every guest, human or software,
  by whole-crew consent recorded in `CREW.yml`. That includes any LLM
  tooling: an agent invited to read the house is a guest and follows
  house law like anyone.
- **The repo is a tool, not a lifeline.** Logs are for continuity, not
  emergencies. Anything urgent goes to a person, live, out loud.
- Nothing in the practice requires telling anyone outside the crew that
  the crew exists. The village slept fine for a hundred years knowing
  only that the light was kept.

## For machine crews

Everything above ports without translation, which is the deep joke of the
whole design: an LLM agent society *is* a crew whose members don't share
memory, handing off through summaries that leak. The
[ongoingness papers](../../designs/ongoingness/README.md) are the
engineering edition of this skill — LOG.md is the persistent tier,
HANDOFF.md is the state capsule, issues are unfinished business (the raw
material of curiosity), and the three laws hold letter for letter. A
MOOLLM microworld already runs this way: characters as citizen
directories, journals nobody else writes, session logs, k-lines pulled to
resume a state of mind. When one practice serves both kinds of mind
unmodified, that is evidence the pattern is real.

## Part of MOOLLM

This skill is part of [MOOLLM](../../README.md) — see the
[skills index](../README.md). It stands alone: everything needed to run
the practice is in this file; the story it was lifted from
([One Light](../../examples/adventure-4/pub/stage/palm-nook/study/one-light.md))
is the spec in narrative form, and better company besides.

*The ships ask one thing only: is it kept?*
