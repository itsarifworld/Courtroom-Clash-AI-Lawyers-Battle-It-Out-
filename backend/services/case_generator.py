from typing import Optional, Dict, Any
import random

QUIRKS = [
    "A man sues a parrot for defamation.",
    "A robot is accused of stealing electricity from a smart home.",
    "A ghost is put on trial for trespassing in an abandoned theater.",
    "A drone photobombs a wedding; florist sues for lost bouquet sales.",
]

def _infer_metadata(text: str) -> Dict[str, Any]:
    """Very shallow inference. TODO: expand with proper NER + rules."""
    t = text.lower()
    meta: Dict[str, Any] = {}
    if any(w in t for w in ["defamation", "libel", "slander", "parrot"]):
        meta["case_type"] = "defamation"
        meta["key_legal_principles"] = ["libel", "publication"]
    elif any(w in t for w in ["privacy", "record", "consent"]):
        meta["case_type"] = "privacy"
        meta["key_legal_principles"] = ["consent", "expectation of privacy"]
    elif any(w in t for w in ["drone", "trespass", "property", "garden"]):
        meta["case_type"] = "property"
        meta["key_legal_principles"] = ["trespass", "nuisance"]
    else:
        meta["case_type"] = "other"
        meta["key_legal_principles"] = []
    meta.setdefault("jurisdiction", "US")
    return meta

def generate_case(prompt: Optional[str] = None, seed: Optional[int] = None) -> Dict[str, Any]:
    """Returns a dict usable by CaseScenario. Service is simple but complete enough."""
    if seed is not None:
        random.seed(seed)
    text = (prompt or random.choice(QUIRKS)).strip()
    return {"id": None, "case": text, "metadata": _infer_metadata(text)}
