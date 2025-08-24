from fastapi import APIRouter
from ..models.case_model import CaseGenerateRequest, CaseResponse, CaseScenario
from ..services.case_generator import generate_case

router = APIRouter()

@router.post("/generate_case", response_model=CaseResponse)
def generate_case_route(req: CaseGenerateRequest):
    """Complete: returns a generated or user-prompted quirky case + basic inferred metadata."""
    scenario = generate_case(prompt=req.prompt, seed=req.seed)
    return CaseResponse(scenario=CaseScenario(**scenario))
