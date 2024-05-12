from fastapi import APIRouter
from typing import List
from collections import Counter

from models.quize import Question

router = APIRouter(
    tags=["GET results"]
)


@router.post("/results/") 
async def process_answers(questions: List[Question]): 
    results = []

    for question in questions:
        for answer in question.answers:
            if answer.value:
                if hasattr(answer, 'types'):
                    results.extend(answer.types)

    word_counts = Counter(results)
    
    user_type = word_counts.most_common(1)[0][0]

    return user_type
