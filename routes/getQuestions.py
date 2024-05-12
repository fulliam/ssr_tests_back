from fastapi import APIRouter
from typing import List
from models.quize import Answer, Question #TODO:  need add types

router = APIRouter(
    tags=["GET combinations"]
)

questions = [
    {
        'src': './images/masik.jpg',
        'alt': 'Вопрос 1',
        'question': 'Как вы проводите свободное время?',
        'answers': [
            { 'text': 'Смотрю телевизор или играю в компьютерные игры ', 'description': '', 'value': False, 'types': ['скуф'] },
            { 'text': 'Занимаюсь спортом или активными видами отдыха', 'description': '', 'value': False, 'types': ['тюбик'] },
            { 'text': 'Читаю книги, занимаюсь творчеством', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Путешествую, ищу новые приключения', 'description': '', 'value': False, 'types': ['тюбик'] }
        ]
    },
    {
        'src': './images/skuf.jpg',
        'alt': 'Вопрос 2',
        'question': 'Как вы относитесь к рискам?',
        'answers': [
            { 'text': 'Избегаю рискованных ситуаций', 'description': '', 'value': False, 'types': ['чечик', 'скуф'] },
            { 'text': 'Готов рисковать ради возможности получить больше', 'description': '', 'value': False, 'types': ['штрих'] },
            { 'text': 'Оцениваю риски и действую осознанно', 'description': '', 'value': False, 'types': ['сигма'] },
            { 'text': 'Погружаюсь в приключения без оглядки ', 'description': '', 'value': False, 'types': ['альтушка'] }
        ]
    },
    {
        'src': './images/chechick.jpg',
        'alt': 'Вопрос 3',
        'question': 'Какое важнее для вас в отношениях?',
        'answers': [
            { 'text': 'Уход и забота о партнере', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Свобода и независимость', 'description': '', 'value': False, 'types': ['штрих'] },
            { 'text': 'Спокойствие и стабильность', 'description': '', 'value': False, 'types': ['душнила'] },
            { 'text': 'Эмоциональная и интеллектуальная близость', 'description': '', 'value': False, 'types': ['винишкотян'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 4',
        'question': 'Что вас больше всего вдохновляет?',
        'answers': [
            { 'text': 'Природа и путешествия', 'description': '', 'value': False, 'types': ['тюбик'] },
            { 'text': 'Социальная активность и общение', 'description': '', 'value': False, 'types': ['нормис'] },
            { 'text': 'Творческие процессы и искусство', 'description': '', 'value': False, 'types': ['альтушка', 'скуф'] },
            { 'text': 'Саморазвитие и достижение целей', 'description': '', 'value': False, 'types': ['сигма'] },
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 5',
        'question': 'Как вы оцениваете свои коммуникативные навыки?',
        'answers': [
            { 'text': 'С трудом нахожу общий язык с людьми', 'description': '', 'value': False, 'types': ['чечик'] },
            { 'text': 'Легко завожу новые знакомства и поддерживаю отношения', 'description': '', 'value': False, 'types': ['тарелочница'] },
            { 'text': 'Предпочитаю общаться в небольших кругах', 'description': '', 'value': False, 'types': ['милф', 'скуф'] },
            { 'text': 'Обладаю харизмой и лидерскими качествами', 'description': '', 'value': False, 'types': ['сигма'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 6',
        'question': 'Как вы относитесь к моде и стилю?',
        'answers': [
            { 'text': 'Следую модным тенденциям и экспериментирую со стилем', 'description': '', 'value': False, 'types': ['винишкотян'] },
            { 'text': 'Предпочитаю классический и удобный стиль', 'description': '', 'value': False, 'types': ['нормис'] },
            { 'text': 'Не обращаю внимания на моду и стиль', 'description': '', 'value': False, 'types': ['чечик'] },
            { 'text': 'Выделяюсь на фоне других своими нестандартными образами', 'description': '', 'value': False, 'types': ['альтушка'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 7',
        'question': 'Что для вас важнее всего в работе?',
        'answers': [
            { 'text': 'Стабильность и безопасность', 'description': '', 'value': False, 'types': ['душнила'] },
            { 'text': 'Карьерный рост и достижение успеха', 'description': '', 'value': False, 'types': ['штрих'] },
            { 'text': 'Творческая свобода и самовыражение', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Интересные проекты и увлекательные задачи', 'description': '', 'value': False, 'types': ['сигма'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 8',
        'question': 'Как вы проявляете заботу о своих близких?',
        'answers': [
            { 'text': 'Помогаю им в решении повседневных проблем', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Выражаю свою заботу словами и поддержкой', 'description': '', 'value': False, 'types': ['тарелочница'] },
            { 'text': 'Предлагаю практическую помощь в трудных ситуациях', 'description': '', 'value': False, 'types': ['чечик'] },
            { 'text': 'Провожу время вместе и уделяю внимание их интересам ', 'description': '', 'value': False, 'types': ['альтушка'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 9',
        'question': 'Что для вас является главной ценностью в жизни?',
        'answers': [
            { 'text': 'Семья и близкие отношения', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Саморазвитие и личностный рост', 'description': '', 'value': False, 'types': ['сигма'] },
            { 'text': 'Свобода и независимость', 'description': '', 'value': False, 'types': ['тюбик'] },
            { 'text': 'Новые впечатления и приключения', 'description': '', 'value': False, 'types': ['альтушка'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 10',
        'question': 'Как вы относитесь к изменениям и неожиданностям?',
        'answers': [
            { 'text': 'Стремитесь к стабильности и планированию', 'description': '', 'value': False, 'types': ['нормис'] },
            { 'text': 'Радуетесь новым возможностям и вызовам', 'description': '', 'value': False, 'types': ['тюбик'] },
            { 'text': 'Избегаете неожиданностей и предпочитаете привычный порядок', 'description': '', 'value': False, 'types': ['душнила'] },
            { 'text': 'Принимаете изменения как часть жизни и адаптируетесь к ним ', 'description': '', 'value': False, 'types': ['сигма'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 11',
        'question': 'Как вы предпочитаете проводить отпуск?',
        'answers': [
            { 'text': 'Активно путешествовать и открывать новые культуры', 'description': '', 'value': False, 'types': ['тюбик'] },
            { 'text': 'Отдыхать на пляже или в горах, наслаждаясь природой', 'description': '', 'value': False, 'types': ['нормис'] },
            { 'text': 'Проводить время дома или с друзьями, занимаясь хобби', 'description': '', 'value': False, 'types': ['милф', 'скуф'] },
            { 'text': 'Участвовать в культурных мероприятиях и фестивалях', 'description': '', 'value': False, 'types': ['альтушка'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 12',
        'question': 'Что для вас важнее всего в дружбе?',
        'answers': [
            { 'text': 'Взаимопонимание и поддержка', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Интересные беседы и общие увлечения', 'description': '', 'value': False, 'types': ['сигма'] },
            { 'text': 'Веселье и развлечения', 'description': '', 'value': False, 'types': ['винишкотян'] },
            { 'text': 'Долгие и надежные отношения', 'description': '', 'value': False, 'types': ['нормис'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 13',
        'question': 'Какое качество у вас самое ценное?',
        'answers': [
            { 'text': 'Доброжелательность и эмпатия', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Умение быстро принимать решения', 'description': '', 'value': False, 'types': ['сигма'] },
            { 'text': 'Творческий подход к решению задач', 'description': '', 'value': False, 'types': ['винишкотян'] },
            { 'text': 'Ответственность и надежность', 'description': '', 'value': False, 'types': ['нормис'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 14',
        'question': 'Как вы относитесь к традициям и обычаям?',
        'answers': [
            { 'text': 'Ценю и придерживаюсь традиций', 'description': '', 'value': False, 'types': ['нормис'] },
            { 'text': 'Считаю, что традиции не всегда необходимы', 'description': '', 'value': False, 'types': ['тюбик'] },
            { 'text': 'Игнорирую обычаи и предпочитаю делать по-своему', 'description': '', 'value': False, 'types': ['альтушка', 'скуф'] },
            { 'text': 'Ищу новые подходы к знакомым вещам', 'description': '', 'value': False, 'types': ['сигма'] }
        ]
    },
    {
        'src': './images/tubik.jpg',
        'alt': 'Вопрос 15',
        'question': 'Как вы реагируете на критику?',
        'answers': [
            { 'text': 'Принимаю критику и стремлюсь улучшиться ', 'description': '', 'value': False, 'types': ['сигма'] },
            { 'text': 'Оправдываюсь или игнорирую критику', 'description': '', 'value': False, 'types': ['душнила'] },
            { 'text': 'Стараюсь найти компромиссное решение', 'description': '', 'value': False, 'types': ['масик', 'папик', 'милф'] },
            { 'text': 'Воспринимаю критику как личное обиду', 'description': '', 'value': False, 'types': ['альтушка', 'скуф'] }
        ]
    },
]

@router.get("/questions/")
async def get_questions():
    return questions
