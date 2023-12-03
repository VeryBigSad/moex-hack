import logging
from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from core.models.models import QuestionAnswer, Test
from core.service.webhooks import trigger_bot_answers_webhook
from core.service.service import get_questions_by_test_id
from core.schemas.user import AnswerRequestModel, QuestionResponseModel
from core.middlewares.webapp_header import init_data_headers_middleware


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/lesson")


@router.get(
    "/route",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
async def get_questions():
    """Get a list of all questions"""
    return {"message": "Hello World"}


