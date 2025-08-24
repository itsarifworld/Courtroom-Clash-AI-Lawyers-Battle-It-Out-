# Report — Courtroom Clash (Learning Edition)

## Goal
Prototype a courtroom debate between a **RAG Lawyer** and a **Chaos Lawyer** with the user as Judge.

## What I Completed
- Built a working FastAPI backend with **three complete routes**:
  - `/generate_case`, `/debate`, `/judge_decision`
- Added a **complete mini-dataset** of precedents (`legal_cases.json`)
- Wrote **partial models** (good enough for end-to-end flow)
- Implemented a **minimal RAG** (keyword-only) and a working **Chaos** generator
- Conducted web scraping from the IndiaKanoon website to extract IPC laws, which wasn’t fully integrated yet but served as a valuable exploration and preparation step.

## What Is Incomplete (and Why)
- Starting from no prior experience, I embraced the challenge of building a RAG retrieval system, initially focusing on keyword scoring as a foundation to grow from.
- The metadata store is currently in-memory, reflecting an early stage in understanding persistence and data management, with plans to deepen this knowledge.
- Models are partially typed, representing a learning curve in balancing rapid iteration with robust type safety.
- `retrieval.py` is a stub, marking the beginning of a more sophisticated hybrid pipeline I am determined to develop.

Each of these areas highlights the growth and determination involved in tackling complex concepts step-by-step, turning gaps into opportunities for learning and improvement.

## What I Learned
- Gained hands-on experience with FastAPI routing and Pydantic schema validation.
- Developed an appreciation for designing request/response models first to stabilize interfaces.
- Learned the value of separating routes and services to enable easy swapping of logic.
- Most importantly, built confidence in navigating unfamiliar territory and iterating through challenges with persistence.

## Next Steps
1. Confidently implement TF–IDF + cosine similarity (scikit-learn) to enhance retrieval.
2. Expand semantic understanding by adding embeddings (sentence-transformers).
3. Improve re-ranking with richer metadata (case_type/jurisdiction/principles).
4. Advance persistence by integrating SQLite for judgments and evidence, and create filtered query endpoints.

This journey continues with determination to deepen expertise and build more powerful, reliable systems.
