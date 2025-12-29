def calculate_severity(change_type: str, field: str | None) -> str:
    """
    Basic rule-based severity.
    Later we will use ML/LLM.
    """
    if change_type == "removed":
        return "high"
    if change_type == "added":
        return "medium"
    if change_type == "modified":
        # critical fields example
        if field in ("acl", "public_access", "security_group"):
            return "high"
        return "medium"
    return "low"
