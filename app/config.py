from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Infrastructure Drift Detective"

    DATABASE_URL: str
    REDIS_URL: str | None = None

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    # 🔑 LLM (Groq)
    GROQ_API_KEY: str | None = None

    # ✅ Pydantic v2 config
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # <-- THIS FIXES YOUR CRASH
    )

settings = Settings()
