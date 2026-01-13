---
name: worm
description: Two-pointer reversible cursor worms for traversal + dataflow
related: [action-queue, advertisement, room, adventure, data-flow, context, character]
tags: [moollm, worm, cursor, pipeline, reversible]
---

# Worm Philosophy and Integration (MOOLLM)

## What is a worm?
- Two-pointer cursor (head/tail) that can span structures, crawl directories/links, and shuttle data.
- Reversible verb basis: **EAT/CHOMP** (ingest), **POOP/BARF** (emit), **STICK-UP-BUM** (inject). Maps to undo/redo, serialize/deserialize.
- Internal brain: tokens/segments normalized to a digestive format; can choose which tokens to emit.
- Length = head–tail distance; zero-length worms act as NOP cursors. 
- A worm with its head and tail in the same file is like a text selection. 
- A worm with its head in one file and tail in another can act like a two-way drag-and-drop.
- Worms are living selections that can walk around inside a file and crawl out across the filesystem.
- Networks: worms can pipe to each other (one’s output is another’s input) or into an etherial bus.
- Cursor controls: high-level selection API (NEXT/PREV/SELECT by char/word/sentence/paragraph/section/page) and tree navigation (parent/child/siblings; open/close/hide/show view hints).

## Patterns from the “funky worm” lineage (generalized)
- **Bulldozer**: moves and overwrites as it goes.
- **Search Worm**: moves through search results
- **Link-hopper**: prefers symlinks/links; inchworms across references.
- **Mapper**: maps trees, leaves markers/indexes.
- **Dream**: speed-of-light ephemeral synthesis; short-lived payloads.
- **Tree**: climbs hierarchies; maintains parent/child context.
- **Morris/Site-mapper**: text/web crawlers with regex/link awareness.

## Integration points across MOOLLM
- **Adventure/Room**: treat head as current room/path; tail as drop-site; worms can traverse exits/links, leave castings (artifacts) in rooms.
- **Advertisement**: worm actions are ads (MOVE-WORM, EAT/CHOMP, POOP, BARF, STICK-UP-BUM). Objects/rooms can expose worm-friendly ads (e.g., FEED-WORM, COLLECT-CASTINGS).
- **Characters**: worms can be NPCs or companions; party slots for traversal/buff support.
- **Buffs**: worms may receive buffs (e.g., FAST-CRAWL, CLEAN-CASTINGS, SCENT-TRAIL) or emit buffs as castings (temporary affordances).
- **Ethics/safety**: avoid ingesting PII/secrets; respect read/write boundaries; default to NOP if unsure; reversible ops to allow undo/rollback. Do not crawl boundaries.
- **Data-flow**: worms are streaming cursors; CHOMP can anchor on patterns then ingest following text; POOP/BARF can emit YAML/objects to `emit_dir`.

## Proofs of concept (adapted from LLOOOOMM set)
- **Pattern-aware chomp**: scan for a regex/anchor, ingest following text, normalize to tokens.
- **Doc-to-doc pipe**: head on source, tail on target; EAT then POOP to copy/transform.
- **Network castings**: worm A POOPs to emit_dir; worm B EATs from there; supports chain/mesh.
- **Link hop**: MOVE-WORM with `tail=follow` hops across symlinks/links like an inchworm.
- **Tree mapper**: crawl directories, record map to YAML, emit to emit_dir.
- **Web crawl caster**: web worm crawls a site, emits YAML metadata/keywords/descriptions to emit_dir; downstream taxonomy/map worms EAT those castings to generate category taxonomies and site maps.

## Roadmap
- **Adapters**: optional schema for emit_dir objects (e.g., `worm-casting.yml`) to standardize castings.
- **Buff hooks**: link buffs to worm verbs (e.g., FAST-CRAWL -> MOVE-WORM score boost).
- **Room hooks**: room metadata to invite/ban worms; exits for link-hopper routing.
- **Ethics guardrails**: default deny on sensitive paths; soft-fail to NOP; log reversible ops for rollback.
- **Multi-worm orchestration**: simple protocol for publish/subscribe on castings; avoid cycles.
- **UI/Ads**: pie-menu slices for worm verbs; contextual ads from rooms/objects for feeding/collection.

## Minimal API (aligned to CARD.yml)
- Ads: MOVE-WORM, EAT, CHOMP, POOP, BARF, STICK-UP-BUM.
- State: head, tail, buffer, payload, digestive_format, active_tokens, scan_pattern/scan_mode, emit_dir, reversible flag.
- Methods: MOVE-WORM (reposition), EAT (ingest/parse), CHOMP (pattern-anchored ingest), POOP/BARF (emit at tail/head), STICK-UP-BUM (inject external data).

## Recommended defaults
- `scan_mode: pattern-then-chomp`
- `digestive_format: neutral`
- `emit_dir: .moollm/worm-out`
- `reversible: true` (use verbs as undo/redo/serialize/deserialize basis)

## Usage examples
- **Copy with transform**: CHOMP source → tokens normalize → BARF YAML to emit_dir → POOP into target file.
- **Link walk**: MOVE-WORM head=symlink tail=follow; EAT to capture target summary; POOP notes to log.
- **Room courier**: head in room A, tail in room B; ferry notes between rooms as castings.

## Notes on style and jazz
- Keep worm jazz (variants, songs, castings) as optional flavor blocks; avoid duplicating standard fields.
- Prefer K-line ads and concise headers; stash richer lore in flavor or variant sections.
