# Emacs skill — design

## Vision

GNU Emacs is a **Lisp machine** that happens to edit text. The daemon keeps **state**; elisp is the API. Agents supply **intent**; Emacs supplies **structure** (defuns, modes, narrowing, undo, TRAMP). Calling this a “buffer tool” understates the surface: the **session** (open buffers, windows, registers, kill ring) is shared **working memory** — a K-line in MOOLLM terms.

## Historical frame

- **NeWS / MOOWS**: Push **code** to a long-lived interpreter; the display is a consequence. Emacs matches that shape: push elisp, not opaque pixels.
- **AJAX**: Client thin, server holds truth. Here the “server” is often **local Emacs**; TRAMP extends the same idea remotely.
- **Programming by demonstration**: Keyboard macros and logged one-shots feed **play → learn → lift** toward reusable `moo-*` functions and Drescher-style schema candidates.

## Protocol: Python ↔ Emacs

- **emacsclient** returns printed elisp values; errors are easy to mis-read in raw terminal output.
- **emacs.py** wraps calls, returns **JSON**, handles **escaping**, optional **batch** of sexps, and **exit status** interpretation.
- **Elisp** should return **structured plists** where possible (`:ok`, `:value`, `:effects`, `:buffers`) — see `templates/moo-protocol.el`.

Bidirectional **logging** (command + result) enables audit and play-learn-lift analysis without replacing Emacs’s own undo.

## emacs:// URLs

Treat URLs as **attention paths** (like `cd` on a Lisp machine):

- `emacs://TARGET` — whole daemon / default buffer context
- `emacs://TARGET/path/to/file` — buffer for file
- Further segments can narrow (defun, class, line) — **resolver lives in elisp**; Python passes the URL through after target lookup.

Emacs may **emit** URLs to an LLM (e.g. `moo-ask`) so the model receives a **structural address**, not a screenshot.

## Targets (multi-Emacs)

`~/.emacs.d/moo/servers.yml` lists **named** instances (socket path, optional TCP/tunnel, workspaces, tags), plus **`current`**. Same UX family as `kubectl context` / `gcloud config configurations`.

`emacsclient` supports **`-s socket-name`** locally; multiple daemons are separate sockets. Remote access typically uses **SSH** (TRAMP, or tunnel to a TCP server). Authentication is **whatever SSH or your admin** provides — the sister script does not invent a crypto protocol; it **documents** how to point a target at a tunnel or socket.

## Speech and accessibility

Tiered **spoken grammar** (see `spoken-grammar.yml`):

1. Intent (fuzzy NL)
2. Structural (semi-formal)
3. Keystroke names (“control x control s”)
4. Spoken elisp (rare)

A **local** small LLM can normalize messy dictation to `emacs.py` commands or elisp; exact matches can skip the model. **RMS-style** explicit “meta”, “control”, “escape” words remain the low-ambiguity layer.

## Router, not only client

`emacs.py` is a **router**: Emacs may invoke it to reach **another** daemon or to loop through the same one for **logging and effects**. Operations that pass the router are **observable** in `command-log.jsonl`.

## Files in this skill

| File | Role |
|------|------|
| GLANCE.yml | Fast orientation |
| CARD.yml | Methods and layout |
| SKILL.md | Protocol and commands |
| spoken-grammar.yml | Data-driven grammar + YAML Jazz |
| scripts/emacs.py | Sister script |
| templates/*.el | Installable elisp stubs |
| templates/servers.yml.example | Target config example |
