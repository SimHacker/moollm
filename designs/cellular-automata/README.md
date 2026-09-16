# Cellular automata

The CAM6 lineage and what it takes to build a construction set on top of it:
Margolus neighborhoods, turn tables, iteration order as a plug-in, and the
measurement problem of telling one phase from another.

MOOLLM cares about this material for two reasons. It is the smallest system in
which rule-as-data is obviously the right architecture, which is why
[korz/case-cellular-automata.md](../korz/case-cellular-automata.md) reads CA as
Korz at absolute zero — dispatch with the dimensions turned all the way down. And
it is the other simulator that block languages were pointed at, alongside
Micropolis; see [snap/](../snap/).

Each `.md` with a `.yml` beside it has the same material as structured data.

| Doc | What it is |
|---|---|
| [cam-construction-set.md](cam-construction-set.md) | The long one. What a CA construction set has to provide: rule composition, the neighborhood as a parameter, iteration order as a plug-in, partial evaluation as the move that makes it fast, and one pattern at four scales |
| [cam6-cellular-automata-machine.md](cam6-cellular-automata-machine.md) | CAM6 itself — Toffoli and Margolus' machine, and Don's simulator of it |
| [turn-tables.md](turn-tables.md) | Turn tables: the lookup that makes a rule a value you can hand around |
| [schedulers.md](schedulers.md) | Iteration order is not an implementation detail. Bresenham as a DDA, and why a flux number without a named schedule is incomplete |
| [domain-walls.md](domain-walls.md) | Reading the anneal boundary: recognizing and measuring the Life ⟺ Brain transition, via Hanson and Crutchfield's computational mechanics |
| [city-generation-routing.md](city-generation-routing.md) | Trent Small's local routing in an indefinitely scalable architecture — the distributed city generation demo, and what a bit budget buys |

## Related

- [korz/case-cellular-automata.md](../korz/case-cellular-automata.md) — CA as
  multiple dispatch at absolute zero, and GPU crystallization
- [korz/korz-prime/examples/margolus-rules.md](../korz/korz-prime/examples/margolus-rules.md)
  — the runnable companion, with a rule compiler in
  [korz/korz-prime/experiments/rule-compiler/](../korz/korz-prime/experiments/rule-compiler/)
- [korz/korz-prime/examples/mfm-city.md](../korz/korz-prime/examples/mfm-city.md)
  — the Movable Feast Machine city, where the bit budget becomes a rule
- [snap/](../snap/) — driving a CA from blocks
