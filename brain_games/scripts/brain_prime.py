#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.prime import TASK, prime


def main():
    run_game(TASK, prime)


if __name__ == '__main__':
    main()
