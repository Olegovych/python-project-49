import prompt
from random import randint, choice
from os import system


def welcome_user():
    system('clear')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congratulation(name):
    print(f'Congratulations, {name}!')


def even():
    question = randint(0, 100)
    if question % 2 == 0:
        return question, 'yes'
    else:
        return question, 'no'


def calc():
    first_num = randint(0, 10)
    operator = choice('+-*')
    second_num = randint(0, 10)
    question = f'{first_num} {operator} {second_num}'
    correct_answer = str(eval(question))
    return question, correct_answer


def check_answer(user_name, func_index):
    functions = (even, calc)
    for _ in range(3):
        question, correct_answer = functions[func_index]()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{correct_answer}'.", sep="")
            print(f"Let's try again, {user_name}!")
            break
    else:
        congratulation(user_name)


def check(question, correct_answer, user_name):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. ",
              f"Correct answer was '{correct_answer}'.", sep="")
        print(f"Let's try again, {user_name}!")
        return False
