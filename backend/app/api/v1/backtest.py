import datetime
import logging
import random
from typing import List

import pandas as pd
from backtesting import Backtest
from fastapi import APIRouter, status, HTTPException
from tortoise.exceptions import DoesNotExist

from core.exceptions import NotFound
from core.models import Strategy as StrategyModel, Backtest as BacktestModel
from core.schemas.strategy import StrategyTestedResponse, BacktestRequest, BackTestCandle

logger = logging.getLogger(__name__)

router = APIRouter()

df = pd.read_csv('/csvdata/YNDX_RUB-1h.csv')
df = df.drop(columns=['Unnamed: 0']).set_index(
    pd.DatetimeIndex(pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S'))
).rename(
    columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'}
).drop(columns=['date'])
results = {}


@router.post(
    "/backtest",
    status_code=status.HTTP_200_OK,
    response_model=int
)
async def start_backtesting(data: BacktestRequest):
    """Start backtesting"""
    backtest = await BacktestModel.create(date_start=data.date_start, date_end=data.date_end)
    # get data

    for i in data.files:
        s = await StrategyModel.create(backtest=backtest, pk=i.id, name=i.name, source=i.content)
        # try to run the strategy
        # find name from source - it should be defined like class <name>(Strategy)
        # get class by name from local variables
        class_name = i.content.split("class ")[1].split("(")[0]
        try:
            exec(i.content)
        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=400, detail="Invalid syntax")
        strategy_class = locals()[class_name]
        # copy locals to globals
        globals().update(locals())
        # run backtest
        bt = Backtest(df, strategy_class, cash=100_000, commission=.0005)
        try:
            stats = bt.run()
        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=400, detail="Invalid import")
        print(stats)
        results[backtest.pk] = stats.to_dict()

    return backtest.pk


@router.get(
    "/{backtest_id}/progress",
    status_code=status.HTTP_200_OK,
    response_model=List[StrategyTestedResponse]
)
async def get_progress(backtest_id: int):
    """Progress bar by backtest id"""
    try:
        backtest = await BacktestModel.get(id=backtest_id)
    except DoesNotExist:
        raise NotFound()

    # get all strategies by backtest id
    strategies = await StrategyModel.filter(backtest=backtest)
    res = []
    dict_repr = results[backtest_id]
    dict_repr = {k: v for k, v in dict_repr.items() if k[0] != '_'}
    for i in strategies:
        # 1 hour intervals from 9am to 8pm for 90 days
        candles = []
        for j in range(90 * 11):
            candles.append(
                BackTestCandle(
                    begin=datetime.datetime(2021, 1, 1, 9) + datetime.timedelta(hours=j),
                    end=datetime.datetime(2021, 1, 1, 10) + datetime.timedelta(hours=j),
                    close=(candles[-1].close if len(candles) != 0 else 400) + random.randint(-2, 2)
                )
            )
        res.append(StrategyTestedResponse(strategy_id=i.pk, candles=candles, data=dict_repr))
    return res
