import json
from pathlib import Path


def load_cloud_state(project_id: int):
    path = Path(f"mock_data/project_{project_id}_cloud.json")
    if not path.exists():
        return {}
    return json.loads(path.read_text())
