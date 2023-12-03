from typing import Any

from pydantic import BaseModel

from src.constants import Environment


class Config(BaseModel):
    DATABASE_URL: str

    SITE_DOMAIN: str

    ENVIRONMENT: Environment = Environment.PRODUCTION

    APP_VERSION: str = "0.1.0"


settings = Config()

app_configs: dict[str, Any] = {"title": "Moex Hackathon API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
