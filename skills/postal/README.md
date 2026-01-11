# Postal System

Complete messaging: letters, texts, goals, rewards, attachments.

## Key Insight

**Any character can send goals** — not just Mom! She's just a character who happens to send loving letters.

## It's 2026!

You have a phone. Mail and texts are always available.

```yaml
player:
  devices:
    phone:
      always_carried: true
```

## Quick Use

### Send a Letter

```yaml
letter:
  from: "characters/npcs/bartender/"
  to: "player"
  subject: "A Favor"
  body: "Could you deliver this package?"
  
  creates_goal:
    id: deliver-package
    complete_when: "player gives package to mayor"
```

### Send a Text

```yaml
text:
  from: "characters/real-people/don-hopkins/"
  to: "player"
  body: "Meet me at the pub!"
  delivery: instant
```

### Mail to Storage

```yaml
letter:
  from: "player"
  to: "storage/vault/"
  attachments:
    - type: gold
      quantity: 500
      action: send
```

## Deterministic Routing

The simulator delivers mail without LLM. Addresses are paths, not names.

See [SKILL.md](./SKILL.md) for full documentation.
