#!/usr/bin/env bash
# Set up showboat skill venv with Python 3.14+ and all ecosystem tools.
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

echo "Installing Python dependencies (chartroom, datasette-showboat)..."
.venv/bin/pip install -q -r requirements.txt

# Showboat and Rodney are Go binaries; uvx handles them without a venv.
# Verify they're accessible:
echo ""
echo "Checking CLI tools (via uvx)..."
if command -v uvx &>/dev/null; then
    echo "  uvx: OK"
    echo "  showboat: run 'uvx showboat --help' to use"
    echo "  rodney: run 'uvx rodney --help' to use"
    echo "  chartroom: run 'uvx chartroom --help' to use"
else
    echo "  uvx not found. Install uv first: curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "  Then: uvx showboat --help"
fi

echo ""
echo "Setup complete. Activate with:"
echo "  source $SKILL_ROOT/.venv/bin/activate"
echo ""
echo "Quick start:"
echo "  uvx showboat init demo.md 'My Demo'"
echo "  uvx showboat exec demo.md bash 'echo hello world'"
echo "  uvx showboat note demo.md 'It works!'"
