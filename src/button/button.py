from abc import ABC, abstractmethod
from typing import Tuple

from telebot import types

from src.button.button_function import ButtonFunction


class Button(ABC):
    def __init__(self, key, callback, inline=False, button_function: ButtonFunction = ButtonFunction.default):
        # self.text_provider = text_provider
        self.inline = inline
        self.button_function = button_function
        self.callback = callback
        self.key = key
        self.native_button = None
        self._create()

    @abstractmethod
    def _create(self):
        pass

    def get_native_button(self):
        return self.native_button

    def get_hash(self):
        return hash(self)

    def pressed(self, user):
        if self.callback:
            self.callback(user)

    def _get_text(self):
        return self.key
        # return self.text_provider.get_text(self.key)


class TgButton(Button):
    def get_hash(self):
        if self.inline:
            return f"Inline:{self._get_text()}"
        else:
            return self._get_text()

    def _create(self):
        text = self._get_text()
        req_phone = self.button_function == ButtonFunction.request_phone
        req_location = self.button_function == ButtonFunction.request_location

        if self.inline:
            self.native_button = types.InlineKeyboardButton(text, callback_data=self.get_hash(),
                                                            request_contact=req_phone, request_location=req_location)
        else:
            self.native_button = types.KeyboardButton(text, request_contact=req_phone, request_location=req_location)


class VkButton(Button):
    def __init__(self, key, callback, text_provider):
        super().__init__(key, callback, text_provider)
        self.outputs = None

    def _create(self):
        text = self._get_text()
        self.outputs = (text,)

    def get_data(self) -> Tuple[str]:
        return self.outputs
