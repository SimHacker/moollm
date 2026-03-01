#!/usr/bin/env python3
"""moo.py — Moocroworld CLI.

GitHub branches as structured object storage. Each branch is a moo (ClassName_ObjectID).

Uses `gh api` under the hood. Requires gh CLI authenticated.

Repos configured in REPOS.yml (alongside this script, or MOO_REPOS_FILE env).

Usage:
    moo repos                                  # list configured repos
    moo ls [repo|alias]                        # list all branches (moos)
    moo ls [repo|alias] --type Issue           # list branches matching Issue_*
    moo ls [repo|alias] --glance               # include GLANCE.yml summary per moo
    moo ls --all --type Issue --glance         # scan all repos for Issue_* moos
    moo tree [repo|alias] [branch]             # list files on a branch
    moo tree [repo|alias] [branch] -r          # recursive file listing
    moo read [repo|alias] [branch] [path]      # read a file from a branch
    moo read [repo|alias] [branch] [path] -k severity  # extract YAML/JSON key
    moo glance [repo|alias] [branch]           # shortcut: read GLANCE.yml
    moo card [repo|alias] [branch]             # shortcut: read CARD.yml
    moo scan [repo|alias] --type Issue -k severity  # scan moos, extract key
    moo scan --all --type Issue -k severity    # scan across all repos
    moo write [repo|alias] [branch] [path] [content]
    moo write [repo|alias] [branch] [path] --file local_file
    moo create [repo|alias] [branch]           # create orphan branch
    moo rm [repo|alias] [branch]               # delete a branch

Environment:
    MOO_REPO        default repo (owner/name or alias)
    MOO_REPOS_FILE  path to REPOS.yml
"""

import argparse
import base64
import json
import os
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def _yaml_load(text):
    if yaml:
        return yaml.safe_load(text)
    return json.loads(text)


def _yaml_dump(data):
    if yaml:
        return yaml.dump(data, default_flow_style=False).rstrip()
    return json.dumps(data, indent=2)


def find_repos_file():
    explicit = os.environ.get("MOO_REPOS_FILE")
    if explicit:
        return Path(explicit)
    candidates = [
        Path(__file__).parent / "REPOS.yml",
        Path("skills/moocroworld/REPOS.yml"),
        Path(".moollm/skills/moocroworld/REPOS.yml"),
        Path.home() / ".moollm" / "skills" / "moocroworld" / "REPOS.yml",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def load_repos():
    repos_file = find_repos_file()
    if not repos_file or not repos_file.exists():
        return {}
    with open(repos_file) as f:
        data = _yaml_load(f.read())
    return data.get("repos", {}) if data else {}


def resolve_repo(name_or_alias, repos_config):
    if not name_or_alias:
        return None, None
    if name_or_alias in repos_config:
        entry = repos_config[name_or_alias]
        return entry["github"], entry
    for alias, entry in repos_config.items():
        if entry.get("github") == name_or_alias:
            return name_or_alias, entry
    if "/" in name_or_alias:
        return name_or_alias, None
    return None, None


def gh_api(endpoint, method="GET", body=None, jq=None, token_env=None):
    cmd = ["gh", "api", endpoint]
    if method != "GET":
        cmd.extend(["-X", method])
    if body:
        cmd.extend(["--input", "-"])
    if jq:
        cmd.extend(["--jq", jq])
    env = os.environ.copy()
    if token_env and os.environ.get(token_env):
        env["GH_TOKEN"] = os.environ[token_env]
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        input=json.dumps(body) if body else None,
        env=env,
    )
    if result.returncode != 0:
        if "404" not in result.stderr:
            print(f"gh api error: {result.stderr.strip()}", file=sys.stderr)
        return None
    return result.stdout.strip()


def get_token_env(repo_entry):
    if repo_entry and repo_entry.get("gh_token_env"):
        return repo_entry["gh_token_env"]
    return None


def list_repos_cmd(repos_config):
    if not repos_config:
        print("No repos configured. Create .moollm/skills/moocroworld/REPOS.yml")
        return
    for alias, entry in repos_config.items():
        gh = entry.get("github", "")
        desc = entry.get("description", "")
        default_type = entry.get("default_type", "")
        token_env = entry.get("gh_token_env", "")
        auth = f" (auth: ${token_env})" if token_env else ""
        type_note = f" [default: {default_type}_*]" if default_type else ""
        print(f"  {alias:16s} {gh:40s} {desc}{type_note}{auth}")


def list_branches(repo, type_filter=None, show_glance=False, token_env=None):
    branches = gh_api(f"repos/{repo}/branches?per_page=100", jq=".[].name", token_env=token_env)
    if not branches:
        return
    names = branches.split("\n")
    if type_filter:
        names = [n for n in names if n.startswith(f"{type_filter}_")]
    for name in sorted(names):
        line = name
        if show_glance:
            glance = read_file(repo, name, "GLANCE.yml", token_env=token_env)
            if glance:
                try:
                    g = _yaml_load(glance)
                    summary = g.get("summary", g.get("what", ""))
                    if isinstance(summary, str):
                        summary = summary.strip().split("\n")[0][:80]
                    severity = g.get("severity", "")
                    status = g.get("status", "")
                    line = f"{name:40s} {severity:10s} {status:16s} {summary}"
                except Exception:
                    pass
        print(line)


def list_tree(repo, branch, recursive=False, token_env=None):
    suffix = "?recursive=1" if recursive else ""
    jq = '.tree[] | "\\(.type) \\(.path)"'
    result = gh_api(f"repos/{repo}/git/trees/{branch}{suffix}", jq=jq, token_env=token_env)
    if result:
        print(result)


def read_file(repo, branch, path, token_env=None):
    import urllib.parse
    encoded_path = urllib.parse.quote(path, safe="")
    result = gh_api(f"repos/{repo}/contents/{encoded_path}?ref={branch}", jq=".content", token_env=token_env)
    if result:
        try:
            return base64.b64decode(result).decode("utf-8")
        except Exception:
            return base64.b64decode(result)
    return None


def read_file_cmd(repo, branch, path, key=None, token_env=None):
    content = read_file(repo, branch, path, token_env=token_env)
    if content is None:
        print(f"Not found: {repo} {branch} {path}", file=sys.stderr)
        sys.exit(1)
    if key:
        try:
            if path.endswith((".yml", ".yaml")):
                data = _yaml_load(content)
            elif path.endswith(".json"):
                data = json.loads(content)
            else:
                print(content)
                return
            for part in key.split("/"):
                if isinstance(data, list):
                    data = data[int(part)]
                elif isinstance(data, dict):
                    data = data[part]
                else:
                    print(f"Cannot navigate into {type(data).__name__} at '{part}'", file=sys.stderr)
                    sys.exit(1)
            if isinstance(data, (dict, list)):
                print(_yaml_dump(data))
            else:
                print(data)
        except (KeyError, IndexError, ValueError) as e:
            print(f"Error extracting key '{key}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(content)


def scan_moos(repo, type_filter, key, file="GLANCE.yml", token_env=None):
    branches = gh_api(f"repos/{repo}/branches?per_page=100", jq=".[].name", token_env=token_env)
    if not branches:
        return
    names = branches.split("\n")
    if type_filter:
        names = [n for n in names if n.startswith(f"{type_filter}_")]
    for name in sorted(names):
        content = read_file(repo, name, file, token_env=token_env)
        if not content:
            continue
        try:
            if file.endswith((".yml", ".yaml")):
                data = _yaml_load(content)
            elif file.endswith(".json"):
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


def write_file_cmd(repo, branch, path, content=None, local_file=None, token_env=None):
    if local_file:
        with open(local_file, "rb") as f:
            raw = f.read()
    elif content:
        raw = content.encode("utf-8")
    else:
        raw = sys.stdin.buffer.read()

    encoded = base64.b64encode(raw).decode("utf-8")
    import urllib.parse
    encoded_path = urllib.parse.quote(path, safe="")

    existing = gh_api(f"repos/{repo}/contents/{encoded_path}?ref={branch}", jq=".sha", token_env=token_env)
    body = {
        "message": f"mw.py: update {path}",
        "content": encoded,
        "branch": branch,
    }
    if existing and not existing.startswith("{") and existing != "null":
        body["sha"] = existing

    result = gh_api(f"repos/{repo}/contents/{encoded_path}", method="PUT", body=body, token_env=token_env)
    if result:
        print(f"Wrote {path} on {branch}")
    else:
        print(f"Failed to write {path}", file=sys.stderr)
        sys.exit(1)


def delete_branch(repo, branch, token_env=None):
    result = gh_api(f"repos/{repo}/git/refs/heads/{branch}", method="DELETE", token_env=token_env)
    print(f"Deleted branch {branch}" if result is not None else f"Failed to delete {branch}")


def main():
    parser = argparse.ArgumentParser(
        description="mw.py — Moocroworld CLI. GitHub branches as structured object storage.",
        epilog="Repos configured in .moollm/skills/moocroworld/REPOS.yml",
    )
    parser.add_argument("--repo", default=os.environ.get("MOO_REPO"), help="repo (owner/name or alias)")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("repos", help="List configured repos")

    ls_p = sub.add_parser("ls", help="List branches (moos)")
    ls_p.add_argument("repo_pos", nargs="?", help="repo or alias")
    ls_p.add_argument("--type", dest="type_filter", help="Filter by ClassName prefix")
    ls_p.add_argument("--glance", action="store_true", help="Include GLANCE.yml summary")
    ls_p.add_argument("--all", action="store_true", help="Scan all configured repos")

    tree_p = sub.add_parser("tree", help="List files on a branch")
    tree_p.add_argument("repo_pos", nargs="?")
    tree_p.add_argument("branch")
    tree_p.add_argument("--recursive", "-r", action="store_true")

    read_p = sub.add_parser("read", help="Read a file from a branch")
    read_p.add_argument("repo_pos", nargs="?")
    read_p.add_argument("branch")
    read_p.add_argument("path")
    read_p.add_argument("--key", "-k", help="Extract YAML/JSON key (slash-separated)")

    glance_p = sub.add_parser("glance", help="Read GLANCE.yml")
    glance_p.add_argument("repo_pos", nargs="?")
    glance_p.add_argument("branch")

    card_p = sub.add_parser("card", help="Read CARD.yml")
    card_p.add_argument("repo_pos", nargs="?")
    card_p.add_argument("branch")

    scan_p = sub.add_parser("scan", help="Scan moos, extract a key")
    scan_p.add_argument("repo_pos", nargs="?")
    scan_p.add_argument("--type", dest="type_filter", required=True)
    scan_p.add_argument("--key", "-k", required=True)
    scan_p.add_argument("--file", default="GLANCE.yml")
    scan_p.add_argument("--all", action="store_true", help="Scan all configured repos")

    write_p = sub.add_parser("write", help="Write a file to a branch")
    write_p.add_argument("repo_pos", nargs="?")
    write_p.add_argument("branch")
    write_p.add_argument("path")
    write_p.add_argument("content", nargs="?")
    write_p.add_argument("--file", dest="local_file")

    rm_p = sub.add_parser("rm", help="Delete a branch")
    rm_p.add_argument("repo_pos", nargs="?")
    rm_p.add_argument("branch")

    args = parser.parse_args()
    repos_config = load_repos()

    if args.command == "repos":
        list_repos_cmd(repos_config)
        return

    scan_all = getattr(args, "all", False)

    if scan_all:
        type_filter = getattr(args, "type_filter", None)
        show_glance = getattr(args, "glance", False)
        key = getattr(args, "key", None)
        file_name = getattr(args, "file", "GLANCE.yml")
        for alias, entry in repos_config.items():
            gh_repo = entry["github"]
            te = get_token_env(entry)
            tf = type_filter or entry.get("default_type")
            if not tf:
                continue
            print(f"\n# {alias} ({gh_repo})")
            if args.command == "ls":
                list_branches(gh_repo, tf, show_glance, token_env=te)
            elif args.command == "scan":
                scan_moos(gh_repo, tf, key, file_name, token_env=te)
        return

    repo_name = getattr(args, "repo_pos", None) or args.repo
    if not repo_name:
        parser.error("repo required (positional, --repo, MOO_REPO, or --all)")
    repo, repo_entry = resolve_repo(repo_name, repos_config)
    if not repo:
        parser.error(f"Unknown repo or alias: {repo_name}")
    te = get_token_env(repo_entry)

    if args.command == "ls":
        tf = args.type_filter or (repo_entry.get("default_type") if repo_entry else None)
        list_branches(repo, tf, args.glance, token_env=te)
    elif args.command == "tree":
        list_tree(repo, args.branch, args.recursive, token_env=te)
    elif args.command == "read":
        read_file_cmd(repo, args.branch, args.path, args.key, token_env=te)
    elif args.command == "glance":
        read_file_cmd(repo, args.branch, "GLANCE.yml", token_env=te)
    elif args.command == "card":
        read_file_cmd(repo, args.branch, "CARD.yml", token_env=te)
    elif args.command == "scan":
        tf = args.type_filter or (repo_entry.get("default_type") if repo_entry else None)
        scan_moos(repo, tf, args.key, args.file, token_env=te)
    elif args.command == "write":
        write_file_cmd(repo, args.branch, args.path, args.content, args.local_file, token_env=te)
    elif args.command == "rm":
        delete_branch(repo, args.branch, token_env=te)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
