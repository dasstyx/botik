from abc import ABC, abstractmethod

from src.button.button import TgInlineButton, TgReplyButton, VkButton
from src.button.button_data import ButtonData
from src.button.button_function import ButtonFunction


class ButtonFactory(ABC):
    def __init__(self, inline):
        self.inline = inline
        self._make_button_type_dict()

    def create(self, button_data: ButtonData):
        button_type = self.button_type_dict[button_data.button_function]

        button = button_type(button_data.text, button_data.callback)
        return button

    @abstractmethod
    def _make_button_type_dict(self):
        pass


class TgButtonFactory(ButtonFactory):
    # TODO: Implement the ButtonFunction-based button construction
    def _make_button_type_dict(self):
        default = TgInlineButton if self.inline else TgReplyButton
        self.button_type_dict = {
            ButtonFunction.default: default
        }


class VkButtonFactory(ButtonFactory):
    def _make_button_type_dict(self):
        self.button_type_dict = {
            ButtonFunction.default: VkButton
        }
