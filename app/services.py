import datetime

questions = [
    {
        'id': 1,
        'text': 'Question 1',
        'answer': None,
        'started': None
    },
    {
        'id': 2,
        'text': 'Question 2',
        'answer': None,
        'started': None
    },
    {
        'id': 3,
        'text': 'Question 3',
        'answer': None,
        'started': None
    }
]

now = datetime.datetime.now()
quizzes = [
    {
        'token': '1',
        'created': now,
        'start': now + datetime.timedelta(minutes=0),
        'end': now + datetime.timedelta(minutes=5),
        'timeout': 60,
        'questions': questions[:]
    },
    {
        'token': '2',
        'created': now,
        'start': now + datetime.timedelta(minutes=2),
        'end': now + datetime.timedelta(minutes=7),
        'timeout': 60,
        'questions': questions[:]
    },
    {
        'token': '3',
        'created': now,
        'start': now + datetime.timedelta(minutes=5),
        'end': now + datetime.timedelta(minutes=10),
        'timeout': 60,
        'questions': questions[:]
    }
]


def list():
    return quizzes


def detail(token):
    for q in quizzes:
        if q['token'] == token:
            q['current_question'] = find_current_question(token)
            return q


def submit_answer(token, answer):
    for q in quizzes:
        if q['token'] == token:
            current_question = find_current_question(token)
            q['current_question'] = current_question
            q['current_question']['answer'] = answer
            break


def start_next_question(token):
    for q in quizzes:
        if q['token'] == token:
            for question in q['questions']:
                if question['started'] is None:
                    question['started'] = datetime.datetime.now()
                    break


def find_current_question(token):
    for q in quizzes:
        if q['token'] == token:
            previous_question = None
            for question in q['questions']:
                if question['started'] is None:
                    return previous_question
                else:
                    if (datetime.datetime.now() - question['started']).total_seconds() > q['timeout'] or question['answer'] is not None:
                        question['seconds_to_expire'] = 0
                        previous_question = question
                    else:
                        question['seconds_to_expire'] = int(q['timeout'] - (datetime.datetime.now() - question['started']).total_seconds())
                        return question
