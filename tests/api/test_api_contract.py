from common.models import ChatOut

def test_health(http):
    r = http.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_chat_contract(http):
    r = http.post("/chat", json={"query":"What is 2+2?"})
    assert r.status_code == 200
    data = ChatOut.model_validate(r.json())
    assert data.text and isinstance(data.used_tools, list) and isinstance(data.meta, dict)
