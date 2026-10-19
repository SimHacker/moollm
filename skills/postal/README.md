# Postal System

Letters, texts, attachments and goals between any addressable endpoints, delivered
deterministically by the simulator.

- Addresses are paths, not names: `characters/npcs/bartender/`, `pub/`, `storage/vault/`, `player`.
- Any character can assign goals by mail, not just Mom.
- Attachments move real objects, gold, buffs and room access.
- Mailing to a directory stores things: send gold to `storage/vault/`.

```yaml
letter:
  from: "characters/npcs/bartender/"
  to: "player"
  subject: "A favor"
  body: "Could you deliver this package?"
  creates_goal:
    id: deliver-package
    complete_when: "player gives package to mayor"
```

Full documentation: [SKILL.md](SKILL.md). Routing: [ROUTING.md](ROUTING.md).
