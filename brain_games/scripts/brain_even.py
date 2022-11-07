#!/usr/bin/env python3
from random import randint
from brain_games.functionz \
    import welcome, welcome_user, congratulation, check, even


def main():
    welcome()
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        question = randint(0, 100)
        correct_answer = even(question)
        if not check(question, correct_answer, user_name):
            break
    else:
        congratulation(user_name)


if __name__ == '__main__':
    main()
