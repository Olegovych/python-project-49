from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(0, 100)
    return (question, 'yes') if question % 2 == 0 else (question, 'no')
