# Mail Routing — Deterministic Message Delivery

> *"The simulator delivers mail without asking the LLM."*
> — Adventure Compiler Design Principle

---

## Why Deterministic?

The adventure simulator needs to deliver messages during its tick cycle **without LLM intervention**. This means:

1. **Addresses are paths**, not names
2. **Routing is rule-based**, not semantic
3. **Delivery is a simulation phase**, not an action

---

## The Message Delivery Phase

Every simulation tick includes a message delivery phase:

```
┌─────────────────────────────────────────────────────────────┐
│                     SIMULATION TICK                          │
├─────────────────────────────────────────────────────────────┤
│  1. RESET        — foo_effective = foo                      │
│  2. BUFFS        — Apply buff modifiers                     │
│  3. SIMULATE     — Objects run simulate()                   │
│  4. MAIL         — Deliver queued messages  ← NEW!          │
│  5. EVENTS       — Process event queue                      │
│  6. NAVIGATION   — Move player if requested                 │
│  7. DISPLAY      — Update UI                                │
└─────────────────────────────────────────────────────────────┘
```

---

## The Message Queue

Messages are queued for delivery, not sent instantly:

```yaml
# world.skills.postal state
mail:
  outgoing: []    # Messages queued this tick
  incoming: []    # Messages received this tick
  
# When you "send" a message, it goes to outgoing:
world.queue_mail(message)

# During MAIL phase, outgoing is processed
```

---

## Routing Instructions

Each message carries routing instructions the simulator can execute:

```yaml
message:
  id: msg-001
  from: "player"
  to: "characters/family/mom/"
  
  # ROUTING INSTRUCTIONS (deterministic)
  routing:
    # Step 1: Resolve destination
    destination_type: character    # character, room, object, directory
    destination_path: "characters/family/mom/"
    
    # Step 2: Find delivery point
    delivery_point: inbox          # inbox, messages_array, directory
    inbox_path: "characters/family/mom/INBOX.yml"
    
    # Step 3: Attachment handling
    attachments_transfer:
      - type: object
        ref: "brass-key"
        action: send
        from_inventory: "player"
        to_inventory: "characters/family/mom/"
        
    # Step 4: Side effects
    triggers:
      - event: MESSAGE_RECEIVED
        data:
          from: "player"
          to: "characters/family/mom/"
          subject: "Found it!"
          
      - event: GOAL_COMPLETE
        condition: "message.completes_goal is not null"
        data:
          goal_id: "find-locket"
```

---

## Address Types

### 1. Reserved Keywords

```yaml
to: "player"       # → world.player
to: "party"        # → all world.party.members
to: "narrator"     # → special: triggers narrative event
```

### 2. Character Paths

```yaml
to: "characters/family/mom/"
# Resolved to:
#   destination_type: character
#   delivery_point: characters/family/mom/INBOX.yml (if exists)
#                   characters/family/mom/messages/ (fallback)
```

### 3. Room Paths

```yaml
to: "pub/"
# Resolved to:
#   destination_type: room
#   delivery_point: pub/messages/ or pub/mailbox.yml
```

### 4. Object Paths

```yaml
to: "start/mailbox.yml"
# Resolved to:
#   destination_type: object
#   delivery_point: object.messages array
```

### 5. Directory Paths (Storage)

```yaml
to: "storage/vault/"
# Resolved to:
#   destination_type: directory
#   delivery_point: storage/vault/deposits/
#   attachments placed directly in directory
```

---

## Delivery Algorithm

```python
def deliver_mail(world):
    """
    MAIL phase of simulation tick.
    Delivers all queued messages without LLM.
    """
    outgoing = world.skills.postal.get('outgoing', [])
    
    for message in outgoing:
        routing = resolve_routing(world, message)
        
        # Transfer attachments
        for transfer in routing.get('attachments_transfer', []):
            if transfer['action'] == 'send':
                move_item(
                    world,
                    transfer['ref'],
                    from_path=transfer['from_inventory'],
                    to_path=transfer['to_inventory']
                )
        
        # Deliver to inbox or create file
        if routing['delivery_point'] == 'inbox':
            add_to_inbox(world, routing['inbox_path'], message)
        elif routing['delivery_point'] == 'messages_array':
            add_to_object_messages(world, routing['destination_path'], message)
        else:
            create_message_file(world, routing['destination_path'], message)
        
        # Update message status
        message['status'] = 'delivered'
        message['delivered'] = world.timestamp
        
        # Trigger events
        for trigger in routing.get('triggers', []):
            if evaluate_condition(world, trigger.get('condition', 'true')):
                world.trigger_event(trigger['event'], trigger['data'])
    
    # Clear outgoing, populate incoming
    world.skills.postal['outgoing'] = []
```

---

## Resolve Routing Function

```python
def resolve_routing(world, message) -> dict:
    """
    Convert symbolic address to deterministic routing instructions.
    This runs ONCE when message is queued, not at delivery time.
    """
    to = message['to']
    routing = {}
    
    # Reserved keywords
    if to == 'player':
        routing['destination_type'] = 'player'
        routing['destination_path'] = 'player'
        routing['delivery_point'] = 'inbox'
        routing['inbox_path'] = 'player/INBOX.yml'
        
    elif to == 'party':
        # Expand to all party members
        routing['destination_type'] = 'multi'
        routing['destinations'] = [
            resolve_routing(world, {**message, 'to': member})
            for member in world.party.get('members', [])
        ]
        
    # Character path
    elif to.startswith('characters/'):
        routing['destination_type'] = 'character'
        routing['destination_path'] = to
        inbox_path = f"{to}/INBOX.yml"
        if path_exists(world, inbox_path):
            routing['delivery_point'] = 'inbox'
            routing['inbox_path'] = inbox_path
        else:
            routing['delivery_point'] = 'directory'
            routing['messages_dir'] = f"{to}/messages/"
            
    # Room path (ends with /)
    elif to.endswith('/') and not to.startswith('characters/'):
        routing['destination_type'] = 'room'
        routing['destination_path'] = to
        # Look for mailbox object or inbox
        mailbox = find_object_with_tag(world, to, 'mailbox')
        if mailbox:
            routing['delivery_point'] = 'messages_array'
            routing['object_path'] = mailbox['path']
        else:
            routing['delivery_point'] = 'directory'
            routing['messages_dir'] = f"{to}/messages/"
            
    # Object path (ends with .yml)
    elif to.endswith('.yml'):
        routing['destination_type'] = 'object'
        routing['destination_path'] = to
        routing['delivery_point'] = 'messages_array'
        
    # Directory (storage)
    else:
        routing['destination_type'] = 'directory'
        routing['destination_path'] = to
        routing['delivery_point'] = 'directory'
        routing['messages_dir'] = f"{to}/messages/"
    
    # Resolve attachment transfers
    routing['attachments_transfer'] = []
    for attachment in message.get('attachments', []):
        if attachment.get('action') == 'send':
            routing['attachments_transfer'].append({
                'type': attachment['type'],
                'ref': attachment['ref'],
                'action': 'send',
                'from_inventory': resolve_inventory_path(world, message['from']),
                'to_inventory': resolve_inventory_path(world, to),
            })
    
    return routing
```

---

## Integration with Postal

The postal system uses deterministic mail routing:

```yaml
# Mom's letter (postal layer)
letter:
  from: "characters/family/mom/"    # Deterministic!
  to: "player"                      # Reserved keyword
  creates_goal:
    id: find-locket
    
# Generates routing instructions:
routing:
  destination_type: player
  destination_path: player
  delivery_point: inbox
  inbox_path: player/INBOX.yml
  triggers:
    - event: GOAL_CREATED
      data:
        goal_id: find-locket
        from: "characters/family/mom/"
```

---

## World Functions

```javascript
// Queue a message for delivery (next tick)
world.queueMail(message)

// Check for incoming mail this tick
world.hasNewMail() -> bool
world.getNewMail() -> list

// Immediate delivery (skips queue, used by narrator)
world.deliverMailNow(message)
```

---

## Protocol Symbol

```
DETERMINISTIC-ROUTING — Simulator delivers without LLM
```
