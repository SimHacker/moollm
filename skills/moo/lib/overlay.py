# Attention-tree overlay: load YAML, expand globs. Focus/batch-glance use this.

import fnmatch
import json
from pathlib import Path

from . import config
from . import gh
from . import util


def load_overlay(path, repos_config):
    """Load attention-tree overlay YAML. Resolve repo aliases to owner/name."""
    with open(path) as f:
        raw = util.yaml_load(f.read())
    if not raw:
        return {"repos": [], "defaults": {}}
    defaults = raw.get("defaults", {})
    repos = []
    for entry in raw.get("repos", []):
        repo_spec = entry.get("repo")
        if not repo_spec:
            continue
        gh_name, _ = config.resolve_repo(repo_spec, repos_config)
        repo_name = gh_name or repo_spec
        repos.append({
            "repo": repo_name,
            "type": entry.get("type"),
            "depth": entry.get("depth", defaults.get("depth", 1)),
            "at_depth": {int(k): v for k, v in (entry.get("at_depth") or defaults.get("at_depth") or {0: ["GLANCE.yml"]}).items()},
            "fragments": entry.get("fragments") or {},
        })
    return {"repos": repos, "defaults": defaults}


def expand_globs(repo, branch, patterns, token_env):
    """Return list of file paths on branch that match any of the glob patterns."""
    result = gh.gh_api(f"repos/{repo}/git/trees/{branch}?recursive=1", token_env=token_env)
    if not result:
        return []
    try:
        tree = json.loads(result)
        paths = [n["path"] for n in tree.get("tree", []) if n.get("type") == "blob"]
    except Exception:
        return []
    out = []
    for pat in patterns:
        if "*" in pat or "?" in pat:
            out.extend(p for p in paths if fnmatch.fnmatch(p, pat))
        else:
            if pat in paths:
                out.append(pat)
    return sorted(set(out))


def default_overlay_path():
    """Default overlay: moocroworld's ATTENTION-TREE.example.yml."""
    moo_dir = Path(__file__).resolve().parent.parent
    candidates = [
        moo_dir.parent / "moocroworld" / "ATTENTION-TREE.example.yml",
        Path("skills/moocroworld/ATTENTION-TREE.example.yml"),
        Path.cwd() / "skills" / "moocroworld" / "ATTENTION-TREE.example.yml",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None
