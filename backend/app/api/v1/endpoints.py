import logging

from fastapi import APIRouter, status

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/lesson")


@router.get(
    "/v1-route",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
async def get_questions():
    """Get a list of all questions"""
    return {"message": "Hello World"}
