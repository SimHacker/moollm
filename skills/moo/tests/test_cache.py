import os
import pytest
from pathlib import Path

from lib import cache


def test_repo_slug():
    assert cache.repo_slug("leela-ai/central") == "leela-ai__central"
    assert cache.repo_slug("") == ""


def test_safe_path():
    assert cache.safe_path("a/b/c") == "a/b/c"
    assert cache.safe_path("/a/b") == "a/b"
    # safe_path drops ".." segments but does not resolve them, so a/../b -> a/b
    assert cache.safe_path("a/../b") == "a/b"
    assert cache.safe_path("") == ""


def test_cache_content_path():
    base = cache.cache_dir()
    p = cache.cache_content_path("owner/repo", "main", "path/to/file.yml")
    assert p == base / "owner__repo" / "main" / "path/to/file.yml"
    p_bin = cache.cache_content_path("owner/repo", "main", "file", binary=True)
    assert p_bin.suffix == ".bin"


def test_cache_get_set_invalidate(tmp_path, monkeypatch):
    monkeypatch.setenv("MOOLLM_WORKSPACE", str(tmp_path))
    cache_base = tmp_path / ".moollm" / "skills" / "moo" / "cache"
    monkeypatch.setattr(cache, "cache_dir", lambda: cache_base)
    cache.set_content("r/o", "br", "f.txt", "hello")
    assert cache.get("r/o", "br", "f.txt") == "hello"
    cache.invalidate("r/o", "br", "f.txt")
    # invalidate clears in-memory cache; get can still read from disk until file is removed
    cache_file = cache.cache_content_path("r/o", "br", "f.txt")
    cache_file.unlink(missing_ok=True)
    assert cache.get("r/o", "br", "f.txt") is None
