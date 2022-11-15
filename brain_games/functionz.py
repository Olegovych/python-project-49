import prompt
from random import randint, choice
from os import system
PRIME_LIST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


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


def gcd():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = f'{first_num} {second_num}'
    smaller, bigger = sorted((first_num, second_num))
    if bigger % smaller == 0:
        return question, str(smaller)
    for div in range(smaller // 2, 0, -1):
        if bigger % div == 0 and smaller % div == 0:
            return question, str(div)


def calc():
    first_num = randint(0, 100)
    operator = choice('+-*')
    second_num = randint(0, 10)
    question = f'{first_num} {operator} {second_num}'
    correct_answer = str(eval(question))
    return question, correct_answer


def progression():
    pr_start = randint(1, 20)
    pr_step = randint(1, 10)
    pr_len = randint(5, 10)
    pr_list = list(str(_) for _ in range
                   (pr_start, pr_start + pr_len * pr_step, pr_step))
    question_index = randint(0, pr_len - 1)
    correct_answer = pr_list[question_index]
    pr_list[question_index] = '..'
    question = ' '.join(pr_list)
    return question, correct_answer


def prime():
    question = randint(0, 100)
    if question in PRIME_LIST:
        return question, 'yes'
    else:
        return question, 'no'


def check_answer(user_name, func_index):
    functions = (even, calc, gcd, progression, prime)
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
