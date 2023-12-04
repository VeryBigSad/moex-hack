import logging

from fastapi import APIRouter, status, UploadFile

from core.exceptions import BadRequest

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/upload",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def upload_strategy(file: UploadFile):
    """Upload strategy file .py"""
    if file.filename.split('.')[-1] != ".py":
        raise BadRequest()
