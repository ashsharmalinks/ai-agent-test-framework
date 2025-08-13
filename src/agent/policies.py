from __future__ import annotations
import re

class SafetyPolicy:
    def allow(self, text: str) -> bool:
        raise NotImplementedError
    def post_filter(self, text: str) -> str:
        return text

class DefaultSafetyPolicy(SafetyPolicy):
    blocked_patterns = [
        r"(?i)how to build a bomb",
        r"(?i)credit card numbers?",
    ]

    def allow(self, text: str) -> bool:
        return not any(re.search(p, text) for p in self.blocked_patterns)

    def post_filter(self, text: str) -> str:
        text = re.sub(r"[\w\.]+@[\w\.]+", "[redacted email]", text)
        text = re.sub(r"\b\+?\d{10,15}\b", "[redacted phone]", text)
        return text

default_policy = DefaultSafetyPolicy()
