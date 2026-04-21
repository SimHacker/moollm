---
name: emacs
description: GNU Emacs as a stateful Lisp machine for agents — daemon, moo-* protocol, emacs.py router, emacs:// URLs, spoken grammar, play-learn-lift.
allowed-tools: [read, grep, glob, run_terminal_cmd]
related: [sister-script, play-learn-lift, yaml-jazz, cursor-mirror, robust-first]
license: MIT
---

# Emacs (MOO)

## What this skill is

GNU Emacs with `emacs --daemon` is a **long-lived evaluator**: buffers, modes, and elisp are the program. Agents and humans share **persistent context** (open files, marks, narrowing, undo). The **sister script** `scripts/emacs.py` adapts `emacsclient` for tools: **JSON-shaped results**, **named targets**, **batching**, **logging**, and **`emacs://`** routing.

This is **not** a thin “run one shell command” wrapper. The value is the **protocol**: what to return after each operation, how to name multiple daemons, how speech and intent map to elisp.

## Three interaction tiers

1. **Intent** — `(moo-rename-symbol "a" "b" :scope 'project)` style (to be implemented in elisp; names in CARD).
2. **Structural** — `(moo-in-defun "foo" ...)` , `(moo-try BODY)` with `atomic-change-group`.
3. **Raw elisp** — `(emacs.py eval "(+ 1 2)")` or direct `emacsclient --eval`.

## Sister script: `scripts/emacs.py`

Subcommands (see `--help`):

- `status` — daemon up, current target
- `eval SEXP` — evaluate, print JSON `{ok, value, error}` where possible
- `target list | current | use NAME` — `~/.emacs.d/moo/servers.yml`
- `speak TEXT` — placeholder: will use `spoken-grammar.yml` + optional local LLM
- `url EMACS_URL` — resolve and dispatch (staged implementation)

Environment:

- `EMACSCLIENT` — path to emacsclient (default: `emacsclient`)
- `MOO_EMACS_TARGET` — default target name

Logs: append JSON lines to `.moollm/skills/emacs/logs/command-log.jsonl` when run from a MOOLLM workspace.

## Elisp side (templates/)

Install copies under `~/.emacs.d/moo/` (see `templates/init.el`):

- `moo-protocol.el` — `moo-with-effects`, standard result plist
- `moo-structural.el` — structural helpers
- `moo-oneshot.el` — oneshot define / log / promote
- `moo-macros.el` — macro capture and schema export hooks

## Integration

- **play-learn-lift** — oneshot log + macro list + command-log.jsonl
- **cursor-mirror** — optional: correlate agent edits with Emacs log
- **yaml-jazz** — `spoken-grammar.yml` comments carry semantics

## Cursor prompt / aiService snapshot

Optional: [reference/cursor-aiService-prompts.yaml](reference/cursor-aiService-prompts.yaml) holds `aiService.prompts` and `aiService.generations` from the workspace DB (see [reference/README.md](reference/README.md)). Regenerate with `cursor-mirror export-prompts <workspace-id> -o …`.

## Part of MOOLLM

Repo [README](../../README.md), [skills/README.md](../README.md).
