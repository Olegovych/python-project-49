#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.game_gcd import TASK, gcd


def main():
    run_game(TASK, gcd)


if __name__ == '__main__':
    main()
