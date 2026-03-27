from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    app_debug: bool = True
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    database_url: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/email_signatures"
    )

    # Brand identity — override via env vars for each environment
    brand_primary_color: str = "#000000"
    brand_secondary_color: str = "#D14954"
    brand_company_name: str = "BT Blue Ativos Judiciais"
    brand_logo_url: str | None = None
    brand_website_url: str | None = None

    # Observability — set LOG_FILE to write structured logs to a rotating file
    log_file: str | None = None

    @field_validator("database_url", mode="before")
    @classmethod
    def normalize_postgresql_driver(cls, value: str) -> str:
        if isinstance(value, str):
            if value.startswith("postgresql://"):
                return value.replace("postgresql://", "postgresql+psycopg://", 1)
            if value.startswith("postgres://"):
                return value.replace("postgres://", "postgresql+psycopg://", 1)
        return value

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
