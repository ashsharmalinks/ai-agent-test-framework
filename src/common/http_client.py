# BEFORE (problem): from server.main import app  ❌  causes circular import

# AFTER:
import requests
from src.common.config import CFG

def make_client():
    """
    Returns a tiny HTTP client bound to CFG.base_url for Behave steps.
    """
    class Client:
        base = CFG.base_url
        def _url(self, path: str) -> str:
            return path if path.startswith("http") else f"{self.base}{path}"
        def get(self, path: str, **kw):  return requests.get(self._url(path), **kw)
        def post(self, path: str, **kw): return requests.post(self._url(path), **kw)
    return Client()
