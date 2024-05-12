from pydantic import BaseModel
from typing import List

class Answer(BaseModel):
    text: str
    description: str
    value: bool
    types: List[str]

class Question(BaseModel):
    sex: str
    age: int
    question: str
    answers: List[Answer]