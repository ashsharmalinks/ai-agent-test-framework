from __future__ import annotations
import subprocess, time, requests
from .config import CFG

def start_server() -> subprocess.Popen:
    proc = subprocess.Popen(["python", "-m", "uvicorn", "server.main:app",
                             "--host", CFG.host, "--port", str(CFG.port)])
    # wait for readiness
    base = f"http://{CFG.host}:{CFG.port}"
    for _ in range(60):
        try:
            if requests.get(f"{base}/health", timeout=0.5).ok: break
        except Exception: pass
        time.sleep(0.2)
    else:
        proc.terminate()
        raise RuntimeError("API failed to start")
    return proc

def stop_server(proc: subprocess.Popen) -> None:
    proc.terminate()
