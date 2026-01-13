from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from orchestrator.database import get_db
from orchestrator import models

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/{job_id}")
def get_logs(job_id: str, db: Session = Depends(get_db)):
    logs = db.query(models.Log).filter(models.Log.job_id == job_id).all()
    return [{"message": l.message} for l in logs]
