from __future__ import annotations

import argparse
import platform

from .config import load_settings
from .memory import MemoryStore


def main() -> int:
    parser = argparse.ArgumentParser(prog="jarvis")
    parser.add_argument("command", choices=["start", "doctor", "status", "memory"], nargs="?", default="start")
    args = parser.parse_args()
    settings = load_settings()

    if args.command == "doctor":
        print(f"Python/platform: {platform.python_version()} / {platform.system()}")
        print(f"Data directory: {settings.data_dir}")
        print(f"Provider: {settings.provider}")
        print(f"Gemini key configured: {'yes' if settings.gemini_api_key else 'no'}")
        MemoryStore(settings.data_dir)
        print("SQLite memory: OK")
        return 0

    if args.command == "status":
        print("JARVIS core: ready")
        print(f"Provider: {settings.provider}")
        return 0

    if args.command == "memory":
        for message in MemoryStore(settings.data_dir).recent():
            print(f"[{message['role']}] {message['content']}")
        return 0

    print("JARVIS core initialized. Configure GEMINI_API_KEY to enable AI conversation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
