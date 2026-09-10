from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.autonomous_qa_testing_suite.schemas import AgenticAutonomousQaTestingSuiteSessionCreate, AgenticAutonomousQaTestingSuiteSessionResponse
from app.domain.autonomous_qa_testing_suite.service import AgenticAutonomousQaTestingSuiteService

router = APIRouter(prefix="/api/v1/autonomous_qa_testing_suite", tags=["Agentic Autonomous Qa Testing Suite Domain"])

@router.post("/sessions", response_model=AgenticAutonomousQaTestingSuiteSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticAutonomousQaTestingSuiteSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Autonomous Qa Testing Suite.
    """
    return AgenticAutonomousQaTestingSuiteService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticAutonomousQaTestingSuiteSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticAutonomousQaTestingSuiteService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
