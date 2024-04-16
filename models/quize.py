from pydantic import BaseModel
from typing import List

class Answer(BaseModel):
    text: str
    description: str
    value: bool

class Question(BaseModel):
    question: str
    answers: List[Answer]