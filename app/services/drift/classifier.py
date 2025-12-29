from dataclasses import dataclass


@dataclass
class DriftFinding:
    resource: str          # resource identifier (name / key)
    change_type: str       # added | removed | modified
    severity: str          # low | medium | high


def classify_diff(
    project_id: int,
    added: dict,
    removed: dict,
    modified: dict,
):
    findings: list[DriftFinding] = []

    # Added resources
    for resource in added.keys():
        findings.append(
            DriftFinding(
                resource=resource,
                change_type="added",
                severity="high",
            )
        )

    # Removed resources
    for resource in removed.keys():
        findings.append(
            DriftFinding(
                resource=resource,
                change_type="removed",
                severity="high",
            )
        )

    # Modified resources
    for resource in modified.keys():
        findings.append(
            DriftFinding(
                resource=resource,
                change_type="modified",
                severity="medium",
            )
        )

    return findings
