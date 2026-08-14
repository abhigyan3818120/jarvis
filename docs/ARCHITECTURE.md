# Architecture

JARVIS is split into small replaceable boundaries:

- `config.py` — environment-backed settings.
- `memory.py` — local SQLite persistence.
- `providers.py` — AI-provider abstraction and Gemini adapter.
- `tools.py` — explicit tool registry and metadata.
- `__main__.py` — command-line entry point and diagnostics.
- `ui/`, `browser/`, and `voice/` are reserved for optional adapters and must not become core dependencies.

The core is intentionally provider- and interface-oriented so cloud failures do not corrupt local state. Secrets belong only in environment variables or local secret stores; they are never checked into Git.
