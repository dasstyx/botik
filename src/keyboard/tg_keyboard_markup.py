from telebot import types

from src.keyboard.keyboard_markup import KeyboardMarkup


class TgKeyboardMarkup(KeyboardMarkup):
    def _make(self, inline, one_time):
        if inline:
            self._markup = types.InlineKeyboardMarkup()
        else:
            self._markup = types.ReplyKeyboardMarkup(one_time_keyboard=one_time)

    def add_row(self, buttons):
        native_buttons = [self._create_native_button(button).get_native_button() for button in buttons]
        self._markup.row(*native_buttons)
