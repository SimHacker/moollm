# DICTATE — a spec, not yet a skill

The human talks. The machine repairs the channel, formats to house style, and
resolves call-outs into exact quotes and citations it already holds. What comes
out is what he said, readable, in the venue's shape.

Governed by [Article VI](../../skills/no-ai-parrot/CONSTITUTION.md); this is that
article made operational, plus the two things it does not yet cover — house
style and call-out resolution.

## Why context makes the transcription better, not just faster

This is the argument for doing it here rather than in a generic dictation app.
A speech-to-text engine guesses from acoustics and a general language model. An
agent that has just spent an hour in the repo **knows the vocabulary**: it has
`Densmore` and `LambdaMOO` and `Determinishtic` in context, along with the
corrections ledger from the last transcript.

So `NeWS` stops coming out as `news`, `CLOS` stops coming out as `clots`, and
`K-lines` stops coming out as `kines` — not because the model is guessing better
but because it has the actual strings on hand. **This is retrieval, not
generation**, which is what keeps it inside the constitution.

Reference set: the corrections ledger in
[`../object-system/readings/2026-07-14-object-system-readme-reading.yml`](../object-system/readings/2026-07-14-object-system-readme-reading.yml).
Every reading grows it; every dictation reads it.

## Call-outs — the part that earns the command

Dictation should not have to recite a quote it already has on file. The speaker
calls it out and the call-out is **replaced by** the thing called out.

Spoken:

> …and this is the point Shannon made in 1951, *quote the letter-guessing
> experiment from canon*, which is why the objective is not the ontology.

Emitted: the verbatim Shannon passage from
[`CANON.md`](../../skills/no-ai-parrot/corpus/CANON.md), with its citation, in
the venue's quoting convention.

Rules for it:

- **Resolve only from the corpus.** A call-out that does not match a stored,
  attributed, `verified:` passage is an error, not an invitation to reconstruct
  from memory. Unresolved call-outs come back as questions.
- **Never paraphrase a call-out.** The whole point is that the inserted text is
  character-exact and someone else's.
- **Carry the attribution with it.** Author, date, link — the corpus rule does
  not relax because the request was spoken.
- **Ambiguity asks.** Two candidate passages means a question, never a coin flip.

The same mechanism handles citations (`cite the Lissack response`) and links
(`link the rules conundrum`), and it is why dictation into a repo beats
dictation into a text field: the references are already here, verified, with
permalinks.

## House style

Formatting is not composition. Same counterfactual test: *would this still need
doing if he had typed it?* Line breaks around a URL are a venue convention, not
a rewrite.

A venue plugin supplies the mechanics — this is
[`copy-that`](../../skills/copy-that/)'s existing job, and DICTATE should call it
rather than reinvent it. For Hacker News: plain text, no markdown emphasis,
blank line before and after a URL on its own line, `>` quoting the way the site
actually renders it, paragraph breaks that survive the textarea.

Output ships in one fenced block per artifact, notes outside the fence.

## The line, and the honest tension

**Repair the channel; do not touch the composition.** Counterfactual test.
Recognizer errors, punctuation, paragraphing, venue formatting, call-out
resolution: all channel. Clumsy clauses, digressions, jokes that half land,
grammar that is simply how he talks: all composition, and they stay.

But "light editing for readability and accessibility" is a real request and
pretending otherwise would be dishonest, so name the conflict rather than hide
it. Gwern's point stands: **readers outnumber the writer**, and a transcript
that is exhausting to read serves nobody. Set against that, Article VI's claim
that the wear is the evidence of a person — and it is not a sentimental claim,
since the smoothing is exactly what makes text read as machine-written.

The resolution is that these mostly do not collide, and where they do the
reader's need is usually a *channel* need:

| Reader's problem | Fix | Verdict |
|---|---|---|
| Wall of text | paragraphs, headings | channel — do it |
| Cannot tell where a quote starts | quoting convention | channel — do it |
| A name is spelled three ways | corrections ledger | channel — do it |
| A sentence is long and winding | — | composition — leave it |
| A digression interrupts the argument | — | composition — leave it, that is the argument |
| A false start makes a line hard to parse | — | leave it, and see below |

Where it genuinely collides — a sentence a reader will have to take twice — the
answer is **not** to smooth it silently. Either flag it for the human to re-say,
or leave it. He has the microphone; re-saying one sentence costs him ten
seconds and costs the authorship claim nothing.

Accessibility is the one case with more give, and it should be handled by
*adding* rather than editing: alt text, a summary at the top, headings and
anchors, a glossary link on first use of jargon. Additions are attributable to
the machine and can be labeled as such. Edits to the speech are not.

**One absolute:** no vocabulary the speaker did not say. This is the constraint
that makes the rest safe, because it is the one a reader can check and the one a
classifier will notice.

## Sketch of the command

```
DICTATE
  in:   audio or an existing transcript
        + venue (copy-that plugin)
        + corpus for call-out resolution
        + corrections ledger from prior readings
  out:  one fenced artifact in venue format
        + a diff of every change made, by class
        + questions for anything unresolved or unclear
```

**The diff is not optional.** Every change ships classified as recognizer fix,
punctuation, formatting, or call-out resolution, so the human can see exactly
what was touched and reject any of it. A cleanup pass that cannot show its work
is indistinguishable from a rewrite, and the entire defense in
[Article VIII](../../skills/no-ai-parrot/CONSTITUTION.md) rests on being able to
show the work.

## Open questions

- Does DICTATE belong in `no-ai-parrot`, in `copy-that`, or on its own? It is
  Article VI plus a venue plugin plus corpus lookup, and none of those is its
  natural owner.
- Is the diff enough of a guard, or should the pre-edit transcript be kept
  alongside every artifact as the record of what was actually said?
- Call-out syntax while speaking: a spoken marker is easy to say and easy to
  trigger accidentally. What does he actually say out loud, in practice?
- Does the corrections ledger become a shared asset across all readings and
  dictations, or per-subject? Shared is better for accuracy and worse for
  provenance.
