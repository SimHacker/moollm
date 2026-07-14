# Live Objects in the Field — Soul City and Adventure-4

The object system described in this directory is not a proposal. It runs. Two public places to
watch it: **Soul City / MicropolisCore** (an application platform being built on it) and
**adventure-4** (the example world that ships in this repo). Both demonstrate the same three
moves — objects as directories, template objects instantiating other objects, and multiple
inheritance that mixes concrete prototypes with named concepts from latent space
([LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md)).

Index: [README.md](README.md) · mechanism: [SELF-AND-MOOLLM.md](SELF-AND-MOOLLM.md) ·
cited YAML rendered: [CREAM.md](CREAM.md)

---

## Example 1: Soul City — LLM + human collaboration over live game objects

[MicropolisCore](https://github.com/SimHacker/MicropolisCore) is the public monorepo where
MOOLLM's object system meets running games: the open-source Micropolis (SimCity) engine, a
TypeScript/SvelteKit stack, and the Soul City project. One application, three layers of the
object system at work.

### Souls: bringing game characters to life as objects

[`apps/soul-angel/`](https://github.com/SimHacker/MicropolisCore/tree/main/apps/soul-angel) is
the outreach vehicle: an always-on game companion whose **Soul Bridges** read and write a game's
own soul — saves, albums, characters — from a web overlay. A Sim pulled out of a Sims 1 save
isn't a screenshot; it's an object: a directory of YAML slots with provenance, ready to be
cloned, edited, narrated, recombined, and written back. The
[Soul Album](https://github.com/SimHacker/MicropolisCore/blob/main/apps/soul-angel/SOUL-ALBUM.yml)
is the cross-game schema; each per-game bridge maps native vocabulary (The Sims' *Family Album*)
onto the uplifted game-independent schema — Postel at the file-format boundary.

The philosophy line from its README is this object system exactly: **"Album card = commit.
DVR = session transcript. Provenance = the trace link"** — the same shape as
[thoughtful-commitment](../../skills/thoughtful-commitment/): freeze the ephemeral moment into a
permanent, cited artifact.

### Content: import, export, edit, transform, combine

The content itself is objects all the way down:

- [`packages/sims-io`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io) —
  TypeScript I/O for Sims content: the game's binary formats lifted into editable, versionable
  structures.
- [`documentation/vitamoo/`](https://github.com/SimHacker/MicropolisCore/tree/main/documentation/vitamoo)
  — the world-model/save-alignment and content-pipeline design docs: how saves round-trip
  between the game's substrate and the object graph.
- The [content registry and plugin autodiscovery designs](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/sims-content-registry.md)
  — community content as discoverable, combinable prototypes.

Import a neighborhood, enumerate its souls, clone one, cross it with a named concept ("make her
more Miss Havisham"), export it back into the running game. Every step is CREATE / EDIT /
INSTANTIATE / PERSIST from the [artifactory](../../skills/artifactory/) operation set, and every
step is a commit — git as the space-time diagram of the edit.

### The collaboration platform: humans and agents on common ground

[`moollm-micropolis-integration.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-micropolis-integration.md)
states the DreamScape principle: *users and agents operate in the same environment*. A human
proposes a road; an AI tutor proposes a tax change; a teacher approves; the command bus executes;
the timeline records; git preserves. The AI is not outside the world narrating from nowhere —
it's a participant with scoped permissions, i.e. an object with slots like everything else.

MicropolisCore carries its own MOOLLM skills in-repo
([`skills/micropolis/`](https://github.com/SimHacker/MicropolisCore/tree/main/skills/micropolis),
[`skills/micropolis-command-bus/`](https://github.com/SimHacker/MicropolisCore/tree/main/skills/micropolis-command-bus))
— the distributed skill path from
[file-system-object](../../skills/file-system-object/SKILL.md): mounted repos contribute their
`skills/` to one flat union. The app repo is itself an object exporting interfaces.

The full synthesis — rooms, characters, K-lines, the coherence engine, the Bifrost crossing
between game substrates — is
[`moollm-microworld-os.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md),
written from the MicropolisCore side looking at MOOLLM.

---

## Example 2: Adventure-4 — the built-in world that uses all of it

[`examples/adventure-4/`](../../examples/adventure-4/) ships in this repo and exercises every
mechanism in this directory at once:

- **Rooms as objects.** `pub/`, `garden/`, `forest/`, `maze/`, `kitchen/` — directories that
  constrain what happens inside them; genre physics inherited by naming it.
- **Characters as constellations of named parents.** The bartender declares
  `PRIMARY INHERITANCES (k-lines): Quark (DS9), James (Bar Karma), Guinan, Sam Malone`
  ([CHARACTER.yml](../../examples/adventure-4/characters/fictional/the-bartender/CHARACTER.yml))
  — four latent-space parents, one working personality.
- **Real people via the incarnation protocol.** The
  [real-people characters](../../examples/adventure-4/characters/real-people/) (including the
  [don-hopkins](../../examples/adventure-4/characters/real-people/don-hopkins/) directory with
  its work-history, project, and session slots) inherit a named person's *expertise and
  tradition* without impersonation — the ethics gate lives in
  [incarnation](../../skills/incarnation/).
- **Template objects making objects.** The whole world was built by the constructor stack:
  [artifactory](../../skills/artifactory/) (INSTANTIATE = clone a prototype;
  "class AND instance" resolved the Self way — a prototype is a full object that's ALSO the
  template), [skill](../../skills/skill/) (the skill for making skills — the artifactory-factory),
  [character](../../skills/character/) and [prototype](../../skills/prototype/) (ordered multiple
  parents), [empathic-templates](../../skills/empathic-templates/) (slots that are prompts, so
  instantiation is reasoning, not string substitution).
- **The compiled output.** [`build/`](../../examples/adventure-4/build/) and the adventure
  compiler show the same source tree emitting multiple views — instructions, data, graphics; the
  homoiconic "axis of eval."

Adventure-4 is the small proof; Soul City is the big one. Same object model, same skills, two
scales: a pub with a bartender assembled from four TV traditions, and a platform where a Sim
walks out of a 2000-era binary save into a git-versioned object graph, gets a new story, and
walks back in.

---

## Why these examples matter for the argument

Class-based systems ([YOUTRACKDB-VS-MOOLLM.md](YOUTRACKDB-VS-MOOLLM.md)) need the schema
declared before the data arrives. Game content is the worst case for that: decades of binary
formats, community mods, half-documented fields, vocabulary that differs per game. The
prototype-plus-latent-space model absorbs it: lift what you can into YAML slots, name what the
LLM already knows ("The Sims Family Album", "Miss Havisham", "SimCity traffic simulation"), keep
provenance in git, and let the coherence engine hold it together. That's not a workaround — it's
the only object model we know of whose resolver already contains the culture the content came
from.
