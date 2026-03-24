# Optional LLM integration for moo (summarize, future abstractions). Start with Gemini.
# Requires: pip install google-genai and GEMINI_API_KEY in environment.

def _gemini_summarize(text, model=None):
    """Return a short summary of text using Gemini API, or None on failure."""
    try:
        from google import genai
    except ImportError:
        return None
    import os
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    model = model or "gemini-2.0-flash"
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model,
            contents=f"Summarize the following in at most 3 short sentences. Output only the summary.\n\n{text[:50000]}",
        )
        if response and response.text:
            return response.text.strip()
    except Exception:
        pass
    return None


def summarize_text(content, provider="gemini", model=None):
    """Summarize text using the given provider. Returns summary string or None.
    provider: 'gemini' (default). Others can be added later.
    """
    if not content or not isinstance(content, str):
        return None
    if provider.lower() == "gemini":
        return _gemini_summarize(content, model=model)
    return None


def summarize_file(repo, branch, path, read_file_fn, cache_get, cache_set, provider="gemini", model=None, use_cache=True):
    """Read file via read_file_fn(repo, branch, path), summarize, optionally cache. Returns (summary, from_cache)."""
    cache_key_path = path + ".summary"
    if use_cache and cache_get:
        cached = cache_get(repo, branch, cache_key_path)
        if isinstance(cached, str):
            return cached, True
    content = read_file_fn(repo, branch, path)
    if content is None:
        return None, False
    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")
    summary = summarize_text(content, provider=provider, model=model)
    if summary and use_cache and cache_set:
        cache_set(repo, branch, cache_key_path, summary)
    return summary, False
