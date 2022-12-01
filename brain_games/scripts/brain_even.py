#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.game_even import task, even


def main():
    run_game(task, even)


if __name__ == '__main__':
    main()
