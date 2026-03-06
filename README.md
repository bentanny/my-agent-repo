# my-agent-repo

Demo research agent connected to LangSmith Improve.

## Structure

- `agent.py` — main entrypoint, loads memory and routes to tools
- `tools.py` — tool definitions (search_web, summarize_document, calendar_lookup)
- `memory.py` — session memory store
- `router.py` — LLM call loop and tool execution

## Connected to LangSmith

This repo is monitored by LangSmith Improve. The improvement agent watches production traces, identifies failure clusters, and opens pull requests with proposed fixes.

Permission level: **Auto-PR** (human review required before merge).
