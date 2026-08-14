from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol


class AIProvider(Protocol):
    def generate(self, messages: Sequence[dict[str, str]]) -> str: ...


class OpenAIProvider:
    def __init__(self, api_key: str, model: str = "gpt-5.6") -> None:
        if not api_key:
            raise ValueError("An OpenAI API key is required")
        from openai import OpenAI

        self._client = OpenAI(api_key=api_key)
        self._model = model

    def generate(self, messages: Sequence[dict[str, str]]) -> str:
        response = self._client.responses.create(model=self._model, input=list(messages))
        text = getattr(response, "output_text", None)
        if not text:
            raise RuntimeError("OpenAI returned no text")
        return text.strip()


class GeminiProvider:
    def __init__(self, api_key: str, model: str) -> None:
        if not api_key:
            raise ValueError("A Gemini API key is required")
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
