import sys

from .. import cache
from .. import llm
from .. import storage


def cmd_summarize(repo, branch, path, provider="gemini", model=None, use_cache=True, token_env=None, why=None):
    summary, from_cache = llm.summarize_file(
        repo, branch, path,
        read_file_fn=lambda r, b, p: storage.read_file(r, b, p, token_env=token_env),
        cache_get=cache.get,
        cache_set=cache.set_content,
        provider=provider,
        model=model,
        use_cache=use_cache,
    )
    if summary is None:
        print("Summarize failed: missing file, missing GEMINI_API_KEY, or install google-genai (pip install google-genai).", file=sys.stderr)
        sys.exit(1)
    if from_cache:
        print("(cached)")
    print(summary)
