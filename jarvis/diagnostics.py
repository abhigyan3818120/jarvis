from __future__ import annotations

import importlib.util
from dataclasses import dataclass

from .config import Settings
from .memory import MemoryStore


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str


def run_checks(settings: Settings) -> list[Check]:
    checks: list[Check] = []
    checks.append(Check("data directory", True, str(settings.data_dir)))
    try:
        MemoryStore(settings.data_dir)
        checks.append(Check("sqlite memory", True, "ready"))
    except Exception as exc:  # pragma: no cover - platform/filesystem dependent
        checks.append(Check("sqlite memory", False, str(exc)))
    checks.append(Check("OpenAI SDK", importlib.util.find_spec("openai") is not None, "installed"))
    checks.append(Check("Gemini SDK", importlib.util.find_spec("google.genai") is not None, "installed"))
    key_ok = bool(settings.openai_api_key) if settings.provider == "openai" else bool(settings.gemini_api_key)
    checks.append(Check("provider credentials", key_ok, "configured" if key_ok else "not configured"))
    return checks
