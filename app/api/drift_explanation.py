from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.database import get_db
from app import models

router = APIRouter(
    prefix="/api/v1/drift",
    tags=["drift"],
)


class DriftExplanationRequest(BaseModel):
    drift_id: int
    explanation: str


@router.post("/explain")
def save_drift_explanation(
    payload: DriftExplanationRequest,
    db: Session = Depends(get_db),
):
    drift = (
        db.query(models.DriftRecord)
        .filter(models.DriftRecord.id == payload.drift_id)
        .first()
    )

    if not drift:
        raise HTTPException(status_code=404, detail="Drift not found")

    drift.explanation = payload.explanation
    db.commit()
    db.refresh(drift)

    return {
        "drift_id": drift.id,
        "status": "explanation_saved",
    }
