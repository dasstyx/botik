from src.core.keyboard.markup_factory import KeyboardMarkupFactory
from src.vk.keyboard.vk_keyboard_markup import VkKeyboardMarkup


class VkKeyboardMarkupFactory(KeyboardMarkupFactory):
    def create(self, **native_args):
        return VkKeyboardMarkup(self.button_factory, native_args)
