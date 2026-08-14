from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: Callable[..., object]
    dangerous: bool = False


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise KeyError(f"Unknown tool: {name}") from exc

    def names(self) -> list[str]:
        return sorted(self._tools)

    def execute(self, name: str, *, confirmed: bool = False, **kwargs: object) -> object:
        tool = self.get(name)
        if tool.dangerous and not confirmed:
            raise PermissionError(f"tool '{name}' requires explicit confirmation")
        return tool.handler(**kwargs)
