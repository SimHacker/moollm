from .. import gh
from .. import storage
from .. import util


def cmd_ls(repo, type_filter=None, show_glance=False, token_env=None, why=None):
    branches = gh.gh_api(f"repos/{repo}/branches?per_page=100", jq=".[].name", token_env=token_env)
    if not branches:
        return
    names = branches.split("\n")
    if type_filter:
        names = [n for n in names if n.startswith(f"{type_filter}_")]
    for name in sorted(names):
        line = name
        if show_glance:
            glance = storage.read_file(repo, name, "GLANCE.yml", token_env=token_env)
            if glance:
                try:
                    g = util.yaml_load(glance)
                    summary = g.get("summary", g.get("what", ""))
                    if isinstance(summary, str):
                        summary = summary.strip().split("\n")[0][:80]
                    severity = g.get("severity", "")
                    status = g.get("status", "")
                    line = f"{name:40s} {severity:10s} {status:16s} {summary}"
                except Exception:
                    pass
        print(line)


def cmd_tree(repo, branch, recursive=False, token_env=None, why=None):
    result = storage.list_tree(repo, branch, recursive=recursive, token_env=token_env)
    if result:
        print(result)
