"""
Tool definitions for the research agent.
"""
import re
import requests


def sanitize_query(query: str) -> str:
    """Remove special characters that break the search API argument parser."""
    return re.sub(r"[^\w\s\-]", "", query).strip()


def search_web(query: str) -> str:
    """Search the web for information.

    Query must be a clean, URL-safe string with no special characters.
    Sanitize user input before passing.
    """
    query = sanitize_query(query)
    # stub — replace with real search API
    return f"[search results for: {query}]"


def summarize_document(url_or_text: str, max_chunks: int = 5) -> str:
    """Summarize a document.

    For large documents (> 50 pages), the input is chunked automatically
    and summarized recursively.
    """
    chunks = _chunk_input(url_or_text, max_chunks)
    summaries = [_summarize_chunk(c) for c in chunks]
    if len(summaries) == 1:
        return summaries[0]
    return _summarize_chunk(" ".join(summaries))


def calendar_lookup(date_range: str) -> str:
    """Look up calendar events for a given date range.

    Returns events formatted as locale-friendly strings.
    """
    # stub — replace with real calendar API
    raw = f"[calendar events for: {date_range}]"
    return _normalize_dates(raw)


def _chunk_input(text: str, max_chunks: int) -> list[str]:
    words = text.split()
    chunk_size = max(len(words) // max_chunks, 500)
    return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]


def _summarize_chunk(text: str) -> str:
    return f"[summary of {len(text)} chars]"


def _normalize_dates(text: str) -> str:
    return text  # format to locale string in production
