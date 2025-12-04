from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Infrastructure Drift Detective"
    DATABASE_URL: str
    REDIS_URL: str | None = None
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
