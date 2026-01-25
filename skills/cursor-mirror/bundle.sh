#!/bin/bash
# bundle.sh — Create cursor-mirror distribution bundle
#
# Usage: ./bundle.sh [version]
#
# Run from moollm repo root:
#   ./skills/cursor-mirror/bundle.sh 1.0.0-alpha
#
# Or from skills/cursor-mirror:
#   ./bundle.sh 1.0.0-alpha

set -e

# Determine repo root
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [[ "$SCRIPT_DIR" == */skills/cursor-mirror ]]; then
    REPO_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
else
    REPO_ROOT="$(pwd)"
fi

cd "$REPO_ROOT"

# Version from arg or default
VERSION="${1:-1.0.0-alpha}"
BUNDLE_NAME="cursor-mirror-bundle-${VERSION}"
DIST_DIR="dist"
DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "═══════════════════════════════════════════════════════════════════════════"
echo "  Cursor Mirror Bundle Creator"
echo "  Version: ${VERSION}"
echo "  Date: ${DATE}"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

# Skills to include (in dependency order)
SKILLS=(
    "cursor-mirror"           # Primary
    "skill-snitch"            # Required
    "thoughtful-commitment"   # Recommended
    "trekify"                 # Recommended
    "session-log"             # Optional
    "sister-script"           # Methodology
    "sniffable-python"        # Methodology
    "play-learn-lift"         # Methodology
    "k-lines"                 # Protocol
)

# Create dist directory
mkdir -p "${DIST_DIR}"

# Create temporary directory for bundle structure
TEMP_DIR=$(mktemp -d)
BUNDLE_DIR="${TEMP_DIR}/${BUNDLE_NAME}"
mkdir -p "${BUNDLE_DIR}/skills"

echo "📦 Bundling skills..."
echo ""

# Copy skills
for skill in "${SKILLS[@]}"; do
    if [ -d "skills/${skill}" ]; then
        cp -r "skills/${skill}" "${BUNDLE_DIR}/skills/"
        
        # Count files
        FILE_COUNT=$(find "${BUNDLE_DIR}/skills/${skill}" -type f | wc -l | tr -d ' ')
        
        echo "  ✓ skills/${skill} (${FILE_COUNT} files)"
    else
        echo "  ⚠ skills/${skill} NOT FOUND — skipping"
    fi
done

echo ""
echo "📄 Creating bundle files..."

# Copy README-EXPORT.md as README.md
if [ -f "skills/cursor-mirror/README-EXPORT.md" ]; then
    cp "skills/cursor-mirror/README-EXPORT.md" "${BUNDLE_DIR}/README.md"
    echo "  ✓ README.md (from README-EXPORT.md)"
else
    echo "  ⚠ README-EXPORT.md not found — creating minimal README"
    cat > "${BUNDLE_DIR}/README.md" << 'EOF'
# Cursor Mirror Bundle

See skills/cursor-mirror/README.md for documentation.

## Quick Start

```bash
python3 skills/cursor-mirror/cursor_mirror.py status
python3 skills/cursor-mirror/cursor_mirror.py --help
```
EOF
fi

# Copy LICENSE
if [ -f "skills/cursor-mirror/LICENSE" ]; then
    cp "skills/cursor-mirror/LICENSE" "${BUNDLE_DIR}/LICENSE"
    echo "  ✓ LICENSE"
else
    # Create MIT license
    cat > "${BUNDLE_DIR}/LICENSE" << EOF
MIT License

Copyright (c) 2026 Don Hopkins, Leela AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
    echo "  ✓ LICENSE (generated)"
fi

# Generate MANIFEST.yml
cat > "${BUNDLE_DIR}/MANIFEST.yml" << EOF
# Cursor Mirror Bundle Manifest
# Generated: ${DATE}

bundle:
  name: ${BUNDLE_NAME}
  version: ${VERSION}
  source: "https://github.com/leela-ai/moollm"
  created: "${DATE}"

skills:
EOF

for skill in "${SKILLS[@]}"; do
    if [ -d "${BUNDLE_DIR}/skills/${skill}" ]; then
        echo "  - ${skill}" >> "${BUNDLE_DIR}/MANIFEST.yml"
    fi
done

cat >> "${BUNDLE_DIR}/MANIFEST.yml" << 'EOF'

primary_skill: cursor-mirror

dependency_tiers:
  required:
    - skill-snitch
  recommended:
    - thoughtful-commitment
    - trekify
  optional:
    - session-log
  methodology:
    - sister-script
    - sniffable-python
    - play-learn-lift
    - k-lines

usage: |
  # Quick status check
  python3 skills/cursor-mirror/cursor_mirror.py status
  
  # Full help
  python3 skills/cursor-mirror/cursor_mirror.py --help
  
  # Browse conversations
  python3 skills/cursor-mirror/cursor_mirror.py tree
  
  # Watch yourself think
  python3 skills/cursor-mirror/cursor_mirror.py thinking @1

part_of: "MOOLLM — https://github.com/leela-ai/moollm"

note: |
  This bundle is extracted from MOOLLM, a skill framework that builds on
  and extends the Anthropic skill standard. These skills work standalone
  but have additional features when used within full MOOLLM.
EOF

echo "  ✓ MANIFEST.yml"

# Create ECOSYSTEM.md
cat > "${BUNDLE_DIR}/ECOSYSTEM.md" << 'EOF'
# The MOOLLM Ecosystem

This bundle is a portable extract from **MOOLLM** — a skill framework that builds on
and extends the Anthropic skill standard.

## What You're Missing

Without full MOOLLM, these features are unavailable:

| Feature | What It Does |
|---------|--------------|
| **Instantiation** | Skills as prototypes that create configured instances |
| **Three-Tier Persistence** | Platform → Narrative → State separation |
| **K-line Activation** | Saying a protocol name activates related knowledge |
| **Hot/Cold Memory** | Advisory hints for context management |
| **Empathic Templates** | Smart generation, not string substitution |
| **Speed of Light** | Many agents, many turns, one LLM call |
| **CARD.yml** | Machine-readable interfaces with advertisements |
| **Ethical Framing** | Room-based inheritance of performance context |

## MOOLLM's Eight Extensions

1. **Instantiation** — Skills as prototypes that create instances
2. **Three-Tier Persistence** — Platform → Narrative → State
3. **K-lines** — Names that activate knowledge constellations (Minsky)
4. **Hot/Cold Memory** — Advisory context hints (working-set, hot.yml, cold.yml)
5. **Empathic Templates** — Smart generation, not string substitution
6. **Speed of Light** — Many agents, many turns, one LLM call
7. **CARD.yml** — Machine-readable interfaces with advertisements
8. **Ethical Framing** — Room-based inheritance of performance context

## Try Full MOOLLM

```bash
git clone https://github.com/leela-ai/moollm.git
cd moollm

# Read the architecture
cat kernel/README.md

# Browse all skills (60+)
cat skills/INDEX.yml

# Bootstrap a session
# (in Cursor) "boot moollm"
```

## The Skill Skill

The `skill` skill teaches you how to create your own skills using the 
**play-learn-lift** methodology:

1. **PLAY** — Explore freely, try things, make mistakes
2. **LEARN** — Notice patterns, document what works
3. **LIFT** — Share wisdom, create reusable skills

cursor-mirror was built this way: exploring Cursor's internals, documenting
patterns, then lifting into a reusable introspection tool.

## Philosophy

> *"The orchestrator is the Operating System. The LLM is the Coherence Engine. 
> The Repo is the Microworld."*

MOOLLM is inspired by:
- **Seymour Papert** — Microworlds, constructionism
- **Marvin Minsky** — Society of Mind, K-lines
- **Dave Ackley** — Robust-first computing
- **The Self Language** — Prototypes and delegation

## Links

- Repository: https://github.com/leela-ai/moollm
- Leela AI: https://leela.ai
EOF

echo "  ✓ ECOSYSTEM.md"

echo ""
echo "📦 Creating tarball..."

# Create tarball
tar -czf "${DIST_DIR}/${BUNDLE_NAME}.tar.gz" -C "${TEMP_DIR}" "${BUNDLE_NAME}"

# Get size
SIZE=$(ls -lh "${DIST_DIR}/${BUNDLE_NAME}.tar.gz" | awk '{print $5}')

# Cleanup
rm -rf "${TEMP_DIR}"

echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  ✅ Bundle Created Successfully"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "  Output: ${DIST_DIR}/${BUNDLE_NAME}.tar.gz"
echo "  Size:   ${SIZE}"
echo ""
echo "  Skills included:"
for skill in "${SKILLS[@]}"; do
    echo "    • ${skill}"
done
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  Distribution"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "  1. Upload to GitHub releases:"
echo "     gh release create v${VERSION} ${DIST_DIR}/${BUNDLE_NAME}.tar.gz"
echo ""
echo "  2. Share the download link"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  Installation (for users)"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "  tar -xzf ${BUNDLE_NAME}.tar.gz"
echo "  cd ${BUNDLE_NAME}"
echo "  python3 skills/cursor-mirror/cursor_mirror.py status"
echo ""
