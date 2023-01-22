#!/usr/bin/env python3

NAMES = ['John', 'Mike', 'Bob']

def print_greeting() -> None:
    greeting_pattern = '{name}さんに、ごあいさつ。'
    nice_person_pattern = '{name}さんはとても良い人です。'
    for name in NAMES:
        print(greeting_pattern.format(name=name))
        print(nice_person_pattern.format(name=name))

print_greeting()
