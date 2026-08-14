# JARVIS

**J**ust **A** **R**easoning **V**irtual **I**ntelligence **S**ystem — a modular, Windows-first personal AI assistant.

JARVIS keeps the dependable pieces local (configuration, memory, diagnostics and tools) and puts cloud providers behind adapters. OpenAI is the default provider; Gemini remains supported.

## Included

- OpenAI Responses API integration
- Google Gemini integration
- Persistent local SQLite conversation memory
- Provider abstraction
- Event bus for UI/integration decoupling
- Explicit tool registry with confirmation gates for dangerous tools
- Bounded Windows system integration with `shell=False`
- `doctor`, `status`, `memory` and interactive `start` commands
- Pytest + Ruff CI on Python 3.11–3.13
- Optional browser, voice and PyQt6 dependency groups

## Requirements

- Windows 10/11
- Python 3.11+
- An OpenAI API key for the default provider

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -e ".[dev]"
Copy-Item .env.example .env
python -m jarvis doctor
python -m pytest -q
python -m jarvis start
```

Set `OPENAI_API_KEY` in your local `.env`. Secrets are ignored by Git and are never included in the repository.

To use Gemini instead, set `JARVIS_PROVIDER=gemini`, `GEMINI_API_KEY`, and an appropriate `JARVIS_MODEL`.

## Commands

```text
jarvis start       Interactive assistant
jarvis doctor      Environment and provider diagnostics
jarvis status      Core/provider status
jarvis memory      Recent local conversation memory
```

## Optional integrations

Browser, voice and UI dependencies are kept optional so the core remains lightweight. An integration is only considered complete when it has a real adapter and tests; unsupported external services are not faked.

## Security

JARVIS does not commit secrets. Dangerous tools require explicit confirmation. Command execution never uses `shell=True`.

See `docs/ARCHITECTURE.md` and `docs/SECURITY.md` for design details.

## License

MIT
