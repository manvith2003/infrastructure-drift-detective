def parse_resource_changes(resource_changes: list, prior_state: dict | None):
    drifts = []

    prior_resources = set()

    if prior_state and "values" in prior_state:
        for res in prior_state["values"].get("root_module", {}).get("resources", []):
            prior_resources.add(f"{res['type']}.{res['name']}")

    for change in resource_changes:
        actions = change["change"]["actions"]
        addr = change["address"]

        # 🚨 REAL DRIFT: resource existed before but now recreated
        if actions == ["create"] and addr in prior_resources:
            drifts.append({
                "resource": addr,
                "change_type": "deleted_manually",
                "severity": "high",
            })

        # New resource
        elif actions == ["create"]:
            drifts.append({
                "resource": addr,
                "change_type": "created",
                "severity": "low",
            })

        elif actions == ["update"]:
            drifts.append({
                "resource": addr,
                "change_type": "modified",
                "severity": "medium",
            })

        elif actions == ["delete"]:
            drifts.append({
                "resource": addr,
                "change_type": "deleted",
                "severity": "high",
            })

    return drifts
