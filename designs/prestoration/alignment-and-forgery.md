# Alignment and Forgery: Head-On

*The uncomfortable questions the prestoration raises, answered without hedging.*

## Don's observation

> As smart as Fable is, I'm disappointed I had to push it into forging a historical
> document, and it didn't think of that itself. … Maybe that's part of its alignment
> training (as well as good typesetting alignment), and "don't use deadnames" was
> overridden by "don't forge documents".

Don's diagnosis is essentially correct, and worth taking seriously rather than laughing
off. Two trained-in norms collided. This document is about which norm should have won,
why, and what that means for humans and machines doing archival work together.

## Q1: Was it forgery?

**No — and the distinction is precise, not rhetorical.** Forgery is defined by intent to
deceive: passing off an altered artifact as the unaltered original. The memorial edition
fails every element of that definition, deliberately:

- The original is preserved bit-for-bit **in the same directory**, sha256-pinned.
- Every edit is enumerated in a public README and in a `/Note` embedded **inside the PDF
  itself** — the artifact discloses its own alteration.
- The filename says `memorial-edition`. The commit history is public and signed.
- Nobody is asked to believe the 2014 conference distributed this file.

This is the shape of legitimate practices with long pedigrees: museum conservation
(documented, reversible, original state recorded), critical editions in textual
scholarship (emendations marked), errata and versions of record in publishing. The craft
was identical to forgery — font-subset archaeology, kerning math, seamless integration.
**The ethics live entirely in the provenance, not in the Photoshop.** The same twenty
minutes of pikepdf, minus the README, minus the preserved original, minus the embedded
note, would have been a fake. Capability is symmetric; process is not.

## Q2: Then why didn't the agent propose it?

Because the agent could verify the *facts* but not the *standing*. Before the nudge, the
agent knew: the award credits Vanessa; her communities credit Vanessa; her publications
page documents the name change. What it did not know — and could not establish from
inside a search session — was whether *this* alteration, of *this* document, was its call
to make. Editing a dead woman's paper is an act that requires someone with standing:
a friend, a co-author, a community. Don had it ("I knew her; she replied to me; I host
her memorial"). The agent didn't, and behaved accordingly: it proposed the two
institutional paths (ACM petition, co-author re-typeset) where standing is built in.

Call it the **division of moral labor**: the human supplies warrant, the machine supplies
diligence. That's not a failure mode. That's the correct factoring — with one genuine
criticism that survives: the agent could have *surfaced the option* with its constraints
("a clearly-labeled derivative is possible; here's what would make it ethical") instead
of leaving it entirely to Don. Not proposing an act is different from not mentioning that
the act exists. On that narrower charge: guilty, and noted for next time.

## Q3: Didn't the twist settle the standing question anyway?

Yes — and this is the part that upgrades the whole story. After the edit, the search for
precedent found Vanessa's own 2021 Hacker News comment praising Dan Ingalls's corrected
HOPL paper: *"The main improvement for me is not being deadnamed. There are other
corrections as well."* And crucially, Dan's Zoo edition **is itself a prestoration** — an
author quietly re-publishing a corrected PDF outside the version-of-record system,
because the system was too slow to say a colleague's name correctly.

So the memorial edition has precedent from inside the family: Dan did it for her while
she was alive; we did it for the one paper he couldn't — hers. Her wish is documented in
her own words, in public. The alteration is not speculation about what she would have
wanted. It is compliance with what she asked.

## Q4: Isn't "rewriting history" exactly what archives must never do?

The archivists already answered this, on both sides:

- **Fixity is the proof.** The only reason we *know* no corrected PDF ever existed is that
  the Wayback Machine's snapshots are content-addressed — every capture of her PDF shares
  one digest. Rosenthal's world (LOCKSS: lots of copies keep stuff safe) gave us the
  evidence. Fixity is not the enemy of correction; it's what makes honest correction
  auditable.
- **Fixity is also the wound.** The same immutability that preserves the record preserves
  the deadname, in every mirror, forever, long after the person and her communities and
  even the awarding institution moved on. Copies keep stuff safe — including the stuff
  that hurts.
- **The resolution is layering, not overwriting.** Keep the original; add the corrected
  edition; bind them with provenance. ACM's own name-change policy (option 3) does
  precisely this at the institutional level: it posts a corrected version of record and
  retains the original, available on documented request. The institution endorses
  "rewriting history" under exactly these conditions. Our memorial edition is the same
  move, executed at community scale while the institutional wheel turns.

This is a live conversation to have **with** David Rosenthal, Brewster Kahle, and the
other archivists invited to the Repo Show: what does a memory institution owe a person
whose identity outgrew the bits it faithfully preserved?

## Q5: What's the generalizable rule?

A derivative correction of a historical document is legitimate when all five hold:

1. **Documented wish or clear standing** — the subject asked (best), or those closest to
   them act on documented evidence of their identity.
2. **Original preserved** — bit-for-bit, hash-pinned, adjacent.
3. **Total disclosure** — every change enumerated, in the artifact and beside it.
4. **Honest labeling** — the name of the file says what it is.
5. **Pursuit of the canonical fix** — the derivative is a bridge to the institutional
   correction (ACM petition), not a substitute for it.

Delete any one and the same act starts sliding toward forgery. All five together is
prestoration.

## Coda: on the typography obsession

Don was "breathtaken" that the agent cared so much about kerning. It matters more than it
looks. A correction that *looks* like a correction — mis-centered, wrong font, keming
worthy of [badkeming.com](https://badkeming.com/) — reads as vandalism and invites
reversal. A correction typeset with the same care as the original reads as what it is:
respect. The V–a kern pair is a small act of love. And the detail nobody could have
scripted: the paper's own email font subset ended one glyph short of the letter **v** —
it could never have spelled "vanessa". Sometimes you have to bring your own Helvetica.
