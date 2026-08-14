# Architecture

JARVIS is deliberately split into small replaceable boundaries:

- `config.py` — typed environment-backed settings.
- `app.py` — conversation orchestration and provider selection.
- `providers.py` — AI-provider abstraction with OpenAI and Gemini adapters.
- `memory.py` — local SQLite persistence.
- `events.py` — lightweight synchronous event bus.
- `tools.py` — explicit tool registry with safety metadata and confirmation gates.
- `system.py` — bounded Windows-native system integration.
- `diagnostics.py` — health checks without making network calls.
- `__main__.py` — CLI entry point and interactive loop.

The core is provider-oriented and testable without external services. Optional browser, voice and UI adapters are kept outside the core dependency path. Cloud failures do not corrupt local memory. Secrets are loaded from environment variables and never committed to Git.
