"""Application configuration using pydantic BaseSettings.

Put non-sensitive defaults here and override via `.env` in development or environment variables in production.
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "almaviva-bot"
    database_url: str = "sqlite:///./data/almaviva_bot.db"
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True

    class Config:
        env_file = '.env'


settings = Settings()
