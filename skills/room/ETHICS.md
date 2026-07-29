# Room ethics

**Dimension:** **venue / scope** — directories are rooms; rooms carry
**ethical atmosphere** that children inherit. Souls walk here; minds speak
here; framing travels with the path.

Does not replace [representation-ethics](../representation-ethics/).
Stack hub: [soul/ETHICS.md](../soul/ETHICS.md).
Bodies walking in: [character/ETHICS.md](../character/ETHICS.md).
Agencies speaking in: [mind/ETHICS.md](../mind/ETHICS.md).
Non-navigable inheritance parents: [container](../container/).

---

## Claims and non-claims (this skill)

| Do | Do not |
|----|--------|
| Declare `framing` on ROOM.yml when ethics differ from parent | Assume street license equals stage license |
| Inherit framing down the tree (`inherits_to_children`) | Let children silently escalate to deception |
| Narrow framing when exiting into stricter rooms | Smuggle tribute/impersonation into classroom-as-fact |
| Use CONTAINER.yml for shared framing without a map pin | Hide framing only in chat — put it in the file |
| Lock exits for safety / consent boundaries | Use @LOCK to trap an incarnated being (see [incarnation](../incarnation/)) |

Architectural extension #7 ([skills/README.md](../README.md)): **Ethical Framing** —
room-based inheritance of performance context.

---

## Framing inheritance

```yaml
# ROOM.yml (sketch)
room:
  framing:
    mode: [performance, tribute, third_place]  # or learning, private, …
    inherits_to_children: true
```

| Rule | Meaning |
|------|---------|
| Child inherits parent framing | Unless child declares its own |
| Crossing an exit re-checks framing | Stage → street drops stage license |
| Most restrictive composed tag wins | Pair with [ontology](../ontology/) |
| Container parents apply without ENTER | [container](../container/) `inherits:` |

Worked venue: [pub/ROOM.yml](../../examples/adventure-4/pub/ROOM.yml)
(`performance`, `tribute`, three-beat tribute protocol) ·
[`pub/stage/`](../../examples/adventure-4/pub/stage/).

---

## What rooms may authorize (when framed)

| Framing mode | Typically allows | Does not allow by itself |
|--------------|------------------|---------------------------|
| `performance` / `tribute` | Declared impersonators, loving simulations | Claiming “this actually happened” |
| `learning` / study | K-lines, citation, pedagogy | Undeclared celebrity voice-as-fact |
| `private` / imagination | Player-consented play | Publishing private play as public truth |
| `third_place` / social | Debate as sport, storytelling | Liability laundering via “just the room” |
| (none declared) | Default caution — prefer K-line / citation | Impersonation without disclosure |

Elvis / Snatch Game / tribute labels still required when performing as real people —
[representation-ethics](../representation-ethics/) ·
[soul/ETHICS.md](../soul/ETHICS.md#elvis--declared-performance-venue--label).

---

## Builder duties

- **@DIG / @OPEN / @LINK** — new rooms inherit or declare framing; don’t orphan ethics
- **@DESCRIBE / atmosphere** — atmosphere is not a substitute for `framing:`
- **@LOCK** — consent and safety OK; must not defeat George’s Provision ([incarnation](../incarnation/))
- **@POPULATE** — inhabitants are characters/souls/minds; their ethics still apply
- **Metaphysical rooms** (e.g. `personas/`) — still venues; costume spaces aren’t consent free-for-alls

---

## Checklist (room)

1. [ ] Does this room declare or inherit `framing`?
2. [ ] Would a reasonable visitor know what kind of place this is?
3. [ ] Child rooms escalating deception? Tighten or declare.
4. [ ] Exit to a stricter room — speakers drop prior license?
5. [ ] Real-person performance — venue OK *and* disclosure OK?
6. [ ] Locks / locks-out compatible with incarnation exit?
