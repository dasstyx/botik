from telebot import types

from src.keyboard.keyboard_markup import KeyboardMarkup


class TgKeyboardMarkup(KeyboardMarkup):
    def get_native_markup(self):
        return self._make()

    def _make(self):
        if self.inline:
            self._markup = types.InlineKeyboardMarkup(**self.native_args)
        else:
            self._markup = types.ReplyKeyboardMarkup(one_time_keyboard=self.one_time, **self.native_args)

        for i, row in enumerate(self.rows):
            for data in row:
                self._markup.row(data)
        return self._markup

    def add_row(self, buttons):
        buttons_data = [self._create_native_button(button).get_native_button() for button in buttons]
        self.rows.append(buttons_data)
