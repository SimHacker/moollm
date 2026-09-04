# Culture ship names are oddly specific K-lines into latent space

*Don's observation, and the operative word is **oddly specific**. That is not a description of the
joke. It is a claim about altitude, and it happens to be the exact thing Minsky's memo says is hard.*

Related: [`GLANCE.yml`](GLANCE.yml) · [`SKILL.md`](SKILL.md) ·
[`../no-ai-humansplaining/`](../no-ai-humansplaining/) · [`../yaml-jazz/`](../yaml-jazz/) ·
[`../../designs/P-PYRAMID.md`](../../designs/P-PYRAMID.md)

## The claim

"Falling Outside The Normal Moral Constraints" is a working character sheet in six words. It gives
you the ship's ethics, its awareness of its own ethics, its register (the phrasing is a
*classification*, as if lifted from a manual), and the strong implication that it is a warship
filed under paperwork. Nothing was described. A name was said, and a stance arrived.

That is a K-line in Minsky's sense — a symbol whose activation reinduces a whole configuration
rather than retrieving a fact ([AI Memo 516](sources/aim-516-k-lines-1979-ocr.txt), 1979).

## Why "oddly specific" is the load-bearing phrase

The memo's hardest practical result is the **level-band principle**, already quoted in
[`GLANCE.yml`](GLANCE.yml): *attach the middle — too low imposes stale detail, too high hallucinates
the problem as solved.* Getting a K-line to work is mostly a question of picking the altitude.

Ship names are a demonstration that the band is real and narrow:

| Altitude | Example | What you get |
|---|---|---|
| Too high | `Warship`, `Vengeance`, `Enterprise` | Genre, and nothing to act on. Activates a category, not a stance |
| **The band** | `Falling Outside The Normal Moral Constraints` | A stance. Specific enough to constrain behavior, abstract enough to generate it |
| Too low | A spec sheet: tonnage, armament, engine class | Stale detail that forecloses improvisation. Nothing left to infer |

"Oddly specific" is what the middle band *feels like from outside*. The oddity is not eccentricity
for its own sake — it is the surprise of a name that is precise about the wrong axis. It tells you
about *disposition* where you expected *function*, which is why one phrase does the work of a
paragraph. Banks found the correct altitude by novelist's instinct and then hit it several hundred
times.

## The specificity is a *scene*, not a mood

The strongest names do not name a quality. They name a **situation with a participant in it**, which
is why a stance comes back rather than an adjective.

- **`Killing Time`** (ROU, Torturer class) is a pun where both readings are true: the saying is
  that 99% of war is killing time and the rest is *the killing time*. One name, two activations,
  and the ship is genuinely both.
- **`Frank Exchange Of Views`** (Psychopath class, nominally demilitarised, actually a fully armed
  warship) is diplomatic language for a blazing argument. The name is a euphemism worn openly.
- **`Grey Area`** names its own moral position, and "grey matter," and the fact that it reads minds.

Compare [`../no-ai-gloss/`](../no-ai-gloss/): EUPHEMISM-LAUNDERING is a sin when it hides the act.
Here the euphemism is *transparent* — everybody knows what a frank exchange of views is — so it
reads as wit rather than evasion. The distinction is whether the audience is in on it.

## They are pre-loaded, which is the whole economy

These names are in the training data along with the novels. Saying one activates the Culture corpus
*and* the specific personality *and* the tonal register, at the cost of six words.

That is [`no-ai-humansplaining`](../no-ai-humansplaining/)'s test passing at full marks: **is the
pointee in latent space? Then point — the name is the activation.** Ship names are the cleanest
available demonstration, because the compression ratio is absurd and the pointee is a whole
character.

The anti-pattern is in the same skill's sin list, and the contrast needs no commentary:

```
agent_7f3a9c                                    # GUID-NAMING. Zero activation.
Falling Outside The Normal Moral Constraints     # A colleague you already have opinions about.
```

## The architecture underneath: six naming layers, and Banks kept them separate

The part that is directly useful, and the part a reader who only knows the joke names will miss:
**the funny name is one layer of six**, and the other five carry the type system.

| Layer | Example | Job |
|---|---|---|
| Type | `GCU`, `ROU`, `GOU`, `GSV`, `LOU` | What it *is*. Terse, enumerable, sortable |
| Class | `Abominator`, `Psychopath`, `Torturer`, `Escarpment`, `Ridge` | Which family, by semantic domain |
| Name | `Falling Outside The Normal Moral Constraints` | Who it is. Self-chosen |
| Alias | `Meatfucker` | What others call it. Socially imposed, contested |
| Status | `(Eccentric)`, `(Ulterior)` | Behavioral standing, orthogonal to type |
| Role suffix | `Bodhisattva, OAQS` | Current assignment — *On Active Quietudinal Service* |

Three of these are worth stealing outright.

**Class names encode the type family by semantic domain.** Warship classes are crimes and criminals
— Abominator, Psychopath, Torturer, Killer, Gangster, Thug. Contact-unit classes are landforms —
Mountain, Escarpment, Ridge, Highpoint. You can tell a warship from a scout by *whether its class is
a crime or a hill*, without a lookup table. That is a naming convention doing a type system's job,
which is precisely the claim [`yaml-jazz`](../yaml-jazz/) makes for plural directories and
big-endian names.

**The role suffix is mutable state living in the identity.** `OAQS` is appended while the ship is so
employed, and presumably dropped after. A name that carries current status is the same move as
[view state in the document](../../designs/webtop/VIEW-STATE-AS-COMMENTARY.md) — Winer's
`expansionState` argument, arrived at from fiction.

**The type prefix is not optional and not decorative.** This is the design constraint hiding in the
joke: Banks needed the terse enumerable prefix *because* the names are long and funny. `GCU` sorts,
scans, and groups. "Falling Outside The Normal Moral Constraints" does none of those things.
**The name is for activation; the prefix is for navigation.** Collapse them and you lose one.

## `Grey Area` is the synonym-collision case study, with politics

The best receipt in the whole set, and it is a warning rather than a model.

Grey Area was ostracised for non-consensual mind-reading of biological individuals. The other Minds
condemned it and **ignored its chosen name in favour of `Meatfucker`.** So:

- **A name can be refused.** Self-naming is a claim, not a fact; the register is social. Compare
  HyperTIES synonyms, where a name is claimed by an author and resolved by an index — here the
  index is *other agents*, and they voted.
- **The imposed alias won.** It is what the ship is known as, including in the wiki's own headings.
- **And then the alias went generic.** By *Surface Detail*, long after Grey Area is gone, a drone
  hurls "Meatfucker!" at Falling Outside The Normal Moral Constraints as a plain insult. The
  synonym **outlived its referent and decayed into a category**.

That last step is the exact failure mode flagged for generated aliases: drift toward the generic,
where "the thing where you do the work" collides with everything. Here it happened to a name that
started maximally specific and personal. **Specificity is not permanent.** A distinctness lint has
to run over time, not once at authoring — see
[`../../designs/webtop/hyperties/LINK-RESOLUTION.md`](../../designs/webtop/hyperties/LINK-RESOLUTION.md).

## Two more mechanisms worth naming

**Deferred activation.** `Sleeper Service` is a sleeper agent whose cover is a suspended-animation
"sleeper service," and the name does not fully resolve until the end of the book. The K-line
*strengthens* retroactively: reading the ending rewrites what the name meant on page one. A pointer
whose target sharpens as the corpus is read is a property worth wanting.

**Renaming as a recorded change of stance.** `No One Knows What The Dead Think` was previously
`Obliterating Angel`. The rename is the character development, and both names are on the record.
That is a git history of identity, and it argues for keeping old names as resolvable aliases rather
than rewriting them away.

## Honest costs

**Cuteness does not scale, and this is the main one.** Banks could afford hundreds of whimsical
names because a reader meets maybe a dozen per novel, spaced across hundreds of pages. Several
hundred whimsical names in one directory is unnavigable and insufferable — the very specificity that
makes *one* name a K-line makes *a thousand* names noise, because nothing sorts and every entry
demands to be read. The type prefix is the mitigation, and it is not a full one.

**A K-line into fiction activates the fiction's assumptions too.** Naming a MOOLLM agent after a
Culture Mind imports benevolent post-scarcity godlike competence along with the personality, which
is flattery the artifact has to live up to. The Culture's Minds are *right* almost all the time.

**Self-chosen names are unfalsifiable claims.** `Honest Mistake` is a name, not a track record, and
Grey Area shows that the fix is social rather than syntactic. Any self-naming scheme needs a place
for what *others* call the thing.

**And this is a literary observation, not a measurement.** The claim that these names sit in the
level band is an argument from how they read, not from an experiment. It would be testable —
generate behavior from a name alone and score whether independent readers recover the same stance —
and nobody here has run it.

## Related

- [`GLANCE.yml`](GLANCE.yml) — `wikipedia_urls_are_k_lines`, the sibling case
- [`../no-ai-humansplaining/`](../no-ai-humansplaining/) — point at latent space; GUID-NAMING
- [`../yaml-jazz/`](../yaml-jazz/) — filenames as K-lines, big-endian naming, directories as advertisements
- [`../../designs/P-PYRAMID.md`](../../designs/P-PYRAMID.md) — the level-band principle
- Source for names, classes and status markers: [The Culture Wiki, List of spacecraft](https://theculture.fandom.com/wiki/List_of_spacecraft)

↑ [k-lines](README.md)
