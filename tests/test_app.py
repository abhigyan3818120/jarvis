from pathlib import Path

from jarvis.app import Assistant
from jarvis.config import Settings
from jarvis.events import EventBus
from jarvis.memory import MemoryStore


class FakeProvider:
    def generate(self, messages):
        assert messages[-1]["role"] == "user"
        return "pong"


def test_assistant_persists_conversation(tmp_path: Path) -> None:
    assistant = Assistant(Settings(data_dir=tmp_path), MemoryStore(tmp_path), EventBus(), FakeProvider())
    assert assistant.ask("ping") == "pong"
    assert assistant.memory.recent()[-1] == {"role": "assistant", "content": "pong"}


def test_event_bus() -> None:
    bus = EventBus()
    received = []
    bus.subscribe("answer", received.append)
    bus.publish("answer", "ok")
    assert received == ["ok"]
