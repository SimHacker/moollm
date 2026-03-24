import sys

from .. import gh
from .. import storage
from .. import util


def cmd_scan(repo, type_filter, key, file="GLANCE.yml", token_env=None, why=None):
    branches = gh.gh_api(f"repos/{repo}/branches?per_page=100", jq=".[].name", token_env=token_env)
    if not branches:
        return
    names = branches.split("\n")
    if type_filter:
        names = [n for n in names if n.startswith(f"{type_filter}_")]
    for name in sorted(names):
        content = storage.read_file(repo, name, file, token_env=token_env)
        if not content:
            continue
        try:
            if file.endswith((".yml", ".yaml")):
                data = util.yaml_load(content)
            elif file.endswith(".json"):
                import json
                data = json.loads(content)
            else:
                continue
            val = data
            for part in key.split("/"):
                if isinstance(val, dict):
                    val = val.get(part)
                elif isinstance(val, list):
                    val = val[int(part)]
                else:
                    val = None
                    break
            print(f"{name:40s} {val}")
        except Exception:
            continue
