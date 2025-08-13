"""
Central configuration used by server and tests.
You can override via environment variables if needed.
"""

from dataclasses import dataclass

@dataclass
class Config:
    host: str = "127.0.0.1"
    port: int = 8000
    base_url: str = "http://127.0.0.1:8000"

CFG = Config()
