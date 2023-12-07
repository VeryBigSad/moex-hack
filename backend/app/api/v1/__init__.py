from fastapi import APIRouter

from .tickers import router as router_tickers
from .strategy import router as router_strategy
from .news import router as router_news

router = APIRouter()
router.include_router(router_tickers, prefix="/tickers", tags=["tickers"])
router.include_router(router_strategy, prefix="/strategy", tags=["strategy"])
router.include_router(router_news, prefix="/news", tags=["news"])

