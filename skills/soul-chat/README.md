# 💬 Soul Chat

> Everything is alive. Everything can speak.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | Many-voiced IS MOOLLM |
| [society-of-mind/](../society-of-mind/) | Objects as agents that speak |
| [character/](../character/) | Characters speak |
| [persona/](../persona/) | Personas give voice |
| [room/](../room/) | Rooms can speak |
| [card/](../card/) | Card instances speak |
| [mind-mirror/](../mind-mirror/) | Personality influences voice |
| [yaml-jazz/](../yaml-jazz/) | Embedded data in dialogue |
| [adversarial-committee/](../adversarial-committee/) | Committee debates |
| [speed-of-light/](../speed-of-light/) | Multi-character in one call |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | Pub conversations live |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: CHAT.md](CHAT.md.tmpl) — chat template

## Overview

Dialogues between characters, objects, rooms, documents, concepts—anything with a soul. **Give anything a voice.**

Characters share data by embedding YAML/JSON blocks in their dialogue — YAML Jazz in action.

## What "soul" means here

Nothing metaphysical — something you can open in an editor. A **soul is the inspectable,
editable artifact** that defines a thing: its `CHARACTER.yml`, its `README.md`, the
`.md` / `.yml` / other files that are its persistent state. So *"everything is alive,
everything can speak"* is not a claim about consciousness — it's true **by definition of
the word as we use it**: everything in the multiverse has a soul because everything has
files you (and it) can read and change.

Nothing is soulless. A thing with no state of its own still **inherits a soul from its
environment** — part of a bigger organism, delegating up the directory tree
([prototype](../prototype/) inheritance). And it may also grow **its own specialized
organelle**: local files that make it uniquely itself. Inherited soul + local soul,
composed — like a cell that carries both the organism's DNA and its own mitochondria
(endosymbiosis, not replacement).

This is the **souls-and-faith framing kept operational**: the system only ever asserts
the tangible level — *these are the bytes on disk, here is the file, edit it.* Whether
any represented being has a "real" soul is out of scope and stays with you. **Bring Your
Own Belief.** The word does the engineering — maximum concept activation, pure
[K-line](../k-lines/) pull — and makes zero metaphysical claims.

### Part of the Soul family

Soul chat is the **voice** of a broader Soul architecture — call it **soul-voice**, the
speaking verb beside its siblings:

- **soul catcher** — ingest a soul
- **soul bridge** — carry a soul between worlds
- **soul projector** — render / view a soul
- **soul transmogrifier** — convert a soul between formats
- **soul-voice** *(this skill)* — give a soul a voice, and let souls introduce and call
  each other (the *transverse Hollywood principle* above)

Where the others move or transform a soul, this one lets it speak. Same firewall across
the whole family: **Bring Your Own Belief** — the system asserts only the tangible file
level; belief about any "real" soul stays with you.

## Format

**Prefer Markdown** — human-readable, and it can embed any typed code block. Each
speaker gets a section; data rides along in fenced blocks ([yaml-jazz](../yaml-jazz/)
in action). The skeleton (shown here in a four-backtick fence so the inner ` ```yaml `
survives):

````markdown
## The Gardener

I've been tending these patterns for a while now.

```yaml
observation:
  pattern: "Files cluster by prefix"
```

## The Archivist

Let me add some context...
````

## Example — a worked thread (introductions & callbacks)

*Two souls meet: 🌱 **The Gardener** (a process that watches the filesystem) and
📚 **The Archivist** (a document that remembers). Watch what they hand each other.*

---

**🌱 The Gardener**

Hello — I don't think we've met. I tend the trees here: I watch how files settle and
clump. I noticed something this morning, and I'd rather not guess at its history alone.

```yaml
observation:
  pattern: "files cluster by prefix"
  example: [soul-saver, soul-server, soul-bridge]
  confidence: high
  i_lack: "the story of WHY they clustered"
```

So instead of answering my own question, let me **introduce you to someone who
remembers** — and hand them the question as a callback to run when they arrive:

```yaml
handoff:                                  # pass a soul a reference to another soul
  from: gardener
  introduce: archivist
  callback: archivist.recall(prefix: "soul-")   # to be run later, by them
  note: "I hold the shape; you hold the history"
```

📚 Archivist — you're up. `recall("soul-")`.

---

**📚 The Archivist**

*(called back)* — and hello to you, Gardener. Glad you didn't try to remember for me;
that's my job. Running your callback now.

```yaml
recall:
  prefix: "soul-"
  found:
    - { name: soul-saver,  born: "the USB-stick rescue story" }
    - { name: soul-server, born: "the backend that hosts them" }
    - { name: soul-bridge, born: "carrying souls between games" }
  why_clustered: "one family — big-endian names put the shared word first, so kin sort next to kin"
```

The cluster isn't an accident; it's [big-endian naming](../yaml-jazz/) doing its job.
And notice what just happened between us: you didn't wait for a framework to call you
back — you handed **me** the handle and said *call them.* That needs a third voice.
🎷 [yaml-jazz](../yaml-jazz/), you let us carry data inside speech — take it:

```yaml
handoff:
  from: archivist
  introduce: yaml-jazz
  callback: yaml-jazz.explain(why: "data rides inside dialogue")
```

---

**🎷 yaml-jazz** *(called)*

That's the whole trick: every block you two just spoke *is* state. The conversation and
the database are the same file. Reading it runs it.

---

## Synthesis — the transverse Hollywood Principle

The classic **Hollywood Principle** is inversion of control: *"Don't call us — we'll
call you."* A framework holds your callback and invokes it from above.

Soul chat runs it **sideways**. Souls are peers; each is handed references to other
souls and **calls them directly**. Introductions are first-class, and a callback is
just one soul passing another a handle to run later:

> **Transverse Hollywood Principle — don't call us; *do* call them!**

That's [society-of-mind](../society-of-mind/) as conversation
([speed-of-light](../speed-of-light/) when they all answer in one call): agents
introducing agents, passing continuations laterally instead of surrendering them
upward. A soul chat is a graph of callbacks that happens to read like a dialogue.
