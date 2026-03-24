#!/usr/bin/env python3
"""moo.py — Moo virtual machine CLI.

GitHub branches as structured object storage. Each branch is a moo (ClassName_ObjectID).
Uses `gh api`. Repos and overlay examples live in the moocroworld skill (REPOS.yml there).

Ephemeral file cache: .moollm/skills/moo/cache/ — per repo/branch/file, whole file;
loaded on first use, saved at exit. Fast random access after first touch.

Usage: moo repos | resolve | ls | tree | read | sniff | glance | card | scan | write | rm | batch-glance | focus
Env: MOO_REPO, MOO_REPOS_FILE (default resolves to moocroworld).

Library: Logic lives in lib/ (config, storage, urls, sniff, overlay, gh, cache, util, why).
Import for programmatic use: add skills/moo to path, then from lib import storage, config, urls, ...
"""

import sys
from pathlib import Path

# Ensure skill root is on path so lib is importable (whether run as script or -m)
_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from lib.cli import main

if __name__ == "__main__":
    main()
