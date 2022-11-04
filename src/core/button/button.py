from abc import ABC, abstractmethod

from telebot import types
from vkbottle import Text

from src.core.button.button_function import ButtonFunction


class Button(ABC):
    # TODO: button_function is a bad name! Change it later!
    def __init__(self, text, callback, button_function: ButtonFunction = ButtonFunction.default,
                 **native_args):
        self.native_args = native_args
        self.inline = self.native_args.pop('inline', None)
        self.button_function = button_function
        self.callback = callback
        self.text = text
        self.native_data = None
        self._create_native()

    @abstractmethod
    def _create_native(self):
        pass

    async def press(self, user):
        if self.callback:
            await self.callback.invoke(user=user)

    def get_text(self):
        return self.text
