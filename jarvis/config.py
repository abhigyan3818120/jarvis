from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    provider: str = "gemini"
    model: str = "gemini-2.5-flash"
    data_dir: Path = Path.home() / ".jarvis"
    log_level: str = "INFO"
    confirm_dangerous: bool = True
    gemini_api_key: str | None = None


def load_settings() -> Settings:
    load_dotenv()
    data = Path(os.getenv("JARVIS_DATA_DIR", "~/.jarvis")).expanduser()
    return Settings(
        provider=os.getenv("JARVIS_PROVIDER", "gemini"),
        model=os.getenv("JARVIS_MODEL", "gemini-2.5-flash"),
        data_dir=data,
        log_level=os.getenv("JARVIS_LOG_LEVEL", "INFO").upper(),
        confirm_dangerous=os.getenv("JARVIS_CONFIRM_DANGEROUS", "true").lower() in {"1", "true", "yes"},
        gemini_api_key=os.getenv("GEMINI_API_KEY") or None,
    )
