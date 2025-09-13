from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./pay.db"
    API_SECRET_KEY: str
    REDIS_URL: str = "redis://localhost:6379/0"

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "payments"

    class Config:
        env_file = ".env"  # tell pydantic where to load values
        env_file_encoding = "utf-8"
@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
