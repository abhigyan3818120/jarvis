from pathlib import Path

from jarvis.config import load_settings
from jarvis.memory import MemoryStore
from jarvis.tools import Tool, ToolRegistry


def test_memory_round_trip(tmp_path: Path) -> None:
    store = MemoryStore(tmp_path)
    store.add("user", "hello")
    store.add("assistant", "hi")
    assert store.recent() == [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi"},
    ]


def test_tool_registry_rejects_duplicates() -> None:
    registry = ToolRegistry()
    registry.register(Tool("ping", "Ping", lambda: "pong"))
    try:
        registry.register(Tool("ping", "Ping", lambda: "pong"))
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate tool was accepted")


def test_settings_defaults(monkeypatch) -> None:
    monkeypatch.delenv("JARVIS_PROVIDER", raising=False)
    monkeypatch.delenv("JARVIS_MODEL", raising=False)
    settings = load_settings()
    assert settings.provider == "gemini"
    assert settings.model
