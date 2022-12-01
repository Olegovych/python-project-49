from random import randint, choice


TASK = 'What is the result of the expression?'


def calc():
    first_num = randint(0, 100)
    operator = choice('+-*')
    second_num = randint(0, 10)
    question = f'{first_num} {operator} {second_num}'
    correct_answer = str(eval(question))
    return question, correct_answer
