from __future__ import annotations

import argparse
import platform

from .app import Assistant
from .config import load_settings
from .diagnostics import run_checks
from .memory import MemoryStore


def main() -> int:
    parser = argparse.ArgumentParser(prog="jarvis")
    parser.add_argument("command", choices=["start", "doctor", "status", "memory"], nargs="?", default="start")
    args = parser.parse_args()
    settings = load_settings()

    if args.command == "doctor":
        print(f"Python/platform: {platform.python_version()} / {platform.system()}")
        failed = False
        for check in run_checks(settings):
            print(f"{'OK' if check.ok else 'FAIL':4} {check.name}: {check.detail}")
            failed |= not check.ok
        return int(failed)

    if args.command == "status":
        print("JARVIS core: ready")
        print(f"Provider: {settings.provider}")
        print(f"Model: {settings.model}")
        return 0

    if args.command == "memory":
        for message in MemoryStore(settings.data_dir).recent():
            print(f"[{message['role']}] {message['content']}")
        return 0

    try:
        assistant = Assistant.create(settings)
    except Exception as exc:
        print(f"JARVIS could not start: {exc}")
        print("Run `python -m jarvis doctor` for diagnostics.")
        return 1

    print("JARVIS online. Type 'exit' or 'quit' to stop.")
    while True:
        try:
            text = input("You > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if text.lower() in {"exit", "quit"}:
            break
        if not text:
            continue
        try:
            print(f"JARVIS > {assistant.ask(text)}")
        except Exception as exc:
            print(f"JARVIS error: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
