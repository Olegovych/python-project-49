#!/usr/bin/env python3
from brain_games.functionz import check_answer, calc


def main():
    task = 'What is the result of the expression?'
    check_answer(task, calc)


if __name__ == '__main__':
    main()
