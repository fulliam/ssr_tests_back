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
        if question.sex == 'женщина' and question.age > 26:
            exclude_types = ['масик', 'папик', 'скуф']
        elif question.sex == 'женщина' and question.age < 27:
            exclude_types = ['скуф', 'папик', 'масик', 'милф']
        elif question.sex == 'мужчина' and question.age < 27:
            exclude_types = ['скуф', 'папик', 'милф']
        elif question.sex == 'мужчина' and question.age > 26:
            exclude_types = ['масик', 'винишкотян', 'альтушка', 'милф']
        else:
            exclude_types = []

        for answer in question.answers:
            if answer.value:
                if hasattr(answer, 'types'):
                    results.extend([type for type in answer.types if type not in exclude_types])

    word_counts = Counter(results)
    
    user_type = word_counts.most_common(1)[0][0]
    
    print(results)
    
    return user_type