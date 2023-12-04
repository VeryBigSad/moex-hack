from fastapi import APIRouter

from .tickers import router as router_tickers
from .strategy import router as router_strategy

router = APIRouter()
router.include_router(router_tickers, prefix="/tickers")
router.include_router(router_strategy, prefix="/strategy")

