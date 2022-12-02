from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = randint(2, 100)
    if is_prime(question):
        return question, 'yes'
    else:
        return question, 'no'


def is_prime(number):
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False
    return True
