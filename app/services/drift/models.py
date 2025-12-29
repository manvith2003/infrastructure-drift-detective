from dataclasses import dataclass
from typing import Any


@dataclass
class DriftFinding:
    project_id: int
    resource: str
    change_type: str  # "added", "removed", "modified"
    field: str | None
    old_value: Any | None
    new_value: Any | None
    severity: str  # "low", "medium", "high"
