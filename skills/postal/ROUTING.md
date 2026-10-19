# Mail Routing

The simulator delivers mail during its tick without the LLM. That works because addresses are
paths, routing is rule-based, and delivery is a simulation phase, not an action.

## Tick order

1. RESET: `foo_effective = foo`
2. BUFFS: apply modifiers
3. SIMULATE: objects run
4. MAIL: deliver queued messages
5. EVENTS: process the event queue
6. NAVIGATE: move the player
7. DISPLAY: update the UI

## Resolve once, deliver later

When a message is queued, its address is resolved into routing instructions stored on the
message. Delivery just executes them.

```yaml
routing:
  destination_type: character        # player, multi, character, room, object, directory
  destination_path: "characters/family/mom/"
  delivery_point: inbox              # inbox, messages_array, directory
  inbox_path: "characters/family/mom/INBOX.yml"
  attachments_transfer:
    - { type: object, ref: brass-key, action: send,
        from_inventory: player, to_inventory: "characters/family/mom/" }
  triggers:
    - { event: MESSAGE_RECEIVED, data: { from: player } }
    - { event: GOAL_COMPLETE, condition: "message.completes_goal", data: { goal_id: find-locket } }
```

## Resolution rules

Checked in order:

| Address | Type | Delivered to |
|---|---|---|
| `player` | player | `player/INBOX.yml` |
| `party` | multi | each member, resolved separately |
| `narrator` | narrator | narrative event |
| `characters/...` | character | its `INBOX.yml`, else its `messages/` |
| path ending in `/` | room | a tagged mailbox object, else `messages/` |
| path ending in `.yml` | object | the object's `messages` array |
| anything else | directory | `messages/`; attachments placed in the directory |

For each `send` attachment, resolution records the sender's and recipient's inventory paths.

## Delivery

For each queued message in the MAIL phase:

1. Move `send` attachments between inventories.
2. Write the message to its delivery point.
3. Set `status: delivered` and the delivery timestamp.
4. Fire each trigger whose condition holds.

Then clear the queue.

## World functions

- `world.queueMail(message)`: queue for the next MAIL phase.
- `world.hasNewMail()`, `world.getNewMail()`: check this tick's arrivals.
- `world.deliverMailNow(message)`: skip the queue (narrator use).
