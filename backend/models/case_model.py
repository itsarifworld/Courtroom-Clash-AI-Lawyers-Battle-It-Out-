from pydantic import BaseModel
from typing import Optional, List, Literal, Dict, Any

CaseType = Literal["defamation", "property", "privacy", "criminal", "public safety", "other"]

class Metadata(BaseModel):
    case_type: CaseType = "other"
    jurisdiction: str = "US"
    year: Optional[int] = None
    key_legal_principles: List[str] = []
    # TODO: add parties/outcome later for richer display

class CaseScenario(BaseModel):
    id: Optional[str] = None
    case: str
    metadata: Optional[Metadata] = None

class CaseGenerateRequest(BaseModel):
    prompt: Optional[str] = None
    seed: Optional[int] = None

class CaseResponse(BaseModel):
    scenario: CaseScenario
