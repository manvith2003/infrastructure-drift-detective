import json
from app.services.llm.prompts import DRIFT_EXPLANATION_PROMPT
from app.services.llm.client import call_llm
from app.services.llm.cache import (
    get_cached_explanation,
    set_cached_explanation,
)


def generate_drift_explanation(
    drift_id: int,
    summary: str,
    terraform_state: dict,
    cloud_state: dict,
) -> str:
    """
    Generate (or fetch cached) LLM explanation for a drift.
    """

    # 1️⃣ Check Redis cache first
    cached = get_cached_explanation(drift_id)
    if cached:
        return cached

    # 2️⃣ Build prompt
    prompt = DRIFT_EXPLANATION_PROMPT.format(
        summary=summary,
        terraform_state=json.dumps(terraform_state, indent=2),
        cloud_state=json.dumps(cloud_state, indent=2),
    )

    # 3️⃣ Call LLM (mock / Groq / OpenAI)
    explanation = call_llm(prompt)

    # 4️⃣ Store in Redis cache
    set_cached_explanation(drift_id, explanation)

    return explanation
