import logging

from fastapi import APIRouter, status, UploadFile

from core.exceptions import BadRequest
from core.models import Strategy

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/upload",
    status_code=status.HTTP_201_CREATED,
    response_model=int
)
async def upload_strategy(file: UploadFile):
    """Upload strategy file .py, return strategy id"""
    if file.filename.split('.')[-1] != ".py":
        raise BadRequest()

    file_text = await file.read()
    strategy = await Strategy.create(strategy_file_source=file_text)
    return strategy.id

