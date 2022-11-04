from abc import ABC

from src.core.input.keyboard.button.button_data import ButtonData


class ButtonFactory(ABC):
    button_type = None

    def __init__(self, inline):
        self.inline = inline

    def create(self, button_data: ButtonData):
        button = self.button_type(button_data.text, button_data.callback,
                                  button_data.button_function, inline=self.inline, **button_data.native_args)
        return button


