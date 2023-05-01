from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = randint(-100, 100)
    return (question, 'yes') if is_prime(question) else (question, 'no')


def is_prime(number):
    if number <= 1:
        return False
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False
    return True
