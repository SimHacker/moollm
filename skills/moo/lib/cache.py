# Ephemeral file cache: .moollm/skills/moo/cache/ — per repo/branch/file.

import os
from pathlib import Path

_file_cache = {}


def cache_dir():
    base = Path(os.environ.get("MOOLLM_WORKSPACE", Path.cwd()))
    return base / ".moollm" / "skills" / "moo" / "cache"


def repo_slug(repo):
    return (repo or "").replace("/", "__")


def safe_path(path):
    p = (path or "").replace("\\", "/").strip("/")
    return "/".join(seg for seg in p.split("/") if seg and seg != "..")


def cache_content_path(repo, branch, path, binary=False):
    base = cache_dir()
    slug = repo_slug(repo)
    safe = safe_path(path)
    if not safe:
        safe = "_root"
    if binary:
        return base / slug / branch / f"{safe}.bin"
    return base / slug / branch / safe


def _ensure_scope_files(cache_file_path, repo, branch):
    try:
        base = cache_dir()
        parts = cache_file_path.relative_to(base).parts
        if len(parts) >= 1:
            (base / parts[0]).mkdir(parents=True, exist_ok=True)
            (base / parts[0] / ".repo").write_text(repo or "", encoding="utf-8")
        if len(parts) >= 2:
            (base / parts[0] / parts[1]).mkdir(parents=True, exist_ok=True)
            (base / parts[0] / parts[1] / ".branch").write_text(branch or "", encoding="utf-8")
    except Exception:
        pass


def _cache_key(repo, branch, path):
    return (repo or "", branch or "", safe_path(path or ""))


def get(repo, branch, path):
    key = _cache_key(repo, branch, path)
    if key in _file_cache:
        return _file_cache[key]
    for binary in (False, True):
        p = cache_content_path(repo, branch, path, binary=binary)
        if p.exists():
            try:
                if binary:
                    content = p.read_bytes()
                else:
                    content = p.read_text(encoding="utf-8")
                _file_cache[key] = content
                return content
            except Exception:
                pass
    return None


def set_content(repo, branch, path, content):
    key = _cache_key(repo, branch, path)
    _file_cache[key] = content
    binary = isinstance(content, bytes)
    p = cache_content_path(repo, branch, path, binary=binary)
    p.parent.mkdir(parents=True, exist_ok=True)
    _ensure_scope_files(p, repo, branch)
    try:
        if binary:
            p.write_bytes(content)
        else:
            p.write_text(content, encoding="utf-8")
    except Exception:
        pass


def invalidate(repo, branch, path):
    _file_cache.pop(_cache_key(repo, branch, path), None)
