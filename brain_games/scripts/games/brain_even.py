#!/usr/bin/env python3
from brain_games.functionz import welcome_user, check_answer


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    func_index = 0
    check_answer(user_name, func_index)


if __name__ == '__main__':
    main()
