from abc import ABC, abstractmethod

from src.button.button import TgButton, VkButton
from src.button.button_data import ButtonData
from src.button.button_function import ButtonFunction


class ButtonFactory(ABC):
    button_type = None

    def __init__(self, inline):
        self.inline = inline

    def create(self, button_data: ButtonData):
        button = self.button_type(button_data.text, button_data.callback,
                                  self.inline, button_data.button_function)
        return button


class TgButtonFactory(ButtonFactory):
    button_type = TgButton


class VkButtonFactory(ButtonFactory):
    button_type = VkButton
