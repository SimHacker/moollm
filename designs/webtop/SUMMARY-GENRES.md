# Summary genres — the pyramid's second axis

*Don Hopkins · September 2026*

**Thesis:** The semantic pyramid has been described with one axis, resolution — glyph, title,
abstract, body. It needs a second: **genre**. The same document at the same resolution can be
summarized straight, or as a sardonic bingo card, or as a changelog, or as a eulogy. These are not
decorations on the abstract; they are different summaries with different truth conditions, and one
of them turns out to be a *better* benchmark than the glyph.

Companion to [GLYPH-BENCHMARK.md](GLYPH-BENCHMARK.md), which is the resolution axis pushed to its
top rung. This is the orthogonal move.

---

## The terms of art

For the thing a bingo square contains — one to three words, specific enough to be recognizable,
general enough to recur:

| Term | Field | What it precisely means |
|---|---|---|
| **topos** (pl. *topoi*) | classical rhetoric | A stock argumentative move. Aristotle's *Topics* catalogues them. **This is the closest term for what you described**, because a topos is defined by being reusable across situations while still having identifiable content |
| **locus communis** → **commonplace** | Latin rhetoric | The same idea, and the root of the *commonplace book* — a personal corpus of collected extracts, which is the direct ancestor of the personal wiki this hub keeps arguing with |
| **snowclone** | linguistics | A phrasal template with slots: "X is the new Y", "have Z, will travel". Use this when the square is a *pattern* rather than a phrase |
| **trope** | narrative criticism | A recurring device. Broader and vaguer than a topos; the TV Tropes sense |
| **formula** | oral-formulaic theory (Parry–Lord) | A recurring phrase occupying a fixed slot. Carries the useful implication that formulas are what make composition *fast* |
| **cliché** / **stock phrase** | general | The pejorative register of the same thing |
| **shibboleth** | sociolinguistics | A phrase that marks which faction the speaker belongs to. The right word when the square identifies a *side*, not just a topic |
| **tell** | poker | An unconscious giveaway. The right word when the square catches something the speaker did not mean to reveal |

So: **the squares are topoi.** If they have slots, they are snowclones. If they identify a faction,
they are shibboleths.

For the genre itself: **buzzword bingo**, also **bullshit bingo**, which is the established name
(Silicon Valley, early 1990s). The mechanics have their own vocabulary worth using literally, because
each one is a design decision: the **free space** at center is granted unconditionally, the **call
list** is the pool the card is drawn from, to **daub** is to mark a hit, and **blackout** or
**coverall** is every square hit — which in this application means the subject was *entirely*
predictable.

For the axis this document adds:

| Term | Field | Why it is the right word |
|---|---|---|
| **register** | linguistics | Style level chosen for an audience and setting. The most accurate single word for "same content, different voice" |
| **genre** | criticism | The form's conventions and the expectations they set |
| **facet** | Ranganathan's faceted classification | Orthogonal axes of description, each independently selectable. Exactly the structure here, from the grandfather of the tagsonomy |
| **focalization** | Genette, narratology | *Whose* viewpoint the account is given from, as distinct from who narrates |
| **projection** | already used in this corpus | [SPARSE-VIEW-OVERLAYS](../pie-stack-views/SPARSE-VIEW-OVERLAYS.md) treats projection as a view parameter; genre is another parameter in the same record |

Note that **register switching** is already named as a failure mode in the ambient `no-ai-gloss`
skill. Making register a *declared* parameter is the fix for that: an undeclared register shift is
laundering, a declared one is a view.

## Why the bingo card is a better benchmark than the glyph

Three properties, and the third is the one that matters.

**It is a contact sheet of textual glyphs.** Twenty-five cells of one to three words, laid out in a
grid, apprehended pre-attentively. The whole argument for the glyph rung — that a thousand abstracts
read serially take an afternoon while a grid is scanned in seconds, and the outliers jump out —
applies to a bingo card in text. It is the parallel-apprehension rung without needing SVG.

**It cannot be faked by extraction, for a stronger reason than glyphs.** A glyph resists extraction
because there is no phrase to steal. A bingo square resists it because the task is **predictive**
rather than descriptive: you are not summarizing what the document said, you are predicting what
this *kind* of document always says. There is no topic sentence to lift, because the answer is not
in the text — it is in the pattern the text belongs to. That makes it the only rung that tests
whether the model has a model of the *genre* and not just of the document.

**It has an objective scoring function, with no human in the loop.** This is the real find. A bingo
square's quality is its **hit rate across the corpus of similar situations**, and the information a
square carries is maximized when that rate is near one half:

- A square that never hits is too specific. Zero bits.
- A square that always hits is too general. Zero bits.
- A square that hits about half the time is maximally informative — Shannon entropy peaks at *p* = ½.

"Specific yet general enough to apply to similar situations" is therefore not a matter of taste. It
is *p* ≈ 0.5, and it is computable: generate a card against one document, then daub it against fifty
others of the same kind and count. Score the card by how close its squares' hit rates cluster around
a half, and penalize the free-space-in-disguise squares that hit every time.

That is a better metric than the glyph blind match on one axis and worse on another. Better: no human
raters, so it scales, and it is not a vibe. Worse: it needs a corpus of *comparable* documents to
daub against, which the glyph test does not.

The trade-off it measures is the same one already named for glyphs — distinctness versus collision.
A glyph too generic collides with everything; a bingo square too generic hits everything. Same
failure, and now one of them has a number.

## The BINGO family: one generator, three parameters

The card is not a single artifact but a **parameterized genre**, and naming the parameters is what
makes it reusable. Three of them:

| Parameter | What it varies | Examples |
|---|---|---|
| **Voice** | the register the squares are written in | deadpan, sardonic, GONZO |
| **Scope** | what gets daubed | one document, a whole blog, a person's corpus, a physical place |
| **Grid** | the coverage budget | 3×3, 5×5, 7×7 |

Named members, with their status:

**BONGO BINGO** — built, and the precedent that matters. A real GPS-driven game where you
**check in to claim a square**, per Don. It establishes that the grid works as a game board over
actual space, not just as a summary layout, which connects the genre directly to
[dispensers and souvenirs](DISPENSERS-AND-SOUVENIRS.md): claiming a square is taking a stamped
souvenir, and a completed line is a set. *(Details are Don's report; not otherwise in the corpus,
and worth writing up properly since it is the only shipped member of the family.)*

**BLOGO BINGO** — proposed. A card for someone's **entire blog** rather than one post, which is
where the predictive property gets its best test: a corpus of one author's writing is precisely a
genre, and the squares predict what that author always does. Don wants one for himself, and several,
for different categories — which is the right instinct, because one card cannot span a large corpus
and a *set* of cards on different axes can.

**GONZO BINGO** — proposed. Hunter S. Thompson's register as the voice parameter. Worth keeping
distinct from "sardonic," because gonzo has a structural commitment beyond tone: the observer is
inside the story and says so. A gonzo card's squares can therefore be about the *encounter* with the
corpus rather than the corpus alone, which is a genuinely different summary and not just a louder one.

**GONZO BONGO BINGO** — the composition, and it is the one that should get built first, because the
structural argument for gonzo *is* the argument for experience logging. Gonzo puts the observer inside
the story, so its squares describe the encounter rather than the subject. That is precisely what a
coffeeshop review is: not the objective properties of the espresso but what happened to you while
drinking it.

So BONGO's GPS check-in mechanic and GONZO's inside-the-story register are the same requirement seen
twice. A square like *"barista assumed you were working on a screenplay"* cannot be evaluated from
the outside, must be claimed by being there, and is exactly the kind of thing a place reliably does
to people. Which makes the card a **map overlay you fill in by living**, and each claimed square a
[souvenir](DISPENSERS-AND-SOUVENIRS.md) with a location and a timestamp — the same
[semantic seeds](../TAGSONOMY-COMPILER.md) the ground-up tagsonomy wants, arriving pre-scored by a
game mechanic.

Don's addition: with a side of garbanzo beans.

### Why this is a universal summary level

Because of a formal property worth stating plainly: **prose summary optimizes for the centroid; a
bingo card optimizes for coverage.** A one-line summary asks *what is this mostly about*, and its
best answer is the middle of the distribution — which is why it regresses to the mean and why
extraction can fake it. A card asks *what are the many dimensions of this space*, and its best
answer must spread out. Filling twenty-five cells with near-synonyms is a visibly bad card, so the
form penalizes exactly the failure that prose summaries reward.

That makes grid dimension a **rung selector** for this genre — the coverage budget is the zoom level.
3×3 is nine dimensions and a glance; 7×7 is forty-nine and a study. Same generator, different budget,
which is the pyramid's own logic applied inside a single genre rather than across genres.

### Cartoons per square: a compound benchmark

Asking the model for a little SVG cartoon in every cell is a **better test than either half alone**,
because it is three tests multiplied, and their failures are distinguishable:

| Failure | What it reveals |
|---|---|
| Wrong square | no model of the genre |
| Right square, generic drawing | no grounding of the concept — it knows the words, not the thing |
| Right concept, illegible drawing | SVG generation failure, isolated from comprehension |

And it yields **twenty-five samples from one context**, so the result is a statistic rather than an
anecdote — the standing weakness of the single-glyph test. The card then inherits parallel
apprehension in both modalities at once: twenty-five tiny drawings scanned in seconds by a human, and
a compact structured artifact for a model. Good at a glance for both readers, which is the whole
premise of the glyph rung arriving with a sample size.

The [parameterized-glyph construction](GLYPH-BENCHMARK.md#parameterized-glyphs-dont-draw-a-thousand-blend-them)
is what keeps twenty-five drawings from saturating into sameness: blend weights over a designed
vocabulary rather than twenty-five independent inventions.

Two costs specific to the cartoons. **Cost multiplies by the grid** — a 7×7 card is forty-nine
drawings, which makes the budget a design constraint rather than an afterthought. And **a charming
drawing can launder a wrong square**, since cuteness reads as competence; the hit-rate metric has to
score the *square*, with the drawing excluded from the judgment, or the benchmark measures charm.

### On self-application

A bingo card about a person is a roast, and the difference between good spirits and punching down is
entirely consent. Self-applied or invited, it is a gift — which is why Don asking for his own is the
right way for this to start, and the right thing to build first. Applied to someone who did not ask,
it is something else, and the clearance rules already governing quotation apply unchanged.

## Other genres worth having

The axis is general, and several of these already exist in the corpus without being recognized as
the same move:

- **The trading card.** `CARD.yml` is already a genre-rendered rung: abilities, effects, combos.
- **The objection list.** [OBJECTIONS.md](OBJECTIONS.md) is a document summarized by its strongest
  attacks, which is a genre with a truth condition — it is wrong if it is weak.
- **The changelog.** The same corpus rendered as what changed, which is the temporal projection in
  [TEMPORAL-SEMANTIC-ZOOM](../pie-stack-views/TEMPORAL-SEMANTIC-ZOOM.md).
- **The scored index.** John Baez's Crackpot Index is a genre *and* a rubric — a summary that
  produces a number, which is what the Church of the Eval Genius does with everything.
- **The eulogy.** Ted Nelson's own eulogy for Engelbart is cited in the nelson pack; a eulogy is a
  life summarized in a register that admits only what mattered.
- **The FAQ**, **the recipe**, **the patch note**, **the tarot card**. Each has conventions strict
  enough to be checkable, which is what makes a genre useful as a rung rather than a costume.

## Honest costs

**Tone is cheaper than insight, and the model knows it.** A model can produce sardonic *voice*
without any understanding of the subject, which is exactly the `TONE-SUBSTITUTION` failure the
ambient `no-ai-gloss` skill names. This is the reason the hit-rate metric has to do the scoring:
tone must earn nothing. A card that sounds cutting and whose squares all hit every document has
failed completely while reading as a success, which makes it the most dangerous output in this whole
design.

**Mocking a subject is not mocking a person.** A sardonic card about a *genre of claim* is fair game.
A sardonic card about a living person whose words this corpus quotes runs straight into the clearance
rules, and the fact that it is funny is not a defense — it is an aggravation, because funny travels.
Anything aimed at a named living person goes through the same register that governs their quotes.

**Twenty-five cells is a closed format.** An abstract can be as long as it needs to be; a card cannot.
Choosing which twenty-five topoi make the card is itself an argument, and a lossy one, and the
document does not get to complain afterward.

**Snowclones drift to the most generic slot fill.** The template survives while its instances
regress to the mean — the same mechanism predicted for glyphs in
[GLYPH-BENCHMARK](GLYPH-BENCHMARK.md#the-predicted-failure-which-is-the-point), one modality over.

---

## Related

- [GLYPH-BENCHMARK.md](GLYPH-BENCHMARK.md) — the resolution axis at its top rung, and the protocol this borrows from
- [hyperties/ARTICLE-SCHEMA.md](hyperties/ARTICLE-SCHEMA.md) — the four-part contract these genres render
- [../TAGSONOMY-COMPILER.md](../TAGSONOMY-COMPILER.md) — genre-rendered rungs are build-time artifacts like every other rung
- [../pie-stack-views/SPARSE-VIEW-OVERLAYS.md](../pie-stack-views/SPARSE-VIEW-OVERLAYS.md) — genre as a view parameter with inheritance and override
- [OBJECTIONS.md](OBJECTIONS.md) — itself an instance
- Ambient skills `no-ai-gloss` (`REGISTER-SWITCHING`, `TONE-SUBSTITUTION`) and `no-ai-slop` (mean regression)

↑ [webtop hub](README.md)
