# Case study: mystery as dispatch, and then all of it

*A [Korz](README.md) case study, alongside [case-zork.md](case-zork.md) (Zork as shipped
five-dimensional dispatch) and [case-cellular-automata.md](case-cellular-automata.md)
(Korz at absolute zero). This one runs the other direction: not a program read as
narrative, but **narrative read as a dispatch configuration** — and the claim is that the
genre names critics have used for a century are descriptions of which coordinate is
unbound.*

## The observation that starts it

> Howcatchem crystallizes who. Whodunit computes who. — Don, Sept 2026

Which is Korz′'s two tiers, named by detective fiction first. In Korz′ a slot is either
**crystallized** — decidable, matched by the strict tier — or it **deoptimizes** to the
soft tier, which improvises an answer the compiled guards could not supply
([korz-prime/README.md](korz-prime/README.md)).

An inverted detective story (Columbo, *Crime and Punishment*, most heists) hands you the
culprit in the first act: `rcvr` arrives **bound**, a constant, and the drama is entirely
in the mechanism. A classical whodunit leaves the same coordinate **unbound** and the whole
form is the computation of it. Same sea of slots. Different guard configuration.

So a genre is not a plot shape. **A genre is a dispatch configuration**: which coordinates
arrive bound, which one you are solving for, and who holds which bindings.

## The mystery table

| Genre | Solving for | Dimension | Specimens |
|---|---|---|---|
| **Whodunit** | the agent | `rcvr` unbound, computed | Christie, the drawing-room form |
| **Howcatchem** | the mechanism of catching | `rcvr` crystallized; `method` computed | Columbo, *Poker Face* |
| **Howdunit** | the mechanism of doing | `method` foregrounded, all else given | heist films, *Rififi*, Ocean's Eleven |
| **Whydunit** | the motive | **`purpose`** unbound | Highsmith, *Crime and Punishment*, most literary crime |
| **Wherecatchem** | the coupling, the place | `place` | *Pokémon Go*, geocaching, the hunt genre |
| **Whendunit** | the alibi, the timetable | `time` | Crofts' railway timetables, *Memento*, time-loop films |
| **Whatdunit** | whether there was an act, and of what kind | the *class* is unbound | Kafka, *The Crying of Lot 49*, cosmic horror |

Three entries earn their place by being more than labels.

**The whydunit is the detective genre of the `purpose` dimension.** It is the form in which
every coordinate is bound except why, and readers experience an unbound `purpose` as the
most unbearable of the gaps — more than who, more than how. Which is a point in favor of
the dimension existing
([korz-prime/examples/purpose-dimension.md](korz-prime/examples/purpose-dimension.md)).

**Whatdunit is the horror case, and it is a guard failure rather than a search.** Cosmic
horror is the genre where the unbound dimension *cannot be bound by the reader's
vocabulary* — no coordinate in the reader's sea fits, so no slot matches, and the dread is
the dispatch failure itself. Lovecraft's adjectives are the transcript of a lookup
returning nothing: unnameable, indescribable, non-Euclidean. He is not being lazy. He is
reporting a miss.

**And a locked room is a type error.** The constraints over-determine and nothing matches.
The solution is *always* the discovery of a dimension nobody knew was in the sea — a
passage, a twin, a clock that was wrong, a room that was not locked at the time you assumed.
Korz's answer to "nothing matched" is that your guards were written over the wrong axes,
which is the locked-room solution stated as a compiler diagnostic. The genre's fair-play
rule is even the Korz discipline: the author must have put the dimension in the sea before
the reveal.

## Point of view is subjective dispatch

Korz's own gloss: gather the sea's slots along `rcvr` and you see objects; gather along
`user` and you see **one person's view of the system**. That is not an analogy for
narrative point of view. It is the same mechanism.

- **Dramatic irony** is differential binding. In Columbo the audience's context has the
  culprit bound and the detective's does not. Same slots, different guards match, and the
  tension is exactly the delta between two gathers.
- **The unreliable narrator** is a transcript that disagrees with the bindings — the
  *hidden dither* quadrant from [moody-temperature.md](korz-prime/examples/moody-temperature.md),
  where the printed context claims `temperature: 0` and the dice are rolling. Same failure
  mode, same diagnosis, and mystery fiction has been exploiting it since 1926.
- ***Rashomon*** is the canonical Korz film: gather four times along `witness`, refuse to
  privilege a cut, and let the absence of a dominant decomposition be the content.
- **Oedipus is an aliasing bug.** `detective` and `culprit` turn out to be the same
  coordinate, and the tragedy is the discovery of the alias rather than the identity. Every
  reveal of the form "you were the monster" is this one bug.

## Widening: the same move outside the mystery

If a genre is which coordinate is unbound and who holds the bindings, the frame does not
stop at crime.

| Form | Configuration |
|---|---|
| **Tragedy** | The audience's context carries a binding the protagonist's lacks — prophecy, the letter that went astray. Fate *is* an ambient coordinate everyone but him can read |
| **Farce** | Two contexts with *conflicting* bindings on one sea. Mistaken identity is a wrong `rcvr` that keeps dispatching plausibly, which is why the mechanism must be watertight to be funny |
| **Romance** | The unknown is `purpose`, held by the other party. A whydunit of the heart, and the reason the genre survives a thousand identical plots is that the coordinate is genuinely unreadable from outside |
| **Bildungsroman** | The protagonist's *own* `purpose` starts unbound and ends bound. Coming of age is binding your own setpoint — which is closure, and is why the form feels like becoming a person rather than learning a fact |
| **Satire** | The acts dispatch under a purpose the reader holds and the characters do not. Remove the reader's binding and satire reads as endorsement, which is the entire history of misread satire |
| **Lyric poetry** | No unknown at all. Maximum meaning gain, zero mystery — the moody keyboard rather than the detective |
| **Ambient and generative art** | The work is a **context author**: it writes bindings the audience's other dispatches then read. MOODY, exactly |

## The two claims worth arguing about

### Cubism is symmetric dispatch

Renaissance perspective is **single-receiver dispatch**: one privileged station point, the
picture composed *to* a particular eye, every other viewpoint wrong. Cubism gathers the
same object along several viewer coordinates at once and declines to make one dominant —
which is Korz's central claim, that no decomposition is the dominant one, rendered in paint
twenty years before Korzybski named the error and eighty before Ungar formalized it.

Which makes the usual complaint about Cubism ("it doesn't look like anything") the exact
complaint a Smalltalk programmer makes about a slot sea: *where is the object?* Gathered,
if you ask along an axis. Not before.

### Melodrama is the is-of-identity; tragedy is E-Prime

Korz is E-Prime for objects — the rose is not red, redness lives in the dispatch
([README.md](README.md)).

**Melodrama binds the moral coordinate into the object.** The villain *is* evil, the way
the rose *is* red. **Tragedy leaves it relational**: the act dispatches monstrous from this
position, in this context, and would not from another. Antigone and Creon are both right
along their own axes, and the form is the collision rather than the verdict.

Which predicts something checkable: melodrama ages into camp and tragedy does not. The
Korzybski violation is the part that spoils, because a property welded into an object stops
matching any context the author did not live in, while a relation recomputes against
whatever context arrives. Same reason a hardcoded constant rots and a guard survives.

## Why this is not a party trick

Two payoffs, one for each direction of the analogy.

**For Korz:** narrative forms are a several-thousand-year empirical search over dispatch
configurations, run by people optimizing for whether an audience can *follow* it. Which
configurations are legible, which are unbearable, which need the binding withheld and which
need it given away in act one — that is data about dimension design, from the only
discipline that has been testing it at scale. The whydunit being the most gripping
configuration is evidence about `purpose`. The locked room always resolving to an unknown
axis is evidence about guard completeness.

**For the reader of this repo:** it is the same claim the rest of the design makes in a
register that is harder to fake. Dimensions are not a programming convenience. They are how
attention gets organized, which is why the publishing ladder, the torch overlay, the
advertisement economy and the mystery genre keep turning out to be one mechanism — and why
literature is the oldest prosthetic for holding a context whose bindings are not yours.

## Open questions

- Is there a genre for `device` — a form whose unbound coordinate is *the medium*? Concrete
  poetry and demoscene work feel like candidates, where the constraint is the content.
- The `assertions` dimension has no obvious narrative analogue, which is either a gap in
  the mapping or a hint that debug modes are peculiar to machines.
- If binding your own `purpose` coordinate is closure, and the Bildungsroman is the
  literary form of that event, is the reason no machine has the form yet the same reason it
  has no closure?

**See also:** [case-zork.md](case-zork.md) — the same repo reading a game engine as five
hardwired dimensions · [korz-prime/examples/purpose-dimension.md](korz-prime/examples/purpose-dimension.md)
— the dimension the whydunit is about ·
[../TELEOLOGY.md](../TELEOLOGY.md) — whodunit / howcatchem / wherecatchem as three genres
of question about minds, which is where this frame came from
