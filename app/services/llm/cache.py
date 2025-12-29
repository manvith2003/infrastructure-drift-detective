import redis
import os

REDIS_TTL_SECONDS = 60 * 60 * 24  # 24 hours

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)


def get_cached_explanation(drift_id: int):
    return redis_client.get(f"drift_explanation:{drift_id}")


def set_cached_explanation(drift_id: int, explanation: str):
    redis_client.setex(
        f"drift_explanation:{drift_id}",
        REDIS_TTL_SECONDS,
        explanation
    )
