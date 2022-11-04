from telebot import types

from src.core.input.keyboard.keyboard_markup import KeyboardMarkup


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
