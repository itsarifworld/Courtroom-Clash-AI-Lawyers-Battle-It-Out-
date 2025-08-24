# Courtroom Clash (Incomplete Backend)
## What is Complete
- **Routes (API):**
  - `POST /generate_case` → returns quirky scenario + basic metadata
  - `POST /debate` → returns RAG (minimal) + Chaos (working) arguments
  - `POST /judge_decision` → stores verdict to `backend/data/judgments.json`
- **Data:** `backend/data/legal_cases.json` (a small but complete mini-dataset)
- **Requirements:** `requirements.txt` is production-ready with future deps included

## What is Incomplete (By Design)
- **Services:**
  - `services/rag_lawyer.py` → *keyword-only* retrieval (no TF-IDF/embeddings yet)
  - `services/metadata_store.py` → in-memory only
  - `services/case_generator.py` → simple heuristics
- **Models (Pydantic):**
  - `models/*` → partial schemas, missing stricter types & fields
- **Utils:**
  - `utils/retrieval.py` → just a placeholder for hybrid retrieval

## Why Each Dependency (requirements.txt)
- `fastapi` → to define the API quickly and cleanly
- `uvicorn[standard]` → ASGI server to run the FastAPI app
- `pydantic` → request/response validation and clear models
- `numpy` → planned vector math for ranking
- `scikit-learn` → planned TF–IDF and cosine similarity
- `sentence-transformers` → planned semantic embeddings for RAG
- `python-dotenv` → environment variable management (future config)

## Run
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open the interactive docs at: http://127.0.0.1:8000/docs

## Endpoints
- `POST /generate_case`
- `POST /debate`
- `POST /judge_decision`
