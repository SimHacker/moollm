# Gas Town, as a foil

> *"It's also 100% vibe coded. I've never seen the code, and I never care to."*
> — Steve Yegge, [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04), January 2026

I've read Steve Yegge for twenty years. "Execution in the Kingdom of Nouns", "Lisp is Not an
Acceptable Lisp", the Google Platforms Rant, "Code's Worst Enemy": those posts taught a lot of
us to think about language and platform design out loud, with jokes, in public. I still send
people to them.

Gas Town is silly, and the crypto episode around it is sad. It also got a lot of attention it
didn't earn, which makes it useful to me: it's a well-known system that made the opposite
choice at almost every fork where MOOLLM had to choose. Explaining why MOOLLM is built the way
it is goes faster with a concrete opposite to point at.

## Files

| File | What it is |
|---|---|
| [GASTOWN-VS-MOOLLM-ANALYSIS.md](GASTOWN-VS-MOOLLM-ANALYSIS.md) | The comparison. Philosophy first, then what Gas Town gets right, what its code shows, and where MOOLLM is weaker. |
| [BEFORE-AND-AFTER-2026-10.md](BEFORE-AND-AFTER-2026-10.md) | Gas Town from January to October 2026: growth, the freeze, Gas City, Wheelhouse, overfencing, fuel. |
| [YEGGE-ARC-ANALYSIS.md](YEGGE-ARC-ANALYSIS.md) | The Steve I learned from, the Gas Town posts, and the $GAS token, with sources. |
| [CONSTRUCTIONIST-TERMINOLOGY.md](CONSTRUCTIONIST-TERMINOLOGY.md) | The vocabulary decision: task, workflow, action, goal, owner, and why not bead, molecule, hook, polecat. |
| [TASK-ORCHESTRATION.yml](TASK-ORCHESTRATION.yml) | How tasks move between MOOLLM's existing skills: queues, stacks, mail, pipelines, board views. |
| [TASKS-2026-01.md](TASKS-2026-01.md) | The January 2026 MOOLLM backlog, kept as a record. An example of the markdown-ledger form of the task skill. |

What came out of this directory as working code:

- [skills/task/](../../skills/task/) — durable work items with guards. Events stored, state computed.
- [skills/workflow/](../../skills/workflow/) — reusable procedures that spawn tasks.

Both READMEs say what they took from Beads and Gas Town and where they part ways.

Related elsewhere: [SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md](../SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md)
(one context simulating many agents, versus many processes passing messages) and
[HUMANSPLAINING.md](../object-system/HUMANSPLAINING.md) (why invented vocabulary costs tokens on
every call).

## Two words

**Gastowning** (v.): gaslighting the model and the humans at once, in the style of Gas Town:
telling both that invented cosplay vocabulary is knowledge and that never reading the generated
code is engineering.

**Tokenmaxing** (v.): burning tokens because the burn is the signal. Rolling coal in a
datacenter. A thirty-agent tmux swarm is Veblen's gold-plated faucet: it doesn't move more
water, it shows what the owner can afford to waste.

I coined both in an HN comment on 2 Aug 2026, archived verbatim in
[2026-08-02-hn-humansplaining-gastowning.yml](../../skills/no-ai-humansplaining/examples/2026-08-02-hn-humansplaining-gastowning.yml).
That looks like breaking MOOLLM's own rule against inventing jargon, so here's the test a new
word has to pass: does it decompress on sight with no explanation? Both parents of "gastowning"
are already in the training data (gaslighting, Gas Town), and so are the parts of
"tokenmaxing" (the -maxing suffix, Veblen, rolling coal). "Bead", "polecat", "GUPP" and "MEOW"
point at nothing the model already knows, so they need explaining in every prompt, every time.

## Sources

- Steve Yegge, [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) (Medium, 1 Jan 2026); [HN discussion](https://news.ycombinator.com/item?id=46458936)
- Maggie Appleton, [Gas Town's Agent Patterns, Design Bottlenecks, and Vibecoding at Scale](https://maggieappleton.com/gastown); [HN discussion](https://news.ycombinator.com/item?id=46734302), where I posted an early, friendlier version of this comparison
- Sean Goedecke, [Crypto grifters are recruiting open-source AI developers](https://www.seangoedecke.com/gas-and-ralph/) (17 Jan 2026)
- Solana Floor, [Solana AI Meta Collapses](https://solanafloor.com/news/solana-ai-meta-collapses)
- Source code: [steveyegge/gastown](https://github.com/steveyegge/gastown), read at `d4126bb8` (24 Jan 2026) and `649b832b` (23 Jul 2026)
