# Configuration

JARVIS reads `.env` through `python-dotenv`.

| Variable | Default | Purpose |
|---|---|---|
| `JARVIS_PROVIDER` | `openai` | `openai` or `gemini` |
| `OPENAI_API_KEY` | empty | OpenAI credential |
| `GEMINI_API_KEY` | empty | Gemini credential |
| `JARVIS_MODEL` | `gpt-5.6` | Model passed to the selected provider |
| `JARVIS_DATA_DIR` | `~/.jarvis` | Local SQLite data directory |
| `JARVIS_LOG_LEVEL` | `INFO` | Application log level |
| `JARVIS_CONFIRM_DANGEROUS` | `true` | Default safety policy flag |

The repository contains only `.env.example`; a real `.env` is intentionally ignored by Git.
