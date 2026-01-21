from fastapi import APIRouter
from app.ai_agent.langgraph_agent import run_agent

router = APIRouter(prefix="/interactions")

@router.post("/log")
def log_interaction(text: str):
    return run_agent(text)
