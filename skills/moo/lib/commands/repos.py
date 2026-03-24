from .. import gh
from .. import util


def cmd_repos(repos_config, why=None):
    if not repos_config:
        print("No repos configured. Create ~/.moollm/skills/moo/REPOS.yml or ~/.moollm/skills/moocroworld/REPOS.yml, or set MOO_REPOS_FILE.")
        return
    for alias, entry in repos_config.items():
        gh_name = entry.get("github", "")
        desc = entry.get("description", "")
        default_type = entry.get("default_type", "")
        token_env = entry.get("gh_token_env", "")
        auth = f" (auth: ${token_env})" if token_env else ""
        type_note = f" [default: {default_type}_*]" if default_type else ""
        print(f"  {alias:16s} {gh_name:40s} {desc}{type_note}{auth}")
