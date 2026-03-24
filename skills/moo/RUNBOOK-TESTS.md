# Moo test suite — runbook

How to run, extend, and interpret the moo test suite.

## Running the tests

From the **moo skill root** (`skills/moo/` in the MOOLLM repo):

```bash
cd skills/moo
python -m pytest tests/ -v
```

From the **MOOLLM repo root**:

```bash
cd /path/to/moollm
python -m pytest skills/moo/tests/ -v
```

Pytest must be installed (`pip install pytest` or `uv pip install pytest`). No other runtime deps are required for the suite; `lib` uses only the stdlib plus optional PyYAML (tests work with or without it).

## What is covered

- **Unit only.** No network or GitHub API calls. Commands that call `gh.gh_api` (e.g. `read`, `write`, `scan` with live repos) are not exercised here.
- **Modules under test:**
  - `lib/urls.py` — `parse_moo_url`, `parse_fragment`, `is_moo_url`
  - `lib/util.py` — `yaml_load`, `yaml_dump`, `apply_line_range`
  - `lib/sniff.py` — `sniff_smelly_lines` (Python, YAML, Markdown; `max_lines` / `max_chars`)
  - `lib/config.py` — `resolve_repo` (alias, github name, owner/name; no `find_repos_file` that touches disk)
  - `lib/cache.py` — `cache_dir`, `repo_slug`, `safe_path`, `cache_content_path`, get/set/invalidate (with `tmp_path` and patched `cache_dir`)
  - `lib/storage.py` — `extract_at_path` (YAML/JSON, key path, list index, non-structured, missing key)
  - `lib/overlay.py` — `load_overlay` (empty file, defaults + repos, alias resolution), `default_overlay_path` (returns path or None)

## Isolation

- Cache tests set `MOOLLM_WORKSPACE` to a `tmp_path` and patch `cache_dir` so the real cache is not used.
- No `MOO_REPOS_FILE` or repo files are required; config tests pass a dict.

## Adding or changing tests

1. **New test file:** Add `tests/test_<module>.py`. Use `from lib import <module>` or `from lib.<sub> import <module>`; `conftest.py` adds the skill root to `sys.path`.
2. **New test:** Add a `test_*` function. Use `tmp_path` and `monkeypatch` for env/path isolation; do not call `gh.gh_api` or real disk outside `tmp_path`.
3. **CLI / commands:** To test commands (e.g. `cmd_read`) without network, mock `lib.gh.gh_api` or `lib.storage.read_file` in the test.

## Optional: install pytest only for this skill

```bash
pip install pytest
# or
uv pip install pytest
```

No `requirements.txt` or `pyproject.toml` is committed; the skill stays dependency-light. CI or local policy can add a dev dependency on `pytest` at repo level if desired.
