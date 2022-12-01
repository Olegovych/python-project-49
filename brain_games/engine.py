import prompt
from os import system


def run_game(task, function):
    user_name = welcome_user()
    print(task)
    for _ in range(3):
        question, correct_answer = function()
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
        print(f'Congratulations, {user_name}!')


def welcome_user():
    system('clear')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
