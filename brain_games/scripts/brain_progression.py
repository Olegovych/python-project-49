#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.game_progression import TASK, progression


def main():
    run_game(TASK, progression)


if __name__ == '__main__':
    main()
