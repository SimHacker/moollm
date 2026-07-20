# Name Change Toolkit — Skill Seed

*A shippable, free product: everything the prestoration taught us, generalized for
everyone whose name has changed — transition, marriage, divorce, religious conversion,
transliteration, stage names, safety. One founding case: Vanessa Freudenberg, who asked
in public in 2021 and got her answer in 2026.*

## The problem

A name change is trivial in one place and impossible in ten thousand. Your name lives in
version-of-record PDFs, citation databases, git histories, DNS whois, conference sites,
Wayback snapshots, other people's bibliographies, mailing-list archives, and metadata you
have never seen. Institutions each have a policy (or don't), a queue (or don't), and a
form (or don't). The work is a distributed systems problem wearing a paperwork costume —
exactly what an agent with provenance discipline is good at.

## Skill sketch (MOOLLM style)

```yaml
skill: name-change
description: >
  Audit, plan, and execute a name change across documents, code, citations,
  and the live web — with originals preserved, every change disclosed, and
  institutional corrections pursued in parallel with community-scale fixes.
methods:
  AUDIT:      # find every occurrence of the old name across a corpus
    - grep is not enough: PDFs split names around kern pairs; fonts subset;
      encodings differ. Inflate streams, extract properly (Ghostscript/mutool),
      search rendered text AND metadata AND link annotations.
    - build a ledger: venue, artifact, hash, byline location, correction path
  PLAN:       # standing, wishes, venues
    - whose wish is documented, who has standing (self > subject's request >
      family/co-authors > community), what each venue's policy allows
  CORRECT:    # venue-specific playbooks (plugins, one file each)
    - acm-petition:    ACM name-change policy option 3 — corrected version of record
    - publisher:       IEEE, Springer, Elsevier, USENIX equivalents
    - orcid:           the identity layer citations should have used all along
    - git-mailmap:     .mailmap maps old commit identities to the new name
                       without rewriting history — git's native prestoration
    - github:          profile, repo transfers, redirect awareness (old handle
                       URLs keep working; update visible references anyway)
    - pdf-prestoration: the full typographic surgery, per the founding case —
                       subset glyph check first (the font may lack your letters)
    - wikipedia-wikidata, dblp, google-scholar, semantic-scholar
    - web-archives:    snapshots are immutable by design; you layer corrected
                       editions beside them, you don't fight fixity
  PRESERVE:   # originals bit-for-bit, sha256-pinned, adjacent to corrections
  DISCLOSE:   # every change enumerated in the artifact and beside it
principles:
  - fixity is evidence, not the enemy
  - honest labeling: the filename says what the file is
  - the derivative is a bridge to the canonical fix, never a substitute
  - never out anyone: auditing exposure is also auditing safety
related: [postel, robust-first, skill-snitch]
```

## The five-condition test (from the founding case)

A correction is legitimate when **all** hold: documented wish or clear standing ·
original preserved · total disclosure · honest labeling · canonical fix pursued.
Any four out of five is a forgery with good manners.
Full argument: [alignment-and-forgery.md](alignment-and-forgery.md).

## Hard-won technical notes

- **Names hide from grep.** In the founding case the byline was stored as
  `(Freudenber)18(g)` — split around a kern. Search rendered text, not bytes.
- **Font subsets can't always spell you.** Vanessa's paper embedded a sans subset that
  ended one glyph short of the letter *v*. Check `/CharSet` and `/LastChar` before
  promising an in-font edit; keep a base-14 fallback and match the family by eye.
- **Wayback digests prove negatives.** Identical CDX digests across snapshots = the
  document never changed. That's how you show no corrected version ever existed.
- **git doesn't need history rewritten.** `.mailmap` corrects attribution in `git log`,
  `shortlog`, and GitHub display without touching a single commit hash.
- **Redirects mask deadnames.** `github.com/oldname/repo` silently redirects to
  `github.com/newname/repo` — which keeps links working and keeps the old name alive in
  every page that displays the URL text. Update the visible text, keep the redirect.

## Brainstorm — warmly invited

People who have changed their names, who we should invite to shape this (via the Repo
Show and the memorial arc — each controls their own story; nobody is outed; participation
is opt-in):

- **The Squeak/Smalltalk community** — Vanessa's colleagues, who watched the founding
  case's gap stay open for five years
- **Archivists** — David Rosenthal, Brewster Kahle: fixity vs. identity, at scale
- **Maintainers** who have processed contributor name changes in large projects (the
  git/.mailmap veterans)
- **Librarians** — authority records (VIAF, LoC) have handled name changes for a century;
  they solved problems software is still discovering
- **Anyone whose name changed** for any reason — marriage, divorce, faith, stage,
  transliteration across scripts, safety — the toolkit is the same; only the paperwork
  differs

Working title options: `name-change` (plain), `true-name` (Le Guin — your true name,
finally spoken), `prestoration` (the family name). Postel says accept all three.
