#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.even import TASK, even


def main():
    run_game(TASK, even)


if __name__ == '__main__':
    main()
