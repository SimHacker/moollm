# Patrons

How support works across MOOLLM, WillWrightShowForFood, amsterdank, and the Repo Shows.
Referenced by every `.github/FUNDING.yml`. Patreon: [DonHopkins](https://www.patreon.com/DonHopkins).

## The principle: time-shifted openness, never paywalling

**Nothing is ever removed from the public to create a patron benefit.** Patrons get things
first, and they get to steer. Everything lands open on a published schedule regardless of
whether anybody pays, because the licenses are already irrevocable: MIT on the code, CC-BY on
the writing, CC0 on the facts.

This is the only monetization that costs the commons nothing. First publication is mine to
time; the license is not mine to retract. A patron is buying **earliness and influence**, not
access to something withheld, and the distinction has to survive contact with a bad month --
which is why the embargo is a number and not a mood.

> Embargo: **two weeks** for clips, posts, and datasets. **One month** for app builds and
> tours. If a release slips, the embargo shortens rather than the public date moving.

## What patrons get, and what each thing means

The features are MOOAM grants, not marketing tiers. See [MOOAM.md](./MOOAM.md) -- a patron is
a **principal**, a repo or room is a **resource**, and these are **permissions** on it.

| Grant | What it actually is |
|---|---|
| `early` | The two-week or one-month window above. |
| `chat` | The patron channel, where the work gets discussed while it is still soft. |
| `comment` | Issue and discussion participation, with your name on it in the repo. |
| `vote` | A weighted say in a **scoped** set of real decisions, listed below. |
| `propose` | Pull requests on a fast path, reviewed within days rather than eventually. |
| `write` | Direct commit access to your own room, and to shared curation queues. |
| `curate` | Triage of other people's contributions: accept, reject, ask for evidence. |
| `incarnate` | A room of your own in the repo, authored by you, credited to you, yours to delete. |

`incarnate` is the interesting one, and it is the reason this is not a Patreon with extra
steps: a patron who authors their own room has stopped being an audience. It is the same
mechanism as a guest's self-authored directory under
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md)
and a budtender's tier-4 self-authored character in
[amsterdank](https://github.com/SimHacker/amsterdank/blob/main/skills/coffeeshop/BUDTENDERS.md).
Handing someone the file that is them is the whole design, and it does not become a paid
feature -- guests and subjects always get it free. Patrons get it because they asked to play.

## Votes that actually decide something

A vote that never decides anything is a gimmick, so the scope is explicit and small:

- **Which addresses the next survey ride covers**, drawn from the review queue.
- **Which Repo Show gets produced next**, from the invited-and-willing list.
- **Which long-form talk gets the next transcript-and-index treatment.**
- **Which module gets built next** when two are equally ready.

Everything else is advisory and said to be advisory. Editorial judgment, who gets invited,
what a guest's room says, and anything touching somebody's rights are not votable -- a
majority cannot vote to publish a person's material, and consent is not a poll.

## What patrons owe

Contributions carry the same rights hygiene as everything else, because one careless import
can compromise a dataset built specifically to be clean:

- **Sign off your commits** (DCO `Signed-off-by`). Your contribution is under the repo's
  license, and it has to be yours to give.
- **Your own photographs only.** No scraped images, no map-traced coordinates, no menus lifted
  from someone else's site. See [amsterdank's LICENSE-DATA](https://github.com/SimHacker/amsterdank/blob/main/LICENSE-DATA).
- **Consent before people.** Nobody appears as a character without a recorded, unexpired yes.
- **Provenance on every claim.** Source, date, confidence. An unsourced value is not a
  contribution, it is a rumour with a commit hash.

## What is not open, and is said so plainly

- **Server-side deployment code is rights-reserved.** The hosted service is the one component
  that is not MIT, because it is the one that could be cloned into a competitor. The client,
  the data, the skills and the tools are all permissive. Loosening a license later is easy and
  tightening it is impossible, so it starts reserved.
- **A curated selection of photographs is all-rights-reserved.** The bulk of the survey
  photography is CC-BY; a small edit of the best is held back rather than reaching for the
  non-commercial licenses, which are non-free and would block Wikipedia and OpenStreetMap --
  the audiences that matter most.
- **Other people's material was never mine to license**, and no tier changes that. See each
  repo's `RIGHTS.md`.

## Write access to a public repo, realistically

Direct commit rights on a public repo is a moderation surface, so: protected `main`, pull
requests as the default path even for patrons who have `write`, `CODEOWNERS` on anything
rights-sensitive (`LICENSE*`, `RIGHTS.md`, `agreements/`, `sources.yml`, consent files), and
`write` scoped to your own room plus the curation queues rather than the whole tree. Nobody
gets to edit a consent record but the person who gave it.
