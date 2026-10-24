# MOOLLM 🐒

MOOLLM treats a git repository as a world that people and LLMs share, like a text adventure or a
MUD. Directories are rooms, files are the objects in them, and characters are files that a person
or a model can play. What the agents know how to do lives in skills: Markdown and YAML that the
model reads and follows, the way an interpreter runs a program. Everything is plain text in git, so
you can read it, diff it, and change it.

The name stands for Microworld Operating system for Orchestrated LLM Living Memory, after MOO, the
programmable MUD. Think of it as The Sims meets LambdaMOO, running inside your coding assistant.

## Try it

Browse on GitHub, with nothing to install:

| What | Where |
|------|-------|
| The main world: a pub, a street, a maze, 78 characters | [examples/adventure-4/](examples/adventure-4/) |
| A photo archive generated and annotated inside the world | [Lane Neverending slideshow](examples/adventure-4/street/lane-neverending/slideshow/SLIDESHOW.md) |
| MOOLLM interviewing itself | [a session transcript](examples/adventure-4/characters/real-people/don-hopkins/sessions/2026-01-28-moollm-interview.md) |
| A maze of twisty little passages, all alike | [examples/all-alike-maze/](examples/all-alike-maze/) |

Or play it: clone the repo and open it in Cursor or Claude Code, and let the editor finish indexing.
[QUICKSTART.md](QUICKSTART.md) walks through it. Drivers for each tool are in
[kernel/drivers/](kernel/drivers/README.md).

```bash
git clone https://github.com/SimHacker/moollm.git
cd moollm
cursor .        # or: claude
```

Then try commands like these:

```
LOOK                 describe the room you're in
GO north             move through an exit
EXAMINE lamp         look closely at something
GET lamp             pick it up
SUMMON palm          bring a character in
AS palm              play as that character
SPEED-OF-LIGHT 10    simulate ten turns in one model call
```

## Start here

| If you want | Read |
|-------------|------|
| The idea in one page | [designs/PROSTHETICS.md](designs/PROSTHETICS.md) |
| A technical tour | [designs/MOOLLM-FOR-HACKERS.md](designs/MOOLLM-FOR-HACKERS.md) |
| Every skill, in one list | [skills/INDEX.md](skills/INDEX.md) (156 skills) |
| How skills work as programs | [designs/eval/EVAL-INCARNATE-FRAMEWORK.md](designs/eval/EVAL-INCARNATE-FRAMEWORK.md) |
| The object system: prototypes, inheritance, and what the model fills in | [designs/object-system/](designs/object-system/README.md) |
| Agents and people sharing the same controls | [designs/INTERFACE-TO-AGENCY.md](designs/INTERFACE-TO-AGENCY.md) · [the 1997 agents debate](designs/AGENTS-DEBATE-1997.md) |
| Who may do what | [designs/MOOAM.md](designs/MOOAM.md) |
| What MOOLLM takes from MOO and LambdaMOO | [designs/MOO-HERITAGE.md](designs/MOO-HERITAGE.md) |
| Writing without AI slop | [skills/no-ai-slop/](skills/no-ai-slop/SKILL.md) |

## Indexes

| Index | What it lists |
|-------|---------------|
| [skills/INDEX.md](skills/INDEX.md) | Skills |
| [indexes/DESIGNS.md](indexes/DESIGNS.md) | Design documents |
| [indexes/SESSIONS.md](indexes/SESSIONS.md) | Play sessions and transcripts |
| [indexes/SLIDESHOWS.md](indexes/SLIDESHOWS.md) | Image galleries |
| [indexes/ANIMALS.md](indexes/ANIMALS.md) | Animal characters, from Palm the monkey to the cats |
| [indexes/DREAMS.md](indexes/DREAMS.md) | Characters' dreams |
| [indexes/PIONEERS.md](indexes/PIONEERS.md) | The people whose ideas this builds on |
| [indexes/XANADU.md](indexes/XANADU.md) · [indexes/FLUXX.md](indexes/FLUXX.md) | Xanadu; the Fluxx card game experiments |
| [indexes/](indexes/README.md) | All of the above |

## How it works

- **Rooms are directories.** Moving between them is navigation; a `ROOM.yml` describes a room, and a README explains it.
- **Objects and characters are files.** A character carries its own state, inventory and
  relationships, and can be played by a person or a model.
- **Skills are instructions the model executes.** Each skill has a short `GLANCE.yml`, a
  `CARD.yml` interface, a `SKILL.md` protocol and a README, read from the top down so the model
  loads only what it needs.
- **Comments are data.** YAML comments carry reasoning and intent that people and models both read.
- **Many turns in one call.** A single model call can play several characters through many turns,
  instead of a round trip per turn.

## Lineage

MOOLLM borrows from LambdaMOO (Pavel Curtis), The Sims (Will Wright), Society of Mind and K-lines
(Marvin Minsky), constructionism (Seymour Papert), Self (David Ungar and Randall Smith), and
Colossal Cave and Zork. [indexes/PIONEERS.md](indexes/PIONEERS.md) has the full list.

## Contributing

Play an adventure and keep the session, make a skill by copying [skills/skill/](skills/skill/), or
improve a map or index, and send a pull request.

## Related repos

| Repo | What |
|------|------|
| [SimHacker/WillWrightShowForFood](https://github.com/SimHacker/WillWrightShowForFood) | Repo Shows, built on MOOLLM |
| [SimHacker/MicropolisCore](https://github.com/SimHacker/MicropolisCore) | Micropolis (SimCity), with MOOLLM characters as tutors |

MIT License. — Don Hopkins
