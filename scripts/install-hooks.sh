#!/usr/bin/env bash
#
# Install git hooks for moollm repository
#
# Run: ./scripts/install-hooks.sh
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "Installing git hooks..."

# Pre-commit hook
if [ -f "$HOOKS_DIR/pre-commit" ]; then
    echo "  Backing up existing pre-commit hook..."
    mv "$HOOKS_DIR/pre-commit" "$HOOKS_DIR/pre-commit.backup.$(date +%s)"
fi

cp "$SCRIPT_DIR/pre-commit" "$HOOKS_DIR/pre-commit"
chmod +x "$HOOKS_DIR/pre-commit"
echo "  ✓ Installed pre-commit hook (YAML + JSON validation)"

echo ""
echo "Done! Hooks will run automatically on git commit."
echo ""
echo "To test manually:"
echo "  git add some-file.yml"
echo "  git commit -m 'test'"
