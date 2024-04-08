from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from itertools import product

router = APIRouter(
    tags=["GET combinations"]
)

class Answer(BaseModel):
    text: str
    description: str
    value: bool

class Question(BaseModel):
    question: str
    answers: List[Answer]

@router.post("/combinations/")
async def combinations(questions: List[Question]):
    print(questions)
    options = [range(len(q.answers)) for q in questions]
    combos = list(product(*options))

    # Generate unique messages for each combination_-
    results = []
    for combo in combos:
        message = []
        for i, index in enumerate(combo):
            theme = questions[i].question.split()[2]  # Extract the theme from the question
            choice = questions[i].answers[index].text  # Get the chosen answer
            message.append(f"You prefer {choice} for {theme}")
        results.append({'combination': combo, 'result': ', '.join(message)})

    return {"combinations": results}