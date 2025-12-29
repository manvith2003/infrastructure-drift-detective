from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app import models
from app.services.drift.detector import run_drift_scan
from app.services.llm.analyzer import generate_drift_explanation

router = APIRouter(
    prefix="/api/v1/drift",
    tags=["drift"],
)

# ================================
# Scan Drift (DETECT ONLY)
# ================================
@router.post("/scan/{project_id}")
def scan_drift(project_id: int, db: Session = Depends(get_db)):
    
    import os
    print("DATABASE_URL USED BY API:", os.getenv("DATABASE_URL"))

    # 1️⃣ Validate project
    project = (
        db.query(models.Project)
        .filter(models.Project.id == project_id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # 2️⃣ Run drift scan
    findings, terraform_state, cloud_state = run_drift_scan(project_id, db)

    # 3️⃣ Save snapshot
    snapshot = models.StateSnapshot(
        project_id=project_id,
        tf_state=terraform_state,
        actual_state=cloud_state,
    )
    db.add(snapshot)
    db.commit()
    db.refresh(snapshot)

    # 4️⃣ Save drift records (NO AI HERE)
    saved_drifts = []

    for drift in findings:
        record = models.DriftRecord(
            project_id=project_id,
            snapshot_id=snapshot.id,
            severity=drift["severity"],
            summary=f'{drift["resource"]} {drift["change_type"]}',
        )
        db.add(record)
        saved_drifts.append(record)

    db.commit()

    # 5️⃣ Response
    return {
        "project_id": project_id,
        "snapshot_id": snapshot.id,
        "drifts": [
            {
                "id": d.id,
                "severity": d.severity,
                "status": d.status,
                "summary": d.summary,
                "detected_at": d.detected_at,
            }
            for d in saved_drifts
        ],
    }


# ================================
# List Drifts
# ================================
@router.get("/")
def list_drifts(db: Session = Depends(get_db)):
    drifts = (
        db.query(models.DriftRecord)
        .order_by(models.DriftRecord.detected_at.desc())
        .all()
    )

    return [
        {
            "id": d.id,
            "project_id": d.project_id,
            "severity": d.severity,
            "status": d.status,
            "summary": d.summary,
            "detected_at": d.detected_at,
        }
        for d in drifts
    ]


# ================================
# Get Single Drift
# ================================
@router.get("/{drift_id}")
def get_drift(drift_id: int, db: Session = Depends(get_db)):
    drift = (
        db.query(models.DriftRecord)
        .filter(models.DriftRecord.id == drift_id)
        .first()
    )

    if not drift:
        raise HTTPException(status_code=404, detail="Drift not found")

    return {
        "id": drift.id,
        "project_id": drift.project_id,
        "snapshot_id": drift.snapshot_id,
        "severity": drift.severity,
        "status": drift.status,
        "summary": drift.summary,
        "explanation": drift.explanation,
        "detected_at": drift.detected_at,
    }


# ================================
# Analyze Drift (AI + Redis Cache)
# ================================
@router.post("/{drift_id}/analyze")
def analyze_drift(drift_id: int, db: Session = Depends(get_db)):
    drift = (
        db.query(models.DriftRecord)
        .filter(models.DriftRecord.id == drift_id)
        .first()
    )
    if not drift:
        raise HTTPException(status_code=404, detail="Drift not found")

    snapshot = (
        db.query(models.StateSnapshot)
        .filter(models.StateSnapshot.id == drift.snapshot_id)
        .first()
    )

    explanation = generate_drift_explanation(
        drift_id=drift.id,
        summary=drift.summary,
        terraform_state=snapshot.tf_state,
        cloud_state=snapshot.actual_state,
    )

    drift.explanation = explanation
    drift.status = "acknowledged"
    db.commit()

    return {
        "drift_id": drift.id,
        "explanation": explanation,
    }
