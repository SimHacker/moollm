import sys

from .. import sniff
from .. import storage

SNIFFERS = sniff.SNIFFERS


def cmd_sniff(repo, branch, path, key=None, depth=None, max_lines=None, max_chars=None, skeleton=False, skeleton_depth=None, skeleton_format="text", token_env=None, why=None):
    content = storage.read_file(repo, branch, path, token_env=token_env)
    if content is None:
        print(f"Not found: {repo} {branch} {path}", file=sys.stderr)
        sys.exit(1)
    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")
    if key:
        try:
            extracted, is_structured = storage.extract_at_path(content, path, key)
        except KeyError as e:
            print(f"No such key path: {key} ({e})", file=sys.stderr)
            sys.exit(1)
        if is_structured and isinstance(extracted, (dict, list)):
            out = sniff.sniff_skeleton_data(extracted, max_depth=skeleton_depth, format=skeleton_format, path_prefix=key)
            if out is None:
                print(f"skeleton of sub-tree failed", file=sys.stderr)
                sys.exit(1)
            print(f"skeleton {path}#{key}" + (f" (depth≤{skeleton_depth})" if skeleton_depth is not None else ""))
            print(out)
            return
        if is_structured:
            extracted = str(extracted)
        content = extracted
    if skeleton and not key:
        out = sniff.sniff_skeleton(content, path, max_depth=skeleton_depth, format=skeleton_format)
        if out is None:
            print(f"skeleton only for .json/.yml/.yaml; got {path}", file=sys.stderr)
            sys.exit(1)
        print(f"skeleton {path}" + (f" (depth≤{skeleton_depth})" if skeleton_depth is not None else ""))
        print(out)
        return
    sniff_path = path if key else path
    total_count, smelly = sniff.sniff_smelly_lines(content, sniff_path, depth=depth, max_lines=max_lines, max_chars=max_chars)
    ext = next((e for e in SNIFFERS if sniff_path.endswith(e)), "?")
    cap_note = f" (showing first {len(smelly)} of {total_count})" if (max_lines or max_chars) and len(smelly) < total_count else f" (total {total_count})"
    print(f"sniff {path}" + (f"#{key}" if key else "") + f" ({ext}): {len(smelly)} smelly lines{cap_note}")
    for line_no, line_text in smelly:
        print(f"{line_no:5d}| {line_text}")
