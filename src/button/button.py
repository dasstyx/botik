from abc import ABC, abstractmethod
from typing import Tuple
from vkbottle import Text

from telebot import types

from src.button.button_function import ButtonFunction


class Button(ABC):
    # TODO: button_function is a bad name! Change it later!
    def __init__(self, key, callback, inline=False, button_function: ButtonFunction = ButtonFunction.default):
        # self.text_provider = text_provider
        self.inline = inline
        self.button_function = button_function
        self.callback = callback
        self.key = key
        self._native_button = None
        self._create_native()

    @abstractmethod
    def _create_native(self):
        pass

    def get_native_button(self):
        return self._native_button

    def get_hash(self):
        return self._get_text()

    async def press(self, user):
        if self.callback:
            await self.callback.invoke(user=user)

    def _get_text(self):
        return self.key
        # return self.text_provider.get_text(self.key)


class TgButton(Button):

    def _create_native(self):
        text = self._get_text()
        req_phone = self.button_function == ButtonFunction.request_phone
        req_location = self.button_function == ButtonFunction.request_location

        if self.inline:
            self.native_button = types.InlineKeyboardButton(text, callback_data=self.get_hash(),
                                                            request_contact=req_phone, request_location=req_location)
        else:
            self.native_button = types.KeyboardButton(text, request_contact=req_phone, request_location=req_location)


class VkButton(Button):
    def _create_native(self):
        pass

    def get_data_for_keyboard(self):
        # TODO: Add a geo button type if possible
        text = self._get_text()
        return (Text(text),)