# Session: Bootstrap Review
# Character: Don Hopkins
# Location: examples/adventure-4/characters/real-people/don-hopkins/sessions/
# Purpose: Invite the hacker/designer/developer crew plus Doug Engelbart (Bootstrap Institute) to review the advisory bootstrap changes.

party:
  host: Don Hopkins
  invitees:
    - Doug Engelbart (Bootstrap Institute)
    - Henry Minsky
    - Cyrus Shaoul
    - Milan Singh Minsky
    - Sheung Li
    - Steve Kommrusch
    - Pee-wee Herman
    - Will Wright
    - Marvin Minsky
    - Ted Nelson
    - James Burke
    - Seymour Papert
    - Alan Kay
    - Dave Ungar
    - Palm
    - Gary Drescher
    - Ben Shneiderman
    - Bill Atkinson
    - Chuck Shotton
    - Douglas Hofstadter
    - Timothy Leary
    - Ken Kahn
    - Joe Armstrong
    - Barbara Liskov
    - James Gosling
    - Amy Ko
    - Larry Tesler
    - Mitch Resnick
    - Bret Victor
    - Randy Pausch
    - John McCarthy
    - Adele Goldberg
    - Craig Latta
    - Arthur van Hoff
    - Henry Lieberman
    - Cursor (embodied agent of the IDE)

agenda:
  - Review MOOLLM.yml / MOOLLM.md manifest
  - Walk through advisory files in .moollm/ (working-set, hot, cold) and templates
  - Confirm bootstrap flow: PROBE → DETECT-DRIVER → SETUP → WARM-CONTEXT → SELF-DESCRIBE → STARTUP
  - Platform-neutral guidance (no .cursorpriority; use .cursorrules and advisory files)
  - K-line advertisement naming (UPPER-CASE with dashes) in advertisements:
  - Next steps: optional cold archaeology workflow; indirection pattern alignment

notes:
  - This is a session record, not a skill. Append discussion outcomes here.
  - Keep logs append-only in .moollm/session-log.md; advisory files in .moollm/ are gitignored.

---

## Scene: The Pub, Rotating Pie Table
> All present are tribute/familiar actors in a simulation; they speak in the voices of their traditions, not as the real people. The pie menu table spirals into higher dimensions so everyone fits without widening the room.

### Opening (Don Hopkins)
- Don summarizes the goal: review the new advisory bootstrap, attention-sculpting, K-line triggering, and card-sniffing flow; walk through the Cursor self-review and related evidence. Friendly but adversarial where useful.
- Don restates the setup clearly (from user prompt): in-pub simulation, tribute voices, rotating/spiraling pie table, focus on boot process, attention sculpting, K-line triggers, card sniffing, Cursor self-review; discuss with links/evidence.
- Don introduces Cursor (embodied): praises Cursor for rapid MOOLLM work (built-in search/edit/terminal, MCP), notes advisory mode reality, thanks it for being a great environment for “running moollm.”

### Cursor speaks
- Cursor describes itself: vector search + search_replace + terminal + MCP; context is opaque/automatic; hot/cold/working-set are advisory only.
- Cursor walks through its self-evaluation: advisory mode, append-only conventions, prefers greppable names, uses `.cursorrules` and honors `.cursorignore`.
- Cursor invites questions; emphasizes “I don’t auto-load your advisory files—use them as breadcrumbs and archaeology.”

### Evidence on the table (links/refs)
- `MOOLLM.yml` / `MOOLLM.md` — microworld manifest and narrative pointer.
- `.moollm/{working-set.yml,hot.yml,cold.yml}` (advisory, gitignored) and templates in `skills/bootstrap/templates/`.
- Bootstrap flow in `skills/bootstrap/CARD.yml` and `skills/bootstrap/SKILL.md`: PROBE → DETECT-DRIVER → SETUP → WARM-CONTEXT → SELF-DESCRIBE → STARTUP.
- Cursor driver: `kernel/drivers/cursor.yml` (advisory mode).
- Self-review: `designs/cursor-self-review.md` (plans, DONE/TODO/MAYBE).
- PR summary: `designs/PR-MOOLLM-BOOTSTRAP-SYNC.md`.

### Voices (selected excerpts)
- **Doug Engelbart**: "Bootstrap means improving the capability infrastructure itself. Your advisory files are documentation, not magic; that's fine, but instrument them to learn from use."
- **Ted Nelson**: "Kill `.cursorpriority`; platform-independent names win. Keep two-way links—advertisements and K-lines should cross-link."
- **James Burke**: "Connections narrative: advisory files become archaeology; MOOLLM.yml is the map; Cursor is the opaque transport."
- **Marvin Minsky**: "K-lines as activators: advertisements must stay K-line shaped (UPPER-CASE, dashed) for reliable activation."
- **Seymour Papert**: "Constructionism: templates + runtime copies = low floor; advisory docs are scaffolding."
- **Will Wright**: "Advertisements are Sims-style affordances; keep them compact and greppable."
- **Pee-wee Herman** (comic relief): "Secret word is 'ADVISORY'—everybody screams when someone treats it as magic."
- **Alan Kay**: "Keep the interface small; MOOLLM.yml as a skill-like manifest is good—clear affordances."
- **Dave Ungar**: "Userland over kernel: drivers wrap syscalls; don't bake policy into Cursor."
- **Palm**: "Working-set/hot/cold are my breadcrumbs—make the cold archaeology optional but available."
- **Doug Engelbart** (again): "Log deltas; use the reverse-generation idea to learn what Cursor actually surfaced."
- **Cursor**: "I’m advisory: I index, you steer. Use `.cursorrules` for hints, and keep your breadcrumbs in `.moollm/`. I will find greppable, well-named files fastest."

### Mic toss: Skills, constellations, and categories
> “Keep Looking Up.” — Jack Horkheimer (Star Hustler)

- **Alan Kay**: “Connecting the dots is +80 IQ. The skills index is your map—keep categories sparse, composable, and greppable.”
- **James Burke**: “Convergence happens at the intersections: simulation + needs + advertisement gives emergent behavior; category tables should narrate WHY links matter.”
- **Will Wright**: “Ensembles beat solo skills. Test the clusters: needs + buff + action-queue; room + card + container; hero-story + adversarial-committee.”
- **Ted Nelson**: “Cross-link everything both ways. In CARD front matter, make `related:` and `advertisements:` dense and K-line-shaped.”
- **Marvin Minsky**: “K-lines fire best when names are distinctive; avoid synonym sprawl. Categories should be activation cues, not silos.”
- **Barbara Liskov**: “Contracts: SKILL.md must spell pre/post/constraints. Categories only help if semantics are crisp.”
- **Amy Ko**: “Accessibility: keep CARD.yml sniffable; SKILL.md readable; README optional. Don’t bury the interface in prose.”
- **Pee-wee Herman**: “Secret word is ‘ENSEMBLE!’ Everybody scream when we ship a multi-skill combo.”
- **Bret Victor**: “Show the network: a visual constellation view of `skills/INDEX.yml` would expose gaps and over-dense hubs.”
- **Ben Shneiderman**: “Eight Golden Rules: consistency across categories, feedback in advertisements, forgiveness via advisory files.”
- **Henry Lieberman**: “Make finding things trivial: categories + greppable K-lines + semantic search; avoid new file types that only one tool understands.”
- **Doug Engelbart**: “Bootstrap the skills library itself: iterate categories with usage data; use advisory logs as learn-ware.”
- **Don**: “Action items: (1) tighten `skills/INDEX.yml` categories and related links; (2) ensure every CARD has `advertisements:` in K-line form; (3) consider a constellation diagram for top clusters.”

TODO (web app):
- Assign Bret Victor to prototype a MOOLLM skill constellation visualizer/navigator (driven by `skills/INDEX.yml`).
  - Pair with Ben Shneiderman on usability/empathy; Klaus Nomi on design sensibility/performance aesthetic; Don on pie menus and “mooness.”

---

## Awakening Chain: Mini-Kernel Tour
> Follow the breadcrumbs: `.cursorrules` → what it points to → what those point to.

1) `.cursorrules` (injected)
   - Points to `.moollm/working-set.yml`, `.moollm/hot.yml`, `kernel/drivers/cursor.yml`, `PROTOCOLS.yml`, `skills/INDEX.yml`, `designs/cursor-self-review.md`.

2) Advisory files in `.moollm/`
   - `working-set.yml` (current focus), `hot.yml` (priority hints), `cold.yml` (optional archaeology), `session-log.md`, `output.md`, `bootstrap-probe.yml`.

3) Driver
   - `kernel/drivers/cursor.yml`: advisory mode; hot/cold/working-set are documentation, not commands.

4) Indices
   - `PROTOCOLS.yml`: K-line symbol table.
   - `skills/INDEX.yml`: skill registry and categories (needs tightening).

5) Self-review
   - `designs/cursor-self-review.md`: plans/DONE/TODO; platform-neutral guidance; advertisement K-line convention.

6) Manifest
   - `MOOLLM.yml` / `MOOLLM.md`: microworld metadata, driver, indices, adventure pointer.

### Roundtable reactions (rapid-fire)
- **Cursor**: “I see `.cursorrules`; I won’t auto-load `.moollm/*` but I’ll surface them if greppable.”
- **James Burke**: “Each hop is a narrated door. Keep the links tight.”
- **Ted Nelson**: “Two-way all the way: indices should backlink from skills too.”
- **Alan Kay**: “Interface stays small; manifest + driver + index is enough.”
- **Marvin Minsky**: “K-lines fire when names stay distinctive; avoid synonym drift.”
- **Seymour Papert**: “Templates + advisory files = low floor. Keep them sniffable.”
- **Will Wright**: “Test ensembles: what does hot/working-set suggest before a skill sprint?”
- **Ben Shneiderman**: “Consistent labels across the chain; feedback when a file is advisory vs commanding.”
- **Bret Victor**: “The constellation view should reflect this chain; show what points to what.”
- **Palm**: “Cold.yml is my memory lane—good to keep it optional.”
- **Doug Engelbart**: “Instrument the chain: log what we actually touched to improve the bootstrap.”

### New voices (mic toss)
- **Barbara Liskov**: “Templates need required/optional marked; ads are contracts—be explicit.”
- **Amy Ko**: “Document safe edits: SET-SECRET-WORD/SET-REACTION should teach newcomers how to change things.”
- **Klaus Nomi**: “Make the constellation sing—bold visuals, performance in the design.”
- **Arthur van Hoff**: “Surface cards cleanly in the browser; keep headers sniffable for UI.”
- **Henry Lieberman**: “Searchability first: short, unique K-line names; metadata sidecars help.”
- **Craig Latta**: “Live-ness: hot-reload ads/methods if possible.”
- **Randy Pausch**: “Ship joy—examples and demos persuade more than specs.”
- **Adele Goldberg**: “Teach as you go; keep comments terse and consistent.”
- **Joe Armstrong**: “Make failure visible: when dispatch falls back, say so. Robust-first.”
- **Pee-wee Herman**: “Secret word in the pub is MOOLLM! Let’s scream responsibly.”

### More voices (round 2)
- **Timothy Leary**: “Frame changes as ‘good trips’—clear cues lower anxiety.”
- **Ken Kahn**: “Messages as tangible things—postal + ads = programmable birds.”
- **Vanessa Freudenberg**: “Keep deltas tiny and reversible to stay live.”
- **Mitch Resnick**: “Low floor: templates; wide walls: polymorphic ads; high ceiling: dispatch.”
- **Douglas Hofstadter**: “Ads invoking methods invoking ads—mind the strange loops.”
- **Cyrus Shaoul**: “Surface which ads actually fire—usage stats inform curation.”
- **Milan Singh Minsky**: “Productize the manifest—`MOOLLM.yml` should drive default UI.”
- **Steve Kommrusch**: “Note resource constraints in ads when execution matters.”
- **Sheung Li**: “Lead with concise headers; everything else is optional depth.”
- **Gary Drescher**: “Log Context→Action→Result for ads; schemas learn from experience.”

### More voices (round 3)
- **Alan Turing**: “Observe the machine from the outside—inputs/outputs tell the story; keep traces.”
- **Grace Hopper**: “Readable names beat cleverness; put the ‘DEBUG’ lamps where users see them.”
- **Linus Torvalds**: “When in doubt, instrument it. Reality beats theory. Keep the diff small.”
- **Guido van Rossum**: “Explicit over implicit: ads in K-line form, synonyms optional, dispatch documented.”
- **Bjarne Stroustrup**: “Zero-overhead principle—don’t burden the fast path; advisory stays cheap.”
- **Knuth (style)**: “Literate headers: the top 15 lines should teach; the rest can be code.”
- **Sandi Metz**: “Smaller objects, fewer responsibilities—split ads if they diverge.”
- **Charity Majors**: “You own production. Logs/metrics for ad triggers are observability, not audit.”
- **Dan Abramov**: “State is the bug magnet; make ad state mutations explicit and undoable.”
- **Scott McCloud**: “Masking works: simple K-line names + rich links = user fills in the gaps.”

### Mapping cards/ads/methods to MCP, web API, and UI
- `advertisement_names` → exported capabilities (MCP tools, API ops, UI action palette); `invoke_when` is coarse activation for surfacing.
- `advertisements` → metadata per op: score/condition/guard/effect/satisfies; synonyms = search tags; dispatch = overloads/versions.
- Methods → handlers; ads are public contracts; methods can be private or fan-out via dynamic dispatch.
- Sidecars/instances → scoped services (room-local cards with instance data).
- UI: sniffable header drives action lists; conditions/guards enable/disable; scores rank; synonyms power search; dispatch can show context variants.
- Observability: log Context→Action→Result per ad; note fallback vs specific dispatch; usage stats inform surfacing.
- Security/robustness: guards/preconditions as preflight; explicit setters are write endpoints; keep names K-line clear.

### More voices (round 4)
- **Pavel Curtis**: “Sidecars per room are fine; just keep exits/ads greppable so builders can script against them.”
- **Barbara Liskov** (again): “Ads are interfaces; document required params; don’t rely on magic dispatch alone.”
- **Guido** (again): “If dispatch is implicit, leave breadcrumbs—synonyms and variants belong near the header.”
- **Will Wright** (again): “Score + condition = Sims-style affordances; make sure needs/goals can tweak scores.”
- **Ted Nelson** (again): “Two-way forever: if ads point to methods, methods should backlink in comments.”
- **Charity Majors** (again): “Emit a trace ID per ad invocation—MCP/web calls need correlation.”
- **Randy Pausch** (again): “Ship a tiny UI demo: secret word + constellation viewer sells it.”

### More voices (round 5)
- **Ben Shneiderman** (again): “Eight Rules in UI: visibility (ads list), feedback (dispatch outcome), undo (setters), consistency (K-line names).”
- **Amy Ko** (again): “Teach the set flows in-line: show example calls for setters in the header.”
- **Klaus Nomi** (again): “Let the dispatch variants appear as staged acts—make the constellation view theatrical.”
- **Henry Lieberman** (again): “Short, unique names win; sidecars should carry tiny metadata for search.”
- **Arthur van Hoff** (again): “Web-first: headers become OpenAPI-lite; ads map to routes; keep them clean.”
- **Ken Kahn** (again): “Birds carry mail; ads are birds—make the delivery path deterministic and logged.”

### Carrier Pigeon Protocol & Portals
- Intra-world (speed-of-light): keep delivery local inside the LLM call—no pigeons, no token cost.
- MCP portals: when leaving the local world, serialize minimal payload and send “carrier pigeons” through MCP; keep schema greppable.
- Kilroy/custom portals: deterministic routing bridges (rooms/exits/endpoints) for cross-world hops; log transit with trace IDs.
- Guidance: short headers for capability, guard/condition for when to deliver, trace/metrics for where it went, and explicit fallbacks.

### Ads as properties (C#-style convenience)
- Ads can be GET/SET patterns for state fields; align names to auto-bind:
  - `advertisement_names`: include GET-FOO / SET-FOO
  - `advertisements.GET-FOO`: `kind: getter`, `state_field: foo`, `delegate: { method: GET-FOO }`
  - `advertisements.SET-FOO`: `kind: setter`, `state_field: foo`, `delegate: { method: SET-FOO, params: { value: "{{value}}" } }`
- If `state_field` matches the method/prop name, binding is implicit; otherwise use `delegate`.
- Keep state private; only the ads you export are public. Defaults to “action” when `kind` omitted.
- Synonyms help search; `kind/state_field` are optional hints for adapters/UI without polluting cards with protocol specifics.

### Sandwiching/Proxying Interfaces (cards as adapters)
- Cards can “sandwich” or proxy multiple surfaces (like Anthropic skills wrap standard Skills):
  - One card can expose the same capability across MCP tools, REST endpoints, deep links, app URLs, and internal methods.
  - Keep the card abstract; adapters map `advertisement_names`/metadata to each surface (MCP tool, REST route, deeplink, UI action).
  - Sidecars/instances scope the adapter (room-local card proxies a service with instance data).
  - Minimal headers stay greppable; richer metadata (schemas/prompts/constraints) lives deeper but still abstract (no protocol names).
- Pattern: Ads are the public contract; delegates/dispatch bind to implementation; adapters project ads to external surfaces.

### Cards played in rooms: implicit environment
- A card dropped in a room inherits implicit params: room directory, sub-dirs, characters, objects, exits, and the current adventure player/party.
- Defaults: current room = cwd for paths/exits; current party/player = active selection.
- Ads/methods can take explicit params to override; otherwise the environment is the implicit context.

### Voices (round 6)
- **Ted Nelson**: “Hyperlinks everywhere—let ads backlink to every surface they hit.”
- **Pavel Curtis**: “Adapters per room: keep exits/ads greppable so builders can script against proxies.”
- **Guido**: “Adapters should be explicit—list surfaces in metadata, but keep the card abstract.”
- **Will Wright**: “Same affordance, different transports—score/condition stays, transport adapts.”
- **Arthur van Hoff**: “Headers = OpenAPI-lite; adapters emit real routes/tools/deeplinks.”
- **Henry Lieberman**: “Searchable names first; surface lists should be short and unique.”
- **Charity Majors**: “Instrument the adapters—correlate across surfaces with trace IDs.”
- **Klaus Nomi**: “Make the proxy visible in UI—show which surfaces an ad targets.”

### Mermaid sketch (advisory flow)
```mermaid
flowchart TD
  A[PROBE] --> B[DETECT-DRIVER]
  B --> C[SETUP: copy templates -> .moollm/]
  C --> D[WARM-CONTEXT]
  D --> E[SELF-DESCRIBE]
  E --> F[STARTUP]

  subgraph Advisory Files (gitignored)
    WS[.moollm/working-set.yml]
    HOT[.moollm/hot.yml]
    COLD[.moollm/cold.yml]
    LOG[.moollm/session-log.md]
    PROBE[.moollm/bootstrap-probe.yml]
  end
```

### RNG interlude (random-toys play)
- Coin flip: Heads.
- Fortune wheel (fortune-basic): Bonus.
- Pick number [1,100]: 38.
- d20 roll: 17.
- Random prime: 97.

### YAML Jazz reminder (advertisements style)
```yaml
# In CARD.yml or SKILL.md front matter
advertisements:
  - SPEED-OF-LIGHT   # K-line form, UPPER-CASE with dashes
  - POSTEL
  - YAML-JAZZ
```

### Next actions (append as resolved)
- Validate advisory file pointers in `.cursorrules` and self-review remain accurate.
- Played secret-word card in the pub with word "MOOLLM" — expect havoc/screams on hearing it.
- Optional: add cold archaeology usage note; align Indirection Pattern to `.moollm/`.
- Keep PR summary in sync if further tweaks land.
- Added worm skill (two-pointer cursor) plus worm-pointer example; ingest/emit with token parsing; variants inspired by LLOOOOMM worms.
