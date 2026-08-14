from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol


class AIProvider(Protocol):
    def generate(self, messages: Sequence[dict[str, str]]) -> str: ...


class GeminiProvider:
    def __init__(self, api_key: str, model: str) -> None:
        if not api_key:
            raise ValueError("A Gemini API key is required for the Gemini provider")
        from google import genai

        self._client = genai.Client(api_key=api_key)
        self._model = model

    def generate(self, messages: Sequence[dict[str, str]]) -> str:
        prompt = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
        response = self._client.models.generate_content(model=self._model, contents=prompt)
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned no text")
        return text.strip()
