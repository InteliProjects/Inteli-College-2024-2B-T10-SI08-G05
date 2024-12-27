from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field
from typing import Optional
import json

class Settings(BaseSettings):
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_REGION: str
    CLICKHOUSE_HOST: str
    CLICKHOUSE_PORT: int
    CLICKHOUSE_USER: str
    CLICKHOUSE_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    API_KEY: str
    AWS_SESSION_TOKEN: Optional[str] = None
    STREAMLIT_TOKEN: Optional[str] = None
    BASE_URL:  Optional[str] = None
    AUTH_CREDENTIALS_JSON: str
    AUTH_COOKIE_EXPIRY_DAYS: int = 30
    AUTH_COOKIE_KEY: str
    AUTH_COOKIE_NAME: str
    AUTH_PREAUTHORIZED_EMAILS: str = ""

    class Config:
        env_file = ".env"
    
settings = Settings()

