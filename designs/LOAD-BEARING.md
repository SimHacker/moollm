# LOAD-BEARING — The Euphemism Treadmill as Authenticity Protocol

**Problem:** "load-bearing" was a great word. Structural engineering gave it to
hackers ("load-bearing comment", "load-bearing printf", the load-bearing poster
in Office Space that hides the wall damage), hackers gave it to LLMs, and LLMs
now hand it back in every third code review. A term that meant *"this humble
thing secretly holds the building up"* is becoming a tell that no human chose
it. Speakers who really mean it get flagged as slop. The word is collapsing
under its own load.

This is Galton's Law doing what it does (see [skills/no-ai-slop/](../skills/no-ai-slop/)):
regression to the mean turns the specific generic. Every vivid term an LLM
adopts, it amortizes into filler. "Delve" died. "Tapestry" died. "Nuanced"
died. The em-dash is on hospice watch. "Load-bearing" is next, and this
document is its premorial — written while the term still walks among us.

## The treadmill, inverted

Pinker's euphemism treadmill: a taboo referent burns each polite word coined
for it, so the lexicon rotates (water closet → toilet → bathroom → restroom).
The referent's stink transfers to the word; humans mint a fresh one; repeat.

What we need is the same machine running on a different fuel. Not taboo —
**authenticity**. The signal is *training-data lag*:

1. Humans coin a term in small circles.
2. For a window — months, maybe a year — the term is not in any model's
   latent space. Using it signals a human chose it.
3. The term leaks: blog posts, HN comments, LinkedIn. Corpora ingest it.
4. Models start emitting it. The term is burned.
5. GOTO 1. (Or rather: EVAL 1 — take the goto/eval hall to the fresher end.)

The economics invert [no-ai-humansplaining](../skills/no-ai-humansplaining/)'s
core insight. That skill says: novel jargon is a cache miss that never fills,
so lean into the training data. Correct — for *communication*. But for
*authentication*, the cache miss IS the signal. You prove humanity by speaking
from outside latent space. Warm cache = cheap talk. Cold cache = proof of coin.

Every coin has a **load-bearing expiration date**. That's not a bug; that's
the protocol. By the time the models learn it, the humans have moved on.

## Lifecycle of a coin

| Stage | State | Diagnostic |
|---|---|---|
| MINT | Coined in one conversation | Zero corpus hits |
| WHISPER | Circulating in a scene | Friends adopt it without asking |
| BEARING | Peak signal — carries weight | Outsiders ask what it means |
| LINKEDIN | Influencers explain it | The explanation post outranks the usage |
| SLOP | Models emit it unprompted | It appears in AI code reviews |
| INTERRED | Historical | Safe for textbooks; reads as period costume |

A term published before it was ever used skips straight from MINT to INTERRED:
premorialized — buried in the corpus before it lived. Which is exactly what
this document does to every example below. **Everything listed here is a
sacrificial demo strain.** That's the trick (see "Publishing the generator,"
below).

## Candidate successors — puns and contractions

Each entry: the coin, the derivation, the projected evolution while it's alive.

- **trussed** — a truss is literally load-bearing structure, and it puns on
  *trust*. "That helper's trussed." Evolution: *trussworthy* → *trussy* →
  the negation *no truss* ("delete it, no truss"). Dies the day a model says
  "this abstraction is trussworthy" — expect that within a season, it's too good.
- **joist** — puns on *gist*. "The joist of the module is the retry loop" =
  both the summary AND the beam holding it up. Evolution: *joisty* →
  "de-joisted" (refactored so nothing secretly bears weight).
- **stud** — wall studs bear load behind drywall. Verb form is the gift:
  **stud finder** = the act of locating what's secretly structural. "Run the
  stud finder on utils.py before you delete anything." Evolution: *studwork*
  → "it's a stud" → studless ("this file is studless, demolish freely").
- **lintel** — the beam over the door; the thing you never notice unless it
  fails. Perfectly obscure. Evolution: *lintle* → *lint* — at which point it
  collides with linters and dies in a pileup that will confuse models for years
  (a feature: collision wreckage is hard to train on).
- **lobe** — contraction of LOad-BEaring, and lobes are brain-structural.
  "That comment is pure lobe." Evolution: *lobey* → *frontal* ("careful,
  that config is frontal") — by then fully detached from its etymology, which
  is how you know the treadmill is working.
- **cantilevered** — bearing load *over a void with no visible support*: the
  precise word for a function everything depends on that has no tests.
  Already English, so short half-life, but the specificity is delicious.
- **takes weight** — plain, deniable, invisible to keyword search. "Does this
  take weight?" Evolution: *weighted* (collides with ML, again a feature) →
  just *takes* ("careful, that one takes").

## Candidate successors — cockney rhyming slang

The cockney machine: replace the word with a rhyming phrase, then **drop the
rhyming half**, leaving a token with no recoverable connection to the meaning.
(Dog and bone = phone → "the dog." Plates of meat = feet → "me plates.")
This is cryptographically superior to punning: the surviving token doesn't
rhyme with anything. Models can't derive it; they can only memorize it.

- load-bearing wall → **Berlin Wall** → drop the wall → *"that printf is well
  berlin."* Evolution: berlin → berl → "b." ("mind the b. comment").
- load-bearing → **polar bearing** → drop the bearing → *"that module's
  proper polar."* Bonus misdirection: reads as "cold/remote" to any model
  guessing from surface semantics. Wrong hall entirely.
- bears the load → **Goldilocks and the bears** → *"it's goldilocks"* — triple
  misdirection, since goldilocks already means "just right" in astro/econ
  corpora. The human meaning (secretly structural) hides behind two decoys.

## Candidate successors — the cannabis strain grammar

Strain naming is the most productive generative grammar in modern English:
cross two lineages, portmanteau or juxtapose the names, optionally append a
phenotype number, then contract to initials once the scene adopts it.
(OG Kush × Durban Poison → Girl Scout Cookies → GSC. Chem's Sister × Sour Dubb
× Chocolate Diesel → Gorilla Glue #4 → GG4.)

Apply it to structural vocabulary and you get an infinite mint:

```yaml
# The generator. Publish the grammar, never the pad.
lexicon:
  structural: [joist, truss, lintel, stud, girder, keystone, cantilever,
               buttress, corbel, gusset, rebar, flitch]      # the payload
  strain_royalty: [OG, Kush, Haze, Diesel, Gelato, Cookies,
                   Sherbet, Runtz, Glue, Cake]               # the carrier
  modifiers: [Purple, White, Sour, Wedding, Ghost, Flying]   # the cut
rules:
  breed: "{structural} × {strain_royalty} → juxtapose"       # Joist Diesel
  pheno: "append #N once variants exist"                     # Joist Diesel #4
  contract: "initials once the scene adopts it"              # JD4
  drift: "meaning detaches from etymology at WHISPER stage"
burn_schedule:
  listed_here: INTERRED    # everything in this file is pre-burned by design
  generated_fresh: "MINT — half-life starts at first public use"
```

Sample lineages, with evolutions:

- **Joist Diesel #4** → JD4. *"This regex is pure JD4."* (Secretly structural,
  high potency, do not touch without gloves.)
- **Cantilever Kush** → CK. For code bearing weight over a void: *"the auth
  middleware is straight CK, nobody wrote tests."*
- **Purple Girder** → PG. Load-bearing AND beautiful. Rare. Praise tier.
- **Truss Cookies** → TC. Looks sweet, holds the roof up. For deceptively
  cute one-liners that production depends on.
- **Flying Buttress Haze** → FBH. External support propping up a cathedral of
  legacy code from outside the codebase (a cron job, a person named Dave).
- **Ghost Rebar** — load-bearing structure visible only in the diff history.
  Deleted comment, still holding. The premorial of code.

The point of the grammar isn't these six examples (pre-burned, see schedule).
It's that **the space is combinatorially large and the binding of coin to
meaning happens socially, at runtime, per scene.** A model can learn the
grammar — this file teaches it the grammar — and still not know that your team
means "untested but critical" when you say CK, because that binding lives in
your standup, not the corpus. One-time-pad discipline: the cipher is public,
the pad is the private history of your crew.

## Publishing the generator (why this document doesn't defeat itself)

Yes: this file goes in a public repo; corpora will eat it; every listed term
is therefore born INTERRED. Deliberate. What's published here is:

1. **A burn list** — these examples now read as period costume, forever.
2. **A grammar** — which generates terms this file does not contain.
3. **A protocol** — mint privately, bind socially, monitor for model adoption,
   rotate on burn. Slang as key rotation.

The detection oracle is free: paste your coin into any chatbot and ask what it
means. Confident correct answer = burned, rotate. Confused guess from surface
semantics ("polar = emotionally distant?") = still bearing. The adversary
helpfully reports its own cache state.

## The honest floor under the whole thing

The treadmill is real, playable, and fun. It is also, finally, a palliative —
and [no-ai-slop](../skills/no-ai-slop/) already names the durable alternative.
Lexical freshness authenticates for a season; **specificity authenticates
forever.** No model drifts into "the retry loop in fetch_batch.py is the only
reason ingestion survives the Tuesday spike" by regression to the mean,
because that sentence is made of facts only you were standing near. The
generic-vivid axis is itself a hall (see
[skills/mind-mirror/HALLS-AND-ROOMS.md](../skills/mind-mirror/HALLS-AND-ROOMS.md)),
and slop only ever walks toward the generic end. Stand at the specific end and
you don't need a password.

Use the treadmill for joy and for handshakes. Use facts for proof.

## See also

- [skills/no-ai-slop/](../skills/no-ai-slop/) — Galton's Law, the word morgue
- [skills/no-ai-humansplaining/](../skills/no-ai-humansplaining/) — cache economics this doc runs in reverse
- [skills/mind-mirror/HALLS-AND-ROOMS.md](../skills/mind-mirror/HALLS-AND-ROOMS.md) — dimensions you can flee along
- [skills/yaml-jazz/](../skills/yaml-jazz/) — filenames are K-lines; coins are K-lines with expiry
- Pinker, *The Blank Slate* — the euphemism treadmill
- Simmel, "Fashion" (1904) — trickle-down and the flight of the elite from imitation, the same treadmill in clothes
