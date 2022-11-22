#!/usr/bin/env python3
from brain_games.functionz import check_answer, even


def main():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    check_answer(task, even)


if __name__ == '__main__':
    main()
