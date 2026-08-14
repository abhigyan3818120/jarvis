from __future__ import annotations

import os
import platform
import subprocess
from pathlib import Path


def system_status() -> dict[str, str]:
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "cwd": str(Path.cwd()),
        "user": os.environ.get("USERNAME") or os.environ.get("USER") or "unknown",
    }


def open_path(path: str | Path) -> None:
    """Open a user-selected path using the native Windows shell."""
    target = Path(path).expanduser().resolve()
    if not target.exists():
        raise FileNotFoundError(target)
    if platform.system() != "Windows":
        raise OSError("open_path is a Windows-only integration")
    os.startfile(str(target))  # type: ignore[attr-defined]


def run_command(command: list[str], *, confirmed: bool = False) -> str:
    """Run an explicitly supplied command; shell=True is intentionally forbidden."""
    if not command:
        raise ValueError("command cannot be empty")
    if not confirmed:
        raise PermissionError("command execution requires explicit confirmation")
    result = subprocess.run(command, capture_output=True, text=True, shell=False, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"command exited with {result.returncode}")
    return result.stdout.strip()
