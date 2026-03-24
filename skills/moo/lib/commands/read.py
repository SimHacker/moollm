import re
import sys

from .. import storage
from .. import util
from .. import urls


def cmd_read(repo, branch, path, key=None, line_range=None, token_env=None, why=None):
    content = storage.read_file(repo, branch, path, token_env=token_env)
    if content is None:
        print(f"Not found: {repo} {branch} {path}", file=sys.stderr)
        sys.exit(1)
    path_str = (key or "").strip()
    if path_str:
        try:
            val, structured = storage.extract_at_path(content, path, path_str)
            if structured and isinstance(val, (dict, list)):
                content = util.yaml_dump(val)
            else:
                content = str(val) if val is not None else ""
        except (KeyError, IndexError, ValueError) as e:
            print(f"Error extracting key '{key}': {e}", file=sys.stderr)
            sys.exit(1)
    if line_range:
        start, end = line_range
        content = util.apply_line_range(content, start, end)
    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")
    print(content)
