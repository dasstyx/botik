from src.core.keyboard.markup_factory import KeyboardMarkupFactory
from src.tg.keyboard.tg_keyboard_markup import TgKeyboardMarkup


class TgKeyboardMarkupFactory(KeyboardMarkupFactory):
    def create(self, **native_args):
        return TgKeyboardMarkup(self.button_factory, native_args)
