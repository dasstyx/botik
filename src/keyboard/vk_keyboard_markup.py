from typing import Sequence

from vkbottle import Keyboard, Text
from src.button.button import VkButton
from src.keyboard.keyboard_markup import KeyboardMarkup


class VkKeyboardMarkup(KeyboardMarkup):

    def get_native_markup(self):
        return self._markup.get_json()

    def _make(self, inline, one_time):
        self._markup = Keyboard(one_time=one_time, inline=inline)

    def add_row(self, buttons: Sequence[VkButton]):
        buttons_data = [self._create_native_button(button).get_data_for_keyboard() for button in buttons]
        for data in buttons_data:
            self._markup.add(*data)

        self._markup.row()
