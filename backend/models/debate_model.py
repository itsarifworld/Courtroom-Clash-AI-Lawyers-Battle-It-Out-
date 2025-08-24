from pydantic import BaseModel
from typing import Optional, Dict, Any



class JudgeDecisionRequest(BaseModel):
    case: str
    winner: str  # 'rag' or 'chaos'
    new_evidence: Optional[str] = None
    metadata_updates: Optional[Dict[str, Any]] = None

class JudgeDecisionResponse(BaseModel):
    status: str
    saved_as: str
