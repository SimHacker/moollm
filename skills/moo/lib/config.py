# REPOS resolution: find REPOS.yml, load repos, resolve alias -> owner/name.

import os
from pathlib import Path

from . import util


# REPOS: user-level only under ~/.moollm (spans repos). Override with MOO_REPOS_FILE.
# We do not use repo_root/.moollm so config is explicit: user vs repo.

def find_repos_file():
    explicit = os.environ.get("MOO_REPOS_FILE")
    if explicit:
        return Path(explicit)
    home_moollm = Path.home() / ".moollm" / "skills"
    for name in ("moo", "moocroworld"):
        p = home_moollm / name / "REPOS.yml"
        if p.exists():
            return p
    return None


def load_repos():
    repos_file = find_repos_file()
    if not repos_file or not repos_file.exists():
        return {}
    with open(repos_file) as f:
        data = util.yaml_load(f.read())
    return data.get("repos", {}) if data else {}


def resolve_repo(name_or_alias, repos_config):
    if not name_or_alias:
        return None, None
    if name_or_alias in repos_config:
        entry = repos_config[name_or_alias]
        return entry["github"], entry
    for alias, entry in repos_config.items():
        if entry.get("github") == name_or_alias:
            return name_or_alias, None
    if "/" in name_or_alias:
        return name_or_alias, None
    return None, None
