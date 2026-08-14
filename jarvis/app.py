from __future__ import annotations

from dataclasses import dataclass

from .config import Settings
from .events import EventBus
from .memory import MemoryStore
from .providers import GeminiProvider, OpenAIProvider

SYSTEM_PROMPT = (
    "You are JARVIS, a concise, capable personal assistant. "
    "Be accurate, transparent about limitations, and never claim an action succeeded unless it did."
)


@dataclass
class Assistant:
    settings: Settings
    memory: MemoryStore
    events: EventBus
    provider: object

    @classmethod
    def create(cls, settings: Settings) -> "Assistant":
        memory = MemoryStore(settings.data_dir)
        events = EventBus()
        if settings.provider == "openai":
            provider = OpenAIProvider(settings.openai_api_key or "", settings.model)
        elif settings.provider == "gemini":
            provider = GeminiProvider(settings.gemini_api_key or "", settings.model)
        else:
            raise ValueError(f"Unsupported provider: {settings.provider}")
        return cls(settings, memory, events, provider)

    def ask(self, text: str) -> str:
        text = text.strip()
        if not text:
            raise ValueError("message cannot be empty")
        self.memory.add("user", text)
        messages = [{"role": "system", "content": SYSTEM_PROMPT}, *self.memory.recent()]
        answer = self.provider.generate(messages)  # type: ignore[attr-defined]
        self.memory.add("assistant", answer)
        self.events.publish("assistant.response", answer)
        return answer
