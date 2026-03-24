# Syntax-aware smelly (structural) line extraction. Supports sniff depths (glance/structure/full).
# Key-skeleton sniff: recursive JSON/YAML structure (keys + array lengths only), depth-limited.
# See skills/sniffable-python for the convention.

import re

from . import util

DEPTH_GLANCE = 1
DEPTH_STRUCTURE = 2
DEPTH_FULL = 3

DEPTH_NAMES = {"glance": DEPTH_GLANCE, "structure": DEPTH_STRUCTURE, "full": DEPTH_FULL}


def _parse_sniff_override(line):
    """If line is # SNIFF: N or # SNIFF: name or # depth: name, return (True, depth_int). Else (False, None)."""
    s = (line or "").strip()
    if not s.startswith("#"):
        return False, None
    rest = s[1:].strip()
    for prefix, name in [("SNIFF:", None), ("depth:", None)]:
        if rest.lower().startswith(prefix.lower()):
            val = rest[len(prefix):].strip()
            if val.isdigit():
                return True, min(DEPTH_FULL, max(DEPTH_GLANCE, int(val)))
            if val.lower() in DEPTH_NAMES:
                return True, DEPTH_NAMES[val.lower()]
            return True, DEPTH_STRUCTURE
    return False, None


def _smelly_lines_python(text):
    """Sniffable Python: section=1, class/def/decorator=2, other smelly=3. Supports # SNIFF: override."""
    lines = text.splitlines()
    out = []
    prev_override = None
    for i, raw in enumerate(lines):
        line_no = i + 1
        s = raw.strip()
        is_override, override_depth = _parse_sniff_override(raw)
        if is_override:
            prev_override = override_depth
            continue
        if not s:
            prev_override = None
            continue
        depth = DEPTH_STRUCTURE
        if s.startswith("def ") or s.startswith("class ") or s.startswith("async def "):
            depth = DEPTH_STRUCTURE
        elif s.startswith("@"):
            depth = DEPTH_STRUCTURE
        elif s.startswith("#"):
            rest = s[1:].strip()
            if rest.startswith("---") or (rest.isupper() and len(rest) > 1) or re.match(r"^[A-Z][A-Z0-9 _-]+$", rest):
                depth = DEPTH_GLANCE
            else:
                prev_override = None
                continue
        else:
            prev_override = None
            continue
        if prev_override is not None:
            depth = prev_override
            prev_override = None
        out.append((line_no, raw, depth))
    return out


def _smelly_lines_yaml(text):
    """YAML: key lines and list markers; single depth (structure) for now."""
    lines = text.splitlines()
    out = []
    for i, raw in enumerate(lines):
        line_no = i + 1
        s = raw.rstrip()
        if re.match(r"^\s*[a-zA-Z0-9_.-]+\s*:", s):
            out.append((line_no, raw, DEPTH_STRUCTURE))
            continue
        if re.match(r"^\s*-\s+", s) or re.match(r"^\s*-\s*$", s):
            out.append((line_no, raw, DEPTH_STRUCTURE))
    return out


def _smelly_lines_markdown(text):
    """Markdown: ## headers; H1–H2=glance, rest=structure for depth filtering."""
    lines = text.splitlines()
    out = []
    for i, raw in enumerate(lines):
        if re.match(r"^#{1,2}\s+.+", raw):
            out.append((i + 1, raw, DEPTH_GLANCE))
        elif re.match(r"^#{3,6}\s+.+", raw):
            out.append((i + 1, raw, DEPTH_STRUCTURE))
    return out


def _smelly_lines_ts_js(text):
    """TypeScript/JavaScript: export/structure; single depth for now."""
    lines = text.splitlines()
    out = []
    for i, raw in enumerate(lines):
        s = raw.strip()
        if not s or s.startswith("//"):
            continue
        if re.match(r"^export\s+", s) or re.match(r"^(async\s+)?function\s+\w+", s) or re.match(r"^class\s+\w+", s):
            out.append((i + 1, raw, DEPTH_STRUCTURE))
            continue
        if re.match(r"^(interface|type)\s+\w+", s):
            out.append((i + 1, raw, DEPTH_STRUCTURE))
    return out


def _normalize_depth(depth):
    """Return integer depth from name or int. None -> None (no filter)."""
    if depth is None:
        return None
    if isinstance(depth, int):
        return min(DEPTH_FULL, max(DEPTH_GLANCE, depth))
    if isinstance(depth, str) and depth.lower() in DEPTH_NAMES:
        return DEPTH_NAMES[depth.lower()]
    if isinstance(depth, str) and depth.isdigit():
        return min(DEPTH_FULL, max(DEPTH_GLANCE, int(depth)))
    return DEPTH_STRUCTURE


def _ensure_triples(smelly):
    """If sniffer returns (line_no, line_text) only, append DEPTH_STRUCTURE."""
    out = []
    for item in smelly:
        if len(item) == 2:
            out.append((item[0], item[1], DEPTH_STRUCTURE))
        else:
            out.append(item)
    return out


SNIFFERS = {
    ".py": _smelly_lines_python,
    ".yml": _smelly_lines_yaml,
    ".yaml": _smelly_lines_yaml,
    ".md": _smelly_lines_markdown,
    ".ts": _smelly_lines_ts_js,
    ".tsx": _smelly_lines_ts_js,
    ".js": _smelly_lines_ts_js,
    ".jsx": _smelly_lines_ts_js,
    ".mjs": _smelly_lines_ts_js,
    ".cjs": _smelly_lines_ts_js,
}


def sniff_smelly_lines(text, path, depth=None, max_lines=None, max_chars=None):
    """Detect file type from path; return (count, list of (line_no, line_text)) for smelly lines.
    depth: optional max depth to include (1=glance, 2=structure, 3=full; or name). None = no filter (full).
    max_lines / max_chars: caps applied after depth filter.
    """
    ext = None
    for e in SNIFFERS:
        if path.endswith(e):
            ext = e
            break
    if ext is None:
        return 0, []
    fn = SNIFFERS[ext]
    raw_smelly = fn(text)
    smelly = _ensure_triples(raw_smelly)
    max_depth = _normalize_depth(depth)
    if max_depth is not None:
        smelly = [(n, t, d) for n, t, d in smelly if d <= max_depth]
    count = len(smelly)
    if max_lines is not None and count > max_lines:
        smelly = smelly[:max_lines]
    if max_chars is not None:
        total = 0
        out = []
        for item in smelly:
            line_no, line_text = item[0], item[1]
            total += len(line_text) + 1
            if total > max_chars:
                break
            out.append(item)
        smelly = out
    return count, [(n, t) for n, t, _ in smelly]


def _skeleton_entries(data, max_depth=None, path_prefix=""):
    """Recursive skeleton: object keys and array lengths only. path_prefix is slash-separated path. Root = depth 0."""
    entries = []
    depth = path_prefix.count("/") if path_prefix else 0
    if max_depth is not None and depth > max_depth:
        return entries
    path_label = path_prefix if path_prefix else "."
    if isinstance(data, dict):
        keys = list(data.keys())
        entries.append({"path": path_label, "type": "object", "keys": keys, "length": None})
        if max_depth is None or depth < max_depth:
            for k, v in data.items():
                seg = f"{path_prefix}/{k}" if path_prefix else k
                entries.extend(_skeleton_entries(v, max_depth=max_depth, path_prefix=seg))
    elif isinstance(data, list):
        n = len(data)
        entries.append({"path": path_label, "type": "array", "keys": None, "length": n})
        if max_depth is None or depth < max_depth:
            for i, v in enumerate(data):
                seg = f"{path_prefix}/{i}" if path_prefix else str(i)
                entries.extend(_skeleton_entries(v, max_depth=max_depth, path_prefix=seg))
    else:
        entries.append({"path": path_label, "type": "leaf", "keys": None, "length": None, "value_type": type(data).__name__})
    return entries


def _format_skeleton_entries(entries, format="text"):
    """Turn skeleton entries list into output string. format: text, yaml, json."""
    if format == "text":
        lines = []
        for e in entries:
            path_str = e["path"]
            t = e["type"]
            if t == "object":
                keys_str = ", ".join(e["keys"]) if e["keys"] else ""
                lines.append(f"{path_str}\tobject\tkeys: {keys_str}")
            elif t == "array":
                lines.append(f"{path_str}\tarray\tlength: {e['length']}")
            else:
                lines.append(f"{path_str}\tleaf\t{e.get('value_type', '')}")
        return "\n".join(lines)
    if format == "yaml":
        return util.yaml_dump(entries)
    if format == "json":
        import json
        return json.dumps(entries, indent=2)
    return util.yaml_dump(entries)


def sniff_skeleton_data(data, max_depth=None, format="text", path_prefix=""):
    """Skeleton of already-parsed dict/list (e.g. sub-tree from extract_at_path). path_prefix labels root of sub-tree."""
    if not isinstance(data, (dict, list)):
        return None
    entries = _skeleton_entries(data, max_depth=max_depth, path_prefix=path_prefix)
    return _format_skeleton_entries(entries, format=format)


def sniff_skeleton(content, path, max_depth=None, format="text"):
    """Parse JSON/YAML and return compact skeleton (keys + array lengths, no leaf values). format: text, yaml, json."""
    if not path.endswith((".json", ".yml", ".yaml")):
        return None
    try:
        data = util.yaml_load(content)
    except Exception:
        return None
    if not isinstance(data, (dict, list)):
        return None
    entries = _skeleton_entries(data, max_depth=max_depth)
    return _format_skeleton_entries(entries, format=format)
