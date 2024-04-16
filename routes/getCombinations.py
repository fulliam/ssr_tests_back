from fastapi import APIRouter
from typing import List
from itertools import product

from models.quize import Question

router = APIRouter(
    tags=["GET combinations"]
)


@router.post("/combinations/")
async def combinations(questions: List[Question]):
    options = [range(len(q.answers)) for q in questions]
    combos = list(product(*options))

    results = []
    for combo in combos:
        message = []
        for i, index in enumerate(combo):
            # theme = questions[i].question.split()[2]
            choice = questions[i].answers[index].description.split()[1]
            message.append(f"Тип {choice}<br/>")
        results.append({'combination': combo, 'result': ''.join(message)})

    return {"combinations": results}