import datetime
import logging
import random
from typing import List

import pandas as pd
from fastapi import APIRouter
from moexalgo import Market, Ticker
from starlette import status

from config.constants import get_sphere, get_name
from core.exceptions import BadRequest
from core.schemas.tickers import TickerResponse, TickerCandleResponse, RelevantTickerResponse, Period

logger = logging.getLogger(__name__)

router = APIRouter()

stocks = Market("stocks")
corr_stats = None

def get_ticker_corr(
        ticker: str,
        days: int = 10,
        corr_ratio: float = 0.3,
        start_date: datetime.datetime = datetime.date(2023, 10, 1),
):
    global corr_stats
    if corr_stats is None:
        dates = [start_date + datetime.timedelta(days=x) for x in range(days)]
        stocks_info = pd.concat([pd.DataFrame(stocks.tradestats(date=i)) for i in dates])
        stocks_info['tradedate'] = stocks_info['ts'].dt.date
        stocks_info['tradetime'] = stocks_info['ts'].dt.time
        # for all stocks info,
        stats = stocks_info.pivot_table(index='tradedate', columns='secid', values='pr_vwap_s', aggfunc='mean')
        corr_stats = stats.corr()

    spl = corr_stats.loc[:, [ticker]]
    l_list = list(spl[(spl[ticker] < corr_ratio) & (spl[ticker] > -corr_ratio)].index)
    r_list = list(spl[(spl[ticker] < corr_ratio) & (spl[ticker] > -corr_ratio)][ticker])

    result_list = [(l_list[i], r_list[i]) for i in range(min(len(l_list), len(r_list)))]
    return result_list


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
        {
            "ticker": ticker["SECID"],
            "price": ticker["PREVLEGALCLOSEPRICE"],
            "name": get_name(ticker["SECID"]) if get_name(ticker["SECID"]) else ticker["SECNAME"],
            "sphere": get_sphere(ticker["SECID"]),
            "is_positive_forecast": bool(random.randint(0, 1))
        }
        for ticker in tickers
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


@router.get(
    "/{ticker}/relevant/",
    response_model=List[RelevantTickerResponse],
    status_code=status.HTTP_200_OK
)
async def get_relevant_tickers(ticker: str):
    """Get a list of relevant tickers for the specified ticker"""
    stocks = Market('stocks')
    tickers = stocks.tickers()
    tickers = {
        ticker["SECID"]: ticker
        for ticker in tickers
    }
    small_corr_tickers = get_ticker_corr(ticker.upper())
    data = [
        {
            "ticker": ticker_name,
            "price": tickers[ticker_name]["PREVLEGALCLOSEPRICE"],
            "name": get_name(ticker_name) if get_name(ticker_name) else tickers[ticker_name]["SECNAME"],
            "sphere": get_sphere(ticker_name),
            "is_positive_forecast": bool(random.randint(0, 1)),
            "correlation_score": corr,
        }
        for ticker_name, corr in small_corr_tickers
        if ticker_name in tickers
    ]
    return data
