from fastapi import APIRouter
from typing import List
from models.quize import Answer, Question #TODO:  need add types

router = APIRouter(
    tags=["GET combinations"]
)

questions = [
    {
        'src': './images/question1.jpg',
        'alt': 'Вопрос 1',
        'question': 'Как вы обычно проводите свой досуг?',
        'answers': [
            { 'text': 'Читаю книги или смотрю фильмы', 'description': 'Оценка интроверта', 'value': False, 'type': 'education' },
            { 'text': 'Провожу время с друзьями', 'description': 'Оценка экстраверта', 'value': False, 'type': 'teamwork' },
            { 'text': 'Рисую или пишу', 'description': 'Оценка эмоциональной личности', 'value': False, 'type': 'art' }
        ]
    },
    {
        'src': './images/question2.jpg',
        'alt': 'Вопрос 2',
        'question': 'Если бы вы могли выбрать одну суперспособность, что бы это было?',
        'answers': [
            { 'text': 'Понимать и говорить на всех языках', 'description': 'Оценка общительной личности', 'value': False, 'type': 'teamwork' },
            { 'text': 'Путешествовать во времени', 'description': 'Оценка приключенческого духа', 'value': False, 'type': 'teamwork' },
            { 'text': 'Читать мысли', 'description': 'Оценка эмпатии', 'value': False, 'type': 'teamwork' }
        ]
    },
    {
        'src': './images/question3.jpg',
        'alt': 'Вопрос 3',
        'question': 'Какой тип книг вы предпочитаете?',
        'answers': [
            { 'text': 'Фантастика или фэнтези', 'description': 'Оценка креативной личности', 'value': False, 'type': 'teamwork' },
            { 'text': 'Научная литература', 'description': 'Оценка аналитического мышления', 'value': False, 'type': 'teamwork' },
            { 'text': 'Биографии или исторические книги', 'description': 'Оценка реалистичной личности', 'value': False, 'type': 'teamwork' }
        ]
    },
    {
        'src': './images/question4.jpg',
        'alt': 'Вопрос 4',
        'question': 'Какой вид спорта вам нравится больше всего?',
        'answers': [
            { 'text': 'Командные игры (футбол, баскетбол)', 'description': 'Оценка командной работы', 'value': False, 'type': 'teamwork' },
            { 'text': 'Игры с мячом (пинг-понг, теннис)', 'description': 'Оценка скорости реакции', 'value': False, 'type': 'reaction' },
            { 'text': 'Индивидуальные занятия (бег, плавание)', 'description': 'Оценка самодисциплины', 'value': False, 'type': 'discipline' }
        ]
    },
    {
        'src': './images/question5.jpg',
        'alt': 'Вопрос 5',
        'question': 'Какой ваш любимый жанр музыки?',
        'answers': [
            { 'text': 'Рок', 'description': 'Оценка независимости', 'value': False, 'type': 'independence' },
            { 'text': 'Поп', 'description': 'Оценка современности', 'value': False, 'type': 'modernity' },
            { 'text': 'Классика', 'description': 'Оценка способности ценить искусство', 'value': False, 'type': 'art_appreciation' }
        ]
    }
]

@router.get("/questions/")
async def get_questions():
    return questions
