"""
Main agent entrypoint.
"""
from tools import search_web, summarize_document, calendar_lookup
from memory import load_memory, save_memory
from router import route

SYSTEM_PROMPT = """You are a helpful research assistant. You have access to the following tools:

- search_web: Search the web for current information. Query must be a clean string.
- summarize_document: Summarize a document given its URL or text content.
- calendar_lookup: Look up calendar events for a given date range.

When you cannot find reliable information, say so clearly rather than guessing.
"""


def run(session_id: str, user_message: str) -> str:
    memory = load_memory(session_id)
    response = route(
        system_prompt=SYSTEM_PROMPT,
        messages=memory + [{"role": "user", "content": user_message}],
        tools=[search_web, summarize_document, calendar_lookup],
    )
    save_memory(session_id, user_message, response)
    return response
