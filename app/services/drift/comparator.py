def compare_states(desired: dict, actual: dict):
    """
    Compare Terraform desired state vs actual cloud state
    Returns: (added, removed, modified)
    """

    added = {}
    removed = {}
    modified = {}

    # Removed or modified
    for key, desired_val in desired.items():
        if key not in actual:
            removed[key] = desired_val
        elif desired_val != actual[key]:
            modified[key] = {
                "desired": desired_val,
                "actual": actual[key],
            }

    # Added
    for key, actual_val in actual.items():
        if key not in desired:
            added[key] = actual_val

    return added, removed, modified
