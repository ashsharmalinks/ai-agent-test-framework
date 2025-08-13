# tests/ui/test_ui_smoke.py
import os
import socket
import subprocess
import time
import requests
import pytest

pytestmark = pytest.mark.slow

PORT = int(os.getenv("UI_PORT", "8000"))
BASE = f"http://127.0.0.1:{PORT}"

def _port_in_use(port: int) -> bool:
    """Check if the given port is already being used."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.2)
        return s.connect_ex(("127.0.0.1", port)) == 0

@pytest.mark.skipif(os.getenv("RUN_UI") != "1", reason="Set RUN_UI=1 to run UI smoke test.")
def test_ui_smoke():
    proc = None

    # Start server only if not already running
    if not _port_in_use(PORT):
        proc = subprocess.Popen(
            ["python", "-m", "uvicorn", "src.server.main:app", "--port", str(PORT)],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )

        # Wait for server to start
        deadline = time.time() + 15
        while time.time() < deadline:
            try:
                if requests.get(f"{BASE}/health", timeout=0.5).ok:
                    break
            except Exception:
                pass
            time.sleep(0.2)
        else:
            pytest.fail("UI server did not start within timeout")

    # Test UI behaviour via API
    r = requests.post(f"{BASE}/chat", json={"query": "What is 2+2?"}, timeout=5.0)
    assert r.ok
    assert r.json().get("text")

    if proc:
        proc.terminate()
