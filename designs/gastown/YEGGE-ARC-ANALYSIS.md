# Steve Yegge, then and now

## The posts I learned from

Steve Yegge's blog rants from the mid-2000s on are some of the best writing about programming
culture there is. "Execution in the Kingdom of Nouns" (2006) explained to a generation of Java
programmers what they were missing, with a fairy tale. "Lisp is Not an Acceptable Lisp" (2006)
took the Lisp tradition seriously enough to criticize it. "Code's Worst Enemy" (2007) argued
that size is the worst thing that can happen to a code base. The Google Platforms Rant (2011),
an internal memo posted publicly by accident, changed how people talk about APIs and dogfooding.

That writing shares the habits MOOLLM depends on: name things precisely, care what the reader
already knows, read the code, and say plainly when something is bad.

## Wyvern, and the Universal Design Pattern

Yegge started Wyvern in 1996, a graphical multiplayer RPG with a Java client, and launched it
in 2001. Its structure is LambdaMOO's: players who earned it became **wizards** who built areas
tile by tile and scripted quests, guilds and spells, and they own what they built. The servers
went down in 2011. In 2013 he wrote that lawyers had told him he didn't own Wyvern and would have
to make a new game. It came back anyway, on mobile in 2016 and on Steam in 2021. He stopped
development in 2022, and since mid-2026 it's his full-time work again, built by his agents.

In ["The Universal Design Pattern"](http://steve-yegge.blogspot.com/2008/10/universal-design-pattern.html)
(2008) he explained Wyvern's object model. Every game object has a property list and an optional
parent link. Reads fall through to the parent, writes and deletes stay local, and any object can
be the parent of any other. He called parents "archetypes" because "I designed Wyvern long before
I'd heard of Self or Lua, and before I'd learned anything about JavaScript." Property metadata
does access control: some properties can be read only by high-level wizards. His argument is that
this is "by far the best known solution to the problem of designing open-ended systems", and that
prototype languages make better extension languages than class-based ones.

That's the MOO object model, rediscovered independently: LambdaMOO had parented objects,
inherited properties and wizard bits by 1990, and Self had prototypes before that. MOOLLM
inherits the same model on purpose ([prototype](../../skills/prototype/SKILL.md),
[SELF-AND-MOOLLM](../object-system/SELF-AND-MOOLLM.md)), with one difference. Wyvern's archetypes
have one parent; MOOLLM's `parents:` is an ordered list, as in Self, and it can also name
parents that live in the model's training rather than in a file
([LATENT-SPACE-INHERITANCE](../object-system/LATENT-SPACE-INHERITANCE.md)).

Whether Wyvern's code still works this way after its post-2012 rewrite, I don't know.

## Gas Town

In January 2026, after leaving Sourcegraph, he published "Welcome to Gas Town": an orchestrator
for twenty to thirty coding agents, built in seventeen days, with a vocabulary of polecats,
convoys, molecules and wisps, an eight-stage ladder of who is allowed to use it, and this:

> "It's also 100% vibe coded. I've never seen the code, and I never care to... Course, I've
> never looked at Beads either, and it's 225k lines of Go code that tens of thousands of people
> are using every day."

The author of "Code's Worst Enemy" shipping a quarter-million unread lines as an issue tracker
is the part I can't get past. The design arguments are in
[GASTOWN-VS-MOOLLM-ANALYSIS.md](GASTOWN-VS-MOOLLM-ANALYSIS.md).

## $GAS

From Sean Goedecke's and Solana Floor's accounts:

1. A trader created a $GAS coin on the Bags platform and configured its trading fees to go to
   Yegge's Twitter account. He didn't create it and wasn't asked.
2. Someone contacted him about his "earnings". Goedecke reported them as $238,000 on 17 January;
   Solana Floor reported over $300,000.
3. Yegge claimed the fees and posted in support, describing Bags as "an innovation engine,
   similar in some ways to the stock market," for predicting and fostering creators.
4. $GAS peaked above a $60 million market cap.
5. On 17 January he said he'd spend less time on Crypto Twitter. Two days later he published a
   disclosure: he didn't create the token, didn't control it, and it conveyed no ownership of
   Gas Town or his work. $GAS fell about 97% from its peak in three days.

Solana Floor's view is that this wasn't a coordinated rug pull, and I agree. Goedecke's view is
that Bags is pump-and-dump as a service aimed at respected open-source developers, whose
reputation is what's being sold, and I agree with that too. Buying $GAS gave nobody anything in
Gas Town. Some of the people who bought it were his readers.

That's sad. It also isn't the argument against Gas Town's design, which stands or falls on its
own.

## Sources

- Steve Yegge, [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) (1 Jan 2026)
- Steve Yegge, [blog archive](https://steve-yegge.blogspot.com/) (2006–2011 rants)
- Sean Goedecke, [Crypto grifters are recruiting open-source AI developers](https://www.seangoedecke.com/gas-and-ralph/) (17 Jan 2026)
- Solana Floor, [Solana AI Meta Collapses](https://solanafloor.com/news/solana-ai-meta-collapses)
- [HN discussion of Welcome to Gas Town](https://news.ycombinator.com/item?id=46458936)
