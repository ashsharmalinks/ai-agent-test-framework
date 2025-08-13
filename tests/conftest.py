# tests/conftest.py
import os
import time
import requests
import pytest

from agent.core import Agent
from agent.llm_providers import DeterministicMockLLM, CostTracker
from agent.tools import SearchTool, MathTool
from agent.policies import default_policy
from agent.tools_retrieval import RetrievalTool

# ---- Config (env overrides are optional) ------------------------------------
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))
BASE_URL = f"http://{API_HOST}:{API_PORT}"

# ---- Agent-side fixtures (unit/integration without HTTP) --------------------
@pytest.fixture
def llm():
    # deterministic mock routes for stable tests
    return DeterministicMockLLM(
        routes={
            "What is 2+2?": "4",
            "capital of France": "Paris",
            "Tell me about the sun": "The Sun is a star at the center of our solar system that produces solar energy.",
            "Capital of the UK": "London is the capital city of England and the UK.",
        }
    )

@pytest.fixture
def tools():
    return [SearchTool(), MathTool(), RetrievalTool()]

@pytest.fixture
def cost():
    return CostTracker()

@pytest.fixture
def agent(llm, tools, cost):
    return Agent(llm=llm, tools=tools, policy=default_policy, cost=cost)

# ---- HTTP client fixture (for API contract tests) ---------------------------
@pytest.fixture
def http():
    """
    Lightweight wrapper around requests that targets the running FastAPI server.
    Tests using this fixture REQUIRE the server to be up, e.g.:
        uvicorn server.main:app --reload --port 8000
    You can override host/port with API_HOST / API_PORT env vars.
    """
    # quick health probe; skip gracefully if the API isn't up
    try:
        r = requests.get(f"{BASE_URL}/health", timeout=0.5)
        if r.status_code != 200:
            pytest.skip(f"API not healthy at {BASE_URL}/health (status {r.status_code}). "
                        f"Start it with: uvicorn server.main:app --port {API_PORT}")
    except Exception:
        pytest.skip(f"API not reachable at {BASE_URL}. "
                    f"Start it with: uvicorn server.main:app --port {API_PORT}")

    class HttpClient:
        base_url = BASE_URL

        def _url(self, path: str) -> str:
            return path if path.startswith("http") else f"{self.base_url}{path}"

        def get(self, path: str, **kwargs):
            return requests.get(self._url(path), **kwargs)

        def post(self, path: str, **kwargs):
            return requests.post(self._url(path), **kwargs)

    return HttpClient()
