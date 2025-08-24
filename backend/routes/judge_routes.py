from fastapi import APIRouter
from ..models.debate_model import JudgeDecisionRequest, JudgeDecisionResponse
import os, json, time

router = APIRouter()
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
JUDG_FILE = os.path.join(DATA_DIR, "judgments.json")

def _load():
    if not os.path.exists(JUDG_FILE):
        return []
    try:
        with open(JUDG_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

@router.post("/judge_decision", response_model=JudgeDecisionResponse)
def judge_decision_route(req: JudgeDecisionRequest):
    """Complete: persists decision to a JSON file for traceability."""
    store = _load()
    rec = {
        "ts": int(time.time()),
        "case": req.case,
        "winner": req.winner,
        "new_evidence": req.new_evidence,
        "metadata_updates": req.metadata_updates,
    }
    store.append(rec)
    with open(JUDG_FILE, "w") as f:
        json.dump(store, f, indent=2)
    return JudgeDecisionResponse(status="saved", saved_as=f"judgments.json[{len(store)-1}]")
