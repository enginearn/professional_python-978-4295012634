#!/usr/bin/env python3

import datetime
import locale

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")


class Greeter(object):
    def __init__(self, staff_name: str) -> None:
        self.staff_name = staff_name

    def greet(self, store: str) -> None:
        print(f"{store}へようこそ！ 私、{self.staff_name}と申します。")
        print(f"{day()}の{part_of_day()}、いかがお過ごしですか？")
        print("本日のお客様に20% OFFのクーポンを差し上げます！")


def day() -> str:
    return datetime.datetime.now().strftime("%A")


def part_of_day() -> str:
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        part_of_day = "AM"
    elif current_hour < 17:
        part_of_day = "PM"
    else:
        part_of_day = "night"

    return part_of_day


greeter = Greeter("John")
greeter.greet("Shop A")
