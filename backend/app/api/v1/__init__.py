from fastapi import APIRouter

from .tickers import router as router_tickers
from .strategy import router as router_strategy
from .news import router as router_news

router = APIRouter()
router.include_router(router_tickers, prefix="/tickers")
router.include_router(router_strategy, prefix="/strategy")
router.include_router(router_news, prefix="/news")

