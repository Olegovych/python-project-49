from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
PRIME_LIST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def get_question_and_answer():
    question = randint(0, 100)
    if question in PRIME_LIST:
        return question, 'yes'
    else:
        return question, 'no'
