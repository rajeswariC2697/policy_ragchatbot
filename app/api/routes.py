from fastapi import APIRouter, HTTPException, Request
from fastapi import status
from app.models.schemas import QuestionRequest, AnswerResponse
from app.rag.pipeline import rag_pipeline

from app.utils.responses import CustomResponse
from app.constants.messages import ChatConstants, Errormessages
from app.constants.http_status import HTTPStatus

router = APIRouter()

@router.post("/ask")
async def ask_question(request: Request, payload: QuestionRequest):
    try:
        if not payload.question.strip():
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=Errormessages.BAD_REQUEST
            )
        result = rag_pipeline.answer(payload.question)
        return CustomResponse.success(
            data=result.model_dump(),
            message=ChatConstants.CHAT_SUCCESS,
            status_code=HTTPStatus.OK,
        )
    except HTTPException as http_exc:
        return CustomResponse.failure(
            message=http_exc.detail,
            status_code=http_exc.status_code,
        )
    except Exception as e:
        return CustomResponse.error(
            error=str(e),
            message=Errormessages.INTERNAL_SERVER_ERROR,
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )
    
@router.get("/health")
async def health_check():
    return CustomResponse.success(
        data={"status": "ok"},
        message="Service is running",
        status_code=HTTPStatus.OK,
    )