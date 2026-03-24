# Ensure skill root is on path so lib is importable when running pytest from skills/moo.
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))
