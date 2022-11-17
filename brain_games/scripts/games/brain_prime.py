#!/usr/bin/env python3
from brain_games.functionz import check_answer, prime


def main():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    check_answer(task, prime)


if __name__ == '__main__':
    main()
