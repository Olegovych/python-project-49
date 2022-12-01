#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.game_calc import task, calc


def main():
    run_game(task, calc)


if __name__ == '__main__':
    main()
