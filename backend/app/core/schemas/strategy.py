import datetime
from typing import List

from pydantic import BaseModel


class BackTestCandle(BaseModel):
    begin: datetime.datetime
    end: datetime.datetime
    close: float


class StrategyTestedResponse(BaseModel):
    strategy_id: int
    candles: List[BackTestCandle]
    data: dict


class StrategyFileModel(BaseModel):
    id: int
    name: str
    content: str


class BacktestRequest(BaseModel):
    files: list[StrategyFileModel]
    date_start: datetime.date
    date_end: datetime.date
