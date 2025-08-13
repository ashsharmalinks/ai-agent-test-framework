from __future__ import annotations

class Tool:
    name: str
    def run(self, query: str) -> str:
        raise NotImplementedError

class SearchTool(Tool):
    name = "search"
    def run(self, query: str) -> str:
        return f"Top result for '{query}': Example Domain — example.com"

class MathTool(Tool):
    name = "math"
    def run(self, query: str) -> str:
        try:
            allowed = set("0123456789+-*/() ")
            if any(ch not in allowed for ch in query):
                return "Unsupported expression."
            return str(eval(query))
        except Exception as e:
            return f"Error: {e}"
