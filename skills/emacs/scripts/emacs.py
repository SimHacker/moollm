#!/usr/bin/env python3
"""MOOLLM Emacs sister script: emacsclient router with JSON-shaped results.

Routes ``emacsclient`` calls to a named target from ``servers.yml`` (socket or
default), appends eval lines to ``logs/command-log.jsonl`` unless ``--quiet``,
and prints JSON for machine-readable status.

Usage::

    emacs.py status
    emacs.py eval '(emacs-pid)' [--target NAME] [--quiet]
    emacs.py target list|current|use NAME
    emacs.py speak TEXT   # stub
    emacs.py url emacs://...   # stub message passthrough

Environment: ``EMACSCLIENT`` binary, ``MOO_EMACS_TARGET`` default target override.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

# --- CONSTANTS

DEFAULT_SERVERS = Path.home() / ".emacs.d" / "moo" / "servers.yml"
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
COMMAND_LOG = LOG_DIR / "command-log.jsonl"

# --- CLI


def build_parser() -> argparse.ArgumentParser:
    """Build the full ``argparse`` tree (``emacs.py --help``)."""
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument(
        "--servers",
        type=Path,
        default=DEFAULT_SERVERS,
        help=f"path to servers.yml (default {DEFAULT_SERVERS})",
    )

    p = argparse.ArgumentParser(description="MOO Emacs sister script (emacsclient router)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("status", parents=[parent], help="daemon / config overview")
    sp.set_defaults(handler="status")

    sp = sub.add_parser("eval", parents=[parent], help="run elisp via emacsclient --eval")
    sp.add_argument("expr", help="elisp expression")
    sp.add_argument("--target", "-t", help="target name")
    sp.add_argument("--quiet", "-q", action="store_true", help="skip command log")
    sp.set_defaults(handler="eval")

    sp = sub.add_parser("target", parents=[parent], help="manage targets")
    tp = sp.add_subparsers(dest="tcmd", required=True)
    t1 = tp.add_parser("list", parents=[parent])
    t1.set_defaults(handler="target_list")
    t2 = tp.add_parser("current", parents=[parent])
    t2.set_defaults(handler="target_current")
    t3 = tp.add_parser("use", parents=[parent])
    t3.add_argument("name")
    t3.set_defaults(handler="target_use")

    sp = sub.add_parser("speak", parents=[parent], help="spoken command (placeholder)")
    sp.add_argument("text")
    sp.set_defaults(handler="speak")

    sp = sub.add_parser("url", parents=[parent], help="pass emacs:// url to resolver (stub)")
    sp.add_argument("emacs_url")
    sp.set_defaults(handler="url")

    return p


def main(argv: Optional[list[str]] = None) -> int:
    """Parse ``argv`` (default ``sys.argv``) and run the selected subcommand."""
    args = build_parser().parse_args(argv)
    return dispatch(args)


def dispatch(args: argparse.Namespace) -> int:
    """Run the handler named by ``args.handler``."""
    h = args.handler
    if h == "status":
        cmd_status(args.servers)
        return 0
    if h == "eval":
        result = run_eval(
            args.expr,
            target=args.target,
            servers_path=args.servers,
            quiet=args.quiet,
        )
        print(json.dumps(result, indent=2))
        return 0
    if h == "target_list":
        cmd_target_list(args.servers)
        return 0
    if h == "target_current":
        cmd_target_current(args.servers)
        return 0
    if h == "target_use":
        return cmd_target_use(args.name, args.servers)
    if h == "speak":
        cmd_speak(args.text)
        return 0
    if h == "url":
        cmd_url(args.emacs_url, args.servers)
        return 0
    raise RuntimeError(f"unknown handler {h!r}")


# --- PRIVATE HELPERS


def _utc_now() -> str:
    """Return current UTC time as ISO 8601 string."""
    return datetime.now(timezone.utc).isoformat()


def _append_log(entry: dict[str, Any]) -> None:
    """Append one JSON object as a line to ``COMMAND_LOG``."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry, ensure_ascii=False) + "\n"
    with COMMAND_LOG.open("a", encoding="utf-8") as fh:
        fh.write(line)


def _emacsclient_path() -> str:
    """Resolve ``emacsclient`` binary (``EMACSCLIENT`` or default name)."""
    return os.environ.get("EMACSCLIENT", "emacsclient")


def _load_servers(path: Path) -> dict[str, Any]:
    """Load ``servers.yml``; return default structure if missing."""
    if not path.exists():
        return {"current": "local", "targets": {}}
    raw = path.read_text(encoding="utf-8")
    if yaml is None:
        raise SystemExit("PyYAML is required to read servers.yml (pip install pyyaml)")
    data = yaml.safe_load(raw)
    return data if isinstance(data, dict) else {}


def _socket_args(target_name: str, servers: dict[str, Any]) -> list[str]:
    """Return ``emacsclient -s SOCKET`` fragment for a socket-type target, or []."""
    targets = servers.get("targets") or {}
    t = targets.get(target_name) or {}
    conn = t.get("connection") or {}
    if conn.get("type") == "socket":
        sock = conn.get("socket")
        if sock:
            return ["-s", str(sock)]
    return []


# --- CORE


def run_eval(
    expr: str,
    *,
    target: Optional[str],
    servers_path: Path,
    quiet: bool,
) -> dict[str, Any]:
    """Run Elisp ``expr`` via ``emacsclient -n [--eval]``; optionally log the call."""
    servers = _load_servers(servers_path)
    name = target or os.environ.get("MOO_EMACS_TARGET") or servers.get("current") or "local"
    sock = _socket_args(str(name), servers)
    argv = [_emacsclient_path(), "-n", *sock, "--eval", expr]
    proc = subprocess.run(argv, capture_output=True, text=True)
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    result: dict[str, Any] = {
        "ok": proc.returncode == 0 and not err,
        "returncode": proc.returncode,
        "stdout": out,
        "stderr": err,
        "target": name,
    }
    if not quiet:
        _append_log(
            {
                "ts": _utc_now(),
                "kind": "eval",
                "target": name,
                "expr": expr,
                "result": result,
            }
        )
    return result


# --- SUBCOMMANDS


def cmd_status(servers_path: Path) -> None:
    """Print JSON: servers file, current target, emacsclient path, ``(emacs-pid)`` eval."""
    servers = _load_servers(servers_path)
    cur = servers.get("current")
    r = run_eval("(emacs-pid)", target=cur, servers_path=servers_path, quiet=True)
    print(
        json.dumps(
            {
                "servers_file": str(servers_path),
                "current": cur,
                "emacsclient": _emacsclient_path(),
                "pid_eval": r,
            },
            indent=2,
        )
    )


def cmd_target_list(servers_path: Path) -> None:
    """Print the full parsed ``servers`` document as JSON."""
    servers = _load_servers(servers_path)
    print(json.dumps(servers, indent=2))


def cmd_target_current(servers_path: Path) -> None:
    """Print the current target name (plain text, one line)."""
    servers = _load_servers(servers_path)
    print(servers.get("current", ""))


def cmd_target_use(name: str, servers_path: Path) -> int:
    """Set ``current`` target in ``servers_path`` and persist YAML."""
    if yaml is None:
        print("PyYAML required for target use", file=sys.stderr)
        return 1
    servers = _load_servers(servers_path)
    servers["current"] = name
    servers_path.parent.mkdir(parents=True, exist_ok=True)
    servers_path.write_text(yaml.safe_dump(servers, sort_keys=False), encoding="utf-8")
    print(f"current target -> {name}")
    return 0


def cmd_speak(text: str) -> None:
    """Placeholder: spoken command pipeline not wired; echo JSON stub."""
    print(
        json.dumps(
            {
                "ok": False,
                "message": "speak: grammar loader not yet wired; text recorded",
                "text": text,
            },
            indent=2,
        )
    )


def cmd_url(url: str, servers_path: Path) -> None:
    """Stub: send URL as a ``message`` into Emacs via ``run_eval``."""
    expr = f'(message "{url.replace(chr(34), chr(92)+chr(34))}")'
    r = run_eval(expr, target=None, servers_path=servers_path, quiet=False)
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
