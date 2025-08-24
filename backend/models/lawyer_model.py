from pydantic import BaseModel
from typing import Optional, List, Dict, Any

# PARTIAL: Missing confidence/weights; enough to shape responses.

class RAGArgument(BaseModel):
    argument: str
    citation: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    retrieved: Optional[List[Dict[str, Any]]] = None  # TODO: define stricter schema

class ChaosArgument(BaseModel):
    argument: str
    rhetoric: Optional[str] = None

class DebateRequest(BaseModel):
    case: str
    metadata: Optional[Dict[str, Any]] = None
    k: int = 3
    alpha: float = 0.5

class DebateResponse(BaseModel):
    case: str
    rag_lawyer: RAGArgument
    chaos_lawyer: ChaosArgument
    judge_decision: str = "Pending user input."
