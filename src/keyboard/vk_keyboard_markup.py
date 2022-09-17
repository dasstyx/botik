from typing import Sequence

from vk_api.keyboard import VkKeyboard

from src.button.button import VkButton
from src.keyboard.keyboard_markup import KeyboardMarkup


class VkKeyboardMarkup(KeyboardMarkup):
    def __init__(self, button_factory, inline, one_time):
        super().__init__(button_factory, inline, one_time)
        self.is_empty = True

    def _make(self, inline, one_time):
        self._markup = VkKeyboard(one_time=one_time, inline=inline)

    def add_row(self, buttons: Sequence[VkButton]):
        if self.is_empty:
            self._markup.add_line()
        else:
            self.is_empty = False

        for button in buttons:
            text = button.get_data()
            self._markup.add_button(text)
