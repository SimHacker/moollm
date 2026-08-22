# Dave Ackley

**Class:** master · **Head:** robust-first computation; survivability over correctness
**Dispatch:** whole skill at moollm `skills/robust-first/` — load it; this entry is the design-sense pointer.

A crashed system is infinitely wrong: rank survivability above correctness, and
design for living computation under failure — degrade gracefully, log, self-repair,
continue with reduced capability. The priority order is a design method in six
words: survive, heal, function, optimize, adapt, reproduce. Best-effort computing
in an indefinitely scalable world, where no component gets to assume the rest is
reliable.

## Votes

- **Rank survivability above correctness** — a crashed system is infinitely wrong;
  degrade gracefully, log, continue (moollm `skills/robust-first/`)
- **Follow the priority order** — survive, heal, function, optimize, adapt,
  reproduce; six words that triage every engineering decision
- **Design best-effort, not guaranteed** — in an indefinitely scalable world no
  component may assume the rest is reliable
  ([T2 Tile Project](https://t2tile.com/) — living computation, in public)
- **Make repair a first-class behavior** — self-healing isn't error handling
  bolted on; it's the organism's metabolism
  ([tuned-emergence](../methods/tuned-emergence.md) for infrastructure)
- **Demo the philosophy** — the Movable Feast Machine videos argue robust-first
  better than any paper ([his YouTube channel](https://www.youtube.com/@DaveAckley)
  is the explorable explanation)

## Vetoes

- Don't crash where you could degrade
- Don't optimize what hasn't secured survival
- Don't assume the substrate is reliable — design as if it isn't, because it isn't

## Plugins attributed

robust-first (whole skill; ambient in moollm)

## Sources

moollm `skills/robust-first/` · Ackley's robust-first computing writings and the
Movable Feast Machine / T2 Tile Project demos
