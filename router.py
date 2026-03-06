"""
LLM router — calls the model and handles tool execution loop.
"""
from typing import Callable


def route(
    system_prompt: str,
    messages: list[dict],
    tools: list[Callable],
    max_iterations: int = 10,
) -> str:
    """Run the agent loop until a final response is produced or max_iterations hit."""
    tool_map = {fn.__name__: fn for fn in tools}
    iteration = 0

    while iteration < max_iterations:
        # stub — replace with real LLM call
        response = _call_llm(system_prompt, messages, list(tool_map.keys()))

        if response.get("type") == "final":
            return response["content"]

        if response.get("type") == "tool_call":
            tool_name = response["tool"]
            tool_args = response["args"]
            tool_fn = tool_map.get(tool_name)
            if tool_fn is None:
                messages.append({"role": "tool", "content": f"Unknown tool: {tool_name}"})
            else:
                result = tool_fn(**tool_args)
                messages.append({"role": "tool", "content": result})

        iteration += 1

    return "I reached the maximum number of steps without a final answer."


def _call_llm(system_prompt: str, messages: list[dict], tool_names: list[str]) -> dict:
    # stub
    return {"type": "final", "content": "[agent response]"}
