# YAML/JSON and small helpers. No moo-specific deps.

import json

try:
    import yaml
except ImportError:
    yaml = None


def yaml_load(text):
    if yaml:
        return yaml.safe_load(text)
    return json.loads(text)


def yaml_dump(data):
    if yaml:
        return yaml.dump(data, default_flow_style=False).rstrip()
    return json.dumps(data, indent=2)


def apply_line_range(text, line_start, line_end):
    """Return lines line_start..line_end (1-based inclusive)."""
    lines = text.splitlines()
    if not lines:
        return ""
    lo = max(0, line_start - 1)
    hi = min(len(lines), line_end)
    return "\n".join(lines[lo:hi])
