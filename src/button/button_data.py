from abc import ABC

from src.button.button_function import ButtonFunction


class ButtonData:
    default_function = ButtonFunction.default

    def __init__(self, text, callback, button_function: ButtonFunction = default_function):
        self.button_function = button_function
        self.callback = callback
        self.text = text
