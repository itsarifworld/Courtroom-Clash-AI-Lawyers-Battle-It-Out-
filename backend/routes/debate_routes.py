from fastapi import APIRouter
from ..models.lawyer_model import DebateRequest, DebateResponse, RAGArgument, ChaosArgument
from ..services.rag_lawyer import RAGLawyer
from ..services.chaos_lawyer import chaos_response
import os

router = APIRouter()

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "legal_cases.json")
rag = RAGLawyer(DATA_PATH)

@router.post("/debate", response_model=DebateResponse)
def debate_route(req: DebateRequest):
    """Complete: returns arguments from both lawyers. RAG is minimal (service incomplete but callable)."""
    rag_arg = rag.argue(req.case, req.metadata or {}, k=req.k, alpha=req.alpha)
    chaos_arg = chaos_response()
    return DebateResponse(case=req.case, rag_lawyer=RAGArgument(**rag_arg), chaos_lawyer=ChaosArgument(**chaos_arg))
