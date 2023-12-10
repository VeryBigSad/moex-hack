from typing import Optional

from pydantic import BaseModel


class StrategyProgressResponse(BaseModel):
    strategy_id: int
    status: str
    progress: Optional[float]
    profit: Optional[float]


class StrategyFileModel(BaseModel):
    name: str
    content: str


class BacktestRequest(BaseModel):
    files: list[StrategyFileModel]
    date_start: str
    date_end: str
