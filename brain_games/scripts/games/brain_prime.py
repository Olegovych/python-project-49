#!/usr/bin/env python3
from brain_games.functionz import welcome_user, check_answer


def main():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    func_index = 4
    check_answer(user_name, func_index)


if __name__ == '__main__':
    main()
