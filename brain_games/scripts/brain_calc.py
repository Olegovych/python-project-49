#!/usr/bin/env python3
from brain_games.functionz import check_answer
from brain_games.games.game_calc import task, calc


def main():
    check_answer(task, calc)


if __name__ == '__main__':
    main()
