import json
import subprocess
from pathlib import Path


class TerraformPlanError(Exception):
    pass


def run_terraform_plan(tf_dir: str) -> dict:
    tf_path = Path(tf_dir)

    if not tf_path.exists():
        raise TerraformPlanError(f"Terraform directory not found: {tf_dir}")

    plan_file = tf_path / "tfplan"

    # ✅ VERY IMPORTANT: remove old plan
    if plan_file.exists():
        plan_file.unlink()

    # 1️⃣ Fresh terraform plan
    plan_proc = subprocess.run(
        ["terraform", "plan", "-out=tfplan", "-no-color"],
        cwd=tf_path,
        capture_output=True,
        text=True,
    )

    if plan_proc.returncode != 0:
        raise TerraformPlanError(plan_proc.stderr)

    # 2️⃣ Convert plan to JSON
    show_proc = subprocess.run(
        ["terraform", "show", "-json", "tfplan"],
        cwd=tf_path,
        capture_output=True,
        text=True,
    )

    if show_proc.returncode != 0:
        raise TerraformPlanError(show_proc.stderr)

    return json.loads(show_proc.stdout)
