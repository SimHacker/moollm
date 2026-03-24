import sys

from .. import storage


def cmd_write(repo, branch, path, content=None, local_file=None, token_env=None, why=None):
    if local_file:
        with open(local_file, "rb") as f:
            raw = f.read()
    elif content:
        raw = content.encode("utf-8")
    else:
        raw = sys.stdin.buffer.read()
    ok = storage.write_file(repo, branch, path, raw, token_env=token_env)
    if ok:
        print(f"Wrote {path} on {branch}")
    else:
        print(f"Failed to write {path}", file=sys.stderr)
        sys.exit(1)


def cmd_rm(repo, branch, token_env=None, why=None):
    ok = storage.delete_branch(repo, branch, token_env=token_env)
    print(f"Deleted branch {branch}" if ok else f"Failed to delete {branch}")
