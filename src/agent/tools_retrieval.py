# src/agent/tools_retrieval.py
from typing import List, Optional

class RetrievalTool:
    name: str = "retrieval"
    description: str = "Naive in-memory keyword retriever for tests."

    def __init__(self, docs: Optional[List[str]] = None) -> None:
        self.docs: List[str] = list(docs) if docs else []

    def add_docs(self, new_docs: List[str]) -> None:
        self.docs.extend(new_docs)

    def search(self, query: str, k: int = 3) -> List[str]:
        if not query or not self.docs:
            return []
        q_tokens = {t for t in query.lower().split() if t.isalpha()}
        scored = []
        for d in self.docs:
            d_low = d.lower()
            hits = sum(1 for t in q_tokens if t in d_low)
            if hits:
                scored.append((hits, d))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [d for _, d in scored[:k]]

    def __call__(self, query: str) -> str:
        # Optional prefix support
        pref = "tool:retrieval:"
        if query.lower().startswith(pref):
            query = query[len(pref):].strip()

        matches = self.search(query, k=3)
        return "No results." if not matches else " | ".join(matches)
