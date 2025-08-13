from __future__ import annotations
from typing import Protocol, Dict

class LLM(Protocol):
    def generate(self, prompt: str) -> str: ...

class DeterministicMockLLM:
    """Deterministic, dependency-free mock LLM."""
    def __init__(self, routes: dict[str, str], default_response: str = "I don't know."):
        self.routes = routes or {}

    def generate(self, prompt: str) -> str:
        for k, v in self.routes.items():
            if k in prompt:
                return v
        if "Tool" in prompt and "returned:" in prompt:
            start = prompt.split("returned:", 1)[-1].strip()
            return f"Summary: {start[:180]}"
        return "Here is a brief answer."

class CostTracker:
    def __init__(self):
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.calls = 0

    def add_call(self, prompt_tokens: int, completion_tokens: int):
        self.calls += 1
        self.prompt_tokens += prompt_tokens
        self.completion_tokens += completion_tokens

    @property
    def total_tokens(self) -> int:
        return self.prompt_tokens + self.completion_tokens
