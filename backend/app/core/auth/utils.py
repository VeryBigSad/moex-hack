from typing import Any

from core.auth.config import auth_config
from config import settings


def get_refresh_token_settings(
    refresh_token: str,
    expired: bool = False,
) -> dict[str, Any]:
    base_cookie = {
        "key": auth_config.REFRESH_TOKEN_KEY,
        "httponly": True,
        "samesite": "none",
        "secure": auth_config.SECURE_COOKIES,
        "domain": settings.SITE_DOMAIN,
    }
    if expired:
        return base_cookie

    return {
        **base_cookie,
        "value": refresh_token,
        "max_age": auth_config.REFRESH_TOKEN_EXP,
    }
