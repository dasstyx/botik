from abc import ABC, abstractmethod

from src.keyboard.tg_keyboard_markup import TgKeyboardMarkup
from src.keyboard.vk_keyboard_markup import VkKeyboardMarkup


class KeyboardMarkupFactory(ABC):
    def __init__(self, button_factory):
        self.button_factory = button_factory

    @abstractmethod
    def create(self, inline, one_time):
        pass


class TgKeyboardMarkupFactory(KeyboardMarkupFactory):
    def create(self, inline, one_time):
        return TgKeyboardMarkup(self.button_factory, inline, one_time)


class VkKeyboardMarkupFactory(KeyboardMarkupFactory):
    def create(self, inline, one_time):
        return VkKeyboardMarkup(self.button_factory, inline, one_time)
