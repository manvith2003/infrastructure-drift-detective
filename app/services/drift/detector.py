from app.services.terraform.scanner import scan_terraform_project
from app import models
from sqlalchemy.orm import Session


def run_drift_scan(project_id: int, db: Session):
    # 1️⃣ Load project from DB
    project = (
        db.query(models.Project)
        .filter(models.Project.id == project_id)
        .first()
    )

    if not project:
        raise ValueError("Project not found")

    # 2️⃣ Build absolute Terraform path
    tf_path = project.tf_path

    if not tf_path.startswith("/app/"):
        tf_path = f"/app/{tf_path}"

    # 3️⃣ Run terraform scan
    drifts, tf_state, actual_state = scan_terraform_project(tf_path)

    return drifts, tf_state, actual_state
