#!/usr/bin/env python3

import random

OPTIONS = ["Rock", "Paper", "Scissors"]


class RockPaperScissors(object):
    def __init__(self) -> None:
        self.computer_choice = None
        self.human_choice = None

    def get_computer_choice(self) -> None:
        self.computer_choice = random.choice(OPTIONS)

    def get_human_choice(self) -> None:
        choice_number = int(input("Enter a number: "))
        self.human_choice = OPTIONS[choice_number - 1]

    def print_options(self) -> None:
        print(
            "\n".join(f"({i}) {option.title()}" for i, option in enumerate(OPTIONS, 1))
        )

    def print_choices(self) -> None:
        print(f"Your chosen: {self.human_choice}")
        print(f"Computer chosen: {self.computer_choice}")

    def print_win_lose(self, human_beats: str, human_loses_to: str,) -> None:
        if self.computer_choice == human_loses_to:
            print(f"Boo! {self.computer_choice} wins!")
        elif self.computer_choice == human_beats:
            print(f"Congrats! {self.human_choice} wins!")

    def print_result(self) -> None:
        if self.human_choice == self.computer_choice:
            print("DRAW")

        if self.human_choice == "Rock":
            self.print_win_lose("Scissors", "Paper")
        elif self.human_choice == "Paper":
            self.print_win_lose("Rock", "Paper")
        elif self.human_choice == "Scissors":
            self.print_win_lose("Paper", "Rock")

    def simulate(self) -> None:
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_result()


start = RockPaperScissors()
start.simulate()
