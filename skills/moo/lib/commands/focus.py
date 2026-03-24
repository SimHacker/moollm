import json
import sys

from .. import gh
from .. import overlay
from .. import storage
from .. import util


def cmd_batch_glance(repo, type_filter, token_env=None, repos_config=None, why=None):
    branches = gh.gh_api(f"repos/{repo}/branches?per_page=100", jq=".[].name", token_env=token_env)
    if not branches:
        return
    names = branches.split("\n")
    if type_filter:
        names = [n for n in names if n.startswith(f"{type_filter}_")]
    for name in sorted(names):
        content = storage.read_file(repo, name, "GLANCE.yml", token_env=token_env)
        print(f"\n--- moo: {repo} / {name} ---")
        if content:
            if isinstance(content, bytes):
                content = content.decode("utf-8", errors="replace")
            print(content)
        else:
            print("(no GLANCE.yml)")


def cmd_focus(overlay_path, repos_config, output_json=False, why=None):
    ov = overlay.load_overlay(overlay_path, repos_config)
    if output_json:
        out = []
    for rentry in ov["repos"]:
        repo = rentry["repo"]
        type_filter = rentry["type"]
        depth_max = rentry["depth"]
        at_depth = rentry["at_depth"]
        fragments_map = rentry["fragments"]
        te = gh.get_token_env(repos_config.get(repo) or next((e for e in repos_config.values() if e.get("github") == repo), None))
        branches = gh.gh_api(f"repos/{repo}/branches?per_page=100", jq=".[].name", token_env=te)
        if not branches:
            continue
        names = [n for n in branches.split("\n") if not type_filter or n.startswith(f"{type_filter}_")]
        for branch in sorted(names):
            if output_json:
                branch_out = {"repo": repo, "branch": branch, "depth": {}}
            else:
                print(f"\n--- moo: {repo} / {branch} ---")
            for d in range(depth_max + 1):
                patterns = at_depth.get(d)
                if not patterns:
                    continue
                paths = overlay.expand_globs(repo, branch, patterns, token_env=te)
                for path in paths:
                    content = storage.read_file(repo, branch, path, token_env=te)
                    if content is None:
                        continue
                    if isinstance(content, bytes):
                        content = content.decode("utf-8", errors="replace")
                    frags = fragments_map.get(path)
                    if frags and path.endswith((".yml", ".yaml", ".json")):
                        try:
                            data = util.yaml_load(content) if path.endswith((".yml", ".yaml")) else json.loads(content)
                            extracted = {}
                            for fp in frags:
                                val = data
                                for part in fp.split("/"):
                                    if not part:
                                        continue
                                    if isinstance(val, list):
                                        val = val[int(part)]
                                    else:
                                        val = val.get(part)
                                extracted[fp] = val
                            content = util.yaml_dump(extracted)
                        except Exception:
                            pass
                    if output_json:
                        branch_out["depth"].setdefault(d, {})[path] = content
                    else:
                        print(f"\n### {path} (depth {d})")
                        print(content)
            if output_json:
                out.append(branch_out)
    if output_json:
        print(json.dumps(out, indent=2))
