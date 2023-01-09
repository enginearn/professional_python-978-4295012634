#!/usr/bin/env python3

import random

options = ['Rock', 'Paper', 'Scissors']
print('1: Rock\n2: Paper\n3: Scissors')

human_choice = options[int(input('番号を入力: ')) - 1]
print(f'Your chosen: {human_choice}')
computer_choice = random.choice(options)
print(f'Computer chosen: {computer_choice}')

if human_choice == 'Rock':
    if computer_choice == 'Paper':
        print('Paper wins!')
    elif computer_choice == 'Scissors':
        print('Congrats! Rock wins!')
    else:
        print('It\'s draw.')

elif human_choice == 'Paper':
    if computer_choice == 'Scissors':
        print('Scissors wins!')
    elif computer_choice == 'Rock':
        print('Congrats! Paper wins!')
    else:
        print('It\'s draw.')

elif human_choice == 'Scissors':
    if computer_choice == 'Rock':
        print('Rock wins!')
    elif computer_choice == 'Paper':
        print('Congrats! Scissors wins!')
    else:
        print('It\'s draw.')
