from random import randint
from math import gcd

TASK = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = f'{first_num} {second_num}'
    return question, str(gcd(first_num, second_num))
