---
name: mapbox
description: Route Mapbox work to the twenty official Mapbox Agent Skills instead of restating them, and own what they cannot know — key locations, measured token-restriction behaviour, and the choice between CLI, REST, MCP and SDK. Use when working with maps, tokens, geocoding, routing, styles, or tiles.
license: MIT
tier: 2
allowed-tools:
  - read_file
  - write_file
  - run_terminal_cmd
related: [sister-script, yaml-jazz, no-ai-humansplaining, robust-first, postel, skill, moollm]
tags: [moollm, mapbox, geospatial, tokens, secrets, cli, mcp, router]
credits:
  - "Mapbox Agent Skills (MIT) — the twenty skills this orchestrates"
moollm:
  upstream: "https://github.com/mapbox/mapbox-agent-skills"
  vendored: false
---

# Mapbox

> **Mapbox wrote twenty skills. This one decides which two you need.**

Mapbox publishes twenty Agent Skills under MIT at
[mapbox/mapbox-agent-skills](https://github.com/mapbox/mapbox-agent-skills) — 6,128 lines
of `SKILL.md`, each with an `AGENTS.md` quick reference, an `evals/evals.json`, and a
`references/` directory. They are good. This skill does not replace them and does not copy
them.

It exists because of three things they do not do.

They ship no router. Twenty skills with no "which one?" layer means the honest default is
loading too much, and attention is the scarce resource, not Mapbox knowledge.

They never say `referer` or `403` — zero occurrences across all 6,128 lines. They tell you
to set URL restrictions but never document the mechanism or its symptom, so the most common
token failure is undiagnosable from their text.

They cannot know your machine: which vault holds which token, which of your tokens is safe
in a browser and which is safe in a shell, and which of your frameworks bakes secrets into
a build artifact.

## Quick start

```bash
cd skills/mapbox
python3 scripts/mapbox_router.py where                  # find the upstream checkout
python3 scripts/mapbox_router.py list                   # the twenty, with descriptions
python3 scripts/mapbox_router.py route "geocoder 403"   # which skills to load
python3 scripts/mapbox_router.py doctor                  # probe tokens and tooling live
python3 scripts/mapbox_router.py measured                # findings upstream lacks
```

The script is its own documentation ([sister-script](../sister-script/)): imports,
globals, CLI definition, implementation. Read the top for the interface.

## Mounting upstream

The relationship is endosymbiotic in the sense moollm already uses the word — Margulis, by
way of [soul-city](../soul-city/) and the korz designs. The official repo is an organelle:
engulfed, but keeping its own genome. It has its own remote, its own license and its own
release cadence, and the host supplies only the envelope — routing, local keys, measured
behaviour. Vendoring would be the opposite operation, copying the DNA into the nucleus and
inheriting its maintenance forever.

Clone it beside your other repos and add it to the workspace. Nothing is vendored, so a
refresh is one `pull`.

```bash
git clone https://github.com/mapbox/mapbox-agent-skills
git -C mapbox-agent-skills pull        # refresh whenever
```

The resolver tries, in order: `$MAPBOX_AGENT_SKILLS`, then `~/GroundUp/git/`, `~/git/`,
`~/src/`, then `./`, `../`, `../../` for a sibling checkout, then `~/.agents/skills` and
`~/.claude/skills` where `npx skills add mapbox/mapbox-agent-skills` installs them. If all
miss, every command still answers and points at the URL rather than failing.

Four other install routes exist and all deliver the same content:
`npx skills add mapbox/mapbox-agent-skills`, `/plugin marketplace add
mapbox/mapbox-agent-skills` (which also wires up the three MCP servers),
`mapbox agent-skills install`, or a plain clone.

## ROUTE

Give the question in plain words; get two or three skill names.

```bash
python3 scripts/mapbox_router.py route "my svelte map is slow and geocoding returns 403"
```

Routing is coarse keyword matching on purpose. The goal is loading three skills instead of
twenty, not cleverness. When nothing matches, it says so and points at `list` rather than
guessing.

When the subject is one upstream does not cover, it says that too, and names the surface
that does. Tilesets, fonts, sprites, accounts, Atlas and the licensed data products have no
skill; they have CLI commands.

## DIAGNOSE

A Mapbox 403 is almost always the URL restriction, and the decision tree is short. Run
`doctor`, which probes a passing origin, the dev port, the preview port, an unrelated
origin, and no referer at all.

Read the result like this. **No referer is 403** for any restricted token, which means that
token is dead from curl, CI, a server-side `fetch`, and every MCP server — they all send
none. Keep an unrestricted token for those and never ship it in a bundle. **An unrelated
origin answering 200** means the restriction is not in force; check the list actually saved.
**The dev port passing while the preview port fails** means the entry is an exact port:
prefer the wildcard `http://localhost:*`, which is Mapbox's own advice in
`mapbox-token-security`.

Two measured traps will otherwise cost you an afternoon.

Enforcement is per-endpoint. Tile and data requests enforce the restriction; style metadata
at `/styles/v1/<user>/<id>` answered 200 from every origin tried. A passing metadata call
proves nothing — probe a tile.

Edits take minutes to reach the edge, and the intermediate state is per-variant. For
several minutes after one save, `http://localhost:5173` answered 200 while
`http://localhost:5173/` answered 403. That reads exactly like a matching bug and is not
one. Re-probe a few minutes later before concluding anything, and never write a finding
from a single probe — three runs minimum.

## SURFACE

Four ways in. MCP is rarely the right one, and the ordering below is by composability.

**REST with curl and jq** is the most composable and needs nothing installed. Every service
is plain HTTP with a token parameter. Note the geocoding v6 path is
`/search/geocode/v6/forward` — `geocoder` returns 404.

```bash
TOK=$(op read "op://Employee/Mapbox/token" --account groundupsoftware.1password.com)
curl -s "https://api.mapbox.com/search/geocode/v6/forward?q=Leliegracht%20Amsterdam&access_token=$TOK" \
  | jq -r '.features[0].properties.full_address'
curl -s "https://api.mapbox.com/isochrone/v1/mapbox/cycling/4.88,52.37?contours_minutes=10&polygons=true&access_token=$TOK" \
  | jq '.features[0].geometry.coordinates[0] | length'
```

**The official CLI** is unified and explicitly agent-first, covering auth, accounts, fonts,
geocoding, search, sprites, static, styles and tilesets. It ships as an install script, not
npm or brew or PyPI, which is why package searches miss it. `mapbox generate-skills` writes
a skill describing its own command surface — point it at a directory and read what it
writes.

```bash
curl -fsSL https://cli.mapbox.com/install.sh | sh
```

**Three MCP servers**, not two. `@mapbox/mcp-server` is the runtime one, wrapping the
location APIs for agents answering questions about the world. `@mapbox/mcp-devkit-server`
is the authoring one, wrapping your account — 23 tools across styles, tokens, validation
and conversion. `@mapbox/mcp-docs-server` looks up documentation. The clean way to hold them
apart: the runtime server queries the world, the devkit server mutates your account. The
devkit needs secret scopes, and it can create tokens, which is a meaningful privilege to
hand an agent.

You do not need an MCP client to call one. A stdio server speaks newline-delimited
JSON-RPC, so a shell pipe is enough — which makes devkit tools usable from a
sister-script without the client overhead.

```bash
{ echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"probe","version":"0"}}}'
  echo '{"jsonrpc":"2.0","method":"notifications/initialized"}'
  echo '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
  sleep 3; } | MAPBOX_ACCESS_TOKEN=$TOK npx -y @mapbox/mcp-devkit-server
```

**SDKs** last. `mapbox-gl` for the browser, `@mapbox/mapbox-sdk` for node. The Python
client last shipped in 2022 and the old `mapboxcli` in 2018; neither is where the work is.

## KEYS

Tokens are resolved by role from 1Password, never pasted. Roles differ by *where the code
runs*, not by who owns them.

| Role | Reference | Where it may run |
|---|---|---|
| prod | `op://Employee/Mapbox/ebike-safari-token` | browser only — 403 without a referer |
| dev | `op://Employee/Mapbox/token` | CLI, MCP, CI, scripts — never in a bundle |

The item is in vault **Employee**; there is no Personal vault on that account. Public
scopes and URL restrictions are editable in place and leave the `pk.` string unchanged, so
changing them needs no redeploy. Secret scopes are different: they produce an `sk.` token
displayed once, which must never reach a browser.

The framework trap worth naming, because it is silent: a SvelteKit app prerendered with
`ssr=false` compiles any `PUBLIC_*` variable into the static bundle at build time, so the
token is baked into the Docker image and rotating it means rebuilding. Name it
`MAPBOX_TOKEN`, read it in a `+server.ts` via `$env/dynamic/private`, and hand it to the
browser at runtime — then rotation is a container restart.

## MEASURE

The measured table in `scripts/mapbox_router.py` is the part of this skill that cannot be
borrowed, so it has an entry rule: **probe first, claim second, three runs minimum.**

Record the endpoint and the date with the finding. Prefer a tile endpoint, since that is
where enforcement lands. When a probe contradicts an earlier entry, replace the entry
rather than annotating it — the table states what is true now, not the history of what was
believed. A finding that came from one request during a propagation window is not a
finding.

## What to borrow back

Upstream ships `evals/evals.json` per skill: real prompts, expected outputs, and
per-expectation checklists — a regression harness for a skill's *judgment*. moollm has no
equivalent rung in its pyramid. That pattern is worth adopting repo-wide, and this skill is
a reasonable place to try it first.

## Related MOOLLM skills

- [sister-script](../sister-script/) — the router script is its own documentation
- [no-ai-humansplaining](../no-ai-humansplaining/) — the argument against vendoring the
  twenty: restating what the agent can read is billed per call, forever
- [robust-first](../robust-first/) — a missing checkout degrades to a URL, never a crash
- [postel](../postel/) — route liberally on messy questions, emit exact skill names
- [yaml-jazz](../yaml-jazz/) — `GLANCE.yml` and `CARD.yml` as semantic YAML

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm), a microworld OS where
the filesystem is navigable space and skills are inheritable prototypes. See the
[repo README](https://github.com/SimHacker/moollm#readme) and
[skills README](https://github.com/SimHacker/moollm/tree/main/skills#readme).

## Credits

The twenty skills, the three MCP servers and the CLI are Mapbox's work, MIT licensed, at
[mapbox/mapbox-agent-skills](https://github.com/mapbox/mapbox-agent-skills). This skill
routes to them and adds only what is local and what was measured.
