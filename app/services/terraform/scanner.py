from app.services.terraform.runner import run_terraform_plan
from app.services.terraform.parser import parse_resource_changes

def scan_terraform_project(tf_path: str):
    plan = run_terraform_plan(tf_path)
    resource_changes = plan.get("resource_changes", [])

    drifts = parse_resource_changes(
    resource_changes,
    plan.get("prior_state")
)

    return drifts, plan.get("prior_state"), plan.get("planned_values")
