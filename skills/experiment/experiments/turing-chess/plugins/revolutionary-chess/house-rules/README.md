# House Rules — surrender policy as dealer's choice

Surrender is not one rule; it's a **parameter axis**. Like poker house rules,
each variant below is an optional **mixin on the ruleset** — a small patch to
`surrender_policy` — composable the way colors are mixins on pieces. Dealer
announces the house rules before the first pawn moves; the mixin files are
the announcement, machine-readable.

The base invariant (unless a mixin overrides it): inheritance flows
**bottom-up, to commoners only** (INDEX.yml `inheritance-rule`). House rules
change *who may join* the commoners, *when*, and *at what price*.

| Mixin | One line | Predicted politics |
|-------|----------|--------------------|
| [`NO-QUARTER.yml`](NO-QUARTER.yml) | Nobody may surrender | War of extermination; cornered aristocrats; longest game |
| [`VICTORS-EXIT.yml`](VICTORS-EXIT.yml) | Only the winning side may surrender | Nomenklatura → oligarchs; treachery rewarded in victory |
| [`VANQUISHED-MERCY.yml`](VANQUISHED-MERCY.yml) | Only the defeated side may surrender | Reconciliation commons vs rigid ancien régime; sandbagging metagame |
| [`GOLDEN-BRIDGE.yml`](GOLDEN-BRIDGE.yml) | Surrender window closes at first execution of your type | Sun Tzu's bridge; sharpened cascade |
| [`AMNESTY-VOTE.yml`](AMNESTY-VOTE.yml) | The commons votes on each surrender | Karma becomes currency; no self-laundering |
| [`EXILE.yml`](EXILE.yml) | Surrender = leave the board, organelle emigrates | Brain drain; the commons prefers execution to exile |

## A second axis: capture policy

Surrender mixins govern *joining* the commons. The deep version adds a
second axis — what capture *means* for an aristocrat:

| Mixin | One line | Predicted politics |
|-------|----------|--------------------|
| [`TRIBUNAL.yml`](TRIBUNAL.yml) | Capture is an arrest; the whole board (both colors, surrendered aristocrats included) votes live-or-die | Cross-color reputation; swing-bloc loyalty theater; square testimony decides close cases |
| [`THE-HAGUE.yml`](THE-HAGUE.yml) | Stacks on TRIBUNAL: full trial mini-game — the board judges, a cross-color jury decides, advocates argue, and the accused's every interaction is replayed from the deep memory logs | Advocacy careers; every move made knowing it may be exhibit A; restorative sentences; stare decisis by season three |
| [`SHOGI-DROPS.yml`](SHOGI-DROPS.yml) | Capture sends every piece to the captor's bench; drop it back on any vacant square as one of yours — allegiance is orientation, five centuries of shogi prior art | Material circulates instead of attriting; the bench is a hand of cards; capture by the revolutionary side is a promotion in disguise |

TRIBUNAL leans on [`DEEP-MEMORY.yml`](../DEEP-MEMORY.yml): pieces keep
append-only memory logs of every step, squares keep ledgers of everything
that occurred on them, and ballots are informed by memory and personality
([`PIECE-CONSCIOUSNESS.yml`](../PIECE-CONSCIOUSNESS.yml)) rather than a
cached karma integer. Without deep memory it degrades gracefully to
karma-weighted ballots ([`TREATMENT-KARMA.yml`](../TREATMENT-KARMA.yml)).

These are hypotheses in the [DYNAMICS.md](../DYNAMICS.md) sense — run them
and see. Combinations are legal where they don't contradict (GOLDEN-BRIDGE +
AMNESTY-VOTE: a closing window *and* a vote; VANQUISHED-MERCY + EXILE: the
defeated may leave but take their moves with them; TRIBUNAL + anything,
since it patches a different axis).
