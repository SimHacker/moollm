---
name: postal
description: Messaging between any addressable endpoints. Letters, texts, attachments, goals, deterministic delivery.
allowed-tools:
  - read_file
  - write_file
tier: 1
protocol: POSTAL-SYSTEM
tags: [moollm, mail, message, goals, rewards, attachments, phone, communication]
related: [goal, character, object, room, storage, buff, inventory]
adversary: instant-coupling
---

# Postal System

Anything addressable can send and receive mail: the player, characters, rooms, objects,
directories. Messages are YAML files that move through the world carrying objects and goals.
The simulator delivers them deterministically, without asking the LLM.

## Addresses are paths

Addresses are paths, not names, so routing needs no interpretation:

```yaml
from: "characters/family/mom/"     # character
to: "player"                       # reserved keyword
to: "pub/"                         # room
to: "start/mailbox.yml"            # object
to: "storage/vault/"               # directory
```

Reserved keywords: `player` (current player), `party` (all members), `narrator` (system voice).

Mail goes anywhere pointers go, using the same pointer syntax as
[inventory](../inventory/SKILL.md): `config.yml#settings`, `README.md#install`,
`engine.cpp:142`. Not every address makes sense as a mailbox, but every one is valid.

## Letters and texts

| | Letter | Text |
|---|---|---|
| Delivery | Queued, takes turns | Instant |
| Attachments | Anything | Photos only |
| Goals | Create, modify, complete | Rarely |
| Template | [LETTER.yml.tmpl](LETTER.yml.tmpl) | [TEXT.yml.tmpl](TEXT.yml.tmpl) |

[MESSAGE.yml.tmpl](MESSAGE.yml.tmpl) is the general transport form with delivery and postage
fields. The player carries a phone, so mail, texts and notifications are always reachable.

## Goals come from anyone

Any character can assign, change or complete a goal by mail. Mom is just a character who happens
to write warm letters; the bartender, a stranger or a real person's portrayal can do the same.

```yaml
letter:
  from: "characters/npcs/bartender/"
  to: "player"
  subject: "A favor to ask"
  body: "Could you deliver this package to the mayor?"
  creates_goal:
    id: deliver-package
    complete_when: "player has talked to mayor with package"
    reward: { gold: 50 }
```

`modifies_goal` and `completes_goal` work the same way. Characters can also send mail from
triggers (`on_goal_complete`, `on_danger`, `on_long_silence`).

## Attachments

| Action | Effect |
|---|---|
| `send` | Move from sender to recipient |
| `give` | Recipient gets it; sender may keep it |
| `copy` | Duplicate for recipient |
| `reference` | Mention without transfer |
| `unlock` | Grant access to a room |
| `apply` | Apply a buff |
| `generate` | Create an image on delivery |
| `forward` | Attach another message |

Attachment types: object, gold, image, buff, room, message. Transfers use the inventory
protocol.

## Inbox and outbox

Each endpoint can have an `INBOX.yml` ([template](INBOX.yml.tmpl)). Without one, mail lands in
the endpoint's `messages/` directory. An `OUTBOX.yml` ([template](OUTBOX.yml.tmpl)) optionally
stages drafts before sending.

Lifecycle: `draft -> outbox -> in_transit -> delivered -> read`.

## Delivery

Mail is a phase of the simulation tick, after objects simulate and before events process. Each
tick decrements `turns_remaining` for messages in `world.skills.postal.in_transit`; at zero the
message is delivered and `MAIL_ARRIVED` fires. Details in [ROUTING.md](ROUTING.md).

| Method | Turns | Cost |
|---|---|---|
| `text` | 0 | free |
| `letter` | 3 | 1 gold |
| `express` | 1 | 5 gold, tracked |
| `courier` | 2 | 10 gold, guaranteed |
| `freight` | 10 | 0.5 gold/kg |
| `logistics` | 0 | free, internal transfers |

Distance is counted in hops through the room graph and adds time and postage per hop. Texts,
system messages and mail within one location are free. Lost mail is an optional mechanic: a
small loss chance, with lost items turning up somewhere findable.

## Postal is the transport layer

Logistics containers don't need bots to move items. When a requester needs something, the
logistics engine sends a `logistics` transfer from a provider: instant and free. Texts can carry
signals, such as a forge texting the player when coal runs low.

Physical couriers stay available as an option for drama: a courier the player can see,
intercept or redirect, at the cost of travel time. Use couriers for drama and postal for
efficiency.

## Commands

`CHECK PHONE`, `READ MAIL`, `READ [letter]`, `COMPOSE`, `REPLY`, `ATTACH [item]`, `SEND`,
`TEXT [character]`.

Browser presentation: [BROWSER-UI.md](BROWSER-UI.md).
