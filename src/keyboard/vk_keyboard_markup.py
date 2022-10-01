from typing import Sequence

from vkbottle import Keyboard, Text
from src.button.button import VkButton
from src.button.button_factory import ButtonFactory
from src.keyboard.keyboard_markup import KeyboardMarkup


class VkKeyboardMarkup(KeyboardMarkup):

    def __init__(self, button_factory: ButtonFactory, inline, one_time):
        super().__init__(button_factory, inline, one_time)
        self.rows = []

    def get_native_markup(self):
        self._markup = Keyboard(one_time=self.one_time, inline=self.inline)

        for i, row in enumerate(self.rows):
            for data in row:
                self._markup.add(*data)
            if i != len(self.rows) - 1:
                self._markup.row()

        return self._markup.get_json()

    def _make(self, inline, one_time):
        if self.inline:
            self.one_time = False

    def add_row(self, buttons: Sequence[VkButton]):
        buttons_data = [self._create_native_button(button).get_data_for_keyboard() for button in buttons]
        self.rows.append(buttons_data)
