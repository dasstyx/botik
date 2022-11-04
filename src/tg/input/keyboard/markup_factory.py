from src.core.input.keyboard.markup_factory import KeyboardMarkupFactory
from src.tg.input.keyboard.keyboard_markup import TgKeyboardMarkup


class TgKeyboardMarkupFactory(KeyboardMarkupFactory):
    def create(self, **native_args):
        return TgKeyboardMarkup(self.button_factory, native_args)
