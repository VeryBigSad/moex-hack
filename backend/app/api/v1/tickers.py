import datetime
import logging
from typing import List

from fastapi import APIRouter, status
from moexalgo import Market, Ticker

from core.exceptions import BadRequest
from core.schemas.tickers import Period, TickerCandleResponse, TickerResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/",
    response_model=List[TickerResponse],
    status_code=status.HTTP_200_OK,
)
async def get_tickers():
    """Get a list of all MOEX tickers"""
    # TODO: cache this list via nginx or redis
    stocks = Market('stocks')
    tickers = stocks.tickers()

    data = [
        {"ticker": ticker['SECID'], "price": ticker['PREVLEGALCLOSEPRICE'], "name": ticker["SECNAME"]} for
        ticker in tickers
    ]
    return data


@router.get(
    "/{ticker}/",
    response_model=List[TickerCandleResponse],
    status_code=status.HTTP_200_OK,
)
async def get_price_for_ticker(ticker: str, date_start: datetime.date, date_end: datetime.date, period: Period):
    """Get price for ticker over time with specified frequency"""
    try:
        ticker = Ticker(ticker.upper())
    except LookupError:
        raise BadRequest(detail={"error": f"Ticker {ticker.upper()} not found"})

    candles = list(ticker.candles(date=date_start, till_date=date_end, period=period))
    return candles
