#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.game_gcd import task, gcd


def main():
    run_game(task, gcd)


if __name__ == '__main__':
    main()
