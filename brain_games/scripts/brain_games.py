#!/usr/bin/env python3
import brain_games.cli


def welcome():
    print('Welcome to the Brain Games!')


def main():
    welcome()
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
