from vkbottle import KeyboardButtonColor

from src.core.api.api_type import ApiType
from src.core.input.keyboard.button.button_data import ButtonData, ButtonCallback
from src.core.page.page import Page
from src.tg.api.api_type import TgApiType
from src.vk.api.api_type import VkApiType


class NativeArgsPage(Page):
    def _create_keyboard_markup(self):
        if self.api.api_type == TgApiType:
            self.markup = self._markup_factory.create(inline=self._data.inline, one_time=self._data.one_time,
                                                      input_field_placeholder="Placeholder text")
        else:
            self.markup = self._markup_factory.create(inline=self._data.inline, one_time=self._data.one_time)

    async def make_page_content(self, user):
        if self.api.api_type == VkApiType:
            positive_button = ButtonData("Positive", ButtonCallback(self.send, message=f"Positive"),
                                         color=KeyboardButtonColor.POSITIVE)
            primary_button = ButtonData("Primary", ButtonCallback(self.send, message=f"Primary"),
                                        color=KeyboardButtonColor.PRIMARY)
        else:
            positive_button = ButtonData("Positive", ButtonCallback(self.send, message=f"Positive"))
            primary_button = ButtonData("Primary", ButtonCallback(self.send, message=f"Primary"))

        back_button = self.templates.button.Back
        self.markup.add_row([positive_button, primary_button])
        self.markup.add_row([back_button])
        await self.send(user, 'This is native args page...', markup=True)
