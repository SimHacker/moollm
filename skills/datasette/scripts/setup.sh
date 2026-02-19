#!/usr/bin/env bash
# Set up datasette skill venv with Python 3.14+.
# Usage: bash scripts/setup.sh
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SKILL_ROOT"

PYTHON=""
for candidate in python3.14 python3.13 python3; do
    if command -v "$candidate" &>/dev/null; then
        ver=$("$candidate" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        major=$(echo "$ver" | cut -d. -f1)
        minor=$(echo "$ver" | cut -d. -f2)
        if [ "$major" -ge 3 ] && [ "$minor" -ge 13 ]; then
            PYTHON="$candidate"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo "ERROR: Python 3.13+ required. Install with: brew install python@3.14"
    exit 1
fi

echo "Using: $PYTHON ($($PYTHON --version))"

if [ ! -d .venv ]; then
    echo "Creating venv..."
    "$PYTHON" -m venv .venv
fi

echo "Installing dependencies..."
.venv/bin/pip install -q -r requirements.txt

echo ""
echo "Setup complete. Activate with:"
echo "  source $SKILL_ROOT/.venv/bin/activate"
echo ""
echo "Then run:"
echo "  datasette --help"
echo "  datasette path/to/database.db -o"
