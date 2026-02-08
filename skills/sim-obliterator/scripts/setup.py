#!/usr/bin/env python3
"""
sim-obliterator SETUP — cross-platform (macOS, Linux, Windows)
Idempotent. Run as many times as you want. Skips what's already done.

Usage: python3 setup.py [path-to-sister-repo]
Default: ../SimObliterator_Suite (sibling of moollm)
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

GIT_URL = "https://github.com/DnfJeff/SimObliterator_Suite.git"

def run(cmd, **kwargs):
    """Run a command, return (success, output)."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
        return result.returncode == 0, result.stdout.strip() + result.stderr.strip()
    except FileNotFoundError:
        return False, f"Command not found: {cmd[0]}"

def venv_python(venv_dir):
    """Path to python inside the venv, cross-platform."""
    if sys.platform == "win32":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"

def venv_pip(venv_dir):
    """Path to pip inside the venv, cross-platform."""
    if sys.platform == "win32":
        return venv_dir / "Scripts" / "pip.exe"
    return venv_dir / "bin" / "pip"

def main():
    script_dir = Path(__file__).resolve().parent
    moollm_root = script_dir.parent.parent.parent
    sister_default = moollm_root.parent / "SimObliterator_Suite"

    sister_repo = Path(sys.argv[1]) if len(sys.argv) > 1 else sister_default
    sister_repo = sister_repo.resolve()
    venv_dir = sister_repo / ".venv"
    requirements = sister_repo / "requirements.txt"
    src_dir = sister_repo / "src"

    print("=== sim-obliterator SETUP ===")
    print(f"platform:     {sys.platform}")
    print(f"moollm root:  {moollm_root}")
    print(f"sister repo:  {sister_repo}")
    print(f"venv:         {venv_dir}")
    print()

    # STEP 1: Prerequisites
    print("[1/5] Checking prerequisites...")

    print(f"  python: {sys.version.split()[0]} at {sys.executable}")

    ok, out = run(["git", "--version"])
    if not ok:
        print("  ERROR: git not found.")
        print("    macOS:   brew install git")
        print("    Ubuntu:  sudo apt install git")
        print("    Windows: https://git-scm.com/download/win")
        sys.exit(1)
    print(f"  git: {out.strip()}")

    try:
        import venv as _venv
        print("  venv module: available")
    except ImportError:
        print("  ERROR: venv module not available.")
        print("    macOS:   brew install python3  (includes venv)")
        print("    Ubuntu:  sudo apt install python3-venv")
        print("    Windows: reinstall Python from python.org with 'Add to PATH' checked")
        sys.exit(1)
    print()

    # STEP 2: Clone sister repo
    print("[2/5] Checking sister repo...")

    git_dir = sister_repo / ".git"
    if git_dir.is_dir():
        print(f"  SKIP: already cloned at {sister_repo}")
        ok, branch = run(["git", "branch", "--show-current"], cwd=sister_repo)
        ok2, commit = run(["git", "log", "-1", "--format=%h %s"], cwd=sister_repo)
        if ok: print(f"  branch: {branch}")
        if ok2: print(f"  latest: {commit}")
    elif sister_repo.is_dir():
        print(f"  WARNING: {sister_repo} exists but is not a git repo")
        print("  Continuing — assuming manual placement.")
    else:
        print(f"  Cloning from {GIT_URL} ...")
        ok, out = run(["git", "clone", GIT_URL, str(sister_repo)])
        if not ok:
            print(f"  ERROR: git clone failed:\n{out}")
            sys.exit(1)
        print("  Cloned.")

    if not src_dir.is_dir():
        print(f"  ERROR: {src_dir} not found.")
        print(f"  Expected: {sister_repo}/src/formats/iff/iff_file.py")
        sys.exit(1)
    print("  src/ directory found")
    print()

    # STEP 3: Create venv
    print("[3/5] Checking venv...")

    py = venv_python(venv_dir)
    if py.is_file():
        print(f"  SKIP: venv exists at {venv_dir}")
        ok, ver = run([str(py), "--version"])
        if ok: print(f"  venv python: {ver}")
    else:
        if venv_dir.is_dir():
            print(f"  WARNING: {venv_dir} exists but looks broken. Recreating...")
            shutil.rmtree(venv_dir)
        print("  Creating venv...")
        ok, out = run([sys.executable, "-m", "venv", str(venv_dir)])
        if not ok:
            print(f"  ERROR: venv creation failed:\n{out}")
            sys.exit(1)
        print("  Created.")
    print()

    # STEP 4: Install dependencies
    print("[4/5] Installing dependencies...")

    pip = venv_pip(venv_dir)
    if not requirements.is_file():
        print(f"  WARNING: {requirements} not found. Skipping pip install.")
    else:
        # Upgrade pip
        run([str(pip), "install", "--upgrade", "pip", "--quiet"])

        # Install requirements
        print("  Running pip install -r requirements.txt ...")
        ok, out = run([str(pip), "install", "-r", str(requirements)])
        if not ok:
            print("  WARNING: Some packages failed to install.")
            print("  This is often OK — DearPyGUI and GUI deps may not build everywhere.")
            print("  The IFF parser (what we need) usually installs fine.")
            # Show last few lines
            lines = out.strip().split("\n")
            for line in lines[-5:]:
                print(f"    {line}")
        else:
            if "Successfully installed" in out:
                print("  New packages installed.")
            else:
                print("  All packages already installed.")
    print()

    # STEP 5: Verify imports
    # tkinter is no longer required for headless use. The BHAV editor
    # (the only tkinter consumer) is lazy-loaded in chunks/__init__.py,
    # so importing chunk parsers like NBRS, FAMI, STR works without
    # a display server or tkinter installed.
    print("[5/5] Verifying SimObliterator imports...")

    verify_script = f"""
import sys
sys.path.insert(0, {str(src_dir)!r})
checks = [
    ("IffFile", "from formats.iff.iff_file import IffFile"),
    ("PersonalityTraits", "from formats.iff.chunks.char import PersonalityTraits"),
    ("NBRS", "from formats.iff.chunks.nbrs import NBRS"),
]
failed = False
for name, imp in checks:
    try:
        exec(imp)
        print(f"  OK: {{name}} imported")
    except ImportError as e:
        if name == "IffFile":
            print(f"  ERROR: {{name}} failed: {{e}}")
            failed = True
        else:
            print(f"  WARNING: {{name}} not available (optional)")
if failed:
    sys.exit(1)
"""
    ok, out = run([str(py), "-c", verify_script])
    print(out)
    if not ok:
        print()
        print("SETUP FAILED: SimObliterator core imports did not work.")
        print(f"Check that {src_dir} contains the expected Python modules.")
        sys.exit(1)
    print()

    # DONE
    print("=== SETUP COMPLETE ===")
    print()
    print("SimObliterator is ready. The CLI entry point is obliterator.py:")
    print()
    obliterator = sister_repo / "obliterator.py"
    if obliterator.is_file():
        print(f"  {obliterator}")
    else:
        print(f"  (not found — expected at {obliterator})")
    print()
    print("Quick start:")
    print(f"  python3 {obliterator} --help")
    print(f"  python3 {obliterator} inspect <Neighborhood.iff>")
    print(f"  python3 {obliterator} character <Neighborhood.iff> 'Bella Goth'")
    print(f"  python3 {obliterator} iff-info <any-file.iff>")
    print(f"  python3 {obliterator} far-list <archive.far>")
    print(f"  python3 {obliterator} uplift <Neighborhood.iff> 'Mortimer' -o mortimer.yml")
    print()

if __name__ == "__main__":
    main()
