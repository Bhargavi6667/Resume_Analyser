from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class InterviewStartRequest(BaseModel):
    resume_text: str
    job_description: str
    topics: Optional[List[str]] = Field(default_factory=list)

class InterviewAnswerRequest(BaseModel):
    session_id: Optional[str] = "session-default"
    question: str
    answer: str
    resume_context: Optional[str] = ""
    job_context: Optional[str] = ""
    history: Optional[List[Dict[str, Any]]] = Field(default_factory=list)

class InterviewQuestion(BaseModel):
    question_id: str
    topic: str
    question: str
    context: Optional[str] = None
    difficulty: str = "Medium"  # Easy, Medium, Hard

class InterviewEvaluation(BaseModel):
    evaluation: str
    score: float
    strengths: List[str] = Field(default_factory=list)
    areas_for_improvement: List[str] = Field(default_factory=list)
    follow_up_question: Optional[str] = None
    next_question: InterviewQuestion
