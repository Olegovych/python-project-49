from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(0, 100)
    if question % 2 == 0:
        return question, 'yes'
    else:
        return question, 'no'
