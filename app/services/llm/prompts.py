DRIFT_EXPLANATION_PROMPT = """
You are a cloud infrastructure expert.

A drift was detected between Terraform and actual cloud state.

Drift summary:
{summary}

Terraform state:
{terraform_state}

Actual cloud state:
{cloud_state}

Explain:
1. What changed
2. Why this drift is risky
3. What probably caused it
4. Recommended fix

Keep it concise and clear.
"""
