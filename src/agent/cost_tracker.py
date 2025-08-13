# agent/cost_tracker.py or agent/llm_providers.py (wherever CostTracker lives)
from typing import Union

class CostTracker:
    """
    Tracks the total cost of LLM queries.
    """
    total: float  # type annotation so Pylance knows it exists

    def __init__(self):
        self.total = 0.0

    def add(self, cost: Union[int, float]) -> None:
        """
        Increment the cost tracker.
        """
        self.total += float(cost)

    def reset(self) -> None:
        """
        Reset the cost tracker to zero.
        """
        self.total = 0.0
