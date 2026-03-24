#!/usr/bin/env python3
"""Thin wrapper: run the moo skill CLI. The moo virtual machine lives in skills/moo/."""

import runpy
import sys
from pathlib import Path

if __name__ == "__main__":
    moo_py = Path(__file__).resolve().parent.parent / "moo" / "moo.py"
    if not moo_py.exists():
        sys.exit("moo skill not found: skills/moo/moo.py")
    sys.argv[0] = str(moo_py)
    runpy.run_path(str(moo_py), run_name="__main__")
