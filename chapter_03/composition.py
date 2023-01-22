#!/usr/bin/env python3


class SpeakMixin(object):
    def speak(self) -> None:
        name = self.__class__.__name__.lower()
        print(f'1匹の{name}が、「こんにちは！」と言った。')


class RollOverMixin(object):
    def roll_over(self) -> None:
        print('回転した！')


class Dog(SpeakMixin, RollOverMixin):
    pass

dog = Dog()
dog.speak()
dog.roll_over()
