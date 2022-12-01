#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.calc import TASK, calc


def main():
    run_game(TASK, calc)


if __name__ == '__main__':
    main()
