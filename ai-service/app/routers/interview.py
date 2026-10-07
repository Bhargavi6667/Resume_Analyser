from fastapi import APIRouter, HTTPException
from app.schemas.interview import (
    InterviewStartRequest,
    InterviewAnswerRequest,
    InterviewQuestion,
    InterviewEvaluation
)
from app.services.interview_agent import interview_agent

router = APIRouter(prefix="/interview", tags=["AI Interview Agent"])

@router.post("/start", response_model=InterviewQuestion)
async def start_interview_session(request: InterviewStartRequest):
    """Initialize an adaptive technical mock interview tailored to candidate's background."""
    if not request.resume_text.strip() or not request.job_description.strip():
        raise HTTPException(status_code=400, detail="Resume context and Job Description are required")

    return interview_agent.start_interview(
        resume_text=request.resume_text,
        job_description=request.job_description,
        topics=request.topics
    )

@router.post("/respond", response_model=InterviewEvaluation)
async def submit_answer(request: InterviewAnswerRequest):
    """Submit candidate's answer for evaluation and retrieve next adaptive question."""
    if not request.question.strip() or not request.answer.strip():
        raise HTTPException(status_code=400, detail="Question and answer text cannot be empty")

    return interview_agent.evaluate_and_next(
        question=request.question,
        answer=request.answer,
        resume_context=request.resume_context or "",
        job_context=request.job_context or "",
        history=request.history or []
    )
