import json
import os
import sys

from .. import config
from .. import urls


def cmd_resolve(url, repos_config, why=None):
    parsed = urls.parse_moo_url(url)
    if not parsed:
        print("Invalid moorl. Use moo:// or moollm://.", file=sys.stderr)
        sys.exit(1)
    path_str, line_start, line_end = urls.parse_fragment(parsed.get("fragment", "") or "")
    out = {
        "scheme": parsed["scheme"],
        "repo": parsed["repo"],
        "branch": parsed["branch"],
        "path": parsed["path"] or None,
        "fragment_key_path": path_str or None,
        "fragment_line_start": line_start,
        "fragment_line_end": line_end,
        "query": parsed["query"] or None,
    }
    if parsed["scheme"] == "moo" and repos_config:
        default_repo = os.environ.get("MOO_REPO")
        if default_repo:
            out["resolved_repo"] = default_repo
    print(json.dumps(out, indent=2))
