from random import randint, choice
import operator


TASK = 'What is the result of the expression?'


def get_question_and_answer():
    first_num = randint(0, 100)
    second_num = randint(0, 10)
    operations = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    )
    operation_name, operation_method = choice(operations)
    question = f'{first_num} {operation_name} {second_num}'
    correct_answer = str(operation_method(first_num, second_num))
    return question, correct_answer
