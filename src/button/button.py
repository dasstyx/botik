from abc import ABC, abstractmethod

from telebot import types
from vkbottle import Text

from src.button.button_function import ButtonFunction


class Button(ABC):
    # TODO: button_function is a bad name! Change it later!
    def __init__(self, text, callback, inline=False, button_function: ButtonFunction = ButtonFunction.default,
                 native_args=None):
        if native_args is not None:
            self.native_args = native_args
        else:
            self.native_args = {}

        self.inline = inline
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


class TgButton(Button):

    def _create_native(self):
        text = self.get_text()
        req_phone = self.button_function == ButtonFunction.request_phone
        req_location = self.button_function == ButtonFunction.request_location

        if self.inline:
            self.native_data = types.InlineKeyboardButton(text, callback_data=self.get_text(),
                                                             request_contact=req_phone, request_location=req_location,
                                                             **self.native_args)
        else:
            self.native_data = types.KeyboardButton(text, request_contact=req_phone, request_location=req_location,
                                                       **self.native_args)


class VkButton(Button):
    def _create_native(self):
        # TODO: Add a geo button type if possible
        text = self.get_text()
        data = {"action": Text(text)}
        data.update(self.native_args)
        self.native_data = data

