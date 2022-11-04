from telebot import types

from src.core.button.button import Button
from src.core.button.button_function import ButtonFunction


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
