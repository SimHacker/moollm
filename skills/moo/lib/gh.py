# GitHub API via gh CLI.

import json
import os
import subprocess


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
        if "404" not in (result.stderr or ""):
            import sys
            print(f"gh api error: {(result.stderr or '').strip()}", file=sys.stderr)
        return None
    return result.stdout.strip()


def get_token_env(repo_entry):
    if repo_entry and repo_entry.get("gh_token_env"):
        return repo_entry["gh_token_env"]
    return None
