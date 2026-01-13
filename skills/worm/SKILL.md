---
name: worm
description: Two-pointer reversible cursor worms for traversal and dataflow
allowed-tools: [read_file, write_file, list_dir]
tier: 1
protocol: WORM
related: [action-queue, advertisement, room, adventure, data-flow, context, character]
tags: [moollm, worm, cursor, pipeline, reversible]
---

# Worm

> Two-ended cursor (head + tail) that can ingest, parse, shuttle, and emit data across the filesystem (and links), with reversible verbs.

## What it is
- Two-pointer worm (head/tail) acting as a cursor/pipeline.
- Verbs are reversible: **EAT/CHOMP** (ingest), **POOP/BARF** (emit), **STICK-UP-BUM** (inject). Maps to undo/redo, serialize/deserialize.
- Internal brain: tokens/segments normalized to a digestive format; active tokens can be re-emitted.
- Length = head–tail distance; zero-length worms act as NOP cursors.
- Network-friendly: one worm’s output can be another’s input (castings).

## When to use
- Crawl directories/links with optional pattern-anchored ingest.
- Pipe from one document to another; copy/transform with reversible ops.
- Build/consume worm castings (YAML metadata, taxonomies, maps).
- Traverse link-heavy graphs (link-hopper) or map trees (tree mapper).

## How it works
- **Ads**: MOVE-WORM, MOVE-HEAD, MOVE-ASS, NEXT-UNIT, PREV-UNIT, SELECT-RANGE, TREE-UP/DOWN/NEXT/PREV/OPEN/CLOSE/HIDE/SHOW, EAT, CHOMP, POOP, BARF, STICK-UP-BUM.
- **Cursor controls**: NEXT-UNIT, PREV-UNIT, SELECT-RANGE for char/word/sentence/paragraph/section/page granularity; tree navigation for parent/child/siblings and view hints (open/close/hide/show).
- **State**: head, tail, buffer, payload, digestive_format, active_tokens, scan_pattern/scan_mode, emit_dir, reversible.
- **Methods**: MOVE-WORM/HEAD/ASS (abs/rel, directions), EAT/CHOMP (ingest + parse), POOP/BARF (emit at tail/head, can write YAML to emit_dir), STICK-UP-BUM (inject data).
- **Dispatch**: Ads as generics; methods as implementations (Self/CLOS-style dynamic dispatch).

## Safety/Ethics
- Default to NOP if unsure; avoid ingesting secrets/PII; respect read/write boundaries.
- Reversible verbs support undo/rollback; log when emitting to emit_dir.

## Examples / Patterns
- Pattern-aware chomp → emit YAML castings; downstream worms build taxonomies/maps.
- Link-hopper inchworms through symlinks/links; mapper leaves markers.
- Dream worm synthesizes ephemeral payloads; bulldozer overwrites as it crawls.

## Notes
- Keep lore/variants as flavor (YAML jazz) without duplicating standard fields.
- Use K-line ads; keep header minimal; stash richer context in flavor/variants.
