from typing import Dict, Any, List, Tuple
import json, os

class RAGLawyer:
    def __init__(self, data_path: str):
        self.data_path = data_path
        with open(self.data_path, "r") as f:
            self.cases = json.load(f)

    def _keyword_score(self, query: str, entry: Dict[str, Any]) -> float:
        """Very naive keyword scorer (incomplete)."""
        q = query.lower().split()
        text = (entry.get("title","") + " " + entry.get("summary","")).lower()
        return sum(1 for token in q if token in text) / max(1, len(q))

    def search(self, query: str, k: int = 3, metadata: Dict[str, Any] | None = None) -> List[Tuple[float, Dict[str, Any]]]:
        # INCOMPLETE: only keyword scoring, no vector embeddings.
        scored = [(self._keyword_score(query, c), c) for c in self.cases]
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[:k]

    def argue(self, case_text: str, metadata: Dict[str, Any] | None, k: int = 3, alpha: float = 0.5) -> Dict[str, Any]:
        hits = self.search(case_text, k=k, metadata=metadata or {})
        if not hits or hits[0][0] == 0:
            return {
                "argument": "No strong precedent found. (RAG incomplete) General principles may still apply (e.g., need for intent/publication in defamation).",
                "citation": None,
                "metadata": metadata or {},
                "retrieved": [{"score": float(s), "title": h.get("title")} for s, h in hits],
            }
        score, top = hits[0]
        arg = (
            f"Referencing {top['title']} ({top['year']}, {top['jurisdiction']}): {top['summary']} "
            f"Given the overlap, this weakly supports our position. (Note: retrieval is keyword-only)"
        )
        return {
            "argument": arg,
            "citation": f"{top['title']}, {top['year']} ({top['jurisdiction']})",
            "metadata": {
                "case_type": top.get("case_type"),
                "jurisdiction": top.get("jurisdiction"),
                "year": top.get("year"),
                "key_legal_principles": top.get("key_legal_principles", []),
                "outcome": top.get("outcome"),
            },
            "retrieved": [{"score": float(s), **h} for s, h in hits],
        }
