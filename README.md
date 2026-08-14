# JARVIS

Windows-first modular personal AI assistant foundation.

## Status

This repository is being built as a tested, maintainable JARVIS implementation. The core is designed to remain useful without optional cloud/browser/UI integrations.

## Requirements

- Windows 10/11
- Python 3.11+
- Optional Google Gemini API key
- Optional Brave/Chromium browser for browser tools

## Quick start

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

Optional integrations:

```powershell
pip install -e ".[browser]"
python -m playwright install chromium
pip install -e ".[voice]"
pip install -e ".[ui]"
```

See `docs/` for architecture, configuration, security, and tool documentation.

## Principles

- No hard-coded secrets.
- Dangerous actions require explicit permission.
- Optional integrations fail gracefully rather than pretending success.
- Core functionality is testable without external services.
- External services are isolated behind adapters.

## License

MIT
