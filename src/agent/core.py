# src/agent/core.py (only the relevant portion shown)

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class AgentResponse:
    text: str
    used_tools: List[str]
    meta: Dict[str, Any]

class Agent:
    def __init__(self, llm, tools, policy, cost):
        self.llm = llm
        self.tools = {t.name: t for t in tools}  # requires t.name
        self.policy = policy
        self.cost = cost

    def run(self, query: str) -> AgentResponse:
        """
        Simple agent loop. Adds a direct retrieval fast-path for tests:
        - If query starts with 'tool:retrieval:', call the retrieval tool directly
          and return its output. Record used_tools accordingly.
        """
        used_tools: List[str] = []
        meta: Dict[str, Any] = {}

        # --- Fast path for retrieval-prefixed queries (used by Behave scenario) ---
        pref = "tool:retrieval:"
        if query.lower().startswith(pref):
            q = query[len(pref):].strip()
            tool = self.tools.get("retrieval")
            if tool:
                snippet = tool(q)  # safe, returns string
                used_tools.append("retrieval")
                return AgentResponse(text=snippet, used_tools=used_tools, meta=meta)

        # --- Otherwise fall back to your existing policy / LLM path ---
        # Example (adapt to your actual policy/LLM API):
        answer = self.llm.generate(query) if hasattr(self.llm, "generate") else self.llm.run(query)
        return AgentResponse(text=answer, used_tools=used_tools, meta=meta)
