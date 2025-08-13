# src/common/agent_factory.py
from typing import Dict, List
from agent import Agent, DeterministicMockLLM, SearchTool, MathTool, default_policy, CostTracker
from agent.tools_retrieval import RetrievalTool

_ROUTES: Dict[str, str] = {
    "What is 2+2?": "4",
    "capital of France": "Paris",
    "Who wrote Hamlet?": "William Shakespeare",
    "Tell me about the sun": "The Sun is a star at the center of our solar system that produces solar energy.",
    "Capital of the UK": "London is the capital city of England and the UK.",
}

_DOCS: List[str] = [
    "The Sun is a star at the center of our solar system, source of solar radiation.",
    "London is the capital of England and the UK.",
]

_cost = CostTracker()
_llm  = DeterministicMockLLM(routes=_ROUTES)
_rt   = RetrievalTool(docs=_DOCS)
_tools = [SearchTool(), MathTool(), _rt]

AGENT  = Agent(llm=_llm, tools=_tools, policy=default_policy, cost=_cost)

def get_agent() -> Agent:
    return AGENT
