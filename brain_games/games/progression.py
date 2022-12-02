from random import randint


TASK = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(5, 10)
    end = start + length * step
    progression = list(range(start, end, step))
    question_index = randint(0, length - 1)
    correct_answer = str(progression[question_index])
    progression[question_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
