# Quotes: attributed playback, and the robot voice as audio quote marks

**Status:** Design (harvested 2026-09, not started)
**Origin:** the "plugs" architecture Don built at the AI Foundation, inverted into a disclosure
mechanism

## Where this comes from

At the AI Foundation, Don rewrote the facial animation system and content pipeline underneath
Digital Deepak — a consented and paid-for digital twin of Deepak Chopra — in Unity3D, so the
existing content could be reused. The pipeline did speech-to-text on the user, mapped the text to
**plugs**, and played them back to carry on a simulated conversation.

A plug was a pre-recorded thing the person actually said. Not text-to-speech. The system could not
put a new sentence in his mouth; it could only choose which of his real sentences to play. That
constraint was an artifact of production reality rather than an ethical stance, but it is the right
constraint, and it generalizes.

`plugs` is the historical term and keeps its provenance value. It is also butt-adjacent, so the
working replacement is **Quotes**. Naming is not settled.

## What a Quote is

A unit of attributed playback. Three media forms, one discipline:

| Form | Playback | Disclosure |
|---|---|---|
| Recorded audio | the actual recording | it *is* the person; nothing to disclose |
| Recorded video | the actual recording | same |
| Text with no recording | text-to-speech in a **designated robot voice** | the voice itself |

The third row is the interesting one.

## The robot voice as audio quote marks

When there is no recording, the words are still theirs, so they should be speakable. But they must
never be spoken in a synthesized imitation of the person. They are rendered in a **designated robot
voice** — deliberately, audibly not them.

The listener chooses that voice, from any voice available on their system. This is first an
accessibility and customizability feature, and the default is whatever common robot voice the
browser already has. But the choice is also the mechanism: **the listener knows it is the robot
voice because they picked it.** A selected voice carries parameters too — pitch, speed, effects — so
if they get tired of the default they change it, which re-establishes the fact rather than eroding
it.

The result functions as audio quotation marks. It declares, structurally and continuously: *these
are the person's words, and this is not a recording of the person saying them.*

**Why structural disclosure beats stated disclosure.** A spoken disclaimer at the top of a session
can be missed, skipped, or simply forgotten twenty minutes in — and the longer the session runs, the
more the memory of the disclaimer decays while the impression of the voice accumulates. A voice the
listener selected cannot decay that way. There is no moment at which they could mistake it for the
person, because the mismatch is present in every syllable.

The corollary is that the medium can carry the disclaimer by itself, without any statement at all.
A parrot voice is the limiting case: what a parrot says is by definition parroting, so the form
announces its own status.

## The fourth configuration

[readings](readings/README.md) tracks who supplied the words versus who supplied the voice,
and whether any substitution is disclosed. Quote playback is a fourth entry, and it discloses by a
different means than the other three.

| Configuration | Words | Voice | Disclosed |
|---|---|---|---|
| Style profile | a machine's, aimed at your voice | counterfeit of yours | no — that is the point |
| A reading | yours, filed by machine, reordered by you | yours | n/a, it is you |
| Gwern / Painter | the author's, verbatim | a different real person's | yes, by statement, immediately |
| **Quote playback** | the subject's, verbatim | **deliberately non-human, listener-chosen** | **yes, structurally and continuously** |

The axis was never whether a machine was involved. It is whose judgment ordered the words, and
whether substitution is evident. Quote playback is the only one of the four where the disclosure
cannot lapse.

## A Quote is an object, not a string

The user's requirement: every Quote carries verifiable attribution, metadata contextualization,
interpretation — and can have issues, discussions and pull requests against it.

That makes a Quote a directory rather than a line of text. It holds, at minimum:

- **Attribution** — source URL or archive file, date, venue, speaker, and how it was verified
- **Contextualization** — what was happening around it, what it was replying to
- **Interpretation** — contested readings, held *separately* from the quote so that disagreement
  about meaning never edits the words
- **Clearance** — whether it may be published, following the register practice already in use in
  `characters/don-hopkins/correspondence/QUOTE-CLEARANCE.yml`
- **Discussion surface** — issues and PRs, so an argument about what a quote means becomes a
  reviewable artifact instead of a comment-section fight

The separation of interpretation from attribution is the part that does real work. It means two
people can disagree violently about what someone meant while both being unable to touch what they
said.

## The provenance player

The natural pairing with [view-source](webtop-gwern-inheritance/TWO-LAYER-VIEW-SOURCE.md): hovering
any quote in the rendered site surfaces the exact URL or archive file that contributed it, and
dropping through goes to the Quote's directory in the backing store, where the discussion lives.

## The hard constraint

**A Quote plays. It does not generate.** Where a real, non-consenting person's material is involved,
the system may retrieve and arrange but never author. No new sentence enters the world in their
voice.

This is the enforceable form of the anti-skin-suit rule in
[representation-ethics](../skills/representation-ethics/SKILL.md). Consented subjects — Don himself,
Richard Bartle — operate under their own terms. For everyone uncontacted, quotes only.

## Open questions

- **The name.** `Quotes` is the working answer. It collides with the existing clearance register's
  use of the word, which may be a feature.
- **Rotted sources.** A Quote whose source URL is dead still has an archive file, but its
  verifiability is now a claim about our own archive. Whether that downgrades its status, and how
  visibly, is undecided.
- **Video consent is not audio consent.** Someone who agreed to be quoted in print did not thereby
  agree to have their face played back in an interactive exhibit. The clearance schema currently
  does not distinguish these.
- **Whether interpretation should be attributed too.** If contested readings are first-class, the
  readings have authors, and those authors have standing.

## See also

- [readings/README.md](readings/README.md) — the taxonomy this extends
- [LATENT-SPACE-REPUTATION.md](LATENT-SPACE-REPUTATION.md) — why attributed playback matters for
  people whose corpus is being summarized without them
- [NOISY-CHANNEL.md](NOISY-CHANNEL.md) — layered loss; a robot voice is a channel artifact made
  deliberate and legible instead of hidden
- [../skills/speech/SKILL.md](../skills/speech/SKILL.md) — the TTS and voice machinery this would
  ride on, which currently has no attribution or consent layer
- [EXPLORATORIUM.md](EXPLORATORIUM.md) — the disposition of the site this plays into
