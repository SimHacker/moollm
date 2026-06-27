# Cards as Objects — polymorphic cards, branches as persistence, pointers, and leaning into GitHub

> Constitutional / kernel note. Extends `DIRECTORY-AS-OBJECT.md` + `NAMING.yml`.
> Origin: Don Hopkins, 2026-06-27. (Reconcile / dedup with existing DIRECTORY-AS-OBJECT and
> NAMING conventions — esp. any prior coined term for `<classname>_<objectid>` branches.)

## Cards are polymorphic objects

A `CARD.yml` (see `skills/card`) is a **generic, polymorphic object**. Same shape, many
kinds:

- **repo-card** — represents a whole repo (or a branch / release / commit of one)
- **show-card** — a Repo Show is *a kind of* card with its own modular interoperable state
- **comment-card**, **classic family-album card** (image+text, à la The Sims)
- **pointer-card** (below)

Every card carries **categorized links** (links typed by KIND/semantic direction —
several `next`, several `prev`, plus `aside`/`prerequisite`/`remix-of`/…), so cards form a
navigable network *and* linear playlists (paths through it). See the project-side schema:
`family-album-cards.yml`.

## README.md is the front page (lean into GitHub)

GitHub auto-renders a directory's `README.md`. So **the card's front page = the dir's
README**:
- the directory listing above it = "show all" / full disclosure / navigation,
- link the README directly to **hide** the listing (just GitHub chrome around it),
- the card **links + activates** that README the standard moollm way; its metadata is
  precious — download it first to drive web apps + simulations,
- a card points to **every facet**: YouTube videos/playlists, Twitch channels/archives,
  GitHub repos/dirs/files.

Using GitHub *right* does a lot of our work — and motivating people (especially **students**)
to learn git/GitHub gives them **something to show**. (Prefer self-hosted / un-enshittified
hosts where possible; the pattern is host-agnostic.)

## A git branch is the persistent side of an object

Convention: a git **branch** named **`<classname>_<objectid>`** (e.g. `card_9345435345`) is
the **persistent state** of one object — a "Donnie Darko" universe branch storing that
object's filesystem-state **timeline**: it evolves, and you can **rewind** it.

- Perfect for SimCity/Sims **saves + metadata + logs + albums + exports** (a family-album
  card = a commit on such a branch).
- `<classname>_<objectid>` is the naming convention (reconcile with `NAMING.yml`; Don may
  have coined a name for this already).

## Pointer cards (and URLs)

A **pointer card** is a card kind that refers indirectly to an object:
- a **repo pointer**: `user / repo / ref / line#from-to`,
- you **declare** the pointed-to thing (e.g. a YAML subtree) is an object of type `foo`; the
  runtime / LLM **dereferences** it (or treats it as dereferenced),
- plain **URLs** work too — a GitHub URL is just one kind of **universal URL**.

This leans into GitHub + plain URLs + ordinary programming-language **pointers/references**.

## Runtime
The orchestrator + **moo CLI** + a **virtual namespaced filesystem** composition (docker-mount
style, with caching) can back all of this — moollm can run inside such a mounted/cached
namespace. See mooco `designs/` (architecture + composition) and
`designs/PARAMETERIZED-SKILLS.md`.

## Ties
- `DIRECTORY-AS-OBJECT.md`, `NAMING.yml`, `constitution-core.md`
- `skills/card` (the card meta-skill / pun-stack)
- DonHopkins `projects/micropolis-moollm/process/family-album-cards.yml` (the worked schema)
