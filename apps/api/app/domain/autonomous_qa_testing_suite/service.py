from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.autonomous_qa_testing_suite.models import AgenticAutonomousQaTestingSuiteSession, AgenticAutonomousQaTestingSuiteItem
from app.domain.autonomous_qa_testing_suite.schemas import AgenticAutonomousQaTestingSuiteSessionCreate, AgenticAutonomousQaTestingSuiteItemCreate

class AgenticAutonomousQaTestingSuiteService:
    @staticmethod
    def create_session(db: Session, data: AgenticAutonomousQaTestingSuiteSessionCreate) -> AgenticAutonomousQaTestingSuiteSession:
        db_obj = AgenticAutonomousQaTestingSuiteSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticAutonomousQaTestingSuiteSession:
        return db.query(AgenticAutonomousQaTestingSuiteSession).filter(AgenticAutonomousQaTestingSuiteSession.id == session_id).first()
