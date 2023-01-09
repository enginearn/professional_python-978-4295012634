#!/usr/bin/env python3

import random

OPTIONS = ['Rock', 'Paper', 'Scissors']

def get_computer_choice() -> str:
    return random.choice(OPTIONS)

def get_human_choice() -> str:
    choice_number = int(input('番号を入力: '))
    return OPTIONS[choice_number - 1]

def print_options() -> None:
    print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS, 1)))

def print_choices(human_choice: str, computer_choice: str) -> None:
    print(f'Your chosen: {human_choice}')
    print(f'Computer chosen: {computer_choice}')

def print_win_lose(human_choice: str, computer_choice: str, human_beats: str, human_loses_to: str) -> None:
    if computer_choice == human_loses_to:
        print(f'{computer_choice} wins!')
    elif computer_choice == human_beats:
        print(f'Congrats! {human_choice} wins!')

def print_result(human_choice: str, computer_choice: str) -> None:
    if human_choice == computer_choice:
        print('It\'s draw.')

    if human_choice == 'Rock':
        print_win_lose('Rock', computer_choice, 'Scissors', 'Paper')
    elif human_choice == 'Paper':
        print_win_lose('Paper', computer_choice, 'Rock', 'Scissors')
    elif human_choice == 'Scissors':
        print_win_lose('Scissors', computer_choice, 'Paper', 'Rock')

print_options()
human_choice = get_human_choice()
computer_choice = get_computer_choice()
print_choices(human_choice, computer_choice)
print_result(human_choice, computer_choice)
