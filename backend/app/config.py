from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    ENVIRONMENT: Literal["local", "prod"]
    postgres_url: PostgresDsn


settings = Settings()
