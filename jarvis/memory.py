from __future__ import annotations

import sqlite3
from pathlib import Path


class MemoryStore:
    """Small local SQLite store for conversation history."""

    def __init__(self, data_dir: Path) -> None:
        data_dir.mkdir(parents=True, exist_ok=True)
        self.path = data_dir / "memory.sqlite3"
        self._init()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        return connection

    def _init(self) -> None:
        with self._connect() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS messages "
                "(id INTEGER PRIMARY KEY, role TEXT NOT NULL, content TEXT NOT NULL, created_at "
                "TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
            )

    def add(self, role: str, content: str) -> None:
        if not role or not content:
            raise ValueError("role and content are required")
        with self._connect() as db:
            db.execute("INSERT INTO messages(role, content) VALUES (?, ?)", (role, content))

    def recent(self, limit: int = 20) -> list[dict[str, str]]:
        if limit < 1:
            raise ValueError("limit must be positive")
        with self._connect() as db:
            rows = db.execute(
                "SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", (limit,)
            ).fetchall()
        return [dict(row) for row in reversed(rows)]
