from abc import ABC, abstractmethod
from typing import Sequence

from src.button.button_data import ButtonData
from src.button.button_factory import ButtonFactory


class KeyboardMarkup(ABC):

    def __init__(self, button_factory: ButtonFactory, inline, one_time, native_args):
        self.native_args = native_args
        self.inline = inline
        self.one_time = one_time
        self.button_factory = button_factory
        self.hash_to_buttons = {}
        self._markup = None
        self.rows = []

    @abstractmethod
    def _make(self):
        pass

    def get_native_markup(self):
        return self._make()

    def add_row(self, buttons: Sequence[ButtonData]):
        buttons_data = [self._create_native_button(button).native_data for button in buttons]
        self.rows.append(buttons_data)

    def _create_native_button(self, button: ButtonData):
        button = self.button_factory.create(button)

        button_hash = button.get_text()
        self.hash_to_buttons[button_hash] = button

        return button

    def get_pressed_button(self, button_hash):
        if button_hash in self.hash_to_buttons:
            return self.hash_to_buttons[button_hash]
        else:
            return None
