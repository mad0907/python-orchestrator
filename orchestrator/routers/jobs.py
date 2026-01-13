from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from orchestrator.database import get_db
from orchestrator import models
import uuid

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/submit")
def submit_job(bot_id: str, payload: str, db: Session = Depends(get_db)):
    # Convert string bot_id to UUID
    bot_uuid = uuid.UUID(bot_id)

    # Create job with correct column names
    job = models.Job(
        bot_id=bot_uuid,        # Use UUID object
        script=payload,         # Use 'script' instead of 'payload'
        status="queued"
    )
    db.add(job)
    db.commit()
    db.refresh(job)  # optional, refresh to get any default fields populated
    return {"job_id": str(job.id)}
