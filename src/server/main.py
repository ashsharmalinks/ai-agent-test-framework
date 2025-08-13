from fastapi import FastAPI
from pydantic import BaseModel
from agent import Agent, DeterministicMockLLM, SearchTool, MathTool, default_policy, CostTracker
from agent.tools_retrieval import RetrievalTool
from src.common.agent_factory import get_agent  # ← use your singleton
import time
from fastapi import HTTPException

app = FastAPI(title="AI Agent API")

def build_agent():
    routes = {
        "What is 2+2?": "4",
        "capital of France": "Paris",
        "Who wrote Hamlet?": "William Shakespeare",
        "Tell me about the sun": "The Sun is a star at the center of our solar system that produces solar energy.",
        "Capital of the UK": "London is the capital city of England and the UK.",
    }
    llm = DeterministicMockLLM(routes=routes)
    tools = [SearchTool(), MathTool(), RetrievalTool()]
    return Agent(llm=llm, tools=tools, policy=default_policy, cost=CostTracker())

AGENT = build_agent()

class ChatIn(BaseModel):
    query: str

class ChatOut(BaseModel):
    text: str
    used_tools: list[str]
    meta: dict

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatOut)
def chat(inp: ChatIn) -> ChatOut:
    """
    Run the query through the singleton Agent and return a stable schema.

    Guarantees:
      - text: str (never None)
      - used_tools: list[str] (never None)
      - meta: dict with at least:
          - cost: float (0.0 if unavailable)
          - latency_ms: float (rounded to 2 decimals)
    """
    agent = get_agent()

    t0 = time.perf_counter()
    try:
        res = agent.run(inp.query)
    except Exception as e:
        # Surface a clean 500 with context instead of crashing
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")

    latency_ms = (time.perf_counter() - t0) * 1000.0

    # Normalize fields so the response model is always satisfied
    text = str(getattr(res, "text", "") or "")
    used_tools = list(getattr(res, "used_tools", []) or [])
    meta = dict(getattr(res, "meta", {}) or {})

    # Cost: robust, Pylance-friendly
    cost_total = getattr(getattr(agent, "cost", None), "total", 0.0)
    try:
        cost_total = float(cost_total)
    except Exception:
        cost_total = 0.0

    meta.setdefault("cost", cost_total)
    meta["latency_ms"] = round(float(latency_ms), 2)

    return ChatOut(text=text, used_tools=used_tools, meta=meta)
# Minimal UI
from starlette.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html><html><head><meta charset="utf-8"><title>AI Agent</title></head>
    <body style="font-family: system-ui, sans-serif; max-width: 720px; margin: 2rem auto;">
      <h1>AI Agent Demo</h1>
      <p>Try queries like <code>What is 2+2?</code> or <code>tool:retrieval: safety checks in agents</code>.</p>
      <form id="f">
        <input id="q" name="q" placeholder="Ask something..." style="width:80%">
        <button>Send</button>
      </form>
      <pre id="out" style="white-space: pre-wrap; background:#f6f6f6; padding:1rem; border-radius:8px; margin-top:1rem;"></pre>
      <script>
        const f = document.getElementById('f');
        const q = document.getElementById('q');
        const out = document.getElementById('out');
        f.onsubmit = async (e) => {
          e.preventDefault();
          const r = await fetch('/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({query: q.value})});
          const j = await r.json();
          out.textContent = 'Response: ' + j.text + '\nUsed tools: ' + j.used_tools.join(', ');
        };
      </script>
    </body></html>
    """
