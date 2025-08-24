from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.case_routes import router as case_router
from .routes.debate_routes import router as debate_router
from .routes.judge_routes import router as judge_router

app = FastAPI(title="Courtroom Clash (Learning Edition)")

# CORS so a future frontend could talk to it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include complete routes
app.include_router(case_router, tags=["case"])
app.include_router(debate_router, tags=["debate"])
app.include_router(judge_router, tags=["judge"])

@app.get("/")
def root():
    return {"status": "ok", "message": "Courtroom Clash backend up", "routes": ["/generate_case", "/debate", "/judge_decision"]}
