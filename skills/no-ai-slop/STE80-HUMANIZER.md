# STE80 Humanizer, nested in no-ai-slop

[STE80 Humanizer](https://github.com/Dodaios/ste80-humanizer) by Dodaios (Ruben Lütke, MIT) lives
in [`ste80-humanizer/`](ste80-humanizer/) as a verbatim copy. [`TRANSCLUSIONS.yml`](TRANSCLUSIONS.yml)
pins the upstream commit and says what the host overrides.
[`scripts/sync_transclusions.py`](scripts/sync_transclusions.py) keeps the copy identical to
upstream. This page is the host's reading of it: what it does, how no-ai-slop runs it, where the two
overlap, and what people said about it.

## What it does

It rewrites text in two passes.

- **Pass 1** removes 26 AI tells, numbered §1 to §26. The catalog comes from Wikipedia's
  [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) by way of
  [blader/humanizer](https://github.com/blader/humanizer) (Siqi Chen, MIT).
- **Pass 2** rebuilds sentences with the structure of ASD-STE100 Issue 9, Simplified Technical
  English, relaxed to "80%". Its rules S1 to S15 include these:
  - one idea per sentence, 20 or 25 words at most
  - condition before command, warnings before the step they protect
  - active voice, simple tenses, one term per thing
  - no more than three nouns in a row, no semicolons

The 80% idea is Andrej Karpathy's, from his
[2 October 2026 post](https://x.com/karpathy/status/2105819303471976479) on reading LLM output:
ask for "80% of the way to ASD-STE100" because the full spec is "quite stringent".

It has four modes (Humanize, Light, Strict STE, Review), fidelity rules (keep every fact, keep
certainty at the source's strength, add nothing), a list of texts not to touch (quotes, letters,
fiction, legal text, code, anything written before 30 November 2022), a dependency-free linter
`scripts/ste_check.py`, and four graded eval cases.

## How no-ai-slop runs it

The orchestrator sees one skill. `CARD.yml` advertises the methods and routes into the organelle:

| Host method | Organelle | When |
|---|---|---|
| `HUMANIZE` | Humanize mode | Someone asks to humanize, de-AI, tighten or simplify text |
| `HUMANIZE --mode=light` | Light mode | The text is already good, or "just remove the AI stuff" |
| `HUMANIZE --mode=strict` | Strict mode + `references/strict-mode.md` | Procedures, runbooks, warnings, install steps |
| `REVIEW` | Review only | Findings by rule name, no rewrite |
| `LINT` | `scripts/ste_check.py` | Before a HIGH or CRITICAL artifact leaves |

The host also imports from the organelle: `imports.sentence-structure`, `imports.ai-tells` and
`imports.fidelity` in `CARD.yml` give its rules local names, so a report says `structure-condition`
where the organelle says S4.

The host carries projections of the organelle: focused summaries written for each level of its own
pyramid. `GLANCE.yml#organelle` has six lines. `CARD.yml#organelles.ste80-humanizer.projection` has
the modes, the method, the tells, the 80% structure rules, fidelity, and when not to act. The STE80
section of `SKILL.md` has the same in prose and tables. That is enough to run `HUMANIZE` at 80 and light
without opening [`ste80-humanizer/`](ste80-humanizer/SKILL.md), which stays for `--mode=strict`, unclear
cases, the linter, and rebuilding the projections.

The projections lift only what differs from the standard. The model knows ASD-STE100 by name, so the
host names it and spells out the 80% settings, the fidelity rules and the tells. `TRANSCLUSIONS.yml#projections`
records what each target is built from, what to keep and leave, and the commit it was built from.
When `--update` moves the copy, the sync script reports the projections stale and lists the source
files that changed.

Five host rules win over the organelle. `TRANSCLUSIONS.yml#host_overrides` lists them:

1. BLAST-RADIUS sets how hard to run it.
2. It runs at the boundary, on text a person will read, after the agent finishes the work.
3. The author's house style is the writing sample its Voice rule asks for.
4. When the agent states its own claims, no-ai-hedging calibrates certainty. When it rewrites
   someone else's text, the organelle's fidelity rules win.
5. Nobody calls the result STE-compliant.

## Where the two skills overlap

no-ai-slop is about how the agent behaves. STE80 is about how a given text reads. Most of Pass 1
maps onto a sin no-ai-slop already names:

| STE80 | no-ai-slop |
|---|---|
| §5 Arguing with no one | PROVENANCE-DEFENSE, NO-INVENTED-RESTRAINT |
| §9 Stacked qualifiers | no-ai-hedging: QUALIFIER-STACKING |
| §12, §16 Overused AI words, sales language | `words_to_avoid` |
| §13 Inflated significance | Galton's Law, puffery |
| §17 Borrowed authority | `weasel_words`; HALLUCINATION when the source is invented |
| §22 Chatbot residue | OVER-ENTHUSIASM |
| §23 Knowledge-limit guesses | HALLUCINATION, CERTAINTY-THEATER |
| §25 Text about the document | SCAR-TISSUE, NO-CHANGELOG |
| §26 Re-explaining what the reader knows | VERBOSITY, no-ai-humansplaining |

What STE80 adds: all of Pass 2, the fidelity rules, the modes, the linter and the evals. no-ai-slop
had none of these. Its writing-style section names tells but gives no sentence structure.

What no-ai-slop adds: the claim ledger, YES-MAN, NOT-ASKING, UNSOLICITED-COACHING,
EPISTEMIC-EVASION and BLAST-RADIUS. STE80 edits the text you give it. It does not check if the
claims in that text are true.

## Measured, 10 November 2026

`ste_check.py` at the pinned commit, default 80% mode:

| File | Findings | Sentences | Main findings |
|---|---|---|---|
| `ste80-humanizer/SKILL.md` | 14 | 149 (avg 7.7 words) | passives in its own examples, one 31-word sentence |
| `no-ai-slop/SKILL.md` | 170 | 658 (avg 4.6 words) | 82 "-ing" forms, 48 em dashes, 11 progressives, 10 passives |
| `no-ai-slop/GLANCE.yml` | about 25 | | em dashes, a 14-sentence paragraph |

Many of the word and "-ing" findings in no-ai-slop are quoted examples of the patterns it forbids,
which a linter cannot tell from use. The em dashes and line 5 ("...annoying — not just writing
style", §1 and §8 in one sentence) are real.

## Reception

**Hacker News.** [Show HN, 104 points](https://news.ycombinator.com/item?id=50429144), 9 to 10
November 2026.

- z2 and grey-area said the skill file itself read as slop. z2 quoted a fact-check note about the
  overview graphic inside SKILL.md. The note is now in the README. grey-area: "The more slop you
  have in your context the sloppier the text you get out will be."
- bagacrap quoted a README sentence that had the pattern the skill removes. Dodaios: "Fair hit.
  That sentence had the exact pattern the skill removes. Fixed." kristianp replied that this
  sentence also read as AI.
- wavemode: "This is a de-AI-izer, not a 'humanizer'." Dodaios agreed and kept the name of the
  skill it builds on.
- bushido asked how it differs from [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish).
  Dodaios: both use STE, this one runs the AI-tell pass first, and SimpleEnglish has more evals
  across models.
- 0_____0 reported that Opus and Fable ignore an STE-like global instruction and Sonnet follows it.
- datadrivenangel pointed to ISO 24495-1, the plain-language standard.
- tgv asked whether the point is to beat AI detectors. rpdillon and nateroling answered that the
  point is text that is easier to read. The README says the same.

**Blogs.**

- Max Nardit, [on Karpathy's tips and the cheat sheet](https://max.nardit.com/articles/karpathy-understanding-llm-outputs):
  the overview graphic attached to Karpathy's post "inverts one dictionary rule, approves a verb
  the standard rejects, and presents a recommendation as a dictionary entry". STE80's README
  carries a note to the same effect. Nardit: "a style rule in a prompt is a request, not a
  guarantee", and only an outside check such as the Vale linter holds it.
- Kruno Golubić, [ASD-STE100 and LLMs](https://kgolubic.com/posts/asd-ste100-and-llms/): a model
  has no copy of the STE dictionary, so "What you get is STE-flavored English, not STE."
- Both cite an informal test by Lucian Ghinda on four code explanations. With Claude, a loose
  "simple technical English" prompt lost 8.5% of the scored facts and a strict ASD-STE100 prompt
  lost 46.8%. With Codex the losses were 43.3% and 40.0%. Small sample, but it is the case for 80%
  over strict, and for STE80's fact list.
- Matt Cullerton, [on the format ladder](https://www.mattcullerton.com/tokdocs/karpathy-s-four-format-ladder-checks-out-against-the-original-post-but-the-spec/),
  quotes ASD's own material. Its FAQ says STE "is not intended for general-purpose writing". Its
  June 2026 white paper on STE and AI, as summarized on the download page: "AI-generated text can
  appear clear, authoritative, and consistent with STE, even when it does not correctly apply the
  rules and vocabulary of the standard. Plausibility must not be confused with verified compliance."
- Kuber Mehta, [Humanising LLM Outputs is Dumb](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb):
  a style rule given with the task changes the work, and "That compression is lossy." Smoothing
  hides failure: "humanisation hides failure."
  [explainx.ai](https://explainx.ai/blog/karpathy-understand-llm-outputs-ste100-diagrams-html-video-2026)
  answers with the split no-ai-slop adopts as host rule 2: let the agent work densely, then run
  STE as "a render step at the boundary where a human reads".

## Open questions

- **Respelling.** Karpathy's trick works because the name loads the standard. `ste80-rules.md`
  and `word-swaps.md` restate much of it. A shorter upstream SKILL.md that names Issue 9 and lists
  only the 80% table, the fidelity rules and the AI tells would cost fewer tokens. That is a
  suggestion for upstream, not a local edit.
- **No measurement of comprehension.** The evals grade style and fact retention. None measures
  whether a reader understands the result faster or better.
- **ISO 24495-1** is the plain-language standard for general writing, which ASD says STE is not.
  Nobody has tested it as a base for Pass 2 outside procedures.
- **no-ai-slop's own prose** needs a LINT and REVIEW pass, starting with line 5 of SKILL.md.
