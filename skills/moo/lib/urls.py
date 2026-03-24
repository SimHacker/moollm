# Moorl parsing: moo:// and moollm:// URLs, fragment, line spec.

import re
from urllib.parse import urlparse


def is_moo_url(s):
    return isinstance(s, str) and (s.startswith("moo://") or s.startswith("moollm://"))


def parse_moo_url(url):
    """Parse moo:// or moollm:// URL into components.
    Returns dict: scheme, repo (None for moo://), branch, path, fragment, query.
    path does not include leading slash; fragment and query are raw (no leading # or ?).
    """
    parsed = urlparse(url)
    scheme = parsed.scheme
    if scheme not in ("moo", "moollm"):
        return None
    netloc = parsed.netloc
    path = (parsed.path or "").lstrip("/")
    fragment = parsed.fragment or ""
    query = parsed.query or ""
    if not netloc:
        return None
    if scheme == "moo":
        branch = netloc
        file_path = path
        repo = None
    else:
        parts = path.split("/", 1)
        branch = parts[0] if parts else ""
        file_path = parts[1] if len(parts) > 1 else ""
        repo = netloc
    return {
        "scheme": scheme,
        "repo": repo,
        "branch": branch,
        "path": file_path,
        "fragment": fragment,
        "query": query,
    }


def parse_fragment(fragment):
    """Split fragment into key path and optional line spec.
    Returns (path_str, line_start, line_end).
    Fragment forms: key/path, L3, L3-L10, key/path:L3, key/path:L3-L10.
    """
    if not fragment:
        return "", None, None
    path_str = fragment
    line_start = line_end = None
    match = re.match(r"^(.+):(L(\d+)(?:-L?(\d+))?)$", fragment)
    if match:
        path_str = match.group(1)
        start_s, end_s = match.group(3), match.group(4)
        line_start = int(start_s)
        line_end = int(end_s) if end_s else line_start
    elif re.match(r"^L\d+", fragment):
        m = re.match(r"^L(\d+)(?:-L?(\d+))?$", fragment)
        if m:
            line_start = int(m.group(1))
            line_end = int(m.group(2)) if m.group(2) else line_start
        path_str = ""
    return path_str, line_start, line_end
