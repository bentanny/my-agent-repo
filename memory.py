"""
Simple in-process memory store. Replace with a persistent backend in production.
"""
from typing import TypedDict

_store: dict[str, list[dict]] = {}


class Message(TypedDict):
    role: str
    content: str


def load_memory(session_id: str) -> list[Message]:
    return _store.get(session_id, [])


def save_memory(session_id: str, user_message: str, assistant_response: str) -> None:
    if session_id not in _store:
        _store[session_id] = []
    _store[session_id].append({"role": "user", "content": user_message})
    _store[session_id].append({"role": "assistant", "content": assistant_response})
