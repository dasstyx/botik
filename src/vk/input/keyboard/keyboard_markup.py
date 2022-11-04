from vkbottle import Keyboard

from src.core.input.keyboard.button.button_factory import ButtonFactory
from src.core.input.keyboard.keyboard_markup import KeyboardMarkup


class VkKeyboardMarkup(KeyboardMarkup):
    def __init__(self, button_factory: ButtonFactory, native_args):
        super().__init__(button_factory, native_args)

        # VK doesn't support inline one_time keyboards
        if self.inline:
            self.one_time = False

    def get_native_markup(self):
        return self._make().get_json()

    def _make(self):
        self._markup = Keyboard(one_time=self.one_time, inline=self.inline)

        for i, row in enumerate(self.rows):
            for data in row:
                self._markup.add(**data)
            if i != len(self.rows) - 1:
                self._markup.row()
        return self._markup
