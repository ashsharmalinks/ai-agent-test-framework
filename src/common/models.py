from pydantic import BaseModel
from typing import List, Dict, Any

class ChatIn(BaseModel):
    query: str

class ChatOut(BaseModel):
    text: str
    used_tools: List[str]
    meta: Dict[str, Any]
