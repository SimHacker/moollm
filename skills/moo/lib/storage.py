# Read/write files on a branch, list tree. Uses cache and gh.

import base64
import sys
from urllib.parse import quote

from . import cache
from . import gh
from . import util


def read_file(repo, branch, path, token_env=None):
    cached = cache.get(repo, branch, path)
    if cached is not None:
        return cached
    encoded_path = quote(path, safe="")
    result = gh.gh_api(f"repos/{repo}/contents/{encoded_path}?ref={branch}", jq=".content", token_env=token_env)
    if result:
        try:
            content = base64.b64decode(result).decode("utf-8")
        except Exception:
            content = base64.b64decode(result)
        cache.set_content(repo, branch, path, content)
        return content
    return None


def extract_at_path(content, path, path_str):
    """Parse content as YAML/JSON and return value at slash-separated path_str. Returns (value, is_structured)."""
    import json
    if path.endswith((".yml", ".yaml")):
        data = util.yaml_load(content)
    elif path.endswith(".json"):
        data = json.loads(content)
    else:
        return content, False
    if not path_str:
        return data, True
    for part in path_str.split("/"):
        if not part:
            continue
        if isinstance(data, list):
            data = data[int(part)]
        elif isinstance(data, dict):
            data = data[part]
        else:
            raise KeyError(part)
    return data, True


def list_tree(repo, branch, recursive=False, token_env=None):
    suffix = "?recursive=1" if recursive else ""
    jq = r'.tree[] | "\(.type) \(.path)"'
    return gh.gh_api(f"repos/{repo}/git/trees/{branch}{suffix}", jq=jq, token_env=token_env)


def write_file(repo, branch, path, raw_bytes, token_env=None):
    import base64
    import json
    encoded = base64.b64encode(raw_bytes).decode("utf-8")
    encoded_path = quote(path, safe="")
    existing = gh.gh_api(f"repos/{repo}/contents/{encoded_path}?ref={branch}", jq=".sha", token_env=token_env)
    body = {
        "message": f"moo: update {path}",
        "content": encoded,
        "branch": branch,
    }
    if existing and not existing.startswith("{") and existing != "null":
        body["sha"] = existing
    result = gh.gh_api(f"repos/{repo}/contents/{encoded_path}", method="PUT", body=body, token_env=token_env)
    if result:
        cache.invalidate(repo, branch, path)
        return True
    return False


def delete_branch(repo, branch, token_env=None):
    result = gh.gh_api(f"repos/{repo}/git/refs/heads/{branch}", method="DELETE", token_env=token_env)
    return result is not None
