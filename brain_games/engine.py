import prompt
from os import system

QUESTIONS_COUNT = 3


def run_game(game):
    user_name = welcome_user()
    print(game.TASK)
    for _ in range(QUESTIONS_COUNT):
        question, correct_answer = game.get_question_and_answer()
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
