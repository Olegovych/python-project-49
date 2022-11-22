#!/usr/bin/env python3
from brain_games.functionz import check_answer, gcd


def main():
    task = 'Find the greatest common divisor of given numbers.'
    check_answer(task, gcd)


if __name__ == '__main__':
    main()
