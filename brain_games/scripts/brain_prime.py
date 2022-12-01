#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.game_prime import task, prime


def main():
    run_game(task, prime)


if __name__ == '__main__':
    main()
