import prompt


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congratulation(name):
    print(f'Congratulations, {name}!')


def even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


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
