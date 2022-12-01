#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.game_progression import task, progression


def main():
    run_game(task, progression)


if __name__ == '__main__':
    main()
